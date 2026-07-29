---
title: "Bringing MCP 2026-07-28 to Claude"
type: article
date: 2026-07-28
date_ingested: 2026-07-29
source_url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
author: Anthropic
tags: [mcp, anthropic, claude, protocol, stateless, oauth, extensions]
---

# Bringing MCP 2026-07-28 to Claude

The fifth spec release of the Model Context Protocol, **MCP 2026-07-28**, is live today. The latest spec moves MCP to a stateless core, while hardening authorization and graduating official extensions. Support is being rolled out across Claude products.

## What's new in MCP

MCP recently surpassed **400M monthly SDK downloads**, a 4x increase this year, and has become the industry standard for connecting AI agents to applications.

MCP 2026-07-28 is one of the most significant spec releases to date:

- **Stateless core.** MCP moves from a bidirectional stateful protocol to a request/response model. Servers can now deploy on serverless and edge infrastructure. This simplifies the experience of building MCP servers for Claude and scaling their usage as they grow in adoption.
- **Standardized extensions.** MCP Apps and Tasks now ship under a versioned extensions framework, giving developers a formal path to add capabilities like interactive UIs and long-running work without changing the core protocol.
- **Auth hardening.** Authorization now aligns with production OAuth 2.0 and OIDC deployments, so MCP servers connect to enterprise identity systems like Entra or Okta without workarounds.

## Industry Endorsements

Companies across the ecosystem have been building on the new spec alongside the MCP community since beta:

- **Figma** (Josh Clemm, VP of Engineering): "More builders are using our MCP server to bring generated outputs into Figma's canvas... with MCP Apps, Tasks, and Enterprise-Managed Auth, we can do even more to keep design and code together in one, connected flow."
- **Intuit** (Chris Kasten, Chief Architect and SVP of Engineering): "The stateless protocol core and extensions framework, including MCP Apps and Tasks, let our technologists and customers build and connect agentic experiences at enterprise scale."
- **Netlify** (Sean Roberts, VP of Applied AI): "The stateless core in the 2026-07-28 spec makes MCP a first-class HTTP workload with no session management to work around."
- **Paul D'Ambra** (Product Engineer): "Moving MCP to a stateless protocol makes it easier to scale our own service and makes it easier for us to add analytics for our customers' MCP servers."
- **Andrew Goodman** (VP of AI): "The stateless core in the open MCP 2026-07-28 spec reduces the complexity we manage, so we can ship more features to our customers, faster and at scale."
- **Zoom** (Ross Mayfield, Head of Product for AI Platform): "The new MCP spec makes it far easier to deploy and scale MCP servers on standard HTTP infrastructure."

## Advancing MCP in Claude

Claude now lists over **950 MCP servers** in the connectors directory, used by millions of people every day. This year Anthropic shipped support for new protocol extensions alongside features that make MCP easier to build on and deploy:

- **MCP Apps** — Let servers render interactive UI directly in the conversation. Users can see what a connector is doing and work with it inline, without switching tabs.
- **Enterprise-managed auth** — Admins provision MCP connectors for their whole organization through their identity provider. Admins authorize a connector once, users inherit access through their existing IdP groups, and it's connected on first login: zero-touch setup for the end user.
- **Observability** — Published connectors in the directory get a dashboard showing how they perform across Claude product surfaces. Developers can track adoption, diagnose errors and latency, and break down usage by product.
- **MCP tunnels** (research preview) — Connect Claude to MCP servers inside a private network without exposing them to the public internet. Teams can bring internal tools to Claude with no inbound firewall rules, no public endpoints, and no IP allowlisting on the origin.

## Getting Started

Explore the spec and SDKs to get started. Support is rolling out across Claude products soon. If you're planning to submit your MCP server to Claude's connectors directory, you can learn more there.

See the [MCP 2026-07-28 release announcement](https://modelcontextprotocol.io) for full details on the new spec.
