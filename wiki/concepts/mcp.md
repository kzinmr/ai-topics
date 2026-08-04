---
title: MCP (Model Context Protocol)
created: 2026-04-26
updated: 2026-08-04
type: concept
tags: [protocol, agentic-engineering, tool, mcp]
sources: [raw/articles/troyhunt.com--heres-what-agentic-ai-can-do-with-have-i-been-pwneds-apis--7eefad3f.md, raw/articles/2026-04-25-langchain-anatomy-agent-harness.md, raw/articles/gemini-deep-research-agent.md, raw/articles/2026-01-26_anthropic-interactive-tools-claude.md, raw/articles/2025-11-21_mcp-apps-proposal.md, raw/articles/2026-01-26_mcp-apps-official-release.md, raw/articles/2026-01-01_mcpui-dev-landing-page.md, raw/articles/2025-10-08_postman-state-of-api-2025-report.md, raw/articles/workos.com--blog-management-mcp-server--d9a49c8a.md, raw/articles/workos.com--blog-mcp-vs-rest--adc9d692.md]
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

### Developer Awareness vs Adoption (Postman 2025 Survey)

Postman's 2025 State of the API report (surveying 5,700+ developers) revealed the awareness-adoption gap for MCP:

| Metric | Percentage |
|---|---|
| Developers aware of MCP | **70%** |
| Use MCP daily | **10%** |
| Planning to explore in future | **24%** |

70% awareness just 9 months after launch shows strong interest in MCP as a "universal language" for AI agents. However, the awareness-to-implementation gap (only 10% daily use) indicates MCP is still in the early adopter phase.

AI API traffic analysis on the Postman platform:

- OpenAI accounts for **56%** of all traffic (4.2M calls over the past 12 months)
- Gemini: **3.1x** year-over-year growth
- Llama: **6.9x** year-over-year growth
- Total AI API calls: **7.53M** (40% year-over-year increase)

Key insight: "Agents are already calling your APIs, with or without MCP" — rather than waiting for MCP adoption, making APIs agent-consumable now should be the priority.

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

## WorkOS Management MCP Server (July 2026)

WorkOS launched a [management MCP server](https://workos.com/blog/management-mcp-server) that exposes the **full WorkOS management surface** as MCP tools, enabling AI agents to manage authentication, SSO, Directory Sync, users, roles, permissions, and more without dashboard interaction.

### Architecture: Discover-Then-Execute Pattern

Rather than exposing one tool per endpoint (which would consume the LLM's context window), WorkOS uses a **discover-then-execute design** with four tools:

1. **`whoami`** — Agent identifies itself and its permissions
2. **`list_operations`** — Agent discovers available operations (hundreds across the full product surface)
3. **`query`** — Read-only data retrieval
4. **`mutate`** — State-changing operations

This pattern solves the **context budget problem**: exposing hundreds of individual tool definitions would exhaust the context window before work begins. Instead, the agent dynamically discovers capabilities at runtime.

### Security Design

- **OAuth-based**: Remote, hosted server; agents authenticate as the user via OAuth
- **Permission inheritance**: Agent inherits exactly the roles and permissions of the user's dashboard login
- **Deliberate exclusions**: Credential-minting, user impersonation, billing flows, and account-level admin are excluded
- **Secret stripping**: API keys, client secrets, webhook signing secrets are stripped from responses
- **Irreversible operation guard**: Nine destructive deletes require two-call confirmation

### Significance

This represents a pattern where **SaaS platforms expose their full admin surface as MCP tools**, enabling agents to perform configuration, debugging, and management tasks that previously required dashboard interaction. The discover-then-execute pattern is likely to become a standard approach for large tool surfaces in MCP.

> **Source**: [WorkOS Blog — Management MCP Server](https://workos.com/blog/management-mcp-server) (July 2026)

WorkOS has also published a companion post, [MCP vs. REST: What's the right way to connect AI agents to your API?](https://workos.com/blog/mcp-vs-rest) (August 2026), which grounds the management server's design decisions — discover-then-execute, deliberately few tools, OAuth-based auth — in a broader comparison of REST and MCP; see [MCP vs REST: When and Why](#mcp-vs-rest-when-and-why) below.

## MCP vs REST: When and Why

For fifteen years, REST has been the backbone of software integration — but LLM-powered agents are a new class of API consumer with different needs. A [WorkOS engineering post](https://workos.com/blog/mcp-vs-rest) frames the question not as "MCP or REST?" but **"Do I need both, and if so, how do they fit together?"**

### What REST does well

REST APIs are general-purpose interfaces designed to let any software system access another system's functionality or data — web browsers, mobile apps, CLIs, or microservices. They are stateless by design, which makes them easy to cache, load-balance, and scale horizontally, and decades of tooling surround them: OpenAPI specifications, Swagger UI, Postman, API gateways, rate limiters, CDNs. For deterministic developer-written clients that know exactly which endpoint to call and what parameters to pass, REST is excellent — and it remains the right tool for high-throughput, low-latency data fetching where HTTP caching, CDNs, and load balancers pay off.

### Where REST falls short for LLM agents

Four structural gaps emerge when the consumer is an LLM making autonomous decisions rather than a developer following a spec:

1. **No self-description at runtime** — A REST API can't tell you what it can do; you have to know going in. OpenAPI specs are static documents designed for developer tooling, not something an LLM can interrogate at runtime. If the API gains endpoints, client code must be manually updated — the API itself can't say "hey, I have a new capability."
2. **Stateless by design** — Each call is isolated. An agent that must look up a user, check their order history, then update their shipping address has to manually pass context between calls. There is no session, no shared state, no memory of what happened two calls ago.
3. **Every API is a snowflake** — Five different REST APIs means five different adapters: five sets of custom integration code, each with its own endpoints, parameter formats, authentication schemes, and error conventions.
4. **Designed for developers, not models** — REST design principles emphasize composability and small atomic endpoints that developers combine cheaply. These actively hurt agents, which pay a token cost for every tool definition they must reason over.

### MCP: purpose-built for AI agents

MCP (originally published by Anthropic in November 2024 as an open JSON-RPC-based standard) was explicitly designed to integrate LLM applications with external data and tools — and it **wraps a REST API rather than replacing it**. The USB-C analogy applies: MCP is to AI applications what USB-C is to laptops, letting any agent connect to any MCP server because they all speak the same protocol. MCP servers advertise their capabilities through three primitives:

- **Resources** — Read-only/passive information retrieval endpoints that do not cause side effects; handlers often support streaming chunks or pagination for large data.
- **Tools** — Active operations that can perform side effects or computations, defining input parameters and output schema clearly, and typically including validation and safety checks.
- **Prompts** — Reusable prompt templates or workflows the server provides to guide model interactions (e.g., a `sqlQueryTemplate` that formats database queries consistently).

Not every MCP server uses all three — many focus on tools — but an agent can query a server at runtime to discover which primitives exist and invoke them through a uniform interface.

### Runtime discovery: `tools/list` vs OpenAPI

This is MCP's most significant departure from REST. When an MCP client connects, it sends a `tools/list` request (JSON-RPC 2.0) and the server responds with a machine-readable catalog of every available tool: its name, a natural-language description, and a full JSON Schema `inputSchema`. The same pattern covers `resources/list` and `prompts/list`. Because every server publishes this catalog, agents discover and use new functionality without redeploying code — picking up new features automatically on each connection. This is fundamentally different from OpenAPI: a static document for developer tooling, versus a live protocol interaction where *"the agent asks, the server answers, and the agent adapts."* (See [[concepts/shared-discovery-paradox]] for the wider implications of runtime capability discovery.)

### Stateful sessions and standardized auth

MCP maintains a persistent session between client and server, established by a mutual handshake during initialization in which both sides advertise what they support. Context persists across multi-step workflows — the opposite of REST's stateless model, and essential when each action depends on what happened before. On authentication, MCP takes an opinionated stance: **OAuth 2.1 with PKCE** is the standard (spec revisions March 2025, June 2025, November 2025), with dynamic client registration and scoped tokens so the server can verify at tool-invocation time that a token authorizes the specific operation an agent attempts — a requirement for enterprise deployments where an agent acts on behalf of a user.

### Design for outcomes, not endpoints

The most common mistake when adopting MCP is **auto-converting every REST endpoint into an MCP tool**. Tools like FastMCP's OpenAPI converter make it tempting — one line of code exposes your entire API to LLMs — but a generous REST API of hundreds of small composable endpoints "drowns" an agent: every tool description is loaded into the context window and costs tokens on every single interaction. The better approach is **outcome-oriented tool design**, built around what the agent is trying to accomplish rather than your internal API structure:

> **Bad**: three separate tools — `get_user`, `get_orders`, `get_shipments` — requiring three round trips and holding intermediate results in conversation history.
> **Good**: one `track_order(email)` tool that calls all three endpoints internally and returns a complete, contextualized answer: "Order #12345 shipped via FedEx, arriving Thursday."

Think of the MCP server as a user interface — the same product thinking you'd apply to a UI, just for a non-human user. (See [[concepts/context-engineering/context-lock-in]] on why context budget drives this trade-off.)

### When to use what — the verdict

REST APIs aren't going anywhere: keep them for web/mobile applications, high-throughput data fetching, third-party developer integrations, and microservice communication. Add MCP when AI agents are the consumer, when you need multi-step workflows (stateful sessions), when you want write-once integrations across any MCP-compatible client, or when you need fine-grained OAuth 2.1 authorization for agentic access. The practical architecture is layered, not adversarial:

```
LLM Agent (Claude, Cursor...) 
  ↕ JSON-RPC / MCP Protocol
MCP Server — discovery & catalog, stateful sessions, OAuth 2.1, outcome-oriented tools
  ↕ HTTP
Your REST API — business logic, data access, existing infrastructure
```

MCP and REST are complementary layers in the AI stack: the REST API handles the business logic, and MCP makes that logic accessible to the AI agents that are increasingly becoming the primary way users interact with software.

## Open Questions & Debates

1. **Context bloat**: Critics argue MCP adds unnecessary abstraction layers. Some argue custom integrations are simpler for single-agent setups.
2. **Security surface**: Thousands of community MCP servers create supply-chain risks. Who audits MCP server code before deployment?
3. **Protocol maturity**: MCP is still young. How does it compare to alternatives like OpenAI's function calling or custom agent tool protocols?
4. **Vendor lock-in vs. openness**: Anthropic created MCP but OpenAI, Google, and Microsoft have all adopted it. Is MCP truly vendor-neutral?

## Related Concepts

- [[concepts/harness-engineering]] — Agent harness architecture where MCP serves as the tool integration layer
- [[entities/claude-code]] — Anthropic's agentic coding system with native MCP support
- [[comparisons/ai-agent-platforms]] — Platform comparison including MCP as a tool integration standard
- [[concepts/multi-agents/multi-agent-orchestration-architecture]] — MCP as part of the tooling layer in multi-agent systems
- [[concepts/security-and-governance/agent-governance]] — Runtime guardrails that apply to MCP tool invocations
- [[concepts/agentic-web]] — Agent-first web architecture, includes MCP Apps as UI standard
- [[entities/mcp-ui]] — Alternative open-source standard for UI over MCP (by Ido Salomon)
