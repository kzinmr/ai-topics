---
title: "What Is Model Drift? Causes, Detection, and How to Fix It | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/what-is-model-drift/"
scraped: "2026-05-10T01:29:03.968684+00:00"
lastmod: "2026-04-16"
type: "sitemap"
---

# What Is Model Drift? Causes, Detection, and How to Fix It | Hex 

**Source**: [https://hex.tech/blog/what-is-model-drift/](https://hex.tech/blog/what-is-model-drift/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
Model drift explained: causes, detection, and fixes
Most drift investigations don't find a model problem. They find a data quality problem upstream. The model was just the canary.
The Hex Team
Data
April 16, 2026
Share:
twitter
linkedin
In this article
What model drift actually means
The causes you can actually control
How to detect drift before it becomes a business problem
What fixing it looks like in practice
How governance and observability reduce drift over time
Keep your models honest
Frequently Asked Questions
Get started for free
Model drift is the gradual loss of predictive accuracy that happens when the conditions behind a model change after deployment. The gap between what a model predicts and what actually occurs keeps widening, and teams usually notice only after the business impact is already visible.
Your churn analysis model worked great in January, and leadership cited it in board meetings. Then, sometime around March, the numbers started feeling off. Customer success flagged accounts that churned despite being classified as low risk, a VP said the forecast "didn't match reality" in a Slack thread, and before long, nobody was calling it "drift." They had simply stopped trusting the model.
That's how model drift usually shows up. It starts with a stakeholder squinting at a dashboard and ends with someone maintaining a shadow spreadsheet "just to double-check."
What model drift actually means
Model drift is sometimes used as a catch-all for any production performance decline, but the underlying causes are distinct enough to be worth separating. Knowing which kind of change you're dealing with changes how you respond, and whether you should touch the model at all.
Data drift (covariate shift)
Data drift — also called covariate shift — happens when the distribution of input features changes after training. A retail demand model trained on in-store purchase data starts seeing online orders surge. The model keeps running, but predictions degrade because the input mix shifted underneath it. The model is doing exactly what it learned to do; it's just working on different data than it was built for.
Concept drift
Concept drift shows up when the relationship between inputs and outcomes changes, even if the input distribution stays the same. If a competitor launches aggressive discounts in your category, shopper behavior may carry a different signal than it did when you trained the model. The features look familiar; the meaning of those features has changed.
Prediction drift
Prediction drift means the distribution of model outputs changes. This can be entirely expected: when fraud attempts spike, your fraud model should start predicting more fraud. Prediction drift only becomes a problem when output shifts happen without a corresponding change in the real world.
Training-serving skew
Training-serving skew refers to mismatches visible shortly after deployment because the training environment and production environment were never the same to begin with: different data sources, preprocessing steps, or feature computation logic. Unlike drift driven by real-world change, skew is structural. It stems from how the model was built and deployed, not from how the world has changed since. If performance looks poor immediately after deployment, check here first before investing in monitoring infrastructure.
Upstream drift
Upstream drift is caused by changes in the data pipeline itself rather than changes in the real world. A schema change, a new data source, a renamed column: any of these can degrade predictions without any shift in the underlying phenomenon the model is measuring. It's the most common cause of apparent drift and the first place to look.
The distinction matters because the remedies are different. Upstream drift needs pipeline fixes. Concept drift may need retraining. Skew needs a closer look at how training data was constructed. Reaching for retraining first is the most common and most expensive mistake.
The causes you can actually control
Most apparent drift is not a model problem. It's a data quality problem, a feature processing problem, or a metric definition problem. All of these sit upstream of the model itself. Check data quality before you set a retraining trigger.
Upstream pipeline changes
This is upstream drift in practice: a column gets removed from an upstream table, and your model can't access a feature it depends on. The result looks exactly like model degradation (dropping accuracy, shifting outputs) even though the model hasn't changed. When you start an investigation, pulling a schema diff or checking recent pipeline deploys against the date drift began will often get you there faster than any statistical test.
Feature engineering breakdowns
Feature engineering can break when processing steps no longer match live data. Consider a StandardScaler fitted on values ranging 1 to 4. When production data starts containing values from 2 to 6, predictions degrade because the feature pipeline is outdated. Updating the feature code matters more here than retraining the model. You're fixing the translation layer, not the learned logic.
Data quality issues masquerading as model problems
If your features fill with nulls, values fall out of range, or a configuration change routes the wrong data into your model, you'll see drift-like symptoms immediately. A text model trained on English that suddenly starts receiving Spanish-language inputs because of a routing change is a clean example: the model hasn't changed, the world hasn't changed, and the pipeline broke.
Stale metric definitions
Stale metric definitions can make a healthy model look broken. New product categories get introduced, fiscal year boundaries change, and a feature encoded at training time no longer maps cleanly to new values. These problems usually trace back to governance gaps that never propagated through the rest of the system. Retraining won't fix them either; you'd just be training on the same broken definitions.
How to detect drift before it becomes a business problem
Teams typically discover drift after someone questions a dashboard number. By then, degradation may have been compounding for weeks. A working detection workflow doesn't need a dedicated MLOps team. It needs a baseline and a daily SQL job.
Store a training baseline
Save summaries from your training data: feature distributions, percentiles, key statistics. Without a clear comparison point, you're diagnosing by intuition, and intuition usually shows up late.
Use accessible statistical checks
Population Stability Index (PSI) measures how much a distribution has shifted between your training baseline and current production data, and it works for both numerical and categorical features. As a widely used rule of thumb, PSI below 0.1 indicates minimal change; between 0.1 and 0.2 signals moderate change worth monitoring; above 0.2 signals a meaningful shift that warrants investigation. Treat these as starting points, not hard rules. The right threshold depends on your use case and data volume.
A basic PSI check for a numerical feature runs in SQL:
with baseline as (
select feature_bin, pct_of_rows as baseline_pct
from training_feature_distribution
where feature_name = 'avg_order_value'
),
current as (
select feature_bin, pct_of_rows as current_pct
from daily_feature_distribution
where feature_name = 'avg_order_value'
and ds = current_date
)
select
sum((c.current_pct - b.baseline_pct) * ln(c.current_pct / nullif(b.baseline_pct, 0))) as psi
from current c
join baseline b using (feature_bin);
For categorical features, applying PSI directly to the category distribution works the same way. A chi-square test is another accessible option for comparing categorical distributions.
Set alert thresholds around business impact
Not all shifts warrant the same response. Work with stakeholders to define in advance which features are high-importance and what thresholds trigger investigation versus immediate action. Without this protocol, alerts pile up unanswered. An ignored alert is functionally the same as no monitoring at all.
Match monitoring frequency to use-case risk
Fraud detection and real-time pricing models typically need daily or near-real-time checks. Lower-risk models can run weekly. If you're investigating a suspicious result in a collaborative notebook, you can run these checks and trace the output directly to the query or metric definition behind it without leaving the environment where the original analysis lives. If your team runs these checks on a regular cadence, publishing the monitoring notebook as an
interactive data app
gives stakeholders visibility into model health without requiring a request every time someone wants to know whether the numbers can be trusted.
What statistical checks don't catch
Input monitoring has a real blind spot. In credit scoring, for example, applicant characteristics might stay stable while default risk rises due to macroeconomic shifts. The feature distributions look fine while predictions quietly get worse. PSI won't surface that.
If you're serving AI analytics queries alongside production models, question patterns from your users can serve as an early signal. Your sales team suddenly asking about a market segment that didn't exist at training time is a clue that your model's assumptions may be going stale before any metric flags it.
What fixing it looks like in practice
The right remedy depends on what changed. Diagnose before you retrain. The table below is a starting point for mapping what you're seeing to where to look first.
Symptom
More likely root cause
First response
Sudden spike in nulls or missing values
Pipeline or schema change
Fix the pipeline
Predictions shift after a data migration
Feature processing issue
Update feature code
Model works on some segments, fails on others
New categorical values or distribution shift
Update encodings or retrain on augmented data
Predictions gradually degrade over months
True concept or data drift
Investigate feature distributions, then consider retraining
Fix the data first
When the root cause is a pipeline issue, schema change, or data quality problem, fix it before anything else. Retraining on dirty data bakes the problem into the next model version: you'd be teaching the model to expect broken inputs.
Retrain when you've confirmed the problem
Retraining makes sense after you've confirmed performance degradation with real outcomes, accumulated sufficient new data, and verified data quality. Some teams use time-based retraining for use cases with predictable change patterns, like seasonal demand forecasting. Others retrain only when monitoring confirms a real performance drop.
The infrastructure cost matters here. More frequent retraining means more operational overhead, so it's worth justifying before you build the pipeline, not after.
Update metric definitions when business logic has changed
When different teams define "revenue" differently, or when business logic has evolved since training, retraining won't solve the underlying issue. Teams need centralized metric ownership, version-controlled definitions, lineage, and change detection so outdated logic stops flowing into models, dashboards, and reports.
This is the category most teams underestimate. And in cases where concept drift is deep enough that the model's original objective no longer maps cleanly to the business outcome you care about, the answer may not be retraining on new data at all, but revisiting the model's architecture or loss function entirely.
How governance and observability reduce drift over time
Many drift investigations turn out to be definition problems, not model problems. When different teams calculate the same business metric in different ways, you lose the ability to tell whether the model changed, the data changed, or the meaning of the target changed. Two dashboards showing different "revenue" numbers don't just slow diagnosis; they make it impossible to agree on whether a problem exists at all.
Calendly's approach
is a useful example of what solving this looks like in practice. Their Go-to-Market analytics team could respond quickly to stakeholder requests, but speed came at the cost of reproducibility. They built a standardized metric library in Hex as company-wide KPI documentation: a shared reference for tie-breaking conflicting reports and a foundation for tracing discrepancies back to their source.
Start where you are
The maturity path typically runs from scattered SQL and notebook logic, to partially shared models with manual upkeep, to governance with version control, testing, lineage, and change management. You don't need to reach that final stage before getting value. Endorsing trusted tables, documenting warehouse objects, and setting workspace rules for how analysts use core metrics all reduce the number of places where conflicting definitions can enter the workflow, and your team can start on any of them today.
For teams that want to go deeper, Hex's
semantic model sync
pulls governed definitions directly from dbt MetricFlow, Snowflake Semantic Views, or Cube so analysts and AI agents are working from the same source of truth. If you're actively authoring or iterating on those definitions,
semantic authoring
drafts the modeling work while keeping the logic transparent and reviewable.
Close the loop with observability
Closing the loop means monitoring not just inputs but outcomes and usage patterns.
Context Studio
surfaces what questions people are actually asking across the workspace, where answers are relying on unstructured sources instead of governed definitions, and where quality is falling short, so your data team can prioritize context improvements before weak answers spread.
For deeper investigations, Hex's Notebook Agent lets you trace a suspicious result through the generated SQL and Python logic in the same notebook where the analysis lives, rather than reconstructing it somewhere else.
Keep your models honest
Drift is one reason data teams lose confidence in models over time, and rebuilding that confidence is harder than preventing the slide in the first place. The teams that manage drift well see problems sooner and respond with a defined process rather than a post-incident scramble.
Start with what you can control today: pipeline quality, metric definitions, and feature engineering hygiene. Build detection you can run in SQL. Use shared definitions, endorsed tables, and visible query logic so inconsistencies surface before someone has to explain away bad numbers in a board meeting. None of it needs a dedicated program. It just means making the invisible visible early enough to act on it.
Frequently Asked Questions
What's the difference between model drift and data drift?
Data drift (also called covariate shift) is one specific cause of model drift: the distribution of input features changes after training. Model drift is the broader term for any loss of predictive accuracy in production, regardless of cause. A model can experience drift from data drift, concept drift, pipeline failures, or stale metric definitions. Data drift is one path to that outcome, not the only one. In practice, many practitioners use the terms interchangeably, but the distinction matters when diagnosing: if inputs look stable but performance is declining, you're likely looking at concept drift or a definition problem, not data drift.
Can we detect drift without ground-truth labels?
Yes — and in many production systems you'll have to, because labels often arrive weeks or months later. PSI and the Kolmogorov–Smirnov (KS) test both compare current input distributions against the training baseline without needing outcome labels. Shifts in prediction distributions or business outcomes can serve as proxy signals while labels catch up. That won't confirm model quality on its own, but it tells you where to look sooner and narrows the window between when a problem starts and when someone files a ticket.
How often should we retrain production models to stay ahead of drift?
Retraining cadence depends on how quickly your data changes and how much infrastructure you're willing to maintain. High-stakes use cases like fraud detection or real-time pricing may need daily or weekly retraining; slower domains often work fine with quarterly updates. In practice, retraining after confirmed degradation or predictable seasonal change tends to outperform autopilot schedules, because it forces you to verify the root cause first. Before you retrain anything, confirm the issue isn't a broken pipeline or stale business logic. Retraining on bad inputs just produces a model that's confidently wrong about newer data.
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
