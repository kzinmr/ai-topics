---
title: "20 Data Visualization Techniques For Clear Stories"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-visualization-techniques/"
scraped: "2026-06-04T06:00:27.874416+00:00"
lastmod: "2026-05-22"
type: "sitemap"
---

# 20 Data Visualization Techniques For Clear Stories

**Source**: [https://hex.tech/blog/data-visualization-techniques/](https://hex.tech/blog/data-visualization-techniques/)

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
20 data visualization techniques for clear stories
You picked the right chart, the colors are clean, and the dashboard still sits unused. Here's what the chart picker can't tell you.
The Hex Team
Data
May 22, 2026
Share:
twitter
linkedin
In this article
Choose the chart based on the question being asked
Comparison: how do values differ across categories?
Distribution: how are values spread?
Composition: how do parts make up a whole?
Relationship: how do variables relate?
Change over time and space
Design techniques that make any chart tell a clearer story
The problems that happen before (and after) you pick a chart
Build visualizations that support decisions and stay connected to the work
Frequently asked questions
Get started for free
You've built the dashboard. The colors look great. The filters work. And then nobody uses it.
This is a familiar pattern for anyone who builds visualizations for a living. The problem is often that the chart doesn't answer the question anyone was actually asking.
Stephen Few's framework
identifies seven core types of quantitative messages: nominal comparison, time-series, ranking, part-to-whole, deviation, frequency distribution, and correlation. Many visualization decisions map back to one of those categories. Start with the message instead of the chart picker and everything downstream gets easier. The chart type becomes obvious, design choices follow logically, and the stakeholder on the other end can actually do something with what they see.
Choose the chart based on the question being asked
The question should determine the chart type. As the Data Visualization Society notes in
Nightingale
, chart taxonomies "can help analysts and designers make better-informed decisions about what charts to use when" while cautioning against treating them as rigid rules. Use the categories below as organizing principles.
Comparison: how do values differ across categories?
1. Bar chart
The foundation of categorical comparison, and still the most reliable. Bars anchored to zero make magnitude differences immediately readable, and
Charles Apple
calls them "one of the most useful tools in creating rapid-read data visualizations." The most common misuse is truncating the y-axis to exaggerate differences.
2. Horizontal bar chart
Same idea, rotated, and surprisingly underused. When your category labels are long or you're comparing more than a handful of items, horizontal bars let viewers scan naturally. Avoid using them for time-series data, where left-to-right convention implies temporal progression.
3. Grouped bar chart
Compares values across categories
and
a secondary variable simultaneously. As
Storytelling with Data
notes, "if you're comparing across categories, grouped bar charts can be clearer" than stacked alternatives when side-by-side comparison is the point. Keep it to 3–4 groups per cluster.
4. Bullet graph
Stephen Few
designed this as a compact alternative to gauge and speedometer charts, which he
criticizes
for wasting space and encoding data poorly. Bullet graphs compare a primary measure against a target in constrained dashboard space. They're ideal when every pixel matters.
5. Slope chart
Comparing values between exactly two time points across multiple categories.
Slope charts
are an appropriate chart type to show change over time for two-endpoint comparisons. More than two points? Switch to a line chart.
Distribution: how are values spread?
6. Histogram
Your go-to for understanding how a single continuous variable is distributed.
Bin width
is the critical choice: too few bins hide structure, too many add noise.
7. Box plot
If you need to compare distributions across groups quickly, box plots show median, quartiles, and outliers at a glance. But box plots are often criticized for obscuring the underlying shape of the data. If distributional shape, bimodality, or skew is your actual question, use a violin or density plot instead.
8. Violin plot
Violin plots
show the full distribution shape across groups and make bimodal or skewed distributions visible where box plots hide them.
Composition: how do parts make up a whole?
9. Stacked bar chart
Stacked bars show part-to-whole composition while comparing totals, but they come with a catch: only the bottom segment shares a common baseline, which means middle and upper segments can't be compared reliably across categories. Stephen Few argues that line graphs are effective for showing change over time, though the specific claim that they "display the data more effectively in every respect" for proportional change over time is not supported by the available evidence.
10. Treemap
For comparing many items as proportions of a whole, especially with hierarchical grouping, treemaps scale where bar charts can't. As Stephen Few notes, treemaps can display more items than a typical bar graph, though they do so using encodings that are less perceptually effective than bar lengths. The tradeoff: area estimation is less accurate than length comparison.
11. Waterfall chart
Shows how an initial value is affected by a series of positive and negative increments.
Waterfall charts
are ideal for visualizing "the composition of the Margin as a Process."
Relationship: how do variables relate?
12. Scatter plot
The default for bivariate correlation, revealing direction, strength, and form of relationships, plus outliers.
One common mistake
is a title that implies causation when only correlation is demonstrated.
13. Heatmap
Shows intensity across two dimensions, or a correlation matrix across many variables.
Color scale
is the key design decision: diverging scales (blue-white-red) for ranges that cross zero, sequential scales for magnitude-only data.
14. Bubble chart
A scatter plot with a third variable encoded as bubble size. This is where one of the most common encoding errors lives: the
Maryland guide
warns that "your bubbles'
area
is what represents the data, not the width of the bubble." Encoding in radius instead of area systematically overstates larger values.
Change over time and space
15. Line chart
The most reliable choice for time-series data. As
Storytelling with Data
confirms, "if you're looking at trends over time, line graphs usually do the job best." Unlike bar charts, the y-axis doesn't need to start at zero, so you can zoom in on small movements. Just don't connect discrete, unordered categories with a line.
16. Area chart
A line chart with the area beneath filled, emphasizing magnitude and cumulative volume. Avoid stacking too many series. Individual values become unreadable fast.
17. Choropleth map
Shows how a variable is distributed across geographic regions using color intensity. Claus Wilke provides the
clearest guidance
: "Choropleths work best when the coloring represents a density." The biggest mistake is mapping raw counts instead of rates, total cases instead of cases per 100,000, which lets large, sparse regions dominate the visual.
Design techniques that make any chart tell a clearer story
18. Annotation
When you don't annotate, you're asking your audience to do unnecessary work. As
Storytelling with Data
notes, "words help graphs make sense." Place the key takeaway at the beginning of the annotation, not buried at the bottom, and use matching color to tie annotation text to its relevant data series. Don't assume the chart communicates the insight on its own. As one data-visualization principle suggests, audiences do not automatically derive insights simply from being shown a chart.
19. Strategic color (the gray-out technique)
Render all non-focal data in gray and apply a single accent color to the series that carries the story.
Storytelling with Data
demonstrates this with slope charts: "I used line color sparingly and strategically just for the top 3 countries and used gray for all other countries." This directs the viewer's eye without requiring them to decode a dense legend.
20. Decluttering
Declutter and question defaults
: remove the chart border, delete gridlines unless someone would physically trace a finger to read a value, use data labels sparingly, and make bars wider than the white space between them. Every element that doesn't add understanding adds cognitive load.
The problems that happen before (and after) you pick a chart
In practice, choosing the right chart is the easy part.
Dashboards built in isolation go unused
Dashboard adoption has been a persistent problem, and
Dataversity reports
that 60% of BI initiatives fail outright, attributed to weak data quality, absence of data culture, and lack of continuous improvement.
Fragmented toolchains make it worse. Analysts lose just under four hours per week context-switching across tools, according to a 2022 Harvard Business Review study. You write SQL in one tool, export a CSV, build charts in another, paste screenshots into a slide deck.
Hex
brings AI analytics into a unified workspace where teams write SQL and Python, build visualizations, and publish results. Notebook Agent helps data teams move from SQL and Python to visualizations and publishing in the same workflow so the analysis and the output stay connected.
Static screenshots don't cut it anymore
Many teams still end up optimizing for
delivery
over decision-making. As the
International Institute for Analytics
argues, the more important outcome is whether a decision was made. The same research identifies this as the core gap: a screenshot in Slack shows
what
happened without explaining
why
, and it can't adapt to different audiences. When a stakeholder can test their own hypothesis ("does this hold for my region?") without submitting a new request, you've shifted from delivering charts to enabling decisions with Threads.
This played out at
Workrise
, where analysts had been recreating visuals after every exploratory analysis because their tools were fragmented. After consolidating into a unified workspace, connecting to Snowflake, writing SQL and Python, and producing interactive visualizations in minutes, over 50 people across the company started creating their own analyses.
Metric chaos is a visualization problem
Metric inconsistency often shows up as the same business concept being defined differently across dashboards and reports. Each definition made sense when it was created, but they've diverged. According to Forrester research cited in the article, 61% of organizations use four or more BI platforms, often contributing to siloed definitions.
This is a structural outcome of how most companies are organized. But it means your perfectly chosen chart type might still mislead people if the metric behind it doesn't match what they think it means.
The fix is governing definitions upstream of any visualization tool. Some teams start by endorsing trusted tables and adding warehouse descriptions so analysts and AI agents know which data to use. Others add workspace rules that shape how queries are written. As definitions mature, semantic models — authored directly in Hex or synced from dbt MetricFlow, Cube, or Snowflake — formalize those definitions so every downstream chart pulls from the same calculation.
Context Studio
closes the loop by surfacing where questions are hitting governance gaps.
When AI-generated visualizations are confidently wrong
AI generates charts fast, but a
benchmark study
found they're wrong more often than most teams realize. Across 24 chart types, GPT-4o produced correct Vega-Lite output only 70% of the time. Gemini managed 24%. Standard types like bar charts and scatter plots performed reliably, but specialist types, violin plots, radar charts, and range plots, failed consistently.
The deeper problem is context: when prompts lack specification about chart structure or the dataset schema is ambiguous, models default to
macro-level visual heuristics
over fine-grained structural cues like exact tick values. The output looks polished whether the numbers are right or wrong, and a
systematic review
found that large language models (LLMs) sometimes generate code referencing columns that don't exist in the dataset.
With well-structured data and clear analytical intent, Notebook Agent can genuinely accelerate standard chart types, and analyst judgment remains essential where the input context is ambiguous or the chart type is specialized.
What self-serve visualization actually needs
A BI tool alone rarely gives stakeholders the answers they need. According to
State of Data Teams
, enabling self-serve dropped out of data teams' top focus areas as AI implementation took over. Yet the underlying access problem remains unresolved for most teams. Accenture's research on
data literacy
explains part of the gap: only 21% of the global workforce describes themselves as fully confident in their data literacy skills.
As one example from Zscaler put it, self-service can be a "double-edged sword": after moving to a self-service analytics model, the data team faced growing pull request review demands.
Real self-serve takes governed metrics, aggregation guardrails, data literacy investment, and a platform that abstracts complexity to match users' actual capabilities. In Hex, Threads provide the conversational self-serve experience, while the underlying metric governance lives in Semantic Modeling.
Build visualizations that support decisions and stay connected to the work
The best chart in the world doesn't help if nobody trusts the number behind it, can't interact with the output, or sees a different answer on someone else's dashboard. Data visualization techniques cover more than chart selection. They shape the entire path from question to trusted, shareable insight.
That path breaks down in predictable places: fragmented toolchains, silently diverging metric definitions, and static outputs that can't adapt to follow-up questions. Fixing chart selection alone leaves those structural problems untouched, and the result is prettier artifacts that still go unused.
The right chart for the right question gets you halfway. Annotation, strategic color, and decluttering carry the rest of the load on the visualization side. They're often the difference between a chart someone glances at and one that changes a decision. The structural pieces matter just as much: governed metrics so every dashboard computes the same number, connected toolchains so analysis doesn't die in a screenshot, and interactive outputs so stakeholders can answer their own follow-up questions.
You don't need to fix everything at once. Start with the metric that causes the most confusion across teams, or the dashboard that gets the most complaints, and work outward. Small, visible improvements in trust compound faster than sweeping overhauls.
Hex brings those pieces together through collaborative notebooks, Threads, and Semantic Modeling so teams can write SQL and Python, build visualizations, and share interactive outputs in one place while keeping metric definitions consistent across charts. When the work stays connected, it actually gets used.
Sign up for a free account
or
request a demo
to see how it works.
Frequently asked questions
How do I decide between a static report and an interactive dashboard?
The answer depends on whether the audience needs to explore or just absorb a conclusion. If you're presenting a specific finding to leadership, "churn increased 12% in Q3, here's why," a static, annotated visualization often lands better than a dashboard full of filters. But if the audience will have follow-up questions that vary by role or region, an interactive output saves you from fielding those requests one by one. Many teams find the right answer is both: a narrative layer for the headline, with
data apps
underneath for anyone who wants to dig deeper.
Should I invest in a semantic layer before improving my visualizations?
If your team regularly encounters conflicting numbers across dashboards, with "revenue" meaning different things in different reports, then governing your definitions will do more for visualization trust than any design improvement. You don't need a full semantic model on day one. Start by endorsing your most-queried tables and adding descriptions that give agents and analysts useful context. Add workspace rules for organizational standards. Then formalize with semantic models when the pain justifies the investment. You can author them directly in Hex or sync existing definitions from dbt, Cube, or Snowflake. Begin with three to five key metrics and expand from there. Without that foundation, even beautifully designed charts can erode trust when they show numbers that don't match.
How many chart types does my team actually need to master?
Fewer than you'd think. Most teams rely heavily on a handful of chart types, bar charts, line charts, scatter plots, heatmaps, and a few others, for the bulk of their work. Instead of memorizing all 20 techniques here, focus on matching the analytical question to the right category: comparison, distribution, composition, relationship, or change over time. Once you've identified the category, the chart type follows naturally, which is exactly what Few's seven quantitative message types from the introduction are designed to do. The specialist types like bullet graphs, violin plots, and waterfalls are worth learning when you encounter their specific use case, not before.
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
