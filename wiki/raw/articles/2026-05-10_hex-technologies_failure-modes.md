---
title: "Machine Learning Failure Modes: Why Production Models Break | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/failure-modes/"
scraped: "2026-05-10T01:28:57.331096+00:00"
lastmod: "2026-01-30"
type: "sitemap"
---

# Machine Learning Failure Modes: Why Production Models Break | Hex 

**Source**: [https://hex.tech/blog/failure-modes/](https://hex.tech/blog/failure-modes/)

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
Failure modes in machine learning: why production models break and how to prevent it
Most ML failures aren't model failures. The model is usually fine — it's the data it trained on, the shortcuts it learned, and the organizational gaps that let both go undetected.
The Hex Team
Data
January 30, 2026
Share:
twitter
linkedin
In this article
What makes ML failure different from software bugs
Data issues and how to catch them early
Shortcut learning and how to test for it
System complexity and how to reduce it
Organizational failures multiply technical ones
Putting it together
Get started for free
You've watched it happen: a model that crushed every metric in development completely falls apart in production. The validation curves looked great, the stakeholders were excited, and then nothing works the way it should.
If that sounds familiar, you're in good company. In a
RAND Corporation study
of AI projects in the U.S. Air Force, interviewees estimated that over 80% of AI efforts failed to reach meaningful operational deployment, roughly double the failure rate they reported for non-AI IT projects. While that study focused on a specific context, it matches what practitioners see across industries. The cause is rarely the model itself. RAND's analysis emphasizes that successful AI deployment depends far more on the surrounding architecture, processes, and organizational capabilities than on the models themselves.
Production ML failures cluster into four categories: data issues that create hidden gaps between training and reality, shortcut learning where models exploit spurious correlations, system complexity that hides failures across component boundaries, and organizational failures where governance gaps let problems compound. Understanding where your failure fits is the first step toward fixing it.
What makes ML failure different from software bugs
Traditional software fails in ways you can see. Null pointer exceptions. Race conditions. Memory leaks. You write tests, and when they pass, you have reasonable confidence the code works. ML systems fail differently. A model can produce valid outputs without any exceptions or crashes while being completely wrong. The failure is silent, statistical, and often invisible until business metrics suffer weeks later.
Your usual engineering instincts don't transfer cleanly. Code review catches logic errors; it doesn't catch a model that learned to predict loan defaults based on zip code correlations that won't hold next quarter. Unit tests verify expected outputs; they can't verify that your model learned the right features rather than spurious shortcuts. The failure surface is different in kind, not just degree.
Data issues and how to catch them early
Industry research and practitioner reports consistently point to data quality as the dominant cause of production ML failures, often outweighing model architecture or hyperparameter choices by a wide margin. Data issues break models by creating hidden gaps between what you trained on and what you're actually seeing in production. Three patterns show up repeatedly.
Data leakage inflates your metrics
Data leakage happens when information that wouldn't be available at prediction time sneaks into your training data. Your model learns to exploit it, your validation metrics look incredible, and then everything falls apart in production when that information isn't there.
Peer-reviewed research
published in
Patterns
examined hundreds of ML-based scientific papers and found data leakage everywhere. Target leakage embeds the answer in features. Train-test contamination lets test data bleed into training. Temporal leakage uses future information to predict the past.
The frustrating part: leaked models often hit near-perfect validation scores. Everything looks great until you deploy.
Data drift erodes performance over time
Production data changes. Customer behavior shifts, market conditions evolve, and the patterns your model learned six months ago may not apply anymore.
Chip Huyen
points out something important: a large percentage of what looks like data drift on your monitoring dashboards is actually caused by internal errors. Pipeline bugs. Missing values filled in wrong. Inconsistencies between how you extracted features during training versus inference. Before you retrain, check whether your pipeline is broken. It often is.
Zillow's home-buying business is the cautionary tale everyone knows. The company experienced model failures contributing to losses exceeding $500 million, ultimately forcing them to shut down Zillow Offers. Many post-mortems have argued that rapid market changes outpaced their valuation models, a classic case of concept drift. In safety-critical domains like medical diagnosis or autonomous vehicles, the same failure mode carries even higher stakes.
Label errors compound over time
MIT researchers
found pervasive label errors in benchmark datasets like ImageNet and CIFAR-10. When they corrected the errors, larger models actually performed
worse
than smaller ones because the high-capacity models had learned to reproduce the annotation mistakes rather than the underlying reality.
If well-resourced benchmark curation produces label errors, your internal labeling process almost certainly does too. This isn't a criticism; it's just the reality of working with labeled data at scale.
How to catch data issues early
You can monitor for data problems before they tank your metrics.
Domino Data Lab notes
that tracking input data distributions is one of the most effective ways to catch model degradation early. Unlike performance metrics that need ground truth labels (which you often don't have for weeks), drift detection works on live production data.
The standard statistical tests each have tradeoffs you should know about. Kolmogorov-Smirnov works well for continuous features but struggles with high-cardinality categoricals. Population Stability Index (PSI) is interpretable but forces you to make binning decisions. Jensen-Shannon Divergence handles probability distributions elegantly but can fire false positives on minor shifts. Most teams run multiple tests and alert on consensus, which cuts down on alert fatigue while still catching real problems.
Libraries like Evidently, WhyLabs, and Great Expectations give you production-ready implementations. The hard part isn't picking a test; it's setting thresholds that catch real issues without waking you up at 3am for nothing.
For leakage, you prevent it earlier, during feature engineering and validation design. Use temporal validation (train only on past data, validate on future). Audit your features by asking "would I actually have this information at prediction time?" And keep your training and test pipelines strictly separated.
Uber built
D3
, an automated drift detection system for their Michelangelo platform. When you're serving millions of predictions across thousands of models, manual monitoring isn't realistic.
Shortcut learning and how to test for it
Even with clean data, your model can learn the wrong things. Neural networks optimize for minimal training loss, which means they'll latch onto whatever features are easiest to extract, regardless of whether those features actually mean anything.
Research on ArXiv
shows that when spurious features correlate strongly with labels and are easy to learn, models will prioritize them over genuinely predictive features.
The classic example: a model trained to identify tanks that actually learned to detect cloudy weather, because all the tank photos happened to be taken on overcast days. It passed validation (same spurious correlation in the test set) and failed completely in production.
This isn't hypothetical. The
Failed-ML repository
documents real cases like Genderify, an AI tool for identifying gender from names and emails that was shut down because it had learned shortcuts that worked on its training data but broke on real-world diversity.
Why your validation set won't save you
Standard practice is holding out part of your data for validation. But if your validation set has the same spurious correlations as your training set, which it usually does, you won't catch shortcut learning until production.
NeurIPS 2023 research
found that dataset composition matters far more than architecture choices for this problem. You can't architecture your way out of bad data.
How to actually test for shortcuts
The most practical metric is worst-group-accuracy: the minimum accuracy across subgroups of your test samples. If your model does great on average but terrible on specific subgroups, it's probably exploiting shortcuts.
A few advanced techniques attack the root cause. Counterfactual data augmentation creates training examples that break spurious correlations, like tanks in sunshine and hospitals without blue scrubs. Invariant risk minimization penalizes reliance on features that don't generalize across environments. Group distributionally robust optimization explicitly optimizes for worst-group performance. These take more work to implement, but they're worth it when standard validation keeps missing problems.
You can also stress test deliberately. Build validation sets that break expected correlations. Financial transactions from unusual geographies. Medical images from different equipment. User behavior from different demographics. If performance craters on these out-of-distribution samples, you've found your shortcuts.
System complexity and how to reduce it
Google's paper on technical debt
made a point that's still underappreciated: ML code is a tiny fraction of a real ML system. The surrounding infrastructure creates most of the complexity and most of the failure surface. Data pipelines, feature stores, monitoring, deployment. It all adds up.
Data dependencies create invisible coupling
Data dependencies are harder to spot than code dependencies, and they break in more insidious ways. When your model consumes signals from another system, silent degradation can happen when that upstream system changes, even if the interface contract still looks satisfied.
The CACE principle from Google's research captures this: Changing Anything Changes Everything. In traditional software, you can make isolated changes with predictable effects. ML systems don't work that way. Tweaking regularization, changing sampling rates, or modifying feature encoding can ripple unpredictably. Improving one metric can degrade another.
Pipeline jungles make debugging impossible
Data pipelines that evolve organically become "pipeline jungles," tangles of scrapes, joins, and sampling steps that nobody fully understands anymore. Configuration sprawl makes things worse. Feature flags, hyperparameter files, and algorithm choices end up scattered across systems, creating failure modes that code review will never catch.
How to reduce system complexity
Start by documenting your data lineage aggressively. Every model should have clear records of upstream dependencies and downstream consumers. When model outputs get used without documentation (undeclared consumers), you end up breaking three other teams' workflows every time you make an improvement. Nobody knows until their metrics tank.
Model registries provide version control for models, giving you reproducibility, rollback capability, and baseline comparisons for detecting degradation. The handoff between development and deployment is where context gets lost; registries help preserve it.
Finally, design for graceful degradation. Production ML systems need the same operational patterns as other critical infrastructure. Circuit breakers fall back to simpler models when the primary fails. Kill switches disable predictions entirely when needed. Canary rollouts limit blast radius. Automated rollback kicks in when metrics degrade.
Teams that work in a
unified workspace
where analysis, monitoring, and collaboration happen together tend to catch dependency issues before they break things downstream. When your data scientists and analysts are scattered across disconnected tools, nobody has visibility into who depends on what, and every change carries unknown risk.
Organizational failures multiply technical ones
Technical failures don't happen in isolation. Industry surveys and post-mortems consistently find that failed AI projects lacked clear ownership, defined success metrics, or cross-team transparency. Companies with well-governed,
centralized data
are better positioned to scale AI initiatives because teams can actually trust and reuse shared assets.
The organizational failure modes are predictable. Nobody owns the model post-deployment. Policies exist on paper but the tooling makes compliance painful. You're optimizing for model accuracy while the business cares about revenue. The person who built it left, and nobody knows how it works.
These failures multiply the technical ones. When monitoring notebooks live alongside the analysis that built the model — shared, versioned, and visible to the whole team — ownership gaps get caught earlier.
Data science workflows
that keep build and monitor in the same environment make the "nobody's watching this" failure mode structurally harder. Data drift becomes catastrophic when nobody's monitoring. Shortcut learning goes undetected when the team that built the model isn't the team that validates it. System complexity compounds when org boundaries block visibility.
So, how do we fix this?
The fix requires ownership clarity, aligned incentives, and tooling that makes good practices the path of least resistance. When setting up drift monitoring means spinning up a separate infrastructure project, it won't happen. When it's a scheduled notebook running alongside the analysis that built the model, it will.
Organizations should also resist the temptation to jump straight to full automation. At Level 0 (manual processes), you run models locally, deploy ad hoc, and monitor reactively; problems only surface when business metrics suffer. At Level 1, continuous training pipelines retrain on fresh data, modular components allow targeted fixes, and basic monitoring catches drift.
Neptune.ai notes
that the goal at this stage is to perform continuous training by automating the ML pipeline. At Level 2, end-to-end CI/CD (continuous integration and deployment) pipelines deploy validated models with canary rollouts and automated rollback. Teams that skip stages build fragile systems. For most teams, getting from manual to robust automation takes a year or more of sustained investment.
Putting it together
The failure modes here cause real losses, from Zillow's $500 million to countless smaller failures that never make headlines. But most are preventable.
Data issues are the dominant cause; catch them with drift detection and temporal validation. Shortcut learning defeats standard validation; catch it with worst-group-accuracy and stress testing. System complexity hides failures; reduce it with lineage documentation and graceful degradation. Organizational gaps multiply everything else; address them with ownership clarity, aligned incentives, and progressive automation.
High failure rates aren't destiny. They're what happens when teams focus on models while ignoring everything around them. When you flip that equation, treating data quality, system architecture, and organizational process as primary concerns, you dramatically improve your odds of building models that not only reach production but stay reliable over time.
Ready to build more reliable ML workflows?
Get started with Hex
or
request a demo
.
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
