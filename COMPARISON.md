# COMPARISON — Pure Python vs Pandas

This task requires producing the same descriptive truths in two independent ways and then explaining agreement, differences, and tradeoffs.  [oai_citation:3‡Research_Task_01.docx](sediment://file_000000000d9c722fb16e30f17069cbab)

## What matched (agreement checks)
Across both scripts:
- Dataset shape matched: 246,745 rows and 40 columns
- Missingness matched in both rank order and counts:
  - ad_delivery_stop_time: 2,159 missing
  - bylines: 1,009 missing
  - estimated_audience_size: 579 missing
- Top categorical values matched for key identity fields, including page_name:
  - Kamala Harris (55,503), Donald J. Trump (23,988), Joe Biden (14,822), The Daily Scroll (10,461), Kamala HQ (7,564)

These matches give confidence that both scripts load the same data correctly and compute consistent frequency-based summaries.

## What differed
### 1) Type inference is explicit in pure Python, automatic in Pandas
- Pure Python required a rule-based strategy to infer numeric vs categorical vs datetime values, including handling non-numeric strings and missing entries
- Pandas inferred types automatically and represented missing values as NaN, which affects downstream summaries

### 2) Datetime handling required different work
- In pure Python, datetime summaries required explicit parsing of YYYY-MM-DD and custom outputs (min_date/max_date/mode/top dates)
- In Pandas, datetime conversion was performed via to_datetime(errors='coerce'), making time-aware analysis straightforward

### 3) “Numeric-looking” columns stayed non-numeric because of how the data is encoded
- spend, impressions, and estimated_audience_size remained object dtype in Pandas because values are dict-like strings encoding ranges
- In pure Python, these columns also behave as categorical unless additional parsing is written
This is not a mismatch; it is a data-structure reality that both approaches must respect.

### 4) Output precision and formatting
- Pandas describe() outputs standardized tables and often rounds displayed values
- Pure Python outputs depend on how values are formatted and printed, even when underlying computations agree

## Why the differences happened
- Pandas makes silent decisions about dtype inference and missing values (NaN), while pure Python forces the analyst to define and implement those decisions
- Datetime conversion is a built-in operation in Pandas but must be implemented manually in pure Python
- The dataset encodes key fields as ranges rather than exact numbers, which prevents traditional numeric summaries unless additional preprocessing is added in either approach

## Reflection: what I learned by doing both
- Pure Python made edge cases obvious (missing values, parsing failures, columns that look numeric but are not), which improves confidence in later LLM-generated summaries
- Pandas made it fast to validate results, produce readable tables, and extend toward deeper analysis and visualization
- Agreement between two independent implementations is a strong correctness check, especially for messy real-world datasets
