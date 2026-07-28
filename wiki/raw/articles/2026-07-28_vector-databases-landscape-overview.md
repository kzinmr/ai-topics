---
title: "Vector Databases Landscape — Overview and Comparison"
source: "synthesis"
author: "Hermes Agent (synthesis from multiple sources)"
date: "2026-07-28"
date_ingested: "2026-07-28"
publication: "Wiki research synthesis"
tags: [vector-database, embeddings, retrieval, rag, infrastructure]
type: raw_article
sources:
  - "https://www.pinecone.io/"
  - "https://www.trychroma.com/"
  - "https://qdrant.tech/"
  - "https://weaviate.io/"
  - "https://milvus.io/"
  - "https://lancedb.com/"
  - "https://github.com/pgvector/pgvector"
---

# Vector Databases Landscape — Overview

Vector databases are specialized database systems optimized for storing and querying high-dimensional vector embeddings, which are central to modern AI applications including RAG (Retrieval-Augmented Generation), semantic search, and recommendation systems.

## Major Players

### Pinecone
- Fully managed, serverless vector database
- Proprietary cloud service
- Popular for production RAG applications
- Strengths: ease of use, no infrastructure management, high availability
- Fortune 50 AI Innovator (2023)

### Chroma
- Open-source, developer-friendly vector database
- Python-native, runs locally or in cloud
- Popular in the LangChain/LlamaIndex ecosystem
- Strengths: simplicity, developer experience, embedded mode

### Qdrant
- Open-source, high-performance vector search engine
- Written in Rust for performance
- Supports both self-hosted and cloud deployments
- Strengths: performance, filtering, quantization for memory efficiency

### Weaviate
- Open-source vector database with hybrid search
- GraphQL and REST APIs
- Built-in vectorization modules
- Strengths: hybrid search (vector + keyword), multi-modal, schema flexibility

### Milvus
- Cloud-native, open-source vector database
- Designed for billion-scale similarity search
- Graduated from LF AI & Data Foundation
- Strengths: scalability, distributed architecture, multiple index types

### pgvector
- PostgreSQL extension for vector similarity search
- Integrates vector operations into existing Postgres workflows
- Supports IVFFlat and HNSW indexes
- Strengths: zero new infrastructure, SQL integration, ACID compliance

### LanceDB
- Serverless, embedded vector database
- Built on Lance columnar format
- Designed for multimodal AI applications
- Strengths: serverless, multimodal, no separate service required

## Key Concepts
- ANN (Approximate Nearest Neighbor) search
- Index types: HNSW, IVFFlat, IVF-PQ, DiskANN
- Distance metrics: cosine similarity, Euclidean, dot product
- Metadata filtering and hybrid search
- Quantization for memory efficiency
