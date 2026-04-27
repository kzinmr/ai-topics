# Claude Code vs Pi Agent — Feature Comparison
**Source:** disler/pi-vs-claude-code | **Version:** Pi v0.52.10 vs Claude Code (Feb 2026)
**URL:** https://github.com/disler/pi-vs-claude-code/blob/main/COMPARISON.md

## 📜 Core Design Philosophies & Key Quotes
| Dimension | Claude Code | Pi Agent | Winner |
|---|---|---|---|
| **Core Mantra** | `"Tool for every engineer" — batteries-included, accessible to all skill levels` | `"If I don't need it, it won't be built" — minimal, opinionated, built for one engineer's workflow` | Both |
| **Safety** | Safe by default — deny-first permissions, 5 modes, filesystem/network sandbox, Haiku pre-screening | `"YOLO by default" — no permissions, no sandbox. "Security in coding agents is mostly theater; if it can write and run code, it's game over"` | Both |
| **Context & Complexity** | Managed for you — auto-compaction, sub-agents handle overflow, system decides context | User-controlled — `"exactly controlling what goes into context yields better outputs"`, `"Three similar lines of code is better than a premature abstraction"` | Pi |
| **Observability** | Abstracted — sub-agents are black boxes, silent compaction, hidden system prompt | Full transparency — every token/tool call visible, no hidden orchestration, session HTML export | Pi |

## 🏗️ Architecture, Licensing & Cost
- **License & Source:** Claude (Proprietary/Closed) vs Pi (MIT/Open Source, forkable, self-hostable) → **Pi**
- **Cost:** Claude (`$20–$200/mo` or Dedicated API keys) vs Pi (`$0`, BYO API keys) → **Pi**
- **System Prompt Overhead:** Claude (`~10,000+ tokens` for guardrails) vs Pi (`~200 tokens`, trusts frontier models) → **Pi**
- **Architecture:** Claude (Monorepo CLI, built-in orchestration) vs Pi (4-package monorepo: `pi-ai`, `pi-agent-core`, `pi-tui`, `pi-coding-agent`) → **Both**
- **Memory File:** `CLAUDE.md` (hierarchical, auto-loaded) vs `AGENTS.md` (compatible with `~/.claude/skills`) → **Tie**

## 🤖 Model & Provider Support
- **Providers:** Claude (4 platforms, Claude-family only) vs Pi (20+ native providers, 324 confirmed models) → **Pi**
- **Local/Non-Anthropic:** Claude requires `ANTHROPIC_BASE_URL` gateway workaround. Pi has native first-class support (Ollama, vLLM, LM Studio via `models.json`) → **Pi**
- **Mid-Session Switching:** Both support it. Pi adds `Ctrl+P` cycle, `Ctrl+L` fuzzy selector, `session.setModel()` SDK → **Tie**
- **Thinking/Effort Levels:** Claude (3 levels on Opus 4.6) vs Pi (5 unified levels across ALL thinking-capable models, `Shift+Tab` to cycle) → **Pi**
- **OAuth/Logins:** Claude (Anthropic subscriptions) vs Pi (Claude Pro, ChatGPT Plus, GitHub Copilot, Gemini CLI, Antigravity via `/login`) → **Pi**

## 🛠️ Tools, Hooks & Event System
### Built-in Tools
| Tool | Claude Code | Pi Agent | Winner |
|---|---|---|---|
| Core (Read/Write/Edit/Bash) | Built-in | Built-in (`read`, `write`, `edit`, `bash`) | Tie |
| Search/Pattern | Built-in (`Glob`, `Grep`) | Optional via `--tools` (`find`, `grep`) | Claude Code |
| Web/Notebook | Built-in (`WebSearch`, `WebFetch`, `NotebookEdit`) | Customizable via extensions | Claude Code |
| Sub-Agents/Teams | Native Task tool (7 parallel, typed roles, teams) | Extension spawns separate `pi` processes | Claude Code |

### Hook & Event System
- **Count & Language:** Claude (`14 shell-based events`, JSON stdin/stdout) vs Pi (`25 TypeScript in-process events`, zero-build via `jiti`) → **Pi**
- **Key Pi-Only Events:** 
  - Real-time streaming: `tool_execution_start`, `tool_execution_update`, `tool_execution_end`
  - Bash interception: `BashSpawnHook` (modify cmd/cwd/env before spawn)
  - Dynamic prompts: `before_agent_start` (modify system prompt per-turn)
  - Context manipulation: `context` (deep copy, filter/prune)
  - Session branching: `session_before_fork`, `session_before_switch`, `session_before_tree`
- **Custom Tools:** Claude uses MCP (external JSON-RPC). Pi uses `pi.registerTool()` (in-process TypeScript, streaming, custom rendering) → **Pi**
- **Tool Override:** Not possible in Claude. Pi allows registering a tool with the same name to replace built-ins (e.g., audited `read`) → **Pi**

## 💻 UI, SDK & Programmatic Control
- **Session Format:** Claude (Linear) vs Pi (JSONL tree with `id/parentId` for branching/forking via `/tree` and `/fork`) → **Pi**
- **SDK/RPC:** 
  - Claude: `claude --print`, `--output-format stream-json`
  - Pi: `--mode rpc` (26+ commands, bidirectional JSON), `steer()`/`followUp()` for mid-stream control, `getSessionStats()` API → **Pi**
- **UI Customization:** Pi allows full terminal overrides (`ctx.ui.setHeader()`, `setFooter()`, `setWidget()`, overlays, custom dialogs). Claude offers basic statusline config → **Pi**
- **Extensions:** Claude (Shell/Markdown) vs Pi (TypeScript, `pi.registerShortcut()`, `pi.registerFlag()`, `pi.registerProvider()`) → **Pi**
- **State Persistence:** Pi uses `pi.appendEntry()` to persist custom data to session across restarts → **Pi**

## 🌐 Multi-Agent, Enterprise & Distribution
- **Multi-Model Orchestration:** Claude (Single provider) vs Pi (Multi-provider with context handoff) → **Pi**
- **Enterprise SSO/Audit:** Claude (SSO, MFA, audit logs, admin dashboard) vs Pi (None) → **Claude Code**
- **IDE Integration:** Claude (VS Code, JetBrains, Cursor inline diffs, @mentions) vs Pi (Terminal-only, RPC for IDE) → **Claude Code**
- **Web/Mobile/Desktop:** Claude (claude.ai/code, iOS app, desktop app) vs Pi (Terminal only, pi-mom Slack bot) → **Claude Code**

## 🏁 Final Verdict
**Claude Code** wins for enterprise teams, IDE integration, built-in safety/sandboxing, and multi-agent orchestration. It's a polished, batteries-included product.

**Pi Agent** wins for customization, transparency, self-hosting, multi-provider flexibility, and SDK embedding. It's a developer-first, minimal foundation that can be adapted to any workflow without forking internals.

Pi's selling point: *"Adapt pi to your workflows, not the other way around."* Claude Code's: *"A tool for every engineer."*
