---
title: "Cohere retrieval models on OpenRouter"
source: "Cohere Blog"
url: "https://cohere.com/blog/embed-rerank-5-openrouter"
scraped: "2026-11-11T06:00:36.328169+00:00"
lastmod: "2026-11-04"
type: "sitemap"
---

# Cohere retrieval models on OpenRouter

**Source**: [https://cohere.com/blog/embed-rerank-5-openrouter](https://cohere.com/blog/embed-rerank-5-openrouter)

Embed 5
and
Rerank 5
are now live on OpenRouter. Here’s how to turn them into a working RAG pipeline in a few dozen lines of Python code through a
single API
.
There are Cohere’s most powerful retrieval models yet, delivering leading performance on enterprise documents and complex retrieval tasks. If you’re already using OpenRouter, you can get started immediately - using the same API key and credits as your existing models, with no additional setup.
RAG grounds an LLM's answer in your own data by fetching relevant chunks before it writes. Embedding search provides a fast and effective first-stage approximation. A reranker then reads the query and each candidate together, adding precision to what’s been retrieved.
Two features of the Cohere models shape this design:
Embed 5 Pro and Fast share one embedding space.
Index with
embed-5-pro
for quality, then query with
embed-5-fast
for latency.
Rerank 5 scores are calibrated.
A score means the same thing across queries and domains, so one relevance threshold can filter out weak context before it reaches the LLM.
By the end you'll have a short Python script that answers questions over your docs with scored citations. This same approach can be applied to virtually any retrieval use case, from enterprise search and customer support to knowledge management and document discovery.
A RAG pipeline has two halves: an offline job that builds a searchable index, and an online path that runs for every question. Knowing which calls happen once and which happen per request help explain most of the pipeline's cost and latency. Indexing runs once per corpus. Each question then costs one Embed 5 Fast call, one Rerank 5 call and one chat call, all through OpenRouter's API.
Setup
You’ll need Python 3.10 or newer, an
OpenRouter API key
, the
OpenRouter Python SDK
, and NumPy for an in-memory vector store.
pip install openrouter numpy
export
OPENROUTER_API_KEY=
"sk-or-..."
import
os
import
numpy
as
np
from
openrouter
import
OpenRouter
client = OpenRouter(api_key=os.environ[
"OPENROUTER_API_KEY"
])
EMBED_INDEX_MODEL =
"cohere/embed-5-pro"
# indexing: highest quality
EMBED_QUERY_MODEL =
"cohere/embed-5-fast"
# queries: lowest latency
RERANK_MODEL      =
"cohere/rerank-5-pro"
# or cohere/rerank-5-fast
CHAT_MODEL        =
"deepseek/deepseek-v4.1-flash-1017"
# any chat model on OpenRouter
DIMS =
1024
# 256 | 512 | 768 | 1024 | 1536 | 2048
Embed 5 returns Matryoshka vectors at six sizes, 2048 by default. We
suggest
1,024-dim int8 vectors as the best quality-to-cost point; OpenRouter's
embeddings API
returns floats, so this post uses 1,024-dim floats.
The NumPy store keeps this demo simple. For production, replace it with your preferred vector database, such as pgvector, Qdrant, Pinecone, or Weaviate.
Indexing
Indexing turns each chunk of text into a vector, a list of numbers where similar meanings sit close together. It runs once per corpus, so it's the step where the highest-quality model pays off.
Split each document into chunks, embed them with Embed 5 Pro as
search_document
, and normalize the vectors so a dot product equals cosine similarity.
The sample corpus is a fictional API's docs, with a few near-misses on purpose:
docs = [
{
"title"
:
"Rotating API keys"
,
"text"
:
"To rotate a key without downtime, create a second key, deploy it to every service, "
"confirm traffic on the new key in the usage dashboard, then revoke the old key."
},
{
"title"
:
"Creating API keys"
,
"text"
:
"Create keys under Settings > API Keys. Each key can be scoped to read or write and to one project."
},
{
"title"
:
"Revoking API keys"
,
"text"
:
"Revoking a key takes effect immediately. Requests with a revoked key return 401 Unauthorized."
},
{
"title"
:
"Webhook signing secrets"
,
"text"
:
"Rotate your webhook signing secret from the Webhooks page. The old secret stays valid "
"for 24 hours so you can update your verifier."
},
{
"title"
:
"Log rotation"
,
"text"
:
"Request logs rotate daily and are kept for 30 days. Export them to S3 for longer retention."
},
{
"title"
:
"Rate limits"
,
"text"
:
"Each API key is limited to 600 requests per minute. Going over returns 429 Too Many Requests."
},
]
def
chunk
(
doc, max_chars=
1500
):
"""Split on blank lines, packing paragraphs up to ~max_chars."""
out, buf = [],
""
for
para
in
doc[
"text"
].split(
"\n\n"
):
if
buf
and
len
(buf) +
len
(para) > max_chars:
out.append({
"title"
: doc[
"title"
],
"text"
: buf.strip()})
buf =
""
buf += para +
"\n\n"
if
buf.strip():
out.append({
"title"
: doc[
"title"
],
"text"
: buf.strip()})
return
out
def
embed
(
texts, model, input_type, batch=
96
):
vecs = []
for
i
in
range
(
0
,
len
(texts), batch):
res = client.embeddings.generate(
model=model,
input
=texts[i:i + batch],
# one request per batch
input_type=input_type,
# "search_document" | "search_query"
dimensions=DIMS,
)
vecs += [d.embedding
for
d
in
res.data]
v = np.array(vecs, dtype=np.float32)
return
v / np.linalg.norm(v, axis=
1
, keepdims=
True
)
chunks = [c
for
d
in
docs
for
c
in
chunk(d)]
doc_vecs = embed([c[
"text"
]
for
c
in
chunks], EMBED_INDEX_MODEL,
"search_document"
)
Three key details to point out:
input_type
:
tells Embed 5 which side of the search a text is on. OpenRouter passes it through to Cohere.
Batching:
sends many chunks per request, which cuts round trips and speeds up indexing. It doesn't change the cost, since embeddings are priced per token.
Chunk size:
packing whole paragraphs follows the by-paragraph strategy in
OpenRouter's guide
, and 1,500 characters is roughly 300–400 tokens of English. Embed 5 accepts up to 128k tokens, but every chunk also goes through Rerank 5, which reads up to 32k tokens of query and chunk combined and splits anything longer into several passes.
Retrieval
Retrieval finds the chunks whose vectors sit closest to the question's vector. This acts as a representation of semantic similarity between the two pieces of content.
Embed the question with Embed 5 Fast as
search_query
, then pull a wide candidate set of 20 chunks by cosine similarity.
def
retrieve
(
query, k=
20
):
q = embed([query], EMBED_QUERY_MODEL,
"search_query"
)[
0
]
scores = doc_vecs @ q
# cosine, since both sides are normalized
top = np.argsort(-scores)[:k]
return
[(chunks[i],
float
(scores[i]))
for
i
in
top]
Querying a Pro-built index with Fast works because the two models
share an embedding space
, as long as both sides use the same
dimensions
. It's the split we recommend: in
Cohere's tests
across 40 datasets, Fast queries on a Pro index kept 98.4% of all-Pro retrieval quality, against 96.6% for Fast on both sides. With any other model family, you’d have to use the same model on both sides.
Let’s cast a wide net at this stage: recall is the retriever's job, precision is Rerank’s. OpenRouter's guide suggests 10–20 candidates feeding a top 3–5 rerank.
Reranking
Reranking re-scores the shortlist by reading the question and each chunk together. That's too slow to run over a whole index but more accurate than vector similarity, so it runs only on the top candidates. Rerank doesn’t require Embed - or any embedding model. It works as a simple second stage with your existing semantic, keyword, or hybrid search system.
Send the query and the 20 candidates to Rerank 5, keep the top 5, and drop anything under a relevance threshold.
MIN_SCORE =
0.3
def
rerank
(
query, candidates, top_n=
5
):
res = client.rerank.rerank(
model=RERANK_MODEL,
query=query,
documents=[c[
"text"
]
for
c, _
in
candidates],
top_n=top_n,
)
return
[
(candidates[r.index][
0
], r.relevance_score)
for
r
in
res.results
# sorted by relevance, highest first
if
r.relevance_score >= MIN_SCORE
]
Each result carries the candidate's position in your list (
index
) and a
relevance_score
, per the
rerank response schema
.
What
Rerank 5
adds at this step:
Calibrated scores.
Scores stay consistent across queries and domains, so a single
MIN_SCORE
decides what reaches the LLM.
32k-token context.
Long chunks are scored whole.
Semi-structured data.
JSON records and tables rerank well when formatted as YAML strings.
No re-indexing to upgrade.
Rerank reads raw text at query time, so switching models is a one-line change.
Use
rerank-5-pro
for reasoning-heavy queries and long or domain-specific documents. Use
rerank-5-fast
for high-volume search and agents that search many times per task. One thing to note:
Rerank 5
is text-only, but will work for parsed pdfs.
Generation
Generation hands the best chunks to an LLM as numbered sources and asks it to answer from those alone. That keeps answers grounded in your docs and gives readers citations they can check. If nothing clears the threshold, skip the LLM call entirely.
SYSTEM = (
"Answer using only the numbered sources. "
"Cite them inline like [1]. "
"If the sources don't contain the answer, say you don't know."
)
def
answer
(
query
):
hits = rerank(query, retrieve(query))
if
not
hits:
return
"I couldn't find that in the docs."
sources =
"\n\n"
.join(
f"[
{i}
]
{c[
'title'
]}
\n
{c[
'text'
]}
"
for
i, (c, _)
in
enumerate
(hits,
1
)
)
res = client.chat.send(
model=CHAT_MODEL,
messages=[
{
"role"
:
"system"
,
"content"
: SYSTEM},
{
"role"
:
"user"
,
"content"
:
f"Sources:\n\n
{sources}
\n\nQuestion:
{query}
"
},
],
)
return
res.choices[
0
].message.content
print
(answer(
"How do I rotate an API key without downtime?"
))
Sending each chunk's title with its text lets the model cite something readable; add URLs too if your docs have them. OpenRouter's guide uses the Responses API for this step instead. To follow it, call
client.responses.send
with the system prompt as
instructions
and the sources and question as
input
, then read the answer from the message item in
res.output
rather than from
choices
.
Results
Here we’ll validate whether the steps we implemented improved our responses.
Reranking earns its extra call when it confidently picks the right chunk and drops near-misses that embedding search ranks just below it.
q =
"How do I rotate an API key without downtime?"
cands = retrieve(q)
hits = rerank(q, cands)
print
(
"Embedding only (top 3):"
)
for
c, s
in
cands[:
3
]:
print
(
f"
{s:
.3
f}
{c[
'title'
]}
"
)
print
(
"After Rerank 5:"
)
for
c, s
in
hits:
print
(
f"
{s:
.3
f}
{c[
'title'
]}
"
)
Rank
Embed 5 only
Embed 5 + Rerank 5
1
Rotating API keys · 0.522
Rotating API keys · 0.808
2
Webhook signing secrets · 0.337
below 0.3 cutoff
3
Creating API keys · 0.316
below 0.3 cutoff
Wrap-up
Everything in this pipeline ran through one API key and one client. Embed 5 Pro built the index, Embed 5 Fast and Rerank 5 handled each question, and a chat model wrote the answer, with no separate SDKs, accounts or bills to juggle.
That single surface is also what makes the pipeline easy to evolve. Every model is just a string, so trying
rerank-5-fast
instead of
rerank-5-pro
, or a different chat model, is a one-line change.
Start with the sample corpus, swap in your own docs, and see what Rerank 5 moves to the top.
Where to take it next:
Hybrid search.
Add keyword (BM25) hits beside the vector hits. Rerank reads raw text, so it scores both lists in one call.
A smaller index.
Drop to 512 or 256 dimensions, or use int8 or binary vectors through Cohere's own API.
Images and PDFs.
Embed 5 embeds images and mixed text-and-image inputs such as PDF pages, and OpenRouter's embeddings API accepts
image_url
content parts. Rerank 5 is text-only, so rerank those results on their text, such as parsed page text or captions, or skip reranking for them.
Evaluation.
Label a small set of real queries, compare hit rate at 5 with and without rerank, and tune
MIN_SCORE
on the same set.
Explore
Compass
. Cohere’s enterprise search and retrieval platform brings Embed and Rerank together in a single solution, making it easier to build powerful search and AI applications across enterprise data. Now available to
cloud customers
.
Useful links
OpenRouter embeddings API
OpenRouter Python SDK rerank
Embed 5 announcement blog
Rerank 5 announcement blog
Embed 5 benchmark results
Rerank 5 benchmark results
Blog
Written By
Cohere Team
Tags
AI for Developers
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
