---
title: "What Is Underfitting in Machine Learning?"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/what-is-underfitting/"
scraped: "2026-06-23T06:00:32.609634+00:00"
lastmod: "2026-05-21"
type: "sitemap"
---

# What Is Underfitting in Machine Learning?

**Source**: [https://hex.tech/blog/what-is-underfitting/](https://hex.tech/blog/what-is-underfitting/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
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
What is underfitting in machine learning?
High training error that won't budge no matter how much data you add is a sign, but most teams don't recognize it until weeks of wasted iteration have already passed.
The Hex Team
Data
May 21, 2026
Share:
twitter
linkedin
In this article
What underfitting looks like in practice
The bias-variance tradeoff: where does your model sit?
Why underfitting is harder to catch than overfitting
The iteration loop and where it breaks down
When AI analytics meets an underfit model
Fixing underfitting often exposes overfitting, and that's the actual job
The work is the diagnosis
Frequently Asked Questions
Get started for free
You train a model, check the metrics, and the numbers look mediocre. Training error is high, validation error is high, and the gap between them is small, which can look reassuring at first. So you collect more data, retrain, and get basically the same result. Weeks go by before someone states the uncomfortable possibility that the model was never capable of learning this pattern in the first place.
That's underfitting. It's one of the most common failure modes in machine learning, and it's easy to miss. This article explains what underfitting is, how to diagnose it with the bias-variance tradeoff, why teams miss it, and what fixing it looks like in practice.
What underfitting looks like in practice
Underfitting occurs when a model hasn't learned the relevant patterns in the training data, so it performs poorly on both training and test sets. The model fails to capture signal that's actually there, rather than memorizing noise.
The technical term is high bias. The model makes systematically wrong assumptions about the data's structure, and those errors show up consistently regardless of which training sample you use.
A concrete example: fit a straight line to data that follows a curve. A line can't represent a curved relationship, so the model misses the pattern entirely. A common polynomial regression illustration shows the same thing: moving from a linear model to a higher-degree polynomial can substantially reduce MSE on the same dataset. The original model never had a chance.
This shows up in less obvious ways, too. A regression model trained to predict house prices using only the number of rooms, while price is actually driven by size, location, age, and amenities, will systematically fail. The limiting factor is the feature set, not the data volume.
Common causes:
Model too simple for the data's structure.
A linear model can miss nonlinear relationships, and a shallow neural network can fall short on a task that needs hierarchical feature learning.
Excessive regularization.
L1/L2 penalties or dropout cranked up to prevent overfitting can over-constrain the model until it can't fit even the training data.
Insufficient training.
Too few epochs or a learning rate so low the optimizer barely moves can leave a model stuck before it learns much.
Wrong or missing features.
Missing predictive inputs mean no amount of model complexity recovers the signal.
Across these cases, the same pattern keeps showing up: high training error, high test error, and a small gap between them. If that pattern holds, you're likely looking at underfitting.
The bias-variance tradeoff: where does your model sit?
The bias-variance tradeoff places underfitting at the low-complexity end of the spectrum, with high bias and low variance. Total prediction error breaks into three components: irreducible noise (which no model can eliminate), bias (how far the model's average prediction deviates from truth), and variance (how much predictions fluctuate across different training sets). As you increase model complexity, bias falls and variance rises. They can't both be minimized by adjusting complexity alone.
You can see this most clearly in learning curves, which plot training and validation error as a function of training set size:
Checking whether training error is high before doing anything else saves a lot of wasted effort.
Why underfitting is harder to catch than overfitting
Underfitting is harder to catch because you can only confirm it by comparison. You need to know what a better model could achieve. Overfitting announces itself through a visible train/validation gap in a single model. Underfitting needs either domain knowledge, an external benchmark, or deliberately trying more capable alternatives. A team that never explores higher-capacity models has no reference point from which to recognize their model is underperforming.
This creates a few persistent anti-patterns.
"We just need more data."
When both training and validation error are high, the reflexive response is to collect more data. But the learning curve for an underfitting model shows both curves plateauing at high error regardless of data volume. More data is the right lever for variance problems, not bias problems.
Cycling through algorithms without auditing features.
Teams swap linear models for tree ensembles for neural networks, watching for improvement that never comes, because the feature matrix itself lacks the information needed to make accurate predictions. Model design and feature design each shape whether a model underfits. Swapping one without examining the other wastes time.
Anchoring to an underfit baseline.
When an early model establishes a performance reference, all subsequent progress is measured against it. If that baseline is severely underfitting, the team implicitly accepts a low ceiling.
A useful diagnostic technique: deliberately try to overfit. Strip all regularization, train a high-capacity model on a small data subset, and see if it can achieve near-zero training loss. If the model can't overfit a tiny unregularized dataset, focus on the architecture, loss function, or data pipeline before spending any time on data quantity.
The iteration loop and where it breaks down
Fixing underfitting usually starts with capacity, then regularization, then features. The order matters because each step addresses a different root cause, and jumping ahead wastes time.
Increase model capacity.
More layers, more neurons, higher polynomial degree, a more expressive algorithm family. Additional training epochs won't help if the model is structurally too simple.
Reduce regularization.
If L1/L2 penalties or dropout are too aggressive, the model can't learn even when it has sufficient capacity. The goal is finding the λ that allows learning without overfitting.
Engineer better features.
Polynomial features, interaction terms, better categorical encoding. When capacity is sufficient but underfitting persists, the feature representation is often the bottleneck.
Improve data quality.
Clean data, augment where it makes sense, verify that training samples actually represent the patterns you're asking the model to learn.
Tune hyperparameters systematically.
Learning rate, number of epochs, architecture parameters. These are secondary to capacity and features, but they matter once structural issues are addressed.
After each step, re-run, measure training and validation loss, and compare to the previous iteration. Did training loss drop? Did validation loss drop with it, or diverge?
Reproducibility is what makes this process trustworthy. When experiments live in personal notebooks without version control, any apparent improvement might come from the code change, a different random seed, a different library version, or a different data state. There's no way to tell which.
The iteration loop works best as a shared process. When every experiment runs in a versioned,
collaborative notebook
environment, the full history of what changed and what moved stays visible to the whole team, not just the person who ran the last cell.
When AI analytics meets an underfit model
When AI analytics sits on top of an underfit model, the result is output that
looks
plausible.
An underfit model still produces structurally valid artifacts: coefficients, cluster assignments, feature importance scores. Regression coefficients come back from a linear model fit to data it can't represent. Cluster assignments come back from a k-means model with too few clusters. The numbers are formatted correctly. They're just not telling you anything real.
When an LLM receives those structurally plausible but essentially meaningless outputs, it can generate a fluent, confident interpretation, with no mechanism in this workflow to evaluate whether the numbers reflect a real pattern or a failed model. This is what makes AI analytics on top of a bad model so dangerous: the system can be confidently wrong. The confidence expressed in LLM-generated explanations directly affects how much users trust them, independent of whether the explanation is accurate.
The result is a pipeline that's wrong at the model layer and persuasive at the explanation layer, with neither failure visibly signaling the other.
Hex's
State of Data Teams
2026 report found that data trust is the top concern around AI adoption, cited by 31% of data leaders, nearly twice as much as any other barrier. That gap is felt most acutely by the practitioners who are closest to the data and responsible for the outputs it generates.
A common safeguard is to force model diagnostics into the explanation pipeline. R², RMSE, confidence intervals, train/test performance gaps: the LLM needs to see these before generating interpretation, with explicit instructions to flag when fit metrics fall below meaningful thresholds. In a collaborative notebook, Notebook Agent can generate the diagnostic code, and you can inspect and edit every step, so you verify the analytical path rather than taking a narrative at face value.
Fixing underfitting often exposes overfitting, and that's the actual job
Underfitting and overfitting are opposing forces you manage continuously.
Every action that reduces bias — adding model capacity, reducing regularization, engineering richer features — pushes you toward higher variance. The irreducible noise in any dataset sets a hard floor on total error. The work is continuous optimization of bias and variance against each other.
In practice, this looks like a pendulum. Increase model complexity to address underfitting, and training loss drops. But if validation loss starts rising while training loss continues falling, you've crossed into overfitting territory. Add regularization, which reintroduces bias, and check that you haven't regressed.
The techniques for managing this tension are well-established: learning curves plotted after every significant model change, k-fold cross-validation as a reliable evaluation signal, early stopping that halts training when validation error begins increasing, and ensemble methods that reduce variance through averaging.
One design principle that's easy to miss: individual ensemble members should lean toward overfitting individually. Their variance gets removed through averaging: that's the mechanism ensembles exploit. Tuning each member for optimal bias-variance balance before ensembling actually undercuts the approach.
The workflow is iterative: establish a baseline, diagnose the current position, increase complexity incrementally and re-diagnose, apply regularization when overfitting appears, monitor for underfitting regression. This process doesn't end at deployment. Model drift over time can pull a model toward either failure mode as the data distribution shifts.
Managing this tension is the actual job. It's a continuous diagnostic practice.
The work is the diagnosis
Underfitting is deceptive because it looks like a data problem when it's often a model or feature problem. It's harder to catch than overfitting (see
overfitting explained
for the other side of the tradeoff) because you need a reference point to recognize it's happening. And when AI layers confident explanations on top of underfit models, the failure becomes invisible to anyone who doesn't check the diagnostics.
The bias-variance tradeoff is the diagnostic frame that tells you which lever to pull. Learn to read learning curves, run deliberate overfitting tests, and audit feature information content before swapping algorithms. Then iterate, reproducibly and collaboratively, with every change tracked.
If your team does that work in a shared environment where the code, diagnostics, and results stay connected, you can trace what actually moved the needle.
Request a demo
to see how that workflow feels in practice.
Frequently Asked Questions
How do I tell the difference between underfitting and genuinely noisy data?
Both produce high error on training and test sets, which is why they're easy to confuse. The distinction comes from what happens when you increase model complexity. If a more expressive model substantially reduces training loss, the original model was underfitting, lacking the capacity to capture real patterns. If training loss barely moves even with a much more powerful model, you may be hitting the irreducible noise floor in the data. Plotting learning curves across model sizes helps you see which regime you're in. Stanford CS229's bias-variance analysis identifies noisy data as one of three distinct causes of high MSE, alongside overfitting and underfitting, treating them as separate diagnoses rather than variations of the same problem.
Can underfitting affect models in production that were performing well at launch?
Yes. This is the data drift scenario. A model that was well-calibrated at training time can drift toward either failure mode as the underlying data distribution shifts. This is why periodic re-evaluation of training and validation metrics matters post-deployment, not just during development. Teams that monitor production models for rising error on both training and holdout sets can catch this kind of regression before it compounds into downstream decision errors.
Should I always try the simplest model first, even if I suspect underfitting?
Starting simple is good practice because it gives you a known baseline against which to measure improvements. The mistake is staying simple when the evidence says you shouldn't. If your baseline model shows high training error with a flat learning curve, that's your signal to increase complexity rather than collect more data or tune hyperparameters. The baseline is the diagnostic starting point. What matters is that you document the baseline and every step after it, so you can trace which change actually moved the needle. In a collaborative notebook environment, that history stays connected to the code and results, making the progression from simple to complex legible to your future self and your teammates.
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
