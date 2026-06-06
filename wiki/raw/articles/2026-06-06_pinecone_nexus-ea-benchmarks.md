---
title: "Nexus in the Wild: Real Results from Our Early Access Customers"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/nexus-ea-benchmarks/"
scraped: "2026-06-06T06:00:34.394868+00:00"
lastmod: "2026-06-05T17:29:19Z"
type: "sitemap"
---

# Nexus in the Wild: Real Results from Our Early Access Customers

**Source**: [https://www.pinecone.io/blog/nexus-ea-benchmarks/](https://www.pinecone.io/blog/nexus-ea-benchmarks/)

←
Blog
Nexus in the Wild: Real Results from Our Early Access Customers
We gave three enterprises a knowledge engine. Here's what happened to accuracy, latency, and costs.
Jasmeet Singh Gujral
,
Siva Ragavan
,
Anthony Mahanna
Jun 5, 2026
Product
Share:
Jump to section:
The Benchmark
Melange: Standard Essential Patent Search
M&A Due Diligence
Revenue Intelligence from Gong Transcripts
Results Across Three Customers
Apply for Early Access
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
For the past year, most enterprise AI discussions were about capability. The question that replaced it is about cost and reliability. AI is expensive to run at scale, and accuracy and latency still break down on the hardest corpora. When teams look at where their inference spend is actually going, most of it isn't on reasoning. It's on retrieval loops that run before the model can say anything.
Pinecone Nexus addresses this at the infrastructure layer. Rather than assembling knowledge at query time, it compiles structured artifacts from a corpus before any query arrives, tuning the retrieval pipeline to the specific shape of the data. We launched four weeks ago and have been engaged with early access users with real enterprise datasets. Our early enterprise partners are seeing real results. Here's what happened to their accuracy, latency, and costs after Nexus.
The Benchmark
For each customer, we ran Nexus against the most common pattern in enterprise agent deployments today: chunk the corpus, embed the chunks, use hybrid retrieval. The agent loops (run the query, rerank, read the top chunks, retrieve again) until it has enough context to answer.
That approach can produce correct answers. The question is at what cost in tokens, time, and consistency, and whether that cost holds at enterprise scale.
Three KPIs:
Token cost.
How many tokens does a single query consume? At enterprise volume, this determines whether the economics of an agentic deployment hold.
Accuracy.
Does the agent return the correct answer, repeatable across runs? Each eval set in our benchmark was built from human-labeled questions with expected answers drawn from the actual corpus. Answers were graded by an LLM judge (claude-sonnet-4-6) on a 0–1 scale against the expected output.
Latency.
How long does a query take, end to end? For agents embedded in live workflows, user-facing products, automated pipelines, or deal support, time to answer matters.
All three trace back to the same dynamic. Agentic RAG assembles knowledge at query time: retrieve chunks, rerank, read, decide what's missing, loop again. The loop runs on a generic index built once from the raw source, with no knowledge of the domain, the query types, or the reasoning the task requires. Each iteration is the agent compensating for what the index doesn't know and working around an absence, not a foundation.
Nexus works differently. Before any query arrives, it derives structured artifacts from the corpus shaped to the subject matter, the query types, and the reasoning the agent will need to do. The agent retrieves precisely and reasons immediately.
Melange: Standard Essential Patent Search
Domain: Intellectual Property / Patent Litigation
Melange Technologies
runs an autonomous, large-scale prior art search engine used by law firms in patent invalidation and litigation.Their core product is an agentic search system which filters the total corpus of around 140 million patent documents down to the most relevant dozen and provides litigators with a first draft of the legal analysis necessary to prosecute their case. The work is nearly fully autonomous with human verification only at the final stage before delivery.
Melange’s next plan of expansion involves Standard Essential Patents, or SEPs. An SEP is a patent that claims technology required to comply with an industry standard. For example, any company building a phone with 5G capability must implement portions of the 5G technical standard. If a patent covers one of those mandatory portions, then practicing the standard may necessarily practice the patent. Patent licensing has become a multi-billion dollar industry, with SEPs at the center of the most valuable and contested disputes.
This has two important implications for the industry. First, it is critical to determine whether a patent is actually essential to the standard. That analysis can be expensive and time-consuming, often requiring human domain experts to compare patent claims against long, technical standards documents line by line. Second, standards documents themselves can serve as prior art, potentially invalidating patents that claim technology already disclosed during the standards-development process.
In just release 1 of the 3GPP technical standard, there are roughly 1,800 documents including 2.3 GB of relevant documents. The pilot evaluated a focused 29-spec slice of the 5G NR standards (~31 MB, converted to markdown). These specifications originate as .docx/.doc files dense with embedded tables and normative requirement language.
Corpus:
3GPP Release 18, ~1,800 .docx/.doc files, ~2.3 GB, covering 5G NR specifications, protocol standards, interface definitions, and normative requirements. Pilot evaluated on a 29-spec NR slice (~31 MB, converted to markdown).
Eval set:
30 SEP-candidacy questions, each a patent-style claim evaluated against the standards corpus for whether a finalized, mandatory 3GPP requirement necessarily practices it. Every answer is one of five verdicts (mandatory, conditionally mandatory, optional, forbidden, or absent) with the exact spec, clause, and information element cited.
Metric
Agentic RAG
Nexus
Δ
Accuracy
52.7%
66%
25% more accurate
Latency (avg per query)
187s
44s
77% faster
Token cost (avg per query)
201k tokens
5.9k tokens
97% fewer tokens
Agentic RAG averaged ~20 retrieval steps per question on this corpus. The loop does not converge on dense, clause-referenced technical standards because the index carries no knowledge of how the standards are structured or what the query requires. Nexus organized the standards into addressable requirement artifacts before any query ran. The correct clause was retrieved directly, at 5.9K tokens versus 201K.
Business impact:
At 97% lower token cost, a previously cost-prohibitive autonomous patent search product becomes economically viable at scale. Latency under one minute per query means the workflow fits live litigation timelines. The accuracy improvement directly reduces attorney review time.
"These early results are genuinely exciting: a 34x reduction in token cost and queries resolving in under a minute on one of the hardest problems in our space tells us we're pointing in the right direction. Adding a purpose-built knowledge engine to Pinecone’s AI infrastructure is already showing signs of real business impact, and we're looking forward to evolving this together as Nexus matures to fully fit the demands of patent search at scale." — Joshua Beck, CEO, Melange
M&A Due Diligence
Domain: Financial Technology / Investment Management
The customer is a large financial technology company serving asset managers, hedge funds, and private equity firms. Their clients operate in document-heavy environments where extracting precise answers from large document sets directly affects deal outcomes and regulatory risk.
The use case evaluated here is M&A due diligence, which is a representative scenario for this customer's client base, where a deal dataroom for even a mid-market acquisition spans hundreds of documents across 10+ categories: audited financials, capitalization tables, customer contracts, IP filings, HR records, real estate leases, tax schedules, legal governance docs. Questions aren't contained within a single document. They require reasoning across all of it simultaneously.
The dataset is a full synthetic M&A dataroom for a $42M ARR enterprise SaaS company, structured across 10 category folders with files spanning PDFs, Excel workbooks, and markdown, covering the full complexity of a live deal room in a controlled, evaluable form.
The questions that matter here are inherently multi-hop. "What capital-structure feature in Vantage's preferred stock affects the equity-value waterfall to common shareholders?" requires reasoning across the cap table, preferred stock terms, and liquidation preference documents simultaneously. "What contingent legal liability could impair Vantage's projected cash flows or warrant a DCF risk discount?" requires connecting IP filings, litigation records, and financial projections across three separate folder categories. No single document holds the answer. The question only resolves when the full dataroom is treated as a unified knowledge surface.
Corpus:
90 documents across 10 category folders (PDFs, XLSX, and markdown) covering company overview, audited financials, ARR schedules, cap tables, customer contracts, IP filings, HR records, tax documents, real estate leases, and process documents.
Eval set:
30 multi-hop M&A diligence queries requiring cross-document reasoning.
Metric
Agentic RAG
Nexus
Δ
Accuracy
57%
65%
14% more accurate
Latency (avg per query)
61s
32s
48% faster
Token cost (avg per query)
66k tokens
5k tokens
92% fewer tokens
Nexus resolved each question in a single retrieval step against RAG's approximately 10 iterative steps. The accuracy improvement holds on the hardest multi-hop queries, where agentic RAG's loop repeatedly retrieves incomplete context across documents and cannot close the reasoning gap without re-querying. Nexus derived artifacts from the dataroom that mapped the cross-document relationships before any query arrived.
Business impact:
Due diligence workflows that required analyst hours to synthesize across folders now complete in seconds. At 92% lower token cost and 48% lower latency, the economics of deploying AI across deal pipelines are fundamentally different. Higher accuracy on multi-hop questions reduces the risk of missed liabilities or misread financial structures.
Revenue Intelligence from Gong Transcripts
Domain: SMS Marketing / E-commerce SaaS
The sales and CS teams for a leading SMS marketing and sales platform for e-commerce brands run a high volume of customer-facing calls every week, pricing conversations, onboarding calls, renewal discussions, competitive deal cycles, all captured in Gong.
The challenge is that insights locked in those transcripts are largely inaccessible at scale. Questions like "Which competitor is mentioned far more than any other across these calls?" or "Name several accounts where RCS is a major topic of discussion" require synthesizing patterns across dozens of calls simultaneously. Searching one transcript at a time, which is what an agentic loop does, is too slow and too expensive for a live revenue workflow. The signal is in the aggregate.
The dataset is one week of real Gong call exports: structured JSON transcripts covering sales, CS, and pricing conversations, with company-specific tracker data (message rate, list growth, churn indicators, competitor mentions, expansion signals) embedded throughout.
Corpus:
217 Gong call transcripts, ~45 MB of structured JSON call data spanning sales, pricing, and customer success conversations with full tracker and topic metadata.
Eval set:
40 revenue intelligence queries requiring cross-call synthesis, trend identification, and pattern recognition.
Metric
Agentic RAG
Nexus
Δ
Accuracy
36%
70%
94% more accurate
Latency (avg per query)
28s
23s
18% faster
Token cost (avg per query)
27K tokens
4K tokens
85% fewer tokens
The accuracy improvement here is the largest of the three cases and reflects the fundamental mismatch between agentic RAG and aggregate synthesis workloads. An agentic loop over 217 transcripts is iterating through documents one at a time, searching for partial answers, and reassembling them into a response. It cannot see across the full corpus simultaneously. Nexus derived structured representations of the call data that made cross-call patterns directly addressable. The nearly 2x accuracy gain is what corpus-level compilation looks like in practice.
Business impact:
Revenue intelligence queries that required manual analyst review become automatable. Competitive signals, churn indicators, expansion patterns, and pricing sensitivities become queryable in real time across the full call corpus. At 85% lower token cost, running these queries continuously as new calls come in becomes economically viable.
Results Across Three Customers
Three customers, three industries (financial services, intellectual property, revenue operations), three knowledge problems. Nexus outperformed agentic RAG on accuracy, latency, and token cost across all three.
Customer / Domain
Use Case
Outcome
Melange / IP & Patent Litigation
SEP claim validation against 3GPP standards
97% fewer tokens, 77% faster, 25% more accurate
FinTech / Investment Management
M&A due diligence across multi-category datarooms
92% fewer tokens, 48% faster, 14% more accurate
SMS SaaS / E-commerce
Revenue intelligence across 217 Gong transcripts
85% fewer tokens, 18% faster, 94% more accurate
The pattern held regardless of corpus shape, query type, or domain. In every deployment, agentic RAG started from the same place: a generic vector index built from the raw source, with no knowledge of the domain, the query types, or the reasoning the task requires. The retrieval loop that follows isn't incidental to that design. It's what happens when the index carries no knowledge of the domain, query types, or task structure.
Nexus gets to the root cause. The artifacts it derives from an M&A dataroom are structurally different from the ones it derives from a patent standards corpus or a Gong transcript database, because the subject matter, query types, and reasoning requirements are different. By the time a query arrives, the knowledge layer has already been shaped to the problem. The agent retrieves precisely and reasons immediately rather than sifting through generic chunks hoping to assemble enough context to answer.
The practical consequence is direct: projects that couldn't clear the business case now can. At 92–97% fewer tokens, inference costs that were prohibitive at enterprise volume become manageable. At 48–77% lower latency, agents that couldn't fit live workflows now do. At accuracy rates that hold on hard corpora, deployments that required constant human review become autonomous.
Apply for Early Access
Nexus is built for teams building agents over enterprise knowledge: documents, contracts, filings, call transcripts, technical specifications. If agentic RAG has hit its ceiling on a corpus, the issue is almost always in the retrieval loop, not the model.
Enterprises with a hard knowledge problem can
apply for Early Access
and run a benchmark on their own data before public preview. We'll work with you.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
