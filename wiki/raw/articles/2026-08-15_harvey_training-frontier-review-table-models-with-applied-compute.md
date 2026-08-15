---
title: "Training Frontier Review Table Models With Applied Compute"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/training-frontier-review-table-models-with-applied-compute"
scraped: "2026-08-15T06:00:09.197414+00:00"
lastmod: "2026-08-14T17:00:00.000Z"
type: "sitemap"
---

# Training Frontier Review Table Models With Applied Compute

**Source**: [https://www.harvey.ai/blog/training-frontier-review-table-models-with-applied-compute](https://www.harvey.ai/blog/training-frontier-review-table-models-with-applied-compute)

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
Shared Spaces
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
Shared Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
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
Training Frontier Review Table Models With Applied Compute
How Harvey and Applied Compute built a specialized model that delivers higher-quality legal document analysis at lower cost.
by
Vasudha Rengarajan
,
Karl de la Roche
,
Stephen Rice
,
Niko Grupen
,
Julio Pereyra
,
Gabe Pereyra
,
Nic Becker
,
Jacob Phillips
, and
Rhythm Garg
•
Aug 14, 2026
Applied Compute and Harvey partnered to train a model for Harvey’s Review Table product, achieving higher accuracy and lower latency at a fraction of the cost of frontier models.
Our post-trained model outperforms the cost-quality pareto frontier on Review Table tasks. Answer Score measures per-cell response quality, combining answer correctness and citation quality into a single 0-1 metric. All models are evaluated at minimal reasoning effort to meet product latency requirements.
Review Table is one of Harvey’s highest inference-volume workloads in production. At production scale, small improvements in accuracy, latency, and cost can compound into meaningful product-level gains. We trained a specialized model for Harvey’s existing semantic-retrieval workflow, testing how far we could push the cost-quality frontier.
Review Tables: Legal Document Analysis at Scale
Review Table is Harvey's large-scale document analysis tool. It allows lawyers to complete tasks that require reviewing enormous volumes of documents, such as litigation document review or the contract-analysis phase of due diligence.
A lawyer uploads up to 10,000 files, writes questions about each document in the corpus (these questions become the column headers of the table), and then Harvey returns a grid: one row per document group, one cell per question, where every cell contains an answer. Harvey also provides its reasoning, and citations to the source text.
Questions vary widely in what they demand of the model. Some ask to extract values that appear verbatim in the text. Others require dates, currencies, or durations to be identified and then parsed into a normalized format. Still others require information scattered across multiple sections to be synthesized into free-form analysis.
Harvey’s Review Tables enable lawyers to run analysis across thousands of documents and dozens of tasks.
Every cell is its own model call over one or more documents. A single table – potentially thousands of files multiplied by dozens of questions – can trigger hundreds of thousands of model calls. At that scale, small differences in per-call accuracy, latency, and cost compound quickly. That compounding is what makes Review Table a natural target for post-training.
Building a Synthetic Review Table Dataset
Harvey has strict data requirements, and no customer data is ever used for training purposes. To model document and query distributions that we expect to see in practice, we scraped open-source legal data, including filings, contracts, emails, and other document types, and turned it into an offline document corpus. This corpus became the foundation for a synthetic dataset designed to reflect how lawyers actually use Review Tables.
We collaborated to develop a synthetic dataset that approximates the true Review Table distribution. Each produced sample went through several rounds of filtering, deduplication, and quality checks.
We built robust data pipelines using the Applied Compute Agent Cloud, or AC2. For every document, we created metadata and embeddings tracking provenance, content, filetype, length, and other attributes. These tags let us filter and deduplicate the corpus, preserving a broad mix of legal domains, document structures, and content before downselecting to approximate the Review Table distribution. To create tasks, we prompted frontier models to emulate representative user personas and generate diverse queries across the corpus. Next, oracle agents with full access to tools and the environment determined ground-truth answers for each query, including when the correct response is to abstain. Finally, several rounds of quality control with human experts compared answers across agents to ensure the training examples were high quality.
Reward Design
Each response in the Review Table must meet multiple requirements to be considered a high-quality answer. The response needs to:
Identify the right part(s) of the document
Correctly answer the question (or abstain from answering when not applicable)
Format the answer according to the user’s specifications
Return the correct value, and cite the correct evidence.
To meet these requirements, we designed a reward function that grades each of these dimensions separately. For a standard answer, the base reward is:
b
=
min
⁡
(
s
s
c
h
e
m
a
,
s
c
o
r
r
e
c
t
n
e
s
s
)
b = \min\left(s_{\mathrm{schema}},\,s_{\mathrm{correctness}}\right)
b
=
min
(
s
schema
​
,
s
correctness
​
)
The minimum acts as a gate such that both schema adherence and correctness of the final answer must be satisfied. Schema adherence, as well as correctness for verifiable response types like dates and numerics, can be computed deterministically. The correctness for extraction and free-response answers are evaluated by an LLM judge that determines whether the model’s response is semantically equivalent to a reference response.
Citations receive a separate sentence-level score. One challenge of explicitly rewarding cited evidence in RL training is preventing the model overzealously citing passages from the document. We found that adding a term to the reward consisting of a product between recall and precision was effective at optimizing citation quality, while penalizing citation spamming behavior more than other metrics like F1 score.
Recall measures how much of the reference evidence the model cited:
R
c
i
t
e
=
∣
matched reference evidence
∣
∣
reference evidence
∣
R_{\mathrm{cite}}
=
\frac{\left|\text{matched reference evidence}\right|}
{\left|\text{reference evidence}\right|}
R
cite
​
=
∣
reference evidence
∣
∣
matched reference evidence
∣
​
Precision measures how many cited sentences actually support the answer:
P
c
i
t
e
=
∑
i
1
⁣
[
citation
i
supports the answer
]
N
r
e
s
o
l
v
e
d
+
N
i
n
v
a
l
i
d
P_{\mathrm{cite}}
=
\frac{\sum_i \mathbf{1}\!\left[\text{citation }i\text{ supports the answer}\right]}
{N_{\mathrm{resolved}} + N_{\mathrm{invalid}}}
P
cite
​
=
N
resolved
​
+
N
invalid
​
∑
i
​
1
[
citation
i
supports the answer
]
​
Each cited sentence is evaluated independently. Invalid citation indices remain in the denominator, preventing the model from receiving free credit for citations that cannot be resolved to the source document.
We combine precision and recall as:
q
c
i
t
e
=
R
c
i
t
e
P
c
i
t
e
q_{\mathrm{cite}} = R_{\mathrm{cite}}P_{\mathrm{cite}}
q
cite
​
=
R
cite
​
P
cite
​
The final reward folds citation quality into the base task score with a soft multiplicative term:
r
=
b
[
(
1
−
λ
)
+
λ
q
c
i
t
e
]
r
=
b\left[(1-\lambda)+\lambda q_{\mathrm{cite}}\right]
r
=
b
[
(
1
−
λ
)
+
λ
q
cite
​
]
This construction keeps answer quality as the most important component of the model’s score. A wrong answer still receives zero regardless of its citations. A fully correct and well-cited answer receives full credit. A correct answer with missing or poorly selected evidence receives less than full credit, but is not treated as equivalent to a wholly incorrect answer. We empirically determined
λ
=
0.3
\lambda=0.3
λ
=
0.3
to be a suitable weighting for this reward.
Specialized Models for Review Table
Harvey’s Review Tables rely on substantial harness and prompt engineering for effective information retrieval. We trained a custom model in the production Review Table harness using Applied Compute’s AC2 platform to optimize for frontier model performance at a fraction of the cost.
A single-turn model optimized for semantic search extraction.
The production Review Table harness uses semantic search to retrieve snapshots of the relevant document corpus for each Review Table cell. This creates a large prefill designed to include information needed to answer the query. During model training, the policy learns to reason over the context, select the correct information, and output the exact schema and behavior that lawyers want.
Across our evaluation set, the custom Review Table model has improved answer quality while using fewer resources than the strongest general-purpose baselines. The largest gains were in
correctness and citation quality
,
where the model achieved a 22.4% increase compared to citation quality over the base GLM 5.2 checkpoint. At the same time, average cost per cell fell by 54.8% compared to Claude Sonnet 5 on the same tasks.
A comparison of AC-Harvey Review Table Answer Score comparing the AC Trained model to a sweep of frontier models from OpenAI, Anthropic, Gemini, and Z.ai families.
On answer quality, the AC Review Table model reached 0.903 on our benchmark, compared with 0.867 for Fable 5 and 0.857 for GPT-5.6-Sol. This represents an improvement of 5.8 percentage points over the base GLM5.2 checkpoint.
A comparison of AC-Harvey Review Table Citation Score comparing the AC Trained model to a sweep of frontier models from OpenAI, Anthropic, Gemini, and Z.ai families.
Citation quality followed a similar pattern, where the custom model achieved 84.1% citation precision and 91.93% citation recall. Relative to the GLM5.2 baseline, this represents
an increase of 15.38 percentage points for the custom model’s citation score.
These results show that model specialization alone can materially improve the Review Table production frontier, without changing the retrieval architecture.
When Agentic Search Helps
The results above show how post-training can improve Review Table performance within Harvey’s existing single-turn semantic-retrieval setup. Fixed retrieval works well when the initial semantic search surfaces the right evidence, but it can be inefficient when only a small portion of a document is relevant. The model is also unable to retrieve additional information if the initial context is incomplete. This motivated a separate experiment: could an agentic model retrieve evidence more selectively while maintaining comparable answer quality?
To isolate the effect of the retrieval harness from the main Review Table model results, we trained two Qwen3.6-35B-A3B models under the same answer score objective. One model was trained in the existing single-turn semantic-retrieval harness, which retrieves a broad set of document context before inference. The other was trained in a multi-turn agentic harness equipped with read- and grep-style tools, allowing it to search the document corpus iteratively as it reasons.
The two approaches have different computational profiles: single-turn retrieval pays for large context up front, while the agentic system instead trades that large prefill for several smaller model turns and targeted searches. This can be particularly useful for questions that can be narrowed to specific information; for example, an agent can search for a particular provision or email address directly rather than loading the broad context.
The single-turn harness commits to large numbers of prefill tokens while the agentic harness takes smaller, iterative turns searching the document. The agentic harness uses half as many total tokens to reach the same Answer Quality eval score.
We compared the two Qwen3.6 models after training them to nearly identical answer scores. The agentic model reached 0.799, compared to 0.794 with the single-turn model and harness. At this matched level of answer quality, the agentic harness used 50.3% fewer input tokens and 28.6% fewer output tokens, trading a modest increase in response time for a large reduction in total token usage. These results suggest that retrieval architecture is an important optimization lever alongside model post-training: training a model to use a more targeted, agentic retrieval strategy can substantially improve token efficiency while maintaining high quality model responses.
The Case for Model Specialization
High-volume document analysis makes small model-level improvements compound quickly. By training against Review Table’s data distribution and production requirements, we built a model that improves answer and citation quality while reducing the cost of serving each cell.
Separately, our agentic retrieval experiments showed that the way a model acquires context is another meaningful optimization lever that can substantially reduce token usage at matched answer quality. Harvey’s Review Table is an excellent example of where domain expertise can build upon open models to create capabilities that outperform more general-purpose models on specific, demanding workloads.
Next Up
The Judgment Contract Redlining Still Requires
The Hidden Constraint in Contract Redlining Software
The Legal Team's Guide to Employment Contract Drafting
Unlock Professional Class AI for Your Firm
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
Shared Spaces
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
In-House
→
Transactional
→
Litigation
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
