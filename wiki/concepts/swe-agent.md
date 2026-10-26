---
title: "SWE-agent"
type: concept
aliases:
  - swe-agent
  - SWE Agent
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - coding-agents
  - agent-harness
  - evaluation
  - open-source
related:
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/swe-bench]]"
sources:
  - https://arxiv.org/abs/2405.15793
  - https://github.com/SWE-agent/SWE-agent
---

# SWE-agent

**SWE-agent** (Princeton/Stanford, Yang, Jimenez, Wettig, Lieret, Preslar, et al., May 2024) is an open-source autonomous coding agent whose central contribution is the **Agent-Computer Interface (ACI)**: a purpose-built set of file-editor, search, and shell commands designed *for LLMs*, rather than exposing raw human tools. It was the reference harness that paired with **SWE-bench** (the same group's benchmark of real GitHub issues) and demonstrated that interface design — not just model quality — dominates agentic coding performance.

## Key Ideas

- **ACI over raw shells.** Human tools (`vim`, raw `grep`, `nano`) assume eyes, persistence, and scrollback. LLMs need: windowed file viewers with line numbers, search that returns compact results, an edit command that fails loudly on ambiguity, and a syntax-checker loop. Small interface changes produced outsized benchmark gains (GPT-4 Turbo: 12.5% → 18.0% pass@1 vs the same model on a bare shell).
- **Cost of bad interfaces.** The paper documents failure modes caused purely by interface friction — infinite scroll loops, accidental whole-file rewrites, silent edit failures — now a canonical catalog for [[concepts/agent-harnesses]] design.
- **Contiguity with this wiki's thesis.** SWE-agent is the empirical ancestor of harness engineering: "Agent = Model + Harness" was proven on SWE-bench numbers before it was a slogan.

## Architecture

```
LLM (any API model)
   │  actions (text commands)
   ▼
ACI layer: open/view/edit/search/create + bash + syntax check
   │  observations (truncated, line-numbered)
   ▼
Docker container with the repo + tests
```

- **Repo exploration**: `search` (ctags-aware), `find_file`, `goto` windowed viewing.
- **Editing**: `edit` requires exact-string match; refusal feedback teaches precision.
- **Mini-SWE-agent** (2025): a ~100-line distillation that became the *default minimal harness* for research (used by Cadence, RLM evaluations, and many 2026 papers as the control harness).

## Ecosystem Position

| Tool | Relationship |
|------|-------------|
| [[concepts/swe-bench]] | Same group's benchmark; SWE-agent is its reference agent |
| mini-swe-agent | Minimal successor harness, standard research control |
| SWE-bench Verified | Human-validated subset that most 2026 model claims cite |
| Claude Code / Codex | Production harnesses that adopted ACI-like patterns (line-numbered reads, exact-match edits) |

## Related Concepts

- [[concepts/swe-bench]] — the benchmark
- [[concepts/agent-harnesses]] / [[concepts/harness-engineering]] — the design discipline it founded
- [[concepts/cadence-strategic-guidance-coding-agents]] — 2026 research using mini-swe-agent as testbed
- [[concepts/agent-first-codebase-design]] — downstream idea: design software for agents to operate

## Sources

- Yang et al., *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering* (arXiv:2405.15793)
- [github.com/SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent)
