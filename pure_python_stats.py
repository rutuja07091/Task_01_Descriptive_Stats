# pure_python_stats.py

import csv
import math
import json
import argparse
from collections import Counter
from datetime import datetime
from typing import Any, Dict, List, Optional

MISSING_STRINGS = {"", "na", "n/a", "null", "none", "nan", "NA", "N/A", "NULL", "None", "NaN"}

def clean_cell(x: Any) -> Optional[str]:
    if x is None:
        return None
    s = str(x).strip()
    if s in MISSING_STRINGS or s.lower() in MISSING_STRINGS:
        return None
    return s

def parse_number(s: str) -> Optional[float]:
    t = s.strip().replace(",", "").replace("$", "")
    if t.endswith("%"):
        t = t[:-1]
    try:
        return float(t)
    except:
        return None

def parse_date_ymd(s: str) -> Optional[datetime]:
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d")
    except:
        return None

def mean(values: List[float]) -> float:
    return sum(values) / len(values)

def median(values: List[float]) -> float:
    v = sorted(values)
    n = len(v)
    mid = n // 2
    return v[mid] if n % 2 == 1 else (v[mid - 1] + v[mid]) / 2

def stddev(values: List[float]) -> float:
    n = len(values)
    if n < 2:
        return 0.0
    m = mean(values)
    var = sum((x - m) ** 2 for x in values) / (n - 1)
    return math.sqrt(var)

def numeric_stats(nums: List[float]) -> Dict[str, float]:
    return {
        "count": len(nums),
        "mean": mean(nums),
        "min": min(nums),
        "max": max(nums),
        "stddev": stddev(nums),
        "median": median(nums),
    }

def categorical_stats(vals: List[str]) -> Dict[str, Any]:
    c = Counter(vals)
    top_5 = c.most_common(5)
    mode_val, mode_freq = (top_5[0][0], top_5[0][1]) if top_5 else (None, 0)
    return {
        "count": len(vals),
        "unique": len(c),
        "mode": mode_val,
        "mode_freq": mode_freq,
        "top_5": top_5,
    }

def datetime_stats(dts: List[datetime], raw_vals: List[str]) -> Dict[str, Any]:
    c = Counter(raw_vals)
    top_5 = c.most_common(5)
    mode_val, mode_freq = (top_5[0][0], top_5[0][1]) if top_5 else (None, 0)
    return {
        "count": len(dts),
        "min_date": min(dts).strftime("%Y-%m-%d"),
        "max_date": max(dts).strftime("%Y-%m-%d"),
        "mode": mode_val,
        "mode_freq": mode_freq,
        "top_5": top_5,
    }

def infer_type(vals: List[str]) -> str:
    """
    Heuristic:
      - if >=80% parse as numeric -> numeric
      - else if >=80% parse as YYYY-MM-DD -> datetime
      - else categorical
    """
    if not vals:
        return "empty"

    num_ok = sum(1 for v in vals if parse_number(v) is not None)
    if num_ok / len(vals) >= 0.80:
        return "numeric"

    dt_ok = sum(1 for v in vals if parse_date_ymd(v) is not None)
    if dt_ok / len(vals) >= 0.80:
        return "datetime"

    return "categorical"

def summarize_csv(csv_path: str) -> Dict[str, Any]:
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []

        store: Dict[str, List[str]] = {c: [] for c in cols}
        missing: Dict[str, int] = {c: 0 for c in cols}
        row_count = 0

        for row in reader:
            row_count += 1
            for c in cols:
                v = clean_cell(row.get(c))
                if v is None:
                    missing[c] += 1
                else:
                    store[c].append(v)

    summary: Dict[str, Any] = {
        "rows": row_count,
        "columns": len(cols),
        "missing_by_column": missing,
        "column_summaries": {}
    }

    for c in cols:
        vals = store[c]
        ctype = infer_type(vals)

        if ctype == "numeric":
            nums = [parse_number(v) for v in vals]
            nums = [x for x in nums if x is not None]
            summary["column_summaries"][c] = {"type": "numeric", **numeric_stats(nums)} if nums else {"type": "numeric", "count": 0}

        elif ctype == "datetime":
            parsed = [(parse_date_ymd(v), v) for v in vals]
            parsed = [(dt, raw) for dt, raw in parsed if dt is not None]
            dts = [dt for dt, _ in parsed]
            raw_vals = [raw for _, raw in parsed]
            summary["column_summaries"][c] = {"type": "datetime", **datetime_stats(dts, raw_vals)} if dts else {"type": "datetime", "count": 0}

        elif ctype == "categorical":
            summary["column_summaries"][c] = {"type": "categorical", **categorical_stats(vals)}

        else:
            summary["column_summaries"][c] = {"type": "empty", "count": 0}

    return summary

def main():
    parser = argparse.ArgumentParser(description="Compute descriptive stats using Python standard library only.")
    parser.add_argument("csv_path", help="Path to the CSV file")
    parser.add_argument("--out", default=None, help="Optional output JSON path")
    args = parser.parse_args()

    result = summarize_csv(args.csv_path)

    print("Rows:", result["rows"])
    print("Columns:", result["columns"])

    print("\nTop 10 columns by missing values:")
    missing_sorted = sorted(result["missing_by_column"].items(), key=lambda x: x[1], reverse=True)[:10]
    for col, miss in missing_sorted:
        print(f"{col}: {miss}")

    print("\nSample column summaries (first 5 columns):")
    first_cols = list(result["column_summaries"].keys())[:5]
    for col in first_cols:
        print(col, "->", result["column_summaries"][col])

    if args.out:
        with open(args.out, "w", encoding="utf-8") as out:
            json.dump(result, out, indent=2)
        print("\nSaved JSON to:", args.out)

if __name__ == "__main__":
    main()
