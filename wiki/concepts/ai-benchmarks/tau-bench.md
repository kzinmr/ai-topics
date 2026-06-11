---
title: "τ-bench"
type: concept
aliases:
  - tau-bench
  - TAU-bench
  - τ-bench ecosystem
created: 2026-04-25
updated: 2026-05-08
tags:
  - benchmark
  - evaluation
  - tool
  - infrastructure
  - company
related:
  - "[[entities/shunyu-yao]]"
  - "[[concepts/tau-squared-bench]]"
  - "[[concepts/tau-knowledge]]"
  - "[[concepts/tau-voice]]"
  - "[[concepts/evaluation/pass-k-metric]]"
---

# τ-bench

> τ-bench (Tool-Agent-User Interaction Benchmark) is a benchmark suite for AI agent evaluation developed by Sierra AI Research. Going beyond simple task success rate measurement, it comprehensively evaluates agents across three dimensions: **multi-turn dialogue**, **domain policy compliance**, and **reliability (pass^k)**. From its initial release in June 2024 to τ³-Bench in March 2026, it rapidly expanded and established itself as the de facto industry-standard evaluation infrastructure.

## Contents

1. [τ-bench Evaluation Philosophy](#τ-bench-evaluation-philosophy)
2. [Architecture](#architecture)
3. [Initial τ-bench (June 2024)](#initial-τ-bench-june-2024)
4. [Key Metrics](#key-metrics)
5. [Ecosystem Evolution](#ecosystem-evolution)
6. [Industry Impact](#industry-impact)
7. [Connection to Shunyu Yao's Evaluation Philosophy](#connection-to-shunyu-yaos-evaluation-philosophy)
8. [Related Pages](#related-pages)

## τ-bench Evaluation Philosophy

τ-bench's design philosophy is based on the insight that "evaluating agents deployable in the real world requires more than single-turn Q&A accuracy or tool calling precision." τ-bench emphasizes three evaluation axes:

### 1. Multi-Turn Dialogue (Tool-Agent-User Interaction)

Agents perform tasks through multi-turn dialogues with users simulated by LMs. Users generate diverse utterances based on user instructions, and agents must respond appropriately and perform tool operations each time. Dialogue management capabilities undetectable in simple Q&A (context maintenance, handling paraphrased questions, clarifying ambiguous requests, etc.) are evaluated.

### 2. Domain Policy Compliance (Policy Following)

Each domain comes with policy documents simulating real-world business rules. Airline ticket change fee regulations, return-eligible periods, exception provisions for specific product categories, etc. Agents must complete tasks without violating policies, incorporating the realistic dilemma of "maximizing customer satisfaction while adhering to policies."

### 3. Reliability Evaluation — pass^k Metric

One of τ-bench's greatest innovations. The same task is executed over k independent trials, and the **probability of succeeding in all trials** is measured as pass^k. This visualizes "inconsistency" hidden by single pass@1 measurements and quantitatively evaluates operational reliability.

> "Even state-of-the-art function calling agents (such as GPT-4o) achieve task success rates below 50% and lack consistency significantly (pass^8 < 25% on retail)"
> — τ-bench paper Abstract

## Architecture

τ-bench's evaluation framework consists of four modules:

| Module | Content | Role |
|-----------|------|------|
| **DB (Database)** | Domain persistent state (reservation info, inventory, customer data, etc.) | Automatic evaluation via comparison with ground-truth task states |
| **API** | Domain-specific tools (search, reservation changes, return processing, etc.) | Agent's operational targets |
| **Policy Document** | Natural language documents describing business rules | Definition of constraints agents must follow |
| **User Instruction** | Instructions to LM-simulated users (goals, constraints, personality) | Generation of diverse user behaviors |

### Evaluation Method: DB State Comparison

Automatic and faithful evaluation is achieved by comparing the database state at task completion with predefined ground-truth states. This enables scalable evaluation without human evaluators while maintaining result reliability. This design has been consistently inherited by subsequent τ²-bench and τ³-Bench.

## Initial τ-bench (June 2024)

### Basic Information

- **Paper**: "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
- **Authors**: Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan
- **Published**: arXiv June 17, 2024 / Accepted at ICLR 2025
- **Affiliation**: Sierra AI Research (at the time)

### Initial Domains

| Domain | Task Content | Characteristics |
|---------|-----------|------|
| **τ-airline** | Flight reservation changes and cancellations | Complex reservation API + airline policies (change fees, upgrade rules, cancellation provisions) |
| **τ-retail** | Online shopping returns and exchanges | Inventory management API + return policies (return deadlines, product category rules, refund method options) |

### Design Features

1. **LM-Simulated Users**: Diverse user utterances generated based on instructions. User behavior variations across the same task prevent overfitting
2. **Database State Comparison Evaluation**: Efficient and faithful automatic evaluation by comparing DB state at conversation end with ground truth
3. **pass^k Metric**: Measuring probability of success across k independent trials to evaluate agent reliability
4. **Modular Framework**: Separating DB, API, policy documents, and user instructions for easy new domain addition

## Key Metrics

### Initial τ-bench Scores (2024)

| Model | τ-airline pass@1 | τ-retail pass@1 | τ-retail pass^8 |
|--------|-----------------|-----------------|-----------------|
| GPT-4o | < 50% | < 50% | < 25% |
| GPT-4 Turbo | Data undisclosed | Data undisclosed | Data undisclosed |
| Claude 3.5 Sonnet | Data undisclosed | Data undisclosed | Data undisclosed |

> **Core finding**: Even state-of-the-art function calling agents achieve single-task success rates below 50%, with reliability (consistency across multiple trials) even lower. Agent inconsistency emerged as the greatest challenge.

### τ²-bench Scores (June 2025)

| Mode | Characteristics | Performance Change |
|--------|------|---------|
| **Solo mode** | Agent performs all operations alone (traditional) | Baseline |
| **Interactive mode** | Agent guides user while coordinating operations | Solo → Interactive transition shows **max -25pt success rate drop** |

- Even cutting-edge LLMs like GPT-4.1 / o4-mini have limits in managing collaborative tasks
- Error analysis separation enables distinguishing reasoning errors from communication/coordination errors

### τ³-Bench Scores (March 2026)

#### τ-Knowledge (τ-Banking, 698 documents)

| Condition | pass^1 | Implication |
|------|--------|------|
| GPT-5.2 with high reasoning (normal) | **~25.5%** | Combined search+reasoning difficulty is extremely high |
| GPT-5.2 with high reasoning (necessary documents directly provided) | **~40%** | Beyond search, understanding and reasoning itself is also a bottleneck |

- Performance differences by search method:
  - **Terminal-type exploration**: High precision but slow
  - **Embedding search**: Fast but precision drops

#### τ-Voice (278 tasks, full-duplex audio)

| Agent Type / Condition | Success Rate | Notes |
|------------------------|--------|------|
| GPT-5 reasoning (text) | **85%** | Upper bound performance in text |
| Voice agent (clean conditions) | **31–51%** | Ideal acoustic environment |
| Voice agent (realistic conditions: noise + diverse accents) | **26–38%** | Production-assumed conditions |

- **Only 30–45% of text capability is maintained**
- **79–90% of failures are due to agent behavior** (not ASR errors)
- Full-duplex (simultaneous bidirectional) interruption handling, back-channeling, and turn-taking are primary challenges

## Ecosystem Evolution

τ-bench rapidly expanded across three generations from 2024 to 2026:

| Generation | Name | Release Date | Domains | Control Model | New Evaluation Axes | Paper | Conference |
|------|------|---------|---------|-----------|-------------|------|------|
| **1st** | **τ-bench** | June 2024 | τ-airline, τ-retail | Single control (agent only operates tools) | Multi-turn dialogue, policy compliance, pass^k | [2406.12045](https://arxiv.org/abs/2406.12045) | ICLR 2025 |
| **2nd** | **τ²-bench** | June 2025 | Telecom | Dual control (agent + user operate tools) | Collaborative operation, Dec-POMDP model, communication quality | [2506.07982](https://arxiv.org/abs/2506.07982) | Under review |
| **3rd** | **τ³-Bench** | March 2026 | τ-Knowledge (τ-Banking: 698 docs), τ-Voice (278 tasks) | Knowledge search + tools / Full-duplex audio | Unstructured knowledge navigation, voice dialogue quality | [2603.04370](https://arxiv.org/abs/2603.04370) / [2603.13686](https://arxiv.org/abs/2603.13686) | Preprint |

### 1st Generation: τ-bench — Establishing the Foundation

Evaluation infrastructure with single control (agent only operates tools). Established the basic paradigm of multi-turn dialogue, policy compliance, and pass^k reliability evaluation across two domains (airline reservations and online retail). Accepted at ICLR 2025, gaining academic recognition.

### 2nd Generation: τ²-bench — Extension to Dual Control

Introduced "dual control" environments where both agents and users operate tools on a shared environment. Modeled as Dec-POMDP (Decentralized Partially Observable Markov Decision Process) in the Telecom domain. Added these innovative elements:

- **Compositional task generator**: Automatically generates diverse verifiable tasks from atomic components
- **Environment-coupled user simulator**: Higher-fidelity simulation constrained by tools and observable state
- **Solo mode vs Interactive mode comparison**: Quantifying collaboration overhead
- **Error analysis separation**: Distinguishing reasoning failures from communication failures

A maximum 25-point success rate drop was observed transitioning from Solo to Interactive, revealing agent capability limits in collaborative multi-agent environments.

### 3rd Generation: τ³-Bench — Two-Front Deployment: Knowledge and Voice

τ³-Bench simultaneously introduced two new domains, dramatically expanding τ-bench ecosystem's evaluation scope:

#### τ-Knowledge (τ-Banking)

- **698 documents, 21 product categories, ~195K tokens** of unstructured knowledge base
- Structured-to-unstructured generation pipeline ensures knowledge consistency and task verifiability
- Tools (account updates, etc.) are only referenced within documents — agents must discover them independently
- Supported search methods: Dense retrieval, Sparse retrieval, Long-context, Filesystem-based exploration, Hybrid

#### τ-Voice

- **278 tasks** of full-duplex voice dialogue evaluation
- Direct comparison with text agents quantifies pure voice modality impact
- User simulator reproduces diverse accents, realistic acoustic environments, and rich turn-taking dynamics
- Wall-clock-decoupled design enables using strongest LLMs as simulators → proves agents themselves (not ASR) are the bottleneck

## Industry Impact

The τ-bench ecosystem has had widespread influence on industrial AI agent evaluation beyond academia:

### 1. Catalyst for Derived Benchmarks

- **MedAgentBench**: Applied τ-bench architecture to the medical domain. Evaluates patient dialogue, EHR operations, and clinical guideline compliance
- **LAM (Large Action Model) Simulator**: Adapted τ-bench's LM-simulated user approach for large action model evaluation

### 2. Standard Adoption at AI Labs

Major AI labs (OpenAI, Anthropic, Google DeepMind, Meta, etc.) have adopted τ-bench and τ²-bench as standard tools for internal agent evaluation. In particular, the pass^k metric has become common language in research reports and product releases as an indicator quantifying agent "reliability."

### 3. Establishment as De Facto Standard

The τ-bench series has established de facto standard status in agent evaluation on these points:

- **Standard format for multi-turn dialogue evaluation**: Led the industry shift from single-turn to multi-turn evaluation
- **pass^k proliferation**: Paradigm shift from "success rate" to "reliability" in evaluation
- **Modular architecture as template**: DB+API+Policy+User separation design became template for subsequent benchmarks
- **Voice evaluation pioneer**: τ-Voice enabled direct comparison between text and voice agents for the first time

### 4. Sierra AI Research's Evaluation Foundation

τ-bench is embedded in Sierra AI's own product development cycle, used for performance assurance and regression testing of actual customer service AI agents. A rare instance of research and practice being directly connected.

## Connection to Shunyu Yao's Evaluation Philosophy

τ-bench is the culmination of Shunyu Yao's research philosophy, deeply resonating with the evaluation philosophy expressed especially in his 2025 blog post "**The Second Half**."

### Core Thesis of "The Second Half"

> "The second half of AI shifts focus from solving problems to defining problems. In this new era, **evaluation becomes more important than training.**"
> — Shunyu Yao, "The Second Half" (2025)

Yao argues that among RL's three elements (algorithm, environment, prior knowledge), "environment" is most important. τ-bench embodies this philosophy, pursuing essential understanding of agent capabilities not through algorithm improvement but through **environment (evaluation infrastructure) design**.

### Yao's Evaluation Philosophy Embodied in τ-bench

| Yao's Principle | τ-bench Manifestation |
|-----------|-------------------|
| "Environment is RL's most important element" | Modular DB+API+Policy+User structure precisely models realistic environments |
| "Reasoning is a strange action that doesn't affect the environment" | Doesn't directly evaluate agent internal reasoning; evaluates via external indicators of DB state changes |
| "Evaluation > Training" | Design maximizing evaluation resolution: pass^k, DB state comparison, Dec-POMDP models |
| "Problem definition is more important than problem solving" | Policy documents and task designs for each domain define the agent's true challenges |
| "RL has finally generalized" | τ-bench ecosystem expansion (single control→dual control→knowledge+voice) demonstrates RL evaluation generalizability |

### Continuity from SWE-bench to τ-bench

Viewing Yao's research trajectory holistically reveals clear consistency in the expansion from SWE-bench (real-world GitHub issue resolution evaluation) to τ-bench (real-world dialogue-based tool operation evaluation):

1. **SWE-bench**: Expanded evaluation from "code generation" to "real-world software problem solving"
2. **τ-bench**: Expanded evaluation from "tool calling" to "policy compliance, dialogue management, reliability"

Common to both is the methodology of "visualizing AI's true capability limits by increasing benchmark resolution." This methodology has been consistently pursued since Yao's Princeton days, and the τ-bench ecosystem can be considered one of its culmination points.

## Related Pages

- [[entities/shunyu-yao]] — τ-bench's creator. All achievements including ReAct, SWE-bench, "The Second Half"
- [[concepts/tau-squared-bench]] — τ²-bench: Dual control evaluation details
- [[concepts/tau-knowledge]] — τ-Knowledge: Unstructured knowledge navigation evaluation details
- [[concepts/tau-voice]] — τ-Voice: Full-duplex voice agent evaluation details
- [[concepts/evaluation/pass-k-metric]] — pass^k metric detailed explanation
- [[concepts/swe-bench]] — Yao's other representative benchmark

---

*Last updated: 2026-05-08 / τ-bench v1–v3 ecosystem comprehensive*
