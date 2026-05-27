---
title: "Desktop Extensions (MCP Bundle)"
type: concept
created: 2026-05-08
updated: 2026-05-27
tags:
  - mcp
  - developer-tooling
aliases:
  - MCP Desktop Extensions
  - .mcpb
  - MCP Bundle
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_desktop-extensions.md
  - https://www.anthropic.com/engineering/desktop-extensions
related:
  - mcp
  - model-context-protocol-mcp
---

# Desktop Extensions (MCP Bundle)

A format that packages an MCP server with its dependencies into a single file, installable with a double-click. Solves the complexity of MCP installation (requiring Node.js/Python, manual JSON config, dependency hell).

## File Format

- Extension: **`.mcpb`** (MCP Bundle, formerly `.dxt`)
- Essence: **ZIP archive**

```
extension.mcpb (ZIP archive)
├── manifest.json         # Extension metadata and configuration
├── server/               # MCP server implementation
│   └── [server files]
├── dependencies/         # All dependency packages/libraries
└── icon.png              # Optional: Extension icon
```

## Before/After

| Traditional | Desktop Extensions |
|------|-------------------|
| Requires Node.js or Python installation | Not required |
| Manual editing of `~/.claude/claude_desktop_config.json` | Not required |
| Resolving package conflicts and version mismatches | Automatic |
| MCP server discovery via GitHub search | Download from browser |
| Manual reinstall for updates | Automatic updates |

## Installation Flow

1. Download the `.mcpb` file
2. Double-click → Opens in Claude Desktop
3. Click "Install"
4. Done (no terminal, no config files needed)

## Problems Solved

MCP local servers are powerful, but installation complexity was a barrier for non-technical users:
- Development tool requirements (Node.js, Python, etc.)
- Manual JSON config file editing
- Dependency management
- Lack of discovery mechanisms
- Update complexity

Desktop Extensions abstracts all of these away.

## See Also

- [[concepts/mcp]] — Model Context Protocol overview
- [[model-context-protocol-mcp]] — Detailed MCP specification
- [[entities/claude-code]] — Claude Code agent harness

## MCP 2026-07-28 RC: Protocol Becomes Stateless

The MCP specification's release candidate for 2026-07-28 introduces a fundamental architectural change: **the protocol is now stateless**.

### Key Changes
- **No handshake** — Connections no longer require an initial negotiation phase
- **No session ID** — Any request can hit any server instance, simplifying load balancing
- **First-class extensions** — New `MCP Apps` and `MCP Tasks` extension points
- **Auth hardening** — Improved authentication flow for production deployments
- **Clearer deprecation policy** — Structured sunset process for older protocol elements

### Implications
- **Easier scaling** — Stateless design removes sticky-session concerns, enabling simpler horizontal scaling
- **Simpler load balancing** — Any server can handle any request, reducing infrastructure complexity
- **Better resilience** — No session state to recover on server restart

> Source: [AINews May 23, 2026](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)

