# Task_01_Descriptive_Stats 
Facebook Political Ads Dataset (2024 U.S. Presidential Election)

## 1. Project purpose
This repository completes **SU OPT Research Task 01**. The assignment requires building **two independent analysis scripts** that compute descriptive statistics on a real-world dataset of Facebook political ads tied to the 2024 U.S. presidential election:

1) `pure_python_stats.py`  
   Uses only Python’s **standard library** (csv, math, collections) to compute statistics “from scratch”

2) `pandas_stats.py`  
   Uses **Pandas** to compute the same descriptive truths and generate reviewable output files

The point of the task is not just generating summaries, but demonstrating:
- Correctness by validating results across two different implementations  
- Understanding by explicitly handling missing values, type inference, and edge cases  
- Reproducibility through clear run instructions and dependency documentation  

## 2. Dataset and compliance (important)
### Dataset is not included in this repo
Per the task rules, the dataset file must **not** be committed to GitHub.

Expected dataset filename:
- `fb_ads_president_scored_anon.csv`

Place the dataset locally at:
- `data/fb_ads_president_scored_anon.csv`

### Note about data encoding
Several conceptually numeric fields are stored as **range buckets encoded as dict-like strings**, not exact numeric values. Example:
- `{'lower_bound': '0', 'upper_bound': '99'}`

This applies to:
- `spend`
- `impressions`
- `estimated_audience_size`

Because these are ranges (intervals), they behave like **categorical buckets** unless additional parsing is implemented to convert them into numeric estimates (e.g., using midpoints).

## 3. Repository structure
- `pure_python_stats.py`  
  Standard-library-only descriptive statistics with missing-value handling and type inference (numeric, categorical, datetime)

- `pandas_stats.py`  
  Pandas descriptive statistics, including:
  - df.shape, df.dtypes, df.info()
  - missing count + missing %
  - describe() for numeric and object columns
  - value_counts() top 5 for categorical columns
  - output files saved to `outputs/`

- `FINDINGS.md`  
  1–2 page research-style narrative of what the data shows

- `COMPARISON.md`  
  Comparison of pure Python vs Pandas outputs:
  what matched, what differed, and why


## 4. How to run (from repo root)

### 4.1 Pure Python script
```bash
python pure_python_stats.py data/fb_ads_president_scored_anon.csv --out outputs/pure_python_summary.json
