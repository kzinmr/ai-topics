---
title: "Deep Research"
type: concept
aliases:
  - deep-research
created: 2026-05-22
updated: 2026-05-28
tags:
  - concept
  - deep-research
  - information-retrieval
  - agentic-retrieval
  - search
  - ai-agents
  - agentic-search
  - benchmark
  - evaluation
  - bm25
sources:
  - raw/articles/2026-03-24_hornet_deep-research-is-a-retrieval-problem.md
  - raw/articles/2026-05-20_hornet_this-is-what-agentic-retrieval-looks-like.md
---

# Deep Research

**Deep research** — the AI capability to answer complex, multi-hop questions by searching across large corpora — is fundamentally a **retrieval problem**. While often framed as an end-to-end reasoning challenge, empirical evidence from BrowseComp-Plus shows that retrieval quality is the dominant bottleneck, not model reasoning capacity.

## The Retrieval Bottleneck

The clearest evidence comes from **oracle retrieval experiments** on BrowseComp-Plus — a multi-hop question answering benchmark with 100,195 web pages (~736M tokens), 830 riddle-like questions, and human-annotated evidence documents.

| Setting | Model | Accuracy |
|---------|-------|----------|
| Oracle (perfect retrieval) | GPT-4.1 | **93.49%** |
| Weak BM25 baseline | GPT-4.1 | **14.58%** |
| Oracle (perfect retrieval) | Qwen3-32B | **83%** |
| Search tool | Qwen3-32B | **<5%** |

When given the right documents upfront (oracle setting), models answer correctly at very high rates. When forced to find those documents themselves with even a weak retriever, accuracy collapses. The **~79-point gap** persists across model tiers — it's not a reasoning limitation, it's a retrieval limitation.

> "The oracle result is the clearest signal. GPT-4.1 answers 93.49% correctly with perfect retrieval, 14.58% with weak BM25. That gap is hard to explain without retrieval playing a major role."
> — Jo Kristian Bergum, Hornet blog, Part 1

## Why Context Windows Don't Solve This

A 128k context window holds ~0.017% of the BrowseComp-Plus corpus. A 1M window holds ~0.14%. **There is no fitting the corpus into the prompt.** Agents must search, and retrieval determines what slice of the corpus they ever get to read.

Furthermore, standard evaluation protocols truncate snippets to **512 tokens** — the answer may be in the retrieved document but past the visible window. This is a failure mode independent of document-level retrieval quality.

## Three Layers the Leaderboard Compresses

The headline accuracy number folds together three distinct evaluation layers:

| Layer | What it measures | Key insight |
|-------|-----------------|-------------|
| **One-shot retrieval** | Retriever quality for single-query (Recall@K, nDCG@10) | Lexical vs. embedding gap |
| **Session-level recall** | Cumulative evidence retrieved across all agent queries | A strong one-shot retriever can fail if the agent formulates weak queries |
| **End-to-end accuracy** | Final answer correctness (the leaderboard number) | Right docs ≠ right answer (snippet truncation, reasoning failures) |

Each layer isolates a different part of the system. The headline number alone does not tell you what is actually constraining performance.

## Agentic Query Workload

Deep research agents don't query like humans. From Part 2's analysis of 19,279 search calls across 830 BrowseComp-Plus questions:

- **Median 10-term queries** (vs. human median 2 terms)
- **24 search calls per question** (median)
- **Phrase quotes in 98% of sessions**
- **`site:` operators in 48% of sessions**
- Queries narrow as evidence accumulates: turn 1 averages 19.1 terms, plateauing near 10

This workload is fundamentally out-of-distribution for retrievers trained on MS MARCO and Natural Questions (short, fluent natural-language queries).

## The Evaluation Challenge

Traditional IR benchmarks evaluate single-shot retrieval. Deep research requires evaluating **iterative, conditioning retrieval** — where each search call depends on the results of previous calls, and errors compound across sessions.

Part 3 (forthcoming) examines why BM25 looks weak in one-shot but considerably stronger inside the agent loop, challenging how retrieval should be evaluated for deep research workloads.


## NVIDIA AI-Q: Open-Source Deep Research Agent (May 2026)

[[entities/nvidia]] released **NVIDIA AI-Q**, an open-source reference architecture for enterprise deep research agents. It ranks #1 on both [DeepResearch Bench I (55.95)](https://paperswithcode.com/sota/deep-research-bench-i?p=deep-research-is-a-retrieval-problem) and DeepResearch Bench II (54.50), beating OpenAI's closed system.

### Architecture

Two-tier routing: Intent Classifier → Shallow (fast, bounded) or Deep (multi-phase).

Deep Researcher orchestrated by LangGraph StateGraph with three roles:
- **Planner**: Scout (maps info landscape) + Architect (designs evidence-grounded plan)
- **Researcher**: 5 specialist sub-agents in parallel (Evidence Gatherer, Mechanism Explorer, Comparator, Critic, Horizon Scanner)
- **Orchestrator**: Coordinates loop, fills gaps, synthesizes report

### Key Design Decisions
- **Evidence-grounded planning**: Planner scouts before committing to structure
- **Context isolation**: Each subagent works in its own context window, returns only synthesis
- **Configurable via YAML**: Swap models, tools, depth thresholds without code changes

### Training Pipeline
- **Teacher model**: GPT-OSS-120B generated 80k trajectories
- **Filtering**: Judge model (Qwen3-Nemotron-32B-GenRM-Principle) filtered → 67k survived
- **Student**: Fine-tuned Nemotron-3-Super-120B-A12B on 16 nodes × 8 H100 GPUs (~25 hours, 5,615 steps)

### Enterprise Integration
- MCP server support for enterprise data sources
- Docker Compose and Helm charts (laptop to air-gapped data center)
- SKILL.md integration with Claude Code, Codex, Hermes Agent harnesses

Sources: [NVIDIA Developer Blog](https://developer.nvidia.com/blog/add-a-specialized-deep-research-skill-to-agent-harnesses/), [GitHub: NVIDIA-AI-Blueprints/aiq](https://github.com/NVIDIA-AI-Blueprints/aiq)

## Related Concepts

- [[concepts/agentic-retrieval]] — The paradigm where AI agents (not humans) are the primary search consumers
- [[concepts/hornet]] — The retrieval engine purpose-built for this agentic query workload
- [[concepts/agentic-search]] — Broader framework covering IR search layer, harness engineering, and agile engineering
- [[concepts/reasoning-aware-retrieval]] — Jointly embedding agent reasoning traces with search queries (AgentIR-4B, 2026)
- [[concepts/bm25]] — Classical lexical retrieval; performs differently in agent loops vs. one-shot
- [[concepts/deep-research-agent-from-scratch]] — Building research agents from scratch (Hugo Bowne-Anderson + Ivan Leo workshop)
- [[concepts/browsecomp]] — The BrowseComp benchmark series
- [[concepts/mutually-assured-distraction]] — Better retrieval → more convincing distractors → more confidently wrong answers
- [[concepts/context-window-management]] — Why long context doesn't eliminate retrieval needs

## Key Sources

- [Deep research is a retrieval problem](https://hornet.dev/blog/deep-research-is-a-retrieval-problem) — Part 1 (Jo Kristian Bergum, Mar 2026)
- [This is what agentic retrieval looks like](https://hornet.dev/blog/this-is-what-agentic-retrieval-looks-like) — Part 2 (Jo Kristian Bergum, May 2026)
- [The context window is not your database](https://hornet.dev/blog/the-context-window-is-not-your-database) — Skip Everling, Hornet blog (Feb 2026)
- BrowseComp-Plus benchmark paper and leaderboard
