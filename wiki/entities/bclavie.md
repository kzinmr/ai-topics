---
title: "Benjamin Clavié"
handle: "@bclavie"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai, information-retrieval, nlp, rag, huggingface]
aliases: ["bclavie", "Ben Clavie"]
related:
  - "[[rag]]"
  - "[[information-retrieval]]"
  - "[[answerdotai]]"
  - "[[colbert]]"
---

# Benjamin Clavié (@bclavie)

| | |
|---|---|
| **X** | [@bclavie](https://x.com/bclavie) |
| **Blog** | [ben.clavie.eu](https://ben.clavie.eu/posts) |
| **GitHub** | [bclavie](https://github.com/bclavie) |
| **Role** | R&D Engineer at Answer.AI |
| **Known for** | Creator of RAGatouille, ColBERT research, JaColBERTv2.5, ModernBERT |
| **Bio** | French NLP/IR researcher based in Tokyo, Japan. Works on retrieval-augmented generation, late-interaction models, and making state-of-the-art information retrieval accessible to practitioners. Previously at Mixedbread AI. Co-lead on ModernBERT and creator of several open-source retrieval libraries. |

## Overview

Benjamin Clavié is a French researcher specializing in natural language processing and information retrieval, currently based in Tokyo, Japan. He works at Answer.AI, where he focuses on building better retrieval systems and bridging the gap between academic IR research and practical production use. His core mission is to democratize advanced retrieval techniques — particularly late-interaction models like ColBERT — that historically had a high barrier to entry for non-specialist practitioners.

Clavié's most visible contribution is **RAGatouille**, an open-source library (3,800+ GitHub stars) that provides a simple, few-lines API for using ColBERT and other late-interaction retrieval methods in RAG pipelines. RAGatouille has been instrumental in popularizing ColBERTv2, driving monthly downloads from ~50k to over 3 million. His philosophy, as he articulates it, is that "ML should be a commodity for everyone, not just ML practitioners," and his work consistently focuses on reducing friction between cutting-edge research and real-world deployment.

Beyond RAGatouille, Clavié has been involved in several notable open-source projects. He co-led **ModernBERT**, a project modernizing the BERT architecture for current hardware and workloads. He released **JaColBERTv2.5**, a Japanese retrieval model that achieved state-of-the-art performance with just 110M parameters trained in under 15 hours on 4 A100 GPUs — demonstrating that careful training methodology can dramatically outperform brute-force scaling. He also created **rerankers**, a unified API library for cross-encoder reranking methods, and contributed to **ColPali** work through the **Byaldi** toolkit.

## Core Ideas

### Late-Interaction Retrieval as the Superior RAG Foundation
Clavié is a vocal advocate for late-interaction retrieval models (especially ColBERT) over dense embedding approaches like OpenAI's text-ada-002. His core argument is that dense embeddings compress documents into single vectors, losing fine-grained matching capability, while ColBERT's "bag-of-embeddings" approach preserves token-level interactions:

> "I like to explain ColBERT as a bag-of-embeddings approach, as this makes it immediately obvious how and why ColBERT works to NLP practitioners: Just like bag-of-words, it works on small information units, and represents a document as the sum of them."

He describes ColBERT as a "semantic keyword matcher" — leveraging strong encoder models like BERT to break documents into contextualized information units rather than single document-level vectors.

### Bridging the Academia-Industry Gap
In a February 2024 blog post titled "Questions & Answer(s): thoughts and joining Answer.AI," Clavié outlined his concern about the gap between IR research and practical usage:

> "I think ML developments are incredibly exciting, and we need to continue to work on bridging the gap between ML-as-a-commodity-for-ML-practitioners to ML-as-a-commodity-for-everyone. This hopefully can happen with a mix of better products and more open source projects."

He likens RAGatouille's role to what SentenceTransformers did for embeddings: taking powerful but hard-to-use research and wrapping it in accessible APIs.

### Token Pooling for Efficient Multi-Vector Retrieval
Clavié co-authored a paper on **token pooling** for late-interaction models, demonstrating that clustering-based token aggregation can reduce ColBERT index sizes by 50% with virtually no performance degradation, and by 66–75% with less than 5% degradation. This work addresses one of the main practical barriers to ColBERT adoption: storage overhead.

### Data-Centric Training Over Brute-Force Scaling
The JaColBERTv2.5 project exemplifies his belief in training methodology over raw scale. By performing nearly 30 ablation experiments, his team reduced training data by 60% while improving performance — showing that "there are still a lot of free lunches on the table" in retrieval training.

## Key Work

### RAGatouille (2023–present)
An open-source library making ColBERT and late-interaction retrieval accessible for RAG pipelines. Features include index building, querying, reranking, and model fine-tuning with a 3-line API. The library has ~3,800 GitHub stars and has driven ColBERTv2 downloads from ~50k to 3M+ per month. Created while at Answer.AI, with contributions from the broader IR community.

- **GitHub**: [AnswerDotAI/RAGatouille](https://github.com/answerdotai/ragatouille)
- **License**: Apache 2.0

### JaColBERTv2.5 (2024)
State-of-the-art Japanese retrieval model with 110M parameters. Trained on 3.2M triplets (40% of the data used by its predecessor) in under 15 hours on 4 A100 GPUs. Outperforms all existing Japanese retrieval models including bge-m3. Released with full training snapshots, teacher scores, and ablation results to support further research.

- **Blog**: [JaColBERTv2.5 at Answer.AI](https://www.answer.ai/posts/2024-08-02-jacolbert-v25.html)

### ModernBERT (2024–2025)
Co-led project (with Benjamin Warner and Antoine Chaffin) modernizing the BERT architecture for current hardware. Focuses on improved training methodology, better tokenization, and architectural updates.

### Token Pooling Paper (2024)
Co-authored paper: "Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling." Introduced clustering-based token aggregation reducing ColBERT storage by 50% with no performance loss.

- **arXiv**: [2409.14683](https://arxiv.org/abs/2409.14683)

### Rerankers Library
A unified API for cross-encoder reranking methods, supporting multiple backends and models. Addresses the fragmentation in reranking tooling for production RAG pipelines.

### Byaldi (ColPali Toolkit)
A one-shot toolkit for experimenting with ColPali, a multimodal document retrieval approach combining ColBERT with vision-language models.

### "Questions & Answer(s)" Blog Post (February 2024)
A reflective essay on the ML/NLP/IR ecosystem, the philosophy behind RAGatouille, and his decision to join Answer.AI. Key themes include the democratization of ML, the importance of open-source tooling, and bridging academia-industry gaps.

- **Link**: [ben.clavie.eu/posts/answer](https://ben.clavie.eu/posts/answer/)

## Blog / Recent Posts

| Date | Title | Link |
|---|---|---|
| Aug 2024 | JaColBERTv2.5: Optimising Retrieval Training for Lower-Resources Languages | [answer.ai](https://www.answer.ai/posts/2024-08-02-jacolbert-v25.html) |
| Feb 2024 | Questions & Answer(s): thoughts and joining Answer.AI | [ben.clavie.eu](https://ben.clavie.eu/posts/answer/) |
| Sep 2024 | Reducing the Footprint of Multi-Vector Retrieval via Token Pooling (paper) | [arXiv:2409.14683](https://arxiv.org/abs/2409.14683) |
| 2023 | JaColBERT: Towards better Japanese-first embeddings for retrieval | [arXiv report](https://arxiv.org/abs/2312.16104) |

Benjamin's personal blog at [ben.clavie.eu](https://ben.clavie.eu/) covers retrieval research, library updates, and broader thoughts on the ML ecosystem.

## Related People

- **Jeremy Howard** — Co-founder of Answer.AI, where Clavié works. Howard's fast.ai philosophy influenced Clavié's approach to making ML accessible.
- **Antoine Chaffin** — Co-author on the token pooling paper, collaborator at Answer.AI.
- **Griffin Adams** — Co-author on the token pooling paper at Answer.AI.
- **Benjamin Warner** — Co-lead on ModernBERT project.
- **Omar Khattab** — Creator of ColBERT; Clavié's work builds extensively on Khattab's research.
- **Clémentine Fourrier** ([[clefourrier]]) — Fellow Hugging Face ecosystem contributor working on evaluation; both focus on making advanced ML accessible.

## X Activity Themes

Clavié's X activity centers on:

- **Information Retrieval research** — Sharing and discussing new papers, particularly around late-interaction, dense retrieval, and reranking.
- **RAGatouille development** — Announcing updates, discussing philosophy, and engaging with user feedback.
- **Critique of dense embeddings** — Frequently arguing that ColBERT-style late-interaction outperforms dense embeddings for most real-world RAG use cases.
- **Japanese NLP** — Updates on JaColBERT development and Japanese retrieval benchmarks.
- **Open-source ML philosophy** — Advocacy for making research accessible, transparent training methodologies, and sharing full experimental results.
- **Life in Japan** — Occasional personal posts about living and working in Tokyo.
