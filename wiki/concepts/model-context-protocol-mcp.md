---
title: "Model Context Protocol (MCP)"
type: concept
created: 2026-04-19
updated: 2026-07-28
tags: [concept, mcp, developer-tooling, protocol, anthropic]
aliases: ["mcp", "model context protocol", "MCP protocol"]
related:
  - concepts/cli-over-mcp-pattern
  - concepts/structured-outputs
  - concepts/code-mode
  - concepts/harness-engineering/system-architecture/code-execution-with-mcp
sources:
  - raw/newsletters/2026-05-17-the-agentic-economy-has-no-black-box.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
  - raw/newsletters/2026-05-26-is-saas-dead.md
  - raw/articles/2026-07-28_anthropic_bringing-mcp-2026-07-28-to-claude.md
  - https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
---

# Model Context Protocol (MCP)

**Model Context Protocol (MCP)** is an open standard created by **Anthropic** (November 2024) for connecting AI assistants and agents to external data sources, tools, and development environments. It replaces fragmented, point-to-point integrations with a universal client-server protocol.

> *"Open technologies like the Model Context Protocol are the bridges that connect AI to real-world applications, ensuring innovation is accessible, transparent, and rooted in collaboration."* — **Dhanji R. Prasanna, CTO at Block**

## Architecture

MCP uses a **client-server model**:

```
┌─────────────┐       ┌──────────────┐
│  MCP Host   │       │  MCP Client  │
│  (Claude    │◄─────►│  (Agent IDE, │
│   Desktop,  │       │   CLI, SDK)  │
│   Cursor)   │       └──────┬───────┘
└─────────────┘              │ stdio / HTTP
                      ┌──────▼───────┐
                      │  MCP Server  │
                      │ (GitHub,     │
                      │  Postgres,   │
                      │  Google Drive│
                      │  Custom...)  │
                      └──────────────┘
```

- **MCP Host**: The AI application (Claude Desktop, IDE, CLI tool)
- **MCP Client**: Connects the host to one or more servers
- **MCP Server**: Exposes resources, tools, and prompts from a data source

## Core Primitives

| Primitive | Description | Example |
|-----------|-------------|---------|
| **Resources** | Read-only data exposed by servers | Files, database rows, API responses |
| **Tools** | Callable functions for agents | GitHub PR creation, Slack messaging, SQL queries |
| **Prompts** | Reusable prompt templates | "Review this code for security issues" |

## MCP in Agent Workflows

### Direct Tool Calling (v1)
Loading hundreds of tool definitions upfront consumes massive context and increases latency.

### Code Execution with MCP (v2 — "Code Mode")
Anthropic's November 2025 engineering blog post revealed a breakthrough pattern: **expose MCP tools as a filesystem of code modules**. Agents write TypeScript/Python scripts that call tools, execute them in a sandbox, and receive filtered results.

**Impact metrics:**
- Token reduction: ~150,000 → ~2,000 per workflow (**98.7% savings**)
- Independent validation by Cloudflare ("Code Mode" pattern)

```typescript
// Agent writes this script instead of calling tools directly
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

### Key Benefits of Code Mode

1. **Progressive Disclosure** — Models load only relevant tool definitions on-demand
2. **Context-Efficient Data Processing** — Filter/aggregate in-code before returning to model
3. **Native Control Flow** — Standard programming constructs replace agent message loops
4. **Privacy-Preserving** — Intermediate data stays in execution environment (PII tokenization)
5. **State Persistence** — Write results to disk, save as reusable SKILL.md files


## MCP 2026-07-28: Stateless Core (Released)

The fifth MCP spec release went live on **July 28, 2026**, making the previously announced RC changes official. MCP has surpassed **400M monthly SDK downloads** (4x increase in 2026).

### Three Pillars of 2026-07-28

| Change | Before (stateful) | After (stateless) |
|--------|-------------------|-------------------|
| **Protocol model** | Bidirectional stateful | Request/response stateless |
| **Deployment target** | Long-running servers | Serverless & edge infrastructure |
| **Extensions** | Ad-hoc | Versioned framework (Apps, Tasks) |
| **Auth** | Varied implementations | OAuth 2.0 / OIDC aligned (Entra, Okta) |

### Stateless Core
MCP moves from a bidirectional stateful protocol to a **request/response model**. Servers can now deploy on serverless and edge infrastructure. No handshake, no session ID — any request can hit any server instance.

**Implications:**
- Horizontal scaling without sticky sessions
- Simplified load balancing
- No session state recovery on restart
- First-class HTTP workload compatibility

### Standardized Extensions
**MCP Apps** and **MCP Tasks** now ship under a versioned extensions framework:
- **MCP Apps**: Interactive UIs rendered directly in the conversation
- **MCP Tasks**: Long-running work with structured inputs/outputs

### Auth Hardening
Authorization now aligns with production OAuth 2.0 and OIDC deployments, enabling MCP servers to connect to enterprise identity systems (Entra, Okta) without workarounds.

### Claude-Specific Features
Claude now lists **950+ MCP servers** in the connectors directory. New features accompanying the spec release:
- **Enterprise-managed auth** — Admins provision connectors via IdP, users inherit access through groups (zero-touch setup)
- **Observability dashboard** — Track adoption, diagnose errors/latency, usage breakdown by product
- **MCP tunnels** (research preview) — Connect to private-network MCP servers without public endpoints

> Source: [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) (Anthropic, Jul 28, 2026)

## WebMCP

Chrome 146 introduced **WebMCP** — a browser-native implementation exposing `navigator.modelContext` for structured tool access. This enables websites to expose callable tools directly to AI agents, replacing fragile DOM scraping with structured APIs.

## MCP Ecosystem Tools

| Tool | Description | Stars |
|------|-------------|-------|
| **mcporter** | MCP server wrapper as CLI (TypeScript) | 3.8k |
| **Peekaboo** | macOS screenshot MCP server | 3.1k |
| **Terminator MCP** | Terminal output relay MCP server | — |
| **WebMCP** | Chrome 146 native model context protocol | — |

## MCP Provider Support Comparison (2026-04)

Martin Alderson's practical evaluation comparing MCP support across major AI APIs:

### Anthropic Claude API — ✅ Works out of the box
- Full remote MCP support. URL-only specification with streaming HTTP transport
- Tool discovery and execution are automatically handled by Anthropic
- Existing remote MCP servers can be added to prompts in seconds
- **Drawback**: API pricing is high (significantly more expensive than Gemini 2.5 Flash)

### OpenAI API — ⚠️ Promising but broken
- Claims full remote MCP support
- Tool discovery succeeds, but tool calls produce `"Session terminated"` errors
- Works correctly with MCP Inspector, Claude, and direct JSON-RPC → Issue lies in OpenAI's implementation
- Improvements expected in future updates

### Google Gemini API — ❌ No real MCP support
- MCP section exists, but it only enumerates tools on the host side and inserts them into tool definitions
- This is not "true MCP" where the LLM provider discovers and executes tools
- Only supports JavaScript/Python SDK
- Gemini web UI excels at Google service integration, but API-level support is weak

### MCP Ecosystem Growth
- As of April 2026: **1,150+ servers** (900→1,150 in one week, ~25-30 new servers per day)
- Real-time tracking available at [mcp-tracker.martinalderson.com](https://mcp-tracker.martinalderson.com)

### Open Weights Opportunity
APIs hosting open-weight models (Qwen3, gpt-oss, etc.) have significant opportunity to provide sophisticated MCP integration options. None currently exist.

## CLI Over MCP Pattern

Some developers (notably @steipete) argue that **standard CLI tools are often superior to MCP servers** for agent workflows:

- No setup overhead — works immediately
- Better error handling — CLIs have decades of maturity
- Smaller context footprint — CLI output is more concise
- No server management — single binary vs. MCP server lifecycle

MCP excels for structured data access and real-time integrations, while CLIs are better for one-off data retrieval and system operations.


## Security Vulnerabilities & Governance Risks (May 2026)

As of May 2026, MCP had reached **150M+ downloads** (now **400M+ monthly SDK downloads** as of July 2026) and become the de facto connective tissue of the agentic web. This scale has surfaced critical security concerns:

### OX Security Findings
- **Trust-boundary risks** in MCP's STDIO execution model affected thousands of publicly accessible servers
- Up to **200,000 vulnerable instances** identified
- 10+ high/critical CVEs in downstream projects
- Researchers successfully **poisoned 9 of 11 public MCP registries**

### Exposure & Authorization Gaps
- Bitsight found ~**1,000 MCP servers exposed** to the internet with **no authorization controls**
- No shared public place to report or track infrastructure-level failures
- Systemic stress fractures reported at scale

### Governance Implications
MCP's rapid adoption as agent infrastructure creates a governance gap: the protocol is open and decentralized, but security responsibility is diffused across server operators, registry maintainers, and agent developers. See [[concepts/security-and-governance/agent-governance]] for the broader multi-owner economy framework.

Source: [Superintel — "The Agentic Economy Has No Black Box"](https://getsuperintel.site/p/the-agentic-economy-has-no-black-box) (Patrick Hussey, May 17, 2026), citing OX Security research

## Related Concepts

- [[concepts/cli-over-mcp-pattern]] — CLI Over MCP design principle
- [[concepts/code-mode]] — Code Mode: LLM writes code instead of sequential tool calls
- [[concepts/structured-outputs]] — Guaranteed JSON/XML/code structure during generation
- [[concepts/harness-engineering/system-architecture/code-execution-with-mcp]] — Anthropic's Code Execution with MCP
- [[concepts/harness-engineering/agentic-workflows/agent-first-design]] — Agent-First Codebase Design

## Sources

- [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (2024-11-25)
- [Anthropic Engineering: Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) (2025-11-04)
- [MCP Specification & SDKs](https://github.com/modelcontextprotocol)
- [MCP Tools Specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- Cloudflare: [Code Mode](https://blog.cloudflare.com/code-mode/)
- Reddit: ["WebMCP just dropped in Chrome 146"](https://www.reddit.com/r/HowToAIAgent/comments/1r36bec/webmcp_just_dropped_in_chrome_146_and_now_your/)
