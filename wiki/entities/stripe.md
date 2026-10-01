---
title: Stripe
created: 2026-09-29
updated: 2026-10-01
type: entity
tags: [company, fintech, ai-agents, infrastructure]
sources:
  - https://stripe.com/blog/agentic-commerce-suite
  - https://blog.cloudflare.com/agents-stripe-projects/
  - raw/articles/2026-09-30_stripe_ousd-default-stablecoin.md
  - raw/articles/2026-09-25_stripe-knowledge-ai-platform-kai.md
  - raw/articles/2026-05-10_cursor_stripe.md
  - https://stripe.dev/blog/meet-stripes-knowledge-ai-platform
  - https://stripe.com/blog/ousd-now-live-on-stripe
confidence: high
---
# Stripe

Payment infrastructure company (founded 2010, Dublin/SF; Patrick and John Collison).
Historically the default payments rails for internet businesses; increasingly the
**payments layer for AI agents** in the agentic commerce ecosystem — and, as of
September 2026, a stablecoin-native financial platform.

## Stablecoin infrastructure: OUSD default (September 2026)

On September 30, 2026 Stripe made **Open USD (OUSD)** — the stablecoin from the
**Open Standard** consortium — the **default stablecoin across its products**
([raw article](raw/articles/2026-09-30_stripe_ousd-default-stablecoin.md)).

- **What is OUSD**: a stablecoin issued by [Open Standard](https://joinopenstandard.com/),
  whose founding companies are **Coinbase, Mastercard, Shopify, Stripe, and Visa**,
  backed by 200+ network partners. Available on **Base, Ethereum, Solana, and Tempo**
  (Stripe's default configuration is OUSD on Tempo — the L1 blockchain Stripe
  co-developed for payments).
- **Deep product integration**: receive/hold/send/spend via **Treasury**; global card
  programs via **Issuing**; **Global Payouts**; fiat↔OUSD conversion via **Crypto
  Onramp**; merchant acceptance via **Payments**.
- **Economics**: low, volume-predictable transaction fees, **no mint/burn fees**;
  Open Standard partners **earn rewards on OUSD activity** (including balances held on
  Stripe) — unusual, since most businesses earn nothing on stablecoin float. Joining is
  free.
- **Stack partners**: **Bridge** (orchestration APIs for OUSD↔fiat/stablecoin
  conversion) and **Privy** (wallet infrastructure; post authored by Privy CEO
  Henri Stern). Finance platform **Ramp** will use Stripe-powered stablecoin accounts
  for 24/7 OUSD balances, rewards, and payments.
- **Migration stance**: existing stablecoin balances are **not** force-converted;
  Stripe keeps multi-stablecoin, multi-chain flexibility.

This makes Stripe the distribution channel that turns a consortium stablecoin into the
default settlement asset for millions of businesses — a "rails layer" play that couples
Stripe's own Tempo chain, Bridge/Privy (both Stripe-acquired startups) and the Open
Standard issuer into one stack.

## Agentic commerce infrastructure

- **Agentic Commerce Suite** (May 2026) — agent-facing product line for invoicing,
  checkout, and machine-readable payment flows. See [[concepts/agentic-commerce]].
- **Invoice Payment MCP** (`xmcp-stripe-invoice`) — lets agents send/pay Stripe
  invoices via natural language, no dashboard access.
- **Link CLI** ([github.com/stripe/link-cli](https://github.com/stripe/link-cli)) —
  one-time-use payment credentials for agents; combined with Stripe Issuing forms
  an "agent wallet" stack.
- **Stripe Projects / Stripe Accounts with Cloudflare** — co-designed so agents can
  create accounts, buy domains, and deploy autonomously. See [[entities/cloudflare]].
- [[entities/metronome]] (usage-based billing) — acquired by Stripe; being integrated
  into Stripe's billing ecosystem.

## Internal AI platform

- **Knowledge AI Platform "KAI"** (July 2026, stripe.dev) — Stripe's internal agent
  platform for non-coding knowledge work, connecting employees to **1,000+ internal
  tools and skills**; handles everything from quick queries to multi-day projects.
  One of the largest known enterprise non-coding agent deployments. See
  [raw article](raw/articles/2026-09-25_stripe-knowledge-ai-platform-kai.md).
- **Cursor at scale** (Feb 2026) — Stripe rolled out a consistent Cursor experience to
  **3,000 engineers** (Cursor customer story;
  [raw article](raw/articles/2026-05-10_cursor_stripe.md)).

## Relevance to AI/agents

Stripe is the payment-rails counterpart to agent identity/auth infrastructure: agentic
commerce, agent wallets, and pay-per-token/usage billing all route through it. Its
billing acquisition (Metronome) targets the token-economics metering problem, and the
OUSD default gives agents and platforms a low-fee, always-on settlement asset — the
stablecoin leg of the agent-economy payment stack alongside x402-style HTTP-402 flows
(see [[entities/cloudflare]]).

## Related

- [[concepts/agentic-commerce]] — the concept this entity anchors
- [[entities/cloudflare]] — co-designed agent account/domain flows
- [[entities/metronome]] — acquired; usage-based billing
- [[entities/stripe-link-cli]] — agent wallet CLI tool
