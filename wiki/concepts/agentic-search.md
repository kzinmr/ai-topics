---
title: Agentic Search
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [search, ai-agents, information-retrieval, deep-research, reranking, coding-agents, rl-training]
aliases:
  - deep-research-retrieval
  - agent-query-mismatch
  - externalized-processing
  - agentic-retrieval
sources:
  - raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md
  - raw/papers/2026-02-25_2602.21456_revisiting-text-ranking-in-deep-research.md
  - raw/papers/2026-03-20_2603.20432_coding-agents-effective-long-context-processors.md
  - raw/articles/2025-12-04_sid-1-agentic-retrieval.md
  - raw/articles/2026-04-06_softwaredoug-agentic-search-grep-moment.md
  - raw/articles/2026-03-30_claude-web-search-dynamic-filtering.md
  - raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how.md
  - raw/articles/2025-12-09_doug-turnbull-rag-users-want-affordances.md
  - raw/articles/2026-02-20_doug-turnbull-build-first-agentic-search-app.md
  - https://arxiv.org/abs/2602.21456
  - https://arxiv.org/abs/2603.20432
  - https://www.sid.ai/research/sid-1-technical-report
  - https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment
  - https://www.gend.co/blog/claude-web-search-dynamic-filtering
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

### Re-ranking Architecture

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

| Metric | Improvement |
|--------|-------------|
| Search accuracy | ~11% average |
| Input tokens used | ~24% fewer |
| DeepsearchQA F1 (Sonnet 4.6) | 52.6% → 59.4% |
| DeepsearchQA F1 (Opus 4.6) | 69.8% → 77.3% |

#### Technical Requirements

- **Models**: Opus 4.6 / Sonnet 4.6
- **Tool versions**: `web_search_20260209` or `web_fetch_20260209`
- **Beta header**: `anthropic-beta: code-execution-web-tools-2026-02-09`
- **Dependency**: Code Execution tool must be enabled (free when used with web tools; standard token costs apply)

#### Connection to the Three-Level Framework

This implementation validates patterns from all three levels:

- **Level 1 (IR)**: The code execution acts as a just-in-time filter, mirroring the re-ranking stage but at the code level rather than with a separate ranker model
- **Level 2 (Harness)**: The harness (Claude API infrastructure) orchestrates the tool flow — search → script → sandbox → context — without the agent needing to manage each step
- **Level 3 (Externalized Processing)**: This is the most direct validation — Claude replaces latent attention (internal HTML parsing) with explicit code execution (script-based extraction), exactly as the Cao et al. paper prescribes, but at the web search layer rather than the file system layer

The key difference from the Cao et al. approach: instead of organizing text in filesystems, Claude uses code execution as an ephemeral processing pipeline for each web fetch. Both externalize processing from the model's internal attention to executable code.

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

## Related Concepts

- [[concepts/markdown-based-skills]] — Skills format used by agentic search (harness layer)
- [[concepts/s3-first-architecture]] — Where skills files are stored
- [[concepts/agent-harness]] — Agentic search is part of the harness layer

## Related Entities

- [[entities/doug-turnbull-core-ideas]] — Practitioner perspective on agentic search
- [[entities/sheshansh-agrawal]] — Academic IR researcher focused on agentic search

## Sources

- [Dynamic Filtering in Claude Web Search](https://www.gend.co/blog/claude-web-search-dynamic-filtering) — Anthropic (2026). Production implementation of externalized processing: Claude writes code to filter web results before context loading. ~11% accuracy gain, ~24% token reduction.
- [SID-1 Technical Report: Test-Time Compute for Retrieval](https://www.sid.ai/research/sid-1-technical-report) — SID Research (2025). First RL-trained agentic retrieval model. Qwen3-14B + GRPO, 0.84 recall, TI/TO pipeline insight.
- [Revisiting Text Ranking in Deep Research](https://arxiv.org/abs/2602.21456) — Meng, Ou, MacAvaney, Dalton (2026). Systematic evaluation of IR methods in deep research contexts.
- [Coding Agents are Effective Long-Context Processors](https://arxiv.org/abs/2603.20432) — Cao, Yin, Dhingra, Zhou (2026). Coding agents as retrieval/processing interface outperforming traditional IR on long-context tasks.
- [Agentic Search Is Having a Grep Moment](https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment) — Doug Turnbull (2026). Practitioner perspective on grep vs search harness architecture.
- [RAG Users Want Affordances, Not Vectors](https://softwaredoug.com/blog/2025/12/09/rag-users-want-affordances-not-vectors) — Doug Turnbull (2025). Foundational critique of vector-centric RAG: embedding crowding, threshold problem, in-domain nuance, and the affordance-based alternative of structured schema extraction via LLMs.
- [Rag is the What. Agentic search is the How. (YouTube)](https://www.youtube.com/watch?v=UXQ916WRK0A) — Doug Turnbull (2026). 54-minute talk: full architectural critique of RAG paradigm shift toward agentic search, with four-stage unwinding and SID-1 endorsement.
- [How To Build Your First Agentic Search Application (YouTube)](https://www.youtube.com/watch?v=AJPH9kpN3Sc) — Doug Turnbull (2026, Vanishing Gradients). 35-minute interview: passive→active spectrum, tool-calling loop, harness validation, long-running agents, build-vs-buy.
- [Lessons from Building AI Agents in Financial Services](raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md) — Agentic search as skill discovery in Fintool.
- [Text Ranking in Deep Research (Code)](https://github.com/ChuanMeng/text-ranking-in-deep-research) — Open-source code and data.
