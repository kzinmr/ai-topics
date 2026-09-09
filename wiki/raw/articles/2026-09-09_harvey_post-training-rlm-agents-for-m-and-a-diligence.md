---
title: "Post-Training RLM Agents for End-to-End M&A Diligence"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence"
scraped: "2026-09-09T06:00:02.338758+00:00"
lastmod: "2026-09-08T17:00:00.000Z"
type: "sitemap"
---

# Post-Training RLM Agents for End-to-End M&A Diligence

**Source**: [https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence](https://www.harvey.ai/blog/post-training-rlm-agents-for-m-and-a-diligence)

Introducing Harvey II:
Harvey's agents inherit project and matter context, and memory of how you work.
Learn more
Introducing Harvey II:
Harvey's agents inherit project and matter context, and memory of how you work.
Learn more
Introducing Harvey II:
Harvey's agents inherit project and matter context, and memory of how you work.
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
Company
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Agents
→
Purpose built agents execute complex legal work end to end.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
New
→
Your preferences carried across Harvey so every response comes back consistent with how you work.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
→
Streamline work and shift focus to strategy and speed.
Law Firms
→
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
→
Resources for maintaining a uniform and professional presentation of the Harvey brand.
Research
→
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
Newsroom
→
Press releases and partnership announcements.
2025 Year in Review
→
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Login
Request a Demo
Platform
Overview
A unified view of how Harvey's products work together to support your entire practice.
Agents
Purpose built agents execute complex legal work end to end.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
New
Your preferences carried across Harvey so every response comes back consistent with how you work.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
Streamline work and shift focus to strategy and speed.
Law Firms
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
Resources for maintaining a uniform and professional presentation of the Harvey brand.
Research
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Insights
Post-Training RLM Agents for End-to-End M&A Diligence
New research with Baseten shows how recursive language model harnesses and post-training can improve AI performance on complex M&A diligence.
by
Niko Grupen
,
Julio Pereyra
,
Gabe Pereyra
,
Charlie O'Neill
,
Mudith Jayasekara
,
Aaron Ellis-Bloor
,
Jonathon Liu
, and
Matthew Blau
•
Sep 8, 2026
In our recent
research preview for Harvey Tenet
, we highlighted the importance of model-harness co-optimization for solving complex, end-to-end legal tasks, and previewed initial results on M&A Diligence, where a single task requires traversing up to 80M tokens of document context. Today, we are sharing updated results from our continued experimentation.
Together with Baseten, we built a
recursive language model
(RLM) harness for M&A Diligence. In our RLM formulation, a complete data room is loaded into a Python REPL and a root agent delegates bounded review and analysis to sub-agents that work within their own context windows. On
LAB Diligence
tasks, this harness improves rubric criteria pass rate by 39.1 percentage points on average across seven models that we evaluated.
We find that post-training within the RLM harness yields further performance gains and options for navigating quality-efficiency trade-offs. We post-trained a Qwen3.5-122B-A10B orchestrator via reinforcement learning and found that post-training increased rubric criteria pass rate from 29.9% to 63.0% on 50 held-out LAB Diligence data rooms.
Figure 1: Mean criteria pass rate on LAB Diligence for base models in the standard tool-loop harness, coding agents in their own harnesses, and models in our RLM harness. Asterisks mark the matched GLM-5.2 results before and after SFT, evaluated on a separate 20-room hold-out set. All other results use the 50-room hold-out set.
These results suggest that post-training within a task-specific harness is a practical route for document-intensive legal work, like M&A Diligence, and that scaling RL within the RLM harness is a promising direction for future work. For this reason, we are also training GLM-5.3, a large frontier open weight model, as the root model in an ongoing scale-up run.
In the rest of this post, we describe the LAB Diligence environments that we evaluated, our methodology, and post-training experiments in more detail.
Environments for M&A Diligence
We recently introduced
LAB Diligence
, an extension of
LAB
that includes synthetic environments for M&A Diligence. A single data room in LAB Diligence contains up to 5,000 documents, organized across dozens of folders by category, and up to 80M tokens of total context.
Figure 2: An example LAB Diligence data room. Aravon Bridge Bank contains 2,270 documents in 82 folders across 14 categories, 31M tokens in total. The agent's diligence memo for this task is graded against 571 rubric criteria.
Working within this data room, the agent is tasked with producing a complete diligence memo, including its findings with document citations, quantified exposure where relevant, and recommended next steps for the transaction. An LLM judge scores the diligence memo against an expert rubric with hundreds of pass or fail criteria. The Aravon Bridge Bank example has 571 rubric criteria in total.
Figure 3: Rubric examples for the Aravon Bridge Bank task in LAB Diligence, with one verbatim criterion of each type.
The evidence needed for diligence is spread across the data room. Some findings require combining several documents, while others require checking whether supporting evidence is missing. In our baseline runs, agents searched and read selectively, leaving much of the data room unexamined. These tasks call for a harness that can distribute review across many bounded contexts and bring the findings together.
An RLM Harness for M&A Diligence
To establish a baseline, we started with the standard tool-loop harness from
Legal Agent Bench
. In this harness, base models pass 23.3% of rubric criteria on average across the 50 held-out data rooms, and no model passes every criterion on any data room.
Figure 4: Mean criteria pass rate in the standard tool-loop harness on the 50 held-out diligence data rooms.
These results suggest a mismatch between task and harness. A LAB Diligence data room is too large to fit within a single model context, but much of the initial review can be divided by category. The root can then combine findings across categories to produce the memo. Deal teams within law firms divide diligence work in a similar way.
Figure 5: The RLM harness at depth-1. The data room is loaded into a Python REPL as queryable variables. The root agent operates on it in code and delegates bounded reading tasks to subagents, which return their findings as REPL variables. Only the output the root agent prints enters its context window, so the root never holds the full data room.
This led us to explore RLMs as a harness for M&A Diligence. In an RLM harness, a root agent is given a Python REPL with the data room loaded as queryable variables, which lets it search the corpus programmatically. The root agent plans and scopes the review and dispatches sub-tasks to sub-agents. Each sub-agent receives a bounded slice of the corpus and instructions from the root agent, works within its own context window, and returns its findings as REPL variables. The experiments below use a single layer of sub-agents unless noted, and in practice the root dispatches many calls in parallel.
Figure 6: Mean criteria pass rate for seven models in the standard tool-loop harness and as the root of the RLM harness (depth-1, Qwen3.6-35B-A3B sub-agents), on the 50-room hold-out set.
Across seven models, the RLM harness raises mean pass rate from 23.3% to 62.4%, a gain of 39.1 percentage points. We also ran two general-purpose coding agents with web tools disabled,
Claude Code
with Opus-5, and
Codex
with GPT-5.6 Sol, using the same minimal instruction as the tool-loop harness. Claude Code passes 24.6% of criteria and Codex 12.0%, below the same models in the tool-loop harness by 17.9 and 4.6 points, respectively. In the traces, both agents stop reading early and write shorter memos, and neither spawns sub-agents despite having the ability to.
Coverage and Cost
The RLM harness substantially increases the amount of useful content that becomes agent context. We estimate coverage with probes that measure the share of data room content reaching any model in the harness, root or sub-agent. In the standard tool-loop harness, no run reads more than 1% of the data room, and most read between 0.1% and 0.5%. In the RLM harness, nearly every run reads more than 10% of the data room and most read close to all of it. Higher coverage is associated with higher rubric criteria pass rates across this range.
Figure 7: Rubric criteria pass rate versus probe-based coverage, one point per run, for seven models in each harness on the 50 held-out data rooms from LAB Diligence. Coverage is on a log scale.
Moving to the RLM harness raises generation cost per data room for six of the seven baseline models, as shown in Figure 8. Claude Opus 5 is the exception. In the tool-loop harness it spends ~$18 per data room reading on its own; as an RLM root it spends ~$7 and scores 35 points higher.
Figure 8: Mean criteria pass rate versus generation cost per data room for seven models in each harness, averaged over 50 held-out data rooms. Dotted lines connect the same model across harnesses. Costs are cache-aware estimates at list prices, log scale.
Division of Labor
To examine how much performance depends on the root agent vs. the sub-agents, we paired four root models with three Qwen sub-agent models on 30 held-out data rooms (see Figure 9). Across the configurations tested, changing the root had a larger effect. Holding the sub-agent model fixed while varying the root model, the gap between the highest- and lowest-scoring roots averaged about 38 percentage points. Holding the root fixed while varying the sub-agents, the corresponding gap between sub-agent models averaged about 8 points (Figure 9b).
Figure 9: Division of labor in the RLM harness, aggregated over four root models and three sub-agent models on 30 held-out data rooms. (a) Root share of input and output tokens, averaged over sub-agent choices. (b) The gap between the highest- and lowest-scoring roots, averaged over sub-agent choices, and the corresponding gap between sub-agents, averaged over roots.
This difference is notable because, in the RLM harness, we observe the root accounting for a
minority
of the agent’s total token usage. With Opus 5 orchestrating, for example, the root accounts for 3.8% of input tokens and 1.1% of output tokens (see Figure 9a). The sub-agents process most of the text, while the root decides how to divide the review and assemble the findings.
Figure 10: Mean criteria pass rate for four root models paired with three sub-agent models, on 30 held-out data rooms.
These results suggest that improving coordination is an important opportunity in this setup, so we focused our initial post-training experiments on the root.
Post-Training in the RLM Harness
The results above point to the root agent as a target for post-training. In this section, we report results from post-training open-weight root models inside the RLM harness.
Self-Distillation SFT
First, we post-trained a GLM-5.2 root using rejection-sampling self-distillation SFT. This experiment uses a different 20-room hold-out evaluation set from the 50-room evaluations reported elsewhere. Its matched base-model score on this hold-out is 46.1%, below the 65.4% GLM-5.2 result reported in Figure 6 over the larger hold-out set.
Base GLM-5.2 does not stably execute a high-scoring policy out of the box — there are frequent performance collapses where the base model, acting as root agent, gives up early, under-delegates, or fails to convert the subagent outputs into a strong deliverable. Given that a strong policy is already within the model’s distribution but needs to be made more robust, we use rejection-sampling self-distillation to sharpen GLM-5.2’s distribution onto the desired mode. We selected successful GLM-5.2 runs with high data room coverage and fine-tuned the root on those trajectories.
Figure 11: GLM-5.2 as the RLM root before and after rejection-sampling self-distillation SFT, evaluated on a separate 20-room hold-out set. These are matched results within the SFT experiment, not the 50-room evaluation used in Figure 6.
On this 20-data room hold-out set, the SFT-trained root scores 60.1% against 46.1% for the base model (see Figure 11). A review of the post-trained agent’s traces suggests that training helps the root agent comprehensively review the data room and carry a larger percentage of sub-agent findings into the final memo.
Table 1 summarizes other behavioral changes we observe after post-training. Most notably, the correlation between sub-agent call volume and data room size rises from 0.17 to 0.84, indicating that the trained root agent scales its delegation to the size of the data room. The trained root also learns to begin writing the memo while sub-agents are still reading, similar to what we found in our RL runs.
Table 1: Behavior of the GLM-5.2 root before and after SFT, averaged over the separate 20-room hold-out set. Coverage is a percentage; the final row is a correlation coefficient.
The behaviors that make a strong root diligence agent, like exhaustive delegation, are learnable from a relatively small number of on-policy traces, with no privileged information and no labeled legal knowledge. Here, self-distillation is effective because good behavior already exists in the model’s distribution and training stabilizes it.
This experiment motivated us to explore RL-based post-training as an attempt to push the model beyond what is within its distribution, eliciting new behavior directly through the task’s reward.
Reinforcement Learning
For reinforcement learning we started with a smaller root model, Qwen3.5-122B-A10B, to keep the initial RL experiment loop tractable.
We trained the RLM root with GRPO, using the judged rubric criteria pass rate as the reward and holding the sub-agent models fixed (sub-agents were each Qwen3.6-35B-A3B model). Over 40 training steps, we found that the mean rollout pass rate rose from about 23% to about 56%. On the 50-room hold-out set, the final checkpoint scores 63.0% against 29.9% for the base model.
Figure 12: Reinforcement learning on the Qwen3.5-122B-A10B root with fixed Qwen3.6-35B-A3B sub-agents. (a) Mean rollout criteria pass rate at each of 40 training steps. (b) Base model and final checkpoint on the 50-room hold-out set.
After RL, mean data room coverage rises from 62% to 96%, even though coverage is not an explicit reward term. Base runs are spread across the full coverage range, with a cluster below 20% that scores near zero. Every RL-trained run reads more than 60% of the data room and most read all of it.
Figure 13: Criteria pass rate versus probe-based coverage, one point per run, for the Qwen3.5-122B-A10B root before and after RL on the 50-room hold-out set.
The post-trained root makes 64% more sub-agent calls per data room. RL also changed delegation volume more than SFT did, 64% against 29%.
Table 2: Behavior of the Qwen3.5-122B-A10B root before and after RL, averaged over the 50-room hold-out set.
Before post-training, the Qwen root agent attempted to write its diligence memo in a single shot and only after all of the sub-agents return. During RL post-training, it learns a more efficient approach, writing the memo incrementally and interleaving section writing with the review of sub-agent work.
Scaling RL With GLM-5.3
To test our RL recipe at scale, we are now training GLM-5.3 as the RLM root with the same GRPO-style configuration: judged criteria pass rate as the reward, Qwen3.6-35B-A3B sub-agents held fixed, LoRA on the root, group size 8 and batch size 24. GLM-5.3 rollouts start well above where the Qwen root started, so there is less headroom. Over steps 0 to 20 (Figure 14), mean rollout pass rate rises from about 51% to about 59%, averaged over the first and last eight steps shown, with the step-to-step noise expected at this batch size.
Figure 14: Early training progress for the ongoing GLM-5.3 RL run, with Qwen3.6-35B-A3B sub-agents held fixed. Mean rollout criteria pass rate is shown over the course of 20 training steps. Grey shows raw per-step values; black shows an exponential moving average. This figure reports training scores, not held-out performance.
What’s Next
The RLM harness improves performance across the models we tested, and RL produces further gains for the Qwen root within that harness. There is still a substantial gap between these scores and the near-perfect pass rates we are working toward.
The training experiments detailed above are initial explorations. In addition to completing the scaled up GLM-5.3 training run, we will also explore combinations of SFT and RL, and trained sub-agents. The RLM harness separates the root's orchestration from the sub-agents' reading, so each can be trained on its own or jointly, including setups in which sub-agents are trained to delegate in turn.
Finally, the core finding here, that
model-harness co-optimization can meaningfully improve agent performance in long-horizon environments
, is not specific to diligence. We are exploring ways to map the same harness structure and training approach to other long-context legal work.
Appendix
RLM Recursion Depth
We also tested whether adding another layer of delegation improves performance. At depth-1, sub-agents return plain LLM completions, with no tools or delegation of their own. At depth-2, sub-agents receive a Python REPL and can delegate further. Within each experiment, we used the same model for the root and every sub-agent.
We evaluated both GLM-5.2 and Qwen3.5-122B-A10B. Many GLM-5.2 depth-2 runs did not finish within the time limit, so we report the Qwen results below. Across 14 data rooms, depth-2 improved scores on four and reduced them on ten, lowering mean criteria pass rate by 19 percentage points (Figure A2). In four of the ten regressions, the depth-2 agent read data room content but never produced a report.
Figure A1: Per-room criteria pass rate at depth-1 and depth-2 for 14 data rooms. We held the model fixed and compared plain-completion sub-agents with sub-agents that could use a REPL and delegate. In four of the ten regressions, the depth-2 run reads the data room but never writes the report.
These results motivated our use of depth-1 for the initial post-training experiments. Whether training agents specifically for deeper delegation can make additional layers useful remains an open question.
RL Infrastructure
RL, especially with such long episode lengths, is as much an infrastructure problem as a training signal problem. For this task, single-episode rollouts could take on the order of an hour or more of wall-clock to complete. To optimize the training wall-clock time, we applied methods like asynchronous off-policy inference, continuous inference batching, oversampling, and in-flight weight updates. Selective token masking and async-related caps were applied to control the effect of off-policyness. Given that in the RLM harness most of the wall-clock is spent waiting for subagents to complete, the ability to use small fast subagents helped to greatly speed up the RL training process.
We plot step wall-clock time below. It is dominated by rollout time which grows over the course of RL as the agent becomes more thorough and sends out larger waves of subagents.
Caption: Figure A2: Wall-clock minutes per RL training step for the 40-step run, with a 5-step rolling mean. Steps 2–10 average 48 minutes and steps 31–40 average 74 minutes; the increase comes from the trained model dispatching more sub-agents per rollout.
Next Up
How Legal Teams Use AI Tools for Contract Generation and Automation
The Legal Client Intake Process and How AI is Changing it
How to Draft Discovery Requests and Responses You Can Trust
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Overview
→
Agents
→
Vault
→
Knowledge
→
Spaces
→
Command Center
→
Contract Intelligence
→
Ecosystem
→
Harvey Mobile
→
Partnerships
→
Solutions
Innovation
→
Transactional
→
Litigation
→
In-House
→
Law Firms
→
Mid-Sized Firms
→
Company
Customers
→
Security
→
About
→
Careers
→
Newsroom
→
Law Schools
→
Resources
Blog
→
Resources Hub
→
Harvey Academy
→
Help Center
→
Legal
→
Privacy Policy
→
Press Kit
→
Your Privacy Choices
→
Follow
X
→
LinkedIn
→
YouTube
→
Instagram
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
