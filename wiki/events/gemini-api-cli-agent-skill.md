---
title: "Gemini API CLI + Agent Skill"
created: 2026-11-03
updated: 2026-11-03
type: event
tags:
  - announcement
  - google
  - gemini
  - agent-skills
  - coding-agents
  - developer-tooling
sources:
  - https://github.com/google-gemini/gemini-api-cli
  - https://github.com/google-gemini/gemini-skills/tree/main/skills/gemini-api-cli
  - raw/articles/github.com--google-gemini-gemini-api-cli--2026-11-03.md
  - https://x.com/_philschmid/status/2117674864907608543
---

# Gemini API CLI + Agent Skill (Nov 2026)

## What happened

On 2026-11-03, Philipp Schmid ([[entities/philipp-schmid]], Google DeepMind DevRel) announced on X that the team shipped an agent skill for the (experimental) **Gemini API CLI** (`gemini-api`): "It gives your agent a CLI to call Gemini models (images, TTS, video, files) without writing one-off scripts."

Install: `npx skills add google-gemini/gemini-skills --skill gemini-api-cli`

## The CLI

A single stateless Go binary that gives Codex, Claude Code, Antigravity, OpenClaw, Hermes, or any shell-access agent direct access to the Gemini API — text/reasoning models, multimodal file analysis, image/audio/music/video generation, and **managed agents** (start a background run, keep the interaction ID, poll the result). Notable design choices for agent use:

- **Self-describing**: `--schema` and `--usage` let an agent introspect commands on the fly.
- **Safe dry-run**: `--dry-run` prints the resolved HTTP request with credentials redacted, no network/keychain access.
- **Agent-friendly output**: JSON (`--output-format json`), compact TOON, or `--jq` field filtering; media written straight to disk.
- **Stateless execution**: the agent supplies context and controls next steps — built for headless coding agents and CI.

## Why it matters

- Google is distributing model capabilities through the **`npx skills add` agent-skills convention** (popularized by Anthropic's skills ecosystem) rather than only via MCP servers — a notable convergence on the skill-packaging format across labs. See [[concepts/agent-skills]].
- The managed-agent delegation pattern (background run + interaction ID) mirrors [[concepts/gemini/gemini-managed-agents]] infrastructure exposed through a plain CLI.

## Related

- [[entities/philipp-schmid]] — announced the skill
- [[entities/google]] — publisher (google-gemini org)
- [[concepts/agent-skills]] — the skills distribution format used here
- [[entities/hermes-agent]] — named as one of the target agents with shell access
