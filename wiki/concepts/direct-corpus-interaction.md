---
title: "Direct Corpus Interaction (DCI)"
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - direct-corpus-interaction
  - search
  - lexical-search
  - coding-agents
  - ai-agents
  - tool
  - benchmark
  - terminal
aliases:
  - DCI
  - grep-based retrieval
  - retrieval-free search
  - terminal-tool retrieval
sources:
  - raw/papers/2026-05-03_2605.05242_direct-corpus-interaction.md
  - https://arxiv.org/abs/2605.05242
  - https://github.com/DCI-Agent/DCI-Agent-Lite
related:
  - concepts/agentic-search
  - concepts/agentic-rag
---

# Direct Corpus Interaction (DCI)

> **"The best retriever ... is no retriever."** — DCI replaces the entire embedding → vector-index → top-k retrieval pipeline with general-purpose terminal tools (`grep`, `find`, `bash`, shell pipelines), letting an agent search raw text directly.

## Definition

**Direct Corpus Interaction (DCI)** is an alternative retrieval paradigm for agentic search where an AI agent searches the raw corpus directly using general-purpose terminal tools — without any embedding model, vector index, offline indexing, or retrieval API. The agent orchestrates its own search trajectory on raw text, like a developer navigating a codebase with `grep`, `find`, and shell pipelines.

DCI was introduced by Li et al. (2026) [[raw/papers/2026-05-03_2605.05242_direct-corpus-interaction]] from a cross-institutional collaboration spanning Texas A&M, Waterloo, Stanford, Washington, UIUC, UC San Diego, Verdent AI, and Lambda.

## Core Insight

Traditional retrievers (sparse, dense, reranking) compress corpus access into a fixed similarity step. This abstraction becomes a bottleneck for agentic tasks requiring:

- **Exact lexical constraints** (specific strings, IDs, codes)
- **Sparse clue conjunctions** (combining multiple weak signals)
- **Local context checks** (reading surrounding text after a match)
- **Multi-step hypothesis refinement** (revising the search based on what was found)
- **Recovery of filtered evidence** (evidence that a top-k retriever dropped early)

DCI eliminates the retriever bottleneck by giving the agent **direct, high-resolution access** to the raw corpus via terminal tools.

## How It Works

```
Traditional Retrieval:
  Query → Embedding Model → Vector Index → Top-k Retrieval → Agent

DCI:
  Query → Agent → grep/find/bash/shell-pipelines → Raw Corpus
                ↑___________________________________________↓
                         iterative refinement loop
```

Instead of a fixed retrieval API, the agent:
1. Issues a `grep` for a specific term or pattern
2. Opens matching files to read surrounding context
3. Extracts new entities or constraints from localized evidence
4. Launches follow-up searches grounded in discovered evidence
5. Writes lightweight scripts for aggregation when needed

## Implementations

The paper provides two DCI agent implementations:

### DCI-Agent-Lite (Minimal)
- Lightweight Pi-based terminal agent
- Uses **only** `bash` and `read` tools
- Runtime context management (truncation + compaction) for long-horizon search
- Base model: GPT-5.4 nano (budget setting)

### DCI-Agent-ClaudeCode (CC)
- Built on Claude Code harness
- Disables web-search, web-fetch, and subagents
- Base model: Claude Sonnet 4.6
- Represents a mature coding-agent harness

## Performance

### BrowseComp-Plus (Agentic Search)
| Setup | Accuracy | Cost |
|-------|----------|------|
| Retrieval Agent + Qwen3-Embedding-8B | 69.0% | $1,440 |
| **DCI-Agent-CC** | **80.0%** | **$1,016** |

**+11.0 points accuracy gain, −29.4% cost** with the same Sonnet 4.6 backbone.

### Multi-Hop QA
| Setup | Avg Accuracy |
|-------|-------------|
| ASearcher-Local-14B (best retrieval agent) | 52.3 |
| **DCI-Agent-CC** | **83.0** |

**+30.7 points** over the strongest retrieval-agent baseline.

### IR Ranking (BRIGHT + BEIR)
| Setup | Avg NDCG@10 |
|-------|------------|
| ReasonRank (best retrieval baseline) | 47.0 |
| **DCI-Agent-CC** | **68.5** |

**+21.5 points** over the best retrieval baseline.

### Generality Check
DCI-Agent-Lite (minimal harness, GPT-5.4 nano) also consistently outperforms conventional retrievers — confirming the DCI **interface** drives the gains, not the specific harness or model.

## Why DCI Works: Mechanism Analysis

The ablation studies (6 research questions) reveal DCI's advantage is not about better recall:

> Among 176 BrowseComp-Plus questions that DCI-Agent-CC correctly answers but the retrieval agent misses, only 34 contain no gold documents in the conventional retriever's results.

DCI's edge comes from **better evidence utilization** — fine-grained discovery, composition, and use of evidence through flexible, compositional bash commands:

1. **Targeted follow-up**: After a grep match, the agent reads surrounding context and extracts new search terms grounded in localized evidence
2. **Compositional queries**: Shell pipelines combine multiple weak signals (`grep X | grep Y`)
3. **No information loss**: Evidence isn't filtered out by an opaque top-k step
4. **Adaptive strategy**: The agent switches between grep, find, file reads, and scripts based on what it discovers

## Context Management

DCI uses runtime context management to handle long-horizon search where repeated tool calls accumulate observations:

| Level | Truncation | Compaction | Summarization | BrowseComp-Plus Acc |
|-------|-----------|------------|---------------|---------------------|
| L0 | ✗ | ✗ | ✗ | 72 |
| L1 | ✓ (50K) | ✗ | ✗ | 72 |
| L2 | ✓ (20K) | ✗ | ✗ | 69 |
| **L3** | **✓ (20K)** | **✓** | **✗** | **77** |
| L4 | ✓ (20K) | ✓ | ✓ | 73 |

**L3 (truncation + compaction)** achieves the best accuracy, despite retaining less gold evidence than L1. More aggressive summarization (L4) degrades performance — selective discarding of old observations is beneficial, but summarization loses critical detail.

## Relationship to Other Approaches

### vs. Coding Agents as Retrieval (Cao et al., 2026)
Cao et al. showed coding agents can outperform retrievers on BrowseComp-Plus by organizing text into file-system structures. DCI generalizes this: **no file-system pre-organization needed** — the agent directly searches raw, unorganized corpora.

### vs. Agentic Search / Retrieval Augmentation
[[concepts/agentic-search]] covers techniques to improve conventional retrievers for agent-issued queries (Q2Q reformulation, AgentIR joint embedding, SID-1 RL training). DCI takes the opposite approach: **eliminate the retriever entirely** rather than optimize it.

### vs. SID-1
SID-1 [[concepts/agentic-search|Level 1: RL-Trained Retrieval]] is an RL-trained model that uses search tools via a retrieval backend. DCI removes the backend — the agent interacts with raw text, not a retrieval API.

### vs. RAG
Traditional RAG [[concepts/agentic-rag]] embeds documents into a vector index. DCI requires **zero preprocessing**: no chunking, no embedding, no indexing. The corpus is ready immediately.

## Practical Implications

1. **Zero setup cost**: No embedding models, no vector databases, no indexing pipelines. Point the agent at a directory of text files.
2. **Immediate corpus updates**: New documents are searchable instantly — no re-indexing.
3. **Auditable search**: Every grep, file read, and shell command is visible in the agent's trajectory.
4. **Lower cost**: DCI-Agent-CC on BrowseComp-Plus costs 29.4% less than the retrieval-agent equivalent.
5. **General interface**: Any terminal-equipped agent harness can use DCI — no retriever-specific integration needed.

## Limitations

- **Requires a capable coding agent**: DCI depends on the agent's ability to use terminal tools effectively — weaker models may struggle with grep syntax and shell pipelines
- **Corpus must be accessible as files**: DCI works on local or mounted file systems, not on API-accessed databases
- **Context management is critical**: Long-horizon searches accumulate observations that must be managed to stay within context windows
- **Not always cheaper than RAG**: For simple lookups, a vector index may be more efficient than iterative grep

## The McLuhan Thesis

The paper frames DCI through Marshall McLuhan's media theory:

> *"The medium shapes and controls the scale and form of human association and action."*

The **retrieval interface** is the medium through which agents perceive external corpora. A similarity-based interface (embeddings → top-k) shapes what agents can discover. DCI proposes a **higher-resolution interface** — direct terminal access — that enables qualitatively different search behaviors. As language agents become stronger, the interface resolution may matter as much as reasoning capability.

## Resources

- **Paper**: [arXiv:2605.05242](https://arxiv.org/abs/2605.05242)
- **Code**: [DCI-Agent/DCI-Agent-Lite](https://github.com/DCI-Agent/DCI-Agent-Lite)
- **Demo**: [Hugging Face Space](https://huggingface.co/spaces/DCI-Agent/demo)
- **Eval Logs**: [Hugging Face Dataset](https://huggingface.co/datasets/DCI-Agent/eval-logs)
