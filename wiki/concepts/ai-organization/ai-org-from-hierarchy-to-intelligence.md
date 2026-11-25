---
title: "Hierarchy to Intelligence — Block's Organizational Model Transformation"
type: concept
aliases:
  - block-hierarchy-to-intelligence
  - jack-dorsey-org-model
created: 2026-04-13
updated: 2026-11-25
tags:
  - concept
  - company
  - ai-native
status: draft
depth_tracking:
  target: 10KB+
  current: ~10KB
sources: []
---

# Hierarchy to Intelligence — Block's Organizational Model Transformation

## Overview

Jack Dorsey's **Hierarchy to Intelligence** model, implemented at Block (formerly Square) in 2024. Abandoning traditional hierarchical decision-making in favor of **"context-driven autonomous execution + transparency-based monitoring."** AI is framed not merely as a productivity enhancement tool, but as **"a redesign of the coordination mechanism itself."**

> *"Most companies are focused on AI as a productivity enhancer. Few are focused on the potential of AI to change how we work together."*

## AI's True Potential

Block's claim: AI is not a "copilot" that makes existing workflows more efficient, but a **coordination mechanism that replaces middle management's information routing function.**

## The History of Hierarchy — Why Hierarchies Emerged

Organizational hierarchy was a product of technological constraints:

| Era | Innovation | Core Function |
|------|--------------|---------|
| **Roman Army** | Hierarchical organization (`contubernium` → `century` → `cohort` → `legion`) | Long-distance coordination with limited communication means |
| **Prussia (1806)** | General Staff | Pre-computed decisions, information routing, formalization of line vs staff |
| **US Railroads (1850s)** | First organizational chart (Daniel McCallum) | Commercialization of military hierarchy. Preventing large-scale collisions |
| **Taylorism** | Scientific management | Task specialization and measurement → functional pyramid |
| **Post-war** | Matrix organization & 7S framework | Balancing central standards with local agility |
| **Tech era** | Squads, holacracy, flat structures | Failed at scale. Reverted to hierarchy due to information routing limits |

> *"The structure (8 → 80 → 480 → 5,000) was an information routing protocol built around a simple human limitation: a leader can effectively manage somewhere between three and eight people."*

> *"The question was never whether you needed layers. The question was whether humans were the only option for what those layers do. They aren't anymore."*

## Company World Model: AI Replaces Information Routing

Two world models built by Block:

### 1. Company World Model (Internal)
- Remote-first, built on machine-readable artifacts (code, decisions, plans, progress)
- Continuously tracks what's being built, what's blocked, what's being resourced
- **Replaces the context-gathering function of management**

### 2. Customer World Model (External)
- Proprietary bi-directional transaction data (Cash App buyers + Square merchants)
- Creates financial reality per customer/merchant. Compounds with every operation
- > *"People lie on surveys. They ignore ads. They abandon carts. But when they spend, save, send, borrow, or repay, that's the truth."*

## 4 Building Blocks

Instead of traditional product teams building pre-determined roadmaps:

| Block | Description | Example |
|---------|------|-----|
| **1. Capabilities** | Atomic financial primitives (payments, lending, banking, payroll, BNPL). No UI. Hard to replicate due to regulatory moats and network effects | Payment processing engine, credit decision logic |
| **2. World Model** | Bi-directional operational and customer intelligence. Raw transaction data → evolves into causal and predictive models | Seasonal cash flow forecasting |
| **3. Intelligence Layer** | **Autonomously composes** Capabilities into contextual solutions. Failure signals become the future roadmap | Detect seasonal downturn → auto-suggest short-term loan + repayment schedule |
| **4. Interfaces** | Delivery surfaces (Square, Cash App, Afterpay, TIDAL, bitkey). Important for distribution, but **value creation lies in the Model & Intelligence layers** | User-facing apps, merchant dashboards |

> **Fundamental shift in roadmapping**: *"When the intelligence layer tries to compose a solution and can't because the capability doesn't exist, that failure signal is the future roadmap."* — From hypothesis-driven PM planning to **reality-driven backlog generation.**

## 3 Roles in an AI-Native Company

Flipping the hierarchy: Intelligence resides in the system. Humans operate at **the edge where intuition, ethics, and novel problem-solving are needed.**

### 1. Individual Contributors (ICs)
- Technical specialists who build and operate the system layer
- World model provides context. **No approval chains needed**
- Focus on implementing and improving Capabilities using deep expertise

### 2. Directly Responsible Individuals (DRIs)
- Temporarily own cross-cutting problems/outcomes (e.g., 90-day merchant churn prevention initiative)
- Have **authority to pull resources** from capability, model, and interface teams
- Dissolve after project completion. Next DRI owns another challenge

### 3. Player-Coaches
- Combine hands-on building with talent development
- Responsible for technical craft and growth
- **Alignment and strategy are automated by the system & DRIs**

## Comparison with Traditional Hierarchy Model

| Dimension | Traditional Hierarchy | Hierarchy to Intelligence |
|------|-----------|---------------------------|
| **Decision-making** | Top-down | Context-driven, autonomous execution |
| **Information flow** | Siloed, restricted | Transparent, open |
| **Management role** | Direct, monitor | Context design, guardrail setting |
| **AI positioning** | Tool, assistant | Autonomous execution agent |
| **Scalability** | Depends on headcount ratio | Depends on context quality |
| **Roadmap generation** | Hypothesis-driven PM | Reality-driven (failure signal) |

## AI and Corporate Identity

> *"If the answer is nothing, AI is just a cost optimization story... If the answer is deep, AI doesn't augment your company. It reveals what your company actually is."*

Block's moat: **The Economic Graph** — real-time bi-directional transaction data spanning millions of merchants and consumers. This understanding compounds with every operation of the system.

## Operational Reality

The transition is not easy. Expect a **"break then move"** phase. Success requires deep proprietary understanding of the domain. Without it, AI ends up as a short-term cost optimization story.

## The Amish Barn-Raising Model of Information Routing (Bowne-Anderson, Nov 2026)

Hugo Bowne-Anderson's O'Reilly Foo Camp lightning talk (expanded in Vanishing Gradients, 2026-11-25) offers an independent, concrete formulation of the same thesis this page develops — that hierarchy exists because **information flow is a bottleneck**. Source: raw/articles/hugobowne.substack.com--p-what-the-amish-can-teach-us-about--5afbb1b68f99df90.md. See [[entities/hugo-bowne-anderson]].

**The barn-raising metaphor.** In an Amish barn raising (Clinton, Wisconsin), a *master carpenter* holds a *shared plan for the barn*; each crew owns a different part of the frame. When someone leaves a part of the frame, a worker elsewhere **sees the gap, recognizes a job they know how to do, and moves over to fill it** — no request travels up a chain. In a company, the person with the skills to help may have no way of seeing that another team needs them: a team tells its manager where it's stuck and the request travels up until it reaches someone who knows where to find help.

**Why AI collapses the bottleneck.** With a strong frontier model and well-curated context about what teams are working on and who has the skills to help, getting the information to the right person is no longer the bottleneck. Bowne-Anderson's explicit generalization: *"hierarchical organizations are designed entirely around the fact that information flow is a bottleneck."* A background agent working from a shared company model could spot the gap and route it directly to someone who can act — letting the request *and* the decision skip the trip up and down the management chain (his framing maps onto Dorsey/Botha's shared-model-vs-local-context distinction on this page).

**Three coordination models he contrasts:** hierarchy (corporations, the military, the mafia — chain of command); flat team (direct coordination — his examples **Instagram** and **Cursor**); core-and-periphery (OSS maintainers + occasional contributors, a potluck).

**Org-chart agent placement (4 patterns):** (1) an agent in an existing department alongside a human; (2) hub-and-spoke where all reporting lines return to one person (Bowne-Anderson ran 6–8 agents this way, since reduced to one coordinator agent for "focus of attention"); (3) dotted lines for agent↔agent communication a reporting structure omits; (4) a **pull request as the trigger** for a background agent (e.g., an unprompted PR security review). Complements the "three org-chart scenarios" in [[concepts/future-of-the-firm-org-chart]].

## Related Concepts

- [[concepts/ai-organization/ai-org-context-as-moat]] — Proprietary Context and Fission-Fusion
- [[concepts/ai-organization/ai-org-solo-founder-and-super-ic]] — Solo Founder and Super IC
- [[concepts/ai-agent-development-workflow]] — Developer AI workflows
- [[concepts/harness-engineering]] — Agent control and structuring
- [[concepts/context-engineering|Context Engineering]] — Context engineering

## Sources

- [Block: From Hierarchy to Intelligence](https://block.xyz/inside/from-hierarchy-to-intelligence) — 2024
- [Jack Dorsey interviews on org design](https://block.xyz) — 2024-2025
