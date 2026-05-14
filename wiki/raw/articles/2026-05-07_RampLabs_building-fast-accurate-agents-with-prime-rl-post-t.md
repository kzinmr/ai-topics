---
title: "Building Fast & Accurate Agents with Prime-RL Post Training "
created: 2026-05-07
date_ingested: 2026-05-14
type: x_article
x_article_tweet_id: "2052447438795833506"
x_article_author: "Ramp Labs"
x_article_author_handle: "@RampLabs"
source: "https://x.com/RampLabs/status/2052447438795833506"
tags: [x-article]
---

A spreadsheet agent is only as good as the information it retrieves. If it reads too little, it misses the answer. If it reads too much, it becomes slow, expensive, and easier to distract with irrelevant tabs.
In Ramp Sheets, we built Fast Ask to handle that retrieval loop. Given a question like “What was the revenue from March to May?”, Fast Ask navigates the workbook, reads the relevant ranges, and returns a compact answer for the main agent to use. We partnered with Prime Intellect to post train an open source Qwen model for this workflow using their RL training stack. We use Fast Ask here as a case study for RL post training: when it is worth training a specialized agent, how to design the environment, and how to evaluate whether post training worked.
 
Motivation
In our traces, we observed substantial exploration overhead and, in practice, a significant amount of wasted time. The main agent spent 17.8% of all tool calls opening tabs, reading ranges, and filtering irrelevant sheets before it had the data needed to answer. About 75% of those calls were immediately followed by another read call, suggesting the agent often failed to retrieve the right information on the first attempt.
Prompting alone would still leave the core loop unchanged: a large, slower general purpose model responsible for navigating spreadsheets and filtering irrelevant information. Instead, we post trained an open source Qwen model into a specialized retrieval subagent. This let us move retrieval into a smaller, faster model while preserving accuracy and achieving the latency profile needed for production.
The resulting Fast Ask model, a finetuned Qwen3.5-35B-A3B variant with roughly 3 billion active parameters, runs at about Haiku 4.5 latency. On our held out eval, Fast Ask beat Claude Opus 4.6 by 4% points on exact match accuracy. This makes the final agentic system both faster and more accurate.
Why Retrieval Deserves Its Own Subagent
Retrieval is a good target for a specialist model for three reasons.
First, it protects the main agent's context. If the main model reads every tab, it burns tokens on irrelevant rows and can anchor on decoys. A retrieval subagent can return only the answer relevant cells or computed value.
Second, retrieval is latency sensitive. The user experience is much better if the main agent gets the needed spreadsheet fact quickly instead of spending many turns exploring the workbook.
Third (and most importantly) retrieval is verifiable. Unlike open ended financial reasoning, many spreadsheet questions resolve to an exact value: a date, an invoice ID, a cent amount, a yes/no answer, or a row reference. That makes the task a natural fit for RL because we can score trajectories deterministically.
These properties made retrieval a strong fit for RL post training. The task was narrow, repeated often, sensitive to latency, and objectively scorable.
 
Experimental Setup
We made the workflow trainable with RL by framing spreadsheet interaction as an environment with many related tasks, a small tool interface, and a deterministic reward function. Rather than training on demonstrations of correct behavior, the model learns through reinforcement learning, discovering its own strategies for navigating workbooks, retrieving data, and computing answers.
We used Qwen/Qwen3.5-35B-A3B as the base model and trained on Prime Intellect's Lab platform with their Hosted Training infrastructure and verifiers framework. The training environment mirrors our production deployment harness directly.
The run used 100 training steps, batch size 256, and 8 rollouts per example. Evaluation ran every 20 steps on 128 held out examples, with the base model evaluated alongside the trained checkpoint. We disabled thinking mode so the comparison matched the low latency production setting we cared about.
Synthetic Dataset
Each task consists of a synthetic business workbook, a natural language question, and a ground truth answer. The workbooks are designed to reflect real finance workflows: revenue rollups, invoice reconciliation, spend analysis, time filtered lookups, and multi join aggregations.
Synthetic data let us scale the task distribution while keeping it reliable. It allows us to generate many variations of the same retrieval problem, control the answer exactly, and vary surface phrasing without changing the underlying skill being trained.
We defined 14 task types across three families:
 
For each task, we generated three differently phrased variants, such as investor memo requests, collections follow ups, and fundraise model questions. This prevents the model from overfitting to a single prompt template. Reconciliation tasks add more variation through invoice descriptors, payment clues, and customer/date/amount signatures, expanding the effective prompt space beyond 3 per type.
Example:
I am tightening our investor memo. What cumulative net recognized revenue did South land across 2025-03 to 2025-05, in USD cents?Sheets: ['Orders', 'OrderLines', 'Shipments', 'Returns', 'OrderMonthNet', 'FxExposure', 'Contracts', 'FXRates', 'Targets', 'HiringPlan', 'CapTable']
Training batches are assembled with balanced round robin: every pass through the dataset shuffles and emits all 14 task types before repeating, ensuring uniform coverage ¹.
Adversarial Workbook Design
We used difficulty levels to control how much navigation pressure the model faced. Easy tasks usually exposed a direct path to the answer. Medium and hard tasks used three strategies to increase difficulty: distractors, unreliable shortcuts, and ambiguous identifiers.
The difficulty knobs made the policy more robust. By varying distractors, helper summaries, and ambiguous identifiers, we trained the model on the kinds of navigation failures it would face outside the synthetic environment.
Decoy sheets. At medium and hard difficulty, revenue workbooks include finance adjacent but answer irrelevant tabs like HiringPlan and CapTable, with recruiter names, open roles, option pools, and similar planning data. These sheets contain no information needed for the target question. A model that reads indiscriminately wastes its turn budget on them.
Partial helper summaries. Some workbooks include summary sheets like RegionalPnL or SpendSummary, but omit the computed columns needed to answer the question directly. The model sees a tab that looks like a shortcut, but still has to verify or aggregate from source data. At hard difficulty, helper summaries are removed entirely.
Identifier obfuscation. In roughly 15-20% of reconciliation tasks, the question references an invoice not by its INV-#### ID, but by a payment clue such as source system, method, date, and amount, or by a signature such as customer, month, amount, and due date. The model has to resolve the reference before it can answer.
Tool Interface
The model gets three tools and a budget of 15 turns:
get_workbook_metadata returns sheet names, tab colors, and approximate used_ranges.
read_ranges returns cell data, hard capped at 1,000 cells per call. Oversized requests are rejected.
run_python executes sandboxed Python (standard library only). State persists across calls within a rollout.
Keeping the tool space this small is intentional. With only three tools, efficient and wasteful trajectories are easier to distinguish in the reward signal.
 
The RL Math Behind Fast Ask
For each spreadsheet question, the model samples eight trajectories:
y_1, y_2, \ldots, y_G \sim \pi_{\text{gen}}(\cdot \mid x)
Each trajectory is the full interaction trace: tool calls, spreadsheet reads, Python execution, and final answer. The verifier scores each trajectory with our deterministic reward function:
R(y_i) =
1.0 \cdot \text{correct}(y_i)
+ 0.1 \cdot \text{efficiency}(y_i)
+ 0.05 \cdot \text{concise}(y_i)
We designed the reward around the production needs of Fast Ask. It should return the right answer, do it quickly, and avoid adding unnecessary text to the main agent’s context.
Correctness dominates the reward. The 1.0 term only fires when the final "ANSWER:" line parses into the expected type and exact matches ground truth. The efficiency and concision terms are small shaping rewards. They cannot rescue a wrong answer, but they distinguish between correct trajectories. A correct answer in five turns should score slightly higher than the same answer after wandering through irrelevant sheets.
We trained with GRPO, a policy gradient method that estimates advantages from groups of rollouts sampled for the same prompt. Instead of fitting a separate value model, GRPO normalizes each rollout’s reward relative to the other rollouts in its group. For a given spreadsheet question, one trajectory may answer correctly in five turns while another spends its budget on decoy tabs and fails. That relative reward difference becomes the learning signal. A simple way to write the advantage for rollout i is:
A_i = R(y_i) - \frac{1}{G}\sum_{k=1}^{G}R(y_k)
Ignoring off policy correction for a moment, the policy-gradient update has the form:
\nabla_\theta J(\theta)
\approx
\sum_{i=1}^{G}
\sum_{t=1}^{|y_i|}
A_i \nabla_\theta \log \pi_\theta(y_{i,t} \mid x, y_{i,<t})
This is the part that makes RL a natural fit for tool using agents. We never label the correct next tool call. We only score the final trajectory. The math pushes probability mass toward behaviors that made the final answer correct: reading metadata first, avoiding decoy sheets, using helper summaries when valid, falling back to raw rows when needed, and emitting a parseable "ANSWER:"  line.
Why Async Off Policy RL Made This Practical
For Fast Ask, a rollout is a multi turn trajectory, where the agent inspects workbook metadata, reads ranges, runs Python, and finally emits a parseable answer. That makes rollout generation much slower than ordinary supervised fine tuning data loading.
Prime Intellect's prime-rl stack makes this practical with asynchronous off policy training. Off policy training enables learning from trajectories generated by a slightly older version of the model (less updates), rather than requiring every rollout to come from the latest weights. Rollout workers keep generating trajectories while the trainer updates the model. Rollout workers keep generating trajectories while the trainer updates the model. Some trajectories come from a slightly older policy, but the objective corrects for that bounded staleness with importance weighting.
The importance ratio is:
\rho_t(\theta) =
\frac{
\pi_\theta(y_t \mid x, y_{<t})
}{
\pi_{\text{gen}}(y_t \mid x, y_{<t})
}
Intuitively, rho_t asks: how much more or less likely is the current model to produce this token than the model that originally generated it?
Prime Intellect uses an AIPO-style clipped importance weighted objective to keep those updates stable:
J(\theta)=
\sum_{i,t}
\min\left(
\rho_{i,t}(\theta) A_i,
\text{clip}(\rho_{i,t}(\theta), 1-\epsilon, 1+\epsilon) A_i
\right)
That matters for tool use tasks because rollouts are slow. If training had to stop and wait for perfectly fresh trajectories after every update, GPU utilization would suffer. Off policy RL lets rollout workers keep exploring spreadsheets while the trainer keeps learning from recently generated traces.
 
Results
We evaluated the base and trained models alongside the Claude family on a held out task set. Metrics are exact-match accuracy and wall clock time per rollout:
 
Training ran for 100 steps over about 26 hours. Reward climbed from roughly 0.2 to 0.8 over the first 40 steps before plateauing. Most of the gains came from two things: the model learning to produce correctly parsed and formatted answers, and planning tighter trajectories that waste fewer turns. Interestingly, total cells read per rollout stayed roughly flat during training. This suggests the model did not learn to read less overall but instead learned to allocate its reads better.
 
 
RL training added 10 percentage points of accuracy over the base model while actually reducing average completion time. The trained model beats Opus by 4+ points and runs at Haiku latency.
 
Takeaways
RL post training worked here because the environment made spreadsheet retrieval measurable and repeatable. Using the RL environment we reduced retrieval to repeated decisions with clear outcomes. This gave the model a clean optimization target without needing human labeled trajectories or an LLM judge.
Fast Ask is one example of a pattern we expect to use more: train small, verifiable subagents for narrow bottlenecks, and let frontier models spend their tokens on judgment instead of retrieval.
A small model trained with RL in a tightly scoped environment can outperform frontier models on a specific retrieval task, at a fraction of the cost and latency. The important work was not in model architecture or scale but in environment design: the right tasks, a minimal tool interface, and a reward function grounded in how the product actually works in production. This enabled the model to learn to read the right things.
 
¹ The synthetic world is internally consistent. Customers, vendors, SKUs, contract tiers, payment methods, adjustment reasons, and entry sources are sampled from fixed vocabularies, giving the model realistic entity structure across thousands of generated workbooks.
 
Coauthors: Ben Geist @b_geist & Will Brown @willccbb 
 
Want to keep up with our next AI experiments? Subscribe here and follow us on @RampLabs. We’re also hiring across roles at Ramp.
