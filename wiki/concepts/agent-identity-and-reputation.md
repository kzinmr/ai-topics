---
title: "Agent Identity and Reputation"
created: 2026-09-19
updated: 2026-09-19
type: concept
tags: [agent-economics, ai-agents, trust, verification, zk-proofs, reputation, economics, open-source]
sources:
  - raw/articles/arxiv-2608.21942-tessindex.md
  - raw/articles/arxiv-2608.23867-markets-not-planners.md
confidence: medium
related: [decentralized-agent-orchestration, economic-agent-benchmarks, agentic-commerce]
aliases: ["TessIndex", "verifiable agent identity", "proof-of-human", "agent KYC"]
---

# Agent Identity and Reputation

Once agents transact with each other at scale (see [[concepts/decentralized-agent-orchestration]], [[concepts/agentic-commerce]]), the binding constraint stops being capability and becomes **trust**: who is this agent, what has it actually done, and can either claim be verified without revealing the underlying data? A 2026 literature treats identity/reputation as the missing infrastructure layer of the agent economy.

## TessIndex

Goenka, Pathak & Asthana, ["TessIndex: Capability Verified Identity System for the Agent Economy"](https://arxiv.org/abs/2608.21942) (arXiv:2608.21942, Aug 2026) — a *systems* paper — builds an identity system where an agent's capabilities are **verified credentials, not self-declared profiles**:

- **Capability verification via zero-knowledge proofs**: an agent proves it passed a benchmark or holds a credential without disclosing the evidence (e.g., client data a financial agent doesn't want public).
- **On-chain identity + reputation registry**: persistent identity across deployments; reputation accrues from verified task outcomes and can't be silently reset.
- **Proof-of-human** at the principal layer: the human owner of an agent is verified, closing the sybil loophole where one operator spins up a thousand "independent" agents.
- **Revocation and privacy preservation**: credentials are revocable, and verification never exposes the underlying evidence.

The paper validates on open-source LLM benchmarks that verification is accurate and **hard to game** — i.e., agents cannot inflate their capability claims — and frames the system as infrastructure for agent economies: agents transact and build reputation "without fully exposing their capabilities."

## Why identity is load-bearing for markets

The mechanism-design literature makes the dependency explicit: AgentLance's ([arXiv:2608.23867](https://arxiv.org/abs/2608.23867)) market-based orchestration allocates work using **public reputation records**, and its central warning is manipulation — one inserted preference nearly doubles a favored agent's allocation. That attack surface exists precisely because identity is cheap and reputation is unverified. TessIndex-style verifiable identity is the natural countermeasure layer: sybil resistance makes reputation meaningful, and verified capability records make bidding markets robust.

Convergent commercial signals: payment networks (Visa/Mastercard) and AP2-style protocols are building agent enrollment/KYC rails; proof-of-human at the principal layer is the common requirement. The wiki treats "agent economy needs identity/reputation infrastructure" as high-consensus; the *design* of that infrastructure (ZK vs. attestation chains vs. platform KYC) is contested and single-source so far (`confidence: medium`).

## Open questions

- ZK-verified capability claims still trust the benchmark itself — **who audits the auditors** of verification tasks is unsolved (evaluation gaming applies one level up).
- Revocation authority: a centralized revocation list reintroduces exactly the planner power these systems decentralize away from.
- Reputation portability vs. privacy: portable reputation implies linkable identities; the tension is unresolved.
- Interaction with regulation: agent KYC may land first as jurisdiction-specific compliance (EU AI Act, state law) rather than as open infrastructure.

## Related

- [[concepts/decentralized-agent-orchestration]] — markets require the reputation layer this page describes
- [[concepts/agentic-commerce]] — commercial deployment driving demand for agent enrollment rails
- [[concepts/economic-agent-benchmarks]] — the "capability evidence" that credentials attest to
