---
title: "Introducing The Specialized Intelligence Index"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/introducing-the-specialized-intelligence-index"
scraped: "2026-09-23T06:00:04.951185+00:00"
lastmod: "2026-09-23T03:29:53.000Z"
type: "sitemap"
---

# Introducing The Specialized Intelligence Index

**Source**: [https://fireworks.ai/blog/introducing-the-specialized-intelligence-index](https://fireworks.ai/blog/introducing-the-specialized-intelligence-index)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Introducing The Specialized Intelligence Index
Introducing The Specialized Intelligence Index
PUBLISHED
9/22/2026
Table of Contents
The measure of real work
Developed by practitioners, for practitioners
SII highlights at a glance
Healthcare
Legal
Finance
Cybersecurity
Customer Support
Productivity
Software
Methodology overview
Contribute a benchmark or a model
Table of Contents
Define AI performance in your industry
Join the index
Table of Contents
The measure of real work
Developed by practitioners, for practitioners
SII highlights at a glance
Healthcare
Legal
Finance
Cybersecurity
Customer Support
Productivity
Software
Methodology overview
Contribute a benchmark or a model
Table of Contents
Define AI performance in your industry
Join the index
The
Specialized Intelligence Index (SII)
is your one-stop destination to explore the performance of open, closed, and specialized models on domain-specific benchmarks. Each benchmark reflects real-world tasks designed by practitioners. Today, we are launching benchmarks in seven initial domains: healthcare, legal, cybersecurity, finance, customer support, productivity, and software. More are coming soon.
The measure of real work
Public benchmarks provide common reference points for tracking progress and comparing models, but they are not a good measure of real work. These evals use bounded tasks, fixed datasets, and standardized scoring. Real work is messier. It involves incomplete information, changing scope, business constraints, complex judgment calls, multi-step workflows, and collaboration.
This distinction matters for organizations seeking to determine if a model is good enough to automate human tasks. An acceptable result must satisfy the standards of real people responsible for real outcomes. Earlier this year,
METR
quantified the difference. In their work, 4 maintainers reviewed 296 AI-generated pull requests (PRs) from 3 SWE-bench Verified repositories. Maintainer acceptance scores averaged 24.2 percentage points below automated benchmark scores. In their own words: “many SWE-bench-passing PRs would not be merged into main.”
To apply benchmarks to real work, we need to establish what a score measures, how closely the evaluation reflects the intended work, and whether better performance produces a useful operational result.
Does the test measure the capability it claims?
This is a question of construct validity: whether the evaluation supports the interpretation attached to its score.
Bean and colleagues
examined 445 LLM benchmarks and identified recurring gaps between the phenomena researchers intended to measure, their tasks, and their scoring methods. For example, a task intended to measure reasoning may also depend on memorized knowledge. This makes it difficult to determine whether a high score reflects reasoning, recall, or both.
Does the test represent the work we care about?
Representativeness concerns the coverage and composition of the task set.
Wang and colleagues
studied 43 agent benchmarks and found a concentration in computer and mathematical work, a category accounting for 7.6% of U.S. employment in their analysis. Management and legal work were underrepresented, as were interpersonal skills common across occupations. Real-work benchmarks must represent their intended domain.
Evaluating models on real work then follows a logical progression, with each step requiring more evidence:
Benchmark score → Capability claim → Business outcome
The score records performance on a defined task set under a specified protocol. A capability claim requires evidence that the system can perform the relevant class of work reliably, including on unfamiliar cases. A business outcome requires evidence that this performance delivers the desired result at acceptable quality and cost.
Three benchmarks across Software, Customer Support, and Finance.
Visit the SII
to explore the scores.
Developed by practitioners, for practitioners
Real-work evals are defined by practitioners who help outline the work, the constraints, and the conditions for acceptance. Designing real-work evals generally involves these steps:
1. Define the job and its value.
Specify the task, intended users, and level of human oversight. Set quality thresholds and time and cost limits. Establish a baseline for the current workflow, then test whether score improvements predict better outcomes in a pilot or controlled deployment.
2. Reflect the work.
Sample routine tasks and difficult cases from the intended setting. Include realistic information, tools, permissions, and policy constraints. Add stress tests for consequential failures, but report them separately when their frequency differs from normal usage. A deliberately difficult test set should not be presented as an estimate of everyday performance.
3. Set acceptance criteria with practitioners.
Translate professional standards into observable outcomes and explicit rubrics. Distinguish minor defects from failures that make an output unacceptable. Evaluate both the final result and any actions that matter, such as seeking approval before changing a protected resource.
4. Validate the grader.
Compare automated judgments with expert review. Examine false acceptances, false rejections, and disagreements among reviewers. Refine the rubric or grading method where those differences reveal ambiguity. Continue sampling outputs for expert review as the system changes.
5. Test generalization and reliability.
Keep development and held-out cases separate, check for contamination, and refresh the evaluation as the work changes. Repeat runs and report uncertainty, performance by task category, and critical failure rates. Record the model, prompts, agent harness, tools, resource limits, and grader version so comparisons remain interpretable.
SII highlights at a glance
Healthcare
Doximity’s BedsideBench v0.2.0
evaluates frontier AI models across 500 physician-validated clinical cases spanning medical reasoning, calculations, drug safety, guideline adherence, hallucination, diagnostic safety, and treatment planning.
Mercor’s APEX-1: General Practitioner (MD) Benchmark
measures how well frontier AI models perform on real primary care physician tasks in diagnosis, workup, and safe escalation.
HealthBench Professional
evaluates whether frontier AI models can provide accurate, useful, and safe responses to challenging clinician-authored tasks.
Legal
Harvey's Legal Agent Benchmark (LAB)
measures how well frontier AI models perform on real legal work across 24 practice areas, requiring them to navigate files and produce work products graded against expert rubrics for factual accuracy, legal analysis, and format.
Harvey’s LAB Contracts
tests whether AI agents can move contract negotiations forward across 500 drafting, review, and negotiation tasks. To successfully complete each task, agents must address all changes and open issues to advance the contract within the constraints of the business and deal.
Mercor’s APEX Agents: Corporate Law
assesses multi-step corporate-law assignments that encompass chain tool use, retrieval, and document drafting. Practicing corporate attorneys grade the output against the work product a firm would accept.
RedlineBench
evaluates realistic, multi-turn contract redlining by an AI agent acting as in-house counsel.
Finance
Rogo’s Big Finance Bench
assesses AI agents on questions spanning valuation models, financial-statement analysis, forecasting, and other critical finance workflows, with practitioner-written rubrics grading how agents find information, apply financial definitions and citations, and perform calculations.
Cybersecurity
depthfirst dfbench v1
targets defensive security across vulnerability detection, validation, and differential analysis. depthfirst's own dfs-large1 model, post-trained with Fireworks on a GLM 5.2 base using RL, achieved a new Pareto frontier in its evaluations. The model’s improvements are attributed to RL reward shaping with an effort penalty, a soft finding-budget penalty, and joint training on vulnerability detection and validation. This result is reported by
depthfirst
.
Novee’s PWNBench-v0.1
evaluates frontier AI models on agentic greybox pentesting of live web applications, covering the full discover–exploit–report workflow. It measures recall, precision, F0.5, and API cost under a shared thin harness.
Customer Support
Decagon’s DuetBench-Diagnosis
replays real Duet customer-support investigations and rates model responses head to head across outcome, investigation, tool use, and communication.
Sierra’s τ-Banking
evaluates customer-support agents on banking tasks that require searching a 698-document knowledge base across 21 product categories, applying policies, and executing multi-step tool calls while managing an ongoing customer conversation.
Sierra’s τ-Voice
evaluates whether voice agents can complete customer service tasks across retail, airlines, and telecom while handling interruptions, background noise, and diverse accents.
Productivity
Genspark Slides Benchmark
evaluates AI-generated presentations on de-identified real user tasks, scoring the finished deck on task completion, content quality, visual design, and process quality, with penalties for layout defects, fabricated content, and ignored instructions.
Software
Traversal’s ORCA-Bench
is a site reliability engineering benchmark that evaluates production-style root-cause analysis (RCA) from ambiguous reports, telemetry, and source code. Hard RCA accuracy is the headline score; Medium RCA and incident hallucination remain separate native metrics.
Proximal’s FrontierSWE V2
is a code generation benchmark that evaluates 34 software-engineering tasks at the edge of what an expert human can do: writing a flight-sim renderer in OpenGL, porting Git to Zig, driving a racing bot from vision alone. Each model gets 5 trials per task and up to 20 hours per trial. Every trial earns a graded reward rather than a pass or a fail, so a run that gets most of the way there still counts.
Mercor’s APEX-SWE
evaluates AI models on 200 software-engineering tasks that require integrating cloud services and business applications or debugging production failures using logs, dashboards, and incomplete context.
Datacurve’s DeepSWE v1.1
evaluates coding agents on 113 original, long-horizon engineering tasks across 91 repositories and five languages, testing their committed code for correct behavior in an isolated environment.
Macroscope's MacroscopeBench
evaluates models’ performance at code review, measuring the reviewer’s ability to detect real known bugs while not posting incorrect comments. It runs over 195 commits from open-source repositories, 144 that introduced a real bug maintainers later had to fix, and 51 clean controls.
Training an open model can deliver better results including: higher pass rates, lower cost per task, and/or lower task duration. Results from Doximity, depthfirst, and Genspark on their specialized intelligence.
Methodology overview
No artificial rollup.
SII does not average ranks, weight quality against cost or duration, or produce a cross-domain composite. Results remain at the benchmark and domain level, with coverage matrices and score-versus-cost and score-versus-duration views so users can apply their own tradeoffs.
Source.
Benchmark results may be reported across models by a partner, Fireworks, or a combination of both; implementation is defined or linked accordingly. Publication follows the benchmark owner’s policy; scores are published, while eval sets, prompts, grading logic, trajectories, and raw partner outputs remain private unless the owner chooses otherwise.
Reproducibility.
Each benchmark is labeled by who can reproduce it: anyone, Fireworks and the benchmark owner, or the partner only. Reproducibility comes from the versioned methodology and pinned execution snapshot, which record the harness, sampling parameters, timeouts, snapshot IDs, executor, and any open issues.
Model selection.
Models are selected based on whether an organization could plausibly deploy them at production scale, with price as a key consideration. New frontier models automatically enter the qualification pipeline and appear on the Index only after they pass this bar.
For further details on the harness, inference, sandbox, run protocol, confidence, reliability, and cost and duration metrics,
visit Fireworks Methodology
.
Contribute a benchmark or a model
If you run a production eval for a specific domain, it may belong on the Index. Fireworks Lab helps organizations design their own benchmarks and specialized models.
To submit to the Index, partners provide tasks and data in a Harbor-compatible format. Fireworks reviews task diversity and calibration, requests and runs the eval across a model roster at no cost, and publishes scores with the partner’s approval.
Visit the Specialized Intelligence Index →
Related Posts
Company News
8/31/2026
Train past the frontier: Training API now generally available
Company News
7/15/2026
Announcing our Series D and $1B ARR
Company News
4/6/2026
Own Your AI: Fireworks Training Preview
Next
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
Introducing The Specialized Intelligence Index
