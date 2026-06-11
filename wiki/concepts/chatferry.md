---
title: "ChatFerry"
created: 2026-05-21
updated: 2026-05-21
type: concept
tags:
  - tool
  - developer-tooling
  - browser-agent
  - coding-agents
  - open-source
  - agent-tooling
  - ai-agents
sources: [https://github.com/shlokkhemani/chatferry, raw/articles/2026-05-20_shloked_chatferry.md]
---

# ChatFerry

A TypeScript CLI tool that lets coding agents and developers interact with ChatGPT and Claude through the terminal — without API keys. ChatFerry opens a real Chromium browser with persistent profiles, navigates to the provider's web UI, types the prompt, waits for the streaming response to complete, and exports the result as structured markdown with metadata sidecars.

Created by [[entities/shloked]] (Shlok Khemani). MIT license. First release v0.1.0 on 2026-03-26.

> "No API keys. Uses your existing ChatGPT Plus / Claude Pro subscription. No per-token costs. You already pay for it." — ChatFerry README

## Definition

ChatFerry is a **browser-automation CLI for AI coding agents** that bridges the gap between terminal-based agent workflows and web-based LLM interfaces. Instead of requiring API keys and paying per-token pricing, it leverages the user's existing paid ChatGPT and/or Claude subscriptions via automated browser sessions. This makes it particularly useful for coding agents ([[concepts/coding-agents/coding-agents]]) that need to send prompts to frontier models (GPT-5.5 Pro, Claude Opus 4.5, etc.) through feature-rich web UIs that expose canvas, artifacts, extended thinking, and other capabilities not available via API.

## Key Features

### No API Keys Required
ChatFerry uses the user's existing browser sessions and paid subscriptions. No API keys, no per-token billing, no separate billing accounts. The user's ChatGPT Plus or Claude Pro subscription handles all usage.

### Persistent Browser Profiles
Login sessions persist across runs via Chromium user data directories stored at `~/.chatferry/profiles/`. Set up once with `chatferry setup` — subsequent runs reuse the authenticated session.

### Provider Daemon with Concurrency
A background daemon manages the browser lifecycle, running up to **3 concurrent prompts per provider** using separate browser tabs. The daemon auto-exits after 60 seconds of inactivity (configurable via `CHATFERRY_DAEMON_IDLE_EXIT_MS`).

### Markdown Exports
Every response is saved as a clean markdown file with YAML frontmatter metadata. A `.meta.json` sidecar stores the prompt, response text, model used, chat URL, and content hashes for deduplication.

### Multi-Provider Support
ChatGPT and Claude through the same CLI interface. Model listing, prompt submission, and result retrieval work identically across providers.

### Async / Fire-and-Forget
Prompts can be submitted in fire-and-forget mode (`--no-wait`), returning immediately with a run ID. Use `chatferry wait <run_id>` to block until completion or `chatferry result <run_id>` to retrieve output later.

### Human-like Text Insertion
Uses a multi-strategy approach for text entry: fill, insertText, and clipboard paste with verification. This mimics human typing patterns to avoid triggering bot detection.

### Streaming Completion Detection
A state machine watches for DOM indicators: streaming text stopping, thinking indicators disappearing, and response content stabilizing before capturing the final output.

## How It Works

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  chatferry   │────▶│   Provider   │────▶│   Markdown   │
│  ask chatgpt │     │   Daemon     │     │   Export     │
│  "prompt"    │     │  (Playwright │     │  + .meta.json│
└──────────────┘     │  + Chromium) │     └──────────────┘
                     └──────────────┘
```

1. **Browser Session** — Launches Chromium with a persistent profile; login cookies persist across runs.
2. **Provider Daemon** — Background process manages the browser, supporting up to 3 concurrent prompts per provider via separate tabs.
3. **Prompt Insertion** — Multi-strategy text insertion: fill, insertText, clipboard paste with verification.
4. **Completion Detection** — State machine monitors DOM for streaming stop, thinking indicator removal, and response stabilization.
5. **Markdown Export** — Response HTML is converted to clean Markdown via Turndown. Sidecar `.meta.json` stores prompt, response, model, chat URL, and content hashes.

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | TypeScript (88.6%), JavaScript (11.4%) |
| **Browser Engine** | Playwright + Chromium |
| **HTML→Markdown** | Turndown |
| **Profiles** | Chromium user data directories |
| **State** | Filesystem (`~/.chatferry/state/`) |
| **Selector Configs** | YAML (per-provider UI element maps) |
| **Requirements** | Node.js 20+, paid ChatGPT/Claude account, desktop session |

## Requirements

- **Node.js 20+**
- **Paid ChatGPT and/or Claude account** (uses existing subscription)
- **Desktop session** (browser window must be visible — not headless, due to provider bot-detection)
- **npx playwright install chromium** (one-time setup)

## Usage / Example

### Installation

```bash
npm install -g chatferry
npx playwright install chromium
```

### First-Time Setup

```bash
# Set up both providers (opens browser for manual login)
chatferry setup

# Or set up individually
chatferry setup chatgpt
chatferry setup claude
```

### Basic Usage

```bash
# List available models for a provider
chatferry models chatgpt

# Ask a question (blocks until markdown export is complete)
chatferry ask chatgpt "What are the trade-offs of event sourcing?"

# Ask Claude with a file attachment
chatferry ask claude "Review this code" --file src/main.ts

# Fire-and-forget (returns immediately with run ID)
chatferry ask chatgpt "Deep research on browser automation" --no-wait --json
chatferry wait <run_id> --json
chatferry result <run_id> --json
```

### Async Workflow for Coding Agents

```bash
# Agent submits a prompt and gets a run ID
RUN_ID=$(chatferry ask claude "Explain the architecture of this codebase" \
  --file ARCHITECTURE.md --no-wait --json | jq -r '.run_id')

# Agent does other work...

# Later: retrieve the result
chatferry result $RUN_ID --json | jq -r '.response' > claude_analysis.md
```

### Command Reference

| Command | Description |
|---------|-------------|
| `chatferry setup [provider]` | Guided first-run login |
| `chatferry login <provider>` | Open browser for manual re-login |
| `chatferry models <provider>` | List available models |
| `chatferry ask <provider> [prompt]` | Send prompt → markdown export |
| `chatferry status <run_id>` | Check current state of a run |
| `chatferry wait <run_id>` | Block until run completes |
| `chatferry result <run_id>` | Get output path of completed run |
| `chatferry runs` | List recent runs |
| `chatferry cancel <run_id>` | Cancel queued or in-flight run |
| `chatferry read <url>` | Extract full conversation from a private ChatGPT/Claude URL |
| `chatferry reload <run_id>` | Reopen saved chat URL and refresh export |
| `chatferry daemon-status` | Show daemon status per provider |

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CHATFERRY_HOME` | `~/.chatferry` | Data directory for profiles, state, debug |
| `CHATFERRY_CHATGPT_CONCURRENCY` | `3` | Max concurrent ChatGPT tabs |
| `CHATFERRY_CLAUDE_CONCURRENCY` | `3` | Max concurrent Claude tabs |
| `CHATFERRY_DAEMON_IDLE_EXIT_MS` | `60000` | Daemon idle timeout (ms) |

## Data Storage

| Data | Path |
|------|------|
| Browser profiles (sessions) | `~/.chatferry/profiles/` |
| Run records, daemon state | `~/.chatferry/state/` |
| Debug artifacts | `~/.chatferry/debug/` |
| Markdown exports (default) | Current working directory |

## Comparison to API-Based Approaches

| Dimension | ChatFerry | Official API |
|-----------|-----------|-------------|
| **Cost** | Included in web subscription | Per-token billing |
| **Setup** | Browser login (one-time) | API key provisioning |
| **Web-Only Features** | ✅ Canvas, artifacts, extended thinking | ❌ Not available |
| **Reliability** | Dependent on UI selectors (may break on UI changes) | Stable API contracts |
| **Concurrency** | 3 per provider (tab-based) | Rate-limit based |
| **Headless** | ❌ Requires visible desktop | ✅ Fully headless |
| **Response Format** | Markdown (HTML→Turndown) | JSON / streaming SSE |

## Limitations

- **Desktop session required** — the browser window must be visible; not suitable for headless servers without a display
- **UI selector fragility** — if ChatGPT or Claude changes their DOM structure, ChatFerry may need selector config updates
- **Provider rate limits** — subject to the same rate limits as the web UI (e.g., Claude Pro's message caps)
- **Not a reverse-engineered API** — intentionally uses real browser sessions, which is slower but more durable than scraping internal API endpoints
- **Single-machine** — browser profiles are local to one machine; not designed for distributed agent fleets

## Related Concepts

- [[concepts/coding-agents/coding-agents]] — The primary consumers of ChatFerry: Claude Code, Codex, Cursor, and other coding agents that need web UI model access
- [[entities/claude-code]] — Anthropic's agentic coding CLI; ChatFerry can send prompts to Claude's web UI for features not in the API
- [[entities/openai-codex]] — OpenAI's coding agent platform; ChatFerry targets ChatGPT web UI for Codex-compatible workflows
- [[concepts/browser-automation]] — The broader technique ChatFerry employs (Playwright + Chromium for web UI interaction)
- [[concepts/agent-tooling]] — The category of tools (CLIs, harnesses, memory systems) that support coding agent workflows
- [[concepts/rodney-browser-automation-cli-for-agents]] — Simon Willison's Rodney, another browser-automation CLI for coding agents
- [[entities/shloked]] — ChatFerry's creator
- [[entities/shlok-khemani]] — Creator's broader work on memory systems and agent architecture

## Sources

- [GitHub: shlokkhemani/chatferry](https://github.com/shlokkhemani/chatferry) — Primary source: README, source code, release notes
- [raw/articles/2026-05-20_shloked_chatferry.md](raw/articles/2026-05-20_shloked_chatferry.md) — Raw article stub (scraped 2026-05-21)

## Changelog

| Date | Event |
|------|-------|
| 2026-03-26 | v0.1.0 initial release (MIT license) |
| 2026-05-18 | Last push (maintenance) |
| 2026-05-21 | Wiki page created |
