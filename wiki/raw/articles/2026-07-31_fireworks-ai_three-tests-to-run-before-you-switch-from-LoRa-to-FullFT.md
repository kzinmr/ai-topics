---
title: "Three Tests to Run Before You Switch from LoRA to FullFT"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/three-tests-to-run-before-you-switch-from-LoRa-to-FullFT"
scraped: "2026-07-31T06:00:02.264015+00:00"
lastmod: "2026-07-31T01:16:03.000Z"
type: "sitemap"
---

# Three Tests to Run Before You Switch from LoRA to FullFT

**Source**: [https://fireworks.ai/blog/three-tests-to-run-before-you-switch-from-LoRa-to-FullFT](https://fireworks.ai/blog/three-tests-to-run-before-you-switch-from-LoRa-to-FullFT)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Three Tests To Run Before You Switch From Lora To Fullft
Three Tests to Run Before You Switch from LoRA to FullFT
PUBLISHED
7/30/2026
Table of Contents
Experimenting with LoRA
The test bed: Qwen3.5-9B
How this relates to prior work
Placement: rank test → data coverage → tuned learning rate
Register allocation: where rank moved the result
Nexa VM: fixed recipe → tuned learning rate → rank sweep → broader curriculum
First, recipe tuning erased a fixed-recipe FullFT advantage
On supported behavior, the rank ladder hit a ceiling
Beyond the horizon, curriculum coverage moved the result
Three-task mixture: matched exposure → fixed budget → recipe sweep
What did the fixed-budget runs cost?
What moved the results
Before you switch from LoRA to FullFT
Fireworks: one platform for inference and training
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
Experimenting with LoRA
The test bed: Qwen3.5-9B
How this relates to prior work
Placement: rank test → data coverage → tuned learning rate
Register allocation: where rank moved the result
Nexa VM: fixed recipe → tuned learning rate → rank sweep → broader curriculum
First, recipe tuning erased a fixed-recipe FullFT advantage
On supported behavior, the rank ladder hit a ceiling
Beyond the horizon, curriculum coverage moved the result
Three-task mixture: matched exposure → fixed budget → recipe sweep
What did the fixed-budget runs cost?
What moved the results
Before you switch from LoRA to FullFT
Fireworks: one platform for inference and training
Table of Contents
If training with LoRA isn't producing the results you were expecting, the adapter itself may not be the problem. We did controlled experiments on Qwen3.5-9B showing how data coverage, optimization, and rank can create or close the quality gap to Full Parameter Fine-Tuning, or FullFT.
Which lever moved?
Within-experiment changes; gray cells were not tested
In our earlier
Kimi K3 work
, LoRA was fast, inexpensive, and effective for bounded objectives, and we drew a line: broad or genuinely novel targets are stronger reasons to test FullFT.
Before you reach for that more expensive FullFT, you should know that in our experiments when a FullFT beat a simple LoRA run, it was hard to tell whether the adapter simply needed better data, a better training recipe, more rank to close the gap, or whether FullFT was genuinely the better method all along.
Experimenting with LoRA
LoRA freezes the base model and trains a small adapter instead. FullFT updates every model weight. When FullFT performs better, it is tempting to conclude that the adapter is simply too small. Our experiments explored three possible explanations:
•
Coverage:
The training data did not show enough of the task's variety. The test: broaden the data and re-measure.
•
Optimization:
The training recipe, especially the learning rate, the size of each training adjustment, was poorly tuned. The test: sweep the learning rate and schedule.
•
Adapter capacity:
The LoRA adapter needed a higher rank — a larger adapter. The test: increase rank while holding update scaling and the rest of the recipe fixed, and look for validity and quality to improve together.
An intervention shows which change helped under the tested conditions. It does not prove that the lever was the only cause or rule out other contributing factors.
The test bed: Qwen3.5-9B
We used Supervised Fine-Tuning (SFT) on Qwen3.5-9B and compared LoRA with FullFT. Within each comparison, both methods received the same prompts, targets, and evaluation code.
We tested three synthetic tasks with automatic checkers: each task comes with the equivalent of a unit-test suite, so every answer could be scored without a human judge:
•
Placement, borrowed from chip design:
Arrange components on a line to minimize wiring while obeying hard constraints. One violated constraint invalidates the answer.
•
Register allocation, borrowed from compilers:
Assign processor registers so values that are in use at the same time never share one.
•
Nexa VM:
Execute a program written in a synthetic instruction language and report every intermediate state. Program "depth" is its number of instructions.
We picked tasks that have programmatic checks for validity, solution quality, and exact execution. That matters because a model can reach nearly zero training loss and still fail when one wrong decision invalidates the whole answer.
How this relates to prior work
Biderman et al. (
LoRA Learns Less and Forgets Less
, 2024) reported that LoRA trails FullFT on demanding domains such as code and math while preserving more of the base model. Thinking Machines (
LoRA Without Regret
, 2025) reported that a well-configured LoRA can match FullFT across much of post-training, with an optimal learning rate roughly an order of magnitude above FullFT's. Our results point the same direction: the best LoRA rate here, 8e-5, sat far above the best FullFT rate, 1e-6 on Nexa. What we add is narrower: a per-gap protocol for testing whether coverage, optimization, or adapter capacity explains a specific FullFT advantage.
Placement: rank test → data coverage → tuned learning rate
Placement asks the model to arrange cells on a line while minimizing total wire length. In the hard version, a single forbidden position or separation violation invalidates the answer, and that all-or-nothing check revealed a clear LoRA–FullFT gap. We first tested rank, then data coverage:
Placement coverage test
LoRA-r32
LoRA-r128
FullFT
2k rows, original seed
34.33%
31.67%
57.00%
2k rows, new data and training seed
37.33%
36.67%
61.67%
20k rows, default recipe
68.33%
69.33%
80.33%
Each held-out set contains 300 examples, and a separately generated dataset and training seed reproduced both the flat rank-32 versus rank-128 result and the direction of the FullFT gap. Both adapters reached 100% validity on sampled training prompts, yet more rank did not improve held-out generalization. We define
validity
as the final output passing the task's checker. An
exact sequence
or
exact trace
matched the reference answer step for step.
Acing the practice questions did not mean passing the new exam.
On the same 6,000-step budget, ten times more unique data roughly doubled LoRA validity and cut the FullFT gap in half; quadrupling rank moved the result by one point.
Coverage was only part of the story. On a common selection suite, default rank-32 LoRA reached 76.33% validity and FullFT reached 83.00%. Holding the data and training budget fixed, we raised LoRA's peak learning rate:
20k placement recipe, common suite
Validity
LoRA-r32, 2e-5
76.33%
LoRA-r128, 2e-5
74.00%
LoRA-r32, 8e-5
82.67%
LoRA-r128, 8e-5
82.00%
FullFT
83.00%
At this sample size, the evaluation could not distinguish tuned rank-32 LoRA from FullFT: the 0.33-point difference had a 95% confidence interval of −4.33 to +5.00 points, which is not evidence that the two methods are equivalent. The selected rank-32 recipe then reached 81.67% on an untouched final suite, compared with 80.33% for FullFT.
Verdict:
The adapter was not too small. The gap came from the training data and the learning rate. More varied data and a higher learning rate closed it; making the adapter four times larger moved the result by one point.
Register allocation: where rank moved the result
Register allocation maps interfering virtual registers onto different physical registers. One conflict makes the allocation invalid. The main evaluation contains 400 held-out graphs.
Placement shows why rank is not always the answer. Here, rank moved the observed result.
Method
Valid allocation
Matches reference register count
Exact decision sequence
LoRA-r8
80.50%
65.75%
3.50%
LoRA-r32
82.50%
69.00%
6.00%
LoRA-r128
90.50%
81.00%
25.50%
FullFT
93.00%
83.75%
35.50%
Moving from rank 32 to 128 improved validity by eight points. It also improved solution quality and exact policy imitation in the same direction. Rank 128 recovered most of the operational gap to FullFT. FullFT retained an advantage in exact trace reproduction. Note what that last metric measures.
Two valid allocations are two routes reaching the same destination. Exact sequence requires taking the reference route.
A lead on exact sequence is a lead in imitation, and does not translate one-for-one into practical quality.
A separate 60-graph control reproduced the direction: r32/r128/FullFT reached 83.33%/90.00%/90.00% validity. The sample is too small to estimate the effect precisely, and we have not completed placement-style coverage and LR controls here. Rank clearly moved validity and quality under the tested recipe, and we have not excluded coverage or optimization as we did for placement.
All register-allocation LoRAs adapted the attention and feed-forward weight matrices. Alpha increased proportionally with rank, keeping
alpha/rank = 2
, which held the nominal update scaling constant while increasing adapter capacity.
Verdict:
Here, adapter size was the lever. A larger adapter improved validity and solution quality together, which is the pattern that points to size. The data and learning-rate checks that would confirm it are still open.
Nexa VM: fixed recipe → tuned learning rate → rank sweep → broader curriculum
Nexa VM asks the model to execute short programs and reproduce the exact state trace. It gives us all three tests (recipe, rank, and coverage) inside one task.
A minimal held-out program shows the exact-execution format:
1
2
3
4
5
6
7
8
9
10
Execute the Nexa VM program using the learned opcode semantics.
Return each bound register in order, then the final output.
program {
input r0 := -0027.
input r1 := -0025.
input r2 := +0012.
bind r3 := baf<r0>.
yield r3.
}
trace
The exact trajectory is:
1
2
r3 = -0027.
output -0027.
The longer depth-24 suite applies the same format across 24 dependent instructions, where one post-horizon error can compound through the remainder.
First, recipe tuning erased a fixed-recipe FullFT advantage
An early 10,000-row comparison made FullFT look much more sample efficient. Under the original recipes, it led LoRA by 20 points on depth-eight final answers and 31 points on exact traces.
A same-suite learning-rate sweep reversed that interpretation:
Tuned 10k recipe, depth-8 subset (n=64)
Peak LR
Final answer
Exact trace
LoRA-r64
8e-5
98.44%
96.88%
FullFT
1e-6
96.88%
95.31%
The table reports the 64-example depth-8 subset. Across the full 480-example suite, LoRA and FullFT reached 478 versus 476 correct final answers and 475 versus 474 exact traces. Learning-rate tuning removed the fixed-recipe FullFT advantage.
Verdict:
A 31-point gap that looked like FullFT learning faster was really an untuned learning rate. Tuning it is the cheapest step in the ladder, and it removed the largest apparent method difference in the study.
On supported behavior, the rank ladder hit a ceiling
We then trained on 100,000 depth-1–8 programs and swept LoRA ranks
{64, 32, 16, 8, 4, 2, 1}
. Exact-trace accuracy stayed between 99.17% and 100%. Supported behavior did not separate the tested ranks.
A separate control trained on the same token count landed near the same ceiling:
Token-matched Nexa control
Final-answer accuracy
Exact-trace accuracy
Depth-extrapolation exact
Sampled train fit
LoRA-r32
99.17%
97.92%
92.97%
100%
LoRA-r128
99.17%
98.33%
94.53%
100%
FullFT
96.88%
95.42%
82.81%
100%
In the control, r128 improved exactness over r32 by two of 480 examples. All ranks were already near ceiling, so supported Nexa behavior did not expose an active adapter-capacity bottleneck. The lower FullFT result describes its tested recipe; it is not evidence that LoRA is intrinsically better.
Beyond the horizon, curriculum coverage moved the result
The failure mode changed on longer programs. Models trained on a fixed range of register positions became less reliable when depth-16 programs introduced new positions. Increasing rank did not produce a monotonic recovery. Randomizing register starts during training did:
Depth-16 exact trace
Fixed register range
Random register starts
LoRA-r64
96.09%
100.00%
FullFT
64.84%
99.22%
The coverage horizon:
The fixed curriculum taught transitions only at familiar register positions. Increasing rank could not supply missing examples; random register starts expanded the support and repaired the depth-16 trace.
Broader register-position coverage moved FullFT by 34.38 points and LoRA by 3.91. Rank had not produced a monotonic recovery. Depth-24 exactness remained lower (89.84% for LoRA and 80.47% for FullFT), so coverage extended rather than eliminated the reliability boundary.
These are method-specific recipes: FullFT was not freshly LR-swept on the random-offset curriculum. And unlike the register-allocation sweep, the Nexa rank ladder held absolute alpha fixed, so rank and effective update scale changed together; the Nexa rank results do not isolate adapter capacity as cleanly. The results establish optimization and coverage responses without excluding every rank-recipe interaction.
Nexa makes the central lesson concrete. Here, a flat rank curve marked either spare capacity at a ceiling or missing support at a coverage boundary. The intervention response distinguished the two; the curve alone could not.
The model learned the rule only for the register positions it saw in training. A perfect training score and flawless step-by-step traces did not reveal that. The gap appeared only when new positions showed up.
Verdict:
On this task all three levers got tested, and two of them did the work: first the learning rate, then broader training data. The 34-point jump FullFT gained from broader data is the largest single effect in the study.
Three-task mixture: matched exposure → fixed budget → recipe sweep
So far, every experiment adapts one bounded task. What happens when one model has to learn all three?
We combined placement, register allocation, and Nexa into one tagged mixture.
First, we preserved each task's original token exposure. That required 18,000 steps, three times the single-task budget.
The three-task average below gives equal weight to placement validity, register-allocation validity, and Nexa exact-trace accuracy; it is not a pooled accuracy over all examples.
Exposure-matched mixture
LoRA-r32
LoRA-r128
FullFT
Three-task average
86.92%
86.11%
84.58%
Placement validity
70.33%
73.33%
75.00%
Register-allocation validity
96.67%
93.33%
88.33%
Nexa exact-trace accuracy
93.75%
91.67%
90.42%
With per-task exposure preserved, neither higher rank nor the tested FullFT recipe improved the macro score. This mixture did not expose a breadth-induced capacity bottleneck.
Then we held the total token and step budget fixed at the single-task level. Each task received roughly one-third as much exposure.
Fixed-budget mixture
LoRA-r32
LoRA-r128
FullFT
Three-task average
69.64%
71.65%
80.89%
Placement validity
61.00%
59.33%
62.67%
Register-allocation validity
60.00%
66.67%
85.00%
Nexa exact-trace accuracy
87.92%
88.96%
95.00%
This protocol asks which method performs better with the same data and number of optimizer steps, and does not ask which is more compute-efficient at matched training FLOPs. FullFT led, and recipe quality remained a confound, so we swept the mixture's compromise LoRA learning rate and schedule.
The table combines six new sweep arms with the two original
4e-5
cosine baselines:
Fixed-budget LoRA recipe
Three-task average
r32, 2e-5, cosine
63.29%
r32, 4e-5, cosine (original)
69.64%
r32, 4e-5, constant
71.54%
r32, 8e-5, cosine
75.25%
r128, 2e-5, cosine
59.60%
r128, 4e-5, cosine (original)
71.65%
r128, 4e-5, constant
70.86%
r128, 8e-5, cosine
76.60%
At rank 32,
8e-5
added 5.61 points over the original recipe. At that tuned rate, rank 128 added another 1.35 points, reaching 76.60%. Together, recipe and rank recovered 6.96 of the original 11.25-point r32 deficit. FullFT still led the best adapter by 4.29 points.
The response is recipe-dependent. Low-LR r128 fell 12.05 points below its original result, while constant
4e-5
reached only 70.86%. Tuned r128 produced valid outputs on every sampled training example across all three tasks, yet FullFT remained ahead on every held-out task: placement, register allocation, and Nexa.
The fixed-budget result is single-seed; a replication seed is queued and we will update this section with it. Relative to the best LoRA recipe tested:
Under a fixed multi-task budget, FullFT is less sensitive to diluted per-task exposure in our tested recipes. Optimization explains most of the original r32 deficit, and rank provides a smaller secondary recovery. A 4.29-point lead remains over the best LoRA recipe tested so far. That remaining gap does not prove that LoRA itself lacks capacity.
When per-task exposure is preserved, the tested LoRA recipes match or beat the tested FullFT recipe. When the budget is fixed and per-task exposure is diluted, FullFT is the more forgiving method under the recipes tried so far. Neither row is the general answer; the protocol is part of the result.
What would resolve the remaining 4.29 points? The candidates we have not yet run: a rank-256 arm at the tuned rate, a per-rank alpha and LR sweep on the mixture, per-task adapters served side by side instead of one shared adapter, and a fresh FullFT LR sweep at the mixture level to confirm its recipe is not similarly undertuned. That is the follow-up experiment set, and we will publish it either way.
Fixed-budget mixture: where the gap went
Three-task average after learning-rate and rank interventions
Optimization recovers 5.61 points and tuned rank adds 1.35 more; FullFT retains a 4.29-point lead under the fixed-budget protocol.
What did the fixed-budget runs cost?
All four runs processed 12.02 million supervised response tokens (the tokens the loss is computed on) for 6,000 steps on two B200 GPUs. Using Fireworks' public
$10 per B200 GPU-hour
dedicated-training rate:
Method
Macro score
Active training time
Active-cost lower bound
Original LoRA-r32
69.64%
2.70 h
$53.97
Tuned LoRA-r32
75.25%
2.57 h
$51.38
Tuned LoRA-r128
76.60%
3.23 h
$64.53
FullFT
80.89%
3.50 h
$70.06
FullFT's final 4.29-point lead cost 8.6% more active training compute than tuned r128. These are lower bounds from time spent updating weights: they exclude provisioning, checkpointing, evaluation, and idle time.
Serverless Training estimate
Value
Training-datum tokens
62.74M
Qwen3.5 9B train price
$1.463 / 1M tokens
Estimated cost
$91.79
Serverless billing counts training-datum tokens, meaning every token in the training rows, which is why this figure (62.74M) is larger than the 12.02M response tokens above. This is a list-price estimate, and the dedicated figures above are active-time lower bounds rather than billed totals.
Training cost is only half of the comparison. Adapters trained here can share one base-model deployment: many LoRAs served concurrently on the same replica, each swapped in per request. A FullFT model needs its own dedicated deployment. For a team running several specialized behaviors, the serving-side difference can outweigh a single-run training delta, so the cost gate in the ladder below should compare training plus serving for the fleet you actually plan to run, and a small quality lead has to pay for a dedicated deployment before it wins.
What moved the results
Targeted data coverage, recipe optimization, and increased adapter rank all had a part in closing the quality gap to FullFT, but FullFT retained a lead when per-task exposure was diluted and no single intervention eliminated the gap across all scenarios.
Setting
Intervention that moved the result
Evidence
Residual result
Placement
More varied data, then a better learning rate
Increasing the dataset 10× raised LoRA validity from 34.33% to 68.33%. Raising its learning rate added another 6.34 points on a common comparison suite.
FullFT led by 0.33 validity points, within the confidence interval.
Register allocation
A larger adapter
Increasing rank from 8 to 128 added 10 validity points. Solution quality and exact-sequence accuracy moved in the same direction.
FullFT retained a 10-point lead on exact sequence, a stricter imitation metric. Coverage and learning-rate controls remain open.
Nexa VM at trained program lengths
A better learning rate
A learning-rate sweep reversed an apparent 31-point FullFT advantage.
Tuned LoRA finished slightly ahead: two more correct final answers and one more exact trace across 480 examples.
Nexa VM beyond trained program lengths
More representative data
Randomizing the initial register positions raised FullFT by 34.38 points and LoRA by 3.91 points.
LoRA reached 100% exact trace and FullFT reached 99.22%.
All three tasks in one model, with a one-task-equivalent training budget
A better learning rate, then a larger adapter
Learning-rate tuning recovered 5.61 points on the three-task average score. Increasing rank to 128 recovered another 1.35 points.
FullFT retained a 4.29-point lead on the three-task average that none of the tested interventions eliminated.
The same three-task mixture, with data exposure matched
The comparison protocol
Matching data exposure changed which method finished ahead.
LoRA led.
Across the four single-task settings, data coverage or optimization eliminated the apparent FullFT advantage in three. Higher rank materially improved the fourth, although coverage and learning-rate controls remain open.
In the combined-task experiment, the result depended on what the comparison held constant. Under a one-task-equivalent training budget, FullFT retained a 4.29-point lead on the three-task average. With data exposure matched, LoRA led.
A FullFT win tells you that a performance gap exists. It does not tell you what caused it.
Before replacing LoRA with FullFT, consider your coverage, recipe, and LoRA rank.
Before you switch from LoRA to FullFT
Evaluate the outputs you will ship.
That means don't focus on training loss alone. A model can fit the training data and still fail on new examples, hard constraints, or multi-step execution.
Start with LoRA on a task that is narrow and testable.
You should be able to describe the target behavior clearly and measure whether the model learned it.
When failures cluster around missing cases, begin broadening the data.
Add more combinations, edge cases, and task variation the model is getting wrong.
When more data helps but a gap remains, tune the training recipe.
Test the learning rate and schedule rather than reusing FullFT defaults. LoRA often prefers a substantially higher learning rate.
Test adapter capacity last.
If higher rank improves both validity and quality, the smaller adapter was part of the constraint.
Compare total economics once multiple methods meet the quality bar.
Include training, iteration speed, serving, and the cost of maintaining a separate FullFT deployment.
Use FullFT when its quality advantage survives these tests and justifies the added cost.
These experiments cover one model and three synthetic, verifiable tasks, closer to a wind tunnel than a production workload.
The diagnostic process travels; the specific numbers may not.
Fireworks: one platform for inference and training
You can run these experiments yourself with
Fireworks Serverless Training and Inference
. The fixed-budget mixture above cost $91.79 at the public Qwen3.5-9B rate at time of publishing. From there, train adapters at multiple ranks, serve them on a shared base deployment, and collect failures in production.
When the evidence points beyond LoRA, the same SDK extends to dedicated B200 training at $10 per GPU-hour without rebuilding the workflow. LoRA is the right way to start; keep the ceiling open, and make the method choice an experiment instead of an infrastructure constraint.
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
