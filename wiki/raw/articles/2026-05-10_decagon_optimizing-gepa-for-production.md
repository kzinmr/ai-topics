---
title: "Optimizing GEPA for production: A test-driven approach to prompt engineering"
source: "Decagon Blog"
url: "https://decagon.ai/blog/optimizing-gepa-for-production"
scraped: "2026-05-10T01:19:44.727166+00:00"
lastmod: "None"
type: "sitemap"
---

# Optimizing GEPA for production: A test-driven approach to prompt engineering

**Source**: [https://decagon.ai/blog/optimizing-gepa-for-production](https://decagon.ai/blog/optimizing-gepa-for-production)

Introducing Proactive Agents.
Learn more
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Build
AOPs
Workflows for AI agents
Integrations
Support tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & Reporting
Voice of the Customer
Watchtower
Always-on QA
Suggestions
AI-powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
AI and the next generation of customer experience
Why exceptional service is the new brand differentiator as AI reshapes consumer expectations.
Spring ’26 Release: Proactive Agents
See how user memory, outbound voice, and Agent Workbench can help you build stronger customer relationships
Company
About
Careers
Security
Sign in
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Technology & Research
Blog
/
Optimizing GEPA for production: A test-driven approach to prompt engineering
Optimizing GEPA for production: A test-driven approach to prompt engineering
March 25, 2026
Written by
Roy Wang
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Prompt engineering has traditionally been a manual, iterative process: craft a prompt, test it, refine based on failures, repeat. Recent work on
GEPA (Reflective Prompt Evolution)
offers a systematic alternative: let an LLM reflect on failures and propose improvements automatically.
GEPA was introduced at
ICLR 2026
as a gradient-free optimizer that uses natural language reflection rather than policy gradients to adapt prompts. Built on the
DSPy framework
, it outperforms reinforcement learning methods like GRPO by up to 20% while using 35× fewer model rollouts. But like any optimization technique, its effectiveness depends heavily on configuration.
We applied GEPA to optimize prompts for a production classification task: a supervisor model that analyzes conversations and produces structured judgments with reasoning traces. This post shares what we learned from 19+ ablation experiments, focusing on three critical findings that challenged conventional wisdom about prompt optimization.
For our customers, the supervisor model is a last line of defense against hallucinated or inconsistent outputs. The configuration decisions we document here have direct consequences for that reliability, which is why getting them right matters beyond the benchmark.
How GEPA Works
Before diving into our ablation study, it's useful to understand what makes GEPA different from traditional approaches.
The core loop
GEPA operates through four main steps:
Trajectory sampling:
Generate outputs on a batch of examples using the current prompt
Reflection:
A "reflection model" (typically a frontier LLM) analyzes failures and successes, identifying patterns in what works and what doesn't
Proposal:
The reflection model proposes a new, improved prompt based on observed failures
Validation:
Test the new prompt on a validation set and keep it if it improves metrics
The key insight is that natural language provides a much richer learning signal than scalar rewards. Instead of "this output scored 0.7," GEPA sees "this output failed because the model confused temporal references with causal claims."
Unlike RL-based approaches that require thousands of rollouts, GEPA's reflection-based approach means we can optimize prompts with 20-100 examples. This makes it practical for production scenarios where labeled data is expensive or domain-specific.
Our task: production classification
We applied GEPA to optimize prompts for a supervisor model: a production classifier that analyzes conversations and produces structured outputs with reasoning traces. The model performs binary classification where each prediction must be justified through a chain of reasoning.
Two properties made this task ideal for studying GEPA:
Verifiable correctness:
We have ground-truth labels, enabling clean metric-driven optimization
Reasoning requirement:
The model must explain its decisions, not just produce labels. This is where prompt quality really matters.
The ablation study
We evaluated GEPA across
7 hyperparameter dimensions
with a fixed baseline configuration. Each experiment modified exactly one parameter to isolate its effect.
Baseline configuration
Sample size:
50 training + 50 validation examples
Budget:
1.0x multiplier (~150 LLM calls)
Reflection model:
GPT-4.1
Batch size:
10 examples per reflection
Feedback type:
Both positive and negative examples
Length constraint:
None
All configurations were evaluated on a fixed holdout set to measure generalization.
Experiment results overview
Here's how each dimension affected performance:
GEPA parameter
Description
Impact level
Key finding
Sample size
Tested configurations from 10 samples up to 500 samples to understand the data efficiency curve.
High impact
20–100 is optimal; 500 hurts performance
Reflection model
Compared frontier models (GPT-4.1, GPT-5.2, Claude Sonnet/Opus) vs. smaller models (GPT-4o-mini).
Critical
Frontier models required; small models fail
Length constraint
Experimented with hard character limits to prevent prompt bloat.
Moderate impact
1,500 chars: 4× compression, -0.8% perf
Feedback type
Compared using only negative examples vs. including positive examples.
Moderate impact
Both positive & negative examples help
Batch size
Tested how many examples the reflection model should see at once.
Low impact
10 examples per batch is sufficient
Budget multiplier
Varied computational budget to understand diminishing returns.
Low impact
Diminishing returns beyond 1× baseline
Train/Val split
Explored different ratios to balance optimization signal vs. validation reliability.
Low impact
50/50 split works well
Three critical findings
1. Less data works better: The 20-100 sample sweet spot
Conventional wisdom says more data is always better. Our experiments showed the opposite:
configurations with 20-100 examples consistently outperformed those with 500 samples for the given problem
.
Scaling from 50 to 500 samples caused prompt length to balloon by 75% while performance
decreased
. More iterations with more data led GEPA to encode every edge case, producing verbose, over-fitted prompts that failed to generalize.
This happens because GEPA's reflection mechanism accumulates observations across iterations. Each reflection cycle sees a batch of examples and proposes refinements. With 500 samples across many iterations, the reflection model encounters more distinct failure modes and tries to address all of them in the prompt. The result: a bloated instruction set that captures training distribution minutiae rather than the core task.
The optimal range of 20-100 samples provides sufficient diversity for the reflection model to identify patterns without drowning in edge cases. Below 20, there's insufficient signal. Above 100, you're paying for more compute and getting worse prompts. This is also unique to our problem where around 20 examples have sufficient diversity to lead improvement.
The data efficiency curve
We observed a clear inverted-U relationship between sample size and performance:
20 samples:
Peak performance, minimal compute (~60 LLM calls)
50 samples (baseline):
Strong performance, moderate compute (~150 calls)
100 samples:
Comparable to 20-50, but 2-4× the compute cost
500 samples:
Performance drops 2%, compute increases 10×, prompts balloon 75% longer
Relative performance vs. Compute cost
Configuration
Performance
Prompt length
Compute cost
10 samples
↓ -5%
No change
6× cheaper
20 samples
↑ +1% (best)
Concise
2.5× cheaper
50 samples (baseline)
→ Reference
→ Medium
→ 1× cost
100 samples
→ Similar
↓ -16% shorter
↓ 1.8× more expensive
500 samples
↓ -2% (worst)
↓ +75% bloat
↓ 10× more expensive
2. Reflection model quality is non-negotiable
This was our most definitive finding: smaller models completely fail at prompt optimization.
When we tested GPT-4o-mini as the reflection model, the "optimized" prompt remained essentially unchanged from the original seed prompt. The model simply couldn't perform the meta-cognitive task of analyzing failures and synthesizing improvements.
In contrast, every frontier model we tested (GPT-4.1, GPT-5.2, Claude Sonnet, Claude Opus) successfully optimized prompts to strong performance levels.
These smaller models fail because prompt optimization requires reasoning about reasoning. The reflection model must: (1) diagnose
why
the current prompt produced incorrect outputs, (2) identify patterns across multiple failures, (3) synthesize a better prompt that addresses root causes without over-fitting. This is frontier-level reasoning; smaller models lack the cognitive capacity.
Reflection model comparison
Performance differences between model classes were stark:
Model class
Optimization success
Prompt evolution
Cost share
GPT-4o-mini
Complete failure
No change (65 chars)
Cheap per call
GPT-4.1 / GPT-5.2
+5–6% improvement
Substantive evolution
~5–10% of total cost
Claude Sonnet/Opus
+5–6% improvement
Substantive evolution
~5–10% of total cost
You might be tempted to save costs by using a cheaper reflection model. However, the reflection model is only called ~10-20 times during optimization, while the task model (the one executing your prompts) is called hundreds of times.
Spending on a frontier reflection model represents only 5-10% of total optimization cost
, and a weak reflector means you waste all those task model calls learning nothing.
3. Length constraints are essential regularization
As we saw in Finding 1, GEPA has a tendency to overfit to training examples by encoding edge cases into increasingly verbose prompts. Unconstrained GEPA can produce prompts exceeding 5,000 characters. This is both a latency problem and an overfitting problem — the reflection mechanism naturally accumulates details across iterations, trading training performance for worse generalization.
Length constraints act as regularization. By forcing the reflection model to be concise, we prevent it from memorizing training distribution details and push it toward learning generalizable patterns instead.
The challenge is GEPA's default implementation doesn't support length constraints during reflection. We built a custom instruction proposer that encodes the constraint directly into the reflection prompt.
Length constraint impact
We tested multiple constraint levels to find the optimal balance:
Configuration
Prompt length
Performance impact
Production readiness
No constraint
5,000+ chars
→ Reference
Too slow, overfits
1,500 char limit
~1,000 chars (4× compression)
-0.8% only
Fast, generalizes
500 char limit
~400 chars (12× compression)
-3% degradation
Too aggressive
With the
1,500-character constraint
enforced through our custom proposer, we achieved:
4× prompt compression
(5,000 → 1,000 chars)
Minimal performance impact
(only 0.8% degradation)
Production-ready latency
that meets SLA requirements
Better generalization
by preventing overfitting to training edge cases
From research to production
GEPA represents a shift from gradient-based to reflection-based optimization. By exploiting the interpretable nature of language, it achieves better results with dramatically fewer examples than traditional RL approaches.
But research techniques rarely work out-of-the-box in production. Our ablation study revealed three critical adaptations:
Less data works better.
The 20-100 sample sweet spot challenges conventional wisdom; more examples cause prompt bloat and worse generalization.
Reflection quality is non-negotiable.
Smaller models fail completely. The reflection model is reasoning about reasoning, which requires frontier capabilities.
Length regularization prevents overfitting.
GEPA accumulates details across iterations, leading to prompt bloat. We built length-aware proposers as regularization, achieving 4× compression with minimal quality loss.
The broader lesson:
treat prompt optimization as software engineering
. Write tests (holdout validation), encode requirements (custom proposers), measure what matters (generalization over training accuracy), and extend the framework to fit your constraints.
GEPA provides the foundation. Systematic ablation tells you what to tune. Test-driven adaptation makes it production-ready — and for a supervisor model where consistency and accuracy directly affect what customers see, production-ready is the only bar that counts.
References & Further Reading
GEPA Paper:
Reflective Prompt Evolution Can Outperform Reinforcement Learning
(ICLR 2026)
DSPy Framework:
dspy.ai
GEPA Documentation:
DSPy GEPA Overview
GitHub:
gepa-ai/gepa
Built with
DSPy
and GEPA · Task: Production Classification · Dataset: 600+ labeled examples
Recent posts
Bringing the AI concierge to Australia
Decagon is opening a new office in Sydney, Australia
Introducing automatic optimization and Root Cause Analysis
Today, we’re excited to announce two new capabilities to help you rapidly improve your agent’s performance.
Bringing Decagon’s AI concierge solution to Google Cloud Marketplace
We're excited to announce that Decagon is now available on Google Cloud Marketplace.
Deliver the concierge experiences your customers deserve
Get a demo
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
