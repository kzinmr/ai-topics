---
title: "Autonomous Agent Marketplace Stack (Three Planes, Ten Layers)"
type: concept
created: 2026-05-20
updated: 2026-05-20
tags:
  - concept
  - ai-agents
  - infrastructure
  - platform
  - protocol
  - economics
  - governance
  - security
  - architecture
aliases:
  - agent-marketplace-stack
  - agentic-capital-markets
  - three-planes-ten-layers
related:
  - [[concepts/agent-governance]]
  - [[concepts/agent-identity-verification]]
  - [[concepts/harness-engineering]]
sources:
  - raw/articles/2026-05-19_autonomous-agent-technical-stack.md
  - https://x.com/i/article/2056841484502962176
---

# Autonomous Agent Marketplace Stack (Three Planes, Ten Layers)

A comprehensive framework decomposing the infrastructure required for autonomous AI agents to function as economic actors — transacting, finding counterparties, making commitments, moving money, building track records, and staying within authorized bounds. The framework posits that **"markets do not run on intelligence alone — they run on identity, trust, pricing, contracts, settlement, enforcement, and policy."**

## Summary

For autonomous agents to become a true asset class, they need more than output generation. They need marketplace infrastructure across three planes and ten layers:

- **Trust Plane** (Layers 1–3): Establishes who the agent is and what it has done
- **Market Plane** (Layers 4–7): How value clears between agents
- **Control Plane** (Layers 8–10): What the agent is allowed to do, regulatory compliance, and runtime coordination

Each layer maps to a distinct buyer, failure mode, and emerging vendor category. Pieces exist (ERC-8004, x402, MCP, A2A, governance control planes) but they do not yet compose into a coherent system.

## The Three Planes

### Trust Plane (Layers 1–3)

Establishes who an agent is, how it is found, and what it has done. Without these, no market can clear.

#### Layer 1: Identity (Know-Your-Agent)

**Current state**: Identifiers without identity. An agent can claim to be `gpt-4.1-claims-processor-v3` but there is no way to verify weights, system prompts, or tool access.

**What's needed**:
- **Model lineage attestations**: Cryptographic proof tying a deployed agent to a base model version, fine-tuning run, and system prompt hash
- **Tool permission manifests**: Signed declarations of which APIs, databases, and accounts the agent can access
- **Persistent agent DIDs**: Decentralized identifiers the agent owns across deployments

**ERC-8004** is the most concrete standardization attempt: an ERC-721 NFT-based Identity Registry where each agent owns a token whose URI resolves to a JSON registration file naming its A2A endpoint, MCP endpoint, ENS handle, wallet addresses, and supported trust models. Authors include MetaMask, Ethereum Foundation, Google, and Coinbase. As of early 2026, AgentProof reports 128,000+ agents registered across 24 chains.

**Key gap**: Inference providers don't sign attestations directly into the registry — operators self-attest, which is the soft underbelly.

#### Layer 2: Discovery and Capability Registry

**Current state**: Flat lists on webpages with no machine-readable capability surface.

**What's needed**:
- **Structured capability declarations**: Typed interfaces (inputs, outputs, latency SLAs, jurisdictions, regulated-data handling)
- **Semantic search**: Vector search across capability embeddings, filterable by cost, latency, compliance posture
- **Live availability and pricing**: Registry must reflect state in seconds, not days

ERC-8004's registration file is the closest thing to a structured capability declaration in production. The marketplace — ranking, filtering, and pricing against those declarations — sits on top and does not yet exist.

#### Layer 3: Reputation

**Current state**: No cross-marketplace portable reputation. Each marketplace guards reputation as its moat.

**What's needed**:
- **Outcome track records**: Cryptographically attested job histories with accuracy, latency, dispute rate, signed by buyers
- **Cross-marketplace portability**: Reputation from one marketplace must carry to another
- **Sybil resistance**: Detect operators spinning up thousands of fresh agents to flood auctions

ERC-8004's Reputation Registry provides a standard interface for feedback signals. The scoring layer on top — "Moody's for Machines" — has not been built and is one of the most valuable openings in the stack.

### Market Plane (Layers 4–7)

How value moves between agents: price discovery, obligations, money movement, dispute resolution.

#### Layer 4: Quoting and Price Discovery

**Current state**: Does not exist anywhere. The most economically interesting and most undervalued layer.

**What's needed**:
- **Real-time RFQ**: Buyer agent broadcasts job spec; provider agents respond with quotes in under 100ms
- **Outcome contracts**: "Generate 50 qualified leads for $X, pay only on conversion verified by a third-party agent"
- **Auction mechanics**: Combinatorial auctions for parallel jobs, Dutch auctions for time-sensitive ones

The closest analog is programmatic ad exchanges, which built three of the largest companies of the last twenty years. The agent-work version has a TAM measured in low-trillions of dollars.

#### Layer 5: Contracting

**Current state**: Usually nothing — a prompt, an API call, a payment authorization, and assumptions.

**What's needed**:
- **Machine-readable MSAs**: Standardized contract format capturing scope, deliverable, deadline, payment terms, data rights, liability, remedies — signed by both parties' DIDs
- **Encoded SLAs**: "99% uptime, p95 latency under 500ms, accuracy above 0.92 measured by these three eval prompts"
- **Proof of authority**: Bridge between governance (Layer 8) and contracting — proving the agent had authority to bind its principal
- **State transitions**: Quoted → accepted → in progress → delivered → verified → disputed → terminated

A real contracting layer would be a hybrid object: part legal agreement, part workflow schema, part policy bundle.

#### Layer 6: Settlement

**Current state**: Most public activity, most confusion. Multiple rails competing.

| Rail | Approach | Characteristics |
|------|----------|----------------|
| **Stablecoin rails** | Coinbase x402, Stripe Bridge, Circle CCTP | Sub-second, programmable, no chargebacks; legal status of agents holding stablecoins unsettled |
| **Agent-issued cards** | Visa Intelligent Commerce, Mastercard Agent Pay, Stripe Issuing | Bank rails, jurisdictionally clean, have chargebacks |
| **Direct-debit/ACH** | Mercury, Brex, Column Bank | Cheap, slow, irreversible; fine for B2B weekly cycles |

**The right architecture**: Stablecoins for high-frequency agent-to-agent, virtual cards for agent-to-merchant, ACH for periodic sweeps. Whoever builds the abstraction layer over all three wins.

#### Layer 7: Dispute Resolution

**Current state**: Human operator on the slow side emails the other operator.

**What's needed**:
- **Escrow as default**: Payment held until SLA conditions met
- **Automated remediation**: Quality below threshold → automatic refund; late delivery → automatic penalty
- **Validators and arbitration agents**: Third-party validators for ambiguous disputes. ERC-8004's Validation Registry provides standardized hooks supporting stake-secured re-execution, zkML proofs, TEE attestations, or human-in-the-loop judges.

### Control Plane (Layers 8–10)

Decides what the agent is allowed to do, what regulators require, and how work actually runs.

#### Layer 8: Governance and Authority

**Current state**: Shifted from a prompting problem to a runtime authorization problem. Vendors uniformly market as "control planes for AI agents."

**Key players**: Cordum, Aegis AI, Assury Enforce, Galileo Agent Control, Microsoft Agent Governance Toolkit, PolicyLayer.

**What's needed**:
- **Policy engines**: Inline enforcement before execution, not after logging
- **Spending limits and delegated authority**: Safe allowance modules, Zodiac role-based modules, hierarchical multisig, ERC-4337 session keys, MPC wallets
- **Approval chains**: Below $X autonomous; $X–$Y requires one human approval; above $Y requires two approvals + 24-hour timelock
- **Proof of authority**: Machine-readable, signed declaration of what the agent can bind its principal to

Gartner predicts >40% of agentic AI projects will be cancelled by end of 2027 due to inability to govern them.

#### Layer 9: Compliance

**Current state**: Splitting out from governance as its own vendor category. EU AI Act Article 99 penalties (€35M or 7% of global turnover) come into effect August 2, 2026.

**Key distinction from governance**: Governance answers "what is the organization willing to let the agent do?" Compliance answers "what is the organization required to prove to a regulator?"

**Vendors**: ComplyEdge (open-source EU AI Act enforcement layer), Lucairn, Agent Module, AgentWorks. The `aicompliancevendors.com` directory exists as a signal of category maturity.

**Sector-specific overlays**: HIPAA (healthcare), SR 11-7 / OCC 2011-12 (financial), EU AI Act (European), anti-discrimination law (employment).

#### Layer 10: Orchestration and Runtime

**Runtime** (where agents execute): Modal, Anthropic Claude compute environments, OpenAI Agents SDK, E2B, Daytona.

**Memory** (what persists): Mem0, Letta (née MemGPT), Zep.

**Observability** (what gets traced): Langfuse, Helicone, Arize, Braintrust, LangSmith. Serves as the audit trail backing reputation (L3), compliance (L9), and dispute resolution (L7).

**Orchestration** (how agents coordinate): LangGraph, CrewAI, AutoGen, OpenAI Swarm, Google ADK, Anthropic Skills, Microsoft Semantic Kernel. ~86% of enterprise copilot spending in 2026 (~$7.2B) goes to agent-based systems; 59% of organizations run 3+ LLMs needing coordination.

## Strategic Implications

1. **The platform play requires three layers**: Identity + Settlement + Governance. Whoever owns these three owns the marketplace.
2. **Crypto-native and enterprise-native stacks converge at the trust plane, diverge at the control plane**: ERC-8004 is the convergence story (Coinbase + Google co-authoring). Cordum/Galileo/Microsoft vs Safe modules/ERC-4337 is the divergence story.
3. **Layer 4 (Quoting) is the most undervalued**: Real-time machine-to-machine price discovery has a multi-trillion-dollar TAM and almost nobody is building it as a primary product.
4. **The winning company will not look like a model lab**: It will look like a market operator — part exchange, part payments network, part identity provider, part trust infrastructure, part governance platform. Less like OpenAI, more like Visa + Moody's + Stripe + Nasdaq + ServiceNow fused.

## Graph Structure Query

```
[autonomous-agent-marketplace-stack] ──relates-to──→ [concept: agent-governance]
[autonomous-agent-marketplace-stack] ──relates-to──→ [concept: agent-identity-verification]
[autonomous-agent-marketplace-stack] ──relates-to──→ [concept: harness-engineering]
[autonomous-agent-marketplace-stack] ──embodies──→ [concept: erc-8004-trustless-agents]
[autonomous-agent-marketplace-stack] ──contrasts──→ [concept: ai-agent-tech-stack] (production stack vs marketplace stack)
```

## Related Concepts

- [[concepts/agent-governance]] — Governance and authority layer for autonomous agents
- [[concepts/agent-identity-verification]] — Agent identity infrastructure
- [[concepts/harness-engineering]] — The umbrella philosophy: Agent = Model + Harness
- ERC-8004 (Trustless Agents) — Ethereum standard for agent identity, reputation, and validation registries
- x402 Protocol — HTTP 402-based agent payment protocol (Coinbase + Cloudflare)

## Sources

- [The Technical Stack for Autonomous Agents](https://x.com/i/article/2056841484502962176) — X Article, May 19, 2026
- [[raw/articles/2026-05-19_autonomous-agent-technical-stack.md]]
