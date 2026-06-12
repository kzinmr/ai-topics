---
title: "MemEx: A Programmable Scratchpad for LLM Agents"
source_url: https://www.databricks.com/blog/memex-programmable-scratchpad-llm-agents
author: The Databricks AI Research Team
published: 2026-05-19
captured: 2026-06-12
type: blog
---

# MemEx: A Programmable Scratchpad for LLM Agents

**Source:** https://www.databricks.com/blog/memex-programmable-scratchpad-llm-agents
**Published:** May 19, 2026
**Authors:** Ashutosh Baheti, Shubham Toshniwal, Arnav Singhvi, Krista Opsahl-Ong, Sean Kulinski, Sam Havens, Jonathan Li, Marco Cusumano-Towner, Jonathan Chang, Wen Sun, Alexander Trott, Jonathan Frankle, Xing Chen, Matei Zaharia

## Summary

In 1945, Vannevar Bush imagined a desk-sized machine that would extend a scientist's memory by storing every document, annotation, and trail of thought for recall on demand. He called it the MemEx. Eight decades later, LLM agents are hitting a remarkably similar wall.

In the current Agentic Tool Calling paradigm, the context window is the only persistent substrate the model can operate over. It is a shared space carrying the system prompt, the user's query, the model's reasoning, tool calls, and raw tool outputs. Tool outputs are the worst offenders: a single SQL query might return millions of rows, and in today's harnesses those rows ride along in every subsequent turn even if only one cell ever mattered.

Databricks built MemEx to address this — a programmable scratchpad for LLM agents.

## Key Results

- On hard enterprise structured retrieval tasks, MemEx pushes the cost-vs-accuracy frontier for every model.
- Frontier models like Opus 4.6 and Sonnet 4.6 gain 2–5 percentage points at 25–30% less token cost.
- Open-weights models like Qwen3.5-122B (18% → 36%) and Qwen3.5-397B (20% → 38%) nearly double their accuracy at 40–50% less token cost.
- MemEx can operate over arbitrarily long inputs, enabling auditing agent trajectories and parallel thinking across multiple trajectories.

## How MemEx Works

MemEx gives the LLM a programmable scratchpad: a typed Python kernel that holds tool outputs, transforms them with code, and materializes only the print statements as tokens in the context. Inside this environment, the rollout becomes a self-extending Python program. During each turn, the agent authors a new block, the kernel keeps state alive, and the next block builds on what came before.

Tools are exposed as typed Python functions with typed parameters and typed return values. Tool outputs land as Python objects in MemEx's scope, where they persist across turns.

### MemEx is in the Code-as-Action Family

MemEx is in the code-as-action family introduced by CodeAct (Wang et al., 2024), with production variants in Anthropic's Programmatic Tool Calling and Cloudflare Code Mode. MemEx sets itself apart by dropping into an existing ReAct (Yao et al., 2022)-style agentic framework, with persistent scope, sub-agent primitives, and typed returns wired in.

### Capabilities

- **Handling arbitrarily large inputs:** Documents, datasets, and other large objects can be kept in Python scope as variables.
- **Returning typed objects:** Tool outputs are typed Python objects kept in memory, not strings the model has to materialize or re-parse on every turn.
- **Composing tool calls:** One call's output flows directly into the next call's arguments within a single line of code. Intermediate outputs do not need to be materialized in the agent's context.
- **Slicing tool outputs:** Outputs can be preprocessed, filtered, or summarized in code before the model sees them.
- **Spawning asynchronous sub-agents:** Agents can programmatically spawn sub-agents that run alongside the parent, and aggregate their results without round-tripping through the main model.

## Evaluation Results

### OfficeQA Pro

Asks the agent to answer grounded reasoning questions over the U.S. Treasury Bulletins corpus, roughly 89,000 pages spanning 1939 to present. Four of the five points on the cost-vs-accuracy pareto frontier are MemEx configurations. Gemini 3.1 Pro MemEx is the cheapest frontier point at $0.62 per rollout (52.9% accuracy). Across nine models, MemEx ties or wins on every model.

### Enterprise Structured Retrieval

Asks the agent to answer natural-language questions over enterprise relational data. Every model shows strong gain under MemEx, excluding GPT 5.5 which shows parity performance. Qwen 122B drops from 56 to 28 tool calls per rollout while doubling its score; Sonnet from 28 to 17; Opus from 33 to 21.

## MemEx Operating on Agentic Trajectories

### MemEx Audits MemEx

An audit agent takes an OfficeQA question, its ground-truth answer, and six solver trajectories (3 from MemEx agent, 3 from Tool Calling agent) directly into its Python scope. Analysis shows MemEx has 2x reduction in search strategy and execution errors compared to Tool Calling.

| Failure Axis | MemEx errors | Tool Calling errors |
|---|---|---|
| Source Selection | 32 | 45 |
| Interpretation | 28 | 38 |
| Search Strategy | 6 | 15 |
| Execution | 3 | 6 |
| **Total** | **69** | **104** |

### Agentic Parallel Thinking with MemEx

MemEx can load multiple trajectories as scope variables, sidestepping lossy summarization entirely. A MemEx-based Sonnet 4.6 aggregator over eight independently generated Qwen-3.6-27B trajectories outperforms the equivalent Tool Calling agent that receives only summaries.

## MemEx Architecture

### Design Choices

1. **Code as action, in a persistent REPL:** The agent's action is an arbitrary Python code block, executed in a namespace that persists across turns.
2. **Drop-in for Tool Calling:** Existing Tool Calling tools are auto-injected as Python functions, including parameter schemas and return-type metadata.
3. **Backend-agnostic execution:** Same agent code runs in three backends — in-process (research), subprocess (evaluation), pool (high-throughput batch generation).

### Four Extensions Over CodeAct

1. Drop-in tool integration with parameter schemas preserved
2. Live Python scope at rollout start
3. Typed `submit()` for structured returns
4. Non-blocking `spawn_agent()` for parallel sub-agents, generalizing Recursive Language Models (Zhang et al., 2025)

## What's Next

- MemEx is being rolled out across Databricks' first-party agents and Agent Bricks
- Databricks is post-training models for the MemEx action space
- MemEx itself generates synthetic data, runs agentic verifiers, and feeds the training loop

## Related Work

- CodeAct (Wang et al., 2024) — the academic ancestor
- Anthropic's Programmatic Tool Calling — production variant
- Cloudflare Code Mode — production variant
- ReAct (Yao et al., 2022) — the base agentic framework MemEx extends
- Recursive Language Models (Zhang et al., 2025) — generalized by MemEx's spawn_agent()
- aroll — Databricks' agentic rollouts framework (powers Genie, Agent Bricks Supervisor Agent, KARL)
