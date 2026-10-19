---
title: "AAuth — Client Identity Protocol for AI Agents"
created: 2026-10-18
updated: 2026-10-18
type: concept
aliases: [AAuth, draft-hardt-oauth-aauth-protocol, agent authorization protocol]
tags:
  - concept
  - protocol
  - agent-identity
  - agent-security
  - agent-communication
  - security
  - ai-agents
  - mcp
sources:
  - raw/articles/2026-10-18-aauth-protocol-site.md
  - raw/articles/2026-10-18-keycard-aauth-intent-auth-panel-transcript.txt
related: [concepts/agent-identity-and-authentication, entities/dick-hardt, entities/keycard, concepts/agent-delegation-budgets, concepts/intent-based-authorization, concepts/security-and-governance/agent-identity-verification, concepts/infrastructure-level-sandbox]
confidence: high
---

# AAuth — Client Identity Protocol for AI Agents

**AAuth** is an HTTP authorization protocol that gives every HTTP client — specifically, every AI
agent — its own cryptographic identity, so agents can call protected resources with **signed
requests instead of bearer tokens or API keys**. It was authored by **Dick Hardt** (author of
OAuth 2.0) and is specified as an IETF Internet-Draft,
`draft-hardt-oauth-aauth-protocol`. AAuth is designed to *coexist* with OAuth 2.0 and OpenID
Connect rather than replace them.

Official site: `https://aauth` + `.dev` (protocol explorer at `explorer.aauth` + `.dev`, demo
resource `whoami.aauth` + `.dev`). Reference implementations under `github.com/aauth-dev`
(`@aauth/bootstrap`, `@aauth/fetch`, `auth-go`, .NET samples).

## Why OAuth does not fit agents

The project's origin story is concrete: after implementing authorization for an MCP server, Hardt
concluded OAuth was the wrong shape for agentic clients and went to work with others in the
identity community who had hit the same wall. The site frames the mismatch as six failures of
build-time assumptions under runtime agents:

| Failure | What breaks for agents |
| --- | --- |
| **Client IDs don't travel** | In OAuth/OIDC a client has no independent identity — a `client_id` at Google is meaningless at GitHub. An agent has no identity of its own to carry between services. |
| **Copied secrets leak** | An API key is a shared secret issued by the service and *copied* into the client. Any secret copied into a workload eventually leaks. |
| **Decisions happen mid-task** | Agents need authorization decisions while a task is running. Consent lands on human timelines, and today's protocols treat *pending* as an error rather than a first-class state. |
| **Tool chains assemble live** | Agents pick their tool chain at runtime, one call at a time; the sequence is never declared in code. |
| **Scopes don't capture intent** | A scope is standing permission, not per-call intent. `mail.read` looks identical whether the agent is summarising one thread or scraping the mailbox — policy cannot tell the two apart. |
| **Calls cross trust domains** | One task spans orgs, clouds and identity domains; workload identity (SPIFFE) — and therefore authority — stops at the trust-domain edge. |

The site's summary line: *the web gave servers identity; it is time clients got the same.*

## Token model

AAuth carries **identity claims and authorization claims in the same token**. The token types:

- **`agent_token`** — establishes the agent's own cryptographic identity (the agent's key,
  published with agent metadata at a URL the agent/operator controls and resolved via JWKS).
- **`person_token`** — names the *person* the agent acts for, at one resource.
- **`resource_token`** — describes the access the resource requires.
- **`auth_token`** — grants an agent access to a resource.
- **`session-token`** — issued by a resource **for its own consumption, deliberately opaque to the
  agent**.
- **`jwks_uri`** — the person server's JWKS endpoint, discovered via well-known metadata.

## Five access modes + per-call authorization

AAuth defines five incremental access modes, all of which replace API keys with cryptographic
identity. They differ in what the resource ends up knowing and which party established it:

1. **Identity based** — an HTTP Signature (`HTTPSig`) carrying an `agent_token` is enough; the
   resource learns the agent's `sub` from the signature alone. No person server, no consent, no
   bearer token.
2. **Resource managed** — the resource decides and issues its own grant.
3. **Person identity** — the person's identity is bound into the call.
4. **Person server managed** — a third-party *person server* stands between agent and resource and
   mints the `auth_token` after the human decides.
5. **Federated** — authority crosses organisational trust domains.

On top of these, **per-call authorization** (from the companion `R3` draft) governs a *single
action* rather than a class of access, and treats **consent-pending as a first-class protocol
state** (401 + resource_token → POST → 202 pending + approval code → poll → 200 with `auth_token`).

## Adoption surface

AAuth is being demonstrated as an agent-native protocol: the site ships a prompt you can paste into
Claude Code, Cursor or any CLI agent that walks a user through bootstrapping a keypair, publishing
agent metadata, and making signed calls. That "paste-a-prompt-to-adopt-a-protocol" pattern is itself
notable — the onboarding path for a wire protocol is now an agent skill rather than a developer
reading an RFC.

Community discussion around it includes Christian Posta ("Do we even need agent identity?",
"Exploring AAuth"), Karl McGuinness (a "mission layer" on AAuth) and Mark Hendrickson (agent
attribution). AAuth events were scheduled for 15 October (AAuth Night) and 19 October 2026
(AAuth Workshop).

## Relationship to OAuth and other identity work

AAuth is additive, not a fork: OAuth/OIDC continue to serve human-delegated web login, while AAuth
covers the client-identity gap that OAuth never attempted. Compared with **A2A Signed Agent Cards**
(which verify the authenticity of a published agent card via Sigstore/Rekor), AAuth operates at the
HTTP call layer and answers a different question: not "is this agent card genuine?" but "which
agent, acting for which person, is allowed to make *this specific call* right now?".

## Open questions

- **Deployment reality.** The drafts are individual submissions to the IETF, not working-group
  documents; adoption outside the identity-community circle is unverified as of October 2026.
- **Key custody.** Giving every agent a private key raises the question of where keys live — see
  [[concepts/agent-delegation-budgets]] and the brain/hands split discussed there.
- **Interaction with browser-side agent detection.** A cryptographic agent identity is only useful
  if resources actually check it; the Resy incident (see
  [[concepts/intent-based-authorization]]) shows most sites still default to blanket bot-blocking.

## See also

- [[entities/dick-hardt]] — author of OAuth 2.0 and of AAuth
- [[concepts/intent-based-authorization]] — the runtime-policy layer AAuth's per-call model enables
- [[concepts/agent-delegation-budgets]] — time-and-resource budgets on issued grants
- [[concepts/security-and-governance/agent-identity-verification]] — A2A Signed Agent Cards, the
  discovery-layer counterpart
