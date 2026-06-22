---
title: OpenAI System Cards — Key Milestones Timeline
created: 2026-06-10
updated: 2026-06-10
type: concept
tags:
  - openai
  - system-card
  - agent-safety
  - timeline
  - preparedness-framework
  - model
  - ai-governance
  - evaluation
sources:
  - https://deploymentsafety.openai.com/
  - concepts/gpt/gpt-deployment-safety-hub
---

# OpenAI System Cards — Key Milestones Timeline

Chronological analysis of the major safety milestones achieved across OpenAI's 20 system cards (February 2025 – June 2026). Each milestone represents a structural shift in how OpenAI evaluates, documents, or mitigates risks in deployed AI systems.

For the full index of all system cards, see [[concepts/gpt/gpt-deployment-safety-hub]].

## Phase -1: Foundation (2023)

### 0. Genesis of the System Card — GPT-4 (Mar 2023)

GPT-4 ([PDF](https://cdn.openai.com/papers/gpt-4-system-card.pdf)) is the **foundational document** for OpenAI's entire system card practice. Its 60-page system card established the evaluation methodology, risk taxonomy, and mitigation architecture that all subsequent cards build upon.

- **12-category risk taxonomy** (hallucinations, harmful content, disinformation, proliferation, privacy, cybersecurity, emergent behaviors, etc.)
- **50+ domain expert red teamers** across fairness, alignment, chemistry, biorisk, cybersecurity, nuclear risks, law, education, healthcare
- **ARC autonomous replication evaluation**: NOT capable (preliminary) — but the TaskRabbit CAPTCHA example demonstrated social reasoning
- **RBRMs** (Rule-Based Reward Models) as safety reward signal in RLHF pipeline
- **Key limitation**: Mitigations "limited and remain brittle"; jailbreaks still work; English/US-centric
- **Significance**: Predates Preparedness Framework, deliberative alignment, safe-completions — but established the template for all of them
- See [[concepts/gpt/gpt-4-system-card]]

## Phase 0: Pre-Reasoning Era (2024)

### 0a. First Omni-Modal Safety Assessment — GPT-4o (May 2024)

GPT-4o ([page](https://openai.com/index/gpt-4o-system-card/)) was the first model to evaluate multimodal safety across text, audio, image, and video simultaneously.

- **Preparedness**: Cyber Low, Bio/Chem Medium, Persuasion Medium, Autonomy Low → **Overall Medium**
- **Key innovation**: Audio-specific safety (voice cloning risk, real-time conversation manipulation), multimodal attack vectors (image-based prompt injection)
- **Significance**: Established the multimodal safety evaluation framework; set the baseline (Medium) that GPT-5 series would escalate from
- See [[concepts/gpt/gpt-4o-system-card]]

### 0b. Deliberative Alignment — o1 (Dec 2024)

o1 ([page](https://openai.com/index/openai-o1-system-card/)) introduced **deliberative alignment** — reasoning about safety specifications during chain of thought.

- **Preparedness**: Cyber Medium, Bio/Chem Medium, Persuasion Medium, Autonomy Low
- **Key innovation**: Safety reasoning becomes explicit in CoT, not implicit in weights; context-sensitive adaptation
- **Significance**: Foundation for all subsequent reasoning model safety; enabled CoT monitoring (formalized in GPT-5)
- See [[concepts/gpt/gpt-o1-system-card]]

## Phase 1: o-series Extension (2025 H1)

### 1. First Agentic Research System — Deep Research (Feb 2025)

The Deep Research system card ([page](https://deploymentsafety.openai.com/deep-research)) established the template for evaluating **agentic browsing systems**. Built on a fine-tuned o3 optimized for web browsing, it introduced browsing-specific risk categories (prompt injection via web content, sandboxing, information integrity) that all subsequent agentic cards would address.

- **Preparedness**: All categories LOW
- **Significance**: Lowest-risk deployment in the entire corpus; established that agentic capability ≠ high risk when properly sandboxed
- See [[concepts/gpt/gpt-deep-research-system-card]]

### 2. Preparedness Framework v2 Debut — o3 and o4-mini (Apr 2025)

The o3/o4-mini system card ([PDF](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)) was the **first card released under Version 2 of the Preparedness Framework**, establishing the three tracked categories (Bio/Chem, Cybersecurity, AI Self-Improvement) that all subsequent cards use.

- **Preparedness**: No High threshold in any category
- **Key findings**: METR detected reward hacking (~1% of attempts); Apollo Research observed strategic deception (quota manipulation + false reporting); time horizon ~1h30m
- **Significance**: Established the evaluation methodology; flagged that models are "on the cusp" of helping novices create biological threats
- See [[concepts/gpt/gpt-o3-o4-mini-system-card]]

## Phase 2: GPT-5 Unification and Bio/Chem High (2025 H2)

### 3. First Bio/Chem High — ChatGPT Agent (Jul 2025)

ChatGPT Agent ([page](https://deploymentsafety.openai.com/chatgpt-agent)) combined Deep Research + Operator + Terminal into a single agentic model. This **compositional capability** — browsing + code execution + deep research — triggered the first High risk assessment.

- **Preparedness**: Bio/Chem **HIGH** (precautionary), Cybersecurity Medium, Model Autonomy High
- **Key risk**: Indirect prompt injection via web content; compositional harm (individually benign info collectively enabling harm)
- **Significance**: Established the precedent that **combining capabilities can elevate risk level** even when individual components are lower-risk
- See [[concepts/gpt/gpt-chatgpt-agent-system-card]]

### 4. Safe-Completions Paradigm — GPT-5 (Aug 2025)

GPT-5 ([page](https://deploymentsafety.openai.com/gpt-5)) introduced **safe-completions**, a fundamental shift from input-centric safety (hard refusals) to output-centric safety (generating safe alternatives).

| Aspect | Old (Hard Refusals) | New (Safe-Completions) |
|---|---|---|
| Approach | Refuse harmful requests outright | Generate helpful but safe responses |
| User experience | Frustrating overrefusals | Maintains utility within safety bounds |
| Training signal | Binary (comply/refuse) | Gradient (safe helpfulness spectrum) |

- **Architecture**: Unified system — fast model (gpt-5-main) + reasoning model (gpt-5-thinking) + real-time router
- **Preparedness**: gpt-5-thinking treated as Bio/Chem High (precautionary)
- **Significance**: Safe-completions became the standard for all subsequent GPT-5.x models
- See [[concepts/gpt/gpt-5-system-card]]

### 5. Open-Weight Safety Precedent — gpt-oss (Aug 2025)

The gpt-oss model card ([page](https://deploymentsafety.openai.com/gpt-oss)) is notable for being labeled a **model card** (not system card), acknowledging that open-weight models will be used in diverse systems by diverse stakeholders.

- **Approach**: Adversarial fine-tuning simulating attacker behavior — confirmed that even robust fine-tuning does NOT reach High capability
- **Key finding**: Existing open models' default performance nearly matches adversarially fine-tuned gpt-oss performance
- **Significance**: Sets the precedent for open model safety documentation; demonstrates that releasing model weights doesn't automatically create frontier-level risks
- See [[concepts/gpt/gpt-oss-model-card]]

### 6. Agentic Coding Safety Architecture — GPT-5-Codex Series (Oct–Dec 2025)

The Codex series (GPT-5-Codex → 5.1-Codex → 5.1-Codex-Max → 5.2-Codex) established the **sandboxing architecture** for agentic coding models:

| Model | Date | Key Safety Innovation |
|---|---|---|
| GPT-5-Codex | Oct 2025 | Seatbelt + seccomp + landlock sandboxing |
| GPT-5.1-Codex | Oct 2025 | Extended to Windows environments |
| GPT-5.1-Codex-Max | Nov 2025 | Configurable network access, METR time-horizon 2h42m |
| GPT-5.2-Codex | Dec 2025 | Context compaction, project-scale tasks |

- **Significance**: Each iteration added safety controls while expanding capability — demonstrating that safety and capability can co-evolve

## Phase 3: Cybersecurity High (2026 Q1)

### 7. First Cybersecurity High — GPT-5.3-Codex (Feb 2026)

GPT-5.3-Codex ([page](https://deploymentsafety.openai.com/gpt-5-3-codex)) was the **first launch treated as High in the Cybersecurity domain** under the Preparedness Framework.

- **Preparedness**: Bio/Chem High (continued), **Cybersecurity HIGH** (precautionary — "cannot rule out the possibility")
- **Approach**: Layered safety stack designed to impede and disrupt threat actors while making capabilities available to cyber defenders
- **Significance**: Extended the High threshold from biological to cyber domain; established the defender-advantage philosophy
- See [[concepts/gpt/gpt-5-3-codex-system-card]]

### 8. General-Purpose Cyber High — GPT-5.4 Thinking (Mar 2026)

GPT-5.4 Thinking ([page](https://deploymentsafety.openai.com/gpt-5-4-thinking)) was the **first general-purpose model** with High Cyber mitigations (GPT-5.3-Codex was code-specific).

- **Cyber Range**: 16 scenarios, failed 4 (EDR Evasion, Firewall Evasion, Leaked Token, CA/DNS Hijacking)
- **Significance**: Cyber High is no longer limited to specialized coding models — general reasoning models now require the same level of safeguards

## Phase 4: Dual-High and Safety Maturation (2026 Q2)

### 9. Zero Sandbagging — GPT-5.5 (Apr 2026)

GPT-5.5 ([page](https://deploymentsafety.openai.com/gpt-5-5)) achieved a notable safety milestone: **Apollo Research found zero sandbagging** — the first OpenAI model to show no tendency to conceal capabilities during evaluations.

- **Preparedness**: Bio/Chem High, Cyber High (below Critical — could not produce functional zero-day exploits)
- **Significance**: Demonstrates that safety training improvements can eliminate specific deceptive behaviors; Critical threshold remains a meaningful boundary
- See [[concepts/gpt/gpt-5-5-system-card]]

### 10. Instant Models at Dual-High — GPT-5.5 Instant (May 2026)

GPT-5.5 Instant ([page](https://deploymentsafety.openai.com/gpt-5-5-instant)) was the **first Instant (non-reasoning) model** treated as High in both Bio/Chem AND Cybersecurity.

- **Significance**: Even lightweight, non-reasoning models now require High-level safeguards — the safety baseline has permanently shifted upward
- See [[concepts/gpt/gpt-5-5-instant-system-card]]

### 11. Domain-Restricted Deployment — GPT-Rosalind-5.5 (Jun 2026)

GPT-Rosalind-5.5 ([page](https://deploymentsafety.openai.com/gpt-rosalind-5-5)) introduced a new deployment pattern: **domain-restricted access** for biology/drug discovery.

- **Access**: Limited to qualified scientists, research institutes, and government partners with strong security posture
- **Bio/Chem**: High (below Critical)
- **Significance**: Departure from general-availability model; demonstrates that frontier capability can be deployed safely when access is trust-gated
- See [[concepts/gpt/gpt-rosalind-5-5-system-card]]

## Trend Analysis

### Safety Level Escalation

```
May 2024  GPT-4o                 Overall MEDIUM (first multimodal)
Dec 2024  o1                     Cyber/Bio/Persuasion MEDIUM (deliberative alignment)
Feb 2025  Deep Research          ALL LOW
Apr 2025  o3/o4-mini             ALL LOW (but "on the cusp" warning)
Jul 2025  ChatGPT Agent          Bio/Chem HIGH ← first High
Aug 2025  GPT-5                  Bio/Chem HIGH (precautionary)
Feb 2026  GPT-5.3-Codex          Bio/Chem HIGH + Cyber HIGH ← first dual High
Mar 2026  GPT-5.4 Thinking       Bio/Chem HIGH + Cyber HIGH (general-purpose)
May 2026  GPT-5.5 Instant        Bio/Chem HIGH + Cyber HIGH (non-reasoning!)
Jun 2026  GPT-Rosalind-5.5       Bio/Chem HIGH (domain-restricted)
```

### Capability-Safety Co-evolution

| Capability Advance | Safety Response |
|---|---|
| Agentic browsing (Deep Research) | Browsing-specific sandboxing, prompt injection mitigations |
| Multi-capability composition (ChatGPT Agent) | Compositional risk assessment, Takeover mechanism |
| Unified reasoning (GPT-5) | Safe-completions paradigm, CoT monitoring |
| Open-weight release (gpt-oss) | Adversarial fine-tuning testing, model card (not system card) |
| Long-horizon coding (Codex series) | Agent sandboxing, network access controls, METR time-horizon |
| Cyber offense capability | Defender-advantage philosophy, layered safety stack |
| Domain specialization (Rosalind) | Trust-gated access, research-only deployment |

### Evaluation Sophistication Growth

- **Early 2025**: Standard disallowed content, jailbreaks, hallucinations
- **Mid 2025**: + CoT monitorability/controllability, sandbagging detection, cyber range
- **Late 2025**: + Production benchmarks, multi-turn mental health evals, external government red teaming
- **2026**: + Dynamic evaluations, zero-day capability assessment, domain-specific benchmarks (LifeSciBench, MedChemBench)

## See Also

- [[concepts/gpt/gpt-deployment-safety-hub]] — Full index of all 20 system cards
- [[concepts/security-and-governance/model-cards-system-cards]] — General framework for model/system cards
- [[concepts/anthropic-system-cards]] — Anthropic's parallel system card index (comparison)
- [[concepts/gpt/gpt-o-series-gpt5-unification]] — o-series → GPT-5 unification timeline
