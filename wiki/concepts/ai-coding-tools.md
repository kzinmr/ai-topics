---
title: "AI Coding Tools"
type: concept
aliases:
  - ai-coding-tools
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - ai-coding
  - coding-agents
  - developer-tools
  - comparison
sources:
  - wiki/concepts/coding-agents/state-of-agentic-coding.md
  - wiki/concepts/ai-coding-effectiveness-debate.md
---

# AI Coding Tools

**AI Coding Tools** is the product category spanning everything from inline autocomplete to autonomous multi-agent coding systems. This page is the **landscape hub**; the deep analysis lives in the [[concepts/coding-agents/coding-agents|coding-agents]] subtree. The category has passed through three overlapping generations:

## Generations

| Generation | Interface | Examples | Era |
|------------|-----------|----------|-----|
| **1. Completion** | Ghost text in editor | GitHub Copilot, Tabnine, Codeium | 2021–2023 |
| **2. Chat + IDE copilots** | Side-panel chat, multi-file edits, agentic apply | Cursor ([[concepts/coding-agents/cursor-ide]]), Windsurf, Copilot Chat, Junie | 2023–2025 |
| **3. Terminal/background agents** | Autonomous loops in CLI/sandbox, PR-based | [[entities/claude-code]], [[entities/codex]], [[entities/grok-build]], Devin, OpenHands ([[concepts/coding-agents/open-swe]]), background agents | 2025– |
| **3.5 App builders** | Natural-language full-stack generation | [[entities/lovable]], v0, Bolt | 2025– |

## The 2026 Field Map

- **Frontier-lab agents**: Claude Code ([[entities/claude-code]], with subagents/hooks/skills), OpenAI Codex ([[entities/codex]]), Google Antigravity ([[entities/google-antigravity]]), Grok Build ([[entities/grok-build]]).
- **IDE-first**: Cursor ([[entities/cursor-ai]], [[entities/cursor-3]], Composer models), JetBrains Junie, Windsurf.
- **Open-source harnesses**: Cline ([[entities/cline]]), Roo Code ([[entities/roocode]]), Kilo ([[entities/kilo]]), OpenCode ([[entities/opencode]]), Amp ([[entities/amp]]/[[concepts/coding-agents/amp-neo]]), pi ([[concepts/coding-agents/pi-autoresearch]]), and deliberately minimal designs ([[concepts/coding-agents/minimal-coding-agent]]).
- **Enterprise platforms**: Devin, Factory, Databricks' agent suite ([[concepts/coding-agents/databricks-coding-agent-benchmark]]).

## What Differentiates Tools (Evaluation Axes)

1. **Harness quality > model choice** — the central finding of [[concepts/coding-agent-harness-design-study]] and [[concepts/bitter-lesson-agent-harnesses]]: context management, tool surface, verification loops, and sandboxing dominate outcome variance.
2. **Autonomy level** — autocomplete → accept/reject edits → supervised agent → async/background agent ([[concepts/coding-agents/background-coding-agent]], [[concepts/coding-agents/async-coding-agents]]).
3. **Feedback closure** — does the tool run tests/linters and self-correct ([[concepts/coding-agents/lint-rules-as-agent-feedback-loop]], [[concepts/coding-agents/closing-agent-loop]])?
4. **Cost & routing** — token economics and model routing ([[concepts/coding-agents/model-routing]], [[concepts/coding-agents/ai-coding-cost-optimization]]).
5. **Trust & governance** — provenance, review burden, security ([[concepts/coding-agents/ai-code-quality]], enterprise security pages).

## Debate Context

Tool adoption claims and efficacy claims diverge sharply — see [[concepts/ai-coding-effectiveness-debate]] (METR's RCT showing slowdown for experienced OSS maintainers vs vendor productivity claims) and [[concepts/coding-agents/normalization-of-deviance-in-ai-coding]] for quality-risk framing. Adoption stats are tracked in [[concepts/coding-agents/state-of-agentic-coding]].

## Related Concepts

- [[concepts/coding-agents/coding-agents]] — the agent-era subtree (taxonomy, harnesses, evaluation)
- [[concepts/vibe-coding]] / [[concepts/vibe-coding-vs-agentic-engineering]] — usage-mode distinctions
- [[concepts/harness-engineering]] — the umbrella philosophy ("Agent = Model + Harness")
- [[concepts/coding-agents/agentic-coding]] — the workflow paradigm these tools enable
- [[concepts/coding-agents/ai-code-quality]] — quality and review implications

## Sources

- Synthesized from the existing `concepts/coding-agents/` subtree, `ai-coding-effectiveness-debate`, and related entity pages (2026)
