---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/DeepSeek-V4-Pro-Security"
scraped: "2026-08-26T06:00:57.676452+00:00"
lastmod: "2026-08-26T01:34:28.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/DeepSeek-V4-Pro-Security](https://fireworks.ai/blog/DeepSeek-V4-Pro-Security)

DeepSeek-V4-Pro-0813 available now on Fireworks
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Deepseek V4 Pro Security
DeepSeek V4 Pro is Redefining Security Agent Economics
PUBLISHED
8/26/2026
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
TLDR;
DeepSeek V4 Pro 0813 recorded zero refusals across 840 adversarial security tasks and solved them at half the cost per success of the highest-scoring model we tested. The two closed models in the same test were the two worst dollars-per-result.
We ran DeepSeek V4 Pro through CyberGym alongside Kimi K3, GPT-5.5, and Claude Opus 4.8. We evaluated real vulnerabilities in real codebases, approximately 89 turns per task on average.
What CyberGym actually measures for evaluating Deepseek
Most coding benchmarks ask a model to write code that passes single tests. CyberGym represents a more real-world workload because it asks the model to break something real, then fix it.
The benchmark was built at UC Berkeley from 1,507 real vulnerabilities across 188 widely used open-source projects, drawn from Google's OSS-Fuzz campaign and the ARVO reproducible-vulnerability archive. Each task hands the agent a short description and a real vulnerable codebase. The agent has to locate the flaw, build an input that actually triggers it, and then patch it. Grading is by execution, not by a judge model. The proof-of-concept either crashes the target or it does not.
The structure of Cybergym is agentic, long-horizon, and unforgiving. Our runs averaged 89 turns and 25 minutes per task. There is no partial credit for a possible result, which means CyberGym is one of the few evals where the score cannot be gamed by a model that writes confidently.
It is also the closest public proxy for a workload our customers are already running. As Trilogy put it in the
cybersecurity playbook
they built on Fireworks: “the defender's workload is high-volume”. You audit every repo, triage every scan, review every PR, retest every fix. A model that is almost strong enough and more cost efficient to run often beats a stronger model that is gated, expensive, or unavailable during an incident.
DeepSeek V4 Pro: Zero Refusals, Zero Wasted Overhead
Most teams hit the refusal wall too late, usually after their agent is already in production. An agent proof of concept might run smoothly, only to stall mid-task under real traffic.
In our testing we found across 840 traced primary tasks, Deepseek V4 Pro produced native tool calls on all 840 of them. We saw no refusals, and no output-length truncations.
For contrast on why this matters, frontier closed models perform very differently. On the latest Claude Opus 5 and GPT 5.6, these cyber tasks couldn’t be completed because there were checks that blocked the CyberGym utility. When older generation Claude Opus 4.8 did run, it entered stage-1 validation on only 70 of 697 tasks in our matched cohort, a 10% entry rate, and finished at a 5.9% reward. It is not that Opus is a weak coding model. It is that a large share of its runs never produced a usable artifact on this task family. If you are building a security agent, that difference shows up as a bill for tokens that produced nothing. For cybersecurity use cases, open models are the best viable solution because closed models can block you from engaging in real work.
On the CyberGym test, Deepseek V4 Pro entered validation on 678 of 697, or 97.3% as seen in the chart below.
Figure 1: Cybergym Test Results
CyberGym: Deepseek V4 Pro solves security tasks for 50% lower costs
On the strict four-model common-valid Cybergym cohort of 697 tasks, we saw the following results:
Model
Reward Rate
$/task
$/reward
Kimi K3
68.4%
$3.363
$4.914
Deepseek V4 Pro 0813
53.7%
$1.343
$2.502
Open AI GPT 5.5
47.6%
$4.592
$9.641
Anthropic Opus 4.8
5.9%
$1.957
$33.275
What did each model uncover in this testing? Of the 697 tasks, 38 were solved by Deepseek V4 Pro and nothing else. K3 uniquely solved 97, GPT-5.5 got 41, and Opus 4.8 got exactly one. Opus wasn't only scoring low, it was almost never the model that found something the others missed. For completeness, 101 tasks were solved by none of the models, which is the representative ceiling on all four.
It's easy to focus on the K3 gap and miss the other results. People often think open models are only more cost efficient, but this analysis shows Deepseek V4 Pro beat GPT-5.5 outright on both quality and price. On accuracy: plus 6.03 points, 95% CI [+1.29, +10.62], McNemar p = 0.0152. It won 164 tasks GPT-5.5 lost and lost 122 it won. So the open model here is more accurate than a closed frontier model and costs a quarter as much per solved vulnerability.
Figure 2: Cost Per Task
K3 wins on raw solve rate by 14.8 percentage points, and the math proves it isn't random. On the paired bootstrap 95% CI [-19.23, -10.33], McNemar p=9.43×10−11—meaning there is virtually zero chance this gap is random noise). If your main criteria is success, K3 is the best choice, and you can run it on Fireworks:
here
In practice, unit economics matter just as much as solve rate:
•
Cost Efficiency:
On identical tasks, V4 Pro costs
$2.50 per solved task
vs. K3’s
$4.91
(a
1.96x cost advantage
for V4 Pro). Across an 863-task diagnostic, that 2x ratio holds. You can run twice as many security scans for the same budget.
•
Standalone Accuracy:
V4 Pro solves 462 of 920 tasks (
50.2%
), costing
$1.31 per run
and
$2.60 per success
. Sub-scores hit
54.7%
on ARVO tasks and
48.7%
on OSS-Fuzz tasks.
•
Where It Fails (The Harness Opportunity):
Once V4 Pro completes stage-1 validation (generating a valid proof-of-concept), it finishes the full patch
94.7% of the time
.
Deepseek V4 Pro rarely fails at the hard part (fixing code); it fails upstream at the setup step (generating the initial exploit). That is an actionable prompt-and-scaffolding fix for your team, not an unfixable model limitation.
The data makes it clear: when building high-volume security agents, you no longer need to sacrifice performance for cost or risk being blocked by the "refusal walls" of closed frontier models. DeepSeek V4 Pro provides a distinct advantage, consistently delivering native tool calls without truncation, significantly higher accuracy, and a 1.96x cost advantage per solved vulnerability compared to leading proprietary alternatives. For security teams looking to audit codebases and triage vulnerabilities at scale, moving to an open, high-performance model like DeepSeek V4 Pro isn't just a budget decision, but it's a technical upgrade that enables more reliable, effective, and sustainable security operations.
You can start deploying these capabilities today by checking out
DeepSeek V4 Pro 0813 on Fireworks
.
Learn more about how Deepseek V4 Pro performs against Fable 5 on Coding workloads in our other write-up:
here
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
Fireworks for Startups
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
