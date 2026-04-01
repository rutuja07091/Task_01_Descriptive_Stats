# pandas_stats.py

import os
import json
import io
import argparse
import pandas as pd

def safe_makedirs(path: str):
    if os.path.exists(path) and not os.path.isdir(path):
        raise ValueError(f"Output path exists but is not a directory: {path}")
    os.makedirs(path, exist_ok=True)

def main(csv_path: str, out_dir: str, parse_dates: bool = True):
    safe_makedirs(out_dir)

    df = pd.read_csv(csv_path)

    # Parse date columns (aligns with pure python datetime detection)
    if parse_dates:
        for col in ["ad_creation_time", "ad_delivery_start_time", "ad_delivery_stop_time"]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")

    # Shape + dtypes
    print("Shape:", df.shape)
    print("\nDtypes:\n", df.dtypes)

    # info() capture
    buf = io.StringIO()
    df.info(buf=buf)
    info_text = buf.getvalue()
    print("\nInfo:\n", info_text)
    with open(os.path.join(out_dir, "pandas_info.txt"), "w", encoding="utf-8") as f:
        f.write(info_text)

    # Missing count + missing %
    missing_count = df.isna().sum().sort_values(ascending=False)
    missing_pct = (missing_count / len(df) * 100).round(3)
    missing_table = pd.DataFrame({"missing_count": missing_count, "missing_pct": missing_pct})
    print("\nTop 15 missing columns:\n", missing_table.head(15))
    missing_table.to_csv(os.path.join(out_dir, "pandas_missing_table.csv"), index=True)

    # describe numeric + object
    num_desc = df.describe(include="number").T
    obj_desc = df.describe(include="object").T
    num_desc.to_csv(os.path.join(out_dir, "pandas_describe_numeric.csv"))
    obj_desc.to_csv(os.path.join(out_dir, "pandas_describe_object.csv"))
    print("\nNumeric describe (head 10):\n", num_desc.head(10))
    print("\nObject describe (head 10):\n", obj_desc.head(10))

    # Top 5 value counts for categorical (object) columns
    obj_cols = df.select_dtypes(include=["object"]).columns.tolist()
    top5 = {}
    for col in obj_cols:
        vc = df[col].value_counts(dropna=True).head(5)
        top5[col] = [(str(idx), int(val)) for idx, val in vc.items()]

    with open(os.path.join(out_dir, "pandas_top5_categoricals.json"), "w", encoding="utf-8") as f:
        json.dump(top5, f, indent=2)

    print("\nTop 5 value counts preview (first 8 object columns):")
    for col in obj_cols[:8]:
        print(f"\n{col}:")
        for v, c in top5[col]:
            print(f"  {v}: {c}")

    print("\nSaved outputs to:", out_dir)

def cli():
    parser = argparse.ArgumentParser(description="Pandas descriptive statistics for Task 01.")
    parser.add_argument("csv_path", help="Path to the CSV file")
    parser.add_argument("--out_dir", default="outputs", help="Directory to save output files")
    parser.add_argument("--no_parse_dates", action="store_true", help="Disable datetime parsing")
    args = parser.parse_args()
    main(args.csv_path, args.out_dir, parse_dates=not args.no_parse_dates)

if __name__ == "__main__":
    cli()
