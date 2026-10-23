---
title: "Death to long-lived static credentials (Vercel)"
source_url: "https://vercel.com/blog/death-to-long-lived-static-credentials"
fetched: 2026-10-23
sha256: f45cb40bd2fa352398eb2b81d38f8c440ab92727e081a4daa843c8e7809f9a5c
---

Death to long-lived static credentials — Malte Ubl (CTO, Vercel), Blog, 22 Oct 2026, 6 min read.

Fifteen years ago, TLS was something you'd use to protect the most sensitive areas of your app. Then Google, Let's Encrypt, the EFF, and others led the push for HTTPS everywhere. Machine-to-machine authentication still resembles HTTPS in 2010, with some vendors leading while long-lived static credentials remain the default for many SaaS vendors and infrastructure providers. Vercel built OIDC UI (a shadcn/ui registry for trust-policy forms and token verification code), is expanding OIDC support, and setting new authentication requirements for Marketplace providers.

Long-lived static credentials (API keys, DB passwords) reused with no expiration. As agents take on more work, they're granted credentials granting permissions far beyond the task. Those credentials can leak into a repo or chat, be stolen via dependency compromise, or be exposed when prompt injection leads an agent to reveal them. Vercel previously spent thousands of engineering hours on painful key rotations.

Better solutions: OIDC — a trusted issuer provides a signed, short-lived token; receiving service verifies it. Stolen token expires. Vercel OIDC federation GA since 2024 (exchange Vercel-issued identity tokens for temporary AWS/GCP/Azure credentials). Expanding OIDC to Blob, AI Gateway, Sandbox.

The rest of the web hasn't followed: surveyed 1,000+ SaaS vendors, only 8.4% supported secure authentication methods. Barriers: (1) tooling/setup complexity, (2) token-exchange latency on request path, (3) weak vendor incentives. Goal: make secure authentication the default on Vercel and push Marketplace vendors.

Quoted from Malte Ubl's earlier post (Jul 2026, quoted by @jobergum): "If you are building a runtime platform in 2026 and dont support OIDC, what are you even doing?"
