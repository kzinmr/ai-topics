---
title: "Legal Agent Benchmark Initial Results"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/legal-agent-benchmark-initial-results"
scraped: "2026-05-28T06:00:22.307886+00:00"
lastmod: "2026-05-26T17:00:00.000Z"
type: "sitemap"
---

# Legal Agent Benchmark Initial Results

**Source**: [https://www.harvey.ai/blog/legal-agent-benchmark-initial-results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results)

Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
About
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Assistant
→
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
→
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
→
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
In-House
→
Streamline work and shift focus to strategy and speed.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
Collaboration
→
Work with legal teams across organizations in secure, shared spaces.
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
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
→
About Harvey, our leadership, and career opportunities.
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
Assistant
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
In-House
Streamline work and shift focus to strategy and speed.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
Collaboration
Work with legal teams across organizations in secure, shared spaces.
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
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
Company
About Harvey, our leadership, and career opportunities.
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
Initial Results on Legal Agent Benchmark
A first look at frontier model performance on long-horizon legal-agent work.
by
Niko Grupen
,
Gabe Pereyra
, and
Julio Pereyra
•
May 26, 2026
Earlier this month, we released
Legal Agent Benchmark (LAB)
, an open-source benchmark for evaluating agents on complex legal work. One of our core motivations for developing and releasing an agent benchmark is to provide transparency into how agents perform on real legal tasks and the trade-offs associated with key agent design decisions like model selection, harness optimization, and post-training.
Since launch, we have been baselining frontier models from prominent AI providers on an evaluation set that mirrors the task distribution of LAB. We scored each task under LAB’s all-pass standard, where a task counts as passing only if every required rubric criterion passes. From this analysis, three meaningful trends have emerged:
Legal work is far from saturated by frontier models
: Under our strict all-pass standard, the frontier models we evaluated complete less than 10% of tasks end-to-end in aggregate. The frontier of model intelligence cannot yet deliver complete legal work product.
Intelligence is not evenly distributed
: Improvements in model capabilities are not evenly distributed across the kinds of expertise and precedent that legal work depends on. Models continue to demonstrate
jagged intelligence
for specialized knowledge work, with high variance across practice areas. On LAB, the leaderboard shifts substantially across legal practice areas, and no single model leads every one.
Frontier intelligence comes at a cost
: The pace of development at the model layer is increasing, with major labs pushing the frontier of general intelligence on a monthly basis. The cost of operating at that frontier rises with it, as the best-scoring models are increasingly token-hungry and reliant on time-consuming, multi-step reasoning. On LAB, reaching the top of the leaderboard runs to roughly $50 per task and over 20 minutes of latency.
We also believe strongly that the way an agent works inside a task carries as much information as the score it produces; and that visibility into agent behavior will increase over time in importance in high-stakes, regulated domains like law. The reinforcement-learning and multi-agent systems literature has long studied agents this way, examining agent action sequences and aggregating them into patterns of behavior. We provide qualitative analysis of agent traces to better understand why some agents succeed while others fall short.
Legal Agent Performance
To evaluate agents in a standardized way, we created a hold-out set of legal tasks that mirror the practice areas and task distribution from
the public LAB set
. Each task is scored under LAB's all-pass standard, against expert-curated rubrics that specify the facts, conclusions, citations, structural requirements, and analytical moves a passing answer must include. To prevent grader bias, we grade agent runs multiple times across model families and average the results.
Figure 1. Overall leaders on LAB, ordered by all-pass percentage.
Figure 1 ranks the frontier models we baselined by overall all-pass on the holdout. Claude Opus 4.7 leads at 7.1%, with Sonnet 4.6 at 5.4%, Opus 4.6 at 4.2%, GPT-5.5 at 2.1%, and Gemini 3.5 Flash at 0.8% to round out the major model families we’ve evaluated thus far. Read against the strict review standard legal work actually demands, these numbers describe a frontier that is improving rapidly but is not yet good enough. Legal work is far from saturated.
Aggregate results also hide a significant degree of variation across the heterogenous practices areas and specializations that exist in legal. Legal work spans dozens of sub-domains, from corporate and regulatory to IP, tax, employment, and healthcare, and the kinds of expertise and precedent each requires are different. Aggregating across all of them into one all-pass number masks that task diversity. To understand model performance across practice areas, we created three equal-sized practice-area groupings and re-ranked the same four model families inside each one.
“
Legal work spans dozens of sub-domains, from corporate and regulatory to IP, tax, employment, and healthcare, and the kinds of expertise and precedent each requires are different.
”
Figure 2 shows all-pass scores across each of the three practice areas. Importantly, a different frontier model outperforms in each grouping.
Figure 2. Practice area sample breakdown.
The pattern shown in Figure 2 is a canonical example of “jagged intelligence”: the uneven profile of LLMs, where some tasks
“work extremely well”
while others
“fail catastrophically,”
often in ways that are difficult to predict and not obvious to human observers. GPT-5.5 leads in the regulated and emerging-company groups, where retrieval-heavy research is a larger part of the work. Opus 4.7 leads the corporate transactions and funds categories, where synthesis and analytical work dominates. Sonnet 4.6 leads in the privacy, tax, and private-client work groupings, where structured comparison against statutes and regulations is central. Different model families bring different priors to legal work, and those priors map onto which categories each family can currently complete.
What this means in practice is that no single model is a silver bullet for legal work today. Maximizing agent performance on a real legal workload requires understanding which model family best matches the task at hand. The strongest production agent deployments will be multi-model from the start.
“
No single model is a silver bullet for legal work today. Maximizing agent performance on a real legal workload requires understanding which model family best matches the task at hand. The strongest production agent deployments will be multi-model from the start.
”
Cost and Latency
For production agents,
single-dimensional benchmarks indexed only on quality
do not capture the full complexity of deployment. In this section, we run additional evaluations that take into account cost, both monetarily and in terms of latency.
Figure 3. Cost and latency trade-offs.
Figure 3 plots the per-task cost and per-task latency of every model configuration we baselined. The spread is wide on both axes, and it shows just how steep the operating cost of agent intelligence at the frontier has become.
Opus 4.7, the highest-performing model by all-pass score, is the most expensive and slowest configuration in the set, at about $50.90 per task and roughly 22 minutes of wall-clock time. GPT-5.5 is approximately 3x cheaper and, in terms of latency, Gemini 3.5 Flash returns a draft in under six minutes (nearly 4x faster), but both land below the all-pass leader on this holdout.
Production agent deployments need more than a high benchmark score. They need a high score inside a budget that a customer will tolerate: the dollars they will spend per task, and the time they will wait for a draft. Both budgets shape what is actually deployable, and on LAB both bend sharply across the model frontier.
“
Production agent deployments need more than a high benchmark score. They need a high score inside a budget that a customer will tolerate: the dollars they will spend per task, and the time they will wait for a draft.
”
Behavioral Analysis
The way an agent works — how it explores its environment, its decision-making patterns, and its failure modes — are as important to understand as raw task success. The reinforcement-learning and multi-agent systems literature has long studied agent behavior qualitatively as well as quantitatively for this reason.
We apply the same lens to legal agents on LAB. The agents we baselined have a fixed action space with six actions that an agent can select from at any given turn:
Read:
Open a document from the matter file.
Search:
Query the matter for content across documents.
Execute:
Run analysis code over the matter or its outputs.
Write:
Produce or extend output in a deliverable.
Validate:
Run an explicit check of a draft against the instruction or the matter record.
Edit:
Modify the work product after a validation step.
In addition to a scored rubric, every LAB run produces an agent trace that captures how the agent sequenced these actions to produce its final deliverable. We analyzed how those actions combine into behaviors and how those behaviors correlate with outcomes.
Figure 4. Agent actions.
Figure 4 shows how each model family allocates its trajectory across available actions. The broad pattern is consistent: agents begin by reading client matter files to build context, then run some amount of analysis via code execution, then write a draft of the final deliverable, and, in a smaller fraction of runs, return to that draft or prior analysis to verify and revise it.
Models also differ in what they emphasize, and mapping their action sequences back to performance reveals what sorts of behavioral priors models have hidden in their weights, and the efficacy of those priors for knowledge work. Opus 4.7 agents, for example, are the most visibly self-corrective, spending more of their trajectory on drafting than other models on average, and frequently re-checking, validating, and revising their own outputs before finishing work. This translates to notably higher scores on drafting-related tasks. GPT-5.5 has by far the largest search segment of any family, running document search more heavily than other models and covering a wider breadth of documents on average. This translates to higher scores on research-focused tasks.
We also examined how patterns of actions coalesce into recognizable behaviors. Studying agents through their behaviors has a strong history in the multi-agent systems literature — for example, revealing
emergent coordination
in simulated environments and how learned
tool use and counter-strategies can emerge from self-play
.
The same lens is useful here, and interestingly the behaviors that emerge when an agent works through a legal task and correlate with strong performance look like the steps a competent associate would take: read the matter, search for what is missing, run analysis on the relevant facts, draft the deliverable, check the draft against the instruction, and revise on the back of that check.
Figure 5. Agent behaviors.
By analyzing sequences of actions across model families, we identified a small set of emergent behaviors that appeared consistently and meaningfully impacted outcomes:
Conducting thorough research before drafting
: When the agent builds broad matter context before producing work product — e.g. achieving >90% document coverage in the research phase — all-pass scores improve by 0.4 points on average.
Post-draft validation
: Agents that run a validation or review step after drafting, rather than treating the first draft as final, see a 0.8 point average improvement in all-pass score.
Verifying and revising
: The strongest positive pattern is not just reviewing, but actually changing the deliverable after review. Agents that close this revise-after-check loop improve all-pass scores by 1.5 points on average.
Using targeted retrieval
: Agents that search the matter file during the run can locate facts across the broader corpus instead of relying only on initially opened documents, improving all-pass scores by 0.3 points on average.
Applying structured analysis
: When agents use code or shell tools to compute, parse, or verify evidence, they turn parts of the legal task into a more systematic analysis step, improving all-pass scores by 0.3 points on average.
Grounding drafts against the record
: Agents that return to source documents after drafting appear to check or correct the work product against the underlying evidence, improving all-pass scores by 0.3 points on average.
Avoiding noisy tool fan-out
: High parallel tool use — i.e. five or more tool calls in a single turn — can cover ground quickly, but is associated with a 0.5 point decrease in all-pass score, suggesting that broad search without enough direction may add noise.
Drafting without review
: Agents that draft but skip later validation or revision perform materially worse, with all-pass scores falling by 1.2 points on average.
The frequency column in Figure 5 is the share of observed agent trajectories that exhibit each behavior. Self-correction is the strongest positive signal.
Taken together, these patterns look less like arbitrary model quirks and more like recognizable markers of strong associate work product: building context before drafting, checking work before submitting it, making substantive revisions after review, and avoiding so many parallel workstreams that the effort becomes difficult to synthesize.
“
These patterns look less like arbitrary model quirks and more like recognizable markers of strong associate work product: building context before drafting, checking work before submitting it, making substantive revisions after review, and avoiding so many parallel workstreams that the effort becomes difficult to synthesize.
”
Next Steps
Closing the gap between today’s frontier and reliable legal-agent performance is going to require sustained research across multiple fronts: how agents handle long-horizon professional tasks, how they internalize the domain knowledge that transfers across legal sub-domains, and how they deliver that performance inside the cost and latency budgets production deployments actually require. Each of these is its own research direction, and progress on each will compound with progress on the others.
Over time, behavioral analysis will be the tool that makes those directions interpretable to both AI researchers and lawyers. We cannot improve what we cannot interpret, and on long-horizon professional work the right unit of measurement is the trajectory as much as the final score. LAB is one of the instruments we are using to do that work.
To facilitate these research directions, LAB is going to keep growing on three fronts:
The benchmark itself.
Richer task families covering more practice areas, adjacent professional-service workflows beyond legal, and longer-context matters. We are partnering with Artificial Analysis to scale up LAB evaluation and publish a regularly-updated leaderboard as new model launches arrive. The leaderboard will be a living record of where the frontier sits on legal work, refreshed as the field moves.
The research program around it.
Each trend in this post opens a research direction. We are starting to run those threads with partners to better measure how agents handle long-horizon legal tasks, study of how domain knowledge transfers across legal sub-domains, and how to bake cost and latency improvements into agents alongside quality.
Collaboration with AI labs and model providers.
We will be working with model providers whose agents we baselined to understand and inform what changes at the model layer move the needle on legal-agent performance.
We will be providing more information on these and other research directions in the near future.
Next Up
Why Attorney Oversight Makes Legal AI More Powerful
The Success Metrics That Matter for Legal AI
How In-House Legal Teams use AI to Review and Manage Contract Work at Scale
Unlock Professional Class AI for Your Firm
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Assistant
→
Vault
→
Knowledge
→
Workflow Agents
→
Ecosystem
→
Partnerships
→
Solutions
Innovation
→
In-House
→
Transactional
→
Litigation
→
Mid-Sized Firms
→
Collaboration
→
About
Customers
→
Security
→
Company
→
Newsroom
→
Careers
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
Copyright © 2026 Harvey AI Corporation. All rights reserved.
