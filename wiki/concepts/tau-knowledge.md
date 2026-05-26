---
title: "τ-Knowledge"
type: concept
aliases:
  - tau-knowledge
  - τ-Knowledge
created: 2026-05-08
updated: 2026-05-08
tags:
  - benchmark
  - fintech
  - evaluation
  - company
sources:
  - raw/papers/2026-03-04_2603.04370_tau-knowledge-unstructured-knowledge.md
  - raw/articles/sierra.ai--blog-tau-knowledge--5dda7a09.md
---

# τ-Knowledge

**τ-Knowledge** extends [[concepts/tau-bench|τ-Bench]] to evaluate conversational agents' ability to search, reason, and combine information from **unstructured knowledge bases** (internal documents, policy manuals, product catalogs, etc.) with tool operations to complete tasks. Published in March 2026 by Quan Shi, Alexandra Zytek, Pedram Razavi, Karthik Narasimhan, and Victor Barres.

> Paper: [arXiv:2603.04370](https://arxiv.org/abs/2603.04370) "τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge"

## Background and Motivation

Traditional agent evaluation (including τ-Bench) assumed that tool specifications and policies were given as **structured API definitions**. In the real world, however, knowledge workers must find, understand, and act on information from **unstructured text** — internal wikis, PDF manuals, product catalogs, policy documents.

τ-Knowledge was designed to fill this gap. Agents must **autonomously discover what is written where**, traverse cross-references between documents, and integrate fragmented information to make correct decisions.

## τ-Banking Domain

The core domain of τ-Knowledge is **τ-Banking**.

| Item | Value |
|------|-------|
| Knowledge documents | 698 |
| Product categories | 21 |
| Total tokens | ~195K |
| Task types | Account opening/closing, dispute transaction processing, etc. |

Notable design features:

- **Structured-to-unstructured generation pipeline**: To guarantee consistency between documents, a pipeline generates unstructured text from structured data. This mimics the "messiness" of real-world documents while ensuring evaluation reproducibility.
- **Self-discovery of tools**: Available API tool specifications are only referenced within documents. Agents must **discover for themselves** which tools exist and how to invoke them by reading the documents. This is fundamentally different from traditional benchmarks (where tool definitions are explicitly provided).
- **Inter-document connectivity**: The 698 documents cross-reference each other — understanding a single policy requires traversing multiple documents.

## Evaluation Metric: pass^1

τ-Knowledge's primary metric is **pass^1** (probability of completing a task in a single attempt). This reflects real-world deployment scenarios where agents need to respond correctly on the first try.

Each task is evaluated on:
- Policy compliance (adherence to prescribed rules)
- Tool operation accuracy (correct API calls with correct arguments)
- Response appropriateness (conversation quality, information accuracy)

## Key Experimental Results

### GPT-5.2 Performance (Initial Results, March 2026)

| Condition | pass^1 | pass^4 |
|-----------|--------|--------|
| GPT-5.2 (high reasoning) | **~25.5%** | **9.3%** |
| Oracle document provision (directly given needed docs) | **~40%** | - |

This result has two important implications:

1. **Retrieval is a major bottleneck, but not the only one**: Even the strongest model (GPT-5.2, high reasoning) achieves only ~25% success when autonomously exploring the knowledge base.
2. **The understanding/reasoning wall**: Even in the "oracle" condition where needed documents are directly provided, success only reaches 40%. This reveals a second bottleneck of **information understanding, integration, and reasoning** — even with the right information in front of it, correctly interpreting and acting on it remains difficult.

### Frontier Model Evolution (May 2026 Update)

Sierra evaluated 11 frontier model variants at maximum reasoning effort over the two months since the March 2026 initial release. Under standardized retrieval settings (BM25, dense vector search, access to free-form shell with each model able to choose its own search strategy):

| Model | pass^1 | pass^4 | Notes |
|-------|--------|--------|-------|
| GPT-5.2 + high reasoning | 25.5% | 9.3% | Initial release (March 2026) |
| GPT-5.5 + xhigh reasoning | **37.4%** | **20.6%** | Current leaderboard leader |

**GPT-5.5 improvements**: +11.9pt in pass^1, more than 2x improvement in pass^4. Still fails on ~60% of tasks, meaning τ-Knowledge is far from saturated.

### Behavioral Patterns Distinguishing Strong and Weak Agents

Sierra's analysis of thousands of agent trajectories revealed the following behavioral patterns:

1. **Search is continuous, not one-shot**: Weak agents search once at task start and work with those results. Strong agents (especially GPT-5.5) re-search whenever new context emerges in conversation (e.g., when a customer says "actually, this is a medical emergency") to discover new internal protocols.

2. **Search smarter, not more**: GPT-5.5 searched less than half as often as GPT-5.2 (19.4 → 9.1 queries/task) yet improved pass^1 by 12pt. The improvement came from precision, not volume — GPT-5.5 issues surgical queries like "transfer reason codes customer frustrated demands human medical emergency" to identify the correct internal document on the first try.

3. **Knowing when to act and when not to act**: Many models correctly execute expected actions, then add unsolicited "helpful" actions without user permission (e.g., automatically filing fraud disputes alongside card replacement orders). Opus 4.7 is more strictly calibrated on this dimension compared to 4.6.

4. **τ-Banking is not yet solved**: Even the current strongest model leaves ~63pt headroom in pass^1, far from production deployment readiness.

### Retrieval Method Comparison

τ-Knowledge supports multiple retrieval strategies, each with performance-efficiency trade-offs:

| Retrieval Method | Description | Characteristics |
|-----------------|-------------|-----------------|
| **Terminal-style search** (filesystem-based) | Explore documents with commands like `grep`, `cat`, `ls` | High precision but slow. Similar to human knowledge worker search patterns |
| **Dense vector retrieval** | Embedding-based semantic search | Fast, but accuracy drops for specialized terminology and abbreviations |
| **Sparse vector retrieval** | Keyword-based (BM25, etc.) | Strong on vocabulary matching, can be effective for specialized documents |
| **Long-context** | Feed large document sets directly into context window | Limited by context capacity, impractical for many documents |
| **Hybrid** | Combination of above | Leverages strengths of each method, but complex to design |

Terminal-style search is the most precise but requires many command invocations and has high latency. Meanwhile, embedding search is fast but has been reported to struggle with semantic similarity for specialized banking terminology (e.g., "Reg E", "ACH", "KYC").

## Reasoning Bottleneck Details

The 40% result in the oracle condition (providing correct documents) reveals the following **reasoning bottlenecks**:

1. **Multi-hop reasoning**: When one policy "conditionally overrides" another, agents must read both documents and correctly determine priority.
2. **Numerical condition interpretation**: Extracting conditions like "transactions over $500", "within 30 days", "minimum balance of $1,500" from documents and matching them against user circumstances.
3. **Exception handling**: Beyond standard rules, exception clauses exist and require correct judgment to apply.
4. **Implicit knowledge completion**: Whether agents can perform expected judgments even when not explicitly stated in documents, based on domain knowledge of banking operations (e.g., checking account balance before closing an account).

## Position in the τ-Bench Family

τ-Knowledge is part of the τ-Bench ecosystem, constituting the following family:

| Benchmark | Focus |
|-----------|-------|
| [[concepts/tau-bench\|τ-Bench]] | Conversational agent evaluation with structured tools |
| **τ-Knowledge** | Information retrieval and reasoning from unstructured knowledge bases |
| [[concepts/tau-squared-bench\|τ²-Bench]] | More complex multi-agent, multi-tool scenarios |
| [[concepts/tau-voice\|τ-Voice]] | Evaluation including voice interaction |

The new evaluation axis τ-Knowledge adds is "knowledge discovery," an essential capability for real-world agent deployment.

## Practical Implications

1. **RAG alone is insufficient**: Retrieval-Augmented Generation is necessary, but τ-Knowledge results show that **reasoning quality** after retrieval is equally important.
2. **Retrieval strategy optimization is key**: Choosing the right retrieval method (terminal vs. embedding) based on task characteristics significantly impacts performance.
3. **Domain specialization is essential**: Tuning for banking domain terminology and document structure is critical.
4. **Autonomous tool discovery**: Even state-of-the-art models significantly lack operational capability in environments where tool definitions are not explicitly provided.

## Future Challenges

- End-to-end optimization integrating retrieval and reasoning
- Development of domain-specific embedding models and retrieval pipelines
- Methods to explicitly train and evaluate multi-hop reasoning
- Exploration of retrieval architectures to close the gap with oracle conditions (the retrieval bottleneck)

## Related Pages

- [[concepts/tau-bench]] — The base conversational agent benchmark
- [[concepts/tau-squared-bench]] — τ²-Bench: More advanced evaluation suite
- [[concepts/tau-voice]] — Voice interaction evaluation
- [[concepts/_index]]
