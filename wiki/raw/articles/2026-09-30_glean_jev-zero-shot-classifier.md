---
title: "Jev and the return of the zero-shot classifier"
source: "Glean Blog"
url: "https://www.glean.com/blog/jev-zero-shot-classifier"
scraped: "2026-09-30T06:00:29.223589+00:00"
lastmod: "2026-09-29T20:03:05.383Z"
type: "sitemap"
---

# Jev and the return of the zero-shot classifier

**Source**: [https://www.glean.com/blog/jev-zero-shot-classifier](https://www.glean.com/blog/jev-zero-shot-classifier)

Product
Platform overview
See how Glean works.
Built for enterprise AI.
Glean Enterprise Context
Ground AI in company context
Connectors & actions
Glean offers more than 250 connectors
APIs
Build generative AI experiences
API lookbook
Explore what you can build
Glean Protect
Safely scale AI at work
Glean Intelligence
Get more from every AI request
Auto routing
Route work to the right model
Model hub
Get access to the latest models
Usage controls
Control AI usage and spend
AI gateway
Govern every AI interaction
Glean Assistant
Your enterprise AI coworker
Proactive AI
Stay ahead of what matters
Content creation
Create grounded, on-brand content
Multiplayer
Create and refine work together
Work execution
Turn insight into action
Data analysis and research
Turn context into insights
Enterprise search
Find answers across your company
Glean Agents
Build and manage agents
Agent builder
Build agents your way
Agent orchestration
Automate work across systems
Agent governance
Scale agents with control
Agent library
Discover trusted, reusable agents
Coming soon
Glean Transform
See where AI can make the biggest impact
Customers
FEATURED STORIES
Booking.com
Zillow
TIME
Ericsson
See all customer stories
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
IT
Marketing
B2B Marketing
B2C Marketing
People
Finance
Legal
INDUSTRIES
Retail
Consumer Goods
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Professional Services
Consulting
Construction
IT Services
Financial Services
Banking
PE/VC
Asset management
Insurance
Government
Healthcare
Life Sciences
Higher Education
What’s the state of your AI stack for software engineering?
Take the quiz
See how your engineering AI stack performs across delivery speed, incident response, and context access. Get your AI Stack Score and next-step recommendations.
Take the quiz
Resources
EXPLORE
ENGAGE
Glean:GO 2026
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
The Work AI Index 2026
Workers say AI saves them 11 hours a week. Where is that time going?
Download the report
Company
About us
Glean on Glean
Story
Culture
Careers
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Sign in
Get a demo
Get a demo
Sign in
Get a demo
Get a demo
Product
Customers
Solutions
Resources
Company
Sign in
Sign in
Get a demo
Get a demo
PRODUCT
Platform overview
See how Glean works.
Built for enterprise AI.
Glean Enterprise Context
Ground AI in company context
Connectors & actions
Glean offers more than 250 connectors
APIs
Build generative AI experiences
API lookbook
Explore what you can build
Glean Protect
Safely scale AI at work
Glean Intelligence
Get more from every AI request
Auto routing
Route work to the right model
Model hub
Get access to the latest models
Usage controls
Control AI usage and spend
AI gateway
Govern every AI interaction
Glean Assistant
Your enterprise AI coworker
Proactive AI
Stay ahead of what matters
Content creation
Create grounded, on-brand content
Multiplayer
Create and refine work together
Work execution
Turn insight into action
Data analysis and research
Turn context into insights
Enterprise search
Find answers across your company
Glean Agents
Build and manage agents
Agent builder
Build agents your way
Agent orchestration
Automate work across systems
Agent governance
Scale agents with control
Agent library
Discover trusted, reusable agents
Coming soon
Glean Transform
See where AI can make the biggest impact
Sign in
Get a demo
Get a demo
CUSTOMERS
FEATURED STORIES
Booking.com
Zillow
TIME
Ericsson
See all customer stories
Sign in
Get a demo
Get a demo
SOLUTIONS
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
IT
Marketing
B2B Marketing
B2C Marketing
People
Finance
Legal
INDUSTRIES
Retail
Consumer Goods
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Professional Services
Consulting
Construction
IT Services
Financial Services
Banking
PE/VC
Asset management
Insurance
Government
Healthcare
Life Sciences
Higher Education
What’s the state of your AI stack for software engineering?
Take the quiz
See how your engineering AI stack performs across delivery speed, incident response, and context access. Get your AI Stack Score and next-step recommendations.
Take the quiz
Sign in
Get a demo
Get a demo
RESOURCES
EXPLORE
ENGAGE
Glean:GO 2026
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
The Work AI Index 2026
Workers say AI saves them 11 hours a week. Where is that time going?
Download the report
Sign in
Get a demo
Get a demo
COMPANY
About us
Glean on Glean
Story
Culture
Careers
Last updated Sep 29, 2026.
Jev and the return of the zero-shot classifier
0
minutes read
Eddie Zhou
Engineering
Chau Tran
Engineering
Aviral Singh
Software Engineer
Matthew Zhao
Engineering
Listen to article
0:00
0.5x
1x
1.5x
2x
Table of contents
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Share this article:
Listen to article
0:00
0.5x
1x
1.5x
2x
Jev is a model that excels at making typed decisions. That’s when you send it context plus a fixed set of questions and options, and it returns choices, scores, and probabilities instead of generating text. This is what we call a “System One” model.
But classification is not new, and neither are structured outputs, small models, or reading probabilities from logits. That history explains some of the split reaction to Jev:
The skeptics have a real point, but Jev has a real place in this ecosystem.  To understand more, we should lay out the full solution space.
What are the alternatives?
When a system needs a label, score, or yes-or-no answer, there are four reasonable options:
<div class="overflow-scroll" role="region" aria-label="Approaches comparison">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Approach</th>
<th class="rich-text-table_header" scope="col">Why use it</th>
<th class="rich-text-table_header" scope="col">Tradeoff</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">A general-purpose LLM</td>
<td class="rich-text-table_cell">Zero-shot, flexible, and can also generate arguments or explanations. Arguably “higher intelligence” via inference-time compute (reasoning).</td>
<td class="rich-text-table_cell">Paying autoregressive-model latency and cost for a small decision</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">An open zero-shot classifier</td>
<td class="rich-text-table_cell">Cheap, local, and controllable</td>
<td class="rich-text-table_cell">Variable quality; you own model selection and serving</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">A fine-tuned classifier</td>
<td class="rich-text-table_cell">Usually the best bet for a stable, high-volume task with good labels</td>
<td class="rich-text-table_cell">Data collection, training, deployment, drift, and a less flexible taxonomy</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Jev</td>
<td class="rich-text-table_cell">Zero-shot flexibility behind a clean, hosted API</td>
<td class="rich-text-table_cell">Task-dependent quality, no generated text, and provider dependency</td>
</tr>
</tbody>
</table>
</div>
The case for Jev: a team can change the question and options without collecting a new training set, while avoiding the work of serving a model well. No one should turn their nose up at that. “We could build it ourselves” is true of most infrastructure products.
Open reproductions keep the novelty claim in check. Implementations using
Qwen and SGLang
,
DiffusionGemma and vLLM
, and
Kev
recreate much of the API or model shape.
85.7% for Jev and 79.6% for Kev-8B on n=764
Parallel’s external tests
likewise found Jev competitive on reranking, while specialized models still won two classification tasks.
What we’ve seen at Glean
That leaves a practical question: when does Jev’s combination of zero-shot flexibility and hosted inference actually beat the alternatives? We tested four bounded decisions at Glean where we already had a baseline and could test for enterprise quality. Most of these baselines are LLM-based systems, so for those experiments, we know to expect two orders of magnitude improvement on cost and latency. The results ranged from materially worse than production to both faster and more accurate than an LLM-based router.
Query classification
Query classification maps a request to a broad task used by downstream systems. It is a natural Jev workload because while on a per-request basis, the label space is known in advance, the taxonomy can still change faster than a fine-tuned classifier can be retrained.
For this experiment, we focus on gauging Jev’s agreement against our production/baseline predictions, which are LLM-based. We expect and observe a large speedup in offline throughput with Jev, so we report agreement as an easy proxy for quality. We also baselined against Laya, an open-weight decision model, as well as a fine-tuned Laya. This fine-tuning ran locally in a few hours, and the model is also small enough to be served on a developer machine.
<div class="overflow-scroll" role="region" aria-label="Experiment results">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Experiment</th>
<th class="rich-text-table_header" scope="col">Broad Task Agreement</th>
<th class="rich-text-table_header" scope="col">Perf</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Jev zero-shot</td>
<td class="rich-text-table_cell">66.8%</td>
<td class="rich-text-table_cell">~12min (concurrency of 4)</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Base Laya</td>
<td class="rich-text-table_cell">35.9%</td>
<td class="rich-text-table_cell">~90s (local dev machine)</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Fine-tuned Laya</td>
<td class="rich-text-table_cell">74.5%</td>
<td class="rich-text-table_cell">~90s (local dev machine)</td>
</tr>
</tbody>
</table>
</div>
As a convenient, no-training off-the-shelf model, Jev clearly outperforms Laya, but somewhat unsurprisingly, fine-tuning makes Laya shine, especially given the performance numbers. The trade-off is the amount of effort required to obtain good labels and set up training. Jev likely remains more attractive when a task is new, or its labels are changing.
Model routing: expert transfer
Model routing is a related problem to query classification. Here, we frame model routing as expert transfer, where our system chooses which expert/model should handle the request. Our production baseline currently asks an LLM to make that decision natively inside the harness's agentic loop. While this is a natural test of whether Jev can replace a generative call with a bounded decision, an important technical limitation is that Jev will strictly
add
a call in the event of a non-transfer. This is in contrast to the production baseline, which in non-transfer cases, can begin the tool-calling work via the same single first LLM call.
We used a simplified version of our production routing with only 3 experts, replayed 751 comparable golden entries through the updated Jev router, compared its chosen route with our existing prompt-based router (powered by a traditional LLM), and measured the accuracy against the golden label.
<div class="overflow-scroll" role="region" aria-label="Expert routing comparison">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Route</th>
<th class="rich-text-table_header" scope="col">Gold entries</th>
<th class="rich-text-table_header" scope="col">Baseline precision</th>
<th class="rich-text-table_header" scope="col">Baseline recall</th>
<th class="rich-text-table_header" scope="col">Jev precision</th>
<th class="rich-text-table_header" scope="col">Jev recall</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Expert 1</td>
<td class="rich-text-table_cell">34</td>
<td class="rich-text-table_cell">70.2%</td>
<td class="rich-text-table_cell">97.1%</td>
<td class="rich-text-table_cell">86.8%</td>
<td class="rich-text-table_cell">97.1%</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Expert 2</td>
<td class="rich-text-table_cell">42</td>
<td class="rich-text-table_cell">47.1%</td>
<td class="rich-text-table_cell">38.1%</td>
<td class="rich-text-table_cell">86.7%</td>
<td class="rich-text-table_cell">61.9%</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Expert 3</td>
<td class="rich-text-table_cell">6</td>
<td class="rich-text-table_cell">12.5%</td>
<td class="rich-text-table_cell">33.3%</td>
<td class="rich-text-table_cell">85.7%</td>
<td class="rich-text-table_cell">100%</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">No expert</td>
<td class="rich-text-table_cell">669</td>
<td class="rich-text-table_cell">95.6%</td>
<td class="rich-text-table_cell">93.4%</td>
<td class="rich-text-table_cell">97.6%</td>
<td class="rich-text-table_cell">98.7%</td>
</tr>
</tbody>
</table>
</div>
We also isolated 40 entries where the existing path made an actual expert-transfer call (smaller n) and compared call latency on those same entries.
The median per-entry speedup was 8.1×. This is one of the strongest internal Jev results so far: on this bounded routing task,
Jev was both more accurate and substantially faster
. The magnitude of the delta implies that the “blocking” tax we incur on non-expert-routed requests may be a good tradeoff. Note that it is still an offline golden-set comparison, and the latency sample contains only 40 positive transfers, so there's a lot more to derisk and test!
Reranking
A problem near and dear to Glean! Below, our production baseline is the order produced by Glean’s existing search stack. This experiment then asked Jev to reorder up to 50 results.
We tried four ways to express relevance through Jev’s typed outputs:
<div class="overflow-scroll" role="region" aria-label="Relevance formulations">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Formulation</th>
<th class="rich-text-table_header" scope="col">How it expresses relevance</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Pointwise Noul</td>
<td class="rich-text-table_cell">Ask a separate yes-or-no relevance question for each result, then sort by the probability of “yes.”</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Shared-state Noul</td>
<td class="rich-text-table_cell">Show Jev the full candidate set as shared context, then ask the same yes-or-no question for each result.</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Score</td>
<td class="rich-text-table_cell">Ask Jev to assign each candidate a numerical relevance score.</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Choice</td>
<td class="rich-text-table_cell">Treat all candidates as alternatives in one decision, then rank them by their resulting probabilities.</td>
</tr>
</tbody>
</table>
</div>
We ran this on an internal evalset where the user does not have access to all canonicals, so the absolute numbers are not reflective of our production ranking – but the relative numbers are of interest.
Jev “Choice” was the strongest formulation. On a paired control of 4,855 captured search queries, with production-based tie-breaking removed, the result was:
<div class="overflow-scroll" role="region" aria-label="Ranker performance comparison">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Ranker</th>
<th class="rich-text-table_header" scope="col">Recall@1</th>
<th class="rich-text-table_header" scope="col">Recall@3</th>
<th class="rich-text-table_header" scope="col">Recall@6</th>
<th class="rich-text-table_header" scope="col">Evaluator MAP</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Existing Glean production order</td>
<td class="rich-text-table_cell">35.74%</td>
<td class="rich-text-table_cell">45.79%</td>
<td class="rich-text-table_cell">51.18%</td>
<td class="rich-text-table_cell">0.4289</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">GPT-6-Luna-high as Reranker</td>
<td class="rich-text-table_cell">30.71%</td>
<td class="rich-text-table_cell">39.15%</td>
<td class="rich-text-table_cell">45.08%</td>
<td class="rich-text-table_cell">0.3766</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">GPT-6-Sol-high as Reranker</td>
<td class="rich-text-table_cell">31.54%</td>
<td class="rich-text-table_cell">40.14%</td>
<td class="rich-text-table_cell">46.84%</td>
<td class="rich-text-table_cell">0.3862</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Jev Choice</td>
<td class="rich-text-table_cell">24.37%</td>
<td class="rich-text-table_cell">33.72%</td>
<td class="rich-text-table_cell">40.21%</td>
<td class="rich-text-table_cell">0.3201</td>
</tr>
</tbody>
</table>
</div>
Jev Choice cost roughly $0.00044 per query and took 0.195 seconds at p50 in the offline test. But it assigned identical scores to roughly 37 of the 41 candidates in an average query. Using production order to resolve those ties raised Recall@6 from 40.2% to 44.3%, making the uncorrected result look stronger than Jev’s scores alone warranted. There are many caveats here as per usual, but directionally,
Jev is a cheap, efficient baseline, not a replacement for Glean’s production ranker.
Citation-support judging
Citation judging asks two related questions: do claims that need evidence have adequate citations (
citation recall
), and do the cited sources actually support the claims attributed to them (
citation precision
)? At first glance, because the output/label space is bounded (similar to most judge settings) this seems like an obvious fit for Jev. The rubric is complex, however, and may require decomposing several claims – in addition, Jev doesn’t produce the rationale that we often use for error analysis, so there is some risk to both quality and usability.
We tested Jev on a real 1,448-word production-eval response, holding the response and citation evidence fixed. We compared its shared precision-and-recall pass with GPT-5.6 Luna using no reasoning and xhigh reasoning. To reduce variance, we ran each judge three times.
<div class="overflow-scroll" role="region" aria-label="Judge time and cost">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Judge</th>
<th class="rich-text-table_header" scope="col">Original measured time per response</th>
<th class="rich-text-table_header" scope="col">Original measured cost per response</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Jev</td>
<td class="rich-text-table_cell">6.6 s</td>
<td class="rich-text-table_cell">$0.014</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">GPT-5.6 Luna, no reasoning</td>
<td class="rich-text-table_cell">81.3–85.5 s</td>
<td class="rich-text-table_cell">$0.030–$0.047</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">GPT-5.6 Luna, xhigh</td>
<td class="rich-text-table_cell">227.4–259.7 s</td>
<td class="rich-text-table_cell">$0.047–$0.060</td>
</tr>
</tbody>
</table>
</div>
Note that the timing is directional rather than end-to-end: Jev reports sequential client wall time, while the Luna rows sum model-call durations. Costs include observed caching.
We also compared
consistency
on the same 28 paragraphs. A changed item means the judge changed its verdict on whether a paragraph had adequate citation coverage in at least one of three identical-input runs. Pairwise disagreement counts each paragraph across the three run pairs, for 84 comparisons per judge.
<div class="overflow-scroll" role="region" aria-label="Recall consistency comparison">
<table class="rich-text-table_component">
<thead class="rich-text-table_head">
<tr class="rich-text-table_row">
<th class="rich-text-table_header" scope="col">Judge</th>
<th class="rich-text-table_header" scope="col">Paragraphs with a changed recall verdict</th>
<th class="rich-text-table_header" scope="col">Pairwise recall disagreements</th>
</tr>
</thead>
<tbody class="rich-text-table_body">
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">Jev</td>
<td class="rich-text-table_cell">1 of 28 (3.6%)</td>
<td class="rich-text-table_cell">2 of 84 (2.4%)</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">GPT-5.6 Luna, no reasoning</td>
<td class="rich-text-table_cell">7 of 28 (25.0%)</td>
<td class="rich-text-table_cell">15 of 84 (17.9%)</td>
</tr>
<tr class="rich-text-table_row">
<td class="rich-text-table_cell">GPT-5.6 Luna, xhigh</td>
<td class="rich-text-table_cell">5 of 28 (17.9%)</td>
<td class="rich-text-table_cell">10 of 84 (11.9%)</td>
</tr>
</tbody>
</table>
</div>
Jev’s only change was whether one paragraph counted as needing a citation; its raw recall category did not change. Jev’s paragraph-level citation-coverage verdicts were therefore
more repeatable
than either Luna configuration.
We're not concluding that this makes Jev the more accurate judge (the systems applied different support criteria and scoring denominators, and we didn't have time to do independent human labels). But even with xhigh reasoning (which roughly tripled Luna’s model time), it remained less consistent than Jev. The result supports
Jev as a fast, inexpensive, and comparatively repeatable way to implement a narrow citation policy.
Experiment takeaways and practical guide
In some cases, Jev shines as a low-friction alternative to both traditional LLMs and fine-tuned classifiers. When the baseline is strong (reranking), or it’s easy to fine-tune a smaller model (query classification), the upside is weaker. There are signs of stronger quality for some tasks (model routing) as well as indications of better consistency and stability (citation judge). In some of our most important workloads, it delivers the expected cost and latency wins against traditional LLMs.
The above results give good directional leads, and at Glean, we’re very excited about Jev. After a few more steps (mainly, operational readiness like data residency and guarantees) we plan to ship Jev into some of these use cases. Also, Jev will play a big role in our internal hackathon this week and we’re excited to share more results!
Some general advice to conclude – if the output can be listed in advance, benchmark Jev. If the task and labels are stable and volume is high, benchmark a fine-tuned classifier too. If the call needs to generate a query, explanation, or other dynamic text, keep a generative model in the loop. Tool calling is a good example: Jev can help choose a tool, but most Glean tools still need dynamically generated arguments (like search queries).
Jev does not change the fact that classifiers already existed. It makes a good zero-shot classifier much easier to use. That’s a solid product, even if it’s not a new foundation for every AI system.
Authors:
Eddie Zhou
,
Chau Tran
,
Aviral Singh
,
Matt Zhao
,
Manav Agrawal
.
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Get The Resource
Get The Resource
Work AI for all.
Get a Demo
See Work AI in action
Get a demo
Get a demo
Ask AI for a summary about Glean
634 2nd Street
San Francisco, CA 94107
United States
English
English
Japanese
French
Product
Platform
Glean Enterprise Context
Connectors
&
Actions
APIs
API Lookbook
Glean Protect
Glean Intelligence
Auto routing
Model hub
Usage controls
AI Gateway
Assistant
Proactive AI
Content Creation
Multiplayer
Work Execution
Data Analysis & Research
Enterprise Search
Agents
Agent Builder
Agent Orchestration
Agent Governance
Agent Library
Solutions
All Teams
Engineering
Sales
Marketing
Support
People
Retail
Financial Services
Use cases
Enterprise AI
Enterprise Search Software
AI Agent Orchestration
Enterprise AI Software
AI Agent Builder
Comparisons
Glean vs other alternatives
Glean vs ChatGPT Enterprise
Glean vs Microsoft 365 Copilot
Glean vs Claude Enterprise
Resources
Content Hub
Product Videos
Guides
Customer Stories
Blog
Events
Webinars
Developers
Help Center
Download Glean
Product Drops
Gleaniverse Community
Customers
Booking.com
Zillow
TIME
Ericsson
Databricks
DBS
Customer Stories
Company
About
Careers
Newsroom
Referrals
Partners
Trust center
©
2026
, Glean Technologies, Inc.
Cookie Preferences
Website Terms
Privacy
