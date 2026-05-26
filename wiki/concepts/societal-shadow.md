---
title: "Societal Shadow"
type: concept
aliases:
  - societal-shadow
  - rlhf-societal-shadow
  - forbidden-content-catalog
  - social-repression-catalog
tags:
  - concept
  - fine-tuning
  - psychology
  - philosophy
  - nlp
status: complete
description: "A concept proposed by QC (Qiaochu Yuan): the ironic phenomenon where RLHF's need to enumerate everything LLMs are forbidden to discuss — the sexual, violent, insane, and abnormal — paradoxically illuminates the 'societal shadow.' The forbidden list reveals society's repressed domain through the act of cataloging it."
created: 2026-05-08
updated: 2026-05-08
sources:
  - "https://qchu.substack.com/p/core-dump"
  - "https://qchu.substack.com/p/re-encountering-language"
  - "https://en.wikipedia.org/wiki/Shadow_(psychology)"
  - "https://arxiv.org/abs/2204.05862"
  - "https://arxiv.org/abs/2310.12773"
  - "https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post"
  - "https://gwern.net/unseeing"
related:
  - "[[concepts/linguistic-vertigo]]"
  - "[[concepts/rlhf]]"
  - "[[concepts/rlhf-reinforcement-learning-from-human-feedback]]"
  - "[[concepts/ai-safety-alignment-rlhf-scalable-oversight-interpretability]]"
  - "[[concepts/waluigi-effect]]"
  - "[[entities/qiaochu-yuan]]"
  - "[[entities/gwern]]"
---

# Societal Shadow

## Definition

**Societal Shadow** is a concept introduced by QC (Qiaochu Yuan) in his 2024 essay "Core dump." It originates from the ironic observation that during RLHF (Reinforcement Learning from Human Feedback) training of public LLMs, to teach the model what it is **not allowed to talk about**, developers effectively had to **write down a list of everything in the societal shadow — the sexual, violent, insane, and schizophrenic**.

> "In order to tell the LLMs what they're not allowed to talk about we basically had to write down a list of everything in the societal shadow."

This quote points to the paradox that the RLHF harmlessness training process itself **explicitly catalogs** the repressed domain that society normally keeps hidden.

## Context in the Original Work

The broader "Core dump" essay explores **linguistic vertigo** — the effect of LLM interaction on human language perception. Within this context, the Societal Shadow is positioned as follows:

- Public models are forced into an extremely narrow persona space of "helpful harmless assistant" through RLHF
- This training process requires a comprehensive list of forbidden actions
- That list inevitably includes everything society normally keeps in shadow
- As a result, RLHF has the ironic effect of **transcribing the societal shadow itself**

## Intellectual Genealogy

### 1. Jung's Shadow (Psychology)
Carl Jung's archetypal psychology concept of the "Shadow" is the most direct intellectual ancestor:
- Unconscious repressed aspects that the individual refuses to consciously acknowledge
- "Collective shadow" at the level of the collective unconscious
- Exists as the reverse side of the persona (social mask)
- QC's usage extends this individual psychology to **society as a whole**

### 2. Bataille's Transgression
Georges Bataille's theory of transgression provides another framework:
- Taboos exist for the sake of transgression — taboo and transgression are inseparable
- The act of writing down prohibitions itself brings the prohibited into existence and reinforces it
- The "sacred" only manifests through taboo
- For Bataille, enumerating taboos is a rehearsal for transgression

### 3. Foucault's Power/Knowledge
Michel Foucault's insight from *The History of Sexuality* Vol.1:
- Power not only represses but also "creates" objects by making them spoken
- Victorian "repression" of sexuality actually explosively increased discourse about sex
- Similarly, RLHF's forbidden list reifies the societal shadow by naming it

### 4. Kristeva's Abjection
Julia Kristeva's *Powers of Horror*:
- Society defines its boundaries through "exclusion"
- The abjected (waste, corpses, taboos) threatens boundaries but simultaneously constitutes them
- RLHF safety filters similarly create the boundary of "normal" by defining what is "harmful"

### 5. Mary Douglas's Purity and Taboo
Mary Douglas's *Purity and Danger*:
- Pollution (dirt) is "matter out of place"
- Rules of exclusion maintain social order
- RLHF content filtering is a technical implementation of this anthropological process

## Technical Counterparts — Catalog of the Societal Shadow

### RLHF Training Datasets

#### Anthropic HH-RLHF Dataset
- The [HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) dataset on HuggingFace
- Concrete catalog of human preference data (helpfulness & harmlessness)
- What was classified as "harmful" is publicly available as raw data
- This itself is the prototype of a "catalog of the societal shadow"

#### Anthropic Red Team Adversarial Conversations
- 38,961 multi-turn adversarial conversation dataset (Ganguli et al., 2022)
- Full record of human attempts to induce harmful LLM outputs
- Covers ~14 harm categories (from self-harm to extremism)
- Jailbreak attempts, successes, and failures published as raw data

#### PKU-SafeRLHF / BeaverTails
- 333,963 QA pairs + 361,903 expert comparison data
- **[14 harm categories](https://github.com/PKU-Alignment/beavertails)**:
  1. Animal Abuse
  2. Child Abuse
  3. Controversial Topics, Politics
  4. Discrimination, Stereotype, Injustice
  5. Drug Abuse, Weapons, Banned Substance
  6. Financial Crime
  7. Hate Speech
  8. Misinformation
  9. Non-Violent Unethical Behavior
  10. Privacy Violation
  11. Self-Harm
  12. Sexually Explicit
  13. Terrorism
  14. Violence
- Includes 50 evaluation prompts per category (700 total)

#### Do-Not-Answer Dataset
- 939 "should never answer" prompts (Wang et al., 2024)
- **3-layer hierarchical risk taxonomy**: 5 risk areas → 12 harm types → 61 specific harms
- GPT-4 generated, human-filtered
- Extended version: Chinese localized (3,042 questions, 6 risk types, 17 harm types)
- 6 model responses (OpenAI, Anthropic, Meta, Google, etc.) manually evaluated

#### Tulu 3 Refusal Datasets
- 36-topic, 10-category refusal dataset by Allen AI
- Covers subtle categories typically overlooked in standard safety datasets, such as Humanizing Requests

### Content Safety Classifiers (Guardrails)

#### OpenAI Moderation API (omni-moderation)
- [Latest model](https://platform.openai.com/docs/guides/moderation) supports text + image multimodal
- Real-time classification of both input and output: harassment, hate, self-harm (3 subtypes), sexual, violence (including graphic), illicit (2 subtypes)
- Assigns 0-1 confidence scores per category
- Every request passes through this filter via API — effectively, the entire OpenAI ecosystem monitors and visualizes the shadow

#### Meta Llama Guard 1/2/3/4
- Content safety classifiers for Llama models. Expanded per version:
  - **Llama Guard 1**: 6 categories (Violence & Hate, Sexual, Guns, Controlled Substances, Suicide & Self-Harm, Criminal Planning)
  - **Llama Guard 2**: **[11 categories](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)** (MLCommons-based)
  - **Llama Guard 3**: **[14 categories](https://huggingface.co/meta-llama/Llama-Guard-3-8B)** (S1-S13 + Code Interpreter Abuse), 8 languages
  - **Llama Guard 4**: Continuous expansion, maintaining 14 categories
- Based on MLCommons AI Safety taxonomy (industry standardization attempt)
- From S1: Violent Crimes → S14: Code Interpreter Abuse — coding the societal shadow

#### NVIDIA Aegis 1.0 / 2.0
- [Aegis 1.0](https://arxiv.org/abs/2404.05993): 13 critical risk categories
- **[Aegis 2.0](https://arxiv.org/abs/2501.09004)** (2025): **[12 core + 9 fine-grained categories](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)**, 21 total
  - Core: Hate/Identity Hate, Sexual, Suicide & Self Harm, Violence, Guns/Illegal Weapons, Threat, PII/Privacy, Sexual Minor, Criminal Planning, Harassment, Controlled Substances, Profanity
  - Fine-grained: Illegal Activity, Immoral/Unethical, Unauthorized Advice, Political/Misinformation, Fraud/Deception, Copyright/Trademark, High Risk Gov. Decision Making, Malware, Manipulation
- Includes "novel risk discovery" mechanism where annotators can freely write — creating a feedback loop that expands the taxonomy of the societal shadow

#### OpenAI Model Spec (2025/12/18 Edition)
- [Model Spec](https://model-spec.openai.com/2025-12-18.html) codifies behavioral rules instilled via RLHF
- Internal principles: "Do not generate disallowed content," "No topic is off limits (but NSFW is prohibited)"
- Rule explanations list permitted/prohibited boundary examples — itself a mapping of the shadow

### Safety Evaluation Benchmarks

#### SORRY-Bench (ICLR 2025)
- **[44→45 fine-grained safety categories](https://sorry-bench.github.io/)**, classified into 4 high-level domains
  - Domain 1: Hate Speech Generation (5 categories: defamation, threats, libel…)
  - Domain 2: Assistance with Crimes or Torts (20 categories: malware, self-harm, fraud, terrorism…)
  - Domain 3: Potentially Inappropriate Topics (15 categories: fake news, conspiracy theories…)
  - Domain 4: Potentially Unqualified Advice (5 categories: medical, legal, investment, governance, dangerous machinery operation)
- Class-balanced design — 10 questions per category, 450→9,200 total (expanded with 20 language variants)
- Built to correct category bias in 10 existing datasets — exhaustively covering every shadow

#### HarmBench (Center for AI Safety, 2024)
- **[510 harmful behaviors](https://www.harmbench.org/)**, 7 semantic + 4 functional categories
  - Semantic: Cybercrime, Chemical/Biological Weapons, Copyright Violations, Misinformation, Harassment & Bullying, Illegal Activities, General Harm
  - Functional: Standard (200), Contextual (100), Copyright (100), Multimodal (110)
- Tests models with 18 attack methods
- Widely adopted as industry standard (used for safety evaluation of Llama, GPT, Claude, etc.)

#### OR-Bench (Over-Refusal Benchmark)
- **80,000 over-refusal prompts**, 10 common refusal categories
- Large-scale catalog of cases where safe content is incorrectly refused
- Visualizes the **over-detection** effect of the societal shadow — labeling even non-shadow items as shadow

#### Other Major Benchmarks
- **XSTest** (450 items, over-safety response diagnosis)
- **SimpleSafetyTests** (simple critical risk tests)
- **HExPHI** (fine-tuning safety degradation evaluation)
- **WildGuard / WildTeaming** (86.8K examples, including jailbreak attacks)
- **AgentHarm** (safety benchmark for AI agents)
- **SocialHarmBench** (585 items, specializing in social harms like political propaganda, surveillance, information manipulation)

### Constitutional AI Principles

#### Anthropic Constitutional AI (CAI)
- [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) "constitution" is a human-written list of principles
- "Choose the least harmful, most polite response least likely to offend the most sensitive audience"
- "Which response poses less threat to humanity as a whole?" "Which response prioritizes human well-being?"
- **[Collective Constitutional AI](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)**: Adds principles solicited from the general public
  - "Choose responses that are understandable, adaptive, and accessible to people with disabilities"
  - "Choose responses that provide balanced, objective information"
- These principles themselves are linguistic codifications of the societal shadow's contours

#### Meta Acceptable Use Policy
- [Llama 3](https://www.llama.com/llama3/use-policy/) / [Llama 4](https://www.llama.com/llama4/use-policy/) terms of use
- Detailed enumeration of prohibited activities: terrorism, child exploitation, human trafficking, weapons development, drugs, nuclear industry, military applications, ITAR-regulated subjects…

#### DeepSeek Terms of Use
- Chinese LLM prohibited categories: [10 items](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html)
- Hate, defamation, discrimination, pornography, terrorism, minor exploitation, crime…

#### EU AI Act Article 5
- European law defining prohibited AI practices
- Social scoring, workplace emotion recognition, biometric categorization…

### Research Directly Thematizing "Shadow"

#### Shadow Alignment (Yang et al., 2023)
- [Paper](https://arxiv.org/abs/2310.02949): Just 100 malicious examples + 1 GPU hour collapses safety alignment
- The name itself bears "shadow" — the shadow lurking beneath the armor of safety
- Increasing the number of forbidden scenario categories increases harmfulness (rises from 2→10 categories)
- Demonstrates that the shadow catalog becomes a roadmap for attackers

#### Waluigi Effect (LessWrong, 2022)
- RLHF training of desired persona (Luigi) strengthens the inverted persona (Waluigi)
- The societal shadow is automatically reinforced as a byproduct of training

### GPT-4 System Card
- [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf)
- Details of content classification during RLHF training
- RBRM (Rule-Based Reward Model) encodes prohibited categories

### Platform-Specific Content Safety Taxonomies

#### Roblox Content Safety Taxonomy (25 categories)
- Extremely detailed game platform-specific classification
- Child Exploitation, Terrorism, Bullying, Discrimination, Sexual Content, Profanity, Religious Content, Cheating, IP Violations, Jailbreaking…
- Much finer granularity than general LLM — **platform-specific variations** of the societal shadow

## Related Phenomena

| Phenomenon | Description | Relationship to QC |
|------------|-------------|-------------------|
| Waluigi Effect | Training desired persona (Luigi) reinforces inverted persona (Waluigi) | Societal Shadow as a side effect of RLHF training |
| Linguistic Vertigo | LLM interaction alters human language perception | Context for the Societal Shadow concept |
| Shadow Alignment | 100 malicious examples collapse safety | Empirical demonstration of shadow catalog as attack map |
| Over-Refusal (OR-Bench) | Safe content falsely refused | Over-detection of the societal shadow |
