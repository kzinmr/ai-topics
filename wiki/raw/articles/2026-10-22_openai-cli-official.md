---
source_url: https://github.com/openai/openai-cli
title: "OpenAI CLI — official CLI for the OpenAI REST API"
published: 2026-10-22
ingested: 2026-10-22
sha256: 87f76ccb41cf2b68
---

OpenAI released `openai/openai-cli`, the **official CLI for the OpenAI REST
API** (Apache-2.0, Go, 924 stars / 82 forks at ingest time, 560 commits).

- Install: `brew install openai/tools/openai` or
  `go install github.com/openai/openai-cli/cmd/openai@latest` (Go ≥ 1.26).
- Repo layout includes `api_reference/`, `generated/`, `docs/`,
  `tests/cli`, plus an `AGENTS.md` — i.e. the repo is itself agent-consumable,
  and ships a code-generated API surface.
- Ships an interactive image picker with Tab shortcuts for Bash/zsh/fish,
  `openai images generate`, and release-update notices that respect
  `HTTPS_PROXY`/`NO_PROXY`, cap at one GitHub-metadata check per day, never
  auto-install updates, and can be disabled with `OPENAI_CLI_NO_UPDATE_CHECK=1`.
- Release tooling: GoReleaser + release-please, checksums, a "castiron"
  ratchet config.

Significance: OpenAI moving from SDK-only to an official first-party CLI puts
it on the same surface as the Claude Code / Codex CLI pattern where the CLI is
the primary agentic entry point (and now a distribution channel that must be
supply-chain hardened — compare the same-week LiteLLM 1.107.0 PyPI compromise).

HN discussion: https://news.ycombinator.com/item?id=50191507 (147 points)
