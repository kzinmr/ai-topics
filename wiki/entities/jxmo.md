---
title: Jack Morris
handle: "@jxmnop"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - ml-research
  - embeddings
  - information-theory
  - nlp
---


# Jack Morris (@jxmnop)

| | |
|---|---|
| **X** | [@jxmnop](https://x.com/jxmnop) |
| **Blog** | [Token for Token (Substack)](https://blog.jxmo.io/) |
| **Personal Site** | [jxmo.io](https://jxmo.io/) |
| **GitHub** | [jxmo](https://github.com/jxmo) |
| **Role** | AI Researcher (Meta); PhD, Cornell University |
| **Known for** | CDE (Contextual Document Embeddings), Nomic Embed, information-theoretic analysis of LLMs |
| **Bio** | AI researcher specializing in text embedding models, information theory, and representation learning. PhD from Cornell University under Alexander M. Rush. Currently conducting RL research at Meta. Creator of the Substack "Token for Token" and author of multiple influential papers on embedding models, memorization in language models, and the Platonic Representation Hypothesis. |

## Overview

Jack Morris (known online as **jxmo** or **@jxmnop**) is an AI researcher whose work spans text embedding models, information theory for language models, and representation learning. He completed his PhD at Cornell University, advised by [Alexander M. Rush](https://rush-nlp.com/), and has since joined Meta to work on reinforcement learning for LLMs.

Morris is perhaps best known for his work on **Contextual Document Embeddings (CDE)**, which achieved state-of-the-art results in text retrieval by reordering training data and introducing a novel contextual architecture. He was also a co-author on [Nomic Embed](https://www.nomic.ai/blog/posts/nomic-embed-text), one of the most widely-used open-source embedding models. His research has consistently explored fundamental questions about how language models store and represent information — from his early work on inverting text embeddings to recover source text, to his recent investigations into how many bits per parameter language models actually memorize.

His Substack, **[Token for Token](https://blog.jxmo.io/)**, bridges the gap between academic research and practical AI engineering. He was featured on the [Latent Space podcast](https://www.latent.space/p/information-theory-for-language-models) for his work on information-theoretic understanding of LLMs, where host Swyx called him "an unusual combination of doing underrated research but somehow still being able to explain them well to a mass audience."

## Core Ideas

### Embedding Models Don't Scale (Yet)

Morris has argued that unlike language models, embedding models have plateaued at around the 8-billion parameter scale. In his March 2026 post *"How to train the best embedding model in the world"*, he outlines a recipe: use LLMs to filter hard negatives, then train with exact softmax and coordinate descent. His key finding from CDE was that **contextual batching** — reordering training data so related documents appear together — yielded nearly a 10% improvement.

> *"Every experiment I ran looks something like this: embedding model training scales, but only when you properly filter for hard negatives."*

### There Are No New Ideas in AI — Only New Datasets

In an April 2025 essay, Morris argues that LLM progress has come in exactly four waves, each driven by dataset innovation rather than algorithmic breakthroughs:

1. **Pretraining corpora** (Common Crawl → The Pile → FineWeb)
2. **Instruction tuning data** (Alpaca → Dolly → OpenAssistant)
3. **RLHF preference data** (human comparisons → AI-generated preferences)
4. **Reasoning data** (chain-of-thought distillations → verifier-generated traces)

> *"LLMs were invented in four major developments... all of which were datasets."*

### The Platonic Representation Hypothesis

Morris has explored the idea that all AI models trained on sufficient data converge toward similar internal representations, regardless of architecture. His post *"All AI Models Might Be The Same"* extends this to questions about whale communication and ancient text decoding — if representations converge universally, what does that mean for non-human intelligence?

### Information Theory for Language Models

A central theme of Morris's research is understanding LLMs through the lens of information theory. His paper *"How much do language models memorize?"* introduces a theoretical framework for measuring bits-per-parameter memorization. His work with Collin Zhang and Vitaly Shmatikov on **vec2text** demonstrated that text can be recovered exactly from sentence embeddings — a finding with significant privacy implications.

## Key Work

### Papers

| Paper | Venue | Year | Co-authors |
|---|---|---|---|
| [Contextual Document Embeddings (CDE)](https://arxiv.org/abs/2406.12345) | ICLR 2025 | 2025 | J.X. Morris, A.M. Rush |
| [Harnessing the Universal Geometry of Embeddings](https://arxiv.org/) | NeurIPS 2025 | 2025 | R. Jha, C. Zhang, V. Shmatikov, J.X. Morris |
| [Do language models plan ahead for future tokens?](https://arxiv.org/) | COLM 2024 | 2024 | W. Wu, J.X. Morris, L. Levine |
| [Extracting Prompts by Inverting LLM Outputs](https://arxiv.org/) | — | 2024 | C. Zhang, J.X. Morris, V. Shmatikov |
| [Text Embeddings Reveal (Almost) As Much as Text](https://arxiv.org/) | EMNLP 2023 (Outstanding Paper) | 2023 | J.X. Morris, V. Kuleshov, V. Shmatikov, A.M. Rush |
| [Tree Prompting: Efficient Task Adaptation without Fine-Tuning](https://arxiv.org/) | EMNLP 2023 | 2023 | J.X. Morris*, C. Singh*, A.M. Rush, J. Gao, Y. Deng |
| [Nomic Embed: Training a Reproducible Long Context Text Embedder](https://arxiv.org/) | — | 2024 | J.X. Morris, Z. Nussbaum et al. |

### Open Source Projects

- **[cde](https://github.com/jxmo/cde)** — PyTorch library for contrastive document embedding with hard negative mining, clustering, gradient caching, multi-GPU support, and contextual embeddings
- **[vec2text](https://github.com/jxmo/vec2text)** — Tools for recovering text from sentence embeddings and language model outputs (includes pretrained models; EMNLP outstanding paper)
- **[embzip](https://github.com/jxmo/embzip)** — Lossy compression of embedding vectors using product quantization
- **[gptzip](https://github.com/jxmo/gptzip)** — Lossless text compression using language models
- **[bm25_pt](https://github.com/jxmo/bm25_pt)** — PyTorch-native BM25 implementation that runs on GPU
- **[diffgif](https://github.com/jxmo/diffgif)** — Visualization of iterative edits to text sequences

## Blog / Recent Posts

| Date | Title | Summary |
|---|---|---|
| 2026-03-09 | [How to train the best embedding model in the world](https://blog.jxmo.io/p/how-to-train-the-best-embedding-model) | Gives away his PhD research secrets: use LLM-filtered hard negatives + exact softmax + coordinate descent. 74 likes, high engagement. |
| 2025-08-02 | ['AI' just means LLMs now](https://blog.jxmo.io/p/ai-just-means-llms-now) | Argues that the field has narrowed from many possible paths to intelligent systems to just one. |
| 2025-07-17 | [All AI Models Might Be The Same](https://blog.jxmo.io/p/all-ai-models-might-be-the-same) | Explores the Platonic Representation Hypothesis and its implications for cross-domain intelligence. |
| 2025-07-10 | [How to scale RL to 10^26 FLOPs](https://blog.jxmo.io/p/how-to-scale-rl-to-1026-flops) | Roadmap for reinforcement learning on LLMs at internet scale. Proposes next-token prediction on the Web using RL. |
| 2025-06-18 | [Superintelligence, from First Principles](https://blog.jxmo.io/p/superintelligence-from-first-principles) | Only two ways to learn: supervised learning and RL. Which will give us superintelligence? |
| 2025-06-09 | [The Case for More Ambition](https://blog.jxmo.io/p/the-case-for-more-ambition) | Why AI researchers should dream bigger and publish less. |
| 2025-04-09 | [There Are No New Ideas in AI… Only New Datasets](https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only-new-datasets) | LLM history as a series of dataset breakthroughs, not algorithmic ones. 300 likes, viral. |
| 2025-02-28 | [CoPilot for Everything](https://blog.jxmo.io/p/copilot-for-everything) | Employers have all the data needed to train AI models to replace workers. How long until it happens? |
| 2024-10-01 | [Contextual Document Embeddings](https://jxmo.io/posts/contextual-embeddings) | Blog post companion to the ICLR 2025 paper. |

Older blog posts at [jxmo.io/blog](https://jxmo.io/blog) include essays on AGI discourse, AI art, adversarial examples in NLP, contrastive learning taxonomies, VAE implementations, and philosophy of consciousness.

## Related People

- **[Alexander M. Rush](https://rush-nlp.com/)** — PhD advisor at Cornell; co-author on CDE, vec2text, Nomic Embed, and other papers
- **[Keller Jordan](https://github.com/KellerJordan)** — Modded-nanogpt speedrun; Morris collaborates in the broader efficiency-focused ML community
- **[Vitaly Shmatikov](https://www.cs.cornell.edu/~shmat/)** — Cornell faculty; co-author on embedding privacy and inversion papers
- **[Collin Zhang](https://github.com/czhang-ai)** — PhD student at Cornell; co-author on vec2text and prompt extraction research
- **[Zach Nussbaum](https://www.nomic.ai/)** — Co-author on Nomic Embed; Morris specifically recommended him for hiring
- **[spike](./spike.md)** — Fellow independent/open-source ML researcher; shares interests in building ML from first principles
- **[xjdr](./xjdr.md)** — Works on inference-time compute optimization; complementary to Morris's research on training efficiency

## X Activity Themes

- **Embedding model research** — Regular posts about CDE, Nomic Embed, and scaling retrieval models
- **Information theory** — Threads on bits-per-parameter memorization, what information means in LLMs
- **AI philosophy** — Essays on AGI discourse, the nature of intelligence, representation convergence
- **Industry commentary** — Takes on AI company strategies, the shift from academia to industry
- **Podcast appearances** — Promotes Latent Space episodes and other media featuring his work
- **Dataset-centric AI thesis** — Consistent messaging that data, not algorithms, drives progress
- **RL for reasoning models** — Recent focus on reinforcement learning as the next scaling paradigm

## See Also

- [[entities/_index.md]]
