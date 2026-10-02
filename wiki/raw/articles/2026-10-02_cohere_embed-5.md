---
title: "Embed 5: Frontier Embedding Models for Enterprise"
source: "Cohere Blog"
url: "https://cohere.com/blog/embed-5"
scraped: "2026-10-02T06:00:12.477103+00:00"
lastmod: "2026-10-01"
type: "sitemap"
---

# Embed 5: Frontier Embedding Models for Enterprise

**Source**: [https://cohere.com/blog/embed-5](https://cohere.com/blog/embed-5)

Key takeaways
State-of-the-art enterprise retrieval:
Embed 5 Pro achieves the highest average score of any model we tested, particularly across financial datasets, parsed PDFs, and visually rich documents.
A new Fast tier:
Embed 5 Fast brings strong retrieval quality to latency, and cost-sensitive workloads, at $0.08 per million tokens.
One index, two models:
Pro and Fast share an embedding space, so teams can index with Pro and query with either model without re-indexing.
Built for complex enterprise data:
Embed 5 supports multimodal inputs and retrieval, 100+ languages, and a 128K-token context window for longer documents.
More efficient at scale:
Matryoshka representations and lower-precision outputs reduce vector storage and search costs, while quantized weights lower serving requirements for private deployments.
Today, we're releasing Embed 5, a new family of embeddings models at the frontier of high-quality enterprise retrieval.
Embed 5 delivers stronger retrieval across complex enterprise data while giving teams more control over latency, cost, and deployment.
Embed 5 Pro
is optimized for maximum quality across multimodal, multilingual, financial, code, and parsed-document retrieval.
Embed 5 Fast
brings highly competitive performance to latency- and cost-sensitive workloads. Both tiers share a single embedding space, so teams can index with Pro and query with either model without rebuilding the index.
Embed 5 establishes the retrieval foundation for search, RAG, and agentic workflows, surfacing more relevant context while filtering out noise before it reaches expensive generative models. Use Embed to improve answer quality and user experience while helping keep downstream inference costs under control.
Embed 5 is generally available today on the
Cohere API and Model Vault
,
Microsoft Foundry
, and
Amazon SageMaker
. Pricing is $0.12 per million tokens for Pro and $0.08 per million tokens for Fast.
Snapshot
Capability
Embed 5 Pro
Embed 5 Fast
Best for
Maximum retrieval quality; offline indexing; complex enterprise corpora
Interactive search; high-volume RAG; agentic retrieval
Context length
128K tokens
128K tokens
Inputs
Text, images, fused text + image
Text, images, fused text + image
Languages
100+
100+
Output dimensions
2048, 1536, 1024, 768, 512, 256
2048, 1536, 1024, 768, 512, 256
Embedding formats
float, int8, binary
float, int8, binary
Matryoshka embeddings
Yes
Yes
Shared embedding space
Yes
Yes
Supports self-hosting
Yes
Yes
Pricing
$0.12 / 1M tokens (text)
$0.40 / 1M tokens (image)
$0.08 / 1M tokens (text)
$0.40 / 1M tokens (image)
Performance
Embed 5 Pro delivers our strongest retrieval performance to date. It achieves the highest average score of any model we tested across ViDoRe V3, financial documents, parsed PDFs, image retrieval, and across key business languages.
Embed 5 is also the first model family evaluated with
RCP-nDCG@10
, our latest retrieval methodology. Instead of scoring only against a limited set of fixed labels, it evaluates retrieved documents against query-specific relevance criteria, capturing relevant results and giving a fuller view of performance on your own corpus.
1
Read more about RCP-nDCG@10
.
Enterprise documents
Embed 5 excels with visually rich documents where meaning lives in tables, charts, diagrams, and layout — not just text. On
ViDoRe V3
, which features documents sampled across key enterprise domains, including financial filings, technical manuals, regulatory material, government reports, textbooks, and lectures, Embed 5 Pro averages 85.8 — an impressive 8.8 gain from Embed 4.
2
That puts it ahead of Voyage 4 Large (83.7), Gemini Embedding 2 (83.2), and OpenAI text-embedding-3-large (75.5). Pro leads five of the eight domains outright and ties Voyage 4 Large on energy, with its largest gains over Embed 4 on HR (+11.4) and industrial (+10.3). Embed 5 Fast averages 84.5, ahead of both Gemini Embedding 2 and Voyage 4 Large. See the full results
here
.
Retrieval quality (RCP-nDCG@10) across eight visually rich document domains. Evaluations consisted of parsed text outputs, curated by the authors of ViDoRe.
Finance
Embed 5 Pro establishes itself as the leading embeddings model for financial document retrieval.
Pro ranks first on three leading public financial benchmarks, with Fast second on each despite being considerably smaller than its peers:
FinanceBench
(80.1 Pro, 80.0 Fast),
FinQA
(90.0, 88.8), and ViDoRe V3 Finance (85.0, 83.9).
Across these, Pro averages 3.3 points higher than the next non-Cohere competitor, Gemini Embedding 2. Compared with OpenAI text-embedding-3-large, the lead grows to 21.4 points on FinanceBench.
Retrieval quality (RCP-nDCG@10) across eight visually rich document domains. Evaluations consisted of parsed text outputs, curated by the authors of ViDoRe.
Multimodal
Parsed PDFs
Most enterprise search pipelines still convert PDFs to text before embedding them, but that process can strip away structure. Tables lose row and column relationships, multi-column layouts can scramble reading order, repeated headers add noise, and charts often disappear entirely. That makes parsed-document retrieval a harder test than clean-text benchmarks suggest.
Our parsed-document suite spans service documentation, corporate reports, SEC filings, product manuals, and privacy policies. Embed 5 Pro achieves the highest average across the suite at 84.8, ahead of Voyage 4 Large at 83.6, Embed 5 Fast at 83.4, Gemini Embedding 2 at 80.8, and Embed 4 at 78.6. The figure below highlights a subset of familiar public benchmarks, with Embed 5 Pro especially strong on financial documents represented by FinanceBench and CoFiF.
Parsed-document retrieval (RCP-nDCG@10) across representative public benchmarks. Documents were parsed using Gemini 1.5 Flash. “Full suite average” includes additional datasets not shown.
Page-image and fused text-image documents
Some documents are better represented visually. Scanned pages, slide decks, schematics, and charts contain information that text extraction may miss. Embed 5 can embed page images directly (page-image), or combine an image with its metadata into a single vector (fused text-image).
On fused text-image corpora, Embed 5 Pro averages 82.3 across five datasets, ahead of Embed 5 Fast at 81.2 and Gemini Embedding 2 at 61.3. Pro outperforms Gemini Embedding 2 on every dataset in the suite. Page image retrieval is also robust: Embed 5 Pro continues to lead on financial datasets, averaging 77.0 from five datasets, ahead of Embed 5 Fast (73.2), Embed 4 (71.1), Voyage Multimodal 3.5 (70.1), and Gemini Embedding 2 (56.7).
Multimodal document retrieval (nDCG@10) with text queries. Fused text-image retrieval combines the page image and document metadata in a single embedding. RepairBench reports the average across multiple multilingual query subsets. High Finance is an internal, Cohere-annotated set of questions that ask models to retrieve the relevant investment banking and hedge fund presentation material.
Multimodal document retrieval (nDCG@10) with text queries. Image-only retrieval uses the page image alone to answer a prompt. AR = Arabic; JA = Japanese; KO = Korean.
Multilingual
Embed 5 is trained on more than 100 languages, with particular focus on the languages most used by our global customer base.
Across German, French, Spanish, Italian, and Russian, Embed 5 Pro achieves the highest average of the models we tested: 77, compared with 76 for Voyage 4 Large, and 73 for Gemini Embedding 2. It improves on Embed 4 by around 7 points on average, with the largest gains in Russian (+9) and Italian (+7).
Retrieval quality across key European languages. Scores represent an average across a number of composite benchmarks. Benchmarks were measured in either nDCG@10 or RCP-nDCG@10.
The table below covers ten further languages where Embed 5 has made important strides against Embed 4. Pro’s largest gains are in middle eastern and subcontinent languages, notably Farsi (+13), Telugu (+12), and Hindi (+12). For the full list of multilingual evaluation results,
click here
.
Language
Cohere Embed 5 Pro
Cohere Embed 5 Fast
Gemini Embedding 2
Voyage 4 Large
Cohere Embed 4
Jina Embeddings v5 Text Small
OpenAI text-embedding-3-large
Japanese
87
85
90
87
83
83
80
Chinese
82
80
81
82
79
78
73
Korean
85
83
87
85
79
79
70
Arabic
83
79
87
86
72
71
67
Farsi
81
78
83
79
68
70
60
Hindi
80
77
84
83
68
73
59
Bengali
83
81
89
85
73
79
61
Telugu
80
76
91
89
68
82
63
Indonesian
85
83
88
85
79
79
81
Thai
82
75
88
84
75
78
67
Meet Embed 5 Fast
Embed 5 Fast is a lighter weight model built for latency-sensitive, high-volume retrieval. It costs a third less than Pro while retaining the same 128K-token context, multimodal inputs, multilingual coverage, and multiple compressed output formats.
That matters most on the query path, where embedding latency is paid on every search — and multiplied in agentic workflows that may issue dozens of searches per task. Fast’s smaller footprint also lowers serving costs in private deployments and speeds large ingestion and re-indexing jobs.
For document throughput — a closer proxy for indexing efficiency — Fast is consistently more efficient, delivering an average of 2.4× higher throughput than Pro across context sizes.
Average document throughput for Fast and Pro across ~200-token and ~1K-token context lengths, measured in documents processed per second. Higher is better.
Performance
Fast raises the bar for compact embedding models. On ViDoRe V3, it leads Voyage 4 Nano by almost seven points and Jina Embeddings v5 Text Small, Perplexity, and Microsoft’s Harrier 0.6B by ten or more. It outperforms Qwen3-VL-Embedding-2B, despite being roughly half the size, by about 20 points. As seen above, its average also exceeds Gemini Embedding 2 and Voyage 4 Large on ViDoRe V3 and on financial retrieval. On parsed PDFs it exceeds Gemini Embedding 2 (83.4 vs 80.8) and trails Voyage 4 Large (83.6).
Retrieval quality (RCP-nDCG@10) across eight visually rich document domains. Evaluations consisted of parsed text outputs, curated by the authors of ViDoRe.
Pro
Fast
Use when…
Use for offline indexing and quality-critical retrieval — especially across complex documents,
                    multimodal content, or nuanced queries.
Use on the live request path, especially for interactive search, agent loops, and other
                    high-volume query workloads.
Financial Services
Bulk indexing of 10-Ks, earnings reports, tables, and footnotes for equity research; compliance
                    or risk search over dense financial records.
Customer-service search, advisor copilots, transaction-support workflows, and agents issuing
                    repeated retrieval calls.
Retail + Commerce
Product discovery across large multimodal catalogs, including nuanced attribute matching and
                    image-plus-text retrieval.
Site search, shopping assistants, recommendations, and conversational product lookup serving
                    large numbers of live queries.
Legal
Digitizing large legal archives, including contract histories, case files, regulatory materials,
                    and internal precedent libraries.
Internal legal knowledge search, clause lookup, matter search, and repeated retrieval within legal
                    assistants or workflows.
Two models, one embedding space
Pro and Fast share a single embedding space, so vectors from either model can be compared directly. We tested every corpus/query pairing across 40 development datasets spanning text, image, fused, and parsed-document retrieval.
That shared space lets teams choose each tier independently: documents can be indexed with Pro for maximum quality, while queries use Fast for lower latency and cost — without rebuilding the index. The cross-model combinations remain close to the same-model baselines (averaging just 1.6% and 2.7% losses for Fast and Pro queries, respectively), with no dataset showing a major failure.
For many customers, we recommend the following deployment pattern:
index with Pro, query with Fast.
It captures much of the quality gain of an all-Pro system while keeping Fast’s latency and cost during request.
3
Mean retrieval quality
Corpus: Fast
Corpus: Pro
Query: Fast
96.6
98.4
Query: Pro
97.3
100
Cross-model retrieval. Mean nDCG@10 across 40 development datasets, normalized to Pro corpus + Pro query = 100.
Vector storage
At enterprise scale, the vector index can cost more to operate than the model that generates it. Embed 5 supports Matryoshka representation learning and lower-precision outputs, letting teams shrink vectors and finely control the tradeoff between quality, storage, and search cost. These savings can be substantial: a 2,048-dimensional float32 vector requires 8 KB; a 1,024-dimensional int8 vector uses 1 KB; and a 256-dimensional binary vector just 32 bytes — a 256x reduction. Across 100 million chunks, that cuts raw vector storage from roughly 819 GB to 3.2 GB.
Importantly, int8 retains near-full-precision retrieval quality in both Embed 5 Pro and Fast. For most deployments, we recommend 1,024-dimensional int8 vectors as the ideal performance-efficiency point. Binary offers the smallest footprint, with some accuracy tradeoff, and is well suited to fast first-pass retrieval before higher-precision reranking.
Retrieval quality (RCP-nDCG@10) against storage cost at different vector dimensions and precisions. Storage cost is given relative to a 2048-dimension FP32 vector. Farther left is more efficient. Retrieval was evaluated using ViDoRe V3 (eight datasets).
Getting started
Deploy Embed 5 Pro and Embed 5 Fast through the Cohere API, Model Vault, Microsoft Foundry (
Pro
,
Fast
), and Amazon SageMaker (
Pro
,
Fast
), or use Embed 5 directly within
North
. For private deployments in your own VPC or on-premises, both models can be served with vLLM.
Batch embedding is available
for large-scale ingestion.
Build with the tools you already use.
Embed 5 fits into existing retrieval stacks, with integrations across frameworks and vector databases, including LangChain, Haystack, Weaviate, Qdrant, Pinecone, Elasticsearch, MongoDB, Redis, Milvus, and OpenSearch.
Read the documentation
.
Start by
creating an API key
, then use the code snippets below to quickly make your first query.
import
os, cohere, numpy
as
np
co = cohere.ClientV2(api_key=os.environ[
"CO_API_KEY"
])
documents = [
"Net interest margin narrowed 12 bps to 2.61% as deposit costs rose."
,
"Torque the mounting bolts to 45 Nm in a star pattern before refitting the cover."
,
"Employees accrue 1.5 days of paid leave for each month of service."
,
]
doc_embeddings = co.embed(
model=
"embed-v5.0-pro"
,
input_type=
"search_document"
,
texts=documents,
output_dimension=
1024
,
embedding_types=[
"float"
],
).embeddings.float_
query_embedding = co.embed(
model=
"embed-v5.0-pro"
,
input_type=
"search_query"
,
texts=[
"What happened to net interest margin last quarter?"
],
output_dimension=
1024
,
embedding_types=[
"float"
],
).embeddings.float_[
0
]
docs = np.array(doc_embeddings)
query = np.array(query_embedding)
scores = docs @ query / (
np.linalg.norm(docs, axis=
1
) * np.linalg.norm(query)
)
print
(documents[
int
(np.argmax(scores))])
What else
Meet the team behind Embed 5.
Join us on X on
October 8, 2026
to hear from our search and embeddings leadership about Embed 5, Parse 5, and what else we’ve been preparing behind the scenes.
Also,
Compass Cloud
, our managed search and retrieval platform, is now in private beta.
Request access
to try it on your own retrieval and agentic workloads.
Key contributors
Samarth Bhargav, Fabian Schmidt, Clifton Poth, Arthur Maciejewicz, Florian Schneider, David Rau, Dennis Zhao, Timothy Ang, Nils Reimers, Carlos Lassance
Footnotes
1
RCP-nDCG@10 requires evaluating embedding models in a two-stage retrieval setup, using their similarity scores to reorder a fixed candidate set. Scores therefore reflect reranking quality rather than first-stage retrieval performance, which we thoroughly evaluate elsewhere against nDCG and Recall.
2
The annotations and code needed to evaluate Vidore V3 with RCP-nDCG are available on
GitHub
.
3
Both sides must use the same output dimension. Compatibility also holds with Matryoshka truncation and int8 quantization, so the same pattern works with compressed indexes.
Blog
Written By
Cohere Team
Tags
Product Launch
Company News
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
