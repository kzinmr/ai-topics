---
title: Unlocking the Codex Harness: How We Built the App Server
category: other
status: active
---

# Unlocking the Codex Harness: How We Built the App Server
**Source:** OpenAI Engineering Blog | **Date:** February 4, 2026 | **Author:** Celia Chen (Technical Staff)
**URL:** https://openai.com/ja-JP/index/unlocking-the-codex-harness/

---

## Unified Codex Architecture
All Codex surfaces (Web, CLI, IDE extensions, macOS app) run on the same **Codex Harness** (agent loop + core logic).

## The Bridge: Codex App Server
Exposes the harness via a **client-friendly, bidirectional JSON-RPC API**.

### Origin
Initially built to reuse the CLI's TUI loop in VS Code without reimplementation. Evolved into a stable, backward-compatible protocol to support internal/external partners (JetBrains, Xcode, Desktop app) and parallel agent orchestration.

### Design Philosophy
Decouple client/server release cycles while preserving rich interaction patterns (streaming, diffs, human-in-the-loop approvals).

## Architecture Components
| Component | Role |
|---|---|
| `Codex Core` | Rust library/runtime — agent logic, thread lifecycle, config/auth, sandboxed tool execution (shell/file, MCP, skills) |
| `stdio Reader` | Ingests client JSON-RPC requests over standard I/O |
| `Message Processor` | Translates client requests → core operations, core events → UI-friendly JSON-RPC notifications |
| `Thread Manager` | Spawns and manages one core session per thread |
| `Core Thread` | Executes the actual agent loop |

## Conversation Primitives (API Design)
1. **Item:** Smallest I/O unit (user message, agent message, tool call, approval request, diff)
   - Lifecycle: `item/started` → optional `item/*/delta` (streaming) → `item/completed`
2. **Turn:** Single unit of agent work triggered by user input
3. **Thread:** Persistent session container (create, resume, fork, archive)

### JSON-RPC Lite
Uses a "JSON-RPC lite" variant — omits `"jsonrpc": "2.0"`, frames as JSONL over stdio. In containerized setups, stdio may be tunneled over persistent network connections (WebSocket-like) but behaves identically to local pipes.

## Integration Options
| Method | Best For | Limitations |
|---|---|---|
| **Codex App Server** | Full harness access, UI-friendly streaming, auth, config, model discovery | Requires building JSON-RPC client bindings |
| **MCP Server** (`codex mcp-server`) | Existing MCP workflows calling Codex as a tool | Lacks rich session semantics (diffs, streaming, turn lifecycle) |
| **Cross-Provider Protocols** | Multi-model orchestration | Converges on common subset; may miss provider-specific features |
| **Codex Exec** | One-off/CI tasks, automation pipelines | Non-interactive, structured logs only |
| **Codex SDK** (TypeScript) | Programmatic control without JSON-RPC | Currently limited scope/languages |

## Key Commands
```bash
# Generate TypeScript bindings from Rust protocol
codex app-server generate-ts

# Generate JSON schema for other languages
codex app-server generate-json-schema

# Run test client to inspect full turn JSON payloads
codex debug app-server send-message-v2 "run tests and summarize"
```

## Acknowledgements
Special thanks to Michael Bolin, Owen Lin, Eric Traut, and Rasmus Rygaard.
