---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/agent-execution-tax"
scraped: "2026-05-21T06:00:53.201360+00:00"
lastmod: "2026-05-20T16:39:39.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/agent-execution-tax](https://fireworks.ai/blog/agent-execution-tax)

DeepSeek V4 Pro is Live → Try it now.
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
Agent Execution Tax
Agents Don't Fail on Intelligence. They Fail on Execution.
PUBLISHED
5/20/2026
Table of Contents
What 720 browser agent runs revealed about the real bottleneck in agentic AI.
Deployment Readiness Scorecard
The Agent Execution Tax
Definition
Applied to Our Data
How the Tax Compounds
Generalised Formulas
Structured Output Reliability: The Root Cause
The Data
Why This Matters More Than You Think
Reliability-Adjusted Accuracy
Why Nobody Measures This
What This Looks Like in Practice
How We Measured This
The Setup
The Models
Scope of This Benchmark
Cost Per Successful Task > Token Pricing
Inference Latency: The Compounding Story
What the Fireworks Serving Layer Contributes
Per-Site Analysis: Where the Thesis Holds or Breaks
Universal Success
Universal Failure
The Differentiators
Gemini's One Win: Google Flights
What This Means for AI Procurement
Procurement Scorecard
Model Profiles: Three Models, Three Strategies
GLM-5: The Reasoning Powerhouse
MiniMax M2.5: The Best Value
Kimi K2.5: Fastest Inference in This Benchmark
The Vision Question
Kimi K2.5 Vision: Infrastructure Constraint, Not Model Limitation
Closing
Appendix
A. Reproducibility
B. Benchmark Configuration
C. Evaluator Methodology
D. Full Per-Site Breakdown (Numeric Reference)
E. Data Files
Table of Contents
Table of Contents
What 720 browser agent runs revealed about the real bottleneck in agentic AI.
Deployment Readiness Scorecard
The Agent Execution Tax
Definition
Applied to Our Data
How the Tax Compounds
Generalised Formulas
Structured Output Reliability: The Root Cause
The Data
Why This Matters More Than You Think
Reliability-Adjusted Accuracy
Why Nobody Measures This
What This Looks Like in Practice
How We Measured This
The Setup
The Models
Scope of This Benchmark
Cost Per Successful Task > Token Pricing
Inference Latency: The Compounding Story
What the Fireworks Serving Layer Contributes
Per-Site Analysis: Where the Thesis Holds or Breaks
Universal Success
Universal Failure
The Differentiators
Gemini's One Win: Google Flights
What This Means for AI Procurement
Procurement Scorecard
Model Profiles: Three Models, Three Strategies
GLM-5: The Reasoning Powerhouse
MiniMax M2.5: The Best Value
Kimi K2.5: Fastest Inference in This Benchmark
The Vision Question
Kimi K2.5 Vision: Infrastructure Constraint, Not Model Limitation
Closing
Appendix
A. Reproducibility
B. Benchmark Configuration
C. Evaluator Methodology
D. Full Per-Site Breakdown (Numeric Reference)
E. Data Files
Table of Contents
What 720 browser agent runs revealed about the real bottleneck in agentic AI.
A
Notte
×
Fireworks AI
benchmark report.
Foundation models keep getting smarter. They ace reasoning benchmarks, write fluent code, and pass professional exams. Yet when you put them inside an agent loop, where they must observe a webpage, decide what to do, and output a structured action ten times in a row, they fail roughly half the time.
We ran 720 browser automation tasks across four LLMs to find out why. The answer was not intelligence. It was execution:
one model wasted nearly 1 in 5 LLM calls on malformed JSON that had to be retried.
That single reliability gap cascaded into higher latency, inflated cost, and lower task success, even though the model's raw reasoning capability was competitive.
We call this overhead the
Agent Execution Tax
: the ratio of wasted inference to productive inference. For the worst-performing model in our benchmark, that tax was 22.9%. For the best, it was zero.
In agent systems, reliability compounds harder than intelligence. The models that won were not the ones with the best reasoning scores. They were the ones that reliably did what they were told, every time, in the format they were asked for.
In production, that reliability is shaped not just by the model itself, but by the inference infrastructure serving it: structured output consistency, latency predictability, and stable execution under repeated agent loops.
At 10,000 agent tasks per day, a modest production volume, the execution overhead of the worst-performing model costs over $40,000 per year in inference that produces no value. A model that looks cheaper per token can cost significantly more per outcome once retries, failures, and inflated call counts are factored in.
Scope.
This is a text-only browser agent benchmark. Results measure structured output reliability and step efficiency in a multi-step agent loop — not general model intelligence, reasoning ability, or multimodal capability. See Scope of This Benchmark below for the full scope statement.
Deployment Readiness Scorecard
If you are evaluating models for an agent deployment, here is how they map to production constraints.
If you need...
Use
Why
Maximum task accuracy
GLM-5
57.1% accuracy; 100% on Google Maps, HuggingFace, BBC News, Wolfram Alpha; strongest on structured data extraction and multi-step reasoning
Lowest cost at scale
MiniMax M2.5
$0.062 per successful task (2.3x cheaper than Gemini); RL-trained agent that takes the fewest steps (9.8 avg) and rarely retries (1.6%)
Fastest real-time response
Kimi K2.5
2.1s p50 LLM latency; zero parse retries across 852 calls; best for user-facing agents where perceived speed matters
Rigorous procurement evaluation
Reliability-Adjusted Accuracy
Token pricing misleads at the model selection stage; cost per successful task and execution tax are the metrics that reflect what you actually pay for
One-line summary per model:
•
GLM-5:
Best accuracy, highest cost. Use for compliance workflows, research automation, and tasks where errors carry downstream consequences.
•
MiniMax M2.5:
Best value. Default choice for scaled production workloads. The $40k/year waste calculation makes it the economically dominant option at volume.
•
Kimi K2.5:
Best speed, zero execution overhead. Use for customer-facing agents, live demos, and any workflow where response latency affects user trust.
The Agent Execution Tax
A browser agent task looks simple from the outside: go to Amazon, search for a product, extract the price. Under the hood, it is a multi-step loop:
observe page → LLM generates action (as JSON) → execute action → observe new page → repeat
A typical task takes 10 steps. Each step is an LLM call that must return valid structured output: a JSON object specifying which element to click, what text to type, or what data to extract. If the JSON is malformed, the framework retries. And that retry is invisible: it does not show up in task success rates or reasoning benchmarks. It only surfaces as inflated call counts, latency, and cost once you instrument the engine itself.
Definition
Agent Execution Tax = (total_inference_calls − productive_calls) / productive_calls
Productive calls
are those that returned valid structured output on the first attempt. The tax measures how much additional inference you pay, relative to the useful work done. Every percentage point is money spent on inference that delivers nothing.
Note the denominator: this is not the same as the raw retry rate (retries / total calls). An 18.6% retry rate translates to a 22.9% execution tax because the denominator shrinks when you remove the wasted calls.
Applied to Our Data
Model
Productive Calls
Total Calls
Execution Tax
Kimi K2.5
852
852
0.0%
GLM-5
869
884
0.6%
MiniMax M2.5
815
828
1.6%
Gemini 2.5 Flash
721
886
22.9%
Measured on instrumented runs (90 tasks per model). Zero parse failures (exhausted retries) recorded across all models.
For every dollar of productive inference Gemini produces, you pay an additional 23 cents in waste. Kimi's tax is zero.
(Note: the hero Execution Tax bar chart at the top of the article is the canonical visual for this section; do not duplicate it here. The table above carries the exact numbers for citation.)
How the Tax Compounds
The tax is not a single cost. It stacks across three dimensions:
Token tax.
Wasted tokens on malformed responses, plus the full input context re-sent on every retry. Gemini averaged 15,482 input tokens per step; each retry re-sends that entire context for zero productive output.
Latency tax.
Each retry adds a full LLM round-trip (~2.5s at Gemini's p50), roughly 12 seconds of dead time per task.
Cascade tax.
A retry at step 8 can desync the agent's internal state, causing downstream steps to misinterpret the page and fail. Hardest to measure; most dangerous at scale.
Generalised Formulas
Expected retries per task = n_steps × retry_rate / (1 − retry_rate)
Token overhead per task   = expected_retries × (avg_input_tokens + avg_output_tokens)
Latency overhead per task = expected_retries × avg_call_latency
For a 10-step task with Gemini's 18.6% retry rate: ~2.3 expected retries, ~36,500 wasted tokens, and ~5.7 seconds of dead time per task.
Structured Output Reliability: The Root Cause
Execution tax is the lens. Structured output reliability is what drives it and is one of the most underreported bottlenecks in production agents.
The Data
Model
Total LLM Calls
Parse Retries
Retry Rate
Calls/Task
Gemini 2.5 Flash
886
165
18.6%
14.7
MiniMax M2.5
828
13
1.6%
9.8
GLM-5
884
5
0.6%
10.3
Kimi K2.5
852
0
0.0%
10.2
Gemini 2.5 Flash produced invalid structured output on
nearly 1 in 5 LLM calls
. The three Fireworks models combined: 18 retries across 2,564 calls (0.7%).
Why This Matters More Than You Think
In a 10-step agent task, the probability that at least one step requires a retry:
•
Gemini (18.6% per call):
86.7%
•
MiniMax (1.6% per call): 14.9%
•
Kimi (0.0% per call): 0%
With Gemini, 87% of tasks experience at least one parse retry. This is not an edge case; it is the default experience. Gemini averaged 14.7 LLM calls per task versus ~10 for the Fireworks models: the extra ~4.7 calls are almost entirely retries and the downstream steps they force.
Reliability-Adjusted Accuracy
Raw task accuracy tells you how often the agent succeeds. It does not account for the cost of getting there. A compound metric,
Reliability-Adjusted Accuracy
, discounts task success by execution overhead:
Reliability-Adjusted Accuracy = Task Success Rate × (1 − Execution Tax)
Model
Task Accuracy
Execution Tax
Reliability-Adjusted Accuracy
GLM-5
57.1%
0.6%
56.8%
MiniMax M2.5
57.5%
1.6%
56.6%
Kimi K2.5
49.7%
0.0%
49.7%
Gemini 2.5 Flash
45.0%
22.9%
34.7%
The gap between Gemini's raw accuracy (45.0%) and its reliability-adjusted accuracy (34.7%) is the clearest illustration of the execution tax: over a third of Gemini's operational capacity is consumed by execution overhead. The Fireworks models barely move.
Why Nobody Measures This
The parse retry happens inside the LLM engine, before the agent framework ever sees the result. Unless you instrument the engine, retries are invisible. Static benchmarks (MMLU, HumanEval, ARC) measure model intelligence in isolation; they do not measure whether a model can sustain structured output compliance across a multi-step loop.
Parse retry rate should be a first-class metric in every agent benchmark.
Prior work has documented adjacent findings. The original
WebVoyager paper
(He et al., 2024) introduced the benchmark we use here and established the framing that end-to-end web agent performance is a distinct measurement from static model evaluation.
AgentBench
(Liu et al., 2024) evaluated LLMs across eight agent environments and found large gaps between model-capability scores and task-completion rates in multi-step loops, reinforcing that agent-specific reliability metrics — not MMLU rank — should drive procurement decisions.
SWE-bench
(Jimenez et al., 2024) extended the same observation to software-engineering agents: models that top reasoning leaderboards resolve only a small fraction of real GitHub issues, because sustained structured execution across long tool-use loops is not what static evals measure.
What This Looks Like in Practice
Task:
"Find all Uniqlo locations in Chicago, IL." (Google Maps, from the WebVoyager benchmark)
Both models received the same task, the same browser environment, and the same starting URL.
At a glance:
Kimi K2.5
Gemini 2.5 Flash
Steps taken
12
16
LLM calls
12
25
Prase retries
0
9
Total duration
51.2s
97.9s
Total LLM time
23.2s
57.5s
Input tokens
87,063
207,971
Output tokens
3,236
8,411
Result
Success
Success
Both models found the answer. One did it in 51 seconds with 12 clean calls. The other took 98 seconds and made 25 calls to accomplish 16 steps. The difference was not reasoning ability; it was execution overhead.
Kimi K2.5: 12 steps, 0 retries
Step
Action
LLM time
1
Navigate to google.com/maps
1.57s
2
Click "Accept cookies"
1.75s
3
Click search input field
1.30s
4
Type "Uniqlo Chicago IL"
1.47s
5
Press Enter
2.06s
6
Click back (close single-location panel)
2.20s
7
Type "Uniqlo stores Chicago"
1.49s
8
Click search
2.09s
9
Click "Nearby" button
2.02s
10
Type "Uniqlo" in nearby search
2.60s
11
Click search
3.33s
12
Submit answer (3 locations found)
1.36s
Every call produced valid JSON on the first attempt.
Gemini 2.5 Flash: 16 steps, 9 retries (25 total LLM calls)
Step
Action
1
Navigate to google.com/maps/
2
Click "Accept cookies"
3
Type "Uniqlo Chicago, IL"
4
Click search
5
Click result (opens single-location panel)
6
Click back to results
7
Click "Next page" button
8
Type "Uniqlo Chicago, IL" (re-search)
9
Click search
10
Click result (opens single-location panel)
11
Type "Uniqlo Chicago" (new query)
12
Click search
13
Click result (opens single-location panel)
14
Type "Uniqlo locations Chicago IL"
15
Click search
16
Submit answer
Gemini took 16 actions but made 25 LLM calls. Nine returned malformed responses and were silently discarded. From the framework's perspective, each step appears to succeed; the retries are invisible inside the inference layer.
What a parse retry looks like at the protocol level
At each step, the agent must return a structured JSON object:
{
"state": {
"previous_goal_status": "success",
"previous_goal_eval": "Clicked the back button successfully.",
"page_summary": "Google Maps showing search results for Uniqlo in Chicago.",
"relevant_interactions": [{"id": "B3", "reason": "Next page button"}],
"memory": "Found one Uniqlo on State Street. Need to find all locations.",
"next_goal": "Click Next page to see if there are more results."
},
"action": {
"type": "click",
"element_id": "B3"
}
}
When the response fails to match this schema (missing a required field, invalid action type, markdown fences around the JSON), the framework catches the validation error and sends back a correction message:
Error parsing LLM response: [{'type': 'missing', 'loc': ('state', 'memory'),
'msg': 'Field required', 'input': {...}}], retrying
The model then receives the full context again plus the error, and regenerates. Each regeneration costs a full inference call: input tokens (the entire conversation history) plus output tokens. At Gemini's context sizes, a single retry adds roughly 12,000–16,000 tokens and 2–3 seconds of latency. Across 9 retries, that is ~20–25 seconds of dead inference time in one task.
Gemini's 98s breaks down roughly as ~40s browser operations, ~37s productive inference, and ~21s retry inference. Kimi's 51s has no retry segment at all. That is the Execution Tax made visible at the level of a single task.
How We Measured This
Notte
is an open-source, model-agnostic browser agent framework. Change the model string, and the same agent pipeline runs identically across providers. This makes it an ideal testbed for isolating model behaviour from framework effects.
The Setup
•
Task suite:
WebVoyager
, 60 multi-step browser tasks across 15 real websites (Amazon, GitHub, Google Flights,
Booking.com
, ArXiv, Coursera, ESPN, BBC News, and more).
•
Runs:
Each model ran every task 3 times (180 runs per model,
720 total
) to control for website variability and non-determinism.
•
Instrumentation:
Per-call LLM latency, parse retry counts, parse failure counts, and token usage captured for every run.
The Models
Model
Provider
Architecture
Pricing (in / out per 1M tokens)
Gemini 2.5 Flash
OpenRouter
Proprietary
$0.30 / $2.50
Kimi K2.5
Fireworks AI
32B active (1T MoE)
$0.60 / $3.00
GLM-5
Fireworks AI
40B active (700B MoE)
$1.00 / $3.20
MiniMax M2.5
Fireworks AI
228.7B MoE
$0.30 / $1.20
All three open-weight models were served by
Fireworks AI's serverless inference
; Gemini 2.5 Flash was served by OpenRouter as a proprietary baseline. No dedicated deployments, no custom infrastructure — standard pay-per-token APIs throughout, the way most developers actually use these models.
Results therefore reflect both model behaviour and production-serving characteristics under a real multi-step agent workload, including latency consistency and structured-output reliability at the inference layer.
Scope of This Benchmark
This benchmark measures structured output reliability and step efficiency in a text-only browser agent loop. It is not a general comparison of model intelligence, reasoning ability, or multimodal capability.
Readers evaluating models for other use cases — chat assistants, code generation, standalone multimodal tasks — should not extrapolate directly from these findings. The rankings, cost-per-outcome figures, and execution tax values below apply specifically to the text-only agent setting.
Within that scope: all models were tested text-only (no screenshots) to ensure a fair comparison, since only 1 of the 3 Fireworks models supports vision. This puts Gemini 2.5 Flash at a structural disadvantage, because Notte's production pipeline is built around Gemini's multimodal capabilities. We address this directly in the results, but the punchline is that even restoring Gemini's vision advantage (which boosts it to 53% in separate testing) does not change the outcome.
All models used identical settings:
temperature=0.0
,
max_steps=20
,
response_format=json_object
(non-strict mode). An independent LLM judge evaluated task success across all models. Full configuration details are in Appendix B.
The same model-agnostic framework used across these 720 runs used
Notte
. Reproducibility steps in Appendix A.
All results reflect the publicly available model versions and infrastructure configurations available during the March 2026 test window.
Cost Per Successful Task > Token Pricing
Token pricing tells you what you pay per unit of inference. Cost per successful task tells you what you pay per unit of value. The gap between them is driven by retry waste, step efficiency, and task success rate, all of which token pricing ignores.
Model
Success Rate
Avg Task Time
Avg Steps
Cost/Task
MiniMax M2.5
57.5%
75s
9.8
$0.036
GLM-5
57.1%
102s
10.3
$0.124
Kimi K2.5
49.7%
60s
10.7
$0.083
Gemini 2.5 Flash
45.0%
76s
11.3
$0.064
180 runs per model (720 total). Parse retry rate measured on instrumented runs (90 per model).
On a per-token basis, Gemini ($0.30/$2.50) looks cheaper than Kimi ($0.60/$3.00) and GLM ($1.00/$3.20). On a per-outcome basis,
MiniMax M2.5 is 2.3x cheaper than Gemini per successful task
while being 12.5 percentage points more accurate. The same pattern makes GLM-5 a premium-but-defensible choice and leaves Gemini economically unattractive despite its sticker price.
Where the tokens actually go (per-task averages, recomputed from v2 instrumented runs):
Model
Productive in
Productive out
Retry in (re-sent context)
Retry out (discarded)
Kimi K2.5
117,140
2,835
0
0
GLM-5
109,575
5.321
623
30
MiniMax M2.5
100,137
4,399
1,597
70
Gemini 2.5 Flash
157,623
3,853
35,901
877
Gemini spends roughly
36,800 tokens per task on inference that is billed and thrown away
— nearly one in five tokens produces zero value. The three Fireworks models combined waste under 3,000 tokens per task.
Inference Latency: The Compounding Story
Per-call latency is only half the picture. Factor in retry-inflated call counts, and the end-to-end story flips.
Model
Avg LLM Latency
p50
p95
Spread (p95/p50)
Kimi K2.5
2,339ms
2,145ms
4,026ms
1.9x
Gemini 2.5 Flash
2,670ms
2,476ms
4,381ms
1.8x
MiniMax M2.5
3,704ms
3,051ms
7,069ms
2.3x
GLM-5
6,283ms
5,634ms
11,028ms
2.0x
Gemini's p50 latency (2,476ms) looks competitive with Kimi's (2,145ms): only 15% slower per call. But Gemini makes ~14.7 calls per task versus Kimi's ~10.2:
Gemini: 14.7 calls × 2,476ms = 36.4s of LLM time
Kimi:   10.2 calls × 2,145ms = 21.9s of LLM time
Gemini spends
66% more time in LLM inference
per task, not because it is slower per call, but because it makes more calls.
Agent deployments should evaluate inference infrastructure alongside model quality. Low tail-latency variance, stable structured-output serving, and predictable retry behavior materially affect end-to-end agent cost and responsiveness once systems operate at production scale.
The p95/p50 spread across all models (1.8–2.3x) is tight, indicating predictable tail latencies from Fireworks' serverless infrastructure. That matters because retry amplification compounds unpredictability quickly in production agent systems: small variances at the inference layer become magnified across multi-step loops. In practice, agent reliability depends not just on the model, but on the serving layer's ability to sustain low-variance inference across thousands of sequential calls.
Time budget per average task (recomputed from v2 per-call latency arrays):
Model
Total
Browser ops
Productive LLM
Retry LLM
Kimi K2.5
62.7s
38.7s
24.0s
0.0s
MiniMax M2.5
8.23s
44.9s
36.8s
0.6s
Gemini 2.5 Flash
81.5s
43.4s
31.0s
7.1s
GLM-5
106.4s
41.8s
64.2s
0.4s
Browser time is roughly equivalent across models (~40–45s). Productive LLM time scales with per-call latency. The distinctive segment is retry LLM time: Gemini spends a full 7.1 seconds per average task on inference that will be discarded. Kimi spends zero.
What the Fireworks Serving Layer Contributes
Two findings in this benchmark are properties of the serving layer, not of the models being served.
Tight tail-latency variance across heterogeneous architectures.
Three Fireworks-served models with very different designs — Kimi K2.5 (32B active, 1T MoE), GLM-5 (40B active, 700B MoE), and MiniMax M2.5 (228.7B MoE) — all delivered p95/p50 spreads inside 1.9–2.3×. Across 90 tasks and thousands of inference calls per model, no Fireworks model produced a long-tail outlier. Tail-latency consistency across heterogeneous architectures is a serving-stack property: the model determines mean latency, but the stack determines whether that mean is the typical case or the lucky one.
Retry recovery stayed stable across the Fireworks lineup.
When the Fireworks-served models did retry — 18 times across 2,564 calls combined — every retry recovered cleanly; none spiralled into the retry-exhaustion failure mode. That depends on structured-output handling that stays consistent under correction loops: even when the first output is malformed, the resend produces something the framework can parse. The difference between an invisible 2-second tax and a task-killing failure sits at the serving layer.
"The model determines capability; the serving layer determines whether that capability survives a multi-step loop."
Per-Site Analysis: Where the Thesis Holds or Breaks
The aggregate numbers support the execution-tax thesis. The site-level breakdown stress-tests it: if execution reliability is the real bottleneck, we should see the Fireworks models win on sites that demand compounded correctness across many steps, and we should see everyone struggle where visual parsing dominates.
Universal Success
Cambridge Dictionary
(100% across all models),
Wolfram Alpha
(83–100%),
ESPN
(83–100%). Clean DOMs, clear information hierarchies, minimal dynamic content. These tasks validate baseline agent competence; they are not where models differentiate.
Universal Failure
Allrecipes
(0–17%),
Google Search
(0–8%). Heavy dynamic loading, recipe card layouts, and deceptively complex DOMs with interleaved ads and knowledge panels. Both likely require vision to solve reliably. Execution tax is irrelevant here; the limiting factor is parsing the page at all.
The Differentiators
These sites reveal genuine capability gaps and carry the core proof weight of the benchmark.
Website
Gemini
Kimi K2.5
GLM-5
MiniMax M2.5
Booking
0%
9%
0%
33%
GitHub
22%
17%
28%
39%
Google Maps
58%
58%
100%
100%
Amazon
70%
70%
55%
88%
ArXiv
40%
57%
77%
86%
HuggingFace
55%
75%
100%
58%
Coursera
44%
47%
67%
39%
GLM-5 and MiniMax M2.5 dominate, but along different axes. GLM-5 wins where depth matters (Google Maps, HuggingFace, Coursera): structured data extraction and multi-step reasoning. MiniMax M2.5 wins where interaction matters (Booking, Amazon, GitHub): form flows and dynamic navigation. The split maps directly to their training — GLM-5 as a general reasoning model, MiniMax M2.5 as the only model in the lineup with RL-based agent training across real-world environments. The execution-tax story is consistent with both: wherever tasks compound across many steps, models with clean structured output and efficient step counts pull ahead, regardless of raw token intelligence.
Gemini's One Win: Google Flights
Gemini leads on exactly one website: Google Flights (83% vs 58–75%). Notably, a Google property. Whether the advantage comes from training data familiarity, an optimised DOM structure aligned with Gemini's text representation, or simply good fortune on these specific tasks is unclear. But it is the only site where Gemini outperforms all three Fireworks models.
What This Means for AI Procurement
When evaluating foundation models for an agent deployment, three metrics should drive the decision. Three should not.
Use these:
•
Cost per successful task
(not cost per token): captures retry waste, step efficiency, and success rate in a single number
•
Parse retry rate
(or execution tax): reveals how much of your inference budget is wasted on malformed outputs before you ever see a result
•
Reliability-Adjusted Accuracy
: combines task success with execution reliability into a single production-representative score
•
Infrastructure consistency under load
: predictable latency, retry handling, and structured-output stability become increasingly important as agent systems scale from demos to production workloads
Do not lead with these:
•
Token pricing
: Gemini is cheaper per token than Kimi; it is 2.3x more expensive per outcome
•
Benchmark reasoning scores
: MMLU and HumanEval do not measure structured output compliance across a multi-step loop
Procurement Scorecard
GLM-5
MiniMax M2.5
Kimi K2.5
Gemini 2.5 Flash
Task accuracy
57.1%
57.5%
49.7%
45.0%
Cost / successful task
$0.217
$0.062
$0.167
$0.141
Execution tax
0.6%
1.6%
0.0%
22.9%
Reliability-Adjusted Accuracy
56.8%
56.6%
49.7%
34.7%
Avg LLM latency (p50)
5,634ms
3,051ms
2,145ms
2,476ms
Production cost at 10k tasks/day
High
Lowest
Mid
High (retry waste)
Enterprise deployment readiness
High
Highest
High
Limited
MiniMax M2.5 occupies the dominant position for most production workloads: highest accuracy, lowest cost per outcome, negligible execution overhead. GLM-5 is the choice where accuracy on complex tasks is non-negotiable. Kimi K2.5 is the choice where real-time responsiveness matters most.
Model Profiles: Three Models, Three Strategies
GLM-5: The Reasoning Powerhouse
57.1% accuracy | 6.3s avg LLM latency | $0.217/successful task | 0.6% execution tax
Highest accuracy on sites requiring multi-step reasoning: Google Maps (100%), HuggingFace (100%), BBC News (100%), ArXiv (77%), Coursera (67%). Trades speed for depth; longer per call, fewer mistakes on complex tasks.
Best for:
Batch and background workloads where accuracy matters more than latency. High-reliability pipelines where incorrect outputs carry downstream consequences: data extraction, compliance workflows, research automation.
MiniMax M2.5: The Best Value
57.5% accuracy | 3.7s avg LLM latency | $0.062/successful task | 1.6% execution tax
Matches GLM-5's accuracy at less than one-third the cost per successful task. Strongest on Amazon (88%), Google Maps (100%), Booking (33%, the only model to consistently complete booking flows), GitHub (39%), and ArXiv (86%). The only model in the lineup with RL-based agent training: it solves tasks in the fewest steps (9.8 avg) and takes the most direct paths.
Best for:
Cost-sensitive production workloads at high volume. The default choice for most scaled deployments; the 2.3x cost advantage over Gemini per successful task compounds significantly across thousands of daily tasks.
Kimi K2.5: Fastest Inference in This Benchmark
49.7% accuracy | 2.3s avg LLM latency | $0.167/successful task | 0.0% execution tax
Fastest inference (p50: 2,145ms), lowest token consumption, and zero parse retries across 852 calls. Competitive across the board with ESPN (100%), Cambridge Dictionary (100%), HuggingFace (75%), and ArXiv (57%). Fireworks' infrastructure and
quality validation pipeline and work on Kimi K2.5
are designed around sustained production inference behavior, not just benchmark throughput, which becomes especially important in long-running agent loops where retry amplification compounds quickly.
Best for:
Real-time agent applications where users watch the agent act. Customer-facing automation, live demos, and interactive workflows where perceived responsiveness affects user trust.
The Vision Question
All results above are text-only. We also ran a supplementary vision experiment with Gemini 2.5 Flash:
Metric
Text-Only
Vision
Delta
Eval Success Rate
47%
53%
+6pp
Avg Duration
70s
85s
+15s
Hard Errors
7
2
-5
Vision gives a meaningful accuracy boost (+6pp) at the cost of ~15s per task. Biggest gains on visually complex sites: GitHub (+34pp), ESPN (+33pp), Coursera (+23pp).
The critical point:
Even with Gemini's vision advantage fully restored (53%), MiniMax M2.5's text-only score (57.5%) still beats it. Vision narrows the gap but does not close it, and the Fireworks models have not yet had the opportunity to use vision themselves.
Kimi K2.5 Vision: Infrastructure Constraint, Not Model Limitation
We attempted to run Kimi K2.5 with vision enabled to make the multimodal comparison symmetric across the Fireworks lineup.
87 of 90 tasks timed out on Fireworks' serverless GPU infrastructure; only 3 completed.
The 3 that did complete ran cleanly — the model is capable; serverless capacity was not sized for sustained vision workloads at benchmark scale during our test window.
This is explicitly an infrastructure limitation, not a model limitation. A dedicated deployment — which Fireworks offers for production customers — would resolve it. We flag it directly here rather than omit it because the Fireworks-side vision comparison is incomplete for this round, and any interpretation of the text-only results should account for that gap. A follow-up benchmark on dedicated vision capacity is on the roadmap.
Closing
The bottleneck in agentic AI is not intelligence alone. It is execution across the full stack.
Reliable agents require more than strong models: they require inference infrastructure that can sustain low-latency, structured, repeatable execution under production workloads.
The Agent Execution Tax — the hidden overhead of malformed outputs, wasted retries, and inflated call counts — is the gap between what models can do and what they reliably deliver in production. For the proprietary baseline in our benchmark, that tax consumed nearly a quarter of all inference. For the best open-weight models on Fireworks, it was effectively zero.
This is not a fixed property of proprietary versus open models. It is an engineering problem, solvable with the right models, infrastructure, and training data. The base capabilities are measured. The training data — hundreds of successful trajectories generated by this benchmark itself — is ready. A follow-up post will report the results of fine-tuning the top-performing open model on that data.
For organisations evaluating agentic AI at scale, execution reliability should gate how accuracy is interpreted across procurement decisions, infrastructure design, and deployment strategy.
The serving layer matters as much as the model.
Low-variance tail latency across architectures, sustained structured-output stability under repeated correction loops, and retry-safe handling that contains malformed outputs without exhausting the budget — the three properties Fireworks demonstrated across the 720 runs in this benchmark.
Appendix
A. Reproducibility
This benchmark is fully reproducible. All models use serverless inference (no dedicated deployments), and the task suite is public.
Requirements:
•
A Fireworks AI API key (
fireworks.ai
)
•
An OpenRouter API key (for Gemini baseline + evaluator)
•
The Notte framework (
pip install notte-agent
)
To run:
# Example: run Kimi K2.5 on the WebVoyager benchmark
uv run pytest packages/notte-eval/src/notte_eval/webvoyager/test_run.py \\
--task_dir "webvoyager/webvoyager_simple.jsonl" \\
--model "fireworks_ai/accounts/fireworks/models/kimi-k2p5" \\
--n_runs 3 --use_vision false --headless true --max_steps 20 -v
Full instructions, code changes, and analysis scripts are documented in
fireworks/FIREWORKS_BENCHMARK.md
.
B. Benchmark Configuration
Parameter
Value
Task suite
WebVoyager (60 tasks, 15 websites)
Runs per model
3 per task (180 per model, 720 total)
Max steps
20
Temperature
0.0
Vision
Disabled (text-only)
Response format
json_object (non-strict)
Browser
Chrome, headless
Evaluator
Gemini 2.5 Flash via OpenRouter (LLM judge)
C. Evaluator Methodology
The WebVoyager evaluator uses Gemini 2.5 Flash as an LLM judge. This is the same model as the proprietary baseline, which creates a theoretical risk that the judge may favour outputs resembling its own reasoning style. We accept this trade-off because: (a) the evaluator judges task outcomes (did the agent reach the correct answer?), not reasoning style; (b) the judge sees only the final answer and screenshot, not intermediate reasoning chains; and (c) changing the evaluator would break comparability with Notte's existing benchmark results.
Critically, this risk cuts in the direction that would weaken our thesis, not strengthen it: any same-judge bias would inflate Gemini's scores, not suppress them — yet Gemini still finished last on every reliability-adjusted metric in this benchmark. The result holds in the direction least favourable to our argument.
D. Full Per-Site Breakdown (Numeric Reference)
Website
Gemini 2.5 Flash
Kimi K2.5
GLM-5
MiniMax M2.5
AllRecipes
0% (0/12)
0% (0/12)
17% (2/12)
9% (1/11)
Amazon
70% (7/10)
70% (7/10)
55% (6/11)
88% (7/8)
Apple
0% (0/9)
43% (3/7)
22% (2/9)
30% (3/10)
ArXiv
40% (6/15)
57% (8/14)
77% (10/13)
86% (12/14)
BBC News
83% (5/6)
67% (4/6)
100% (6/6)
75% (3/4)
Booking
0% (0/12)
9% (1/11)
0% (0/12)
33% (4/12)
Cambridge Dictionary
100% (12/12)
100% (12/12)
100% (12/12)
100% (12/12)
Coursera
44% (8/18)
47% (8/17)
67% (12/18)
39% (7/18)
ESPN
83% (5/6)
100% (6/6)
100% (6/6)
100% (6/6)
GitHub
22% (4/18)
17% (3/18)
28% (5/18)
39% (7/18)
Google Flights
83% (10/12)
75% (9/12)
58% (7/12)
75% (9/12)
Google Maps
58% (7/12)
58% (7/12)
100% (11/11)
100% (12/12)
Google Search
8% (1/12)
8% (1/12)
0% (0/12)
0% (0/12)
HuggingFace
55% (6/11)
75% (9/12)
100% (12/12)
58% (7/12)
Wolfram Alpha
100% (6/6)
83% (5/6)
100% (6/6)
100% (6/6)
E. Data Files
Directory
Contents
Runs
results_gemini/
Gemini 2.5 Flash, batch 1
90
results_gemini_v2/
Gemini 2.5 Flash, batch 2 (instrumented)
90
results_kimi/
Kimi K2.5, batch 1
90
results_kimi_v2/
Kimi K2.5, batch 2 (instrumented)
90
results_glm/
GLM-5, batch 1
90
results_glm_v2/
GLM-5, batch 2 (instrumented)
90
results_minimax/
MiniMax M2.5, batch 1
90
results_minimax_v2/
MiniMax M2.5, batch 2 (instrumented)
90
results_gemini_vision/
Gemini 2.5 Flash with vision
90
results_kimi_vision/
Kimi K2.5 with vision (mostly failed)
90
fireworks/
Benchmark plan, partnership notes, vision findings
-
Each task directory contains per-run output JSONs (with full step traces, token counts, and logs), screenshots, and error tracebacks where applicable. Batch 2 (
*_v2
) directories include instrumented logs with per-call LLM latency, parse retry counts, and parse failure counts.
Benchmark conducted by
Notte
. All models tested on their publicly available serverless API endpoints. Pricing as of March 2026.
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
