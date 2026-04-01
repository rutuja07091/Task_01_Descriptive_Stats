---

## FINDINGS.md (detailed narrative)

```md
# FINDINGS: Facebook Political Ads (2024 U.S. Presidential Election)

## Overview
This dataset contains 246,745 Facebook ads with 40 columns describing advertiser identity, ad identifiers, delivery timing, and additional labeled fields connected to ad content. The dataset can be used to examine who is advertising at scale, when ad activity increases, how ads are distributed across spend/impressions reporting buckets, and how often specific labels/topics appear.

A key structural feature of this dataset is that major quantitative fields like impressions and spend are reported as bracketed ranges instead of exact values. This affects how descriptive statistics should be interpreted.

## Dataset size and completeness
At a high level, the dataset is large (246,745 rows) and mostly complete, with only a few columns containing meaningful missing values. The highest missing field is `ad_delivery_stop_time` (2,159 missing, 0.875%), followed by `bylines` (1,009 missing, 0.409%) and `estimated_audience_size` (579 missing, 0.235%). The majority of other fields show full coverage.

Missing stop times may reflect ads that were still running at the time the data was collected or incomplete reporting. Missing bylines suggest that sponsor/attribution metadata is not consistently present for every ad.

## Advertising concentration among a small number of pages
Ad volume is concentrated among a relatively small number of advertiser pages. The top page by ad count is Kamala Harris (55,503 ads), followed by Donald J. Trump (23,988) and Joe Biden (14,822). Additional high-volume pages include The Daily Scroll (10,461) and Kamala HQ (7,564).

This concentration suggests that a small number of high-profile political pages account for a large share of the ads captured in the dataset, rather than the activity being evenly distributed across thousands of pages.

## Timing patterns: spikes near the end of the election cycle
The date fields in the dataset span multiple years, with the earliest observed date at 2021-07-06 and the latest observed date at 2024-11-05. Within this overall range, ad creation and ad delivery start dates show clear clustering in late October 2024.

The most common ad_creation_time is 2024-10-27 (8,619 ads), and the most common ad_delivery_start_time is 2024-10-28 (10,089 ads). This indicates a surge in ad creation and launches in the final days leading into Election Day, consistent with late-cycle campaign strategy where activity ramps up as the election approaches.

## Spend and impressions are categorical ranges
Although `spend` and `impressions` look like numeric fields conceptually, the values are stored as string representations of lower/upper bound ranges (e.g., `{'lower_bound': '0', 'upper_bound': '99'}` for spend). This means a direct mean/median computed on these values would not be meaningful without additional parsing and conversion.

The most common spend bucket is `0–99` (135,950 ads). The most common impressions bucket is `0–999` (80,822 ads). The dominance of these lowest buckets suggests that many ads are small-budget ads and/or low-impression ads, at least according to the reporting granularity in the dataset.

A useful next step (not required for this task, but logically motivated) would be to extract lower/upper bounds and compute a midpoint estimate to enable numeric summaries of spend and impressions.

## Indicator fields provide additional interpretability
A large set of columns in the dataset are `illuminating_*` indicator fields. In Pandas, these appear as int64 and many behave like 0/1 flags. For such columns, the mean can be interpreted as the share of ads that carry that label.

For example, `illuminating_msg_type_advocacy`, `illuminating_msg_type_issue`, and `illuminating_msg_type_attack` have non-zero means, indicating that a meaningful share of ads falls into each message category. This provides a way to describe the composition of the ad corpus beyond advertiser identity and timing.

## Key takeaways
1) The dataset is large and mostly complete, with missingness concentrated in a small set of metadata fields (stop time, bylines, estimated audience size)
2) Ad volume is concentrated among major political pages, with Kamala Harris and Donald J. Trump among the most frequent advertisers by ad count
3) Activity spikes in late October 2024, suggesting heavy late-cycle ad launches
4) Spend and impressions are range-encoded, requiring careful interpretation and optional parsing for deeper spend analysis
5) Binary indicator fields provide measurable rates that help characterize ad types and topics

## Next steps (optional)
If extending this analysis, the most natural “go deeper” step would be:
- parsing spend/impressions ranges into numeric estimates and ranking top pages by estimated spend
- plotting ads over time (daily/weekly) to visualize spikes
- comparing indicator field rates across top advertiser pages to see differences in message strategy
