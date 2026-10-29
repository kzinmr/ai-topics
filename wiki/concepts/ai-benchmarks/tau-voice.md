---
title: "τ-Voice"
type: concept
aliases:
  - tau-voice
created: 2026-05-08
updated: 2026-10-23
tags:
  - benchmark
  - ai-agents
  - evaluation
  - company
related:
  - "[[concepts/ai-benchmarks/tau-bench]]"
  - "[[concepts/ai-benchmarks/tau-squared-bench]]"
  - "[[concepts/ai-benchmarks/tau-knowledge]]"
  - "[[concepts/evaluation/pass-k-metric]]"
sources:
  - raw/papers/2026-03-14_2603.13686_tau-voice-full-duplex-voice-agents.md
  - raw/articles/sierra.ai--blog-tau-entity-can-voice-agents-get-the-details-right--bee3927c.md
---

# τ-Voice

**τ-Voice** extends τ²-bench to evaluate **full-duplex (simultaneous bidirectional) voice agents**. With 278 tasks, it simultaneously evaluates **task completion ability and conversation management ability**. Published March 2026 by Soham Ray, Keshav Dhandhania, Victor Barres, and Karthik Narasimhan.

> Paper: [arXiv:2603.13686](https://arxiv.org/abs/2603.13686) "τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains"

## Background: The Voice Frontier

The next frontier of conversational AI is **full-duplex voice interaction**. The system must simultaneously listen, simultaneously speak, gracefully handle interruptions, and make real-time turn-taking decisions. This is a fundamentally different paradigm from turn-based interaction (speak → wait → speak).

A new generation of voice-native LLMs (GPT-4o voice, Gemini Live, etc.) is making this possible. Customer service is a key application domain, where voice remains preferred for complex issues.

**However, being able to maintain a conversation and being able to simultaneously handle returns, order changes, and billing disputes with reliability comparable to text agents are entirely different problems.**

## Why End-to-End Evaluation is Needed

Voice agents must simultaneously demonstrate **two capabilities**:

| Capability | Content | Existing Evaluation |
|------|------|-----------|
| **Task Completion** | Request reasoning, correct tool calling, DB state changes | τ-bench, τ²-bench (text only) |
| **Conversation Management** | Turn-taking, interruptions, backchanneling | Full-Duplex-Bench (artificial tasks) |

**No benchmark existed that evaluates both simultaneously.** τ-Voice fills this gap.

## How Voice Complicates Tasks

Voice increases task difficulty in ways text does not:

1. **No punctuation** — Voice has no periods or commas. Structuring information is harder
2. **Fillers and disfluencies** — "Um," "uh," restarts, hesitations make information extraction difficult
3. **Audio encoding of special characters** — Email addresses, passwords, account numbers must be accurately conveyed via voice
4. **Acoustic environment** — Background noise, accents, phone line compression introduce errors that propagate across turns
5. **Real-time conversation dynamics** — Must fluidly handle interruptions, backchannels, turn-taking

> **Concrete example from the paper:** "A customer calls for account changes. Background noise and an unfamiliar accent cause the agent to mishear the name and fail authentication. Does the agent ask for spelling? If the customer spells it, can the agent accurately transcribe it despite the noise? Can it correct the authentication tool call? Or does it make mistakes when integrating information distributed across multiple turns?"

Such failures **cannot be captured by evaluating ASR, dialogue state tracking, and tool use separately.**

## User Simulator Design

τ-Voice's user simulator is **decoupled from wall-clock time**. This is a critical design choice:

| Traditional Voice Benchmarks | τ-Voice |
|----------------------|---------|
| Real-time constraints force weaker LLMs as simulators | No time constraints enable strongest LLMs as simulators |
| Simulator limitations contaminate evaluation | Simulator is smart enough → can be confident failures are agent-caused |
| Difficult to control diverse accents/acoustic environments | Controllable diversity (accents, noise levels, phone line quality) |

This design enables the strong claim that **"79-90% of failures are attributable to agent behavior."** ASR errors are not the primary cause.

## Two Evaluation Axes

### 1. Task Completion (pass@1)

Whether the database state reaches the correct target state. Directly comparable with the text version τ²-bench.

### 2. Voice Interaction Quality

Appropriateness of turn-taking, response to interruptions, naturalness of backchanneling, appropriateness of silence duration.

## Key Experimental Results: Loss of Text Capability

| Condition | Success Rate | vs Text |
|------|--------|------------|
| **GPT-5 (reasoning) Text** | **85%** | Baseline |
| Voice Agent (clean) | 31–51% | 36–60% |
| Voice Agent (realistic) | 26–38% | 30–45% |

**Only 30–45% of text capability is retained.** The voice modality fundamentally erodes task execution ability.

### Failure Analysis

| Failure Cause | Percentage |
|-----------|------|
| Agent behavior | **79–90%** |
| ASR/voice recognition errors | 10–21% |

This result is significant. The bottleneck for voice agents is not **speech recognition**, but the **agent's reasoning and action selection ability in multimodal situations**.

## Accessibility Implications

τ-Voice reveals a **societal challenge beyond technical issues**:

> Users with non-standard accents, users with speech impairments, and users in noisy environments may experience **systematically degraded service** from voice agents that only work well under ideal conditions.

τ-Voice's evaluation under realistic conditions (noise + diverse accents) provides the first framework to quantify this problem.

## Position in the τ-bench Family

| Dimension | τ-bench | τ²-bench | τ-Knowledge | **τ-Voice** |
|------|---------|----------|-------------|------------|
| Released | June 2024 | June 2025 | March 2026 | **March 2026** |
| Control Model | Single | Dual | Single + KB | **Dual + Voice** |
| Main Domain | Airline, Retail | Telecom | Banking | **Telecom (Voice)** |
| Core Challenge | Dialogue + Tools | Dialogue + Tools + Coordination | Knowledge Retrieval + Reasoning | **Voice Dialogue + Tools + Coordination** |
| Representative Numbers | GPT-4o <50% | Solo→Interactive -25pt | GPT-5.2 ~25.5% | **26–38%** |
| Task Count | — | — | — | **278** |

## Successor: 𝜏-Entity (October 2026)

Sierra's **𝜏-Entity** (Oct 2026, shipped with **𝜏-i18n**) narrows τ-Voice's detail-capture failure mode into a controlled single-field benchmark: 200 tasks × 10 entity types (names, phone numbers, addresses, emails), scored with **Pass³** across regular/noise-heavy/speech-heavy conditions. Best agent (GPT Live 1): 60.3% regular capture but only 34.0% Pass³; Korean Pass³ as low as 3.5–8.5%. Companion **𝜏-Elicitation** paper: agents adapt verification effort to some difficulties (hard/unfamiliar entities) but not others (noise, bad caller voices); prescribed ask→spell→confirm→submit verification raises success 14–41% → 37–54% at +21–28s latency; only 24–37% of verified wrong captures actually get repaired. See [[entities/sierra]]. Source: [[raw/articles/sierra.ai--blog-tau-entity-can-voice-agents-get-the-details-right--bee3927c.md]]

## Practical Implications

1. **Voice is not just "adding a modality"** — It's an intrinsic difficulty increase that loses 55–70% of text capability
2. **ASR is not the primary bottleneck** — Agent multimodal reasoning capability is the challenge
3. **Evaluation should be end-to-end** — Separate evaluation of ASR/dialogue management/tool use cannot capture reality
4. **Accessibility must be built into evaluation** — Performance gaps under diverse conditions are a serious ethical and business issue

## Related Pages

- [[concepts/ai-benchmarks/tau-bench]] — Overview of the τ-bench ecosystem
- [[concepts/ai-benchmarks/tau-squared-bench]] — Dual-control benchmark (foundation of τ-Voice)
- [[concepts/ai-benchmarks/tau-knowledge]] — Evaluation with unstructured knowledge bases
- [[concepts/evaluation/pass-k-metric]] — Reliability evaluation metric
