---
title: "Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/rag-system-mongodb-atlas"
scraped: "2026-05-10T01:27:31.140818+00:00"
lastmod: "2026-02-12T18:52:17.000Z"
type: "sitemap"
---

# Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas

**Source**: [https://fireworks.ai/blog/rag-system-mongodb-atlas](https://fireworks.ai/blog/rag-system-mongodb-atlas)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Rag System Mongodb Atlas
Building Enterprise-Scale RAG Systems with Fireworks AI and MongoDB Atlas
PUBLISHED
4/9/2025
Table of Contents
Why Enterprises Need RAG
High-Level Architecture
Performance & Fireworks Metrics
Future Additions & Scalability
Advantages of the Fireworks + MongoDB Atlas Stack
Conclusion & Call-to-Action
Table of Contents
Table of Contents
Why Enterprises Need RAG
High-Level Architecture
Performance & Fireworks Metrics
Future Additions & Scalability
Advantages of the Fireworks + MongoDB Atlas Stack
Conclusion & Call-to-Action
Table of Contents
This project is completely open-source, including all documentation, code, and tests, which can be found at:
https://github.com/shubcodes/earnings-ai-demo
In the fast-paced world of enterprise data, extracting actionable insights from vast amounts of unstructured information is a challenge many organizations face. Whether it’s earnings calls, financial reports, legal documents, or technical specifications, the ability to retrieve, synthesize, and act on this information quickly can make or break a company’s competitive edge. Enter Retrieval-Augmented Generation (RAG) – a cutting-edge solution combining Large Language Models (LLMs) with powerful retrieval systems to deliver contextually rich, actionable insights in real time.
Why Enterprises Need RAG
Let’s face it: traditional search systems just don’t cut it anymore. They’re limited to keyword matching and fail to grasp the semantic and contextual relationships necessary for enterprise-scale decision-making. Here’s why RAG stands out:
Multi-Format Analysis
: RAG handles data from PDFs, Word documents, spreadsheets, and even audio recordings, breaking silos between formats.
Cross-Document Insights
: It synthesizes information across multiple documents, answering complex queries like “How has our AI strategy evolved over the last three earnings calls?”
Real-Time Results
: Sub-second query responses empower businesses to act on insights immediately.
Natural Language Interaction
: With RAG, asking questions feels intuitive, like speaking to a knowledgeable colleague.
High-Level Architecture
Our enterprise RAG system is built using Fireworks AI for inference and MongoDB Atlas for vector storage. Here’s an overview of the pipeline:
Document Processing Pipeline
The ability to process diverse document formats is the cornerstone of any robust RAG system. Without this capability, organizations are left with data silos and limited insights. The document processing pipeline ensures that content from PDFs, DOCX files, and plain text is not only extracted but also enriched with metadata for better querying.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
class
DocumentExtractor
:
def
extract_text
(
self
,
file_path
:
str
)
-
>
Dict
:
path
=
Path
(
file_path
)
if
path
.
suffix
.
lower
(
)
==
'.pdf'
:
text
=
self
.
_extract_pdf
(
path
)
elif path
.
suffix
.
lower
(
)
==
'.docx'
:
text
=
self
.
_extract_docx
(
path
)
else
:
text
=
path
.
read_text
(
encoding
=
'utf-8'
)
return
{
"text"
:
text
,
"metadata"
:
{
"filename"
:
path
.
name
,
"file_type"
:
path
.
suffix
.
lower
(
)
[
1
:
]
,
"file_size"
:
path
.
stat
(
)
.
st_size
}
}
Key Features
:
•
Format-Specific Processing
: Handles PDFs, DOCX, and text files with tailored methods.
•
Metadata Preservation
: Retains file context for better querying.
•
Error Handling
: Detects and logs corrupt or unsupported files.
Audio Transcription with Fireworks Whisper V3 Turbo
Efficient transcription of audio content is another vital component. Fireworks’
Whisper V3
Turbo can transcribe one hour of audio in just 3 seconds, making it 20x faster than competing solutions such as OpenAI Whisper. This speed advantage significantly reduces latency and enhances user experiences.
1
2
3
4
5
6
7
8
9
10
11
class
AudioTranscriber
:
def
__init__
(
self
,
api_key
:
str
,
base_url
:
str
=
"https://api.fireworks.ai/audio/v3-turbo"
)
:
self
.
client
=
AudioInference
(
api_key
=
api_key
,
base_url
=
base_url
)
def
transcribe_audio
(
self
,
file_path
:
str
)
-
>
Dict
:
with
open
(
file_path
,
'rb'
)
as
audio_file
:
response
=
self
.
client
.
transcribe
(
audio
=
audio_file
.
read
(
)
)
return
{
"transcription"
:
response
.
text
,
"duration"
:
response
.
metadata
.
duration
}
Key Advantages
:
•
Speed
: Processes audio up to 900x faster than real-time.
•
Cost Efficiency
: 10x cheaper than most alternatives.
•
Feature Completeness
: Includes transcription alignment, translation, and preprocessing capabilities.
Vector Embedding
Once the content is extracted, converting it into vector embeddings allows the system to understand and process queries semantically. This step is critical for enabling similarity searches and advanced data retrieval.
1
2
3
4
5
6
7
8
def
generate_document_embedding
(
self
,
text
:
str
,
prefix
:
str
=
""
,
method
:
str
=
"mean"
)
-
>
List
[
float
]
:
chunks
=
self
.
_chunk_text
(
text
)
chunk_embeddings
=
self
.
generate_embeddings_batch
(
chunks
,
prefix
)
if
method
==
"mean"
:
return
np
.
mean
(
chunk_embeddings
,
axis
=
0
)
.
tolist
(
)
elif method
==
"max"
:
return
np
.
max
(
chunk_embeddings
,
axis
=
0
)
.
tolist
(
)
Why This Works
:
Chunking
: Splits documents into manageable parts while maintaining context.
Batch Processing
: Optimizes GPU utilization.
Aggregation
: Combines embeddings for holistic document representation.
MongoDB Atlas for Vector Search
Efficient storage and retrieval of vector embeddings ensure that enterprise systems can handle queries at scale without compromising performance. MongoDB Atlas provides a scalable, high-performance solution for this task.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
def
query_similar
(
self
,
query_embedding
:
List
[
float
]
,
limit
:
int
=
5
,
filters
:
Dict
=
None
)
-
>
List
[
Dict
]
:
pipeline
=
[
{
"$vectorSearch"
:
{
"index"
:
"vector_index"
,
"queryVector"
:
query_embedding
,
"path"
:
"embeddings"
,
"numCandidates"
:
limit
*
10
,
"limit"
:
limit
}
}
]
if
filters
:
pipeline
.
append
(
{
"$match"
:
filters
}
)
pipeline
.
append
(
{
"$project"
:
{
"text"
:
1
,
"metadata"
:
1
,
"score"
:
{
"$meta"
:
"vectorSearchScore"
}
}
}
Fireworks AI: The Intelligence Layer
The intelligence of the RAG pipeline lies in its ability to synthesize information and generate coherent, actionable answers. Fireworks AI powers this layer, ensuring low-latency, high-accuracy responses. By integrating with MongoDB Atlas for semantic retrieval, Fireworks AI orchestrates an end-to-end workflow where user queries are processed efficiently and contextually enriched responses are returned.
Query Process and Contextual Retrieval
When a user submits a query, the RAG system performs the following steps:
Query Embedding Generation
: The user’s query is transformed into a vector embedding using a pre-trained embedding model.
Semantic Retrieval
: This embedding is sent to the MongoDB Atlas vector store, where it matches against the stored document embeddings to retrieve the top relevant documents. The retrieval process ranks these documents based on their similarity to the query, measured by cosine similarity or other vector distance metrics.
Contextual Aggregation
: The retrieved documents are then aggregated to form a cohesive context block. This includes the full text of relevant sections, metadata such as document titles, and their confidence scores.
LLM Query Processing
: The aggregated context is appended to the user’s query, which is passed into the LLM hosted on Fireworks AI. The LLM generates an answer based on the query and the contextual information.
Response Augmentation
: Alongside the generated response, the system includes the source documents and their confidence scores to ensure transparency. Confidence scores indicate the retrieval model’s certainty in the relevance of each document.
Transparency and Confidence
Including the source and confidence score in the response provides critical benefits:
•
Traceability
: Users can see exactly which documents informed the response, improving trust in the system.
•
Decision Confidence
: Higher confidence scores reassure users about the reliability of the retrieved information.
•
Iterative Queries
: If needed, users can refine queries based on the provided sources, enabling a more interactive experience.
Performance & Fireworks Metrics
To highlight the system’s efficiency:
Metric
Fireworks AI
OpenAI
Throughput
100 req/s
50 req/s
Latency
<500ms
~1000ms
Cost Efficiency
10x cheaper
Standard
Audio Transcription
3 sec/hour (V3 Turbo)
105 sec/hour
Fireworks achieves remarkable performance through advanced quantization techniques and hardware optimizations, ensuring top-tier throughput and low cost without sacrificing accuracy.
Future Additions & Scalability
The future of enterprise RAG systems lies in expanding capabilities while maintaining efficiency. Here’s how Fireworks AI and MongoDB Atlas are set to evolve:
Multi-Agent Orchestration
Imagine a system where specialized agents handle specific types of data. For instance:
•
Financial Insights
: One agent focuses on financial documents, offering deep analysis of earnings reports and balance sheets.
•
Legal Parsing
: Another agent excels at interpreting legal contracts, highlighting key clauses and compliance risks.
•
Human Resources
: A third agent manages HR documents, extracting employee trends and policy effectiveness.
These agents would collaborate within a unified architecture, enabling seamless cross-domain queries.
Enhanced Data Structuring
Structured data, such as tables and charts, remains a challenge for many RAG systems. Future iterations will integrate advanced table-parsing models, enabling:
•
Time-Series Analysis
: Automatic interpretation of financial trends from spreadsheets.
•
Graph Insights
: Extraction of relationships and hierarchies from organizational charts.
Cross-Company Insights
Organizations often operate in competitive landscapes where comparative analysis is key. Multi-tenant RAG systems will allow companies to:
•
Benchmark Performance
: Compare metrics against industry peers.
•
Market Analysis
: Synthesize competitor strategies from publicly available data.
•
Collaborative Insights
: Securely share and analyze data across subsidiaries or partners.
Dynamic Scaling and Optimization
Fireworks AI will continue to push boundaries in scalability by integrating:
•
Speculative Decoding
: Predicting user intents to prefetch relevant documents, reducing query latency.
•
Adaptive Workloads
: Dynamic resource allocation based on query complexity and system demand.
•
Federated Learning
: Securely training models across distributed data sources to enhance performance without compromising privacy.
Advantages of the Fireworks + MongoDB Atlas Stack
Unmatched Speed
: Fireworks AI processes tasks 20x faster than many competitors, including OpenAI.
Flexibility
: Offers state-of-the-art embedding models and custom deployments.
Scalability
: MongoDB Atlas’ vector search supports millions of documents efficiently.
Advanced Features
: Includes speculative decoding, dynamic resource allocation, and compliance with SOC2 and HIPAA standards.
Cost Efficiency
: Reduced operational costs with optimized compute resources.
Conclusion & Call-to-Action
The Fireworks AI + MongoDB Atlas stack revolutionizes how enterprises extract insights from unstructured data. By leveraging cutting-edge transcription, retrieval, and generation technologies, organizations can accelerate decision-making, reduce time-to-insight, and unlock the full potential of their data.
Ready to transform your data strategy? Start building on
fireworks.ai
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
