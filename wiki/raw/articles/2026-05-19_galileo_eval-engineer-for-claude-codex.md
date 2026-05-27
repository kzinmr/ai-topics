# Galileo: Introducing Eval Engineer — Bringing Eval Expertise to Claude and Codex

- **Source:** https://galileo.ai/blog/introducing-eval-engineer-bringing-eval-expertise-to-claude-and-codex
- **Author:** Pratik Bhavsar (Evals & Leaderboards @ Galileo Labs), Paul Lacey (Head of Product Marketing)
- **Published:** May 19, 2026
- **GitHub:** https://github.com/Galileo-Agent-Labs/eval-engineer

## Summary

Eval Engineer is a skill bundle for Claude Code and OpenAI Codex that brings professional evaluation engineering practices into coding agent workflows. It bridges the gap between: (1) codebase knowledge (how the app is built), (2) Galileo observability (how the app behaves), and (3) eval expertise (what to do about failures).

The tool produces three artifacts per run: a diagnosis, a bounded fix plan, and a verification plan. It installs as repo-local skill files (`.claude/skills/eval-*` for Claude Code, `.agents/skills/eval-*` for Codex) and maintains a `.galileo/` working directory.

## Key Commands

| Command | Purpose |
|---------|---------|
| `/eval-engineer` | Router: inspects working set and routes to the right specialist |
| `/eval-setup` | Prepares `.galileo/` working set, config, editable files, verification commands |
| `/eval-fetch` | Imports Galileo evidence (log-stream URL, trace ID, time window, exported packet) |
| `/eval-measure` | Checks whether metrics match the use case |
| `/eval-diagnose` | Root cause analysis from evidence → diagnosis + fix plan |
| `/eval-cost` | Reduces tokens/latency/tool calls without quality regression |
| `/eval-audit` | Launch-readiness, safety, metric coverage, production-readiness review |

## Architecture

- **Installer:** Python package, installable via `uvx --from git+... eval-engineer install`
- **Skills location:** `.claude/skills/eval-*` (Claude Code), `.agents/skills/eval-*` (Codex)
- **Working directory:** `.galileo/` with `config.yml`, `current/`, `sessions/`, `eval-dataset/`, `learnings.md`
- **Design principle:** Loose coupling to the app, tight coupling to the workflow

## Design Philosophy

- **Bounded by design:** Editable files declared in `.galileo/config.yml`; skill prefers small changes to prompts, tool descriptions, routing rules, and eval cases
- **Artifact-driven:** Every run produces auditable diagnosis.md, fix-plan.md, verification-plan.md, and before/after evidence packets
- **Not a magic self-improving agent:** Human owns product decisions, merge decisions, and architecture changes
- **Framework-agnostic:** Works across RAG apps, tool-calling agents, agentic workflows, and custom harnesses

## Example RCA Loop

Production agent routed billing disputes to general support (tool_selection_quality dropped from 0.80 → 0.33). The fix loop:

1. `/eval-fetch` imports Galileo log-stream evidence → compact `debug-packet.json`
2. `/eval-diagnose` identifies root cause: tool description ambiguity causing wrong routing
3. Fix: tighten `escalate_to_support` description + add routing rule to system prompt
4. Verify: local pytest + Galileo canary comparison → 0.33 → 0.83 quality score
5. Candidate eval case proposed for human review

## Customization

Primary customization via `.galileo/config.yml`: app type, editable files, off-limits files, verification commands, quality gates, risk profiles. Team knowledge in `.galileo/learnings.md`.
