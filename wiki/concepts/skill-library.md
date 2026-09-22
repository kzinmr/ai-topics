---
title: "Skill Library — Managed Repositories of Reusable Agent Skills"
created: 2026-09-22
updated: 2026-09-22
type: concept
tags:
  - agent-skills
  - skill-graph
  - memory
  - agent-memory
  - self-improving
  - arxiv
sources:
  - raw/articles/2026-09-22_arxiv_se-gos-self-evolving-skill-graph.md
  - raw/articles/2026-09-22_arxiv_subagents-vs-agent-skills.md
related:
  - "[[concepts/agent-skills]]"
  - "[[concepts/agent-skills-skillmd]]"
  - "[[concepts/skill-graph]]"
  - "[[concepts/ai-agent-memory]]"
  - "[[concepts/continual-learning]]"
---

# Skill Library — Managed Repositories of Reusable Agent Skills

## Definition

A **skill library** is a persistent, curated repository of reusable procedural
knowledge that an LLM agent selects from at inference time, instead of solving
each task from scratch. The term is used most precisely in recent arXiv work
(September 2026) to describe the open-ended, agent-authored alternative to the
static, human-authored libraries that dominated early 2026 practice (Claude
Code / Codex [[concepts/agent-skills-skillmd|SKILL.md]] files, MCP tool servers).

A skill is a multi-step *procedure* ("how to do X"), not a fact and not a tool
endpoint. Libraries therefore sit between an agent's
[[concepts/ai-agent-memory|memory]] (what it knows) and its tools (what it can call).

## Why It Matters

Two September 2026 papers converge on the same diagnosis: skill libraries are
the bottleneck, not skill *formatting*.

- **SE-GoS** (arXiv:2609.08228) argues current libraries are "built and
  maintained manually, lacking mechanisms for autonomous skill acquisition and
  structural organization." Its fix is a **self-evolving Graph-of-Skills**:
  skills are distilled from past agent trajectories into a DAG, so shared
  primitives and dependencies are *explicitly represented* — unlike flat
  libraries or retrieval-based designs that ignore skill relationships. An
  edit-evaluate-decide loop maintains the graph. Claimed gains on SpreadsheetBench,
  WikiTableQuestions, and PilexTyper over static, flat, and retrieval-based
  libraries, with transfer to unseen task categories.
- **"Subagents vs Agent Skills"** (arXiv:2609.09233) is an *evaluation* paper:
  it benchmarks SKILL.md-style progressive disclosure against subagent-isolated
  execution across ALFWorld, ScienceWorld, and AppWorld across four agent
  systems, and finds the **effect of skill representation depends heavily on
  the specific agent system and environment** — no universal winner. This
  tempers hype about any single library design.

## Relationship to the Skill Graph

The wiki's [[concepts/skill-graph]] page (May 2026) described a human-curated
folder of interlinked Markdown files acting as an agent "playbook." The arXiv
Graph-of-Skills is the *machine-managed* version of the same idea: dependencies
between skills become a graph the agent itself grows and repairs. The
distinction — human-curated skill graph vs. self-evolving skill graph — is the
interesting frontier.

## Open Questions

- Does a DAG representation pay off outside spreadsheet/table domains where
  SE-GoS was evaluated?
- Who audits a self-authored skill library? Procedural knowledge can encode
  unsafe shortcuts more durably than declarative memory.
- 2609.09233's "it depends on the harness" result suggests skill-library design
  is [[concepts/agent-harnesses|harness-specific]] — is a portable library format even meaningful?

## Sources

- SE-GoS: Self-Evolving Graph-of-Skills for Skill Library at Scale — arXiv:2609.08228 (2026-09-08)
- Subagents vs Agent Skills — arXiv:2609.09233 (2026-09-07)
