---
title: "The New MCP Roadmap (Model Context Protocol)"
url: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
date: 2026-08-22
fetched_at: 2026-08-26
source: modelcontextprotocol.io (official MCP blog)
authors:
  - David Soria Parra (Lead Maintainer)
  - Den Delimarsky (Lead Maintainer)
tags: [mcp, roadmap, protocol, agent-communication, enterprise-security, governance]
---

# The New MCP Roadmap

An update on the Model Context Protocol roadmap and focus areas for upcoming specification releases.

August 22, 2026 · 6 min · David Soria Parra (Lead Maintainer), Den Delimarsky (Lead Maintainer)

## Looking back

The previously published roadmap came out in March with four priority areas: transport evolution and scalability, agent communication, governance maturation, and enterprise readiness. Significant progress was made in all of these over the past five months.

The bulk of the changes landed in the 2026-07-28 specification release:

- **Stateless servers**: Protocol-level sessions and the initialization handshake are gone, so a server can scale horizontally without holding state (SEP-2575, SEP-2567).
- **`server/discover`**: Clients can now call `server/discover` to learn a server's supported versions and capabilities before doing anything else.
- **Cacheable list results**: List results are now cacheable (SEP-2549).
- **Tasks as extension**: Tasks were reworked based on early adopter feedback — moved into an official extension (SEP-2663).
- **Multi Round-Trip Requests**: The brand-new Multi Round-Trip Requests pattern (SEP-2322) replaced server-initiated requests so that elicitation and similar flows work on stateless servers.
- **Server Card Working Group**: Continues work on `.well-known` metadata conventions for MCP servers, so a server can be discovered and reasoned over without connecting to it.

Governance evolved: a Contributor Ladder was formally adopted, Working Groups now triage SEPs in their own area, and the specification has a proper feature lifecycle and deprecation policy that the 2026-07-28 deprecations were the first to follow.

Enterprise readiness was heavily focused on security in the past release cycle, most of it arriving as authorization improvements: issuer validation, issuer-bound client credentials, and Client ID Metadata Documents (CIMD) as the preferred registration path for clients, with Enterprise-Managed Authorization available as an extension (now stable).

## Priority areas

The new roadmap is organized into five priority areas. Several pick up work the previous roadmap listed as being on the horizon (server-initiated events, result type improvements, agent identity) that have since matured enough to become priorities in their own right. Each area has a set of Core Maintainers responsible for it and one or more Working Groups.

### 1. Agentic messaging primitives

Modern agentic workloads no longer fit the standard request-and-response pattern. Loops can run for longer, servers can push streamed results, and there is a clear need to steer work mid-flight. MCP has been growing to meet these requirements, introducing Tasks, subscriptions/listen, and progress notifications. The work here spans:

- **Server-initiated events** — webhooks and channels, so clients aren't left polling for results
- **Composition review** across the Agents, Transports, and Triggers & Events Working Groups
- **Maturing the Tasks extension** (SEP-2663) so it can move into the specification

### 2. HTTP-native transport unification and hardening

With the 2026-07-28 release, a remote MCP server is now no different from any other HTTP workload, making it easy to host and operate one on any infrastructure that developers and organizations already use for their APIs and services. This approach has proven to scale, and the team wants to stretch it to cover other deployment modes as well, including local servers speaking Streamable HTTP over stdio. Unifying on one transport lets MCP server and client development be simplified even further.

### 3. Agent identity and enterprise-ready security

MCP authorization today is built around a person approving access in a browser. That works well for interactive clients, but more and more of the callers are agents running as cloud workloads with their own identity, acting on behalf of a user who isn't present, or delegating narrower authority to sub-agents. MCP servers need a standardized way to recognize and trust those agent identities, built on existing standards rather than pasted API keys and long-lived tokens.

The work covers:

- **Finalizing Demonstrating Proof of Possession (DPoP)** and driving its adoption
- **Defining an opinionated path for agent identity and delegation** through Workload Identity Federation, the ID-JAG grant behind Enterprise-Managed Authorization, and standard token exchange
- **Continuing engagement with OAuth standards bodies** — IETF OAuth and WIMSE working groups — to help the underlying standards evolve with the building blocks that agent identity needs

### 4. Improved primitives

Tool calling is the part of MCP most developers touch first, and it has held up well over the lifetime of the protocol. Where it falls a bit short is in result handling: a `tools/call` response can carry the same output in more than one form, and a server developer today has no way to know which form a given client will put in front of the model. The team aims to standardize on one clear contract.

The other challenge is the ever-growing scale of primitives. Connecting to a server with a hundred tools means the model pays for that entire surface before the user has asked a single question, and tool selection tends to get worse as the list grows. A **progressive discovery** effort is starting so a server can offer a small entry point and reveal more of its catalog as the conversation narrows.

### 5. Improved SDK developer experience

The SDKs are how developers experience MCP. Investment is going into their ergonomics and conformance with the specification, and making them intuitive and well-documented across every platform and language. This is more important now that many developers build MCP clients and servers by pointing an agent at the libraries, where clear APIs and accurate docs decide whether the code will work with minimal friction.

## Proposal prioritization

Specification Enhancement Proposals (SEPs) that fall within these priority areas get expedited review and have the best chance of acceptance. Proposals outside them aren't rejected automatically, but maintainer review time is scarce and goes to these areas first.

If considering a SEP: identify the priority area it belongs to, raise it with the relevant Working Group, and work with its members to shape the proposal. Each area on the roadmap names the Core Maintainers responsible for it.

## Get involved

Every priority area has a Working Group behind it (or forming around it), and all of them have room for more contributors:

- Join a Working Group or Interest Group (see the Working and Interest Groups page and the community channels)
- Propose or comment on a SEP (read the SEP guidelines, then open one or weigh in)
- Start an experimental extension — SEP-2133 lets any WG or IG experiment in an `experimental-ext-` repository before a formal SEP
- Contribute directly (the contributing guide covers the specification, SDKs, and tooling)

**HN discussion**: https://news.ycombinator.com/item?id=49399591 (269 points, 160 comments, Aug 22 2026)
