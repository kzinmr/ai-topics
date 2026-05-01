---
title: Agentic Commerce
created: 2026-05-01
updated: 2026-05-01
type: concept
tags: [concept, ai-agents, platform, protocol, infrastructure]
sources:
  - https://stripe.com/blog/agentic-commerce-suite
  - https://blog.cloudflare.com/agents-stripe-projects/
  - https://open.substack.com/pub/bensbites/p/building-gets-easier
---

# Agentic Commerce

**Agentic Commerce** is the emerging paradigm where AI agents autonomously discover products, negotiate purchases, and complete financial transactions on behalf of human users. It represents the convergence of AI agent infrastructure and payments infrastructure — enabling a new economy where agents are both buyers and intermediaries.

Stripe launched the **Agentic Commerce Suite** in April 2026, establishing itself as the foundational infrastructure provider for this economy. The suite was co-developed with OpenAI and released alongside complementary infrastructure from Cloudflare (via Stripe Projects).

## Core Components

### Discovery: Making Products Agent-Readable

Businesses upload their product catalog to Stripe, which syndicates it to AI agents via a hosted **ACP** (Agentic Commerce Protocol) endpoint. This allows agents to browse products with near real-time price, availability, and description data — without businesses needing bespoke integrations for each agent platform.

### Checkout: In-Chat Transactions

Stripe powers embedded checkout flows within AI interfaces. Microsoft Copilot Checkout (powered by Stripe) and ChatGPT Instant Checkout are early examples — users complete purchases without leaving the chat. Google's **UCP** (Universal Commerce Protocol), announced at NRF 2026, is another protocol in this space; Stripe's suite supports it without additional integration.

### Payments: Shared Payment Tokens (SPTs)

The key payment primitive. SPTs allow agents to initiate payments using a buyer's saved payment method **without exposing actual payment credentials**. Every token is:

- **Scoped** to a specific seller
- **Bounded** by time and amount
- **Observable** throughout its lifecycle
- Protected by Stripe Radar fraud detection

This solves the core security challenge of agentic payments: agents can spend money but can't steal credentials or exceed authorized limits.

### Agent Wallets: Link CLI

The **Link CLI** ([github.com/stripe/link-cli](https://github.com/stripe/link-cli)) provides one-time-use payment credentials for agents. An agent can pay for cloud resources, API calls, or services without exposing real card details. Combined with Stripe Issuing for agents, this creates a full agent wallet infrastructure.

## Protocols

| Protocol | Origin | Purpose |
|----------|--------|---------|
| **ACP** | Stripe + OpenAI (Sep 2025) | Product discovery, checkout, agentic payments |
| **MPP** | Stripe | Machine-to-machine payments (cards, stablecoins, BNPL) |
| **UCP** | Google (NRF 2026) | Competing/parallel discovery + commerce protocol |
| **x402** | Community | HTTP 402-based machine payments |

Stripe's Agentic Commerce Suite supports all protocols through a single integration.

## Infrastructure Integration: Stripe Projects

Co-designed with Cloudflare, **Stripe Projects** ([projects.dev](https://projects.dev)) lets agents provision cloud infrastructure and pay for it in a single flow. An agent can:

1. Create a Cloudflare account
2. Start a paid subscription (via Stripe)
3. Register a domain
4. Obtain an API token
5. Deploy code to production

— all without a human touching a dashboard or entering credit card details.

## Strategic Significance

Agentic commerce represents the next frontier for both AI agents and payments infrastructure:

- **For businesses**: A new distribution channel — being discovered by AI agents becomes as important as SEO was for the web
- **For agent platforms**: Commerce capability turns agents from information tools into economic actors
- **For Stripe**: Positions as the TCP/IP layer of the agentic economy, analogous to its role in internet payments

## Relationships

- [[entities/stripe]] — Creator of the Agentic Commerce Suite
- [[entities/openai]] — Co-developer of ACP; ChatGPT Instant Checkout partner
- [[entities/cloudflare]] — Stripe Projects partner; agent infrastructure provider
- [[concepts/ai-agent-engineering]] — Agent infrastructure that commerce plugs into
- [[entities/stripe-link-cli]] — Agent wallet CLI tool
- [[entities/microsoft-copilot]] — Copilot Checkout powered by Stripe

## Sources

- [Stripe: Introducing the Agentic Commerce Suite](https://stripe.com/blog/agentic-commerce-suite)
- [Stripe Docs: Agentic Commerce](https://docs.stripe.com/agentic-commerce)
- [Cloudflare: Agents can now create accounts, buy domains, deploy](https://blog.cloudflare.com/agents-stripe-projects/)
- [Ben's Bites: Building gets easier (Apr 30, 2026)](https://open.substack.com/pub/bensbites/p/building-gets-easier)
