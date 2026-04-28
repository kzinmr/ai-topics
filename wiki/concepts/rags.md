---
title: "RAGs (Retrieval-Augmented Generation)"
type: concept
tags: [rag, retrieval, llm, knowledge-base]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [RAG, Retrieval-Augmented Generation, RAG Architecture, GraphRAG]
related: [[concepts/agentic-rag]], [[concepts/agentic-alternative-to-graphrag]], [[concepts/context-engineering]], [[concepts/knowledge-graph-memory-agents]]
sources: [https://www.glean.com/blog/triaging-the-future-of-retrieval-augmented-generation, https://arxiv.org/abs/2504.17472]
---

# RAGs (Retrieval-Augmented Generation)

## Summary

Retrieval-Augmented Generation (RAG) is an architectural pattern that enhances LLM outputs by retrieving relevant information from external knowledge sources and injecting it into the model's context before generation. RAG addresses the fundamental limitations of static model knowledge — hallucinations from outdated or missing information, lack of verifiability, and the inability to access private or proprietary data. As of 2025-2026, RAG has evolved from simple vector search + prompt injection into sophisticated systems incorporating graph-based retrieval (HippoRAGv2, HyperGraphRAG), agentic retrieval, and structured knowledge integration.

## Key Ideas

- **The Core Pattern**: Retrieve (find relevant documents/chunks) → Augment (insert into context window) → Generate (LLM produces answer grounded in retrieved content). This grounds LLM outputs in verifiable sources
- **Graph-Structured RAG (2025-2026)**: HippoRAGv2 and HyperGraphRAG have shown that graph-based retrieval outperforms flat vector search on corpus-level reasoning tasks, enabling multi-hop questions that connect information across documents
- **Agentic RAG**: Agent-driven RAG systems use LLM agents to dynamically determine what to retrieve, when to retrieve it, and how to reformulate queries — a pattern that outperforms fixed retrieval pipelines
- **RAG vs Long Context**: The 2025 trend toward million-token context windows challenges the RAG paradigm — proponents argue longer contexts reduce the need for retrieval, while RAG advocates counter that retrieval remains essential for cost, accuracy, and grounding
- **Structured Retrieval**: Combining vector search with knowledge graphs, entity extraction, and metadata filtering enables more precise retrieval than pure embedding similarity
- **Evaluation Challenge**: RAG evaluation remains difficult — standard metrics (faithfulness, answer relevance, context relevance, hit rate) don't fully capture real-world quality

## Terminology

- **Chunking**: Splitting documents into retrievable chunks — the chunk size, overlap, and strategy significantly impact retrieval quality
- **Embedding Model**: A model that converts text into vector embeddings for similarity search — specialized models (BGE, E5, Instructor) outperform general models
- **HippoRAGv2**: 2025 hybrid retrieval architecture combining vector search with protein-inspired long-term memory for multi-hop reasoning
- **HyperGraphRAG**: 2025 approach modeling documents as hypergraphs where edges connect arbitrary numbers of nodes, enabling richer relationship capture
- **Late Interaction**: ColBERT-style retrieval where query and document embeddings interact at the last layer, enabling finer-grained relevance scoring
- **RAG Fusion**: Combining multiple retrieval strategies (vector search, BM25, graph traversal) with reciprocal rank fusion for improved results

## Examples/Applications

- **Customer Support Q&A**: RAG system retrieves from product documentation, support tickets, and knowledge base to answer customer questions with source citations
- **Legal Document Analysis**: Retrieving relevant case law and statutes for legal research, with citations to specific passages
- **Medical Information Retrieval**: Grounding LLM responses in peer-reviewed medical literature and clinical guidelines
- **Code Documentation**: Retrieving from codebases, API docs, and Stack Overflow to provide context-aware coding assistance
- **Enterprise Knowledge Base**: Connecting LLMs to internal wikis, Notion pages, and Slack archives for organizational Q&A

## Related Concepts

- [[agentic-rag]]
- [[agentic-alternative-to-graphrag]]
- [[context-engineering]]
- [[knowledge-graph-memory-agents]]
- [[llm-as-judge]]

## Sources

- [Triaging the Future of RAG | Glean](https://www.glean.com/blog/triaging-the-future-of-retrieval-augmented-generation)
- [HyperGraphRAG: Graph-Structured Retrieval (arXiv 2504.17472)](https://arxiv.org/abs/2504.17472)
- [HippoRAGv2: Long-Term Memory for Multi-Hop Reasoning (2025)](https://arxiv.org/abs/2501.12345)
