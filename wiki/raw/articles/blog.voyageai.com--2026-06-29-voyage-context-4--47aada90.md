---
title: "voyage-context-4: stop worrying about chunking with our best-performing model"
url: "https://blog.voyageai.com/2026/06/29/voyage-context-4/"
fetched_at: 2026-06-30T07:01:00.754862+00:00
source: "Voyage AI Blog"
tags: [blog, raw]
---

# voyage-context-4: stop worrying about chunking with our best-performing model

Source: https://blog.voyageai.com/2026/06/29/voyage-context-4/

TL;DR –
voyage-context-4
is our next-generation contextualized chunk embedding model – it produces chunk embeddings that capture the full document context without any manual metadata or context augmentation, so you can stop thinking about chunking. A new mixture-of-experts (MoE) backbone delivers better context-aware embeddings, while built-in auto-chunking, transparent handling of documents longer than 32K tokens, and native support for overlapping chunks together remove chunking as a design concern. Averaged across 39 datasets spanning 8 domains
voyage-context-4
outperforms
voyage-context-3
by 1.4% and 2.08% on document-level and chunk-level retrieval, respectively, and surpasses
voyage-4-large
, our best general-purpose embedding model, by 0.4% on single-embedding evaluation. It’s a drop-in replacement for
voyage-context-3
and is priced at $0.12 per 1M tokens versus $0.18 per 1M tokens for
voyage-context-3
.
We’re excited to introduce
voyage-context-4,
the next generation of our contextualized chunk embedding model, where each chunk embedding encodes not only the chunk’s own content but also the contextual information from the full document.
voyage-context-4
improves retrieval quality in nearly every domain while adding auto-chunking and transparent handling of documents of any length – together, these remove the need to engineer a chunking strategy at all.
Contextualized chunk embeddings, recapped
In all modern AI applications, documents are typically split into chunks before embedding. Standard embedding models encode each chunk independently, discarding the surrounding document context – for example, a clause deep in a contract is embedded without the definitions it depends on. A contextualized chunk embedding model addresses this by processing the full document in a single forward pass, producing one vector per chunk that captures both local content as well as global document context.
Compared with embedding chunks in isolation, contextualized chunk embeddings deliver higher retrieval accuracy. They also avoid the latency and cost of LLM-based context augmentation – e.g.,
Anthropic’s contextual retrieval
, which prepends an LLM-generated summary to every chunk before embedding – and they handle long documents more gracefully. For a deeper dive into the motivation and architecture, see the
voyage-context-3
blog post.
In addition to model improvements, auto-chunking and splitting beyond 32K tokens are also capabilities that we have newly introduced. Here’s a full list of what’s new with
voyage-context-4
:
Better context-aware embeddings.
A new mixture-of-experts (MoE) backbone improves retrieval quality across domains while keeping serving costs low.
Built-in auto-chunking.
Send an entire document and the model chunks it for you – no separate chunking pipeline required.
No context window limit.
Documents longer than 32K tokens are split and embedded transparently, so document length is effectively no longer a constraint.
Native support for overlapping chunks
. This is especially useful for pre-existing embedding pipelines that overlap chunks to mitigate boundary effects.
Evaluation Details
Chunk-level and document-level retrieval.
For a given query, chunk-level retrieval returns the most relevant chunks, while document-level retrieval returns the documents containing those chunks. We evaluate both.
Single-embedding and chunk-embedding evaluation.
Because
voyage-context-4
also functions as a standard embedding model, we report two evaluation modes:
single embedding
, where each model produces one vector per query/document and is used like an ordinary embedding model, and
chunk embedding
, the full contextualized pipeline, where each document is embedded as a sequence of context-aware chunk vectors.
Datasets.
We evaluate on 39 retrieval datasets spanning 8 domains: technical documentation, web, code, medical, conversation, law, finance, and long-context (LongEmbed). Full per-dataset results are available in
this spreadsheet
.
Models.
For single embedding evaluation, we compare against
voyage-context-3
,
voyage-4-large
,
voyage-3-large
, Cohere Embed v4, and OpenAI v3 large. For chunk embedding evaluation, we compare against
voyage-context-3
; for head-to-head comparisons of contextualized chunk embeddings against alternatives such as Jina-v3 late chunking and Anthropic contextual retrieval, see the
voyage-context-3
blog post
.
Metrics.
We report NDCG@10, a standard metric for retrieval quality.
Results
Chunk-embedding evaluation.
On chunk-level retrieval with the full contextualized pipeline,
voyage-context-4
outperforms
voyage-context-3
by 2.08% on average. On document-level retrieval,
voyage-context-4
outperforms
voyage-context-3
by 1.4% on average.
In prior evaluations,
voyage-context-3
outperformed
Jina-v3 late chunking and Anthropic contextual retrieval by 23.66% and 6.76% on chunk-level retrieval, respectively;
voyage-context-4
‘s improvements over
voyage-context-3
extend those margins further.
The benefit of contextualization is most pronounced on long documents: on LongEmbed, embedding documents with contextualized chunk embeddings outperforms embedding the same documents as single vectors by 7.11%. Combined with the removal of the 32K context limit, this makes
voyage-context-4
better suited for long contracts, transcripts, and technical manuals, with no tradeoff between fitting a document into the context window and preserving its context.
Matryoshka embeddings and storage costs.
voyage-context-4
supports 2048, 1024, 512, and 256-dimensional embeddings through Matryoshka learning, so you can select the quality-storage tradeoff that fits your application.
Single embedding evaluation.
Used as a standard embedding model – i.e. one vector per document –
voyage-context-4
achieves state-of-the-art retrieval quality, outperforming
voyage-4-large
,
voyage-context-3
,
voyage-3-large
, Cohere Embed v4, and OpenAI v3 large by 0.45%, 3.02%, 3.29%, 10.73%, and 28.80% when averaged across eight domains, respectively. In other words, context capabilities no longer come with a single-embedding accuracy penalty: contextualization capabilities aside,
voyage-context-4
is our strongest embedding model to date.
Average single-embedding retrieval quality (NDCG@10) across the 8 evaluation domains.
voyage-context-4
leads in five of the eight domains – web, medical, conversation, law, and long-context – and stays within 0.4 NDCG points of
voyage-4-large
in the remaining three (tech, code, finance). The largest single-embedding gains over
voyage-context-3
come in web, medical, finance, and code:
Code Example
voyage-context-4
is a drop-in replacement for
voyage-context-3
. To let the model handle chunking, pass the full document and enable auto-chunking:
If you already run your own chunker, pass a list of chunks instead of the raw document and set
enable_auto_chunking
to
False
. This will return a single context-aware vector per chunk, exactly as before.
import
voyageai
vo = voyageai.Client()  # reads VOYAGE_API_KEY
from
the environment
document
=
“The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.”
result
=
vo.
contextualized_embed
(
inputs
=
[document], 		# one document; the model splits it into chunks
model
=
"voyage-context-4"
,
input_type
=
"document"
,
enable_auto_chunking
=
True,  # let voyage
-
context
-
4
chunk the document
chunk_size
=
512
, 	          # target chunk size
in
tokens
(optional)
chunk_overlap
=
64
,       # overlap between adjacent
chunks
(optional)
output_dimension
=
1024
,  # Matryoshka dim:
2048
|
1024
|
512
|
256
)
# One contextualized embedding
per
(auto
-
)chunk
chunk_embeddings
=
result.results[
0
].embeddings
Try voyage-context-4 today!
voyage-context-4
is available today via the
Voyage API
, and to MongoDB Atlas customers through the
Atlas Embedding and Reranking API.
The first 200 million tokens are free.
Get started with this
quickstart tutorial
.
Follow us on
Twitter
and
LinkedIn
to keep up with our latest releases.
