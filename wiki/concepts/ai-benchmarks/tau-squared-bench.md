---
title: "τ²-bench"
type: concept
aliases:
  - tau-squared-bench
  - tau2-bench
created: 2026-05-08
updated: 2026-07-15
tags:
  - benchmark
  - evaluation
  - coordination
  - company
related:
  - "[[concepts/ai-benchmarks/tau-bench]]"
  - "[[concepts/tau-knowledge]]"
  - "[[concepts/tau-voice]]"
  - "[[concepts/evaluation/pass-k-metric]]"
sources:
  - raw/papers/2025-06-09_2506.07982_tau-squared-bench-dual-control.md
---

# τ²-bench

**τ²-bench** (tau-squared-bench) breaks the "single control" assumption of τ-bench, introducing a **"dual-control" environment where both the agent and the user can manipulate a shared environment using tools**. Published June 2025 by Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. **Presented as an Oral at ICML 2026** (top 0.7% of ~24,000 submissions).

> Paper: [arXiv:2506.07982](https://arxiv.org/abs/2506.07982) "τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment"

## Background: Limits of Single Control

Existing conversational agent benchmarks, including τ-bench, all assumed a **single-control environment**. The agent manipulates the world with tools while the user remains a passive information provider. But in real-world **technical support**, the situation is fundamentally different:

> The agent can check account info or reset backend flags, but the user must **restart their smartphone**, **change settings**, and **check on-screen status**. Task success depends on **both parties acting in coordination**.

τ²-bench is designed to evaluate this **shared agency**.

## Technical Foundation: Formulation as Dec-POMDP

τ²-bench's Telecom domain is modeled as a **Dec-POMDP (Decentralized Partially Observable Markov Decision Process)**.

| Element | Content |
|------|------|
| **Shared State** | Database (customer info, device state, network settings) |
| **Agent Observation** | Output of own tools, conversation with user |
| **User Observation** | Own device state (tool output), conversation with agent |
| **Agent Actions** | Backend operations (get_customer, toggle_network_feature, etc.) |
| **User Actions** | Device operations (toggle_airplane_mode, check_data_status, etc.) |

This formulation requires the agent to **explicitly model user behavior** under **incomplete information** and provide accurate guidance at the right timing.

## Telecom Domain

τ²-bench's Telecom domain is built from real-world technical support scenarios:

- **Data connection repair** — Troubleshooting slow/non-functional mobile data
- **MMS issue resolution** — Multimedia messaging configuration and troubleshooting
- **Network mode switching** — Switching between 4G/5G/Wi-Fi and configuration
- **Device setting verification** — Checking and changing airplane mode, data enablement, APN settings

In each task, the agent must follow Telecom policy documents, issue instructions to the user, wait for user feedback, and update strategy accordingly.

## Two Operating Modes

| Mode | Agent Role | User Role |
|--------|-------------------|---------------|
| **Solo** | Proxy-executes all operations (traditional) | Passive information provider |
| **Interactive** | Backend operations + user guidance | Executor of device operations |

### Complexity of Interactive Mode

In Interactive mode, simply "issuing correct instructions" is insufficient:

1. Must **model the user's cognitive load** — too many instructions at once causes confusion
2. Must **track the user's context** — what screen the user is looking at, what they understand
3. **Instruction accuracy and timing** are critical — wrong instructions or too early/late directly cause task failure

> From the paper: "Effective collaboration is non-trivial. Agents must not only issue precise, understandable instructions, but also model the user's context and cognitive load."

## Key Experimental Results

### Solo → Interactive Performance Drop

| Model | Solo Mode | Interactive Mode | Drop |
|--------|------------|-------------------|--------|
| GPT-4.1 | High | Max -25pt | Significant |
| o4-mini | High | Max -25pt | Significant |

This dramatic drop shows the steepness of the **difficulty gradient introduced by the dual-control environment**.

### Error Analysis: Reasoning vs Communication

One of τ²-bench's key contributions is the ability to **isolate error causes**:

| Error Type | Content | Example |
|-------------|------|-----|
| **Reasoning Error** | Incorrect problem-solving logic | Wrong troubleshooting procedure selection |
| **Communication/Coordination Error** | Incorrect/unclear user instructions | Ambiguous instructions, wrong order of instructions, misunderstanding user state |

This separation clarifies **what the bottleneck is**.

## Technical Innovations

### 1. Compositional Task Generator

A mechanism for **programmatically generating diverse verifiable tasks** from atomic components. This enables:

- Guaranteed **coverage** of the entire domain
- **Controlled gradual increase** in complexity
- Mathematically guaranteed task **verifiability**

### 2. Environment-Coupled User Simulator

Unlike conventional LM-based user simulators, τ²-bench's user simulator is **constrained by tools and observable state**:

- Users can only act based on **their own device state**
- Tool output constrains the user's **next utterance**
- This dramatically improves simulation **fidelity**

## Position in the τ-bench Family

| Dimension | τ-bench | **τ²-bench** | τ³-Bench |
|------|---------|-------------|----------|
| Released | June 2024 | **June 2025** | March 2026 |
| Control Model | Single | **Dual** | Dual + Voice |
| Main Domains | Airline, Retail | **Telecom** | Banking, Voice |
| Core Challenge | Dialogue + Tools | **Dialogue + Tools + Coordination** | Knowledge Retrieval + Voice Dialogue |
| Representative Numbers | GPT-4o <50% | **Solo→Interactive -25pt** | 25.5% / 26-38% |

## Practical Implications

1. **Coordination is intrinsically hard** — Up to 25-point drop from Solo to Interactive shows coordination itself demands high-level cognitive abilities
2. **Technical support automation is immature** — Even state-of-the-art models still struggle to solve problems while properly guiding users
3. **User modeling is critical** — Architectures that can accurately model user cognitive state are needed

## Related Pages

- [[concepts/ai-benchmarks/tau-bench]] — τ-bench ecosystem overview
- [[concepts/tau-knowledge]] — Evaluation with unstructured knowledge bases
- [[concepts/tau-voice]] — Full-duplex voice agent evaluation
- [[concepts/evaluation/pass-k-metric]] — Reliability evaluation metric
- [[entities/shunyu-yao]] — τ-bench original author
