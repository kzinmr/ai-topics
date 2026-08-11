---
title: "Nexus GA: It's the Knowledge, Not the Models"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pinecone-nexus-generally-available/"
scraped: "2026-08-11T06:00:34.784252+00:00"
lastmod: "2026-08-07T14:17:16Z"
type: "sitemap"
---

# Nexus GA: It's the Knowledge, Not the Models

**Source**: [https://www.pinecone.io/blog/pinecone-nexus-generally-available/](https://www.pinecone.io/blog/pinecone-nexus-generally-available/)

←
Blog
Nexus GA: It's the Knowledge, Not the Models
Pinecone Nexus Is Now Generally Available
Jasmeet Singh Gujral
,
Siva Ragavan
Aug 6, 2026
Product
Share:
Jump to section:
What's Ready Now
The Benchmark: Same Models, Different Knowledge
Where Enterprise Agents Break in Production
How Nexus Works: Compile Once, Answer Every Time
Four Failures, Solved at the Knowledge Layer
We Ran It On Our Own Support Queue
A Knowledge Layer That Stays True
Start Building
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Five weeks ago we opened Pinecone Nexus to Public Preview. Today Nexus is generally available to be deployed in your own cloud.
On τ-Knowledge, Sierra's open benchmark for agentic customer-service work, we gave GPT-5.5 and GPT-5.2 a Nexus knowledge layer and ran them against the same models using the benchmark's own tools. GPT-5.5 held its accuracy at 77% less cost per task. GPT-5.2 achieved 12% more accuracy and saw 80% cost reduction. Both cut their tool calls and model calls roughly in half.
We also pointed Nexus at our own customer support queue. The agent handling inbound tickets went from resolving 25% of them on its own to 55%.
Here’s why the benchmark reads the way it does, what Public Preview taught us about how enterprises manage knowledge, and what GA changes for you.
What's Ready Now
The durable advantage an enterprise has is its knowledge and how its people do the work. Every agent call that ships that knowledge to a third-party model transfers a piece of that advantage to someone else. Nexus keeps it where it belongs: in a governed layer, in your cloud, shaped by your own experts. That principle runs through everything shipping today. Nexus is ready for the standard enterprise motion: evaluate, pilot, procure, run in production. As of today:
Deployment.
The Nexus data plane runs in your own cloud, on AWS, Google Cloud, or Azure. Your documents and compiled knowledge never leave your infrastructure.
Model choice.
Nexus runs on the models you choose, including open-weight. You supply the model credentials, and inference calls go from your cloud to the provider you name. Each workflow can use an ensemble, with the right model picked for each step.
No lock-in.
The knowledge layer Nexus compiles is yours. You can download it as an archive.
One interface.
Agents, chatbots, AI search, and recommendation systems all query the same layer through KnowQL. Find the specifications at
spec.knowql.org
.
Platform fit.
Nexus sits within the broader Pinecone platform, with Pinecone Database as its retrieval foundation and Pinecone Marketplace offering production-ready knowledge apps.
All of that rests on one claim: enterprise agents hit a knowledge ceiling long before they hit a model ceiling. To check it, we ran the following test.
The Benchmark: Same Models, Different Knowledge
τ-Knowledge is Sierra's open-source benchmark for agentic customer-service work: multi-step reasoning, strict policy adherence, coordinated tool use. It grades on whether the agent drives the system to the correct end state. Its newest domains are knowledge-intensive by design. The agent has to find and apply the right policy before it acts, and a plausible answer grounded in the wrong version of a policy scores zero. That is the workload we built Nexus for, so we ran its
domain that has 97 tasks, where the agent has to find and apply the right policy before it acts.
GPT-5.2
GPT-5.2 with Nexus
GPT-5.5
GPT-5.5 with Nexus
Tool calls per task
42.5
17.7
28.6
16.0
Model calls per task
81.7
42.6
60.9
39.4
Note
: Results are from benchmarks ran as of Aug 4, 2026.
GPT-5.2 on its own averaged 42.5 tool calls and 81.7 model calls per task, grinding through documents to assemble an answer. With Nexus it asked for the answer instead: 17.7 tool calls, 42.6 model calls, and about six KnowQL queries per task. Half the model calls, and each one carrying less context, is where a $1.45 task becomes a $0.53 task. GPT-5.5 moved the same way, from 28.6 tool calls and 60.9 model calls down to 16.0 and 39.4. The cost advantage held on 97 of 97 tasks for GPT-5.2 and 96 of 97 for GPT-5.5, so this is not an average hiding a wide spread.
Why the gap is this large: the models by themselves have enough reasoning capability. What they lack is grounded knowledge they can reach cheaply. And it gets expensive for an agent when it spends most of its token budget locating and re-reading policy documents. Give the same model a compiled, governed layer it can query in one call and the reasoning gets spent on the task.
Where Enterprise Agents Break in Production
Enterprises have moved agents out of demo and into production across finance, insurance, legal, retail, and support. The move exposes four failures at once which can be a deal-breaker for enterprises in regulated industries:
Task completion and accuracy
on hard corpora stalls short of what production needs.
Token bills
climb faster than the value the agents return.
High latency
per task breaks production service levels.
And the answers carry no citation
, so nobody can trace a claim back to the document and clause it came from.
Most enterprises blame the model and wait for the next frontier release. But the data doesn’t support this approach. In a survey of 306 teams running agents in production, reliability outranked model capability as the top development challenge, and 68% cap their agents at ten steps before a human steps in. Meanwhile it was evident that cost does not respond to cheaper models. Blended inference costs fell about 67% year over year while average enterprise AI budgets rose from $1.2 million in 2024 to $7 million in 2026, because one agent task runs many model calls, each re-sending the context gathered so far. Goldman Sachs projects token consumption to multiply 24x between 2026 and 2030, so the waste per task compounds. A bigger model does not fix a bill that scales with retrieval, or a completion rate capped by the context an agent can reach.
Failure points in accuracy, latency, cost, and trust share one root cause, which is the work an agent does before it reasons. It reads the task, searches for context, reads the result, searches again, and re-sends everything it has gathered on the next turn before it takes a single action. Most of the token and latency budget is spent before the agent decides anything.
The retrieval itself is lossy. A vector or hybrid search returns the top matching chunks of text, stripped of the relationships that connect them. The agent gets fragments and has to reconstruct, on every request, how a policy connects to a record or how one clause qualifies another. When the answer depends on the relationship rather than the passage, top-K retrieval misses it. In a knowledge-intensive task, a fluent answer grounded in the wrong version of a policy scores zero.
Agentic RAG re-derives context on every query and re-embeds whenever the data or the task changes. Central ontologies, the model-the-whole-business approach from Palantir and Microsoft, are authored up front by a team that does not do the work, and they decay from the day they ship. Either the knowledge is assembled at query time, or it is modeled once and left to drift. That is the ceiling.
How Nexus Works: Compile Once, Answer Every Time
Watch "
Youtube Video Player
" on YouTube
Watch
Nexus moves the retrieval work out of the per-query loop. It compiles your systems-of-record data into governed, domain-specific knowledge once, ahead of time, and agents reuse that compiled layer on every call. Three parts that make it work:
The manifest.
A subject matter expert describes the work in their own terms, and that description becomes a Manifest: the entities that matter, the relationships between them, and the shape of the answers the work requires. The person who understands the domain defines it, not a central modeling team. A Manifest is scoped to a job rather than to the whole company.
The compiled knowledge layer.
Guided by the Manifest, Nexus compiles raw sources into structured knowledge artifacts: summaries, structured extracts, and the entity-and-relationship graph that top-K retrieval throws away.
KnowQL.
Agents query the compiled layer through KnowQL, a declarative language built for agents. The agent states what it needs, the question, the output shape, the scope, the grounding, and the budget. It gets back a typed, cited answer in one call.
Four Failures, Solved at the Knowledge Layer
Accuracy:
The compiled layer keeps the relationships between facts and carries per-field citations and confidence, so an agent gets connected, grounded knowledge rather than a bag of passages, with conflicts already resolved by the expert. Task completion clears the ceiling that keeps agents stuck in pilot, on answers an auditor will accept.
Latency:
One KnowQL call against a precompiled layer replaces the retrieve-evaluate-re-retrieve loop and its round trips. Agents meet production service levels instead of timing out and losing the user.
Cost:
Compiling knowledge once and reusing it removes the largest line item in an agent's bill, and re-curation processes only what changed rather than the whole corpus. AI spend becomes predictable and capped instead of scaling with every query, and low enough that smaller and open-weight models become viable.
Trust:
Governance lives at the data layer, enforced by construction rather than requested in a prompt. Access control is applied at retrieval. Every field carries a citation and a confidence score. PII is tagged at ingest. Each answer traces back to its source. The compiled layer runs inside your own cloud with no standing Pinecone access, on the models you choose. Agents pass a security review and deploy in regulated industries.
We Ran It On Our Own Support Queue
We put Nexus behind our own support agent on July 17th.
Metric
Without Nexus
With Nexus
Resolution rate
24.6%
55.1%
Assign rate
76.5%
94.2%
Assist rate
60.5%
87.8%
More than half of our tickets now close without a person touching them. This was made possible because Nexus holds contexts about our customer accounts, so the agent can reason across everything available to it and sort a question into three buckets: what it already knows, what it can look up, and what only the customer or another team can tell it. That third bucket is where Nexus made a significant difference to the overall performance against business metrics.
A Knowledge Layer That Stays True
Public Preview customers created 300 contexts, compiling 3.5 million source chunks into nearly 26,000 structured, queryable knowledge artifacts. The corpora that flowed through those projects: support knowledge bases, legal contracts, financial filings, research papers, meeting minutes, and call transcripts. We asked for bounded corpora where a single question draws on files across the corpus, and that is what we got.
The headline learning from those engagements: customers validate accuracy fast, usually in the first week of evaluation. The rest of the engagement goes to a different question. How do we manage this knowledge layer as a living thing? Three demands came up in almost every conversation.
Keeping knowledge current has to be effortless.
Enterprise corpora do not hold still. New tickets land daily, contracts get amended, a process doc gets revised on a Tuesday. Preview customers wanted new source data flowing into the compiled layer as it arrives, incrementally, without rebuilding from scratch. Nexus curates incrementally: new and changed sources flow into the existing knowledge layer instead of triggering a full rebuild.
The knowledge layer has to follow the business.
The right knowledge structure changes as the work changes. A revenue team reorganizes its pipeline stages. A compliance team inherits a new regulation. The questions people ask in month three are not the questions from month one. Today the SME handles this directly: update the Manifest to reflect the new requirements, re-curate, ship. That loop is fast, and it keeps the person who understands the domain in control. Every query an agent runs against the layer is also a signal about what the layer should contain, and a Manifest-driven architecture can read that signal. We are investing there.
The knowledge layer has to handle source conflicts.
The wiki says one thing, the contract says another, and one of them is three years stale. A retrieval system hands the agent both, which is how confident wrong answers get made. Curation surfaces conflicts in the compiled knowledge, where the SME can adjudicate them. A knowledge layer should know what it knows and flag what is contested.
The preview confirmed a design conviction. The durable value is a knowledge layer your experts can keep true over time, well past the first curation run. Approaches built on static, declarative context, central ontologies included, define knowledge once and let it decay. Nexus recompiles as the outcome requirements change, guided by the person with direct experience of the domain.
Start Building
If your agents are unreliable on your corpus, or token and latency costs keep climbing without the accuracy to show for it, the ceiling is the knowledge layer. That is the problem Nexus was built for, and as of today you can solve it with a standard procurement conversation.
Pinecone Nexus is generally available now. Learn more at
pinecone.io/nexus
, or
Start Your Trial
today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
