# Gemini API CLI (`gemini-api`) + gemini-api-cli Agent Skill

- Source: https://github.com/google-gemini/gemini-api-cli
- Skill: https://github.com/google-gemini/gemini-skills/tree/main/skills/gemini-api-cli
- Shared on X by Philipp Schmid (@_philschmid), 2026-11-03: "We made a skill for the Gemini API CLI. It gives your agent a CLI to call Gemini models (images, TTS, video, files) without writing one-off scripts. `npx skills add google-gemini/gemini-skills --skill gemini-api-cli`"
- Scraped from GitHub README, 2026-11-03.

## What it is

"An (experimental) CLI for the Gemini API" — a single stateless Go binary (`gemini-api`) that gives Codex, Claude Code, Antigravity, OpenClaw, Hermes, or any agent with shell access the ability to call the Gemini API directly, without one-off scripts. Configure an API key, put `gemini-api` on PATH, and let the agent choose a model, generate an asset, analyze a file, or launch a managed agent to handle a task.

## Why this CLI (from README)

A coding agent building an app may need a hero image, a voiceover, a second opinion on a design, or an answer inside a PDF. Design points:

- **One binary for models, media, and managed agents**: text/reasoning models, multimodal file analysis, image/audio/music/video generation, and managed agents from the command line. Runs on macOS, Linux, Windows.
- **Delegate long-running work**: start a Gemini managed agent in the background, keep the returned interaction ID, retrieve the result when needed.
- **Self-describing interface**: commands, flags, request schemas (`--schema`), and machine-readable usage (`--usage`) built into the binary so an agent can inspect what it needs on the fly.
- **Safe dry-run validation**: `--dry-run` validates inputs and prints the resolved HTTP request with credentials redacted — no network call, no OS keychain read.
- **Script- and agent-friendly output**: stream text, write media to disk, structured JSON (`--output-format json`) or compact TOON (`--output-format toon`), inline field filtering with `--jq .`.
- **Stateless execution**: each invocation runs independently; the agent supplies context, chooses the model, controls the next step. Built for headless use by coding agents and CI jobs.

Example: `gemini-api image "A friendly robot mascot for a developer tool" --out ./assets/` — prompt in, image on disk, agent gets the file path and keeps building.

## Agent skill wrapper

The companion `gemini-skills` repo packages this as an installable agent skill:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-cli
```

This follows the Anthropic-style `npx skills add` agent-skills distribution convention, applied by Google to Gemini's own capabilities — agents get model/media/managed-agent access via CLI + skill rather than an MCP server.
