---
title: "Model Context Protocol (MCP)"
type: concept
created: 2026-04-19
updated: 2026-05-27
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


## MCP 2026-07-28 RC: Stateless Protocol

In May 2026, the MCP specification announced a **Release Candidate** targeting July 28, 2026, with foundational changes:

### Stateless Protocol
The most significant architectural change: MCP shifts from stateful to **stateless protocol** design. Server implementations no longer maintain session state between requests. This dramatically simplifies server deployment, scaling, and fault tolerance:

- **Horizontal scaling**: Stateless servers can be deployed behind load balancers
- **Simplified failover**: No session migration needed
- **Reduced memory footprint**: Servers don't track client sessions
- **Easier integration**: Existing RESTful tooling and middleware works natively

### First-Class MCP Apps and Tasks
New primitives introduced:
- **MCP Apps**: Runnable, shippable agent configurations bundling servers, tools, and prompt templates
- **MCP Tasks**: Structured, multi-step workflows with defined inputs, outputs, and verification conditions

### Authentication Hardening
Enhanced auth support for production deployments, including OAuth 2.0 integration and API key management.

### Significance
Stateless MCP represents MCP's maturation from an experimental protocol to a production-grade infrastructure standard. The shift to statelessness aligns with general web protocol evolution (cf. HTTP/1.1→HTTP/2 stateless semantics) and is a prerequisite for enterprise-scale agent deployments.

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

As of May 2026, MCP has reached **150M+ downloads** and become the de facto connective tissue of the agentic web. This scale has surfaced critical security concerns:

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
MCP's rapid adoption as agent infrastructure creates a governance gap: the protocol is open and decentralized, but security responsibility is diffused across server operators, registry maintainers, and agent developers. See [[concepts/agent-governance]] for the broader multi-owner economy framework.

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
