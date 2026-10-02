---
title: "Compass is coming to the cloud"
source: "Cohere Blog"
url: "https://cohere.com/blog/compass-cloud-beta"
scraped: "2026-09-30T06:00:30.421267+00:00"
lastmod: "2026-09-25"
type: "sitemap"
---

# Compass is coming to the cloud

**Source**: [https://cohere.com/blog/compass-cloud-beta](https://cohere.com/blog/compass-cloud-beta)

Compass
is Cohere’s retrieval platform for developers building AI applications with their enterprise data. It surfaces the most relevant information from your company’s corpus for use in retrieval-augmented generation (RAG), search, and agentic workflows. Now, Compass is entering private beta as a managed offering -
Compass Cloud
.
Compass was built for builders. It provides the retrieval foundation that developers can freely configure around their data and workflow requirements. Instead of assembling and operating the stack themselves, teams access Compass through its APIs, MCP server, or
Python SDK
to shape their desired end user experience.
Until now, Compass has principally powered retrieval for
North
, Cohere's enterprise agent workspace, including its document libraries and MCP ecosystem. We have also shipped Compass into highly secure, self-hosted environments for partners in regulated industries whose workloads cannot be offloaded to SaaS.
Customer demand for a managed option has been clear and consistent: teams want Compass' best-in-class retrieval capabilities, but many do not want the operational overhead that comes with self-hosting.
We’ve listened to those calls. Compass Cloud expands Compass to a broader market. It lets Cohere manage the full pipeline
and
model inference, so that our customers can focus even more on building. In parallel, self-hosted deployments remain available for privacy-constrained projects.
We're working with a limited number of enterprise teams as beta partners. Interested?
Request access
.
Compass is solving open problems in enterprise search
Search and retrieval have improved, but enterprise performance is no longer defined by relevance and latency for a single query. As retrieval becomes key supporting infrastructure for generative AI and agents, three developments are changing the requirements:
Token economics:
Every irrelevant result passed to a model consumes tokens and occupies limited context space. More precise retrieval creates smaller, higher-quality inputs, reducing inference costs and cutting the time needed to complete a task. Retrieval is one of the most effective cost levers available to businesses today.
Agentic access patterns:
Agents may issue dozens of queries while completing one task, reformulating requests and traversing multiple sources. In these multi-hop loops, latency accumulates, relevance can drift, and permissions must be enforced at every step. Retrieval must therefore perform reliably across sequences of machine-generated queries, not only single-shot searches.
A fragmented retrieval stack:
Production pipelines often combine separate systems for ingestion, indexing, reranking, access control, and orchestration. Different middleware and sources of truth leave teams spending substantial effort on integration rather than retrieval quality.
Compass exists to address each of these: 1) by providing relevant, governed context for generative workloads; 2) supporting both agentic and conventional search applications; and 3) consolidating the core retrieval stack into an integrated enterprise platform.
Full-stack search and retrieval
Compass packages document processing and retrieval into one configurable service. Teams can access a single interface instead of integrating and operating separate services.
Cohere Compass architecture: a governed enterprise retrieval stack connecting data sources to front-end applications through parsing, embedding, hybrid search, and reranking.
Connect:
Access out-of-the-box connectors for your file sharing and cloud storage workspaces, such as SharePoint, OneDrive, and Google Drive. Quickly access the content you need with Compass’ near-universal data compatibility — multilingual, multimodal, and file format-agnostic.
Parse:
Turn complex documents into searchable, structured data. Compass transforms multimodal enterprise files into AI-ready content, applying the right parsing strategy to each document and using vision processing only where it adds value, reducing unnecessary model usage.
Embed:
Capture meaning and exact terminology. Compass generates dense and sparse representations together, so search can match both semantic intent and domain-specific language across text and multimodal content.
Index:
Keep your source files, parsed content, and embeddings as separate records, so a new embedding model can be adopted without crawling and uploading the same content again. At search time, they sit in one index with their metadata, reducing the need to keep each system in sync.
Retrieve:
Combine search strategies in one request. Semantic, sparse, and keyword search can run independently or together, balancing recall and precision. Permissions are enforced during retrieval rather than left to the application.
Rerank:
Send stronger evidence to the model. Cohere’s best-in-class reranker identifies the most relevant passages from a broad candidate set, reducing irrelevant context and the tokens required for generation.
Govern:
Enforce multi-tenant access control and document-level permissions during retrieval, so applications don’t have to filter results themselves. In Compass, retention policies expire content automatically and prevent deleted documents from being resynced.
Premium retrieval accuracy
The core objective of Compass is simple: improve the relevance of information surfaced for enterprise knowledge applications, be that a RAG pipeline or an autonomous agent. That quality is rooted in Cohere's best-in-class search and document-processing models together with Compass's hybrid search: lexical, sparse, and dense retrieval, then rerank.
The figure below is one instance of the accuracy gain over traditional or standalone search infrastructure on a representative financial-industry RAG workload: embed a query, retrieve presentation materials from an index, and score the top results. On High Finance, a Cohere-built investment-banking benchmark, Compass achieved a 14-16 point improvement on Azure Search (from 64.8 to 81.1). A gap of this size can be the difference between an unsatisfactory answer and a great one for the end user.
Retrieval accuracy (nDCG@10) on High Finance. High Finance is an internal, Cohere-annotated set of questions that ask models to retrieve the relevant investment banking and hedge fund presentation material. Azure Search documents were parsed with GPT-4.1 Mini. Cohere Embed 4 did not use a separate parsing solution, but embedded the input PDFs directly as an image before searching.
Build on your terms
Users can upgrade their search performance with Compass Cloud in two key ways, depending on how they want to integrate retrieval into their application:
Compass API:
Best for teams building custom RAG and search applications. Use Compass APIs to integrate directly with the models and retrieval components that power Compass, giving developers more control over how content is represented, retrieved, ranked, and incorporated into their application.
Model Context Protocol (MCP):
Best for agentic retrieval. Compass ships a dedicated, independently versioned MCP server that exposes retrieval as reusable tools through an open standard. MCP-compatible clients can discover and call those tools directly, making Compass portable across agent frameworks without a bespoke integration for each one.
Agentic retrieval is an emerging approach at the intersection of large language models and information retrieval. Rather than relying on a single query-and-response retrieval step, an agent can decide what to look for, search for relevant information, evaluate the results, and refine its search before answering.
This is especially useful for tasks that cannot be resolved with a single lookup. With the Compass MCP server, agents can progressively narrow the retrieval corpus, reducing unnecessary context and making complex retrieval tasks faster and more token-efficient.
Connecting an enterprise agent to the Compass MCP in North.
Get early access
We’re opening this private beta for teams building retrieval-heavy and agentic applications.
Beta participants get hands-on support from the engineering team, early access to the cloud deployment, and direct influence on the roadmap.
Request access
.
We’re also running a live session on
October 8th
on
X
with Cohere’s engineering and product leadership on where enterprise search goes next.
Blog
Written By
Cohere Team
Tags
Product Launch
AI for Developers
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
