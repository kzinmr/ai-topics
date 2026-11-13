---
title: "Pinecone integrated embedding now supports Google's Gemini Embedding 2"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/integrated-embedding-google/"
scraped: "2026-11-13T06:00:30.370764+00:00"
lastmod: "2026-11-12T16:00:01Z"
type: "sitemap"
---

# Pinecone integrated embedding now supports Google's Gemini Embedding 2

**Source**: [https://www.pinecone.io/blog/integrated-embedding-google/](https://www.pinecone.io/blog/integrated-embedding-google/)

←
Blog
Pinecone integrated embedding now supports Google's Gemini Embedding 2
Gavin Johnson
,
Manish Talreja
Nov 12, 2026
Product
Share:
Jump to section:
Let Pinecone make the embedding calls
How to use Gemini Embedding 2 in Pinecone
Availability and limits
Get started
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Pinecone
integrated embedding
on the
Documents API
now supports Google's Gemini Embedding 2, alongside the Pinecone-hosted models it launched with. Gemini Embedding 2 is
Google's newest Gemini embedding model
. Teams can now run semantic search on it without building and maintaining an embedding pipeline.
Set Gemini Embedding 2 on a text field in a Documents API index and send plain text. Pinecone embeds every write and every query for that field with that model. There's no Google Cloud account or key to manage, and the tokens appear on your Pinecone invoice at Google's list price.
Through December 31, 2026, the Builder plan gets twice its included tokens for Gemini Embedding 2: 20M a month.
Let Pinecone make the embedding calls
Using a Google embedding model means calling Google's API on every write and every query. Development teams manage the Google Cloud account, API key, and rate limits, and pay Google separately from Pinecone. Integrated embedding moves that work into Pinecone:
Send plain text instead of calling an embedding provider first. Pinecone embeds the query and runs the search in one call.
Pinecone writes each document's text and its embedding together, so full-text and semantic search always see the same version of each document.
Pinecone serves Gemini Embedding 2 from Google Vertex AI, and retries failed calls, so teams don't have to build their own retry logic.
There's no Google API key to manage, and no separate bill for embedding. Tokens are billed on the Pinecone invoice at Google's list price.
How to use Gemini Embedding 2 in Pinecone
Set the model in the
embed
setting of a text field when creating a Documents API index. The Python example below embeds the
body
field with
gemini-embedding-2
at 1,536 dimensions and turns on full-text search for
body
, so the same field serves semantic and keyword search.
Note:
Gemini Embedding 2 needs a Builder plan or above.
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

pc.indexes.create(
    name="support-articles",
    schema={
        "fields": {
            "body": {
                "type": "string",
                "full_text_search": {},
                "embed": {
                    "model": "gemini-embedding-2",
                    "dimension": 1536,
                },
            }
        }
    },
)

index = pc.index("support-articles")

index.documents.upsert(
    namespace="articles",
    documents=[
        {"_id": "kb-205", "body": "Refunds take five business days."},
    ],
)
To search, send the query as text. This search also tells Gemini Embedding 2 to embed the query for question answering:
results = index.documents.search(
    namespace="articles",
    top_k=5,
    score_by=[
        {
            "type": "embed",
            "fields": ["body"],
            "query": "how long do refunds take",
            "parameters": {"task_type": "question_answering"}
        }
    ],
    include_fields=["body"],
)
If you leave out the
dimension
, the field uses the model's full size. Any size the model supports works, so you can keep the dimensions your existing indexes already use.
Gemini Embedding 2 expects a short instruction at the start of each input that says whether the text is a document or a query. Pinecone adds the right instruction to every write and every query, so you don't need model-specific prompts.
By default, Pinecone embeds Gemini Embedding 2 fields for general search. Set
task_type
on the field for
classification
,
clustering
, or
sentence_similarity
. A single search can also set
task_type
to
question_answering
,
fact_verification
, or
code_retrieval_query
for that query. See the
full list of task types Pinecone supports
.
Gemini Embedding 2 supports text in more than 100 languages. The model processes text globally, which means Google can handle each request in any of its regions, with no specific region guaranteed.
Availability and limits
Gemini Embedding 2 works on serverless Documents API indexes. BYOC, pod-based, and Records API indexes aren't supported.
The console and Python SDK 10.3.0 support Gemini Embedding 2. Support in the Node.js and Go SDKs is coming soon.
Existing vector indexes can be converted to Documents API indexes without re-embedding. Adding integrated embedding to a converted index is coming soon. Until then, use Gemini Embedding 2 on new Documents API indexes and send them your text.
Integrated embedding works on text fields today, not on multimodal fields. So, while Gemini Embedding 2 can also embed images, video, and audio, it is only offered as a text model today. Multimodal support is planned for a later release.
Builder plan includes 10M tokens a month for Gemini Embedding 2, and
twice that through December 31, 2026.
Get started
Read the
integrated embedding docs
to learn how to set up Google's Gemini Embedding 2 on a Documents API index.
Through December 31, 2026, the Builder plan gets twice its included tokens for Gemini Embedding 2: 20M a month.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
