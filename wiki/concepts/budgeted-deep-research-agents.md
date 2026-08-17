---
title: "Budgeted Deep-Research Agents"
created: 2026-08-17
updated: 2026-08-17
type: concept
tags: [deep-research, research-agent, agents, verification, privacy, cost-optimization, go, cli, mcp, local-first]
sources:
  - raw/articles/2026-08-13_mole-budgeted-deep-research-agent.md
---

# Budgeted Deep-Research Agents

**Budgeted deep-research agents** are [[concepts/deep-research|deep research]] systems that add hard resource and trustworthiness guarantees on top of the standard decompose → search → read → synthesize loop: an *enforced* cost budget, *verified* citations, and a *privacy boundary* for local data. The leading open-source example is **Mole** (224 GitHub stars, Show HN Aug 2026).

## The Three Guarantees

Mole (written in Go, single static binary, MCP-exposed) distinguishes itself from a chat interface with web search on three axes:

1. **Enforced budget, not estimated.** Every model call is *reserved* against a budget before it is made and *settled* after, against a ledger with non-negative constraints enforced in the database schema itself. `--usd 0.50` means the run stops at fifty cents — measured overshoot across the test corpus is 0%.

2. **Verified quotes.** Every claim carries a quote checked against the source: a claim whose quote does not appear verbatim in the mined page is discarded *at extraction*, before it can reach an answer. Surviving claims can be re-read against sources afterward; an unsupported claim is flagged in the report rather than dropped.

3. **Local data stays local.** Point it at a CSV or folder and it analyses the data without the contents leaving the machine: the model chooses a hypothesis template and column names, Mole renders and runs the SQL, and only aggregates (counts, means, test results, buckets of ≥5 records) are allowed back. `mole crossings` shows exactly what left.

## Design Implications

- **Cost ceiling as a correctness property** — making budget a schema-level invariant (not an after-the-fact estimate) turns cost control from a monitoring concern into an architectural one, related to [[concepts/reasoning-model-cost-transparency|reasoning model cost transparency]] and the broader [[concepts/llm-cost-crisis|LLM cost crisis]].
- **Citation verification as agent safety** — verbatim-quote checking is a lightweight, mechanical form of [[concepts/parametric-factuality-recall-bottleneck|factuality]] enforcement that sidesteps full hallucination detection.
- **Differential privacy by aggregation** — the "only aggregates leave" rule is a privacy-preserving pattern for [[concepts/mcp|MCP]]-driven local-data analysis, in the spirit of [[concepts/security-and-governance/agent-sandboxing|agent sandboxing]]: constrain what the model can exfiltrate, not just what it can touch.

## Positioning

Mole speaks MCP so a coding agent can drive it in two modes: hand Mole a question and collect the answer, or use **toolkit mode** where the driving agent does the reasoning while Mole supplies the non-model-call parts (search, extraction, verification). This makes it a composable research *component* within a larger [[concepts/coding-agents/coding-agents|coding agent]] harness rather than a standalone product.

## Related

- [[concepts/deep-research]] — the deep-research capability and its retrieval framing
- [[concepts/deep-research-agent-from-scratch]] — building deep-research agents from scratch
- [[concepts/mcp]] — the protocol Mole exposes itself over
- [[concepts/parametric-factuality-recall-bottleneck]] — factuality limits of retrieval-augmented models
