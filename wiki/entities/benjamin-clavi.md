---
entity: benjamin-clavie
type: person
status: complete
aliases:
  - bclavie
  - Benjamin Clavié
tags:
  - nlp-researcher
  - information-retrieval
  - ml-researcher
  - colbert
  - ragatouille
  - open-source
  - japan-based
related:
  - colbert
  - ragatouille
  - modernbert
  - information-retrieval
  - natural-language-processing
---

# Benjamin Clavié

## Overview

Benjamin Clavié (@bclavie, b.clavie.eu) is a French NLP and information retrieval (IR) researcher based in **Tokyo, Japan**. He is the creator of **RAGatouille** (3.5k+ GitHub stars), the go-to library for ColBERT-based retrieval in Python, and a co-lead of **ModernBERT** (5.5k+ GitHub stars), a project that brought BERT-style encoders into modernity via architecture changes and scaling. He currently works at **Mixedbread** (Berlin, founded 2023), a company specializing in embedding and reranking models, and is also a PhD student at the **National Institute of Informatics (NII)** in Tokyo under Professor **Makoto P. Kato**. Clavié is the main organizer of the **Late Interaction Workshop series** at IR conferences and serves on the program committees of **CIKM** and **ECIR**. His work bridges academic rigor and production impact, consistently pushing lightweight retrieval models to SOTA performance with constrained compute budgets.

## Timeline

| Date | Event |
|------|-------|
| ~2017 | First research publication: "Employing machine learning techniques for detection and classification of phishing emails" (Computing Conference) |
| 2017–2018 | NLP Engineer at Biggerpan (Paris, France) — contributed to a research project exploring basic NLP applications to cybersecurity |
| 2018 | NLP Engineer / Data Science Animator at LexisNexis (Paris) — contributed to some of the first legal transformer-based language modeling work in French; put models in production in 2018 |
| 2018–2019 | Computing undergraduate studies at Edinburgh Napier University |
| 2019–2020 | MScR in AI at **University of Edinburgh**, School of Informatics |
| 2019-12 | Published "EduBERT: Pretrained Deep Language Models for Learning Analytics" at IEDM |
| 2020–2021 | Research and Teaching Assistant at University of Edinburgh under **Kobi Gal** |
| 2020-05 | Published "Deep Embeddings of Contextual Assessment Data for Improving Performance Prediction" at IEDM |
| 2021–2022 | Lead Data Scientist at **Jus Mundi** (LegalTech) — pre-trained domain-specific language models for international arbitration; secured a GENCI research GPU grant |
| 2021-09 | Published "LegaLMFiT: Efficient Short Legal Text Classification with LSTM Language Model Pre-Training" |
| 2021-09 | Published "The Unreasonable Effectiveness of the Baseline: Discussing SVMs in Legal Text Classification" at JURIX |
| 2022–2024 | Machine Learning Lead at **Bright Network** (Edinburgh, UK) — LLM-generated synthetic data for skill matching; 25-point Recall@5 improvement at RecSys |
| 2023-07 | Published "Large Language Models as Batteries-Included Zero-Shot ESCO Skills Matchers" at RecSys in HR workshop |
| 2023-03 | Published "Large Language Models in the Workplace: A Case Study on Prompt Engineering for Job Type Classification" at NLIS |
| 2023-12 | Published "JaColBERT: Optimising multi-vector retrievers to create state-of-the-art Japanese retrievers with constrained compute" — improved Japanese retrieval SOTA |
| 2023-12 | Created **RAGatouille** — Python library for ColBERT-based retrieval |
| 2024–2025 | Researcher at **Answer.AI** (co-led by Jeremy Howard) |
| 2024-05 | Began co-leading **ModernBERT** with Benjamin Warner and Antoine Chaffin at Answer.AI |
| 2024-08 | Published "Reducing the footprint of multi-vector retrieval with minimal performance impact via token pooling" |
| 2024-09 | Published "It's all in the [MASK]: Simple instruction-tuning enables BERT-like masked language models as generative" |
| 2024-12 | Published "Smarter, faster, longer: A modern bidirectional encoder for fast, memory efficient, and long context" (ModernBERT) — arXiv:2412.13663 |
| 2024-12 | Published "JaColBERTv2.5: Optimising multi-vector retrievers to create state-of-the-art Japanese retrievers" — SOTA on Japanese retrieval with ~130M params |
| 2025–present | Researcher at **Mixedbread** (Tokyo office) |
| 2025–present | PhD student at **National Institute of Informatics (NII)**, Tokyo, under **Makoto P. Kato** (Kasys lab) |
| 2025-04 | Published JaColBERTv2.5 in Journal of Natural Language Processing (vol. 32, pp. 176–218) |
| 2025 | Published "It is all in the [MASK]" in Natural Language Processing Journal (vol. 11, 100150) |
| 2025-10 | Published "Simple Projection Variants Improve ColBERT Performance" (arXiv:2510.12327) with Mixedbread team |
| 2025-10 | Published "Fantastic (small) Retrievers and How to Train Them: mxbai-edge-colbert-v0" (arXiv:2510.14880) |
| 2026-02 | Late Interaction Workshop at ECIR 2026 (organizer) |
| Ongoing | RAGatouille reaches 3.5k+ GitHub stars; 1,500+ HuggingFace downloads for ColBERT model |

## Core Ideas

**Retrieval is the bottleneck of practical AI.** Clavié's central thesis is that the retrieval layer — not the LLM — is the most impactful lever for real-world AI systems. Better retrieval means better RAG, which means better outcomes for everyone. His work on ColBERT, token pooling, and projection variants all aim to make retrieval models more accurate while using fewer resources.

**Lightweight models can outperform giants.** Clavié has repeatedly demonstrated that carefully-designed small models can beat larger ones on specific tasks. JaColBERT achieved SOTA for Japanese retrieval with ~130M parameters. The mxbai-edge-colbert-v0 series (17M and 32M params) pushes the boundaries of what tiny retrievers can do. ModernBERT showed that architectural changes + scaling can make BERT-style models competitive with much larger encoders.

**Synthetic data is a force multiplier.** From his Bright Network work showing that LLM-generated synthetic data for training first-stage retrievers "considerably outperformed all previous approaches to automated skills detection," to his broader research agenda, Clavié is a strong advocate for synthetic data strategies in IR. As he puts it, "synthetic data can solve all your problems" — when used correctly.

**Late interaction (MaxSim) is fundamentally powerful.** ColBERT's late-interaction architecture, which computes token-level similarity via MaxSim, is a recurring focus. Clavié's research on projection layers showed that "MaxSim has pretty cool learning properties" and that simple projection variants can significantly improve ColBERT performance. His work bridges the gap between ColBERT's theoretical elegance and its practical deployment.

**Open science and community building matter.** Clavié is not currently an academic but is affiliated with NII Tokyo and actively organizes the **Late Interaction Workshop series** at IR conferences. He serves on program committees of CIKM and ECIR. His philosophy: "It's important that we nurture an open IR community to see the same kind of growth experienced by NLP/Language Modeling."

**Production-first research.** Clavié's work at companies like LexisNexis, Jus Mundi, Bright Network, and Mixedbread grounds his research in real-world constraints. He has built scalable recommender systems and LLM-based RAG workflows serving 500k+ users daily. His approach: start with what works in production, then push the frontier.

## Key Quotes

> "I love figuring out ways that make the models work, so we can improve them."
> — On ColBERT projection layers research

> "Synthetic data can solve all your problems."
> — On LLM-generated data for retrieval model training (paraphrased from Bright Network case study)

> "I'm not, currently, an academic, although I am affiliated with the National Institute of Informatics (NII) in Tokyo. I think that it's important that we nurture an open IR community to see the same kind of growth experienced by NLP/Language Modeling."
> — On community building in Information Retrieval

> "MaxSim has pretty cool learning properties."
> — On ColBERT's late-interaction architecture

> "I'm the main organizer of the Late Interaction Workshop series at IR conferences."
> — On conference organization

> "We're trying to solve information retrieval."
> — On Mixedbread's mission

## Recent Themes

**Late-Interaction Research at Mixedbread (2025–Present):** Clavié leads research on ColBERT-family models at Mixedbread. Recent outputs include the mxbai-edge-colbert-v0 series (tiny retrievers at 17M and 32M params), projection variant improvements, and token pooling for reducing multi-vector retrieval footprints. These models achieve state-of-the-art results with dramatically smaller parameter counts.

**PhD at NII Tokyo (2025–Present):** Clavié is pursuing his PhD under Professor Makoto P. Kato in the Kasys lab at NII. His research focus spans information retrieval, encoder models, and language modeling.

**ModernBERT Co-Leadership:** As co-lead (with Benjamin Warner and Antoine Chaffin), Clavié helped deliver ModernBERT — a project that brought BERT-style masked language models into the modern era through architectural improvements and scaling. The work was published at NLPJ 2025 and has 5.5k+ GitHub stars on AnswerDotAI/ModernBERT.

**RAGatouille Ecosystem:** RAGatouille remains the standard Python interface for ColBERT-based retrieval. It is designed for "modularity and ease-of-use, backed by research." The library has 3.5k+ GitHub stars, 260+ forks, and is widely used in production RAG pipelines.

**Late Interaction Workshops:** Clavié is the main organizer of the Late Interaction Workshop series at IR conferences, including the first workshop at ECIR 2026. This series has become a focal point for researchers working on multi-vector retrieval, ColBERT, and related architectures.

**Japanese Language IR:** JaColBERT and JaColBERTv2.5 represent Clavié's sustained commitment to non-English retrieval optimization, achieving SOTA results for Japanese with constrained compute budgets. This work was published in the Journal of Natural Language Processing (2025).

## Influence Metrics

| Project | GitHub Stars | Language | Notes |
|---------|-------------|----------|-------|
| **RAGatouille** | 3,500+ | Python | Go-to library for ColBERT-based retrieval; 260+ forks |
| **ModernBERT** (co-lead) | 5,500+ | Python | Architecture changes + scaling for BERT-style models |
| **JaColBERTv2.5** | — | Python | SOTA Japanese retrieval with ~130M params |
| **ColBERT model on HuggingFace** | 1,500+ downloads | — | Primary ColBERT retriever model |

**Google Scholar Citations:**
- Total: ~1,000+ citations
- 2024: 725 citations
- 2023: 138 citations
- 2022: 50 citations
- 2021: 21 citations
- 2020: 49 citations

**Mixedbread GitHub Org:** 42 public repos, 226 followers. Top projects include mgrep (3.9k stars), baguetter (209 stars), batched (160 stars).

**Industry Impact:** Built RAG workflows serving 500k+ users daily at Bright Network; delivered 25-point Recall@5 SOTA improvement published at RecSys.

## Related Concepts

[[concepts/colbert]], [[concepts/ragatouille]], [[concepts/modernbert]], [[concepts/information-retrieval]], [[concepts/natural-language-processing]], [[concepts/rag]], [[concepts/embeddings]], [[concepts/token-pooling]], [[concepts/late-interaction]], [[concepts/synthetic-data]], [[concepts/mxbai-embed]], [[concepts/jacolbert]], [[entities/jeremy-howard]], [[entities/benjamin-warner]], [[entities/antoine-chaffin]], [[entities/makoto-kato]], [[entities/nathan-cooper]], [[entities/kobi-gal]], [[entities/griffin-adams]]

## Sources

- https://ben.clavie.eu/about/ — Personal site and about page
- https://github.com/bclavie — GitHub profile
- https://github.com/AnswerDotAI/RAGatouille — RAGatouille repository
- https://github.com/AnswerDotAI/ModernBERT — ModernBERT repository
- https://scholar.google.com/citations?user=vuMln98AAAAJ — Google Scholar profile
- https://openreview.net/profile?id=~Benjamin_Clavi%C3%A92 — OpenReview profile
- https://www.mixedbread.com/ — Mixedbread company site
- https://huggingface.co/mixedbread-ai — Mixedbread HuggingFace org
- https://www.mixedbread.com/blog/mxbai-embed-large-v1 — mxbai-embed-large-v1 blog post
- https://arxiv.org/abs/2412.13663 — ModernBERT paper
- https://arxiv.org/abs/2510.12327 — Simple Projection Variants Improve ColBERT Performance
- https://arxiv.org/abs/2510.14880 — Fantastic (small) Retrievers and How to Train Them
- https://arxiv.org/abs/2408.17344 — Token Pooling paper
- https://www.linkedin.com/in/benclavie — LinkedIn profile
- https://www.getprog.ai/profile/16307635 — Prog.AI profile
