---
title: "Personal Agent Protocol (Poppy)"
created: 2026-11-15
updated: 2026-11-15
type: concept
tags:
  - concept
  - agent-protocol
  - interoperability
  - agent-identity
  - personal-ai
  - agent-communication
  - agentic-commerce
  - mcp
  - api-monetization
  - company
  - product
  - ai-agents
sources:
  - raw/articles/sierra.ai--blog-releasing-poppy--1f27a1fb.md
  - raw/articles/sierra.ai--blog-poppy--ba1ffb49.md
  - raw/articles/sierra.ai--blog-caller-id-in-the-age-of-agents--3933abd6.md
confidence: high
---

# Personal Agent Protocol (Poppy)

**One-line**: Sierra's open standard for how a *consumer's* agent introduces itself to a *company*, published v1.0 on 2026-11-14 with Shopify live on all merchants and Meta's Muse checking for a Poppy file on every site it visits.

## Position in the protocol stack

Poppy is Sierra's answer to a question the agent-interoperability stack had left open: MCP standardizes **agent ↔ tools**, [[concepts/a2a-agent-protocol]] standardizes **agent ↔ agent**, and Universal Commerce Protocol (UCP) standardizes the **transaction**. None of them answers the step *before* all three — an agent arrives at a store or a bank's API, and the company has no standard way to establish who the agent is acting for and what it is permitted to do.

Poppy fills that gap. It is deliberately built out of existing standards rather than on a new wire format: MCP for capability discovery, OpenAPI for the surface description, UCP for the commerce flow, and OAuth for consent. That composition choice is the reason a company can adopt it incrementally — v1.0 explicitly supports staged adoption, "starting with the basics and adding capabilities over time," which is the main change the five-week draft-to-v1.0 cycle produced alongside refined reuse of those underlying standards.

## v1.0 contents (2026-11-14)

- **Protocol surface**: a Poppy file published by the company describes what personal agents may access, authenticated through OAuth, with customer-managed grants that can be revoked over time. The customer, not the agent vendor, controls the scope.
- **Adoption at v1.0**: Shopify enabled Poppy for **every merchant** on its platform — 175+ countries, and because every Shopify store already supports UCP by default, stores publish a Poppy file automatically with no merchant-side implementation work. Meta's **Muse** AI agent looks for Poppy **first** on every site it visits, which converts the standard from opt-in courtesy into de facto distribution pressure.
- **Design-partner expansion**: 60 new companies joined at v1.0, taking the total past 100 — Affirm, Aflac, Agoda, Aviva, Banco Sabadell, Braze, Browserbase, Checkout.com, Cisco, Creditas, Delta Air Lines, Five9, Freshworks, Fullstory, Gen Digital, Global Payments, GoFundMe, GoodRx, Guardian, HelloFresh, Hyatt, Infoblox, Intuit, Lemonade, Liberty Global, Manus, Mercury, Navy Federal Credit Union, Ora, Persona, Ping Identity, Remitly, Salesforce (Fin, Commerce Cloud, Agentforce), SoFi, Symphony by Wix, Travelers, Turkish Airlines, Twilio, Wayfair, Wix, WorkOS, Zoom, and others. First to go live: Mercury, Synchrony, Turkish Airlines.
- **Commerce extension (co-authored with Shopify)**: links Poppy to UCP along a clean seam — UCP handles finding products, filling a cart, and checking out; Poppy handles the part where an agent shows up, says who it is, and finds out what it is allowed to do. The extension lets an agent shop as a guest or sign in under the customer's account, and requires the agent to ask the customer before certain actions. It also wires into **UCP Ask** so a shopper's agent can talk directly to the store's agent.

## Live deployments

- **Mercury** (banking): a personal agent can check balances, review transactions, categorize spending, and maintain budgets and receipts; initiating a payment or transfer is allowed but must pass the account's existing approval policy before anything leaves. The notable design property is that Poppy does not create a parallel authorization path — the agent inherits the account's policy.
- **Synchrony** (financing/rewards): exploratory work on agent-led shopping that weighs affordability and relevant Synchrony offers across a 500,000+ merchant network.
- **Turkish Airlines**: fares, flight status, stopovers, and booking retrieval by reference number plus surname; Miles&Smiles members can have an agent find business-class upgrades, which the customer approves before paying. Completion of purchase without leaving the conversation is in progress.

## Assessment

Two things make Poppy more than another vendor protocol announcement. First, the **Shopify + Muse pairing** supplies both sides of a two-sided coordination problem in one release — the largest commerce surface auto-publishing the file, and a major consumer agent auto-looking for it. That is the specific condition under which interoperability standards stop being aspirational. Second, Poppy's OAuth-and-staged-adoption design concedes the thing most agent-protocol announcements avoid: companies want to *govern* personal-agent traffic, not merely receive it. Sierra frames it explicitly as fine-grained control over how personal agents touch a brand, positioned against its own "personal agents — opportunity or threat" framing; see [[entities/sierra]].

Caveats: Sierra authors and donates the standard, so the partner list is Sierra's count and the live deployments are Sierra-selected. The comparison with Decagon's **PACT** (Personal Agent Consent & Trust Protocol, announced 2026-10-07) is not yet settled — both address consent for personal agents, and it is too early to say whether the space consolidates or forks.

## Related

- [[entities/sierra]] — Author of the standard; also the τ-bench and Horizon lineage
- [[concepts/a2a-agent-protocol]] — Agent-to-agent protocol; Poppy sits before it in the flow
- [[concepts/agent-communication-standards]] — ACP → A2A convergence under the Linux Foundation
- [[concepts/mcp]] — Capability-discovery substrate Poppy reuses
- [[concepts/agentic-commerce]] — The transaction layer Poppy hands off to via UCP
- [[concepts/x402]] — Machine-to-machine payment rail in the same problem space
- [[concepts/agent-identity-and-reputation]] — The "caller ID for agents" problem Poppy operationalizes

## Sources

- Sierra, "Releasing Personal Agent Protocol 1.0" (2026-11-14) — `raw/articles/sierra.ai--blog-releasing-poppy--1f27a1fb.md`
- Sierra, initial Poppy announcement with design partners — `raw/articles/sierra.ai--blog-poppy--ba1ffb49.md`
- Sierra, "Caller ID in the age of agents" — `raw/articles/sierra.ai--blog-caller-id-in-the-age-of-agents--3933abd6.md`
