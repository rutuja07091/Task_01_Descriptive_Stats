---

## FINDINGS.md

```md
# FINDINGS — Facebook Political Ads (2024 U.S. Presidential Election)

### 1) What this dataset captures
This dataset contains 246,745 Facebook ads (40 columns) connected to the 2024 U.S. presidential election, where ads mention one or more presidential candidates. Each row is an ad purchase and includes advertiser identity (page_id/page_name), ad identifiers, delivery timing (creation/start/stop dates), and multiple labeled “illuminating_*” fields that describe ad characteristics (message type/topic flags and other indicators).

A critical feature of this dataset is that key quantitative fields such as spend and impressions are not provided as exact numbers. They are recorded as lower/upper bound ranges represented as dict-like strings. This affects how “spending” can be summarized.

### 2) Basic structure and data quality
The dataset is large and mostly complete. Missingness is concentrated in three fields:
- ad_delivery_stop_time: 2,159 missing (0.875%)
- bylines: 1,009 missing (0.409%)
- estimated_audience_size: 579 missing (0.235%)

The missing stop time likely reflects ads that were still running at the time of capture or incomplete reporting. Missing bylines suggests sponsor/attribution metadata is not consistently present for every record.

### 3) Candidate mentions and advertiser concentration
Ad volume is strongly concentrated among a small set of advertiser pages. The highest-frequency advertiser page_name values are:
- Kamala Harris: 55,503 ads
- Donald J. Trump: 23,988 ads
- Joe Biden: 14,822 ads
- The Daily Scroll: 10,461 ads
- Kamala HQ: 7,564 ads

This indicates that a limited set of high-profile political pages account for a large portion of total ads in the dataset, rather than volume being evenly distributed across thousands of pages (4,546 unique page_name values).

### 4) Timing and late-cycle spikes
Date parsing shows the dataset spans multiple years:
- earliest observed date: 2021-07-06
- latest observed date: 2024-11-05

Within that overall range, ad creation and ad delivery starts cluster heavily in late October 2024:
- most frequent ad_creation_time: 2024-10-27 (8,619 ads)
- most frequent ad_delivery_start_time: 2024-10-28 (10,089 ads)

This suggests a clear late-cycle ramp-up in ad publishing and launches as the election approached.

### 5) “Who spent how much” is bucketed, not exact
The spend field is stored as range buckets (object dtype in Pandas). The most frequent spend bucket is the lowest:
- spend {'lower_bound': '0', 'upper_bound': '99'} appears 135,950 times

Similarly, impressions are also bucketed:
- impressions {'lower_bound': '0', 'upper_bound': '999'} appears 80,822 times

This means a large fraction of ads fall into the lowest reporting buckets for both spend and impressions. Without converting ranges into numeric estimates (e.g., midpoint of the interval), we cannot compute an exact mean/median spend per advertiser, but we can validly describe the distribution of ads across these spend/impression bins.

### 6) Content indicators show measurable prevalence rates
Many illuminating_* columns are binary indicator variables (int64). For binary indicators, the mean is interpretable as the share of ads with that label. For example:
- illuminating_msg_type_advocacy mean ≈ 0.549 (about 54.9% of ads flagged as advocacy)
- illuminating_msg_type_issue mean ≈ 0.382
- illuminating_msg_type_attack mean ≈ 0.272
- illuminating_scam mean ≈ 0.072
- illuminating_election_integrity_Truth mean ≈ 0.050

These rates show that the dataset contains a mix of message strategies, with advocacy and issue-oriented content appearing more frequently than attack content in this labeled view.

### 7) Summary takeaways
1) The dataset is large and mostly complete; missingness is limited to a few metadata fields
2) Ad volume is concentrated among major candidate pages, especially Kamala Harris and Donald J. Trump
3) There is a pronounced spike in ad creation and launch activity in late October 2024
4) Spend and impressions are reported in buckets, so spending analysis is best framed as distributions over ranges unless additional parsing is implemented
5) Binary indicator fields provide measurable prevalence rates that help describe ad strategy and content composition
