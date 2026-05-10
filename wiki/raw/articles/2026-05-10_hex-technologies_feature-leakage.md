---
title: "Feature leakage in ML: Detect, Prevent, and Fix It | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/feature-leakage/"
scraped: "2026-05-10T01:29:43.206078+00:00"
lastmod: "2026-05-05"
type: "sitemap"
---

# Feature leakage in ML: Detect, Prevent, and Fix It | Hex 

**Source**: [https://hex.tech/blog/feature-leakage/](https://hex.tech/blog/feature-leakage/)

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
Feature leakage in ML: Detect, prevent, and fix it
Your churn model hits 0.97 AUC in validation, leadership greenlights production, and two weeks later, it's predicting no better than a coin flip. That's feature leakage, and nothing in your evaluation loop warned you.
The Hex Team
Data
May 5, 2026
Share:
twitter
linkedin
In this article
Why feature leakage fails silently
The confidently wrong model problem
Catching leakage during EDA, before it compounds
Where pipeline decisions introduce leakage
AI-generated code as a new leakage vector
Making leakage prevention a team habit
Build models you can trust in production
Frequently Asked Questions
Get started for free
Most ML failures are obvious: accuracy drops, errors spike, and someone notices. Feature leakage is different because your
churn analysis
model can hit 0.97 AUC in validation, the team celebrates, leadership greenlights production deployment, and two weeks later the model is predicting roughly as well as a coin flip, with nobody able to explain why the metrics collapsed.
That pattern points to feature leakage. A model looks brilliant in development and falls apart the moment it touches real data, even though every standard evaluation metric said it was working. That's what makes leakage so frustrating. It doesn't just produce wrong predictions. It produces wrong predictions you had every reason to trust.
Why feature leakage fails silently
Feature leakage, sometimes called data leakage, happens when information that wouldn't be available at prediction time sneaks into your training data. The model learns patterns that are technically valid in your dataset but impossible to reproduce in production.
Leakage is uniquely dangerous because it defeats the standard diagnostic for model quality. With classical
overfitting explained
, you see high training accuracy and low test accuracy, a gap that signals something's wrong. With leakage, both training and test metrics can be inflated at the same time, so the evaluation loop itself is compromised.
Target leakage
A feature in your dataset contains information that's only knowable
after
the outcome has occurred. Think of including minutes_late when predicting is_late, or adding refund_amount to a churn model. Refunds happen because the customer already churned.
The model learns to read the answer key instead of solving the problem. Because the leaking feature exists in both your training and test splits, evaluation scores can look great. There's no train/test gap to tip you off. The failure only surfaces in production, where that feature genuinely doesn't exist at prediction time.
Train-test contamination
Preprocessing steps that need to be fit on data, like
scalers
and encoders, get applied to the entire dataset before the split. Your test set is supposed to simulate unseen production data. When its statistical properties have already been baked into your training pipeline, it can't do that job.
As the docs put it directly: "Feature selection should only use the training data. Including the test data in feature selection will optimistically bias your model."
Temporal leakage
For time-ordered data, a random train/test split places future observations in the training set and past observations in the test set. The model learns to predict the past using the future, the inverse of what it'll need to do in production.
This form is especially sneaky.
Stanford research
warns that when data is highly autocorrelated, random splitting can mask problems such as temporal leakage and lead to overly optimistic evaluation results. The model appears to generalize because autocorrelated values genuinely are similar across time. In production, though, it must predict forward, not interpolate within a known range.
The confidently wrong model problem
The performance cliff from leakage isn't subtle. Documented cases show models going from strong offline metrics to significantly degraded real-world performance:
A
sepsis review
found that a validation study of the Epic Sepsis Model found AUC dropping from about 0.76 in the developer's internal validation reports to 0.63 in external validation, but published studies do not report that approximately 40% of predictive features were missingness indicators rather than clinical values or that this explained the performance drop.
A
civil war study
found leakage errors in 4 of 12 published papers; after correcting these errors, machine learning models did not perform substantively better than logistic regression, and in the Wang paper the difference in AUC between ML and logistic regression dropped from 0.14 to 0.015. Ninety-three percent of the complex model's claimed advantage was a leakage artifact. All four papers had passed peer review at top journals.
In fraud detection,
before-split preprocessing
, including before-split normalization, produced accuracy of 0.996 and precision of 0.996 while masking recall of just 0.80. The headline metrics looked near-perfect. The model was missing one in five fraudulent transactions.
These cases aren't outliers. A
Kapoor and Narayanan review
found data leakage affecting 294 published papers across 17 scientific fields, with corrected results often comparable to simpler models. Taken together, they show how easily leakage can survive standard evaluation and still look convincing on paper.
Catching leakage during EDA, before it compounds
The cheapest place to catch leakage is during
exploratory data analysis
, before you've trained anything.
Start by
split before exploration
. In practice, EDA should operate exclusively on X_train and y_train. If you're computing correlations or running baseline models on the full dataset, you've already introduced the conditions for contamination.
A few signals should make you pause.
Suspiciously high feature-target correlation.
Any feature approaching perfect correlation with the target deserves scrutiny. Ask a causal question: would this value realistically be available at prediction time?
mutual_info_classif
can also surface nonlinear dependencies that simple correlation measures miss.
Near-perfect accuracy on a naive baseline.
If a logistic regression or shallow decision tree achieves accuracy far exceeding what you'd expect from the domain, before any hyperparameter tuning, that's a red flag worth investigating, not celebrating. As
IBM docs
note, significantly higher accuracy than expected is one of the primary warning signs.
One feature dominating importance scores.
Fit an extremely shallow decision tree (max_depth=2) and check whether a single feature captures a disproportionate share of importance. If one feature is doing nearly all the work in a two-level tree, it's often a proxy for the label itself.
Differential null rates by target class.
In medical datasets, a diagnostic test field might be null only for non-diseased patients, because the test was only ordered when disease was suspected. The null pattern can encode the label directly through missingness structure.
Null rates by class
is a fast way to surface that pattern.
Features with timestamps after the target event.
If a feature's timestamp is later than the event you're predicting, something is wrong.
These checks aren't exotic. They're the kind of exploratory work that belongs in any well-documented notebook, and they stay most useful when they're connected to the modeling pipeline they're meant to protect.
Where pipeline decisions introduce leakage
Beyond EDA, several common pipeline decisions introduce leakage through how the pipeline prepares data, not through the features themselves.
Preprocessing before the split.
This is the most common structural mistake. When you call scaler.fit_transform(X) on your full dataset before splitting, the scaler computes its statistics using test rows. Every scaled training value now carries a fingerprint of the test set's distribution. The fix is wrapping these steps inside a
scikit-learn Pipeline
, which ensures preprocessing is fit only on each training fold during cross-validation.
Random splits on time-series data.
The default train_test_split() shuffles data randomly. For sequential data, this means your model can train on January records and validate on December records from the same year, learning temporal patterns it could never access in production.
TimeSeriesSplit
enforces chronological ordering, and its gap parameter adds a buffer between folds to prevent lookback features from spanning the boundary.
Group overlap in cross-validation.
When your data contains natural groups, patients, users, geographic regions, standard KFold can place the same entity in both training and validation folds. The model memorizes individual-level patterns and exploits them at validation time.
Cross-validation guide
explains: "If the model is flexible enough to learn from highly person specific features it could fail to generalize to new subjects." GroupKFold and StratifiedGroupKFold enforce clean entity separation.
AI-generated code as a new leakage vector
AI coding assistants have made ML pipelines faster to build. They've also introduced a new category of leakage risk that's harder for you to audit than hand-written code.
Perry et al.
and the additional research cited for this article describe a pattern that's relevant here: LLMs generate code that is syntactically plausible, follow statistically common patterns, and can increase user confidence in flawed outputs. In ML workflows, that makes preprocessing-before-split, default random splitting, and target-correlated feature suggestions easier to introduce and easier to miss.
The difference between leaky and clean code often comes down to a single WHERE clause:
-- AI-generated (leaky): aggregates all history including post-prediction data
SELECT user_id, AVG(purchase_amount) AS avg_purchase
FROM transactions
GROUP BY user_id
-- Correct: bounded by prediction cutoff
SELECT user_id, AVG(purchase_amount) AS avg_purchase
FROM transactions
WHERE transaction_date < prediction_date
GROUP BY user_id
The same research found that developers using AI assistants produced code with more vulnerabilities and displayed greater confidence in the security of that code. That confidence-competence inversion is particularly dangerous for ML pipelines, where the distance between a leaky and correct pipeline is often a single line of code. In Hex,
Notebook Agent
helps technical users generate and edit SQL and Python in the notebook environment, which makes that generated work easier to inspect rather than treat as a black box.
AI coding tools increase the need for human review of generated pipelines.
According to
industry research
, data trust is the number-one concern around AI adoption, cited nearly twice as much as any other concern.
Making leakage prevention a team habit
Checklists are the intuitive answer to leakage prevention, but research suggests they're structurally insufficient.
Princeton research
developed model info sheets inspired by model cards to address data leakage, rather than stating that standard checklists and model cards do not address leakage.
What works better is making the analysis itself inspectable.
Reproducible, versioned pipelines
are the prerequisite. When a reviewer can open the exact notebook, see the exact data transformations, and re-run the pipeline, they can verify data flow rather than read a description of it. As a
Data Science Journal study
explains, team members develop implicit knowledge during a project that makes leaky patterns feel normal. A second reviewer without that context asks the questions that stopped being asked.
Code review as a first-class ML practice
catches the specific issues checklists can't. A review heuristic that takes minutes is to run feature importance charts and check whether any single feature carries anomalously high weight. If it does, investigate whether it's a proxy for the label. This check is only possible when the pipeline is reproducible and artifacts are shared.
Shared feature libraries
reduce the surface area for independently reproduced leakage patterns. When feature engineering logic lives in a reviewed, versioned library rather than scattered across individual notebooks, a leakage-prone pattern gets caught once and stays fixed. This played out at
Figma's analytics team
, where the research team built reusable components with predefined logic that ensured consistency across teams' calculations, a pattern that can also support feature engineering by centralizing definitions.
Temporal validation as the team default
forces the question of what data would genuinely be available at prediction time. Making chronological splitting the enforced convention, not a per-project decision, means your team defines the temporal boundary explicitly before feature engineering begins.
Visibility ties these practices together. When analysis lives in a
data collaboration
environment like Hex, where SQL, Python, and visualizations share one versioned environment, a second set of eyes can inspect the actual pipeline before it ships. For technical users working in that environment, Notebook Agent helps generate and refine SQL and Python while keeping the analysis inspectable for review. Hex brings
AI capabilities
to data analysis. Anyone can explore data using natural language, with or without code, all on trusted context, in one AI analytics environment.
Build models you can trust in production
Feature leakage thrives when pipelines are fragmented, when preprocessing decisions happen in isolation, and when evaluation metrics are the only quality signal anyone checks.
Target leakage, train-test contamination, and temporal leakage are commonly discussed forms of data leakage, each of which can lead to overly optimistic model evaluation. They inflate both training and test metrics at the same time, defeating the standard diagnostic for model quality. A low-cost early intervention is EDA on properly split data, where suspiciously high correlations and dominant features can surface before they compound into false confidence. The most durable intervention is a reproducible, reviewable pipeline, because a second set of eyes catches what the original author has normalized.
As AI coding tools accelerate pipeline development, the gap between writing code and understanding code widens. A generated pipeline that looks correct and produces strong metrics can still encode leakage invisible to automated checks. Inspectable, collaborative workflows matter more now because the speed these tools enable can outpace the scrutiny that leakage demands.
The fix is a
data science workflow
where the work is reproducible, the analysis is documented, and a reviewer can see exactly how data flows from raw features to model predictions. Hex brings that workflow together: SQL, Python, and collaboration in one place, so the exploratory work that catches leakage stays connected to the modeling work it protects. When your analysis is visible by default, leakage has fewer places to hide.
Sign up for a free account
or
request a demo
to see how it works.
Frequently Asked Questions
How do I tell the difference between a genuinely strong feature and one that's leaking target information?
Ask a causal question: would this feature's value be known at the exact moment you need to make a prediction in production? Leakage features are different from legitimately predictive ones because they encode the outcome itself, either directly or through a proxy that only exists after the event. If you can't confidently explain how a production system would populate that feature before inference time, treat it as suspicious. Running a shallow decision tree and checking whether a single feature dominates importance is a fast diagnostic. If one feature is doing all the work, investigate its temporal and causal relationship to the target before trusting it.
Does using scikit-learn's Pipeline completely eliminate the risk of feature leakage?
Pipelines solve one important category of leakage. They ensure preprocessing steps like scaling, imputation, and feature selection are fit only on training data during cross-validation. But they don't address target leakage, because a feature that encodes the label will still be present in both splits, temporal leakage, where you need a time-aware splitter like TimeSeriesSplit, or group overlap, where you need GroupKFold. Pipelines are a structural defense against train-test contamination specifically. For the full picture, you also need to audit your features for causal validity, use appropriate cross-validation splitters for your data's structure, and have a second reviewer inspect the pipeline logic. Tools like Hex's collaborative notebook environment make that review easier, and Notebook Agent can help technical users generate and edit SQL and Python while keeping the full pipeline, SQL, Python, and visualizations, in one inspectable, versioned environment.
What should I do if I suspect leakage in a model that's already in production?
Start by comparing your production metrics against the validation metrics from development. A large gap between performance on the training set and the test set is a common signature of data leakage. Then work backward: audit your feature set for values that wouldn't be available at prediction time, check whether preprocessing was fit on the full dataset, and verify that your train/test split respected temporal ordering if your data has a time component. If you confirm leakage, retrain without the offending features or pipeline steps and re-evaluate on a properly held-out set. Document what happened and why, so your team learns from it. The
Kapoor and Narayanan review
found leakage in 294 published papers across 17 fields, so if it happened to you, you're in plenty of company.
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
