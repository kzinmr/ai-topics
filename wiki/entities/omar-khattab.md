---
title: "Omar Khattab"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---

# Omar Khattab (@lateinteraction)

**Position:** Assistant Professor, MIT EECS (TIBCO Founders' Career Development Professor)

**Affiliation:** CSAIL, AI+D

**Domain:** Information Retrieval, NLP, ML Systems, Foundation Model Programming

**Core Thesis:**
> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."*
> — Omar Khattab, PhD Dissertation (Stanford, 2024)

---

## Profile

Omar Khattab is an Assistant Professor at MIT EECS, where he joined in July 2025. His research creates **models, systems, supervision strategies, and programming abstractions** for building reliable, transparent, and scalable NLP systems. He is the creator of **ColBERT** (the late interaction retrieval paradigm), **DSPy** (declarative foundation model programming), **GEPA** (genetic-pareto prompt evolution), and co-author of **RLMs** (Recursive Language Models).

**Background:**
- **PhD in Computer Science, Stanford University (2019–2024)**, advised by **Christopher Potts** and **Matei Zaharia**
  - Dissertation: *"Building More Reliable and Scalable AI Systems with Foundation Model Programming"*
- **BS in Computer Science (Minor: Math), Carnegie Mellon University in Qatar (2015–2019)**, advised by Mohammad Hammoud
- Apple PhD Scholar in AI/ML Fellowship (2022–2024)
- Eltoukhy Family Graduate Fellowship (2019–2020)
- Research Intern at Apple AI/ML (2022), advised by Dr. Ruoming Pang (Distinguished Engineer)
- Research Scientist at Databricks (June 2024–June 2025)
- SIGIR 2025 Best Paper Award (WARP, last author)

---

## ColBERT: Late Interaction Retrieval (2020–2022)

ColBERT is Khattab's most influential contribution to information retrieval — introducing the **late interaction** paradigm that balances efficiency and quality in neural search.

### The Core Innovation

Instead of encoding queries and documents into single vectors (as in standard dense retrieval), ColBERT:
1. **Independently encodes** queries and documents into sets of contextual token embeddings using BERT
2. **Performs fine-grained token-level interaction** using cheap MaxSim operations at query time
3. **Leverages vector-similarity indexes** for end-to-end retrieval from large collections

> *"By delaying and yet retaining fine-granular interaction, ColBERT leverages the expressiveness of deep LMs while keeping the cost of query processing low."*
> — ColBERT paper (SIGIR 2020)

### Key Papers
| Paper | Venue | Contribution |
|-------|-------|--------------|
| **ColBERT** | SIGIR 2020 | Original late interaction architecture |
| **ColBERTv2** | NAACL 2022 | Lightweight late interaction via distillation |
| **PLAID** | CIKM 2022 | Efficient engine for late interaction retrieval (co-first with Santhanam) |
| **WARP** | SIGIR 2025 | Efficient multi-vector retrieval engine (🏆 Best Paper) |
| **ColBERT-serve** | ECIR 2025 | Multi-stage memory-mapped scoring for production scale |

### Impact
- ColBERT's late interaction paradigm has become the de facto standard for multi-vector retrieval
- 500,000+ monthly downloads across open-source implementations
- Used by Google, Amazon, IBM, VMware, Databricks, Baidu, and numerous startups
- Spawned derivative architectures (ColPali, ColBERT-Multilingual, etc.)

---

## DSPy: Declarative Foundation Model Programming (2022–present)

DSPy is Khattab's framework that replaces ad-hoc prompt engineering with composable, optimizable LM programs.

### Philosophy

> *"It's actually better to think of language models as modules in programs, not end products."*
> — Omar Khattab, Cohere talk (2024)

DSPy treats LMs as **learnable modules** in a computational graph:
1. **Define** a program with LM modules (Chain of Thought, ReAct, program-level reasoning)
2. **Specify** a metric for evaluation
3. **Optimize** the prompts (or fine-tune weights) automatically using built-in optimizers

### Key Insight
DSPy unifies prompting, fine-tuning, and retrieval-augmented generation under a single programming model. Small models (T5, <1B parameters) expressed in DSPy routinely outperform large standalone LMs with hand-crafted prompts.

### Open-Source
- PyPI packages: `dspy`, `dspy-ai`
- GitHub: stanfordnlp/dspy
- 500,000+ monthly downloads

---

## GEPA: Genetic-Pareto Prompt Optimization (2025)

**Paper:** *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*

GEPA introduces a **genetic algorithm** approach to prompt optimization that uses the LLM's own reasoning to evolve prompts:
- Parents are selected via Pareto optimality (balancing multiple objectives)
- Offspring are generated through LLM-based reflection and mutation
- Outperforms reinforcement learning-based prompt optimization on several benchmarks

This work sits at the intersection of Khattab's interests in **programmatic control** and **automated optimization** of LM behavior.

---

## RLM: Recursive Language Models (2025–2026)

**Co-authors:** Alex L. Zhang, Tim Kraska, Omar Khattab
**Paper:** arXiv:2512.24601 (Dec 2025, revised Jan 2026)
**Code:** [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm)
**Ecosystem:** DSPy v3.1.2+ ships built-in RLM support; Google ADK has enterprise-ready implementation

RLMs represent Khattab's latest contribution — an **inference-time scaling paradigm** that allows LMs to process arbitrarily long prompts by treating context as an external variable in a REPL environment.

### Khattab's Role
As co-author and PhD advisor to Alex Zhang, Khattab provided the theoretical foundation for treating **context as an environment** rather than a fixed prompt. This connects directly to his broader thesis of **foundation model programming** — LMs should be programmable components, not monolithic text processors.

### The Deep Insight
Khattab framed RLMs' core contribution on X:

> *"Most people misunderstand RLMs to be about LLMs invoking themselves. The deeper insight is LLMs interacting with their own prompts as objects."*
> — Omar Khattab (@lateinteraction), 2026

This reframes RLMs from mere recursive calling to **context-as-data** manipulation. The model doesn't just call itself — it writes code to examine, filter, chunk, and selectively expose parts of its input. This is an **out-of-core algorithm design** pattern applied to language models.

### RLM as the Culmination of Khattab's Research Program

| Phase | Framework | What it delays | Why it matters |
|-------|-----------|---------------|----------------|
| **Phase 1** | ColBERT | Interaction (token-level matching) | Quality without compute at index time |
| **Phase 2** | DSPy | Prompt design (optimization) | Declarative programs over ad-hoc prompts |
| **Phase 3** | RLMs | Context consumption (selective reading) | Models manage what they see and when |

The through-line across all three: **architectural flexibility over brute-force scaling.** Don't make the model bigger — make the architecture smarter about when and how the model engages with information.

### Benchmark Results (MIT OASYS Lab)
- **RLM(GPT-5-mini)** outperforms GPT-5 by >34pts on OOLONG (132k context)
- **RLM-Qwen3-8B** beats base Qwen3-8B by 28.3% average across 4 benchmarks
- **BrowseComp-Plus:** perfect performance at 1000 documents (10M+ tokens)
- **Cost:** RLM runs are comparable to or cheaper than base model calls (median)
- **Scale:** effectively processes 10M+ token inputs — 100× beyond native context windows

### Connection to Shunyu Yao's "The Second Half"
Both Khattab/Zhang's RLM framework and Yao's RL generalization thesis converge on the same insight:

> *"In RL, there are three key components: algorithm, environment, and priors. For a long time, RL researchers focused on the algorithm... but the algorithm is the trivial part."*
> — Shunyu Yao, "The Second Half" (2025)

Khattab's RLM makes the **environment** (the REPL, the context-as-data) the focus, not the model architecture. Yao's work makes the **environment design** (Agent-Computer Interfaces) the focus, not the RL algorithm. Both argue that **how we structure the interaction** matters more than the raw capability of the model.

### Prime Intellect's Assessment
> *"Teaching models to manage their own context end-to-end through reinforcement learning will be the next major breakthrough in AI inference."*
> — Prime Intellect on RLMs (Jan 2026)

This connects Khattab's inference-time scaffolding with Yao's RL-first worldview: the next step is training models natively to use RLM patterns rather than wrapping them in a scaffold.

---

## Baleen & Retrieval-Augmented Reasoning (2021–2022)

**Paper:** *Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval* (NeurIPS 2021 Spotlight)

Baleen introduced a **condensed retrieval** approach where LMs retrieve evidence in stages, condensing previously-retrieved information to inform subsequent retrieval steps. This work presaged modern agentic RAG patterns and demonstrated that retrieval and reasoning could be interleaved effectively.

---

## Research Trajectory

### Phase 1: Neural Information Retrieval (2019–2022)
- ColBERT, ColBERTv2, PLAID
- Multi-hop retrieval (Baleen)
- Relevance-guided supervision for open QA
- *Theme:* How do we make deep LMs efficient for search?

### Phase 2: Foundation Model Programming (2022–2024)
- DSPy: composable, optimizable LM modules
- DSPy optimizers (teleprompters)
- Industry adoption at scale
- *Theme:* How do we program LMs systematically rather than prompting ad-hoc?

### Phase 3: Inference-Time Scaling (2025–)
- RLMs: recursive context processing
- GEPA: genetic prompt evolution
- Multi-module GRPO
- *Theme:* How do we scale LM capabilities at inference time without training larger models?

---

## Key Publications

| Year | Title | Venue | Role |
|------|-------|-------|------|
| 2026 | Recursive Language Models | arXiv | Co-author |
| 2025 | Multi-module GRPO | arXiv | Co-author |
| 2025 | GEPA: Reflective Prompt Evolution | arXiv | Co-author |
| 2025 | WARP: Efficient Multi-Vector Retrieval | SIGIR 2025 (Best Paper) | Last author |
| 2025 | ColBERT-serve | ECIR 2025 | Co-author |
| 2025 | FreshStack: Realistic Retrieval Benchmarks | arXiv | Co-author |
| 2025 | LangProBe: Language Programs Benchmark | arXiv | Co-author |
| 2024 | Grounding by Trying (RL-Enhanced Retrieval) | ICLR 2025 | Co-author |
| 2024 | DSPy | (various) | Creator |
| 2022 | PLAID: Efficient Late Interaction | CIKM 2022 | Co-first |
| 2022 | ColBERTv2 | NAACL 2022 | Co-first |
| 2022 | Demonstrating-Search-Predict | arXiv | Creator |
| 2021 | Baleen: Condensed Retrieval | NeurIPS 2021 (Spotlight) | First author |
| 2020 | ColBERT | SIGIR 2020 | First author |

---

## Relationships & Collaborations

**Advisees:**
- **Alex L. Zhang** — PhD student at MIT CSAIL, first author of RLMs

**PhD Advisors (Stanford):**
- **Christopher Potts** — NLP, semantics, pragmatics
- **Matei Zaharia** — Spark creator, ML systems

**Key Collaborators:**
- **Keshav Santhanam** — ColBERTv2, PLAID (co-first author)
- **Simran Arora** — KernelBench
- **William Hu** — GPU MODE

**Industry Connections:**
- Apple AI/ML (2022 intern)
- Databricks (2024–2025 research scientist)

---

## Impact Metrics

- **ColBERT:** Shaped modern multi-vector retrieval; 500,000+ monthly downloads across implementations
- **DSPy:** Most widely used declarative LM programming framework
- **PyPI Packages:** 7 packages (`rlms`, `dspy-ai`, `dspy`, `colbert-ai`, `RAGatouille`, `dspy-ml`, `dsp-ml`)
- **Awards:** SIGIR 2025 Best Paper, Apple PhD Scholar, Eltoukhy Family Graduate Fellowship
- **Industry Adoption:** Google, Amazon, IBM, VMware, Databricks, Baidu, AliExpress

---

## Philosophy: Decomposition at the Right Joints

In 2026, Khattab articulated the unifying philosophy across all four of his major research contributions — a direct response to "bitter lesson maximalists" who believe only scale and compute matter:

> *"A subtle thing that's worth observing is how all four are actually riffs on the same fundamental concept: decomposing something that the mainstream paradigm insists as treating as a monolith."*
> — Omar Khattab (@lateinteraction), 2026

The four "riffs" on decomposition:

| Framework | What it Decomposes | Monolith it Replaces | Longevity |
|-----------|-------------------|---------------------|-----------|
| **Late Interaction (ColBERT)** | Document representations → sets of objects; similarity → compositional operations | Single-vector dense embeddings | 6.5+ years (2020–present) |
| **DSPy** | Specification vs optimization; AI programs → symbolic modules with NL specs | Monolithic prompt debt | 3.5+ years (2023–present) |
| **GEPA** | Learning signals → actual tokens + feedback (not scalar rewards) | Policy gradient RL rewards | Emerging (2025) |
| **RLMs** | Hard problems → symbolic programs that invoke models; context → recursive access | Monolithic attention over massive contexts | Emerging (2025) |

### Against Bitter Lesson Maximalism

Khattab explicitly argues that decomposition, when done correctly, is **compatible with scaling** — not opposed to it:

> *"I guess I failed to make that clear, but this is a post against the naive bitter lesson maximalists. You *can* and in fact *need* to win with decomposition. It's not against scale and does not need to expire with time. It's what enables scaling to go beyond brute force."*
> — Omar Khattab, X post (2026)

The key insight: **decomposition done poorly runs foul of the bitter lesson** (Sutton, 2019), but decomposition done at the *right fundamental joints* enables scaling to transcend brute force. All four of Khattab's frameworks have endured (6.5 years for ColBERT, 3.5 for DSPy) precisely because they decompose at natural architectural boundaries rather than imposing artificial structure.

This philosophy connects directly to his PhD thesis: *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."*

### Connection to Harness Engineering

Khattab's decomposition philosophy aligns with Anthropic's Harness Engineering principle: **design the right scaffolding, don't just scale the model**. Both approaches recognize that the bottleneck is often *how we structure the interaction* between components, not the raw capability of any single component.

---

## Key Quotes

> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."*
> — Omar Khattab, PhD Dissertation

> *"It's actually better to think of language models as modules in programs, not end products."*
> — Omar Khattab, Cohere talk (2024)

> *"DSPy takes a different approach: we say it's actually better to think of language models as procedures — as functions — and build a programming model around that."*
> — Omar Khattab, on DSPy vs. prompt engineering

---

## See Also

- [[concepts/rlms]] — Recursive Language Models (co-author)
- [[alex-zhang]] — PhD student, RLM first author
-  — Late interaction retrieval (creator)
- [[concepts/dspy]] — Declarative LM programming (creator)
- [[concepts/gepa]] — Genetic-Pareto prompt optimization (creator)
-  — RLM co-author, MIT CSAIL databases/ML systems
