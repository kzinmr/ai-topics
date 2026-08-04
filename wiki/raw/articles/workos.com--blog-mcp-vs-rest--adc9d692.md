---
title: "MCP vs. REST: What's the right way to connect AI agents to your API?"
url: "https://workos.com/blog/mcp-vs-rest?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q32026"
fetched_at: 2026-08-04T10:18:16.138453+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# MCP vs. REST: What's the right way to connect AI agents to your API?

Source: https://workos.com/blog/mcp-vs-rest?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q32026

For the past fifteen years, REST APIs have been the backbone of software integration. They're well-understood, battle-tested, and supported by a rich ecosystem of tooling. When a developer needs to integrate with your service, the workflow is familiar: read the docs, grab an API key, write some code that calls
GET /users/123
, parse the response, and handle errors.
But a new class of API consumer has arrived: LLM-powered agents. And these consumers need to
discover
what your API can do,
reason
about which operation to use, and
maintain context
across multi-step workflows, all at runtime, without a human writing integration code in advance.
This is the gap that the
Model Context Protocol (MCP)
fills. Originally published by Anthropic in November 2024, MCP is an open JSON-RPC-based standard that lets AI applications discover tools, resources, and prompts from external servers and invoke them through stateful sessions. It doesn't replace your REST API; it wraps it in a layer that AI agents can actually work with.
The question for developers building APIs today isn't "MCP or REST?" It's "Do I need both, and if so, how do they fit together?"
REST APIs: What they do well
REST APIs are general-purpose interfaces. They were designed to let any software system access another system's functionality or data, regardless of whether the client is a web browser, a mobile app, a CLI tool, or a microservice. They're stateless by design, which makes them easy to cache, load-balance, and scale horizontally. Decades of tooling exist around them: OpenAPI specifications, Swagger UI, Postman, API gateways, rate limiters, CDNs.
For traditional software clients (where a developer writes deterministic code that knows exactly which endpoint to call and what parameters to pass) REST is excellent. The API acts as an abstraction layer: the requesting application doesn't need to know the internal details of the service, just how to format requests and understand responses. A frontend engineer building a dashboard doesn't need their API to explain itself at runtime. They read the docs, write the fetch call, and move on.
REST also benefits from proven infrastructure. HTTP caching, content delivery networks, load balancers, and API gateways all speak REST natively. These techniques have demonstrated scalability over decades. When you need high-throughput, low-latency data fetching for a web application, REST remains the right tool.
Where REST falls short for AI agents
The problems emerge when the client is an LLM making autonomous decisions rather than a developer following a spec. REST wasn't created with AI or LLMs in mind, and that's fine, it wasn't supposed to be. But it means there are structural gaps when the consumer is an agent:
‍
No self-description at runtime.
A REST API doesn't tell you what it can do, you have to know that going in. OpenAPI specs exist, but they're static documents designed for developer tooling, not for an LLM to interrogate at runtime. If the API changes or new endpoints are added, a developer has to manually update the client code. The API itself can't say "hey, I have a new capability you might want to use."
‍
Stateless by design.
Each REST call is isolated. If an agent needs to look up a user, check their order history, then update their shipping address, it must manually pass context between each call. There's no session, no shared state, no memory of what happened two calls ago.
‍
Every API is a snowflake.
Each REST API has its own unique endpoints, parameter formats, authentication schemes, and error conventions. If an AI agent wants to use five different REST APIs, it needs five different adapters; five sets of custom integration code, each with its own assumptions and edge cases.
‍
Designed for developers, not for models.
REST API design principles emphasize composability, discoverability for humans, and atomicity (small endpoints that developers combine). These principles work well for human developers who read docs once, write code, and iterate cheaply. They actively hurt AI agents, who pay a token cost for every tool definition they have to reason over.
MCP: Purpose-built for AI agents
Where REST is a general-purpose interface that any software client can use,
MCP was explicitly designed to integrate LLM applications with external data and tools
. It standardizes patterns like providing context and invoking tools in ways that align with how AI agents actually operate.
A useful analogy: MCP is to AI applications what USB-C is to laptops. A laptop with USB-C ports can connect to any peripheral (monitors, drives, power supplies) regardless of manufacturer, because they all share a common standard. Similarly, an AI agent using MCP can connect to any MCP server (databases, code repositories, email systems, calendars) because they all speak the same protocol. It doesn't matter who built the server; the interface is identical.
MCP doesn't replace your REST API. It's a protocol layer that
sits on top of your existing APIs and makes them consumable by AI agents
. Your REST API handles the actual business logic. MCP provides the AI-native discovery and session management on top.
The three primitives
MCP servers advertise their capabilities through three types of primitives:
Resources
are endpoints for information retrieval. A resource handler might return data from a database, fetch a document, or list items in cloud storage. Importantly,
resources
are read-only or passive – they provide data but typically
do not cause side effects
. For example, an MCP server for a knowledge base might have a resource called
searchArticles
that takes a query and returns relevant articles from a corpus. The server’s request handler for
searchArticles
would handle the JSON-RPC request by executing the search and formatting the results to send back. Resources often need to handle large data (files, big query results), so their handlers might support
streaming chunks or pagination
for efficiency.
‍
Tools
are active operations that
can perform side effects or computations
. A tool handler might create a new record in a database, send an email, invoke an external API, or even control something like a web browser. Tools enable the AI to
act
on the world (within limits). For instance, an MCP server could expose a tool
sendSlackMessage
that, given a channel and message, posts to Slack. The request handler for this tool would contain the logic to call Slack’s API and return a success/failure result. Because tools can have effects, their handlers usually include validations and safety checks. They also define input parameters and output schema clearly, so the AI (and client) know how to use them.
‍
Prompts:
These are a bit unique: they are
reusable prompt templates or workflows
that the server can provide to guide interactions with the AI model. Essentially, a prompt capability might supply a pre-defined prompt or chain-of-thought that the AI can use. For example, a server could have a prompt called
sqlQueryTemplate
that helps an AI format a database query request consistently. The request handler for a prompt might not hit an external system at all, but instead return a carefully crafted template or even initiate a multi-step workflow involving the model (some advanced MCP servers use prompt capabilities to orchestrate complex interactions). Prompt handlers ensure the template variables are filled and the final prompt is delivered to the AI client.
Not every MCP server uses all three. In practice, many focus primarily on tools. But the important thing is that an AI agent can query an MCP server at runtime to discover which primitives are available and then invoke those capabilities through a uniform interface.
How discovery actually works
This is MCP's most significant departure from REST. When an MCP client connects to a server, it sends a
tools/list
request using JSON-RPC 2.0:
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}
The server responds with a machine-readable catalog of every available tool, including its name, a natural-language description, and a full JSON Schema defining its inputs:
{
  "tools": [
    {
      "name": "get_weather",
      "description": "Get current weather information for a location",
      "inputSchema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "City name or coordinates"
          }
        },
        "required": ["location"]
      }
    }
  ]
}
The same pattern works for
resources/list
and
prompts/list
. Because every MCP server publishes this machine-readable catalog, agents can discover and use new functionality without redeploying code. The agent retrieves the latest capabilities list each time it connects, picking up new features automatically.
This is fundamentally different from OpenAPI. An OpenAPI spec is a static document designed for developer tooling. MCP's
tools/list
is a live protocol interaction: the agent asks, the server answers, and the agent adapts.
One protocol, every server
Here's what makes the standardization matter practically: every MCP server, regardless of what service or data it connects to, speaks the same protocol and follows the same patterns. The tool invocation flow is always
tools/call
. The discovery flow is always
tools/list
. The initialization handshake is always the same.
If an AI agent wants to interact with five different services (GitHub, Slack, a database, Google Calendar, and a file system) and each has an MCP server, the agent uses the exact same protocol for all five. No custom adapters, no service-specific integration code. Build once, integrate many.
Stateful sessions
MCP maintains a persistent session between client and server. During initialization, both sides advertise what they support. The server declares whether it offers tools, resources, or subscriptions, and the client declares what it can handle. This mutual handshake creates a contract for the session.
Within that session, context persists. When an AI agent opens a file, runs tests, and identifies errors, it doesn't lose context between steps. This is the opposite of REST's stateless model, and it matters enormously for multi-step agentic workflows where each action depends on what happened before.
REST vs. MCP at a glance
Dimension
REST API
General-purpose
MCP server
AI-native
Primary consumer
Developer-written code (web apps, mobile clients, microservices)
LLM-powered agents that reason about which tool to call
Discovery
Static docs (OpenAPI specs, Swagger UI, READMEs a developer reads once)
Runtime protocol: agent sends
tools/list
and gets a live catalog
Communication
HTTP verbs on resource URLs
GET /books/123
JSON-RPC 2.0 method calls
tools/call → get_book
State
Stateless, each call is isolated, context passed manually
Stateful sessions, context persists across multi-step workflows
Interface consistency
Every API is unique: endpoints, params, errors, auth all vary
Every server speaks the same protocol: build once, integrate many
Auth
Anything goes: API keys, Basic, Bearer, OAuth 2.0, custom headers
OAuth 2.1 + PKCE: spec-mandated, scoped tokens, dynamic registration
Schema
OpenAPI / Swagger: developer-facing, static documentation
JSON Schema per tool: model-facing, machine-readable at runtime
Error handling
HTTP status codes (400, 404, 500, etc.)
Two layers: protocol errors (JSON-RPC) + tool execution errors
Scaling
Battle-tested (load balancers, CDNs, HTTP caching, decades of tooling)
Session-aware (persistent connections, lower overhead for multi-step tasks)
Integration cost
Custom glue code per service: N APIs × M agents = N×M adapters
Standardized: one protocol for all servers, eliminates N×M problem
MCP vs. REST: Layers, not adversaries
Here's the part that gets lost in the "MCP vs. REST" framing: in most real-world implementations,
MCP servers use REST APIs internally
to do their actual work.
Take the GitHub MCP server as a concrete example. It exposes high-level MCP tools like
repository/list
as primitives that any AI agent can discover and call through the standard MCP protocol. But internally, it translates each tool invocation into the corresponding GitHub REST API request. The MCP layer handles discovery, session management, and provides a uniform interface. The REST API handles the actual GitHub operations.
This pattern repeats across the ecosystem. Whether it's Stripe, Slack, Notion, or Salesforce, the MCP server is typically a thin, intelligent layer that translates between the MCP protocol and the underlying service's native REST API.
MCP and REST are not competing technologies. They're complementary layers in the AI stack. MCP provides an AI-friendly interface on top of the underlying functionality that REST APIs already deliver. Today you can find MCP servers for file systems, Google Maps, Docker, Spotify, Stripe, and a growing list of enterprise services, and nearly all of them are, under the hood, calling REST APIs.
Design for outcomes, not endpoints
The most common mistake developers make when adopting MCP is auto-converting every REST endpoint into an MCP tool. Tools like FastMCP's OpenAPI converter make this tempting: one line of code and your entire API is exposed to LLMs.
The problem is that a good REST API and a good MCP server have fundamentally different design goals.
A REST API is generous. It offers hundreds of small, composable endpoints because programmatic iteration is cheap. A human developer reads the docs once and their code can chain together
get_user()
, then
get_orders(user_id)
, then
get_order_details(order_id)
with fast network hops. For developers, more choice is good.
When you hand this same interface to an LLM agent, you're not empowering it, you're drowning it. The agent must load every tool description into its context window, pay a token tax on each one, and reason about which of your fifty user-related tools to call. Agentic iteration is expensive in ways that programmatic iteration isn't: every extra tool costs tokens and latency on every single interaction.
A better approach: design MCP tools around
what the user is trying to accomplish
, not around your internal API structure.
‍
Bad:
Three separate tools:
get_user
,
get_orders
,
get_shipments
; requiring the agent to make three round trips and hold intermediate results in conversation history.
‍
Good:
One tool (
track_order(email))
that calls all three endpoints internally and returns a complete, contextualized answer like "Order #12345 shipped via FedEx, arriving Thursday."
Same outcome, one call, designed for the actual consumer. Think of your MCP server as a user interface: same product thinking you'd apply to a UI, just for a non-human user.
Authentication: MCP's opinionated approach
REST APIs support a wide range of authentication mechanisms: API keys, Basic auth, Bearer tokens, OAuth 2.0, custom headers, mutual TLS. This flexibility is both a strength (it fits any use case) and a weakness (every integration needs its own auth implementation).
MCP takes an opinionated stance: OAuth 2.1 with PKCE is the standard. The MCP authorization specification, which has gone through several revisions (March 2025, June 2025, November 2025), defines how clients discover authorization requirements, register dynamically, and obtain scoped access tokens.
This matters for enterprise deployments. When an AI agent acts on behalf of a user, you need to know
which
user authorized
which
actions. OAuth 2.1's scoped tokens solve this: every access token declares exactly which resources and actions it authorizes, and the MCP server can verify at tool invocation time that the token has the specific scope needed for that operation.
WorkOS AuthKit
supports OAuth 2.1 as a compatible authorization server for MCP applications. It handles the complexity of the evolving protocol (dynamic client registration, Client ID Metadata Documents (CIMD), token validation, Protected Resource Metadata) so developers can focus on building the actual tools rather than implementing an OAuth provider from scratch.
When to use what
Keep your REST API for:
Web and mobile applications
where the client is developer-written code that knows exactly what to call.
High-throughput data fetching
where HTTP caching, CDNs, and load balancers provide performance benefits.
Third-party developer integrations
where human developers consume your API using SDKs and documentation.
Microservice communication
where services call each other in well-defined patterns.
Add MCP when:
AI agents are your consumer.
If you're building for Claude, ChatGPT, Cursor, or any LLM-powered tool, MCP gives them a way to discover and use your API without bespoke integration code.
You need multi-step workflows.
Stateful sessions mean the agent can chain operations without losing context.
You want write-once integrations.
Build one MCP server and it works with any MCP-compatible client; no custom adapter per model.
You need fine-grained authorization for agentic access.
OAuth 2.1 with scoped tokens gives you the controls enterprises require.
The practical architecture
In most production setups, MCP doesn't replace your REST API, it wraps it:
┌──────────────────────────────────┐
│  LLM Agent (Claude, Cursor...)   │
│  ↕ JSON-RPC / MCP Protocol       │
├──────────────────────────────────┤
│  MCP Server                      │
│  - Tool discovery & catalog      │
│  - Stateful session management   │
│  - Auth (OAuth 2.1)              │
│  - Outcome-oriented tool logic   │
│  ↕ HTTP                          │
├──────────────────────────────────┤
│  Your REST API                   │
│  - Business logic                │
│  - Data access                   │
│  - Existing infrastructure       │
└──────────────────────────────────┘
Your REST API continues to serve your web app, mobile app, and third-party integrations unchanged. Your MCP server sits alongside it as a new interface layer, providing the AI-native protocol that agents need.
Getting started
If you already have a REST API with an OpenAPI spec, the fastest path is to use that spec as a starting point, but resist the urge to auto-convert everything. Instead:
Identify the top five workflows
your users would ask an AI agent to perform with your API.
Design outcome-oriented tools
for those workflows. Each tool should return a complete, useful result in one call.
Use your REST API as the backend.
Your MCP server calls your existing endpoints internally, no need to rewrite business logic.
Implement
OAuth 2.1
for auth.
Use an identity provider like WorkOS AuthKit that already supports MCP's authorization requirements out of the box.
Test with real MCP clients.
Connect to Claude Desktop, Cursor, or the MCP Inspector to verify the agent experience feels right.
The SDKs are mature enough for production use. FastMCP (Python), the official MCP TypeScript SDK, and platforms like Stainless can accelerate server creation. But the most important work isn't in the tooling, it's in the design. The difference between a mediocre MCP server and a great one is the same difference between a bad UI and a good one:
understanding your user
. The user just happens to be an LLM.
The bottom line
REST APIs aren't going anywhere. They remain the right choice for traditional software clients, high-performance data access, and developer-facing integrations. But when the client is an LLM agent, one that needs to discover capabilities at runtime, reason about which tool to use, and maintain context across multi-step tasks, REST alone isn't enough.
MCP provides the missing layer: runtime discovery, stateful sessions, standardized auth, and a protocol designed from the ground up for how AI agents actually work. The two aren't competing standards, they're complementary layers in the stack:
Your REST API handles the business logic.
MCP makes that logic accessible to the AI agents that are increasingly becoming the primary way users interact with software.
The enterprises building for this future are the ones that will be ready when agents become the default interface.
