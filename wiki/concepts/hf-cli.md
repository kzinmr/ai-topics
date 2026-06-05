---
title: "hf CLI (Hugging Face CLI)"
type: concept
created: 2026-06-05
updated: 2026-06-05
tags:
  - cli
  - developer-tooling
  - huggingface
  - ai-agents
  - coding-agents
  - tool-use
  - agent-ergonomics
  - benchmark
sources:
  - raw/articles/2026-06-04_hf-cli-for-agents.md
---

# hf CLI (Hugging Face CLI)

The `hf` CLI is the official command-line interface to the [Hugging Face Hub](https://huggingface.co/), rebuilt in 2026 to serve both human developers and coding agents (Claude Code, Codex, Cursor, etc.) from a single binary. It wraps the full Hub API — model/dataset/Space management, repos, branches, PRs, Jobs, Buckets, Collections, webhooks, and Inference Endpoints — into a `resource + verb` command pattern (`hf models ls`, `hf repos create`, `hf jobs ps`).

## Agent-Optimized Design

The key design principle: **one command, multiple renderings**. The CLI auto-detects when a coding agent is driving it by reading environment variables (`CLAUDECODE`/`CLAUDE_CODE`, `CODEX_SANDBOX`, `AI_AGENT`, etc.) and switches output format without any flags.

### Human vs Agent Output

| Aspect | Human Mode | Agent Mode |
|--------|-----------|------------|
| Format | Aligned table, truncated to terminal width | TSV, nothing truncated |
| Values | Abbreviated with `...` suffix | Full ISO timestamps, full repo IDs, all tags |
| Visual | ANSI color, `✓`/`✔` symbols, progress bars | No ANSI, plain text |
| Hints | Prose hints below output | Same hints, stderr-separated |

Agent mode produces denser, more parseable output that stays light on tokens while preserving every detail.

### Key Design Features

- **Next-command hints**: Commands end with the natural next step, pre-filled with IDs (`hf jobs logs 6f3a1c2e9b`). Reduces agent tool calls by ~30%.
- **Non-blocking and safe to retry**: No interactive prompts in agent mode; destructive commands fail fast with `--yes` hint. `--exist-ok` flags make operations idempotent. `--dry-run` previews transfers.
- **Discoverable commands**: Consistent `resource + verb` pattern with aliases (`ls`/`list`, `rm`/`remove`). Every `--help` includes copy-pasteable examples. Output composes: `-q` prints one ID per line, `--json` feeds `jq`.
- **stdout vs stderr separation**: Data goes to stdout; hints/warnings/errors go to stderr, keeping agent parsing clean.

## Benchmarking Results

Hugging Face benchmarked the `hf` CLI against curl/Python SDK baselines across 18 multi-step Hub tasks, ~1,000 graded runs on Claude Code (Sonnet 4.6) and OpenAI Codex (GPT-5.5):

| Agent | Tool | Success Rate | Token Usage | Self-Report Errors |
|-------|------|-------------|-------------|-------------------|
| Claude Code (Sonnet 4.6) | `hf` CLI | 0.94 | baseline | 2/163 |
| Claude Code (Sonnet 4.6) | curl/SDK | 0.84 | 1.3–1.6× | 11/163 |
| Codex (GPT-5.5) | `hf` CLI | 0.93 | baseline | 3/163 |
| Codex (GPT-5.5) | curl/SDK | 0.92 | 1.6–1.8× | 10/163 |

Key findings:
- On **simple reads** (count rows, batch metadata), curl/SDK are comparable or slightly lighter
- On **complex multi-step tasks** (create repo with branch+tag, delete files, copy across repos, sync bucket), curl/SDK burn **2× to 6×** the tokens — the CLI composes chains of REST calls into a few high-level commands
- On Sonnet, curl/SDK **fail to complete** write-heavy tasks entirely; on GPT-5.5 they succeed but at higher cost

## hf-cli Skill

The `hf` CLI ships a **skill** — a compact, auto-generated command reference that agents load as context. It reduces tool calls by ~30% (from ~10 to ~7 commands per task) by eliminating `--help` probing:

```bash
# For Codex, Cursor, OpenCode, Pi
hf skills add

# Includes above + Claude Code
hf skills add --claude
```

The skill is regenerated every release via `hf skills preview`. It doesn't reduce tokens (fixed context overhead) but helps agents spend time executing rather than discovering commands.

## Agent Traffic Tracking

Starting April 2026, Hugging Face attributes agent traffic via user-agent strings (`agent/<name>`). Early numbers: Claude Code ~40k users / ~49M requests, Codex close behind. Agent harness registration is open via PR to [`agent-harnesses.ts`](https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/src/agent-harnesses.ts).

## Installation

```bash
# macOS / Linux
curl -LsSf https://hf.co/cli/install.sh | bash

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://hf.co/cli/install.ps1 | iex"
```

## Relation to Agent Ergonomics

The `hf` CLI is a notable case study in tool design for agents:
- **Agent-first output design** (TSV over tables, full values over truncation)
- **Idempotent, composable commands** that reduce agent retry/correction loops
- **Skill-as-documentation** pattern for reducing agent discovery overhead
- **Benchmarking agent tool efficiency** as a first-class engineering practice

This aligns with the broader trend of [[concepts/agent-ergonomics|agent ergonomics]] — designing developer tools that work well for both humans and AI coding agents.

## Related Pages

- [[entities/hugging-face]] — Parent organization
- [[concepts/huggingface-skills]] — Standardized agent skill repository (includes `hf-cli` skill)
- [[concepts/agent-ergonomics]] — Tool/language design for AI agents
- [[concepts/cli-first-development]] — CLI-first design philosophy
- [[entities/clefourrier]] — HuggingFace team member (evaluation, benchmarks)
- [[entities/elie-bakouch]] — Former HuggingFace (SmolLM, FineWeb)
