---
title: "Vector Databases"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags: [embeddings, retrieval, rag, infrastructure, database, vector-search, hnsw, ann, agent-memory, quantization]
sources: [raw/articles/2026-07-28_vector-databases-landscape-overview.md]
---

# Vector Databases

Vector databases are specialized database systems designed to store, index, and query high-dimensional vector embeddings. They are a foundational infrastructure category for modern AI applications, powering semantic search, Retrieval-Augmented Generation (RAG), recommendation engines, and agent memory systems.

Unlike traditional databases that excel at exact matches or structured queries, vector databases perform **similarity search** — finding items that are semantically close to a query vector in high-dimensional space. This makes them indispensable when meaning matters more than literal keyword matching.

## Why Vector Databases Matter

The rise of [[entities/embeddings|embedding models]] has made vector representations the lingua franca of AI systems. Every text passage, image, audio clip, or code snippet can be converted into a fixed-length vector that captures its semantic essence. Vector databases provide the storage and retrieval layer that makes these embeddings actionable:

- **RAG pipelines**: Retrieve relevant context from a knowledge base before generating responses with an LLM. See [[concepts/modern-retrieval-toolkit]] for the full retrieval stack.
- **Semantic search**: Find documents by meaning rather than keywords, enabling more robust and forgiving search experiences.
- **Recommendation systems**: Match users to items based on behavioral or content embeddings.
- **Agent memory**: Store and retrieve conversation history, facts, and experiences for long-running AI agents. See [[concepts/ai-agent-memory-middleware]] for agent memory infrastructure patterns.
- **Multimodal retrieval**: Search across text, images, and audio in a unified embedding space.

## Key Concepts

### ANN Search

**Approximate Nearest Neighbor (ANN)** search is the core algorithm family that makes vector databases practical. Exact nearest neighbor search scales poorly with dimensionality and dataset size. ANN algorithms trade a small amount of accuracy for massive speed improvements — often returning results in milliseconds across billions of vectors.

### Index Types

Different ANN algorithms suit different workloads:

| Index | Approach | Best For |
|-------|----------|----------|
| **HNSW** (Hierarchical Navigable Small World) | Graph-based, multi-layer proximity graph | High recall, moderate memory; general-purpose workhorse |
| **IVFFlat** (Inverted File Flat) | Clustering-based, coarse quantization | Balanced speed/accuracy; widely supported |
| **IVF-PQ** (Product Quantization) | Compressed vector storage | Memory-constrained deployments |
| **DiskANN** | SSD-resident graph index | Billion-scale datasets on commodity hardware |

### Distance Metrics

The choice of distance metric depends on the embedding model and use case:

- **Cosine similarity**: Measures the angle between vectors; most common for text embeddings (range: -1 to 1)
- **Euclidean distance (L2)**: Straight-line distance in vector space; sensitive to magnitude
- **Dot product**: Equivalent to cosine similarity when vectors are normalized; efficient on GPUs

### Metadata Filtering and Hybrid Search

Pure vector search has blind spots — it can miss exact matches (e.g., "documents from 2024") or struggle with rare terms. Most production vector databases support:

- **Metadata filtering**: Pre-filter or post-filter results based on structured metadata (dates, tags, authors, categories)
- **Hybrid search**: Combine vector similarity with traditional keyword search (BM25, TF-IDF) for improved recall on mixed queries

### Quantization

To reduce memory footprint, vector databases apply quantization techniques that compress vectors from float32 to int8, binary, or other compact representations. This enables larger datasets to fit in RAM at the cost of some recall. See [[concepts/embedding-long-context-degradation]] for related embedding quality concerns.

## Comparison of Major Players

| Database | Type | Index Support | Hybrid Search | Deployment | Key Differentiator |
|----------|------|---------------|---------------|------------|--------------------|
| **Pinecone** | Managed cloud (proprietary) | Proprietary serverless index | Yes (sparse-dense) | Cloud only | Zero-ops serverless; Fortune 50 AI Innovator |
| **Chroma** | Open-source, Python-native | HNSW | Basic metadata filtering | Local, client/server, cloud | Developer experience; deep LangChain/LlamaIndex integration |
| **Qdrant** | Open-source (Rust) | HNSW, quantization | Yes (full-text + vector) | Self-hosted, cloud | Performance; Rust-based; advanced filtering |
| **Weaviate** | Open-source | HNSW, flat | Yes (hybrid BM25 + vector) | Self-hosted, cloud | GraphQL API; built-in vectorization modules; multi-modal |
| **Milvus** | Open-source (cloud-native) | 12+ index types (HNSW, IVF, DiskANN, etc.) | Yes | Self-hosted (Kubernetes), cloud | Billion-scale; graduated LF AI & Data Foundation |
| **pgvector** | PostgreSQL extension | IVFFlat, HNSW | Native SQL filtering | Any Postgres deployment | Zero new infrastructure; ACID compliance; SQL integration |
| **LanceDB** | Open-source, serverless | IVF-PQ, disk-based | Metadata + full-text | Embedded (no server) | Serverless multimodal; Lance columnar format |

## Relationship to Agent Memory

Vector databases are a critical building block for [[concepts/ai-agent-memory-middleware|agent memory systems]]. They enable agents to store and retrieve past interactions, learned facts, and contextual information using semantic similarity. This allows agents to maintain state across sessions and build up knowledge over time — a key requirement for [[concepts/agentic-search|agentic search]] and long-running autonomous workflows.

## Selection Considerations

When choosing a vector database, consider:

1. **Scale**: Thousands of vectors? pgvector or Chroma. Billions? Milvus or Pinecone.
2. **Infrastructure**: Already running Postgres? Start with pgvector. Want serverless? LanceDB or Pinecone.
3. **Search requirements**: Need hybrid keyword+vector? Weaviate or Qdrant. Pure dense retrieval only? Chroma is simpler.
4. **Multi-modality**: Working with images, audio, and text together? Weaviate or LanceDB.
5. **Control vs. convenience**: Self-host for data sovereignty (Qdrant, Milvus, Chroma), managed for zero-ops (Pinecone).

## Open Questions

- **Are specialized vector databases always necessary?** For many use cases, pgvector on an existing Postgres instance is sufficient. The bar for adopting a separate vector database is rising.
- **Late interaction vs. single-vector models**: Models like ColBERT produce multiple vectors per document, requiring different retrieval architectures than traditional single-vector ANN.
- **Embedding drift**: As embedding models are updated, stored vectors become outdated. Re-indexing strategies remain an open engineering challenge.
