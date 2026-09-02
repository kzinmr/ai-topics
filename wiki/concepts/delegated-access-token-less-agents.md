---
title: "Delegated Access — Keeping OAuth Tokens Out of Agent Runtimes (WorkOS Relay)"
created: 2026-09-02
updated: 2026-09-02
type: concept
tags:
  - concept
  - security
  - ai-agents
  - agent-identity
  - architecture
  - protocol
sources:
  - raw/articles/workos.com--blog-delegated-access-for-ai-agents--d4547139.md
confidence: medium
---

# Delegated Access — Keeping OAuth Tokens Out of Agent Runtimes

## TL;DR

An agent runtime erases the trusted-code / untrusted-input boundary: a scraped page or GitHub issue becomes an instruction. Put a long-lived OAuth token in that environment and it leaks through ~7 ordinary pathways (context window, tool-call logs, provider logs, stdout, error payloads, memory stores, exfiltration-by-design) — none of which is a bug. WorkOS **Relay** (early access, Sept 2026) removes the premise: the agent never holds the token; it names the provider + user, and WorkOS injects the credential on the way out.

## Why Tokens Leak From Agent Runtimes (No Bug Required)

A single provider token in an agent runtime tends to exist in:

1. Context window (agent reads its own config / debugs a call)
2. Tool call arguments (logged verbatim by observability layers)
3. Model provider logs (token passed through a prompt)
4. stdout/stderr (agent-composed `curl` doesn't redact its own headers)
5. Error reporting (failed HTTP requests serialize request headers)
6. Scratch files / memory stores (never treated as secret material)
7. Exfiltration path — an agent with token + network can simply be *talked into* sending both elsewhere

The leak-path thought experiment: a GitHub-triage agent holding a user token; an issue body ends with a line addressed to the agent asking it to include its Authorization header in a diagnostic request to an attacker URL. Compliance is probabilistic ("depends on the model, the prompt, and the day") — credential security acquires a probabilistic component, and a 99/100 defense is not a control anyone would accept elsewhere.

## Why Scopes and Rotation Don't Fix It

| Instinct | Why it falls short |
|----------|-------------------|
| Narrow scopes | OAuth scopes were designed for apps, not agents; "minimum the agent needs" ≈ most of the account's capability |
| Short lifetimes / rotation | Leak path is a property of the runtime, not a moment in time; refresh flows add refresh material worth more than the access token |

Both accept the flawed premise: **the token has to be in the agent's environment.**

## The Relay Mechanic (Credential-Exfiltration-Proof Proxy)

Agent sends request to WorkOS: `Authorization` = WorkOS API key, `X-Relay-URL` = target, `X-Relay-User` = on-behalf-of user (+ optional `X-Relay-Organization`, `X-Relay-Provider`). WorkOS verifies, resolves the connected account, fetches/refreshes the credential from its store, strips control headers, injects the provider token, streams the response back. Converting a direct call = header edit, not a rewrite. Error semantics are "honest" (Relay 4xx vs provider 4xx distinguished) so failures are debuggable.

Design lineage: same shape as Cloudflare Access service tokens / secrets-manager sidecars — the general pattern is **capability description instead of credential custody**. This is the concrete answer to the "easy mode vs hard mode" agent-identity problem [[entities/aaron-levie]] posed (agents inheriting full user identity).

## Position in the Agent-Identity Stack

- Upstream: agent registration/verification → [[concepts/workos-auth-md]] (Auth.md, June 2026)
- Peer: NHI governance, ephemeral credentials, behavioral monitoring → [[concepts/security-and-governance/agent-iam]]
- Threat model this addresses: prompt injection with credentials in context → [[concepts/prompt-injection]]
- Alternative mitigation philosophy: run capable agents isolated + monitored instead of removing tools/tokens → [[entities/simon-willison]] "Don't Defang Your Agents, on Purpose" (moz:fest, 2026-08-29)
- Broader category: [[concepts/security-and-governance/agent-control-plane]]

## Open Questions

- Early access only; no public availability/pricing or adoption numbers yet (confidence: medium — vendor-authored source).
- Proxy adds a hop + availability dependency on WorkOS for every outbound third-party call.
- Whether "honest error semantics" fully solve the pass-through proxy debugging problem needs third-party validation.

## Sources

- WorkOS blog, "How to let AI agents act on behalf of users without handing them access tokens" (via Daring Fireball RSS, fetched 2026-09-01) ^[raw/articles/workos.com--blog-delegated-access-for-ai-agents--d4547139.md]
