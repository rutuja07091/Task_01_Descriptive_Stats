# Task 01 – Descriptive Statistics (Pure Python vs Pandas)

## Project overview
This project explores a real-world political advertising dataset of Facebook ad purchases tied to the 2024 U.S. presidential election. The goal is to compute descriptive statistics in two independent ways:
1) `pure_python_stats.py` using only the Python standard library
2) `pandas_stats.py` using Pandas

The purpose is to verify that both approaches arrive at the same statistical truths while documenting tradeoffs in correctness, transparency, and development speed.  [oai_citation:1‡Research_Task_01 (1).docx](sediment://file_000000005b2871f5a29327a553f4a717)

## Dataset (not included in this repo)
Per assignment requirements, the dataset is NOT committed to GitHub.  [oai_citation:2‡Research_Task_01 (1).docx](sediment://file_000000005b2871f5a29327a553f4a717)

Expected file:
- `fb_ads_president_scored_anon.csv`

Place the dataset locally in:
- `data/fb_ads_president_scored_anon.csv`

Source: Google Drive – 2024 Facebook Political Ads (provided via SU OPT Research task materials).  [oai_citation:3‡Research_Task_01 (1).docx](sediment://file_000000005b2871f5a29327a553f4a717)

## Repo structure
- `pure_python_stats.py`  Standard library descriptive stats (with type inference)
- `pandas_stats.py`       Pandas descriptive stats + saved outputs
- `FINDINGS.md`           1–2 page narrative summary of what the data shows
- `COMPARISON.md`         Reflection on differences between the two approaches
- `requirements.txt`      Dependencies for Pandas script
- `.gitignore`            Prevents dataset/temp files from being committed
- `outputs/`              Saved results (optional to commit; can be ignored)

## How to run

### 1) Pure Python (no third-party libraries)
```bash
python pure_python_stats.py data/fb_ads_president_scored_anon.csv --out outputs/pure_python_summary.json
