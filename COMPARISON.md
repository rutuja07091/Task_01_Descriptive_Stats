# COMPARISON: Pure Python vs Pandas

This task requires two independent analyses of the same dataset:
- `pure_python_stats.py` using only Python’s standard library
- `pandas_stats.py` using Pandas

The goal is to confirm both approaches produce consistent descriptive truths while understanding how different tools handle type inference, 
missing values, and summarization.  [oai_citation:3‡Research_Task_01 (3).docx](sediment://file_000000000d9c722fb16e30f17069cbab)

## What matched
- Dataset shape matched across both approaches: 246,745 rows and 40 columns
- Missingness results matched closely across both approaches, including the highest-missing fields:
  - `ad_delivery_stop_time`: 2,159 missing (0.875%)
  - `bylines`: 1,009 missing (0.409%)
  - `estimated_audience_size`: 579 missing (0.235%)
- High-frequency categorical results aligned for key identity fields. For example, 
The top page_name values and counts matched:
  - Kamala Harris: 55,503
  - Donald J. Trump: 23,988
  - Joe Biden: 14,822
  - The Daily Scroll: 10,461
  - Kamala HQ: 7,564

Agreement across independent scripts increases confidence that the dataset was parsed correctly and that missing-value rules and frequency calculations are consistent.

## What differed
- Datetime handling differed in implementation. Pandas represents date fields as datetime64[ns] via `to_datetime`, 
while pure Python required explicit parsing logic and custom datetime summaries (min/max dates plus top frequency dates)

- Pandas immediately produced numeric summaries for the 26 `illuminating_*` columns inferred as int64. 
Because many of these behave like 0/1 flags, the mean is interpretable as the share of ads with that label. 

In pure Python, numeric summaries also required explicit parsing and were dependent on the type-inference heuristic
- Several conceptually numeric fields (`spend`, `impressions`, `estimated_audience_size`) 
remained non-numeric in both approaches because they are stored as string-encoded lower/upper bound dictionaries. 
Without extra parsing, these behave as categorical buckets rather than true numeric columns

## Why it differed
- Pandas performs automatic dtype inference and uses NaN for missing values, which shapes how summaries are computed and displayed by default. 
Pure Python depends on explicit cleaning rules and parsing decisions

- Datetime conversion is built-in and concise in Pandas, but must be implemented manually in pure Python,
including decisions about formats and error handling
- Range-encoded columns require additional preprocessing in both approaches to become truly numeric (for example, extracting bounds and computing midpoints)

## Reflection
- The pure Python implementation forced explicit decisions about parsing, type inference, and edge cases (missing values, non-numeric strings, empty columns), 
which strengthened the understanding of how descriptive statistics work

- The Pandas implementation was significantly faster for exploration and produced standard summaries with minimal code, 
making it easier to extend the project into plotting and deeper analysis

- Comparing outputs across both methods provided validation that the descriptive results are trustworthy
