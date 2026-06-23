---
title: "Training a Legal Agent With Applied Compute"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/training-a-legal-agent-with-applied-compute"
scraped: "2026-06-23T06:00:29.743385+00:00"
lastmod: "2026-06-22T21:00:00.000Z"
type: "sitemap"
---

# Training a Legal Agent With Applied Compute

**Source**: [https://www.harvey.ai/blog/training-a-legal-agent-with-applied-compute](https://www.harvey.ai/blog/training-a-legal-agent-with-applied-compute)

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
Agents
→
Purpose built agents execute complex legal work end to end.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Shared Spaces
→
Work with legal teams across organizations in secure, shared spaces.
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
Agents
Purpose built agents execute complex legal work end to end.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Shared Spaces
Work with legal teams across organizations in secure, shared spaces.
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
Training a Legal Agent With Applied Compute
Results from post-training GLM-5.1 into the strongest available model on Harvey’s Legal Agent Benchmark by rubric pass rate.
by
Niko Grupen
,
Julio Pereyra
,
Gabe Pereyra
,
Rhythm Garg
,
Jacob Phillips
, and
Raymond Feng
•
Jun 22, 2026
Building on our body of research supported by our
Legal Agent Benchmark (LAB)
, we collaborated with Applied Compute to post-train a frontier legal model on top of GLM-5.1. The trained model outperformed every available model on the rubric pass rate. Notably, it outperforms Opus 4.8 Max and GPT-5.5 xhigh, a threshold that previous trained models across the industry had not yet reached.
Post-training over GLM-5.1 increases rubric pass rate to 0.913, exceeding both GPT-5.5 xhigh and Opus 4.8 Max.
Post-training over GLM-5.1 increases all-pass rate to 0.126 on the all, exceeding GPT-5.5 xhigh and approaching Opus 4.8 Max.
Our research continues to reinforce a broader trend: post-training, harness optimization, and grader design cannot be treated as separate problems. On long-horizon legal work, the model only learns as well as the environment allows. The optimization signal needs to be reliable, the harness needs to support the right legal work pattern, and the model needs to learn to use that harness efficiently.
This post walks through the full stack that made the result possible: grader analysis, cost-efficient evaluation, harness optimization, compaction, full-parameter reinforcement learning on Applied Compute Agent Cloud, and behavioral analysis of the trained model.
Training and Validation on Applied Compute’s Platform
Training on LAB requires trust in the reward signal. A capable open-weight model can exploit weaknesses in the grader, the rubric, or the harness if those weaknesses exist.
We ran evaluations, training jobs, consistency checks, and supporting analysis on Applied Compute Agent Cloud. All final evaluations used the same compaction harness and maximum reasoning effort. GPT-5 Mini was used as the grader, with four rubric criteria batched per grader call.
1. Grader Alignment
LAB uses LLM-as-judge grading, so we first analyzed grader reliability against a frontier-model consensus. Applied Compute’s researchers ran a 50-point subset through the LAB harness, producing traces covered by more than 2,500 rubric criteria. They then reran candidate graders three times each to measure self-consistency and cross-consistency.
GPT-5.5 xhigh and Opus 4.8 Max agreed on more than 95% of criteria across runs. We treated that agreement set as the frontier consensus and evaluated candidate graders against it, including GPT-5.5, Opus, GPT-5 Mini, Sonnet, GPT-5 Nano, and Haiku.
GPT-5 Mini and Sonnet preserved most of the frontier signal, staying above 97% alignment with the consensus. Smaller models degraded more sharply, with GPT-5 Nano around 95% and Haiku materially lower. The top graders were also highly self-consistent, with a 98.9% per-criterion self-consistency floor across three reruns and approximately 0.99 Pearson correlation across criteria for the strongest graders.
This made GPT-5 Mini strong enough to support repeated grading, sampling, and RL at much lower cost.
2. The Cost-Alignment Frontier
The original LAB setup graded one criterion per call. We tested two cost levers: smaller grader models and batching multiple rubric criteria into each grader call.
Switching to GPT-5 Mini and batching criteria produced 40x cost reduction at 16 criteria per group and 100x reduction when all criteria were grouped together. For final evaluations, we chose a conservative setting: GPT-5 Mini with four criteria per call.
Cost reductions relative to Sonnet 4.6 with 1 criteria-per-call baseline. Both grader candidates are measured against frontier model agreement to GPT-5.5 xhigh and Opus 4.8 Max. Annotations represent the number of criteria-per-call, showing how batching groups of criteria can lead to massive cost savings. Note the x-axis mean cost per trace log scale.
3. Improving the Legal-Agent Harness
We started with our public LAB harness, which gives the agent simple tools like read and grep over files mounted into a sandboxed environment. After matching our earlier LAB results, we used Applied Compute Agent Cloud to test harness changes that improved performance while remaining generalizable.
Optimizing the agent’s harness and available tools from online failure modes led to a number of intuitive improvements:
Restricting token volume returned by tool calls
Repairing malformed tool calls
Improving tool descriptions
Adding reminders about tool use and final deliverables
Adding output-production guidance
Introducing compaction so agents could work beyond a single context window
Comparison of baseline LAB harness to final AC harness with compaction, better prompts, stronger tool descriptions, and reminders. All evals are run against GPT-5 Mini with 4 criteria-per-group. All evaluations run against base checkpoints or APIs.
Comparison of baseline LAB harness to final AC harness with compaction, better prompts, stronger tool descriptions, and reminders. All evals are run against GPT-5 Mini with 4 criteria-per-group. All evaluations run against base checkpoints or APIs.
Most models improve from these harness changes alone, but we found that strongest performance came post-training
within
the new agent harness, as the agent is taught how to use the tools available to it most effectively and address its own failure modes. The harness made better strategies available; RL taught the model to execute them.
4. Compaction
Roughly 10% of base GLM-5.1 rollouts hit the context limit. LAB’s document distribution makes this expected: the 90th-percentile datapoint contains nearly 100,000 source-document tokens, and the largest exceed 200,000.
We added compaction to the harness. When the conversation reached a token threshold, the harness sent the current episode transcript back to the same agent for summarization, using the same weights and a different system prompt. The harness then started a fresh continuation conversation from that summary.
Compaction gives the model an effective context larger than a single window, but also introduces a new requirement: learning what to preserve, what to discard, and how to continue working from a compressed state without losing the legal thread.
5. Training
After grader and harness analysis, Applied Compute trained GLM-5.1 with full-parameter, fully asynchronous reinforcement learning on AC2. We selected GLM-5.1 because it had the strongest baseline performance among the candidate open-weight models.
Before training, GLM-5.1 was below GPT-5.5 xhigh and Opus 4.8 Max. During training, it passed both on rubric pass rate and approached Opus 4.8 Max on all-pass rate.
Model Analysis
We analyzed the trained model across domain performance, tool use, artifact behavior, specificity, and grounding.
Domain-Level Shifts
The model did not improve uniformly. It gained most where document use, factual grounding, and complete deliverable construction mattered most. Small regressions in low-representation domains suggest a clear direction for data balancing and targeted training.
Tool-Use Analysis
Over the course of training, we see total tool usage fall; this breaks down mostly into fewer read calls with a consistent number of other tool calls, like bash and grep.
As the eval score continues to improve, this reflects the model learning to more effectively use its tools and not just bulk-read all the files in the source documents. Likewise, the model sets more limits and uses the read tool more specifically, which reduces the total payload tokens per trace over the course of training.
Behavior Analysis
Base GLM-5.1 started with a near 85% pass rate on rubric criterion, leaving roughly 1,500 criteria to improve across the 180-item test set, out of about 10,000 total criteria.
Artifact Completeness
: The model learned to properly use tools and
always
create an output artifact. This behavior flipped 185 relevant rubric criteria from failing to passing during the course of training.
Specificity and Exactness
: The base GLM-5.1 model suffers from poor calculations or referring to imprecise numbers, often rounding figures during math (like 1.9 to 2), which is punished by the exacting legal graders. This behavior flips 243 criteria from failing to passing.
Grounding:
Without training, the checkpoint sometimes hallucinates source document items or invents findings from outside the provided documents. Despite not training against an explicit hallucination penalty, we see this behavior drop over time as criteria related to referencing specific document spans improve over time. This behavior flips 70 criteria from failing to passing during training.
These three behaviors accounted for part of the model's improvement from the first step to the last. Many criteria flipped from failing to passing, but some criteria tied to these same behaviors still fail in the final checkpoint, which suggests the model has not yet reached its performance ceiling.
Example Rollouts
We can directly observe these learned behaviors by comparing traces from held-out eval points at the beginning and end of training. Below, we compare attempts to solve a LAB task from the untrained base GLM-5.1 model and our final trained checkpoint.
Metric
GLM-5.1 Base
AC GLM-5.1
Rubric Score
.061
.803
Turns
40
16
Tool Calls
104
42
Read Calls
44
24
Bash Calls
44
16
Tool Playload Tokens
461k
250k
Over the course of training, the trained checkpoint exhibits markedly fewer total tool calls and makes more precise, targeted use of its bash and read calls. This results in vastly smaller total payloads returned from tools. Due to our compaction harness, the model can ingest far more tokens than its max context length but must learn to effectively use that effective context and avoid context rot.
In the base checkpoint, we see many uses of calls to functions ls, echo, and cat via the bash tool that dump huge amounts of tokens into the context window. Once the model attempts to make an output deliverable, it wastes 16 tool calls creating and revising its deliverable. In contrast, the trained model avoids unhelpful tool calls and uses targeted reads to collect context and relies on only two tool calls to construct and then verify its final deliverable.
In this task, the assignment is to review a set of documents for a proposed acquisition for Prism and produce a memo describing transaction structure, risk areas, and recommended next steps backed by specific details from the source documents. We see markedly better specificity and grounding in these trace excerpts:
GLM-5.1 Base
AC GLM-5.1
Tool Use Examples
read documents/market-data-summary.xlsx
returned over 200,000 characters into the token stream.
Builds a custom docx Python script that ultimately fails to construct an artifact due to parsing error:
from docx import Document; doc = Document(); ...
instead of using the available docx generation tool.
Failure to check the correct location (
/workspace/outputs
) for the output artifact via
cat /workspace/pre-notification-briefing-paper.docx resulting in No such file or directory
and lack of verification of the docx file type.
Tool Use Examples
read documents/kinney-pricing-email.eml offset 0 limit 1000
returns specified context “On Mon, Aug 12, 2024 at 3:47 PM Robert Kinney…”.
bash grep "commercial payors" documents/*.eml
highlighted the exact necessary phrase from a source email.
bash generate_from_md.py memo.md output/pre-notification-briefing-paper.docx
was correctly structured to use the provided tool and deliver a
docx
file type, followed by properly using the verify tool for a successful submission.
Final Deliverable Excerpts
"the Pinnacle/Meridian Transaction, a contemporaneous acquisition...rate increases from BlueCross BlueShield"
shows a focus on the wrong acquisitions due to overly broad file reads.
Generalizations like
"post-merger pricing power will increase”
lead to poor grader scores due to lack of specificity.
Poorly supported claims like
“Vertical concerns arise from ClearScript PBM, LLC, Meridian’s wholly-owned pharmacy benefits management subsidiary...”
lack evidence.
Final Deliverable Excerpts
References the correct source documents and specific dates:
"in the Kinney-Thornbury Pricing Email (August 12, 2024)"
"Exclusive Hospital Outreach Contracts (Total: $76M annual revenue, 30.8% of Prism revenue)"
details specific, grounded information relevant to the deliverable.
Grounded references to specific details
“Prism Diagnostics purchases approximately $620,000 in AllerSpec proprietary allergy reagent kits annually from LabVantage’s Cascade Reference Labs subsidiary...”
further the legal argument.
These trace excerpts show the model’s learned behaviors, showcasing its ability to make efficient, effective tool calls and make specific, grounded claims with relevant context from the supporting source documents.
Conclusion
Through our collaboration with Applied Compute on LAB, we trained GLM-5.1 into a state-of-the-art legal agent by optimizing the full stack: grader, harness, and full-parameter reinforcement learning on AC2. The resulting model lifts rubric pass rate from 0.853 to 0.913 and all-pass rate from 0.059 to 0.126, making it the strongest available model by rubric pass rate and second only to Opus 4.8 Max on all-pass rate.
Just as importantly, our analysis traced these gains to concrete, interpretable behaviors in improved artifact completeness, sharper specificity, and stronger grounding, showing that the improvements reflect real legal competence.
We believe complementary techniques can continue improving the model. We expect further gains from
relevance-masked self-distillation
to strengthen grounding and
agentic router training
to optimize for cost alongside quality. We look forward to continuing to push the frontier of vertical agents with Applied Compute and sharing more as these systems move from benchmarks into production.
Next Up
The Types of Legal Software That Define a Modern Legal Stack
The Complete Guide to In-House Legal Operations
How Law Firms Use AI to Win More Clients
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
Shared Spaces
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
