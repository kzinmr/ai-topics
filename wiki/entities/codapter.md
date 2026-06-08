---
title: "Codapter"
created: 2026-05-27
updated: 2026-05-27
type: entity
status: complete
tags:
  - protocol
  - architecture
  - open-source
  - coding-agents
aliases:
  - codapter
  - kcosr/codapter
related:
  - concepts/codex-app-server
  - concepts/hermes-codex-app-server-runtime
  - comparisons/harness-backend-routing
sources:
  - https://github.com/kcosr/codapter
---

# Codapter

**Codapter** (kcosr/codapter) is a protocol adapter that translates Codex App Server's JSON-RPC wire protocol to alternative AI backends. It lets Codex Desktop, VS Code extension, and other app-server clients communicate transparently with non-Codex backends (Pi with any LLM, extensible via `IBackend`).

---

## Overview

Codapter implements the App Server protocol and translates client requests into the target backend's native protocol:

```
Client (Codex Desktop, VS Code, etc.)
    |
    |  App Server JSON-RPC (stdio/WebSocket)
    |
    v
Codapter
    +-- BackendRouter -- model prefix routing
    |     +-- pi::gpt-5.4 --> Pi backend (any LLM)
    |     +-- (unprefixed)  --> Codex backend
    |
    +-- IBackend interface -- extensible
```

## Key Features

- **Multi-backend routing**: Model ID prefix selects backend (`pi::model` → Pi, unprefixed → Codex)
- **`IBackend` interface**: Easy to add new backends
- **Full App Server protocol**: `initialize` → `model/list` → `thread/start` → `turn/start` — complete lifecycle
- **Model aggregation**: All backend models show up in unified `model/list`
- **Session management**: `~/.local/share/codapter/backend/{pi,codex}/`

## Environment Variables

| Variable | Description |
|----------|-------------|
| `CODAPTER_PI_COMMAND` | Pi launch command (default: `npx`) |
| `CODAPTER_PI_ARGS` | Pi launch args |
| `CODAPTER_PI_IDLE_TIMEOUT_MS` | Idle timeout (default: 5 min) |
| `CODAPTER_CODEX_DISABLE` | Disable Codex backend |
| `CODAPTER_CODEX_TRANSPORT` | Codex transport (`stdio`/`websocket`) |

## Ecosystem Role

Codapter plays a key role in the App Server protocol's evolution from "Codex-only" to a **common wire format**. While ACP spread spec-first, the App Server protocol spreads implementation-first — and Codapter is a primary enabler of that shift.
