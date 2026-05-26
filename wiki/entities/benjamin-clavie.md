---
title: Benjamin Clavié
type: entity
aliases: [bclavie, Ben Clavie]
created: 2026-04-10
updated: 2026-05-22
status: L3
sources:
  - https://ben.clavie.eu/
  - https://ben.clavie.eu/about/
  - https://ben.clavie.eu/posts/answer/
  - https://ben.clavie.eu/posts/sick/
  - https://ben.clavie.eu/ragatouille/
  - https://github.com/bclavie/RAGatouille
  - https://github.com/AnswerDotAI/ModernBERT
  - https://arxiv.org/abs/2412.13663
  - https://arxiv.org/abs/2510.12327
  - https://arxiv.org/abs/2510.14880
  - https://www.mixedbread.com/blog/edge-v0
  - https://parlance-labs.com/education/rag/ben.html
  - raw/articles/2026-05-20_clavie-tsukuba-ir-talk-colbert-late-interaction.md
related:
  - colbert
  - information-retrieval
  - late-interaction
  - token-pooling
  - synthetic-data
  - entities/jeremy-howard
  - entities/omar-khattab
  - entities/antoine-chaffin
  - entities/benjamin-warner
  - entities/makoto-kato
  - entities/griffin-adams
tags:
  - person
  - search
  - open-source

---

# Benjamin Clavié (@bclavie)

| | |
|---|---|
| **X** | [@bclavie](https://x.com/bclavie) |
| **Blog** | [ben.clavie.eu](https://ben.clavie.eu/) |
| **GitHub** | [bclavie](https://github.com/bclavie) |
| **Role** | ML Researcher at Mixedbread; PhD student at NII Tokyo (Kasys lab) |
| **Known for** | RAGatouille (3.9k★), ModernBERT co-lead, JaColBERT series, ColBERT projection research |
| **Bio** | French NLP/IR researcher based in Tokyo, Japan. Creator of RAGatouille, co-lead of ModernBERT. Bridges the gap between academic IR research and production-grade retrieval systems. Advocates for late-interaction (ColBERT) over single-vector dense embeddings. |

## Overview

Benjamin Clavié is a French NLP/Information Retrieval (IR) researcher currently based in **Tokyo, Japan**, working as an ML R&D researcher at **Mixedbread** and pursuing a PhD at the **National Institute of Informatics (NII)** Kasys lab (supervisor: Prof. Makoto P. Kato).

His notable contributions span three axes:
1. **RAGatouille** — A library making ColBERT-based search usable in just a few lines of Python (3.9k+ GitHub stars)
2. **ModernBERT** — Co-lead of the project rebuilding BERT-style encoder models with modern architecture (5.5k+ GitHub stars)
3. **JaColBERT series** — Multilingual ColBERT models achieving SOTA in Japanese retrieval

Clavié's philosophical position is clear: **"Retrieval is the bottleneck of practical AI."** He believes that the retrieval layer — not the LLM itself — determines the success or failure of real-world AI systems. His career is consistently dedicated to the practical application and democratization of IR research.

## Core Ideas

### 1. "RAG Is Not Dead" — Defending Naive RAG Criticism and True Retrieval

In his talk for Hamel Husain's Mastering LLM course, Clavié clearly distinguished between "RAG" as a marketing term and "Retrieval" as the underlying search technology.

> "RAG isn't going away. Naive methods (like basic cosine similarity) are showing their limits, pushing us toward better, more sophisticated retrieval techniques. RAG is the best way to provide models with up-to-date information. Long context windows are not a replacement for retrieval."
> — Hamel Husain's Mastering LLM course, P1: "I don't use RAG, I just retrieve documents"

His argument distills to three points:

- **Limits of single-vector search**: Compressing an entire document into one vector creates an information bottleneck
- **Giant context windows are not a replacement for search**: LLM weights are frozen at a point in time; they don't know about new internal documents or recent information
- **True retrieval should be multi-faceted**: Combine BM25, ColBERT, cross-encoders, and metadata filters

> "What people often call 'RAG' is a naive brute force, single-vector semantic search. This definition was pushed heavily by marketing in 2023-2024 because it was simple to sell."
> — On the "RAG is dead" narrative

### 2. ColBERT as a "Semantic Keyword Matcher"

Clavié succinctly expresses ColBERT's working principle in his own words:

> "I like to explain ColBERT as a `bag-of-embeddings` approach... Just like bag-of-words, it works on small information units, and represents a document as the sum of them... ColBERT is a semantic keyword matcher. It leverages the power of strong encoder models, like BERT, to break documents into token-level embeddings."
> — RAGatouille documentation, "Late-Interaction" section

This metaphor is important. Rather than viewing ColBERT as "a type of dense vector search," positioning it as **the semantic version of keyword search** provides an intuitive explanation for why late-interaction generalizes better than dense retrieval.

### 3. MaxSim Gradient Properties and Projection Layer Importance

In the 2025 arXiv paper "Simple Projection Variants Improve ColBERT Performance," Clavié systematically analyzed for the first time how ColBERT's MaxSim operator affects learning dynamics.

> "MaxSim has pretty cool learning properties."
> — On ColBERT's late-interaction architecture

> "Multi-vector dense retrieval methods like ColBERT systematically use a single-layer linear projection to reduce the dimensionality of individual vectors. In this study, we explore the implications of the MaxSim operator on the gradient flows of the training of multi-vector retrieval models."
> — arXiv:2510.12327 (2025)

Their finding was groundbreaking:
- Using FFN or GLU as projection layers improved **more than 2 NDCG@10 points** over linear projection
- MaxSim has unique gradient flow properties that can be amplified with proper projection design
- This improvement is achievable with no additional parameters

### 4. The "Small but Mighty" Philosophy

Clavié consistently advocates for "smarter design over giant models":

> "Our 17 million parameter model... comfortably outperforms ColBERTv2. And it does so while scaling exceptionally well across datasets and tasks, with an incredibly low memory footprint."
> — Mixedbread blog on mxbai-edge-colbert-v0 (2025)

His lightweight model philosophy rests on three principles:
1. **ModernBERT architecture efficiency** — unpadding + flash attention 2
2. **Minimal projection dimensionality** — 48 dimensions at 17M params (1/3 of conventional)
3. **Muon optimizer adaptation** — Effective for late-interaction models

### 5. ML Democratization and Ecosystem Problems

In his February 2024 blog post "Questions & Answer(s)," Clavié pointed out fundamental issues in the ML industry:

> "For a long time now, I've been of the opinion that the democratisation of ML has an ecosystem problem... ML as a whole rarely feels like pure research: to me, it's an R&D field, although with heavy emphasis on the D."
> — ben.clavie.eu/posts/answer/ (Feb 4, 2024)

> "To the end user, ML isn't an end, it's the means to one."
> — On the purpose of ML tooling

> "I think ML developments are incredibly exciting, and we need to continue to work on bridging the gap between ML-as-a-commodity-for-ML-practitioners to ML-as-a-commodity-for-everyone."
> — On the future of ML

This perspective is the foundation of his **RAGatouille philosophy**: "bridging the gap between state-of-the-art research and alchemical RAG pipeline practices."

### 6. Open Source as a Bridge Between Research and Development

Clavié's approach to open source resonates deeply with Jeremy Howard's Answer.AI philosophy:

> "I feel like the philosophy of Answer.AI is about as close to a perfect match to my own as you're going to get... We don't know much about what will come next, and even less about what the path forward looks like. What I do know for sure is that we need to tinker and try new things."
> — On joining Answer.AI (Feb 2024)

> "It's important that we nurture an open IR community to see the same kind of growth experienced by NLP/Language Modeling."
> — On the state of Information Retrieval

### 7. Token Pooling — Reducing Redundancy

> "The core idea of ColBERT, funnely enough, is to go against pooling as it's most commonly performed: into a single-vector. On the other hand, we believe that introducing a small degree of pooling could go a long way!"
> — Answer.AI blog, "A little pooling goes a long way for multi-vector representations"

> "Not all tokens are created equal... somewhat redundant semantic information, meaning keeping all of them is likely not useful."
> — On token pooling intuition (tf-idf analogy)

### 8. Health and Productivity — "Working While Sick" Philosophy

Clavié is unusually candid in the ML community about the relationship between health issues and productivity:

> "We all do stuff, and we all feel like it's not good enough. I think part of working well when you're unwell is accepting that, yeah, you're not gonna be 100% productive all the time."
> — ben.clavie.eu/posts/sick/

> "Everyone is struggling in some way. Every single person with major achievements definitely has periods where things go less smoothly, they're more tired, they're sick, things don't work. And from my experience and private chats, they, too, second-guess themselves."
> — On impostor syndrome and productivity

> "Do work. Put things out there. If it's not good, you'll learn, but eventually, you'll put something out there that is good."
> — Advice for working under constraints

## Timeline

| Date | Event |
|------|-------|
| ~2017 | First publication: "Employing ML techniques for detection and classification of phishing emails" |
| 2017–2018 | NLP Engineer at Biggerpan (Paris) — NLP × cybersecurity research |
| 2018 | NLP Engineer at **LexisNexis** (Paris) — French transformer-based legal language modeling; **put models in production in 2018** |
| 2018–2019 | Computing studies at Edinburgh Napier University |
| 2019–2020 | MScR in AI at **University of Edinburgh**, School of Informatics |
| 2019-12 | Published "EduBERT: Pretrained Deep Language Models for Learning Analytics" at IEDM |
| 2020–2021 | Research/Teaching Assistant at Edinburgh under **Kobi Gal** |
| 2021–2022 | Lead Data Scientist at **Jus Mundi** (LegalTech) — domain-specific LMs for international arbitration; secured GENCI GPU grant |
| 2022–2024 | ML Lead at **Bright Network** — LLM synthetic data for skill matching; 25pt Recall@5 improvement at RecSys |
| 2023-12 | Created **RAGatouille**; published JaColBERT |
| 2024-02 | Blog: "Questions & Answer(s)" — ML ecosystem philosophy |
| 2024-03 | Joined **Answer.AI** (co-led by Jeremy Howard) |
| 2024-05 | Began co-leading **ModernBERT** with Benjamin Warner & Antoine Chaffin |
| 2024-08 | Published token pooling research for ColBERT |
| 2024-08 | "Small but Mighty": answerai-colbert-small-v1 |
| 2024-12 | ModernBERT paper: arXiv:2412.13663 |
| 2024-12 | JaColBERTv2.5 published |
| 2025 | JaColBERTv2.5 in Journal of NLP (vol. 32, pp. 176–218) |
| 2025 | "It is all in the [MASK]" in Natural Language Processing Journal (vol. 11) |
| 2025–present | Researcher at **Mixedbread** (Tokyo office) |
| 2025–present | PhD student at **NII Tokyo**, Kasys lab (Prof. Makoto P. Kato) |
| 2025-10 | arXiv:2510.12327 — "Simple Projection Variants Improve ColBERT Performance" |
| 2025-10 | arXiv:2510.14880 — "Fantastic (small) Retrievers and How to Train Them: mxbai-edge-colbert-v0" |
| 2026-02 | Late Interaction Workshop at ECIR 2026 (main organizer) |
| 2026-03 | **Wholembed v3** released — the first semantic search model to surpass BM25 (LIMIT benchmark) |
| 2026-03 | Mixedbread Search Public Beta — agentic search support, sub-90ms search latency |
| 2026-03 | incompebench-lenient/strict datasets published |
| 2026 | Co-launched **"RAG Is Not Dead"** 7-part series with [[entities/hamel-husain|Hamel Husain]] — argued RAG is not dead, naive single-vector search is |
| 2026 | Presented **Part 1: "I don't use RAG, I just retrieve documents"** for Hamel Husain's Mastering LLMs course — the modern retrieval toolkit |
| 2026-05-20 | **Tsukuba IR Talk**: "ColBERT and Late Interaction Retrieval: Why, How, and What Next?" — comprehensive overview of IR paradigms, MaxSim mechanics, Single-Vector dilution ceiling, ViDoRe effect, oracle gap analysis (~12% tasks still wrong), and future directions (agentic redefinition of search, MaxSim instruction-following collapse, late interaction scaling). [[raw/articles/2026-05-20_clavie-tsukuba-ir-talk-colbert-late-interaction|slides]] |

## Recent Themes (2025–Present)

**Multimodal Search at Mixedbread:** Clavié currently leads R&D on "ever-better multimodal retrieval systems" at Mixedbread, working on image-text cross-modal search continuing the ColPali/ColQwen lineage.

**Edge ColBERT Frontier:** mxbai-edge-colbert-v0 (17M/32M params) is gaining attention as a practical ColBERT model even on CPU inference. Achieving superior performance to ColBERTv2 at 48 projection dimensions is a clear antithesis to the "bigger is better" paradigm.

**Wholembed v3 — Semantic Search Paradigm Shift (2026-03):** Clavié released the **first semantic search model to surpass BM25** at Mixedbread. It achieved Recall@5 of 92.45 on the LIMIT benchmark (BM25: 85.7, Voyage 4 Large: 1.85) — a groundbreaking result overturning the conventional wisdom that "semantic search has a hard ceiling." Wholembed v3 is an omnimodal (text, audio, image, video) late-interaction model supporting 100+ languages, now the default engine for Mixedbread Search. On BrowseComp-Plus (830 complex search queries), it dramatically reduced agent search failure rates.

> "We built Wholembed v3 to tackle current challenges, rather than simply improve on largely solved ones."
> "Search doesn't need to be complicated, it just needs to be good."
> "Retrieval is at the core of most agentic applications. For AI systems to be truly powerful, they need to be grounded in relevant knowledge."
> — Mixedbread Wholembed v3 release blog (March 2026)

**Mixedbread Search — Agentic Search Support (2026-03):** Traditional RAG assumes human-written queries, but Mixedbread Search is optimized for autonomous agent-driven searches (agentic search), achieving sub-90ms search latency and sub-120ms reranking. Also offers Vercel Native Integration.

**PhD Research:** Studying information retrieval, encoder models, and language modeling at NII Tokyo's Kasys lab under Prof. Makoto P. Kato (University of Tsukuba/NII).

**Late Interaction Workshop:** Organized the first Late Interaction Workshop at ECIR 2026, playing a role in building the ColBERT family research community.

**Tsukuba IR Talk (2026-05-20):** In "ColBERT and Late Interaction Retrieval: Why, How, and What Next?", Clavié provided a systematic overview of IR paradigms. Key insights: Single-Vector's limits lie not in the model itself but in the **scoring mechanism (cosine similarity)**; the Max component of MaxSim is the key to performance (SumSim/AvgSim collapses); ColBERT achieves comparable performance with one order of magnitude less data than single-vector (data efficiency); 0.13B ColBERT outperforms 8B single-vector models on BrowseComp-Plus. Open questions: oracle gap (even best retrieval ~12% of tasks still wrong), MaxSim instruction-following collapse, delayed large-scale contrastive pre-training (first appeared April 2026, standard for single-vector since 5 years ago). [[raw/articles/2026-05-20_clavie-tsukuba-ir-talk-colbert-late-interaction|slides]]

**Open-Source Toolchain:** Built an ecosystem covering the entire IR toolchain: RAGatouille → rerankers → byaldi → PyLate.

## Influence Metrics

| Project | Stars/Downloads | Significance |
|---------|----------------|-------------|
| **RAGatouille** | 3,900+ ★, 260+ forks | De facto standard for Python ColBERT retrieval |
| **ModernBERT** (co-lead) | 5,500+ ★ | Flagship of BERT modernization |
| **mxbai-embed-large-v1** | 22M+ downloads | Mixedbread's primary embedding model |
| **JaColBERTv2.5** | SOTA Japanese retrieval | SOTA at 130M params for Japanese retrieval |
| **ColBERT model (HF)** | 1,500+ downloads | Major ColBERT retriever |
| **Wholembed v3** | SOTA multimodal retrieval | LIMIT: Recall@5 92.45 (surpassing BM25) |
| **Google Scholar** | ~1,000+ citations (2024: 725) | Rapidly growing citation count |

## Key Quotes Collection

> "Bridging the gap between state-of-the-art research and alchemical RAG pipeline practices."
> — RAGatouille README

> "ML is infrastructure now, and it's infrastructure whose total addressable market is just about everyone."
> — Questions & Answer(s) blog (Feb 2024)

> "I'm not, currently, an academic, although I am affiliated with the National Institute of Informatics (NII) in Tokyo. I think that it's important that we nurture an open IR community to see the same kind of growth experienced by NLP/Language Modeling."
> — About page

> "We don't know much about what will come next, and even less about what the path forward looks like. What I do know for sure is that we need to tinker and try new things."
> — On joining Answer.AI

> "ColBERT has always been powerful, and used by specialists. RAGatouille's contribution has been to bridge the excellent Research work with the constraints of Development."
> — On RAGatouille's role (echoing Omar Khattab)

> "A funny example I have is my talk at Hamel's Mastering LLM course... I was second-guessing whether it was good enough right up until I delivered it."
> — On impostor syndrome (Working while sick)

> "Everyone with major achievements definitely has periods where things go less smoothly. They, too, second-guess themselves."
> — On the universality of struggle

## Related People

- **[[concepts/jeremy-howard]]** — Answer.AI co-founder. Clavié joined in 2024. Heavily influenced by fast.ai philosophy
- **[[entities/omar-khattab]]** — ColBERT/DSPy inventor (Stanford). Direct inspiration for Clavié's ColBERT research
- **[[concepts/benjamin-warner]]** — ModernBERT co-lead, fastkmeans co-author
- **[[concepts/antoine-chaffin]]** — ModernBERT co-lead, PyLate developer
- **[[concepts/makoto-kato]]** — Clavié's PhD supervisor (NII Tokyo/Kasys lab)
- **[[concepts/griffin-adams]]** — ColBERT token pooling co-author
- **[[concepts/rikiya-takehi]]** — mxbai-edge-colbert-v0 first author (Waseda Univ/Mixedbread intern)
- **[[concepts/xianming-li]]** — Mixedbread/Wholembed v3 co-author, ECIR 2026 LIR Workshop co-organizer
- **[[tom-aarsen]]** — Hugging Face, PyLate contributor, ECIR 2026 LIR Workshop co-organizer

## Related Concepts

[[concepts/colbert]], [[concepts/ragatouille]], [[concepts/modernbert]], [[concepts/information-retrieval]], [[late-interaction]], [[concepts/token-pooling]], [[concepts/synthetic-data]], [[concepts/rag-not-dead-series]], [[concepts/modern-retrieval-toolkit]],

## Sources

- https://ben.clavie.eu/ — Personal blog
- https://ben.clavie.eu/about/ — About page (detailed project list)
- https://ben.clavie.eu/posts/answer/ — "Questions & Answer(s): thoughts and joining Answer.AI" (Feb 2024)
- https://ben.clavie.eu/posts/sick/ — "Working while sick" (personal philosophy on health/productivity)
- https://ben.clavie.eu/ragatouille/ — RAGatouille documentation and philosophy
- https://github.com/bclavie/RAGatouille — RAGatouille repository (3,900+ ★)
- https://github.com/AnswerDotAI/ModernBERT — ModernBERT repository (5,500+ ★)
- https://arxiv.org/abs/2412.13663 — ModernBERT paper (Dec 2024)
- https://arxiv.org/abs/2510.12327 — Simple Projection Variants Improve ColBERT Performance (Oct 2025)
- https://arxiv.org/abs/2510.14880 — Fantastic (small) Retrievers and How to Train Them: mxbai-edge-colbert-v0 (Oct 2025)
- https://www.mixedbread.com/blog/edge-v0 — mxbai-edge-colbert-v0 blog post
- https://parlance-labs.com/education/rag/ben.html — Mastering LLMs talk transcript
- https://www.answer.ai/posts/colbert-pooling.html — Token pooling blog post
- https://huggingface.co/bclavie — HuggingFace profile (72 followers, 53 models)
- https://scholar.google.com/citations?user=vuMln98AAAAJ — Google Scholar profile
- https://mixedbread.com/blog/wholembed-v3 — Wholembed v3 release blog (March 2026)
- https://www.lateinteraction.com/ — Late Interaction Workshop @ ECIR 2026 (main organizer)
- https://mixedbread.ai/changelog — Mixedbread platform changelog
- https://hamel.dev/notes/llm/rag/not_dead.html — "Stop Saying RAG Is Dead" — co-launched 7-part series with Hamel Husain (2026)
- https://hamel.dev/notes/llm/rag/p1-intro.html — "P1: I don't use RAG, I just retrieve documents" — Part 1 presentation (2026)
