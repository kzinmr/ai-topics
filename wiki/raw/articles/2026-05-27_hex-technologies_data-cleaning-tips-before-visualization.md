---
title: "6 Data Cleaning Tips Before Visualizations"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-cleaning-tips-before-visualization/"
scraped: "2026-05-27T06:00:54.249161+00:00"
lastmod: "2026-05-22"
type: "sitemap"
---

# 6 Data Cleaning Tips Before Visualizations

**Source**: [https://hex.tech/blog/data-cleaning-tips-before-visualization/](https://hex.tech/blog/data-cleaning-tips-before-visualization/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex
with the sharpest minds in data - this Summit season in SF
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
Blog
6 data cleaning tips before visualizations
The chart looked fine — until a stakeholder asked why Marketing showed up three times.
The Hex Team
Data
May 22, 2026
Share:
twitter
linkedin
In this article
Why dirty data breaks visualizations
1. Handle nulls and missing values deliberately
2. Standardize formats and deduplicate
3. Triage outliers with a defensible rationale
4. Use charts during cleaning, not just after
5. Keep your cleaning reproducible
6. Automate prevention, not just correction
Clean data, trustworthy charts
Frequently asked questions
Get started for free
You've probably had a version of this morning: you build a bar chart for a stakeholder meeting, and something looks off. Marketing shows 45 employees, but there's also a bar for "marketing" with 23 and another for "MARKETING" with 12. Three bars where there should be one. The total headcount is wrong, the department comparison is wrong, and now you're debugging casing inconsistencies instead of presenting insights.
The underlying data caused the problem.
Dirty data doesn't usually announce itself with error messages. Instead, it shows up in the chart itself: a bar chart that overstates revenue, a time series with physically impossible negative values, or a histogram with a suspicious spike at zero. Because the visualization looks complete and plausible, those errors are easy to miss and dangerous to trust.
Here are six concrete steps that prevent those failures, with examples of what goes wrong when you skip them.
Why dirty data breaks visualizations
Unclean data distorts charts in predictable ways, and those patterns show up in real datasets regularly.
Duplicates inflate totals silently.
Duplicate records can inflate count-based and sum-based charts, making category totals look plausible while overstating the underlying count.
Mixed date formats produce impossible values.
A practitioner on
date-format discussion
documented this with a hotel booking dataset: check-in and check-out dates mixed
MM/DD/YYYY
and
DD/MM/YYYY
formats. The "total nights stayed" calculation produced negative values, which are impossible results that only surfaced in the time series.
Nulls encoded as zeros skew distributions.
In some datasets, zeros are actually placeholders for missing values rather than true observations. Any histogram can show an artificial spike at zero, and box plots can calculate misleading quartiles.
Mixed units create false anomalies.
When a single column mixes units, a line chart can show dramatic jumps or drops that reflect inconsistent measurement rather than a real shift.
According to Hex's
State of Data Teams
research, data quality remains a top concern for data teams and is now the primary barrier cited for AI adoption. When 31% of data leaders cite trust as their top AI concern — nearly twice any other barrier — dirty data feeding into dashboards and AI-generated answers makes the problem worse.
So let's fix it. Here are six cleaning steps worth doing before you build a single chart.
1. Handle nulls and missing values deliberately
Nulls are a common data quality issue and can be especially consequential for visualizations, because different handling strategies can produce materially different charts from identical underlying data.
You usually decide between imputing missing values and dropping them. That choice depends on dataset size, the proportion missing, and why the data is missing.
Dataset size.
For larger datasets, dropping rows with missing values may have less impact on the analysis. For smaller datasets, imputation can help preserve more of the available information.
Proportion missing.
If a column has a very high share of missing values, dropping the column may be the right call. Below that threshold, evaluate the pattern.
Why the data is missing.
This factor matters most. Data that's missing completely at random may be safer to drop. Data that's missing because of the value itself, like high earners not reporting income, needs more care, because dropping those rows can introduce systematic bias.
For visualization, each strategy changes the chart differently.
The visual difference is real. Forward fill creates steps. Interpolation creates smooth lines that may not reflect reality. Mean imputation creates a spike in your histogram at exactly the mean. Each choice tells a different story, so make sure it's the right one.
The SQL null trap
SQL aggregate functions make this worse because they handle NULLs silently.
COUNT(column_name)
ignores NULLs, while
COUNT(*)
counts all rows.
SUM()
and
AVG()
also skip NULLs without warning. So a "department distribution" bar chart built on a query that doesn't account for null departments silently excludes every employee without one. The chart looks complete. The business doesn't know.
The fix is straightforward: make nulls explicit.
Copy
-- Explicit handling (accurate):
Copy
SELECT COALESCE(category, 'Unknown') as category, COUNT(*) as count
Copy
FROM products
Copy
GROUP BY COALESCE(category, 'Unknown');
Now
Unknown
shows up as a visible bar, and the viewer can assess data completeness for themselves.
2. Standardize formats and deduplicate
Structural inconsistencies are a common source of phantom categories in grouped visualizations. SQL
GROUP BY
and pandas
groupby()
can treat character-level differences as distinct values, which means
"Marketing"
,
"marketing"
, and
"MARKETING"
may produce three separate bars in a bar chart. The aggregation is technically correct because it's operating on the data it received. The data itself is inconsistent.
The common problems show up in a familiar handful of places:
Case sensitivity:
"Marketing"
≠
"marketing"
≠
"MARKETING"
Whitespace pollution:
" Boston"
≠
"Boston"
because leading or trailing spaces prevent matching
Date format inconsistency:
"01/12/25"
,
"2025-01-12"
, and
"12-Jan-2025"
can't be grouped on a time axis
Abbreviation mixing:
"New York"
vs
"NY"
creates two groups for one city
Boolean variation:
"Yes"
,
"y"
,
"Y"
,
"true"
,
"True"
,
"1"
can turn into up to seven categories in a pie chart for what should be two
Standardize before you deduplicate. If you run dedup logic before format normalization, your matching algorithm correctly decides that
"New York"
and
"new york"
are not duplicates, because they differ at the string level. Normalize first, or dedup will miss the very duplicates you're looking for.
In Python, the core normalization chain is compact:
Copy
# Case + whitespace in one step
Copy
df['city'] = df['city'].str.strip().str.upper()
Copy
Copy
# Date standardization
Copy
df['event_date'] = pd.to_datetime(df['event_date'], infer_datetime_format=True)
Copy
Copy
# Boolean normalization
Copy
bool_map = {'yes': True, 'y': True, 'true': True, '1': True,
Copy
'no': False, 'n': False, 'false': False, '0': False}
Copy
df['is_active'] = df['is_active'].str.lower().map(bool_map)
In SQL, the equivalent:
Copy
SELECT UPPER(TRIM(city_name)) as city_normalized
Copy
FROM locations;
For large datasets, performance can vary depending on how you normalize text columns. For production pipelines processing millions of rows, that can be the difference between viable and not.
A practical caveat
Not all variation should be normalized. If you're working with historical data, multilingual datasets, or cases where different spellings carry semantic meaning, standardization can erase valuable information. As the
Programming Historian
notes, "To 'clean' that data in the expected manner, to standardize it, would erase historically significant information." Domain knowledge is needed to determine whether a variation is noise or signal before applying bulk normalization.
3. Triage outliers with a defensible rationale
In business data, many outliers may be real. Your highest-revenue customer is a statistical outlier. Removing that point without a documented rationale is methodologically equivalent to cherry-picking data.
A
statistical outlier
is a value far from the center of the distribution. A
domain anomaly
is a value that shouldn't exist given what you know about the domain. A customer with age 200 is a domain anomaly, so remove it. Your highest-revenue account is a statistical outlier, so keep it.
Outlier triage starts with statistical detection, moves to domain validation, and ends with visual confirmation.
Statistical detection.
Use IQR/Tukey's fences or z-scores to flag
candidates
for investigation, not removal. Note that IQR-based methods
for skewed data
can over-flag valid data, and z-scores are sensitive to the very outliers they're trying to detect. For high-dimensional data, multivariate methods can catch patterns that univariate methods miss.
Domain validation.
For every flagged point, ask: Is this value physically or logically possible? Could it represent a genuine extreme event? Are flagged points concentrated in a time period or data source that suggests a process failure?
Visual confirmation.
Plot the distribution with and without the flagged points. Does removing the point change the story, or just make the chart look tidier?
Outliers shift means in bar charts, compress histogram scales into narrow strips, and squash scatter plot clusters into corners. When they're legitimate but distort your chart, transformation often beats removal: a log scale compresses skewed right tails, and winsorization replaces extreme values at the Nth percentile rather than removing them. That preserves your row count while limiting outlier influence.
Whatever you decide, document it. Record the detection method, the domain assessment, the decision, and the rationale. As one
Stack Exchange discussion
puts it bluntly: "To conclude that [an extreme value] reflects some problem with the data is tantamount to claiming that reality must conform to your statistical assumptions."
4. Use charts during cleaning, not just after
Charts are useful during cleaning because they surface problems that summary statistics can hide. A histogram catches issues that
df.describe()
buries.
Exploratory data analysis
emphasizes flexible use of summaries and visualizations to understand data, so visualizations can play an important role during data cleaning rather than only at the end.
A few chart types work especially well as first-line diagnostics during cleaning.
Histograms
catch impossible values. A spike at zero in a biological measurement likely means null-encoded-as-zero. A spike at 9999 probably means a sentinel value. Multiple peaks in a supposedly unimodal column can point to mixed populations or unit inconsistencies.
Box plots
flag outliers with a statistically grounded threshold and reveal inconsistent collection across groups. Different IQR ranges for the same measure across regions might mean one region recorded in different units.
Scatter plots
expose relational violations that single-variable analysis can't detect. A 20-year-old with 30 years of work experience. A purchase before the customer's account creation date. These problems are invisible in column-level summaries.
Time series line plots
surface process failures. A flat line period is likely a sensor failure encoded as a constant. A sudden step-change suggests a unit conversion or system migration.
Correlation heatmaps
catch structural issues across many columns simultaneously. A correlation of exactly 1.0 can mean one column is a duplicate or directly derived from another. Near-zero correlation for a column that should relate to several others signals a wrong join key.
The workflow is iterative: profile, clean, check relationships, clean again, verify temporal patterns, then re-profile. That last step matters because cleaning operations can introduce their own artifacts, like a
pd.to_datetime()
call with the wrong format string silently converting dates to
NaT
.
This iterative cycle is where the right tooling makes a meaningful difference. In Hex's
notebook environment
, updating a SQL cell can trigger dependent downstream logic to re-execute, and its results flow into charts and other downstream cells. SQL and Python live in the same workspace, so after updating the cleaning logic you see the impact in downstream charts without switching tools.
Copy
# Quick diagnostic suite — run these before any other cleaning
Copy
df.hist(bins=50, figsize=(20, 15))
Copy
plt.tight_layout()
Copy
Copy
import seaborn as sns
Copy
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
Copy
Copy
df.boxplot(column='amount', by='region', figsize=(12, 6))
5. Keep your cleaning reproducible
If a stakeholder can't trace a chart's value back through documented transformations to a known source, the chart isn't trustworthy, regardless of how accurate the data actually is.
A common principle in analytics engineering is that cleaning logic belongs in version-controlled, tested SQL models. It should not live only in ad-hoc scripts, in notebook cells that aren't committed anywhere, or in Excel transformations that happen before data enters the warehouse. The rigor depends on context.
Documented notebooks
matter for exploratory analysis.
In practice, reproducibility means a few concrete things.
Version-control transformation logic.
Store SQL models and Python cleaning scripts in Git with descriptive commits so you can reference exactly which logic a chart was built from.
Write transformations as code, not ad-hoc queries.
SQL models can be reviewed, tested, and reused across environments.
Test automatically.
In dbt,
not_null, unique, accepted_values
, and
relationships
tests help catch cleaning failures before they propagate to dashboards.
Build and expose lineage.
Lineage makes the clean-to-chart chain visible and auditable. When a stakeholder asks "where did this number come from?" lineage provides a clear answer.
Log cleaning decisions.
Every rule applied in production should record what action was taken, how many rows were affected, and why:
Copy
- drop_invalid_email: 1,247 rows removed
Copy
- dedupe_order_id_latest: 89 duplicates resolved (kept most recent)
Copy
- impute_country_from_email_domain: 334 nulls filled
This is what Calendly's Go-to-Market analytics team did by building a
Standardized Metric Library
as company-wide KPI documentation, a single source of truth that helps tie-break conflicting reports.
6. Automate prevention, not just correction
The five tips above focus on fixing problems you've already found. This last one focuses on catching them before they reach your analysis at all.
Format standardization rules often belong in the staging layer of your pipeline, applied once when data enters the
warehouse architecture
. If every city name gets
UPPER(TRIM())
on ingestion, you never see phantom categories in a downstream bar chart. For teams using dbt, this means writing these rules into staging models:
Copy
models:
Copy
- name: stg_customers
Copy
columns:
Copy
- name: email
Copy
tests:
Copy
- not_null
Copy
- unique
Copy
- name: region
Copy
tests:
Copy
- accepted_values:
Copy
values: ['NA', 'EMEA', 'APAC', 'LATAM']
These tests run on every pipeline execution. When upstream data changes in ways that would break a visualization, such as a new region code or a null in a required field, you find out in CI, not from a stakeholder staring at a broken chart.
Clean data, trustworthy charts
Data cleaning isn't glamorous work, but it's the foundation that every chart, dashboard, and data app rests on. The six steps here, handling nulls deliberately, standardizing formats, triaging outliers with rationale, using charts as diagnostic tools during cleaning, keeping transformations reproducible, and automating prevention, won't eliminate every data quality issue. But they'll catch the ones that mislead stakeholders silently, which are the ones that actually matter.
The common thread is iteration: clean, chart, verify, repeat. Environments that support that loop tightly, where you can write SQL, run Python, plot a histogram, and
share the work
without switching tools, make this work faster and more reliable. Hex brings that full workflow into its notebook environment, a collaborative notebook in a unified workspace, so cleaning and visualization aren't separate stages but a continuous conversation with your data.
Sign up for a free account
or
request a demo
to see how it works.
Frequently asked questions
How do I decide whether to clean data in SQL or Python?
It depends on where the data lives and what kind of cleaning you're doing. SQL is typically better for filtering, deduplication, type casting, and standardization that runs close to the warehouse, especially for recurring pipelines where you want the logic in a dbt model. Python shines for more complex transformations: regex-based parsing, fuzzy matching, statistical imputation, and anything that benefits from libraries like pandas or scikit-learn. In practice,
data science workflow
use both.
Should I clean data differently if I'm building an exploratory chart versus a production dashboard?
Yes. The bar is different. For exploratory work, speed matters more than rigor. You might drop nulls quickly, plot a histogram to check the shape, and move on. For a production dashboard, every cleaning step should be tested, documented, and version-controlled so the numbers are reproducible and auditable. The risk is that exploratory cleaning becomes load-bearing infrastructure by accident. A quick notebook gets shared, people start relying on it, and suddenly an undocumented
fillna(0)
is driving a quarterly forecast.
How do I communicate data quality limitations to stakeholders who just want the chart?
Make limitations visible in the visualization itself rather than burying them in footnotes nobody reads. If a meaningful share of your data is missing for a particular dimension, add an "Unknown" category to the bar chart instead of silently dropping those rows. If you've applied imputation, annotate the chart. For dashboards, a simple data freshness indicator and a completeness percentage go a long way toward building appropriate trust, giving stakeholders enough context to make informed decisions rather than overconfident ones.
Share:
twitter
linkedin
Get "The Data Leader’s Guide to Agentic Analytics"  — a practical roadmap for understanding and implementing AI to accelerate your data team.
Download
Request a demo
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
