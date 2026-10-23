---
title: "Vercel — Death to long-lived static credentials (OIDC push)"
created: 2026-10-23
updated: 2026-10-23
type: event
tags: [announcement, security, supply-chain, vercel, ai-agents, prompt-injection, event]
sources:
  - https://vercel.com/blog/death-to-long-lived-static-credentials
  - raw/articles/vercel.com--blog-death-to-long-lived-static-credentials--2026-10-23.md
  - https://x.com/jobergum/status/2113515603923173478
---

# Vercel — Death to long-lived static credentials

On 2026-10-22 **Malte Ubl** (CTO, Vercel) published *"Death to long-lived static
credentials"*, arguing that machine-to-machine authentication in 2026 resembles
HTTPS in 2010: encryption-at-rest is assumed, but **long-lived static credentials
(API keys, DB passwords) remain the default** for many SaaS vendors and infrastructure
providers. Vercel is pushing OIDC as the replacement, drawing a direct parallel to the
"HTTPS everywhere" movement led by Google, Let's Encrypt and the EFF.
Article: https://vercel.com/blog/death-to-long-lived-static-credentials

## Why it matters for AI agents

The post explicitly ties the credential problem to **agentic AI**: as agents take on
more useful work, they're granted credentials that "can grant permissions far beyond
the task at hand." Those credentials can leak into a repo or chat, be stolen when a
dependency is compromised, **or be exposed when prompt injection leads an agent to
reveal them**. A stolen long-lived credential stays exploitable until revoked; Vercel
recalls spending "thousands of engineering hours" on painful key rotations it never
wants to repeat. This reframes OIDC adoption as an **agent-safety / blast-radius**
issue, not just a hygiene one — a credential that a prompt-injected agent is tricked
into leaking only carries short-lived, scoped authority if OIDC is in use.

## The proposal

- **OIDC** replaces stored provider keys: a trusted issuer provides a signed,
  short-lived token identifying the application; the receiving service verifies it
  before granting access. A stolen token expires, limiting exposure.
- Vercel's **OIDC federation** has been GA since 2024 — Vercel apps exchange
  Vercel-issued identity tokens for temporary AWS/GCP/Azure credentials under
  project/environment trust policies. Expanding OIDC to Blob, AI Gateway, Sandbox.
- **OIDC UI**: a shadcn/ui registry giving providers trust-policy forms and token
  verification code, to lower the setup barrier.
- New **Marketplace authentication requirements** for Vercel Marketplace providers,
  using Vercel's leverage to push vendors toward secure auth.

## The gap (data)

Vercel surveyed **1,000+ SaaS vendors** and found **only 8.4% supported secure
authentication methods**. Three adoption barriers identified:
1. Tooling/setup makes secure auth more complex than a static key.
2. Added latency from token fetching/exchange on the request path.
3. Weak vendor incentives to offer/prioritize secure auth.

## Context

Amplified by **Jo Kristian Bergum** (@jobergum, Hornet CEO / former Vespa Chief
Scientist) on 2026-10-23 ("Great post by @cramforce"), quoting Malte Ubl's earlier
July 2026 take: *"If you are building a runtime platform in 2026 and don't support
OIDC, what are you even doing?"*

## Related

- [[concepts/ai-supply-chain-security]] — credential theft / dependency compromise.
- [[concepts/prompt-injection]] — the agent-leak vector the post cites.
- [[entities/vercel-sandbox]] / [[entities/vercel-eve]] — Vercel services under the OIDC push.
- [[entities/jo-kristian-bergum]] — amplified the post.

## Sources

- Vercel blog: https://vercel.com/blog/death-to-long-lived-static-credentials
- Bergum amplification: https://x.com/jobergum/status/2113515603923173478
