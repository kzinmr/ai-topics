---
type: article
date: 2026-06-26
source: https://github.com/openclaw/mcporter
tags: [mcp, tool, typescript, agent-tooling]
title: "MCPorter: TypeScript Runtime, CLI, and Code-Generation Toolkit for the Model Context Protocol"
author: openclaw (steipete)
license: MIT
stars: 4722
forks: 315
latest_version: v0.12.2
latest_release_date: 2026-06-27
website: https://mcporter.sh
language: TypeScript (95.3%)
---

# MCPorter — Call MCPs via TypeScript

**Source**: [https://github.com/openclaw/mcporter](https://github.com/openclaw/mcporter)

> *TypeScript runtime, CLI, and code-generation toolkit for the Model Context Protocol.*

MCPorter helps you lean into the "code execution" workflows highlighted in Anthropic's **Code Execution with MCP** guidance: discover the MCP servers already configured on your system, call them directly, compose richer automations in TypeScript, and mint single-purpose CLIs when you need to share a tool. All of that works out of the box — no boilerplate, no schema spelunking.

## Key Features

- **Zero-config discovery.** `createRuntime()` merges your home config (`~/.mcporter/mcporter.json[c]`, or `$XDG_CONFIG_HOME/mcporter/mcporter.json[c]` when set) first, then `config/mcporter.json`, plus Cursor/Claude/Codex/Windsurf/OpenCode/VS Code imports, expands `${ENV}` placeholders, and pools connections so you can reuse transports across multiple calls.
- **One-command CLI generation.** `mcporter generate-cli` turns any MCP server definition into a ready-to-run CLI, with optional bundling/compilation and metadata for easy regeneration.
- **Typed tool clients.** `mcporter emit-ts` emits `.d.ts` interfaces or ready-to-run client wrappers so agents/tests can call MCP servers with strong TypeScript types without hand-writing plumbing.
- **Friendly composable API.** `createServerProxy()` exposes tools as ergonomic camelCase methods, automatically applies JSON-schema defaults, validates required arguments, and hands back a `CallResult` with `.text()`, `.markdown()`, `.json()`, `.images()`, and `.content()` helpers.
- **Record/replay fixtures.** `mcporter record` captures MCP JSON-RPC traffic as NDJSON, and `mcporter replay` serves the same responses deterministically for offline debugging and redacted repros.
- **Ad-hoc connections.** Point the CLI at *any* MCP endpoint (HTTP or stdio) without touching config, then persist it later if you want. Hosted MCPs that expect a browser login (Supabase, Vercel, etc.) are auto-detected — just run `mcporter auth <url>` and the CLI promotes the definition to OAuth on the fly.
- **Bridge mode.** `mcporter serve` exposes daemon-managed keep-alive servers as one MCP bridge with readable `server__tool` names.
- **Release confidence.** `v0.11.0` is published on npm and Homebrew, and live/published install smokes are green.

## Quick Start

MCPorter auto-discovers the MCP servers you already configured in Cursor, Claude Code/Desktop, Codex, or local overrides. You can try it immediately with `npx` — no installation required.

```shell
npx mcporter list
npx mcporter list context7 --schema
npx mcporter list https://mcp.linear.app/mcp --all-parameters
npx mcporter list shadcn.io/api/mcp.getComponents           # URL + tool suffix auto-resolves
npx mcporter list --stdio "bun run ./local-server.ts" --env TOKEN=xyz
```

```shell
# Colon-delimited flags (shell-friendly)
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# Function-call style (matches signatures from `mcporter list`)
npx mcporter call 'linear.create_comment(issueId: "ENG-123", body: "Looks good!")'

# Literal positional values that start with `--`
npx mcporter call server.tool -- --raw-value
```

Tool calls understand a JavaScript-like call syntax, auto-correct near-miss tool names, and emit richer inline usage hints.

## Installation

```shell
npx mcporter list              # Instant run
pnpm add mcporter              # Add to project
npm install -g mcporter        # Global install
brew tap steipete/tap && brew install steipete/tap/mcporter   # Homebrew
```

## Configuration

`config/mcporter.json` mirrors Cursor/Claude's shape:

```json
{
  "mcpServers": {
    "context7": {
      "description": "Context7 docs MCP",
      "baseUrl": "https://mcp.context7.com/mcp",
      "headers": {
        "Authorization": "$env:CONTEXT7_API_KEY"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"],
      "env": { "npm_config_loglevel": "error" }
    }
  },
  "imports": ["cursor", "claude-code", "claude-desktop", "codex", "windsurf", "opencode", "vscode"]
}
```

- `${VAR}`, `${VAR:-fallback}`, and `$env:VAR` interpolation for config strings.
- Automatic OAuth token caching in the shared vault (`~/.mcporter/credentials.json`).
- Stdio commands inherit the directory of the file that defined them.
- Import precedence matches the array order.
- `chrome-devtools-mcp --autoConnect` receives a small compatibility patch.

## Compose Automations with the Runtime

```typescript
import { createRuntime, createServerProxy } from 'mcporter';

const runtime = await createRuntime();
const chrome = createServerProxy(runtime, 'chrome-devtools');
const linear = createServerProxy(runtime, 'linear');

const snapshot = await chrome.takeSnapshot();
console.log(snapshot.text());

const docs = await linear.searchDocumentation({
  query: 'automations',
  page: 0,
});
console.log(docs.json());
```

- Property names map from camelCase to kebab-case tool names (`takeSnapshot` → `take_snapshot`).
- Positional arguments map onto schema-required fields automatically.
- Results are wrapped in a `CallResult` with `.text()`, `.markdown()`, `.json()`, `.images()`, `.content()`, or `.raw`.

## Generate a Standalone CLI

```shell
npx mcporter generate-cli \
  --command https://mcp.context7.com/mcp

# Outputs:
#   context7.ts        (TypeScript template with embedded schemas)
#   context7.js        (bundled CLI via Rolldown or Bun, depending on runtime)
```

## Generate Typed Clients

```shell
# Types-only interface (Promise signatures)
npx mcporter emit-ts linear --out types/linear-tools.d.ts

# Client wrapper (creates a reusable proxy factory alongside the .d.ts)
npx mcporter emit-ts linear --mode client --out clients/linear.ts
```

## Daemon for Keep-Alive Servers

- `chrome-devtools`, `mobile-mcp`, and other stateful stdio servers auto-start a per-login daemon.
- `mcporter daemon status` / `start` / `stop` / `restart` for lifecycle management.
- `mcporter serve --stdio` exposes every daemon-managed keep-alive server as one MCP stdio bridge.

## Testing and CI

| Command | Purpose |
|---|---|
| `pnpm check` | Oxfmt formatting plus Oxlint/tsgolint gate |
| `pnpm build` | TypeScript compilation (emits `dist/`) |
| `pnpm test` | Vitest unit and integration suites (streamable HTTP fixtures included) |

CI runs the same trio via GitHub Actions.

## Tech Stack

- **Language**: TypeScript (95.3%), JavaScript (4.5%), Shell (0.2%)
- **Package**: npm (`mcporter`), Homebrew (`steipete/tap/mcporter`)
- **License**: MIT
- **Website**: [mcporter.sh](https://mcporter.sh)

## Stats (as of June 2026)

- **Stars**: 4,722
- **Forks**: 315
- **Watchers**: 18
- **Releases**: 42 (latest: v0.12.2, Jun 27, 2026)
- **GitHub Topics**: cli, mcp, ts-api
