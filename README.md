# Task 01 – Descriptive Statistics with and without Pandas

## Purpose
This repository completes SU OPT Research Task 01: compute descriptive statistics for a real-world political advertising dataset using two independent approaches:
1) A pure Python implementation using only the standard library (no Pandas, no NumPy)
2) A Pandas implementation that reproduces the same descriptive truths

The goal is not only to compute statistics, but also to compare how manual computation differs from library-driven analysis in terms of type inference, missing value handling, and reproducibility.  [oai_citation:1‡Research_Task_01 (3).docx](sediment://file_000000000d9c722fb16e30f17069cbab)

## Dataset
This dataset contains Facebook ads run during the 2024 U.S. presidential election period. Each row represents an ad purchase and includes:
- Advertiser/page identifiers (page_id, page_name)
- Ad identifiers (ad_id)
- Date fields (creation and delivery timing)
- Spend and impressions fields (reported as ranges)
- Multiple “illuminating_*” columns that act as binary indicator fields describing message types, topics, and other characteristics

### Dataset is NOT included in this repo
Per the task requirements, the dataset file must not be committed to GitHub.  [oai_citation:2‡Research_Task_01 (3).docx](sediment://file_000000000d9c722fb16e30f17069cbab)

Expected file name:
- `fb_ads_president_scored_anon.csv`

Place the dataset locally at:
- `data/fb_ads_president_scored_anon.csv`

## Repository contents
- `pure_python_stats.py`  
  Loads the CSV using the Python standard library and computes descriptive statistics with custom parsing, missing-value rules, and type inference (including datetime detection)

- `pandas_stats.py`  
  Loads the same CSV using Pandas and produces matching descriptive summaries, missing-value tables, and top categorical value frequencies

- `FINDINGS.md`  
  A 1–2 page narrative summary of key patterns in the data (written like the opening section of a research report)

- `COMPARISON.md`  
  A reflection describing what matched between the two scripts, what differed, and why

- `requirements.txt`  
  Dependencies needed for the Pandas script

- `.gitignore`  
  Prevents raw data and temp outputs from being committed

- `outputs/`  
  Optional folder where scripts write result files (JSON/CSV). Depending on workflow, this may be ignored by git.

## How to run

### 1) Pure Python (standard library only)
From the repo root, run:

```bash
python pure_python_stats.py data/fb_ads_president_scored_anon.csv --out outputs/pure_python_summary.json
