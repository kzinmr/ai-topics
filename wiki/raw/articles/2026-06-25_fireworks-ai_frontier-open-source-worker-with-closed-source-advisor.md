---
title: "Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor."
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/frontier-open-source-worker-with-closed-source-advisor"
scraped: "2026-06-25T06:00:59.388156+00:00"
lastmod: "2026-06-25T04:03:22.000Z"
type: "sitemap"
---

# Frontier AI at a fraction of the cost: open-source worker agents with a closed-source advisor.

**Source**: [https://fireworks.ai/blog/frontier-open-source-worker-with-closed-source-advisor](https://fireworks.ai/blog/frontier-open-source-worker-with-closed-source-advisor)

GLM 5.2 is live! Opus-level intelligence at open-source rates. Pay per token on serverless. Try it today.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Frontier Open Source Worker With Closed Source Advisor
Frontier AI at a fraction of the cost: open-source workers with a closed-source advisor
PUBLISHED
6/24/2026
Table of Contents
TL;DR
The setup: an open-source worker + a closed-source advisor
Frontier quality with cost efficiency
Ablations
What’s next
Try it yourself
Methodology details
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
TL;DR
The setup: an open-source worker + a closed-source advisor
Frontier quality with cost efficiency
Ablations
What’s next
Try it yourself
Methodology details
Table of Contents
TL;DR
A simple worker + advisor setup produces better outcomes at lower cost.
An open-source worker (Kimi-K2.6 / GLM-5.2) that calls a closed-source frontier model (Claude Opus 4.8) once per task as an advisor,
raises the success rate in every cell
across three benchmarks studied, while doing so at a fraction of the cost.
•
Consistent lift:
+4 (Kimi) / +7 (GLM) pp on SWE-bench Pro; +8 / +4pp Terminal-Bench 2.1; and +1 / +4 pp on Legal Agent Benchmark.
•
Frontier quality or better, far cheaper.
GLM-5.2 + advisor matches Opus run as the worker on Terminal-Bench (≈80%) at ~half the cost ($3.50 vs $6.61/task), beats it on Legal Agent Bench at ~40% lower cost, and captures most of the frontier on SWE-bench Pro at ~3× lower cost.
The setup: an open-source worker + a closed-source advisor
Two roles, one tool.
The open-source worker runs the task end to end (implement → review → revise); at the single review step it consults a read-only frontier advisor, then produces the deliverables.
•
Worker
— an open-source model (Kimi-K2.6 / GLM-5.2) drives the task end to end: reads the problem, edits files, runs commands, verifies its own work.
•
Advisor
— a frontier model (Opus 4.8) exposed to the worker as a single
review
consult. It cannot edit files. It reads the worker’s trajectory-so-far plus the working diff and returns an assessment with concrete pass/fail checks.
There is no external router or orchestrator.
The worker decides when to consult the advisor,
after it has done the work and run its own verification. The advisor audits what was actually done — it sees the diff — and flags gaps the worker missed. The worker receives the feedback and does additional work if needed. The result is a pattern of
sparse advisor calls, denser worker activity upstream and downstream.
The advisor is
pure brain with no hands
. Everything expensive — writing, running, iterating — stays on the open-source worker.
The advisor lifts quality across the board
Resolve rate over graded tasks (see Method notes). Worker baselines are the same model with no advisor; advisor = Opus 4.8, effort = medium. The Legal benchmark is harder where task resolved = all criteria pass, over all 100 tasks, so its absolute numbers run lower.
Benchmark + worker
Baseline
with Advisor
Uplift
SWE-bench Pro + Kimi-2.6
55%
59%
+4 pp
SWE-bench Pro + GLM-5.2
59%
66%
+7 pp
Terminal-Bench 2.1 + Kimi-2.6
64%
72%
+8 pp
Terminal-Bench 2.1 + GLM-5.2
76%
80%
+4 pp
Legal Agent Bench + Kimi-2.6
8%
9%
+1 pp
Legal Agent Bench + GLM-5.2
12%
16%
+4 pp
The lift is positive  using a single setup with no per-model or per-benchmark tuning
— across three task types (software engineering vs. terminal/ops vs. legal work) and two open-source workers. This robustness to task type and to worker model makes the advisor setup deployable at scale. Notably, GLM-5.2 + advisor reaches
parity-or-better with Opus run as the worker on 2 of the 3 benchmarks.
It matches on Terminal-Bench and beats on Legal, both at a fraction of the cost. This confirms and extends the findings from our
previous research
shared in partnership with the team from Harvey AI.
A few disclosure caveats: with only 60–100 tasks per cell, a one-task swing is ~1–1.8 pp, so cell directions are solid and exact magnitudes are subset estimates. The Opus/GLM-5.2 Terminal-Bench tie (80.5 vs 79.5) is within sampling noise and should be read as parity, not a win. Additionally, the Legal Agent Benchmark with Kimi-K2.6 + advisor cell (+1 pp, one task) is likewise within noise and so should also be read as flat, not a lift.
Frontier quality with cost efficiency
We plot three operating points per benchmark: the open-source worker alone, the open-source worker + Opus advisor, and the frontier model run as the worker (Opus, no advisor).
Cost vs. resolve rate across all three benchmarks
Figures 1–3 Below: x = inference cost per task (USD), y = resolve rate.
For each worker, the dashed line goes base → + advisor; the red square is Opus run as the worker (4.8 on SWE/Terminal, 4.7 on Legal).
Performance on SWE-Bench Pro
Performance on Terminal-Bench 2.1
Performance on Legal Agent Benchmark (LAB)
The detailed cost breakdown below. The lessons are clear:
•
Open source + advisor reduces spend across the board
. Every cell undercuts Opus-as-worker — 19% to 67% cheaper.
•
The win compounds with GLM quality.
GLM beats Kimi on quality, advisor spend, and savings all at once.
Benchmark + worker
Opus 4.8 (frontier)
Open-source + advisor (worker + advisor)
Savings vs Opus
SWE-bench Pro + Kimi-2.6
$18.28
$6.13 ($4.02 + $2.11)
66%
SWE-bench Pro + GLM-5.2
$18.28
$6.09 ($4.64 + $1.45)
67%
Terminal-Bench 2.1 + Kimi-2.6
$6.61
$4.11 ($2.70 + $1.41)
38%
Terminal-Bench 2.1 + GLM-5.2
$6.61
$3.50 ($2.20 + $1.30)
47%
Legal Agent Bench + Kimi-2.6
$9.54
$7.73 ($5.35 + $2.38)
19%
Legal Agent Bench + GLM-5.2
$9.54
$5.74 ($5.03 + $0.71)
40%
Ablations
Plan+review vs. review-only: is it better to call the advisor once or multiple times?
We tested a stronger version of the advisor harness, where we instruct the agent to consult the advisor twice: a plan call before building, plus the review call before finishing. The verdict: review-only is
as good or better in 5 of 6 (benchmark × worker) experiments.
It is distinctly better on Terminal-Bench (Kimi-K2.6 72% vs. 63%) at roughly
half the advisor calls
(≈1 vs. ≈2 per task). In short, the additional plan call doesn’t pay for itself.
Does the reviewer have to be the frontier?
Run GLM-5.2 as both worker and reviewer: a same-model reviewer
reproduces the frontier advisor’s lift on neither benchmark
— flat on SWE-bench (58% vs. 59% base, vs. frontier-advised 66%) and worse on Terminal-Bench (72% vs. 76% base, vs. frontier-advised 80%). The judgment the frontier reviewer supplies is exactly what the open model can’t supply about its own work — so the reviewer has to be the frontier. The Legal benchmark sharpens it: GLM-5.2 self-review is again flat (12→12%), and a same-tier GLM-5.2 reviewer over a different open worker (Kimi-K2.6) actively
degrades
it (8→6%) where the frontier reviewer is neutral-to-positive (8→9%).
Advisor effort: medium is the default.
Medium vs. high advisor effort lands within one task (SWE-bench: Kimi 34 vs. 35, GLM 36 vs. 35) — cheaper and faster at no quality cost.
What’s next
This six-cell sweep is a snapshot. The natural next steps:
•
More task types and models.
Code and ops are two regimes; further agentic domains (data analysis, web, longer workflows) and newer model tiers, to confirm the uplift holds as both the open and frontier tiers advance.
Try it yourself
The advisor is open-sourced as a single self-contained file in the Fireworks cookbook:
github.com/fw-ai/cookbook/tree/main/advisor
book/advisor
.
Two roles: an open-source (GLM-5.2)
worker on Fireworks
does the task; a
frontier reviewer (Claude)
reviews its diff before it finishes.
1
2
3
4
5
# The advisor is the reviewer (Claude). Grab the one file (Node 18+),
set
its key
:
curl
-
O https
:
//
raw
.
githubusercontent
.
com
/
fw
-
ai
/
cookbook
/
main
/
advisor
/
advisor
.
mjsexport ADVISOR_API_KEY
# Anthropic key for the Claude reviewer
# Your agent — the GLM-5.2 worker on Fireworks — calls this before it finishes:
node advisor
.
mjs review
-
-
question
"<what to check>"
-
-
files
"<key files>"
Then add one line to your agent’s instructions (CLAUDE.md / AGENTS.md) so it consults the advisor before finishing.
Full walkthrough in the
README
.
Methodology details
•
Benchmarks.
SWE-bench Pro (cais/swebenchpro), a stratified 60-task subset over 11 repos (≈8% of the 731-task set);
Terminal-Bench 2.1
, 84 text tasks;
Legal Agent Benchmark
, 100 expert-authored legal tasks (Harvey), scored as
all-criteria-pass over all 100 tasks
(every sub-requirement must pass — a stricter bar than the SWE/TB resolve rate, hence the lower absolute numbers), judged by Kimi-K2.6. We also ran GLM 5.1 as judge model and got comparable results, ruling out same-family scoring bias. Opus as worker on Legal is 4.7 (4.8 scored lower on the subset); Legal per-task cost is uncached and scaled to a measured Kimi-K2.6 baseline.
•
What the review call actually says: The whole mechanism is one prompt, and the exact wording is the design.
The review call is a skeptic, not a cheerleader.
It is told to distrust the worker — both its framing and its prose. e.g.
“do NOT accept the agent’s framing, arithmetic, or boundaries … … Verify claimed edits against the
worktree, not the agent’s prose
… … Confidence: score each issue 0–100.”
Two choices do the work.
Calibrated confidence
(only ≥80 becomes “critical”) keeps the advisor from drowning a working solution in nitpicks the worker would waste turns chasing.
And
auditing the diff, not the narrative
, means the worker cannot talk its way to “done”: the advisor reads git diff as ground truth and marks each check as
PASSING / FAILING / NOT IMPLEMENTED / DEVIATED
. The worker then fixes what’s flagged and finishes.
Sihan Sandy Yuan
Member of Technical Staff
Sandy previously completed his PhD at Harvard and conducted his post-doctoral research at Stanford.
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
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
