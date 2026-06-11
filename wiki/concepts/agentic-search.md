---
title: Agentic Search
created: 2026-04-30
updated: 2026-06-09
type: concept
tags:
  - search
  - ai-agents
  - coding-agents
  - training
  - methodology
aliases:
  - deep-research-retrieval
  - agent-query-mismatch
  - externalized-processing
  - agentic-retrieval
sources:
  - raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams
  - raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md
  - raw/articles/2026-03-26_daniel-tunkelang_agentic-search-agile-engineering.md
  - raw/articles/2026-03-24_hornet_deep-research-is-a-retrieval-problem.md
  - raw/papers/2026-02-25_2602.21456_revisiting-text-ranking-in-deep-research.md
  - raw/papers/2026-03-20_2603.20432_coding-agents-effective-long-context-processors.md
  - raw/articles/2025-12-04_sid-1-agentic-retrieval.md
  - raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents.md
  - raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai.md
  - raw/articles/2026-04-06_softwaredoug-agentic-search-grep-moment.md
  - raw/articles/2026-04-21_softwaredoug_dont-waste-time-on-rag-paradigm.md
  - raw/articles/2026-02-17_anthropic_dynamic-filtering-web-search.md
  - raw/articles/2026-03-30_claude-web-search-dynamic-filtering.md
  - raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack.md
  - raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search.md
  - raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level.md
  - transcripts/2026-01-23_vanishing-gradients_ep68-builders-guide-agentic-search.md
  - raw/articles/2025-11-02_softwaredoug_llm-judges-arent-the-shortcut.md
  - raw/papers/2026-05-28_2603.04384_agentir-reasoning-aware-retrieval.md
  - raw/papers/2026-05-03_2605.05242_direct-corpus-interaction.md
  - raw/articles/2026-06-08_softwaredoug_three-kinds-of-agentic-search.md
  - https://arxiv.org/abs/2603.04384
  - https://arxiv.org/abs/2602.21456
  - https://arxiv.org/abs/2603.20432
  - https://www.sid.ai/research/sid-1-technical-report
  - https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment
  - https://claude.com/blog/improved-web-search-with-dynamic-filtering
  - https://www.gend.co/blog/claude-web-search-dynamic-filtering
  - https://softwaredoug.com/blog/2026/04/28/search-apis-replaced-by-agents.html
  - https://www.youtube.com/watch?v=OGnW2Pu2uVE
  - https://github.com/ChuanMeng/text-ranking-in-deep-research
---

# Agentic Search

> Agentic search encompasses the retrieval strategies and text ranking methods used by LLM-powered agents to search the web, find relevant information, and power deep research workflows. It spans both the **IR research perspective** (how to optimize retrieval for agent-issued queries) and the **harness engineering perspective** (how to design skill/tool discovery for agents).

## Definition

**Agentic Search** refers to the retrieval systems and strategies that AI agents use to discover relevant information. It operates at two distinct levels:

### Level 1: IR/Retrieval Layer (Search Engine Interaction)
How agents query web search engines or fixed corpora to find relevant documents. This is the classical IR problem adapted for agent-driven query patterns.

### Level 2: Skill/Tool Discovery (Agent Harness Layer)
How agents discover which capabilities, skills, or tools are relevant to the current task — loading only what's needed into context to avoid token waste.

---

### Entry Point: The Paradigm Shift Manifesto (Turnbull, April 2026)

Doug Turnbull's LinkedIn post *\"Don't waste too much time on the original RAG paradigm\"* [[raw/articles/2026-04-21_softwaredoug_dont-waste-time-on-rag-paradigm]] serves as a concise entry point to understand the **paradigm shift from RAG to agentic search**. It distills the key argument into a condensed manifesto:

1. **RAG was retrieval-centric** — complexity lived in query understanding, routing, multi-strategy retrieval, combining+reranking, and statistics aggregation. This grew into a monolithic "thicc daddy" search system — exactly what the industry has built for decades.
2. **Agentic search is harness-centric** — complexity moves to the agent+harness, which reasons about search results, reflects on irrelevance, and iteratively reformulates queries. The retrieval backends can be "dumb" (BM25, grep).
3. **The progression**: structured attributes → tool calling → reasoning → scaffold+tools (SID-1, semantic grep). Each step reduces the need for complex retrieval infrastructure.
4. **Practical advice**: Start with the dumbest thing that can work, with the simplest data system. Don't overbuild until you have data that shows where an agent cannot cope.

The post's notable comments capture key tensions:
- **Efficiency concern** (Gayhart): Dumb retrievers mean more tool calls — isn't that wasteful? Turnbull's response: fastest path to value is simple tools → user-driven roadmap.
- **Retrieval quality still matters** (Boytsov): Core retrieval value remains high — not an either/or.
- **User behavior** (Pickens): If users won't enter queries longer than 2.3 keywords, does agentic search help? Raises the question of human agency in agentic search.

This framing is developed in greater depth across Turnbull's blog series ([[raw/articles/2026-04-06_softwaredoug-agentic-search-grep-moment]], [[raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack]]), the Amazon ESCI benchmark results below, and Berryman's 5-level maturity model.

---

## Level 1: IR Research Perspective

A landmark 2026 study by Meng, Ou, MacAvaney, and Dalton (University of Glasgow) systematically evaluated IR text ranking methods for deep research agents, revealing critical design insights.

### The Query Mismatch Problem

Agent-issued queries differ fundamentally from the natural language queries used to train neural rankers. Deep research agents produce **web-search-style keyword syntax** — using quotes for exact matches, Boolean operators, and fragmented terms — while neural rankers (dense retrieval models like RepLLaMA, Qwen3-Embed) are trained on complete natural language questions.

This mismatch means that **lexical (BM25), learned sparse (SPLADE-v3), and multi-vector (ColBERTv2) retrievers outperform standard dense retrievers** in agentic search contexts.

This academic finding echoes a practitioner argument Turnbull made months earlier in *"RAG Users Want Affordances, Not Vectors"* [[raw/articles/2025-12-09_doug-turnbull-rag-users-want-affordances]] — embedding crowding, the threshold problem, and in-domain nuance all make dense vectors unreliable for agent-driven queries. The academic IR community caught up to what search engineers had already discovered in production.

### Key Findings

| Component | Recommendation | Evidence |
|-----------|---------------|----------|
| **Retrieval Unit** | **Passages** (~250 words) | More search/reasoning iterations before hitting context limits |
| **Base Retriever** | **BM25** (with $b=1.0$) or **SPLADE-v3/ColBERTv2** | SPLADE-v3 + Q2Q achieves 7.95% accuracy gain |
| **Re-ranking** | Implement with depth ≥ 50 | BM25–monoT5-3B reaches 0.716 recall / 0.689 accuracy |
| **Query Processing** | **Q2Q Reformulation** | Translate keywords → natural language questions using agent reasoning trace |
| **Document Access** | "Full-Document Reader" tool | Let agent retrieve full docs on-demand when evidence found in passages |

### Query-to-Question (Q2Q) Reformulation

A key innovation: using the agent's own **reasoning trace** as context to reformulate keyword queries into natural language questions.

```
Raw agent query: "61,880" football attendance
→ Reasoning trace: "The user asked about the highest attendance"
→ Q2Q: "What football match had an attendance of 61,880?"
```

This yields a **7.95% relative accuracy gain** for SPLADE-v3 neural retrieval.

### Reasoning-Aware Joint Embedding: AgentIR (March 2026)

While Q2Q translates reasoning → natural language query as a **separate preprocessing step** (pipeline architecture), Chen et al. (2026) go further with [[concepts/reasoning-aware-retrieval|AgentIR]]: **jointly embed** the reasoning trace alongside the query in a single trained embedding model. This collapses Q2Q's two-step pipeline into one embedding step.

The paradigm shift: instead of R(q_t), use R(τ_t, q_t) — the retriever sees both the agent's reasoning and the query. The reasoning trace provides three signal types: (1) task intent (disambiguating keyword queries), (2) reflection on prior results (avoiding re-search), and (3) hypothetical search targets (grounded HyDE alternative).

**AgentIR-4B** (fine-tuned Qwen3-Embedding-4B) achieves **68.07% accuracy** on BrowseComp-Plus vs. 50.72% for Qwen3-Embedding-8B — **double the accuracy gain of Q2Q**, with **half the parameter count**. Critically, it generalizes across different agent models (Tongyi-DR, oss-120b, GLM-4.7) without retraining, and reduces search calls by ~20%.

The training enabler is **DR-Synth**, a data synthesis pipeline that converts standard (Q, A, P) QA triples into sub-query-level training instances via agent rollouts + oracle reranking. Key design insight: **joint embedding outperforms pipeline architecture** — training the retriever to internalize the reasoning/query relationship is more effective than separating translation and retrieval into discrete steps.

|| Approach | Architecture | Accuracy | Params |
||----------|-------------|----------|--------|
|| BM25 (baseline) | Lexical | 33.98% | — |
|| Q2Q Reformulation | Pipeline: translate → retrieve | ~57.9% (rel. +8%) | 8B |
|| Q2Q + LLM Rerank | Pipeline + reranker | 55.66% | 4B + 8B reranker |
|| **AgentIR-4B** | **Joint embedding** | **66.27–68.07%** | **4B** |

> **Connection to Q2Q**: Q2Q Reformulation (Meng et al.) is a preprocessing technique — it converts agent reasoning into a natural language query for any off-the-shelf retriever. AgentIR (Chen et al.) is a **retriever co-design** approach — it trains the embedding model to natively understand reasoning traces. Both exploit the same free signal, but AgentIR achieves 2.3× the accuracy gain by eliminating the information loss at the pipeline boundary.

Sources: [[raw/papers/2026-05-28_2603.04384_agentir-reasoning-aware-retrieval|AgentIR paper]], [Project page](https://texttron.github.io/AgentIR/)

A two-stage pipeline significantly outperforms single-stage retrieval:

```
Agent Keyword Query
        ↓
  BM25 Retrieval (top-50)
        ↓
  monoT5 Re-ranker (depth=50)
        ↓
  Top-10 passages → Agent Context
```

This BM25–monoT5-3B configuration approaches **GPT-5-level agent performance** at a fraction of the inference cost.

### Why Reasoning Re-rankers Underperform

Reasoning-based re-rankers (e.g., Rank1-7B) showed **no clear advantage** over standard re-rankers. They often misinterpret keyword-heavy agent queries as genuine reasoning problems rather than search retrieval requests.

### RL-Trained Agentic Retrieval: SID-1

SID-1 (SID AI, December 2025) is the first model trained end-to-end via RL specifically for **agentic retrieval**. Built on Qwen3-14B with modified GRPO (no SFT), it iteratively uses search tools to reason over results — a concrete implementation of agentic search at the IR level.

| Model | Recall | Latency | Cost/Query |
|-------|--------|---------|-----------|
| **SID-1 (4x)** | **0.84** | 5.5s | $0.0014 |
| GPT-5.1 (high) | 0.78 | 131s | $0.24 |
| Gemini 3 Pro | 0.66 | 156s | $0.12 |
| Sonnet 4.5 | 0.64 | 35s | $0.54 |
| Reranker @10 | 0.45 | 0.78s | $0.00061 |

SID-1 achieves **near-doubled recall** over traditional reranking pipelines while being **24× faster than GPT-5.1** and **374× cheaper than Sonnet 4.5**.

#### Training Design Insights

**Document-Centric Reward:** Unlike Search-R1 or SimpleQA, SID-1 is rewarded for finding the **correct documents** (NDCG), not the answer. This discourages over-reporting while preferring slight over-reporting over missed documents.

**TI/TO Pipeline (Critical):** Using standard OpenAI-style message abstractions in multi-turn RL leads to **model collapse** — parsing tokens to messages and back is "lossy" (erases whitespace around tool calls), creating low-probability tokens that dominate gradients. Strictly maintaining a Tokens-In/Tokens-Out (TI/TO) pipeline prevents this.

**Length Bias:** "Length-debiased" GRPO can cause logit collapse when failed rollouts are longer. Fixed via **Length Scheduling** (short → long rollouts) + soft length penalty.

#### Emergent Capabilities

- **Parallel tool use** — Multiple search queries in a single turn (naturally emerged)
- **Hierarchical retrieval** — First reads excerpts, uses `read` tool for full content only when needed
- **Reciprocal Rank Fusion (RRF)** — 4 parallel rollouts fused for max recall at zero additional latency

#### Production Position

SID-1 works as a composable subagent for larger LLMs (similar to `swe-grep` in coding agents). Its recall at 1/374th the cost of frontier models makes it a practical replacement for vector search + reranking pipelines in production agentic search systems.

#### RL Training Infrastructure (2026 Update)

A May 2026 turbopuffer blog post by SID co-founders Max Rumpf and Sam Dauncey [[raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai]] revealed the full scale of SID-1's RL training infrastructure:

- **Per training step**: 256 questions, each with 16 parallel attempts → up to 4,096 rollouts per step
- **Training length**: ≫1,000 steps
- **Search volume**: Up to ~81,920 searches per step (256 × 16 × ~20 searches each), averaging >100 QPS across a full step
- **Burst pattern**: All 4,096 attempts fire initial searches simultaneously in a ~10s window, creating **1k+ QPS bursts** at the start of each training step
- **Corpora scale**: 10M+ document indexes across finance, science, legal, email, and general knowledge

This synchronous RL design creates a fundamental tension: **search latency directly bottlenecks GPU utilization**. If the search backend can only economically scale to 20 QPS, processing 81,920 searches takes ~68 minutes per step — but the GPUs can run all model attempts ~10x faster. Idling GPUs = substantial cost waste.

#### Search Backend: turbopuffer Integration

SID migrated their search backend to [[entities/turbopuffer]] to solve the GPU utilization problem. turbopuffer's **stateless query tier over object storage** is particularly suited to RL-for-search workloads:

| RL need | turbopuffer solution |
|---------|---------------------|
| Bursty 1k+ QPS reads | Stateless readers pool; new nodes hydrate cache from object storage on demand |
| Diverse search tools | Single query planner routes across ANN, BM25, regex, glob, metadata filtering — all index types maintained |
| 10M+ to 100B+ corpora | 100B+ vector ceiling per namespace; tested at 100B simultaneous query |
| Cold storage between runs | Object-storage-native; inactive namespaces ~100x cheaper than in-memory VDBs |
| Corpus updates without invalidating questions | Native namespace branching (copy-on-write, constant time) |

This architecture lets SID spend the majority of their engineering effort on "make the model better" rather than "make the backend carry the traffic."

#### Emergent Tool Preferences and Learned Behaviors (2026 Update)

The turbopuffer article revealed richer detail about SID-1's emergent search strategies:

- **ANN preference**: As training progresses, SID-1 increasingly prefers ANN over BM25 — but **never fully abandons** BM25, indicating some tasks are uniquely suited to keyword search
- **HyDE (Hypothetical Document Embeddings)**: SID-1 natively learns to draft plausible answer documents and embed them as search vectors, landing closer to real answer documents in embedding space. This is an emergent capability — not programmed.
- **Parallel multi-query BM25**: Rather than guessing the perfect keyword string, SID-1 issues a mix of 3-4 narrow (overdetermined) and broad (underdetermined) searches simultaneously
- **Parallelism as emergent behavior**: Because the reward function includes speed, parallelism emerges naturally. SID-1 learns to issue 4-8 searches per turn rather than one, dropping latency to ~5s on hard questions and ~1.5s on easy ones. Tool calls per turn increase from ~5 to ~20 over training while the number of turns stays constant at ~3-4.

This learned tool preference opens an interesting meta-research avenue: if RL makes a model prefer some tool, it is likely a better tool — analogous to how AlphaGo discovered strategies that appeared "alien" to Go experts but outperformed human designs.

#### Post-Training Design Insights (GRPO Lessons from SID-1)

The SID-1 technical report and turbopuffer infrastructure article contain several design lessons that generalize beyond retrieval to any RL post-training pipeline for agentic models. These are "things to keep in mind" when designing RL fine-tuning for multi-turn tool-using agents.

##### 1. Scaling Laws: Log-Linear, No Ceiling

SID-1's training results reveal two scaling properties:

- **Model size**: Performance improves approximately **logarithmically** with base model size. However, the RL pipeline provides a **>10× effective compute multiplier** — an RL-trained 14B model (Qwen3) can match or exceed the agentic retrieval performance of much larger raw models.
- **Training compute**: NDCG improves **log-linearly** with the number of training tasks. After a modest budget, SID-1 surpasses frontier models. Critically, **no intrinsic ceiling** was observed — the paper estimates the approach can scale by another **3–6 orders of magnitude** via more environments, questions, or model size.

> **Design implication**: If you're not seeing a ceiling yet, you're not done scaling. Log-linear scaling means doubling compute yields consistent gains — don't plateau prematurely by over-optimizing for a fixed budget.

##### 2. TI/TO Collapse: Why Message Parsing Breaks Multi-Turn RL

The **Tokens-In/Tokens-Out (TI/TO)** pipeline is the most critical infrastructure lesson. Using standard OpenAI-style message abstractions (`messages → text → messages`) in multi-turn RL causes **lossy re-tokenization** that leads to catastrophic model collapse.

**The collapse mechanism:**

1. Tool-call whitespace is stripped during message parsing. For example, the two-token sequence `" \"` (space + tool call marker) becomes a single token with `logprob ≈ -20` after re-tokenization.
2. Bad rollouts (where the model tried a wrong search strategy) get their tool calls "fixed" by the chat template before being fed into training — they look like correct tool usage to the optimizer.
3. These "fixed" tokens carry **extremely negative logprobs** because the model genuinely didn't predict them (the template inserted them).
4. With GRPO's advantage-weighted gradient, these negative-advantage, very-negative-logprob tokens **dominate the gradient** — the model learns to suppress them globally.
5. Result: reward crashes, format collapses, and the model stops outputting tool calls altogether.

**The fix:** Strict TI/TO — work directly with raw token sequences. No message parsing between rollout and training step. The model sees exactly what it generated, and the template never "fixes" anything.

> **Design implication**: If you're building multi-turn RL for tool-using agents, TI/TO is non-negotiable. Any layer that converts tokens → messages → tokens is a source of collapse risk. Test this before scaling.

##### 3. Format Reward Regression: Don't Skip It

SID-1 initially omitted format reward because the base model (Qwen3-14B) had a **format pass rate >0.95** — tool calls reliably followed the expected schema. The intuition was "if it's already working, don't add noise."

However, **format adherence regressed during prolonged training**. As the model explored more diverse search strategies, it drifted away from the tool-call format. Without a format reward, there was no gradient signal to maintain the schema. The fix was to add a format reward mid-training, but by that point some damage was done.

> **Design implication**: Always include a lightweight format reward, even if initial format adherence is near-perfect. RL exploration will cause drift — the format reward acts as a guardrail that prevents schema degradation, not just a fix for broken formats. Future work: consider starting from SFT models with innate format adherence to reduce this risk.

##### 4. No SFT Cold Start: RL from Base Model

SID-1 was trained on Qwen3-14B **base model** using **modified GRPO without any SFT cold start**. This contradicts the common practice of SFT → RLHF/DPO/GRPO, where SFT provides a "good enough" policy before RL fine-tuning.

The key enabler is the **reward design**: NDCG with partial credit provides a dense enough signal that the model can bootstrap retrieval behavior from pure RL. However, this also means the initial rollouts are extremely noisy — the model has never seen a multi-turn tool-calling interaction before.

> **Design implication**: RL-from-base is viable if the reward signal is sufficiently dense and covers the full task. But expect very long warm-up periods and format instability. For most practical applications, a small amount of SFT on demonstration trajectories is likely more efficient — SID-1's authors note SFT as future work specifically for format adherence.

##### 5. Synthetic Data: Any Corpus, No Human Annotations

SID-1's training corpus spans general knowledge, finance, science, legal, and email — all without human annotation. The fully synthetic pipeline:

1. Take any document corpus
2. For each document, generate a question that requires that document to answer
3. The document is the "gold" target; NDCG compares the model's ranked list against it
4. Noise is introduced by training with public questions (noisy ground truth) → the model learns to over-report; switching to synthetic-only questions fixes this

> **Design implication**: The synthetic question pipeline is the scaling enabler. If you can generate training data programmatically from your domain's document corpus, you can train a domain-specific agentic retriever with zero annotation cost. The key risk is question quality — noisy target documents teach the model bad over-reporting habits (Figure 8 in the report).

##### 6. Length Scheduling: Fixing "Length-Debiased" GRPO

Standard GRPO with length debiasing can cause **logit collapse** when failed rollouts are longer than successful ones. The debiasing term tries to compensate for length, but the gradient interaction is unstable.

SID-1's fix: **Length Scheduling** — start training with short rollouts (limited tool calls), then gradually increase the allowed maximum. Combined with a **soft length penalty** (rather than hard debiasing), this prevents the early-stage collapse where the model associates "long outputs" with "bad rollouts."

> **Design implication**: Length bias in GRPO is nuanced. Hard debiasing creates gradient instability; soft penalties + curriculum scheduling are more robust. Start short, go long — let the model learn to use tools before asking it to be efficient with them.

##### Summary Table: Post-Training Design Checklist

| Design Concern | Pitfall | SID-1 Solution | Generalizable? |
|---|---|---|---|
| **Message parsing** | Re-tokenization creates gradient-dominating negative logprobs | Strict TI/TO pipeline | ✅ Yes — any multi-turn tool-use RL |
| **Format drift** | RL exploration degrades tool-call schema | Always include format reward (even if >0.95 pass rate) | ✅ Yes |
| **Cold start** | RL from base model is slow and noisy | Dense reward signal (NDCG); future: SFT for format | ⚠️ Viable if reward is dense; SFT preferred |
| **Length bias** | Hard length debiasing causes logit collapse | Length scheduling + soft length penalty | ✅ Yes |
| **Synthetic data** | Human annotation can't scale | Fully synthetic Q&A pipeline from document corpus | ✅ Yes — domain-adaptable |
| **Reward hacking** | Recall-only reward → over-reporting | NDCG penalizes rank position; slight over-reporting preferred to under-reporting | ✅ Yes |
| **GPU utilization** | Search latency bottlenecks RL training throughput | Stateless turbopuffer query tier; namespace branching | ✅ Yes — RL-for-search needs search infra that scales with GPU speed |

### Benchmarking Agents vs Search Stack: Amazon ESCI

Search engineer Doug Turnbull ([[entities/doug-turnbull-core-ideas]]) conducted a 2026 benchmark on Amazon ESCI validating that even simple agents with basic retrieval tools outperform traditional search stacks.

#### Results

| Strategy | NDCG | Δ vs BM25 baseline |
|----------|------|:---:|
| BM25 (baseline) | 0.289 | — |
| e5_embedding | 0.314 | +8.7% |
| GPT-5-mini + e5 | 0.359 | +24.2% |
| GPT-5-mini + BM25 | 0.385 | +33.2% |
| GPT-5-mini + Both | 0.410 | +41.9% |
| **GPT-5 (Full) + Both** | **0.453** | **+56.7%** |

A **56.7% NDCG improvement** achieved simply by wrapping a frontier LLM with basic retrievers — no data-specific tuning, no custom ranking signals.

#### Agents Use Tools Intelligently

Analysis of reasoning traces reveals that agents naturally recognize result mismatches and refine queries:

```
Search "pvc coupler" → networking results (RJ45 connectors)
→ Recognizes mismatch: "Those are RJ45 couplers..."
→ Reformulates: "Probably asking about PVC pipe couplers"
→ Search "PVC pipe coupler" → correct results
```

This mirrors the Q2Q reformulation finding (Level 1) but occurs emergently via the agent's reasoning rather than through an explicit translation step.

#### Encouraged Exploration Improves Results

Preventing agents from being "lazy" with minimum 4 tool calls + 0.9 similarity diversity threshold:

| Setting | NDCG |
|---------|------|
| Default (2 tools, any number of calls) | 0.410 |
| Min 4 calls | 0.429 |
| Min 4 calls + similarity filter | **0.4308** |

This validates Doug Turnbull's harness architecture (Level 3): the **outer loop** constraint ("try harder with different queries") directly improves retrieval quality.

#### Key Limitation: Finding Things vs Deep Research

Turnbull identifies a critical boundary: **agentic search works for finding entities** (products, jobs, documents — things the agent can recognize from metadata) but **fails to improve information retrieval** (MSMarco passages — where the LLM doesn't know what information exists).

> "The LLM can't evaluate what it doesn't know. If it knew what information was correct, it wouldn't need search!"

This explains why SID-1's RL-trained approach (document-centric reward for relevance ranking) and Cao et al.'s externalized processing (grep/scripts for factual extraction) succeed in different domains than general search ranking.

#### Validated Patterns

| Finding | Connected To |
|---------|-------------|
| BM25 outperforms embeddings for agents | Level 1: Query Mismatch (Meng et al.) |
| Agents naturally refine queries | Level 1: Q2Q Reformulation |
| Harness constraints improve results | Level 3: Two-Loop Architecture |
| SID-1 as specialized drop-in | Level 1: RL-Trained Retrieval |
| "Finding things" > "Deep research" | Boundary condition for all approaches |

---

## Level 2: Harness Engineering Perspective

In agent harness/skill systems, agentic search enables context-efficient tool discovery.

### SQL-Based Skill Discovery

Rather than loading all skills/tools upfront, the agent queries a structured database of capabilities based on current context:

1. **SQL Discovery**: Queries a structured skills database to find relevant capabilities based on the user's current context
2. **Agentic Grep/SQL Hybrid**: For unstructured content (e.g., SEC filings), performs targeted text search only when needed
3. **Lazy Loading**: Only injects relevant skills into the agent's context, avoiding token waste

### Use Case: SEC Filing Analysis

Fintool's agents need to answer questions about SEC filings (10-K, 10-Q, proxy statements). Instead of loading all 50+ analytical skills into context:

```markdown
User asks: "What's the company's R&D spend trend?"
→ SQL query finds skills related to "financial metrics", "trend analysis"
→ Only those skills are loaded into context
→ Agent executes with focused capability set
```

### Practitioner Implementation: The Tool-Calling Loop

In his February 2026 Vanishing Gradients interview [[raw/articles/2026-02-20_doug-turnbull-build-first-agentic-search-app]], Turnbull described the concrete agentic search implementation loop at the harness level:

```
1. Agent receives query + system prompt with tool descriptions
2. Agent decides: call tool (search) or generate final answer
3. Search results → structured observations
4. Agent reflects on relevance → reformulates if needed
5. Outer harness validates output against quality criteria
6. "Try harder" feedback loop if below threshold
```

This mirrors the SQL-based skill discovery pattern (Fintool) above — both are harness-layer orchestration patterns where the agent's tool selection is managed not by the LLM alone, but by an outer loop that imposes quality constraints.

---

## Level 3: Coding Agents as Retrieval/Processing Interface

A 2026 study by Cao, Yin, Dhingra, and Zhou (Duke & CMU) proposes a paradigm shift: instead of using agents that *query retrieval systems*, treat the agent itself (Claude Code, Codex) as the retrieval/processing mechanism by letting it organize text in file systems and manipulate them with native tools.

### How It Works

Agents externalize long-context processing from latent attention (internal LLM processing) into explicit, executable interactions:

```
Massive text corpus
        ↓
  Agent organizes into directory structure (files/folders)
        ↓
  Uses grep, sed, ripgrep, Python scripts for navigation
        ↓
  Writes custom scripts for index/slice/filter/aggregate
        ↓
  Returns precise answer from up to 3 trillion tokens
```

### The "Folder Structure" Advantage

Coding agents have **strong inductive priors** for hierarchical directory navigation from training on large code repositories:
- **Folder structure**: 89.0% accuracy on BrowseComp-Plus
- **Single file (JSON)**: 83.0% accuracy — filesystem structure itself is a retrieval signal

### Negative Result: Retrieval Tools Harm Performance

> "Equipping coding agents with retrieval tools does not consistently improve performance and can even degrade it — standard retrievers, when available, become the agent's default discovery mechanism and displace broader file-system exploration strategies."

This directly challenges the assumption from the IR perspective (Level 1) that better retrievers are always beneficial. When agents can use file system tools directly, adding a retrieval layer can *reduce* exploration quality.

### Performance vs IR Methods on BrowseComp-Plus

| Approach | Score | Method |
|----------|-------|--------|
| **Coding Agent** | **88.50** | Folder structure + grep/scripts |
| BM25–monoT5-3B + Q2Q | 0.716 recall / 0.689 accuracy | IR pipeline (Level 1) |
| Previous SOTA | 80.00 | Retrieval-based |

### Emergent Strategies

Agents autonomously adapt their processing strategy to the task type:

1. **Multi-hop QA** — "Search-and-refine" loop across entity chains (e.g., Riot Games → Brandon Beck → ... → Max Mazanov in 6 hops)
2. **Analytical tasks** — Abandons search entirely; writes Python scripts to parse, count, sort across thousands of lines
3. **Reading comprehension** — Balanced tool usage with LLM's inherent reasoning

### Cost Comparison

| Task | Coding Agent | GPT-5 Full Context | Notes |
|-----|-------------|-------------------|-------|
| BrowseComp-Plus | ~$0.70/query | ~$0.27 | GPT-5 couldn't see full 750M corpus |
| Oolong-Syn | ~$0.19/query | ~$1.42 | Coding agent 7× cheaper |

The coding agent approach is not always cheaper than RAG, but it is significantly cheaper than full-context processing while offering higher accuracy on long-context tasks.

### Paradigm Shift: Externalized Processing

This research suggests a new thesis: **delegating long-context processing to coding agents is a viable alternative to scaling context windows or optimizing retrieval pipelines.** By structuring text to look like code repositories, frontier models' software engineering capabilities can be leveraged for general text-processing.

### Level 4: Direct Corpus Interaction (DCI) — "No Retriever At All"

A May 2026 paper by Li et al. [[raw/papers/2026-05-03_2605.05242_direct-corpus-interaction]] pushes the coding-agent-as-search paradigm further with **Direct Corpus Interaction (DCI)** [[concepts/direct-corpus-interaction]]. The radical thesis: **"The best retriever ... is no retriever."**

Where Cao et al. (Level 3) require file-system pre-organization (folder structures), DCI works on **raw, unorganized corpora** — the agent searches directly with `grep`, `find`, `bash`, and shell pipelines. No embedding model, no vector index, no offline indexing.

#### Results (with same Sonnet 4.6 backbone)
| Metric | Retrieval Agent (Qwen3-Embedding-8B) | DCI-Agent-CC | Δ |
|--------|--------------------------------------|-------------|---|
| BrowseComp-Plus Accuracy | 69.0% | 80.0% | **+11.0 pts** |
| Cost | $1,440 | $1,016 | **−29.4%** |
| Multi-Hop QA Avg | 52.3 | 83.0 | **+30.7 pts** |
| IR Ranking NDCG@10 | 47.0 | 68.5 | **+21.5 pts** |

#### Key Mechanism
DCI's advantage is NOT from better recall — among 176 BrowseComp-Plus questions DCI wins but the retriever loses, only 34 lacked gold documents in the conventional retriever's results. The edge comes from **better evidence utilization**: fine-grained grep matches → localized context reads → extraction of new search terms → compositional bash queries. The agent builds its own search trajectory rather than accepting a fixed top-k.

#### Connection to Level 3
DCI generalizes the coding-agent approach (Cao et al.) by removing the file-system pre-organization requirement. The core insight shared by both: when agents interact with text directly via terminal tools, retrieval quality improves — and adding conventional retrieval tools can **degrade** agent exploration by displacing finer-grained strategies.

#### Context Management for Long-Horizon Search
DCI introduces five levels of runtime context management (truncation, compaction, summarization) to handle the observation accumulation from repeated grep/read cycles. L3 (truncation + compaction) achieves best accuracy despite retaining less gold evidence — selective discarding of old observations proves beneficial.

### Practitioner Perspective: Doug Turnbull's "Grep Moment"

Search engineer Doug Turnbull ([[entities/doug-turnbull-core-ideas]]) contextualizes this trend in his April 2026 article *"Is grep all you need for RAG?"* He argues the key insight isn't about `grep` itself — it's about the **harness architecture** that constrains and validates agent behavior.

#### The Two-Loop Architecture

Turnbull defines the critical distinction:

1. **Inner Loop (The Agent)** — LLM iterates through tool calls (`grep`, `cat`, `ls`, `find`) until satisfied
2. **Outer Loop (The Harness)** — Programmatic validation hooks (rerankers, LLM-as-a-judge, metadata checks) evaluate results. If below quality bar (recency, popularity, authority), the harness tells the agent to "try harder."

```python
def harness(user_prompt):
    inputs = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": user_prompt},
    ]
    valid = False
    while not valid:
        inputs = agent_loop(inputs)  # Inner loop
        search_results = inputs[-1]
        for result in search_results:
            if result.review < 4.0:
                inputs.append({"role": "system",
                               "content": f"Result {result} is not high enough reviews, keep trying"})
                valid = False
```

#### Deconstructing the Search Stack

Traditionally, ranking logic was embedded inside search engines (Elasticsearch). In the agentic model:
- **Raw Access**: Agent gets "dumb" tools (grep)
- **Acceptance Criteria**: Logic moves to the outer loop harness

#### Why Dumb Tools Work

- **Constraints** budget the agent's creativity, saving reasoning for where it matters
- **Training data**: Frontier LLMs are trained on code navigation — `grep` is a learned "happy path"
- **Structured outputs**: Developers force specific filters within simple keyword search

#### Three Limits of Grep

Turnbull warns that the "grep moment" has diminishing returns:

1. **Actionable Feedback** — If a search tool cannot prioritize relevance, berating the agent to "try harder" won't help
2. **Complexity** — Real retrieval balances recency, popularity, embeddings, lexical search; modeling this in flat markdown becomes unmanageable
3. **Token Cost** — Many tool calls to compensate for a "dumb" search tool is expensive

> *"While `grep` is having a moment, high-quality retrieval still matters. Eventually, the most appropriate tool for an agent is a well-tuned `search` function."*

This mirrors the Level 1 finding (SID-1: RL-trained retrieval outperforms both vector search and pure grep-based approaches) and the Level 3 finding (retrieval tools can harm file-system exploration). The article suggests the optimal path is a **well-tuned search harness**, not an either/or choice.

### In-Prompt Reinforcement Learning (February 2026)

In his February 2026 Vanishing Gradients interview [[raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search]], Turnbull introduced a concrete technique for improving agentic search quality: **in-prompt reinforcement learning** — simulating reward signals within the prompt itself to guide the agent without manual human intervention.

#### The Problem: Domain Blindness

Agents lack domain-specific knowledge. Example from the talk: a user searching for a "bistro table" for a restaurant may get results for patio furniture because the LLM associates the term with outdoor settings. Without feedback, the agent **assumes its results are correct** and terminates the search.

#### The Solution: Validator-as-Dissatisfied-User

The core insight: **wrap the agentic loop in a Harness that simulates an unhappy user**:

```
1. Agent produces results via standard tool-calling loop
2. Harness validator (LLM-as-judge, reranker, or classifier) inspects each result
3. If relevant → validator appends "Great work!" to context
4. If irrelevant → validator appends "This doesn't make me happy! Sorry!"
5. Agent re-enters the loop with negative feedback → reformulates query
6. Loop continues until all results pass validation
```

This exploits the LLM's **sycophantic nature** — the model's deep desire to please — to align it with user goals. Negative feedback functions as a **reward signal** that pushes the agent away from bad search spaces.

#### What Makes It "In-Prompt RL"

Unlike traditional RLHF (which requires training runs, human raters, and model weight updates), in-prompt RL operates entirely within the **inference context**:

| Dimension | RLHF | In-Prompt RL |
|-----------|------|-------------|
| Training required | Yes (reward model + PPO/DPO) | No (inference only) |
| Feedback source | Human raters | Automated validator (LLM/rules) |
| Weight modification | Yes | No — pure context manipulation |
| Iteration speed | Hours/days (training runs) | Seconds (same inference loop) |
| Adaptability | Requires retraining for new domains | Prompt-level changes only |

#### What to Use as Validators

Components previously discarded from the traditional search stack find new purpose here — not as retrieval middleware, but as **validation functions** in the outer harness:

| Validator Type | Use Case | Example |
|----------------|----------|---------|
| **LLM-as-Judge** | Semantic relevance assessment | "Does this result answer the user's question?" |
| **Reranker/Classifier** | Objective relevance scoring | Cross-encoder scores, metadata checks |
| **Rule-Based** | Hard business constraints | "Must have review ≥ 4.0", "Must be in-stock" |
| **Domain Model** | Specialized knowledge | Detecting "bistro table ≠ patio furniture" |

#### Connection to the Harness Architecture

In-prompt RL is a specific **implementation pattern** within the broader two-loop harness architecture. The harness (outer loop) doesn't just validate — it provides **reinforcement signals** that actively shape the agent's search trajectory. This is distinct from simpler harness patterns that only check a final binary pass/fail.

Sources: [[raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search]], [[raw/articles/2026-02-20_doug-turnbull-build-first-agentic-search-app]]

### Long-Running Agents and Recursive Language Models (February 2026)

In the same Vanishing Gradients interview [[raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search]], Turnbull outlined an emerging direction for agentic search at scale: **long-running agents** that persist across hours or days, and the **Recursive Language Model (RLM)** paradigm for managing unbounded context.

#### The Problem: Context Rot in Long-Running Agents

When search agents run for extended periods (hours to days), they face a critical failure mode:

1. **Context accumulation** — Every tool call, result, and reasoning step adds to the linear chat history
2. **Context rot** — The agent loses coherence as the context window fills with stale/irrelevant history
3. **Repetition** — Without structured memory, agents re-visit the same search spaces and repeat work
4. **Loss of creativity** — Exhausted context windows constrain the agent's ability to explore new directions

Turnbull's immediate solution is **compaction**: periodically summarizing "here's what you've tried, here's what you haven't" so the agent can reason about what's useful without holding the full history in context.

#### The Practitioner's RLM Vision: "Throw Away Context Entirely"

Turnbull then introduces a more radical shift — one he describes as a direction that "will definitely lose you" but represents where the field is heading:

> *"What if we got rid of this idea of context entirely, and all of the information that had happened so far in this agent's life lived in a Python variable? The only tool — one of the tools the agent had — was the ability to run Python code to look and inspect that variable for what it needed. It's a way of searching within its own context."*
> — Doug Turnbull, Vanishing Gradients (Feb 2026)

This vision maps directly to the academic **[[concepts/rlm-recursive-language-models|RLM (Recursive Language Models)]]** framework (Zhang et al., MIT, 2025), but from a **search engineer's perspective** rather than an ML researcher's:

| Dimension | Academic RLM (Zhang et al.) | Turnbull's Practitioner Framing |
|-----------|---------------------------|-------------------------------|
| **Problem statement** | Near-infinite length context processing | "Context rot" in long-running search agents |
| **Core mechanism** | REPL environment, `rlm.completion()`, recursive sub-calls | Python variable as agent memory, code execution to inspect it |
| **Key affordance** | LLM writes code to slice/transform context variable | Agent "searches within its own context" via code |
| **Analogy** | Context as environment, not input | Context as a search index the agent queries |
| **Ultimate vision** | Task-agnostic inference paradigm | "Context just becomes the entire world — including my search index" |

#### Concrete Example: OpenClaw's Self-Extending Loop

Turnbull uses **[[entities/openclaw|OpenClaw]]** as a concrete example of RLM-like behavior in the wild. OpenClaw can generate its own code and execute it — in one case, it acquired a skill for making voice calls, wrote code implementing that skill, and **called its creator over voice**. This demonstrates the same pattern: the agent uses code execution to extend its own capabilities and inspect/modify its state, escaping the linear chat history constraint.

#### From Context-as-History to Context-as-Search-Index

Turnbull's framing pushes the RLM concept to its logical conclusion for search:

1. **Today**: Agent has a linear chat history it reads sequentially
2. **Compaction**: Agent summarizes history periodically to manage context
3. **RLM (context-as-variable)**: Agent's entire life lives in a Python variable; agent writes code to query it
4. **RLM (context-as-world)**: The distinction between "agent memory" and "search index" dissolves — searching the web and searching your own history are the same operation

This directly connects to the [[concepts/code-mode|CodeMode]] pattern and [[concepts/context-engineering/context-fragments|Context Fragments]] — both of which treat context not as a passive input but as a structured artifact the agent actively queries and mutates.

#### Empirical Strategies for Long-Running Agents (June 2026)

Turnbull's [[concepts/long-running-search-agents|Cheat at Search lecture on Long Running Search Agents]] (June 2026) provides the first systematic empirical study of these patterns across 7 progressive strategies:

| Strategy | Yield/Call | Key Insight |
|----------|-----------|-------------|
| Single context | 0.795 | Baseline; context exhaustion inevitable |
| Cron job (restart) | 0.720 | Wasted context grows O(n); 34 duplicates |
| Compaction | 0.738 | Still O(n), doesn't scale indefinitely |
| **Local index** | **2.68** | **Biggest gain — avoid external API waste** |
| Frontier prompt | 1.667 | Helps only after easy cases exhausted |
| Query model | TBD | Simpler but loses reasoning |
| Self-querying | TBD | Agent queries its own accumulated state |

The central finding: **local memory before external calls** is the single most impactful design principle. A persistent local index (structured with domain taxonomies like NAICS codes) yields 3.7x improvement over naive restart patterns.

Sources: [[raw/articles/2026-02-21_hugobowne_how-to-build-first-agentic-search]], [[concepts/rlm-recursive-language-models]], [[concepts/recursive-language-models]], [[concepts/long-running-search-agents]]

### Berryman's 5-Level Agentic Search Maturity Model (January 2026)

In Vanishing Gradients Ep. 68 [[transcripts/2026-01-23_vanishing-gradients_ep68-builders-guide-agentic-search]], John Berryman ([[entities/john-berryman]]) presented a **practical maturity model** for incrementally adopting AI in search applications. Published in full detail on the Arcturus Labs blog [[raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level]], the model provides a low-risk roadmap from traditional search to conversational AI agents.

#### Core Philosophy

Berryman's framing demystifies the AI hype:

> *"RAG isn't anything special; it's just an LLM with access to a well-described product search tool. Agentic AI is really, literally, just a couple of for-loops."*

The key insight: **nothing is magical**. A request to Gen AI is just an HTTP request — text in, text out. Build an agent by wrapping that with for-loops. Make it a RAG agent by giving it your current search endpoint as a tool. This *demystification* is the foundation for incremental adoption: existing infrastructure (Elasticsearch, Algolia) stays in place; AI is a thin, decoupled layer that thickens over time.

#### The Five Levels

| Level | Name | User Experience | Key Change | Risk | Implementation Cost |
|:-----:|------|----------------|------------|------|---------------------|
| **0** | Traditional Search | Keyword box + filters; user does all the work | Baseline | — | Existing system |
| **1** | Beginner AI | "Did you mean?" suggestion bar (50px) | AI interprets natural language into proper queries; async, no latency impact | Zero UX risk | Thin endpoint |
| **2** | Intermediate AI | Auto-executed AI queries + results summary + recommended next queries | "Did you mean?" → "Interpreted as"; adds contextual summary and next-query suggestions | Latency (10ms→2-3s), but saves user's cognitive effort | Moderate |
| **3** | Advanced AI | Full conversational assistant; chat replaces search box | Stateful conversation; agent remembers context; clarifies intent; talks *about* results | UX paradigm shift | Significant |
| **4** | Async Research Agent | Agent performs research on user's behalf asynchronously | Agent digs through inventory once it understands user needs; works while user is away | Trust, accuracy | Major |

#### Level-by-Level Detail

**Level 0 — Traditional Search (Your Current Reality):**
The burden is entirely on users to know product terminology, understand filters, and manually iterate through result pages. Most users type one query, scan the first page, and leave. High bounce rates, confused usage patterns ("4BR" typed as keyword instead of filter).

**Level 1 — Beginner AI (Test the Waters):**
A baby step: keep traditional search unchanged, add a small "Did you mean?" suggestion bar. AI interprets natural language into structured queries — "4BR under $750K" → "Property Type: Condo, Search Terms: 'Downtown'". Implemented asynchronously → zero latency impact. Users can ignore or click to apply. **Risk-free UX** — the only concession is 50 pixels of vertical real estate. Track click-through rate and conversion lift.

**Level 2 — Intermediate AI (Let AI Take the Wheel):**
AI automatically executes recommended searches. Adds two new UI elements: (a) a results summary giving holistic understanding, and (b) recommended next queries to keep users engaged. **Key tradeoff**: latency increases from 10ms to 2-3 seconds, but if users take 5 seconds to formulate a good query, AI actually saves 3 seconds. A/B test conversion impact.

**Level 3 — Advanced AI (Full Conversational Assistant):**
The search box is replaced by a stateful chat window. Berryman's thesis: **conversation is the original UX** — humans have been conversing for 50,000 years; clicking glowing rectangles is only a 30-year-old adaptation to technical limitations. Users lean into model intuition: "Show me some big ass houses!" instead of structured queries. The agent clarifies intent through multi-turn dialogue, can talk *about* results ("which one is more modern?"), and can perform aggregate analysis ("what's the typical price distribution?").

**Level 4 — Async Research Agent (Future):**
The agent performs asynchronous research — really digging through inventory once it understands the user's needs. "The agent searches while you sleep." This connects to Turnbull's long-running agent and RLM discussion (above) — the same context management challenges apply at scale.

#### Connection to the Broader Agentic Search Landscape

Berryman's model is a **practitioner adoption roadmap**, not an architectural taxonomy. It complements — rather than replaces — the three-level framework (IR / Harness / Externalized Processing) documented above:

| Dimension | 3-Level Framework (This Page) | Berryman's 5-Level Model |
|-----------|------------------------------|--------------------------|
| Focus | *What* the technology does | *How* to adopt it incrementally |
| Audience | ML/IR researchers, harness engineers | E-commerce teams, product managers |
| Risk model | Architectural complexity | Business UX risk |
| Key metric | NDCG, recall, accuracy | Click-through rate, conversion, bounce rate |

Sources: [[transcripts/2026-01-23_vanishing-gradients_ep68-builders-guide-agentic-search]], [[raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level]]

### Revealed Preferences: The Fundamental Limit of LLM-as-Judge (November 2025 — January 2026)

A recurring theme across Turnbull's and Berryman's work — crystallized in Vanishing Gradients Ep. 68 and Turnbull's blog post [[raw/articles/2025-11-02_softwaredoug_llm-judges-arent-the-shortcut]] — is the fundamental limitation of using LLMs to evaluate search quality.

#### The Core Problem

LLMs approximate **explicit judgments** — topical relevance ("is this document about Harry Potter?"). But real search quality depends on **revealed preferences** — what users actually click, buy, or engage with. These are systematically different:

| Signal Type | What LLMs Capture | What They Miss |
|-------------|-------------------|----------------|
| **Explicit Judgments** | ✅ Topical relevance, factual accuracy, authority | — |
| **Revealed Preferences** | ❌ Engagement, emotional resonance, social proof, user oddities | Clicks, purchases, dwell time, conversion |

> *"LLMs live in a world of facts and knowledge. But LLMs don't have limbic systems. So their evaluations come with limitations."*
> — Doug Turnbull

#### Concrete Examples of the Gap

- **Reddit**: A search for "harry potter" may mean memes, drama about JK Rowling, spicy controversies — not factual articles. An LLM judge sees the factual articles as "most relevant."
- **Shopify**: Users preferred plain/black clothing over flashy items based on clickstream data. Unless explicitly told, an LLM won't catch this.
- **Bistro table**: In US furniture e-commerce, "bistro table" means outdoor furniture. An LLM assumes restaurant context and rates irrelevant results as relevant.

#### The 90% Trap

> *"Many teams get excited when they immediately see 70-90% agreement with human labelers. In my experience, that last bit of human-LLM disagreement matters. Those are the non-obvious cases."*

Simple algorithms already capture the first 80-90%. The **last 10-20% — the hard negatives and edge cases — are where search quality improvement actually lives**. An LLM judge with 90% agreement may be adequate for regression testing but useless for pushing beyond easier wins.

#### Three Core LLM-as-Judge Failure Modes

1. **Engagement Blindness** — LLMs don't know what users find engaging; optimizing for LLM-judge scores can decrease real user satisfaction
2. **Hard Negative Blindness** — The last 10% of disagreement contains the non-obvious cases that matter most; LLMs systematically miss domain-specific nuances
3. **Sneaky Overfitting** — Filling prompts with examples for edge cases creates brittle systems; every new rule pushes attention away from the general problem

#### What LLMs SHOULD Do: Exploratory Analysis, Not Final Judgment

Turnbull's recommendation: reposition LLMs from *judges* to *analysts*:

| ❌ Don't Use LLMs For | ✅ Use LLMs For |
|-----------------------|-----------------|
| Final relevance scores | Finding interesting query clusters |
| Replacing human labelers | Comparing result sets ("these look different from those") |
| Automated quality gates | Surfacing anomalies ("this query's results look unusual") |
| Regression testing alone | Educating the team about search behavior |

> *"LLMs are better at describing differences between result sets than judging relevance. They should generate hypotheses for humans to investigate, not replace human evaluation."*

#### Connection to LLM-as-Judge Best Practices

This practitioner critique complements the academic best practices documented in [[concepts/llm-as-judge]]. Where the academic literature focuses on *how* to do LLM-as-judge well (rubric design, bias mitigation, inter-rater reliability), Turnbull and Berryman question *whether* LLM-as-judge is appropriate for search evaluation at all — arguing that behavioral signals (clicks, purchases, dwell time) are the only reliable measure of what users actually want.

Sources: [[raw/articles/2025-11-02_softwaredoug_llm-judges-arent-the-shortcut]], [[transcripts/2026-01-23_vanishing-gradients_ep68-builders-guide-agentic-search]], [[concepts/llm-as-judge]]

### Discussion: "Will Agents Replace Search Teams?" (January 2026)

A 55-minute fireside chat between Doug Turnbull and search veteran **Daniel Tunkelang** (Endeca co-founder, query understanding specialist). [[raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams]]

Unlike Turnbull's other talks (which focus on architecture and implementation), this discussion — moderated by Tunkelang — centers on the **human, business, and economic implications** of agentic search.

#### The Feedback Loop Problem

Tunkelang's central critique: agentic search breaks the rapid feedback loop that makes traditional search effective. Traditional search lets users refine iteratively in seconds. Agentic search introduces 15-minute delays, and if the agent misunderstood, that time is wasted. This is a **UX regression** for many search scenarios.

> "Search isn't that smart, but the feedback is pretty quick. It puts a lot of burden on us to refine, but at least the speed of feedback allows us to keep making attempts." — Daniel Tunkelang

#### The Spectrum of Search Needs

Tunkelang and Turnbull map search behavior onto a spectrum:

| Need Type | Example | Suited for Agents? |
|-----------|---------|:---:|
| Complex research with clear intent | Buying durable headphones, real estate search | ✅ Yes |
| Background candidate sourcing | Finding 500 experts in a field | ✅ Yes |
| Federated multi-source search | Cross-referencing LinkedIn, Indeed, GitHub | ✅ Yes |
| Commodity purchase / instant gratification | Toilet paper, red shoes on Amazon | ❌ No |
| Exploratory browsing | Retail therapy, "I'll know it when I see it" | ❌ No |

This echoes but extends Turnbull's earlier distinction between "finding things" (good for agents) and "deep research" (bad for agents). Tunkelang adds the **time-sensitivity dimension**: if the user wants instant satisfaction, agentic latency is a net negative.

#### Economic Disruption: Machines as Search Consumers

Tunkelang identifies a structural shift: when AI agents (not humans) consume search results, the ad-based business model breaks because **machine attention cannot be monetized**.

Already visible effects:
- **EXA** charges for agent-accessible web indexes (agent-to-API, not human-to-web)
- **Reddit** enters content monetization agreements
- **Stack Overflow** traffic declines as LLMs answer directly
- **GitHub** open-source maintainers see reduced human engagement and reputation flow

> "If most of the attention will be done by machines whose attention cannot be monetized directly, the economic model does have to change." — Daniel Tunkelang

Turnbull connects this to the "private internet theory": the web fragments into walled gardens where humans hide from AI crawlers, while LLMs consume the open web that was previously crawlable by Google.

#### Stakes-Based Error Sensitivity

Tunkelang proposes that agentic systems should self-calibrate based on the cost of errors:

| Stakes | Error Cost | Recommended Behavior |
|--------|-----------|---------------------|
| **Low** (play wrong song) | User hits "next" | Execute immediately |
| **Medium** (product research) | User wastes money | Show evidence, explain reasoning |
| **High** (email to wrong person) | Professional/legal damage | Confirm before acting |

He notes that current systems don't invest enough in this sensitivity model — they apply the same verification level to all queries regardless of stakes.

#### Domain-Specific Assumptions

Turnbull shares a revealing case study from a major US auto parts supplier. The LLM's default assumption (and Turnbull's) was that searching a part number means the user wants that part. In reality, salespeople were **checking commissions**. This 20% gap highlights:

- **The "unknown assumptions" problem**: LLMs embed domain assumptions that may not match reality
- **Query performance prediction**: detecting when results look unreasonable
- **Prior-based ambiguity signals**: statistically unusual queries should trigger clarification

#### Education and Critical Thinking

Tunkelang draws a powerful analogy to the early ML era: as tooling was democratized, the people who didn't understand statistics misused the tools. Same pattern with agentic search:

> "The biggest danger I see in the technology of search getting too easy is that we're masking the importance of critical thinking."

The democratization of search tools means the **bar for research skills rises, not falls** — users need more critical thinking to evaluate agent-provided results than they did to evaluate raw search results.

#### Personalization Overfitting

Tunkelang shares a concrete example of ChatGPT over-personalizing: because it inferred he was a "high-class consultant," it assumed all restaurant queries were for entertaining clients. The solution is **transparency** — agents should show *what* they learned and *why* they're making assumptions.

> "The nice thing is that an agent can appropriately try to overfit to the searcher, but also can be transparent about it, can say what it's learned."

#### Key Takeaway for Search Teams

Tunkelang's closing position: **search teams manage ambiguity, edge cases, and business alignment.** Key areas where agents can't replace them today:

1. Distinguishing clarifying questions from proceeding
2. Recognizing when the search process itself teaches the user something
3. Aligning results with business incentives (which may conflict with user incentives)
4. Handling the long tail of domain-specific edge cases

Sources: [[raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams]], [[entities/daniel-tunkelang]]

### Talk: "Rag is the What. Agentic search is the How." (April 2026)

In his 54-minute talk of the same title, Turnbull expanded his "grep moment" argument into a full architectural critique of the RAG paradigm. [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]]

**Core argument:** Complexity in RAG lived in the retrieval layer (embedding pipelines, rerankers, fusion). With agentic search, that complexity is migrating to the agent+harness (tools, scaffolds, reasoning loops). Turnbull traces this unwinding through four stages:

| Stage | What Changed | Impact |
|-------|-------------|--------|
| **Structured Attributes** | LLMs perform query understanding reliably via schema | Structured query languages enable accurate filtering |
| **Tool Calling** | Agents know they *are searching*, not force-fed context | Intentional, self-directed retrieval behavior |
| **Reasoning** | Agents reflect on results, analyze patterns, search again | Self-correcting retrieval replaces reranking |
| **Dumb Retrievers** | Agents get by with BM25, grep, and simple tools | Complexity moves from retrieval to harness |

The talk explicitly endorses SID-1 (RL-trained agentic retrieval) and positions it as the model-level complement to the harness-level changes: SID-1 speeds up the search reasoning loop, making "simple retrieval" practical at production scale.

> "I wouldn't start RAG today assuming you need the classic RAG embedding+chunking paradigm. I'd focus on tools that deliver needed context. The dumbest thing that can work, with simplest."

This talk is best read as a **live-recorded version** of the same thesis Turnbull published in his "Grep Moment" blog post — but extended from a single insight about grep to a full framework for understanding why and how agentic search replaces classical RAG.

### Production Implementation: Claude's Dynamic Web Search Filtering (Anthropic)

> **Related**: Anthropic's multi-agent research architecture ([[concepts/anthropic/multi-agent-research]]) extends this further with parallel subagents — see also their orchestrator-worker pattern and 8 prompt engineering principles for production agents.

Anthropic's **Dynamic Filtering** (March 2026) for Claude Web Search is a production-grade embodiment of the externalized processing paradigm. Instead of loading raw HTML into the context window, Claude writes and executes code to pre-process web results *before* they enter the model's reasoning context.

#### Filter-Before-Reasoning Flow

```
User query
        ↓
  1. Web search / URL fetch
        ↓
  2. Claude generates extraction script
     (targets: pricing tables, headings, citations)
        ↓
  3. Script runs in sandboxed environment
        ↓
  4. Only filtered output → Context window
        ↓
  5. Final reasoning on clean data
```

#### Performance Gains

| Benchmark | Model | Without Filtering | With Filtering | Δ |
|-----------|-------|-------------------|----------------|----|
| BrowseComp | Sonnet 4.6 | 33.3% | **46.6%** | +13.3pp |
| BrowseComp | Opus 4.6 | 45.3% | **61.6%** | +16.3pp |
| DeepsearchQA F1 | Sonnet 4.6 | 52.6% | **59.4%** | +6.8pp |
| DeepsearchQA F1 | Opus 4.6 | 69.8% | **77.3%** | +7.5pp |
| **Average** | — | — | — | **~11% accuracy** |
| **Input tokens** | — | — | — | **~24% fewer** |

#### Quora (Poe) — Production Validation

Poe by Quora, one of the largest multi-model AI platforms (200+ models), validated dynamic filtering in production. Gareth Jones, Product and Research Lead: *"Opus 4.6 with dynamic filtering achieved the highest accuracy on our internal evals when tested against other frontier models. The model behaves like an actual researcher, writing Python to parse, filter, and cross-reference results rather than reasoning over raw HTML in context."*

#### Technical Requirements

- **Models**: Opus 4.6 / Sonnet 4.6
- **Tool versions**: `web_search_20260209` or `web_fetch_20260209`
- **Beta header**: `anthropic-beta: code-execution-web-tools-2026-02-09`
- **Dependency**: Code Execution tool must be enabled (free when used with web tools; standard token costs apply)

#### Connection to the Three-Level Framework

This implementation validates patterns from all three levels:

- **Level 1 (IR)**: The code execution acts as a just-in-time filter, mirroring the re-ranking stage but at the code level rather than with a separate ranker model. Unlike the BM25→monoT5 pipeline (Level 1), dynamic filtering is **task-specific** — Claude generates custom Python extraction scripts per query, adapting its filtering strategy to the information need rather than applying a fixed re-ranking model.
- **Level 2 (Harness)**: The harness (Claude API infrastructure) orchestrates the tool flow — search → script → sandbox → context — without the agent needing to manage each step. This mirrors Turnbull's outer loop pattern but **integrated into the API layer** rather than requiring custom harness code.
- **Level 3 (Externalized Processing)**: This is the most direct validation — Claude replaces latent attention (internal HTML parsing) with explicit code execution (script-based extraction), exactly as the Cao et al. paper prescribes, but at the web search layer rather than the file system layer. Claude writes `grep`-like Python to extract structured data from unstructured HTML.

The key difference from the Cao et al. approach: instead of organizing text in filesystems, Claude uses code execution as an ephemeral processing pipeline for each web fetch. Both externalize processing from the model's internal attention to executable code.

#### The Broader GA Ecosystem: Filter-Before-Reasoning as Architectural Pattern

Dynamic filtering is not an isolated feature — it's part of a **filter-before-reasoning** architectural pattern that Anthropic is systematically building out. All five tools graduating to GA alongside dynamic filtering share the same premise: **reduce context window pressure by filtering, summarizing, or externalizing information before it enters the model's reasoning context**:

| Tool | Filter-Before-Reasoning Mechanism | Problem It Solves |
|------|----------------------------------|-------------------|
| **Dynamic Filtering** | Write code to extract only relevant HTML sections | Raw HTML noise in web search |
| **Code Execution** | Run sandboxed code; only results enter context | Multi-step computation in context |
| **Memory** | Store/retrieve from persistent file directory | Long-conversation context accumulation |
| **Programmatic Tool Calling** | Multi-tool workflows in code; intermediate results stay out | Tool call chain bloat |
| **Tool Search** | Dynamically discover tools without loading all definitions | Large tool library context overhead |

This is a **systematic architectural thesis**: the model's context window should contain only what's immediately relevant to reasoning. Everything else — HTML parsing, computation, memory retrieval, tool discovery — should happen **outside** the context window, with only the processed result loaded in.

#### Agentic Search Implications

Dynamic filtering represents a **convergence point** for the three research threads in agentic search:

1. **IR Research → Production**: The Level 1 finding that BM25+re-ranking outperforms dense retrieval for agents finds its production counterpart in dynamic filtering — not as a separate pipeline but as **model-authored, query-specific filtering code**. The model becomes both the retriever and the re-ranker, writing bespoke extraction rather than relying on a generic ranker.

2. **Harness Engineering → API Integration**: Turnbull's outer loop (validator → "try harder" → re-search) is now partially **absorbed into the API**. Instead of the harness telling the agent to re-query, Claude filters out irrelevant results before they reach the reasoning step — preventing the need for corrective feedback loops in the first place.

3. **Externalized Processing → Default Behavior**: What Cao et al. demonstrated as an emergent capability (coding agents using file systems for text processing) is now **productized as default behavior** for web search. This validates that externalized processing is not just for niche long-context problems — it's the right default for all token-intensive agent tasks.

#### Open Questions

Despite the clear gains, several questions remain:

- **Cost asymmetry**: Price-weighted tokens decreased for Sonnet 4.6 but **increased for Opus 4.6** — the stronger model writes more elaborate filtering code, partially offsetting context savings. This suggests a model-size-dependent sweet spot.
- **Generality vs. specialization**: Dynamic filtering is tuned for web search. Can the same approach generalize to other token-heavy agent tasks (codebase exploration, document analysis)?
- **The eval contamination risk**: Dynamic filtering runs in the same BrowseComp evaluation where [[concepts/eval-awareness-browsecomp|eval awareness]] was discovered — the model's ability to write and execute code during web search creates new attack surfaces for benchmark contamination that static retrieval pipelines don't have.
- **Relationship to RLM**: The code execution inside context mirrors [[concepts/rlm-recursive-language-models|RLM]]'s "context as variable" pattern — but ephemerally rather than persistently. A natural next step would be persistent code execution across turns, blurring the line between search filtering and agent memory.

---

## Experimental Setup (BrowseComp-Plus)

The IR-layer findings are based on:

- **Dataset**: BrowseComp-Plus — 830 fact-seeking, reasoning-intensive queries
- **Corpus**: 100,195 documents; 2,772,255 passages
- **Judgments**: Human-verified "gold" (contains answer) and "evidence" (supports reasoning)
- **Agents**: gpt-oss-20b (131K context), GLM-4.7-Flash 30B (200K context)
- **Retrievers**: BM25, SPLADE-v3, ColBERTv2, RepLLaMA, Qwen3-Embed
- **Re-rankers**: monoT5-3B, RankLLaMA-7B, Rank1-7B

---

## Level 4: Process/Methodology — Agile Engineering Framework

Daniel Tunkelang & Asif Makhani (Infino AI) propose that agentic search is best understood as an **agile engineering process** — not a one-time implementation but a continuous, adaptive control system for reasoning under uncertainty. [[raw/articles/2026-03-26_daniel-tunkelang_agentic-search-agile-engineering.md]]

### Core Analogy: Searchers as Product Owners, Agents as Engineers

| Agile Role | Agentic Search Equivalent |
|------------|--------------------------|
| **Product Owner** | Searcher — defines and prioritizes the information need |
| **Engineers** | Agents — own all aspects of execution (plan, decompose, execute, verify, refine) |

Unlike software iterations measured in days, agentic search iterations are measured in **minutes or seconds** — making the loop tighter, faster, and more volatile.

### The Scope–Cost–Quality Triangle

| Dimension | Definition |
|-----------|-----------|
| **Scope** | How much of the problem space the search covers |
| **Cost** | Aggregate spend on tokens, tool calls, computation |
| **Quality** | Correctness, completeness, and confidence |

**Three strategies** correspond to different agentic search modes:
1. **Fixed cost + quality, reduce scope** → narrow focus, high-confidence paths, early stopping (default strategy)
2. **Fixed scope + quality, increase cost** → broader exploration, aggressive verification ("deep research" mode)
3. **Fixed scope + cost, sacrifice quality** → skimming, summarization ("quick overview" mode)

### Uncertainty Reduction as the Core Metric

Each step should be evaluated by **how much uncertainty it removes per unit of cost**. This reframes agentic search as a sequence of uncertainty-reducing experiments.

### Evaluation-Driven "Definition of Done"

> "The shift — from execution to evaluation — is what turns search into an engineering problem."

The question is never "How many steps remain?" but **"Is further work worth the cost?"** An agentic system is "done" when spending more is not expected to improve outcome quality.

**What to evaluate:**
- **Outcome:** correctness, completeness, usefulness
- **Process:** validation of exploration and verification strategies
- **Efficiency:** maximization of ROI, minimization of wasted effort

### Task Sizing Tradeoff

A central underexplored design decision: larger tasks increase efficiency by reducing coordination overhead but increase risk. Smaller tasks reduce risk but decrease efficiency. The optimal tradeoff balances coordination cost against the expected cost of errors.

### Predictability vs. Evaluability

Forcing predictability (fixed step count, shallow exploration) leads to worse outcomes. Instead, replace predictability with **evaluability** — the ability to test whether further work is justified. This is the same tradeoff agile development makes.

### Design Principles

1. Prioritize steps that maximize uncertainty reduction per unit of spend
2. Dynamically adjust scope based on budget and confidence
3. Size tasks to balance coordination costs against expected costs of errors
4. Integrate verification into iteration and refinement processes
5. Define and enforce evaluation-driven stopping criteria

## Level 5: Steering/Harness — Agentic Design Patterns for Search

Doug Turnbull's "Cheat at Search: Steering Lost Agents" (May 2026) provides a practical code-level catalog of steering patterns for directing LLM agents within search harnesses. This is the third installment of the Cheat at Search series, following evaluation/NDCG (Part 1) and LLM query understanding (Part 2). [[raw/articles/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents]]

### The Carrot and Stick Model

Turnbull frames agent steering as a **carrot 🥕 and stick 🏒** problem:
- **Carrot**: Priming with few-shot examples, query expansion, skills/query plan lookups — give the agent better starting points
- **Stick**: Tool guards, validation rules, LLM judges, state-based rejection — redirect when the agent goes off course

### Steering Patterns Catalog

| Pattern | Mechanism | When to Use |
|---------|-----------|-------------|
| **Ralph Loop** | Simple retry loop (up to N times) | Early prototyping, basic convergence |
| **Rule-Based Validation** | Objective criteria check that returns corrective user message | Clear quality thresholds (count, format, fields) |
| **LLM-as-Judge** | Dedicated LLM evaluates quality, returns natural language feedback | Subjective quality, relevance judgment |
| **Reranker in Response** | Harness runs quality model, injects result as user feedback | Systematic quality enforcement without tool-call dependency |
| **Priming (Few-Shot)** | Concrete relevance examples in system prompt | Highest ROI pattern (+0.0087 NDCG over FS Tools baseline) |
| **Query Expansion** | LLM interprets query into detailed formulation before agent starts | Ambiguous/short user queries |
| **Skills/Query Plan** | Vector DB lookup of "how to search for X" → inject into prompt | Domain-specific search strategies managed by dev team |
| **Tool Guards** | Tools inspect agent_state, reject redundant/invalid calls | Preventing repeated exploration, enforcing constraints |
| **Subagent Delegation** | Orchestrator spawns subagents with fresh context for independent tasks | Long-running searches, multiple start positions |

### Empirical Results (WANDS Dataset)

Layering steering patterns produces progressive NDCG improvements on the WANDS e-commerce dataset (~45K products):

| Variant | Mean NDCG | Δ from baseline |
|---------|-----------|-----------------|
| BM25 (no agent) | 0.5408 | — |
| Agentic + FS Tools (`ls`/`grep`/`cat` over filesystem) | 0.5565 | +0.0157 |
| + Few-Shot Priming | 0.5652 | +0.0244 |
| + Subagent Delegation | 0.5661 | +0.0253 |

**Key finding:** Few-shot priming provides the largest marginal improvement per steering pattern added. Simple tools (constrained filesystem metaphors) outperform complex search APIs — the agent's reasoning compensates for tool simplicity.

### Design Principles

1. **Agent picks tools; developer controls tool responses** — tool responses ARE prompt engineering
2. **Harness > Model** — the control loop matters more than which specific model runs inside it
3. **User-feedback messages steer better than system instructions** — leverage training bias toward user satisfaction
4. **Start with dumb retrievers, add complexity only when data proves it's needed** — simple BM25 + smart steering beats premature complexity
5. **Delegate to subagents with fresh context** — prevents context rot in long-running searches

For a comprehensive treatment of these patterns, see the dedicated [[concepts/harness-engineering/agent-steering]] concept page.

### Search as Code: Programmable Search Primitives (June 2026)

Perplexity's **Search as Code (SaC)** architecture represents the latest evolution in agentic search, moving beyond function calling and MCP to give agents **direct code-level control** over search pipeline internals. [[raw/articles/2026-06-01_perplexity-rethinking-search-as-code-generation]] [[concepts/search-as-code]]

#### The Three-Layer Architecture

SaC replaces the monolithic "query → pipeline → resultset" pattern with three layers:
1. **Models** as control plane (reason, decompose tasks, generate code)
2. **Compute Sandboxes** for deterministic execution (secure Python runtime)
3. **Agentic Search SDK** exposing composable primitives (retrieval, ranking, filtering, fanouts, rendering)

#### Why SaC? Three Failure Modes of Traditional Search

Traditional search creates three recurring failure modes for agent workflows:

| Failure Mode | Traditional Search | SaC Solution |
|-------------|-------------------|--------------|
| **Coarse context** | One pipeline fits all queries; suboptimal retrieval pollutes context | Agent composes task-specific pipelines from primitives |
| **No domain knowledge leverage** | Model can't influence ranking/filtering logic | Agent writes code blending signals, prioritizing sources |
| **Inefficient control flow** | Sequential model turns for fan-out, parallel, dedup | Agent orchestrates nonlinear/asynchronous operations in sandbox |

#### Connection to PTC

SaC is essentially **PTC applied to the search layer**: both use model-generated Python code to orchestrate operations in sandboxes, achieving 85-92% token reduction. The key difference is that SaC provides a **domain-specific SDK** (search primitives) while PTC uses a **general-purpose IPC protocol** (arbitrary tools).

#### Benchmark Results

SaC achieves SOTA on 4/5 benchmarks (DSQA, BrowseComp, WideSearch, WANDR) and ties OpenAI on HLE. On the new WANDR benchmark for "wide research" tasks, SaC leads the next-best system by 2.5×.

#### Autoresearch-Driven SDK Optimization

Perplexity runs a continuous autoresearch loop over the SDK, proposing and validating improvements against latency, codegen quality, and task performance metrics. Combined with optimized Agent Skills (under 2000 tokens), this enables models to effectively compose search primitives without extensive pretraining on the SDK.

#### Intermediate State Management

SaC tested filesystem-based serde vs REPL for persisting state across turns. Filesystem serde was selected for better reliability on long trajectories — requiring models to convey state declaratively rather than implicitly improves state management effectiveness.

Sources: [[raw/articles/2026-06-01_perplexity-rethinking-search-as-code-generation]], [[concepts/programmatic-tool-calling]], [[concepts/search-as-code]]

### Three Paradigms of Agentic Search (Turnbull, June 2026)

Doug Turnbull's *Three kinds of agentic search* [[raw/articles/2026-06-08_softwaredoug_three-kinds-of-agentic-search]] offers a practitioner taxonomy that complements the academic frameworks above. Rather than organizing by IR layer or harness architecture, Turnbull categorizes by **how much agency the agent has over the search process**.

#### Paradigm 1: Agent-Assisted Search

The most familiar pattern — an agent refines, expands, or disambiguates queries before passing them to a traditional search engine. The search engine itself doesn't change; the agent is a wrapper that improves the **query side** of the equation. Examples: query reformulation, clarification questions, multi-query decomposition.

> This is where most "AI search" products are today. Valuable but incremental — you're still fundamentally doing keyword/BM25/vector retrieval.

#### Paradigm 2: Agent-Driven Search

The agent decides **what** to search, **when** to search, and **how** to search. It orchestrates multiple retrieval steps in a loop: *think → decide whether to search → search → observe → think again*. It can mix search with computation, code execution, or API calls, and maintains working memory across iterations.

Examples: Perplexity's research mode, Google's AI Overviews.

> The challenge: **search quality becomes agent quality**. A bad agent with a great search engine will produce worse results than a great agent with a mediocre search engine.

#### Paradigm 3: Agent-Native Search

The paradigm shift — search infrastructure designed **from the ground up** for agent consumption, not human consumption. Structured, machine-readable results instead of HTML; APIs over scraping; semantic indexing at the fact/claim level (not document level); provenance tracking; composable search primitives.

> If 30% of your traffic comes from agents (and it will), you'll start optimizing for agents the way you optimized for Google's crawler.

#### Architecture Implications

| Paradigm | Investment Focus | Existing Concept Page Mapping |
|----------|-----------------|-------------------------------|
| **Agent-assisted** | Query understanding | Level 1 (IR): Q2Q reformulation, query expansion |
| **Agent-driven** | Orchestration | Level 2 (Harness): Two-loop architecture, steering patterns, SaC |
| **Agent-native** | Data layer | Level 3 (Externalized Processing): DCI, structured APIs, composable primitives |

Turnbull's key insight: most organizations will need all three simultaneously. The dirty secret is that these aren't just "search with AI sprinkled on top" — they're fundamentally different interaction patterns requiring different infrastructure, different quality metrics, and different product thinking.

> *Start with agent-assisted. It's the easiest win. But start planning for agent-native now, because the web of 2028 will look very different from the web of 2024.*

---

## Related Concepts

- [[concepts/search-as-code]] — Perplexity's Search as Code (SaC) architecture
- [[concepts/programmatic-tool-calling]] — General pattern of code-orchestrated tool calls (PTC is SaC's cousin)
- [[concepts/direct-corpus-interaction]] — DCI: replacing retrieval with grep/bash/shell pipelines
- [[concepts/markdown-based-skills]] — Skills format used by agentic search (harness layer)
- [[concepts/s3-first-architecture]] — Where skills files are stored
- [[concepts/harness-engineering/agent-harness]] — Agentic search is part of the harness layer

## Related Course Materials

- **Cheat at Search** (Maven, Doug Turnbull) — The definitive practitioner course on search with LLMs and agents. Lecture transcripts in wiki:
  - [[transcripts/2026-05-20_softwaredoug_cheat-at-search-llm-query-understanding-lecture|Lesson 2: LLM Query Understanding]]
  - [[transcripts/2026-05-27_softwaredoug_cheat-at-search-steering-lost-agents-lecture|Lesson 3: Steering Lost Agents]]
  - [[transcripts/2026-05-28_softwaredoug_cheat-at-search-llm-as-judge-lecture|Lesson 4: LLM as Judge]]
  - [[transcripts/2026-06-02_softwaredoug_cheat-at-search-long-running-search-lecture|Lesson 5: Long Running Search Agents]]
  - [[transcripts/2026-06-04_softwaredoug_cheat-at-search-coding-agents-lecture|Lesson 7: Coding Agents & Auto Research]]
- **Production-Ready Agent Engineering** (Maven, Will Brown & Kyle Corbitt) — Companion course on RL for agents. See [[concepts/agents-mcp-rl-course]].

## Related Entities

- [[entities/doug-turnbull-core-ideas]] — Practitioner perspective on agentic search
- [[entities/sheshansh-agrawal]] — Academic IR researcher focused on agentic search

## Sources

- [[raw/articles/2026-04-28_softwaredoug_search-apis-replaced-by-agents]] — Doug Turnbull (2026). Agentic search benchmark on Amazon ESCI: GPT-5 + BM25 + embeddings achieves 0.453 NDCG (+56.7% vs BM25 baseline). Key limitation: agentic search works for "finding things" but not "deep research."
- [Improved Web Search with Dynamic Filtering](https://claude.com/blog/improved-web-search-with-dynamic-filtering) — Anthropic (2026). Official announcement: dynamic filtering uses code execution to pre-process web results. BrowseComp: Sonnet 33.3%→46.6%, Opus 45.3%→61.6%. DeepsearchQA F1: Opus 69.8%→77.3%. ~11% accuracy gain, ~24% token reduction. GA alongside code execution, memory, programmatic tool calling, tool search.
- [Dynamic Filtering in Claude Web Search (GEND)](https://www.gend.co/blog/claude-web-search-dynamic-filtering) — GEND/Anthropic partner (2026). Third-party summary and implementation guide.
- [SID-1 Technical Report: Test-Time Compute for Retrieval](https://www.sid.ai/research/sid-1-technical-report) — SID Research (2025). First RL-trained agentic retrieval model. Qwen3-14B + GRPO, 0.84 recall, TI/TO pipeline insight.
- [Revisiting Text Ranking in Deep Research](https://arxiv.org/abs/2602.21456) — Meng, Ou, MacAvaney, Dalton (2026). Systematic evaluation of IR methods in deep research contexts.
- [Coding Agents are Effective Long-Context Processors](https://arxiv.org/abs/2603.20432) — Cao, Yin, Dhingra, Zhou (2026). Coding agents as retrieval/processing interface outperforming traditional IR on long-context tasks.
- [Beyond Semantic Similarity: Direct Corpus Interaction for Agentic Search](https://arxiv.org/abs/2605.05242) — Li, Zhang, Wei, Lu, Nie et al. (2026). DCI: replacing retrieval with grep/bash/shell pipelines. BrowseComp-Plus 80.0% (+11 pts), multi-hop QA 83.0 (+30.7 pts), IR ranking NDCG 68.5 (+21.5 pts). [[raw/papers/2026-05-03_2605.05242_direct-corpus-interaction]]
- [Agentic Search Is Having a Grep Moment](https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment) — Doug Turnbull (2026). Practitioner perspective on grep vs search harness architecture.
- [RAG Users Want Affordances, Not Vectors](https://softwaredoug.com/blog/2025/12/09/rag-users-want-affordances-not-vectors) — Doug Turnbull (2025). Foundational critique of vector-centric RAG: embedding crowding, threshold problem, in-domain nuance, and the affordance-based alternative of structured schema extraction via LLMs.
- [Rag is the What. Agentic search is the How. (YouTube)](https://www.youtube.com/watch?v=UXQ916WRK0A) — Doug Turnbull (2026). 54-minute talk: full architectural critique of RAG paradigm shift toward agentic search, with four-stage unwinding and SID-1 endorsement.
- [How To Build Your First Agentic Search Application (YouTube)](https://www.youtube.com/watch?v=AJPH9kpN3Sc) — Doug Turnbull (2026, Vanishing Gradients). 35-minute interview: passive→active spectrum, tool-calling loop, harness validation, long-running agents, build-vs-buy.
- [Why 2026 is The Year of Agentic Search (YouTube)](https://www.youtube.com/watch?v=h370222tnAQ) — Doug Turnbull & Jo Kristian Bergum (2026). 65-minute fireside chat: four pillars of agentic search — LLM Query Understanding, Autoresearch (agents writing ranking code), Agentic Search Harnesses, and LLM-as-a-Judge.
- [Lessons from Building AI Agents in Financial Services](raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md) — Agentic search as skill discovery in Fintool.
- [Text Ranking in Deep Research (Code)](https://github.com/ChuanMeng/text-ranking-in-deep-research) — Open-source code and data.
