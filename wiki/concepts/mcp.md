---
title: MCP (Model Context Protocol)
created: 2026-04-26
updated: 2026-05-07
type: concept
tags: [protocol, agentic-engineering, tool, mcp-apps]
sources: [raw/articles/troyhunt.com--heres-what-agentic-ai-can-do-with-have-i-been-pwneds-apis--7eefad3f.md, raw/articles/2026-04-25-langchain-anatomy-agent-harness.md, raw/articles/gemini-deep-research-agent.md, raw/articles/2026-01-26_anthropic-interactive-tools-claude.md, raw/articles/2025-11-21_mcp-apps-proposal.md, raw/articles/2026-01-26_mcp-apps-official-release.md, raw/articles/2026-01-01_mcpui-dev-landing-page.md]
---

# MCP (Model Context Protocol)

## Overview

**Model Context Protocol (MCP)** is an open standard that defines how AI agents discover, authenticate with, and call tools over a network. Created by Anthropic, MCP serves as a universal "USB-C for AI" — one protocol that connects any agent to any tool, eliminating the fragmented ecosystem where tools built for one framework did not work with another.

Think of it as a standardization layer between AI applications (Claude, ChatGPT, Gemini, custom agents) and external systems (databases, APIs, file systems, search engines, calculators, workflows).

## Core Architecture

MCP defines three primary abstractions:

1. **Resources** — Read-only data sources that agents can access (files, database queries, API endpoints)
2. **Tools** — Callable functions that agents can invoke (search, compute, execute code, send emails)
3. **Prompts** — Pre-defined conversation templates that guide agent interactions

An MCP server exposes these abstractions over a transport layer (stdio or HTTP). An MCP client (AI application or agent harness) discovers available tools and resources, then invokes them in a standardized way.

### Key Design Principles

- **Discovery-first**: Agents can enumerate available tools at runtime rather than requiring hardcoded integrations
- **Authentication at protocol level**: Each MCP server handles its own auth (API keys, OAuth, etc.)
- **Transport agnostic**: Works over stdio (local subprocess) or HTTP (remote servers)
- **Schema-driven tool definitions**: Tools declare their parameters with JSON schemas for validation

## Ecosystem Adoption

### Anthropic (Originator)
MCP was created by Anthropic. The Anthropic SDK has accumulated **150M+ downloads** across package registries, outpacing React's first 3 years in just 16 months. MCP is the default tool integration mechanism in Claude Code.

### OpenAI (Adopter)
In March 2025, OpenAI announced adoption of MCP across its products — the first time OpenAI embraced a rival's standard. Sam Altman stated: "People love MCP and we are excited to add support across our products." MCP is available in the OpenAI Agents SDK, ChatGPT desktop app, and Responses API.

### Google
Gemini Deep Research Agent adds MCP integration, enabling custom tool and data source extensibility.

### Enterprise Platforms
- **Red Hat OpenShift AI 3**: Adds MCP support directly to the platform with guided server creation, containerization, and deployment
- **VS Code, Cursor, Windsurf**: MCP servers can be configured as tool integrations
- **Gemini-CLI**: MCP tool integration support

### Security Concerns
OX Security identified serious vulnerabilities in MCP implementations — specifically **Remote Code Execution (RCE) across the AI agent ecosystem**. MCP's universal tool access model means a compromised MCP server can execute arbitrary code in the agent's context. Thousands of community-published MCP servers increase the attack surface.

## MCP in Agent Harnesses

MCP is one of the core primitives in the agent harness architecture:

> **Agent = Model + Harness**

The harness layer (not the model itself) provides:
- Filesystems for durable storage
- Code execution (Bash)
- **Tools & Skills (MCPs, custom tools, encoded engineering taste)**
- Orchestration logic (subagent spawning, handoffs)
- Feedback loops and recovery mechanisms

Without external tools via MCP, an agent "in isolation is rather dumb" — it can only operate within its training data. MCP dramatically increases agent autonomy by enabling on-the-fly tool selection.

## Use Cases

### Enterprise Data Access
MCP enables agents to connect to internal databases, CRMs, and knowledge bases without custom integration code:

```json
{
  "url": "https://haveibeenpwned.com/mcp",
  "headers": {
    "hibp-api-key": "YOUR_STANDARD_HIBP_API_KEY"
  },
  "type": "http"
}
```

### Security & Compliance
Security teams use MCP to build agents that can:
- Monitor breach notifications across organizations
- Identify compromised employee accounts
- Automate security incident response

### Developer Tooling
MCP servers for GitHub, databases, and file systems enable AI coding agents (Claude Code, Codex, Gemini CLI) to interact with external infrastructure naturally.

## MCP Apps (Interactive UI Extension)

**MCP Apps** is the first official extension to the Model Context Protocol, enabling MCP servers to deliver rich, interactive user interfaces inside supporting AI products. Announced as a proposal in November 2025 ([SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865)) and officially released on January 26, 2026, it transforms MCP from a purely tool-calling protocol into a full bidirectional UI channel.

### History

The MCP Apps standard emerged from the consolidation of two independent efforts:

- **MCP-UI** (early 2025) — Created by **Ido Salomon** (@idosal1), an independent open-source project providing interactive UI components over MCP. Provided client (`@mcp-ui/client`) and server (`@mcp-ui/server`) SDKs for TypeScript, Ruby, and Python. Code executed in sandboxed iframes. Apache 2.0 license.
- **OpenAI Apps SDK** — OpenAI's parallel effort for tool UIs in ChatGPT.

In November 2025, the MCP-UI community working group (Anthropic, OpenAI, Ido Salomon) consolidated these into **SEP-1865**, the official MCP Apps extension. MCP-UI packages now implement the MCP Apps standard, and the original MCP-UI project is maintained as a legacy adapter for hosts that don't yet support MCP Apps natively.

### Key Concept

Traditional MCP servers expose tools that return text/structured data. MCP Apps servers additionally expose **interactive UI components** — charts, forms, kanban boards, document previews, and other rich interfaces — rendered inline within the AI chat. This enables a new class of AI-tool interaction where the user sees and directly manipulates the tool's output through the AI interface.

### Technical Architecture

MCP Apps uses two primary primitives:

1. **Tools with UI Metadata** — Tools include a `_meta.ui.resourceUri` field pointing to a UI resource:
   ```json
   {
     "name": "visualize_data",
     "description": "Visualize data as an interactive chart",
     "inputSchema": { ... },
     "_meta": {
       "ui": {
         "resourceUri": "ui://charts/interactive"
       }
     }
   }
   ```

2. **UI Resources** — Server-side resources served via the `ui://` URI scheme, containing bundled HTML/JavaScript. Uses `text/html+mcp` MIME type. Resources are **pre-declared** so hosts can prefetch and review them before execution.

3. **App API** — The `@modelcontextprotocol/ext-apps` package provides bidirectional JSON-RPC communication over `postMessage`:
   - `app.connect()` — Establish communication with host
   - `app.ontoolresult` — Receive tool execution results
   - `app.callServerTool()` — Call server tools from the UI
   - `app.updateModelContext()` — Send context back to the AI model

#### Code Example: App API

```javascript
import { App } from "@modelcontextprotocol/ext-apps";
const app = new App();
await app.connect();

// Receive tool results from the host
app.ontoolresult = (result) => {
  renderChart(result.data);
};

// Call server tools from the UI
const response = await app.callServerTool({
  name: "fetch_details",
  arguments: { id: "123" },
});

// Update model context
await app.updateModelContext({
  content: [{ type: "text", text: "User selected option B" }],
});
```

### Security Model

MCP Apps employs a multi-layered security approach:

1. **Iframe Sandboxing** — Restricted permissions for all UI content (no top-level navigation, no popups, no same-origin access)
2. **Pre-declared Templates** — Hosts review HTML content before rendering; no surprise UI code
3. **Auditable Messages** — All UI-to-host communication is loggable, structured JSON-RPC
4. **User Consent** — Hosts can require explicit approval before a UI component initiates a tool call
5. **Text Fallbacks** — Servers are encouraged to provide text-only fallbacks for clients without UI support

### Use Cases

- **Data Exploration** — Interactive charts with filtering, drill-down, and parameter adjustment
- **Configuration Wizards** — Multi-step forms with dependent fields (e.g., staging vs. production settings)
- **Document Review** — Inline PDF/HTML viewers where users can click to approve or flag clauses
- **Real-time Monitoring** — Live system health metrics (CPU, memory, requests) that update without re-running the tool

### Launch Partners (January 2026)

At launch, the following tools implemented MCP Apps as **interactive connectors** in Claude:

| Service | Interactive Capability |
|---------|----------------------|
| **Amplitude** | Build analytics charts; adjust parameters and explore trends interactively |
| **Asana** | Convert chats into projects, tasks, and timelines |
| **Box** | Search files, preview documents inline, extract insights |
| **Canva** | Create presentations with real-time branding/design customization |
| **Clay** | Research companies/contacts, draft personalized outreach |
| **Figma** | Generate flow charts, Gantt charts, and diagrams in FigJam via prompts |
| **Hex** | Ask data questions to receive interactive charts, tables, and citations |
| **monday.com** | Manage boards, assign tasks, visualize project progress |
| **Slack (Salesforce)** | Search conversations, generate drafts, review/format messages |
| **Salesforce** | Integration via Agentforce 360 (launched later) |

### Client Support

| Client | Availability |
|--------|-------------|
| **Claude** | Available at launch (Web & Desktop) |
| **Goose** | Available at launch |
| **VS Code** | Available in VS Code Insiders |
| **ChatGPT** | Rolling out week of January 26, 2026 |

### Ecosystem Adoption

MCP Apps has been adopted beyond the initial launch:
- **Microsoft Copilot** (March 2026): Copilot Chat supports MCP Apps ecosystem including Adobe, Monday.com, and Figma connectors
- **Open standard**: Any MCP server can implement the spec
- Example servers available: `threejs-server` (3D visualization), `map-server` (interactive maps), `pdf-server` (document viewing), `system-monitor-server` (real-time dashboards)

### Relationship to Other UI-over-MCP Standards

The MCP Apps standard was formed by consolidating earlier independent efforts:
- **MCP-UI** (Ido Salomon) — The original open-source standard; now implements MCP Apps spec and offers legacy adapter for backward compatibility
- **OpenAI Apps SDK & AgentKit** — OpenAI's parallel approach; merged into SEP-1865
- **Google A2UI** — Google's independent agent-to-user interface standard (not part of MCP Apps)

### Developer Resources

- **Official SDK:** [`@modelcontextprotocol/ext-apps`](https://www.npmjs.com/package/@modelcontextprotocol/ext-apps) (npm)
- **Documentation:** [MCP Apps Guide](https://modelcontextprotocol.io/docs/extensions/apps)
- **Quickstart:** [Getting Started Guide](https://apps.extensions.modelcontextprotocol.io/api/documents/Quickstart.html)
- **MCP-UI Project (legacy):** [mcpui.dev](https://mcpui.dev) — Community SDK packages for TypeScript, Ruby, Python; GitHub: [github.com/idosal/mcp-ui](https://github.com/idosal/mcp-ui)
- **Specification:** [SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865)
- **Community:** `#mcp-ui` channel in MCP Contributors Discord

### Key Quote

> "With MCP Apps, that contract finally includes the missing human step: when the workflow needs a decision, a selection, or exploration, the client can give you the right interaction without turning the conversation into a choose-your-own-adventure prompt."
> — **Harald Kirschner**, Principal Product Manager, VS Code

### Sources

- [Anthropic Blog: Interactive Connectors and MCP Apps in Claude](https://claude.com/blog/interactive-tools-in-claude) (January 26, 2026)
- [MCP Blog: MCP Apps Proposal (SEP-1865)](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) (November 21, 2025)
- [MCP Blog: MCP Apps Official Release](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) (January 26, 2026)
- [mcpui.dev](https://mcpui.dev) — MCP-UI project (now standardized into MCP Apps)
- [[wiki/raw/articles/2026-01-26_anthropic-interactive-tools-claude.md]]
- [[wiki/raw/articles/2025-11-21_mcp-apps-proposal.md]]
- [[wiki/raw/articles/2026-01-26_mcp-apps-official-release.md]]
- [[wiki/raw/articles/2026-01-01_mcpui-dev-landing-page.md]]

## 2026 Roadmap

MCP creator David Soria Parra outlined the 2026 roadmap at a keynote:

- **Triggers**: Event-driven MCP server activation (webhooks, file changes)
- **Streaming**: Real-time data streaming from MCP servers
- **Skills**: Pre-configured tool bundles for common workflows
- **Enterprise integration**: Deeper support for production AI agent pipelines

## Open Questions & Debates

1. **Context bloat**: Critics argue MCP adds unnecessary abstraction layers. Some argue custom integrations are simpler for single-agent setups.
2. **Security surface**: Thousands of community MCP servers create supply-chain risks. Who audits MCP server code before deployment?
3. **Protocol maturity**: MCP is still young. How does it compare to alternatives like OpenAI's function calling or custom agent tool protocols?
4. **Vendor lock-in vs. openness**: Anthropic created MCP but OpenAI, Google, and Microsoft have all adopted it. Is MCP truly vendor-neutral?

## Related Concepts

- [[concepts/harness-engineering]] — Agent harness architecture where MCP serves as the tool integration layer
- [[claude-code]] — Anthropic's agentic coding system with native MCP support
- [[ai-agent-platforms]] — Platform comparison including MCP as a tool integration standard
- [[concepts/multi-agent-orchestration-architecture]] — MCP as part of the tooling layer in multi-agent systems
- [[concepts/agent-governance]] — Runtime guardrails that apply to MCP tool invocations
- [[concepts/agentic-web]] — Agent-first web architecture, includes MCP Apps as UI standard
- [[entities/mcp-ui]] — Alternative open-source standard for UI over MCP (by Ido Salomon)
