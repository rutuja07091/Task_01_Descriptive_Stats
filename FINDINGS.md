---

## FINDINGS.md

```md
# FINDINGS: Facebook Political Ads Dataset (2024 U.S. Presidential Election)

## Dataset overview
This dataset contains 246,745 Facebook ads across 40 columns tied to advertising activity during the 2024 U.S. presidential election period. Each row represents an ad purchase linked to an organization/page and includes identifiers (page_id, page_name, ad_id), timing fields (ad_creation_time, ad_delivery_start_time, ad_delivery_stop_time), metadata fields (bylines, publisher_platforms, currency), and a set of labeled “illuminating_*” fields that function as content indicators.

The dataset is useful for understanding which political actors are advertising at scale, how activity changes over time, and how ads are distributed across reporting buckets for impressions and spend.

## Data completeness and quality
Most columns are complete, with missingness concentrated in a small number of fields:
- `ad_delivery_stop_time`: 2,159 missing (0.875%)
- `bylines`: 1,009 missing (0.409%)
- `estimated_audience_size`: 579 missing (0.235%)

The missing stop times likely reflect ads that were still running at the time of capture or incomplete reporting. Missing bylines suggest that sponsor/attribution metadata is not consistently present across all records. Overall, the dataset appears clean enough for descriptive summaries and deeper analysis.

## Concentration among major advertiser pages
Ad volume is highly concentrated among a limited number of advertiser pages. The top page_name values by ad count are:
- Kamala Harris: 55,503
- Donald J. Trump: 23,988
- Joe Biden: 14,822
- The Daily Scroll: 10,461
- Kamala HQ: 7,564

This concentration suggests that a small group of major political pages account for a large fraction of the ad activity in the dataset, rather than ad volume being evenly distributed across thousands of pages.

## Timing patterns and late-cycle spikes
Datetime parsing shows that the dataset spans multiple years:
- Earliest observed date: 2021-07-06
- Latest observed date: 2024-11-05

Within that range, the highest-frequency creation and launch dates cluster in late October 2024. The most common ad_creation_time is 2024-10-27, and the most common ad_delivery_start_time is 2024-10-28. This indicates a strong surge in ad publishing and launches in the final period leading up to Election Day.

## Spend and impressions are range-encoded buckets
Although `spend` and `impressions` are conceptually numeric, they are stored as string-encoded lower/upper bound ranges (for example, `{'lower_bound': '0', 'upper_bound': '99'}` for spend). Because these are intervals rather than single values, direct numeric summaries (mean/median) are not meaningful unless the ranges are transformed into numeric estimates (e.g., using lower bounds or midpoints).

The most frequent buckets indicate many ads fall into the lowest reporting ranges:
- Spend bucket `0–99` is the most common
- Impressions bucket `0–999` is the most common

This suggests a large portion of ads are reported in low spend and low impressions categories, at least by the platform’s reporting granularity.

## Indicator fields provide interpretable rates
The dataset contains many `illuminating_*` columns stored as binary indicators (0/1). In Pandas, these appear as int64 fields. For binary indicators, the mean can be interpreted as the share of ads with that flag. For example, fields such as `illuminating_msg_type_advocacy`, `illuminating_msg_type_issue`, and `illuminating_msg_type_attack` have non-zero means, implying that ads in the dataset span multiple message strategies rather than a single content type.

These indicators offer a way to characterize the corpus beyond volume and timing.

## Key takeaways
1) The dataset is large and mostly complete, with missingness concentrated in stop time, bylines, and estimated audience size
2) Ad volume is concentrated among a small set of major political pages
3) There is a clear spike in ad creation and launch activity in late October 2024
4) Spend and impressions are reported as range buckets, so interpretation should reflect interval data rather than exact values
5) Binary indicator fields provide measurable rates that describe ad message and topic characteristics

## Optional next steps
If extending this analysis, the most natural next step would be extracting numeric estimates from the spend and impressions ranges to rank advertisers by estimated spend (not just ad volume), and plotting activity over time (daily/weekly) to visualize spikes and changes through the election cycle.
