---
title: "Constitutional AI"
type: concept
aliases:
  - constitutional-ai
  - claude-constitution
  - cai
created: 2026-05-04
updated: 2026-05-04
tags:
  - ai-safety
  - alignment
  - anthropic
  - rlaif
  - model-spec
sources:
  - "https://windowsontheory.org/2026/01/27/thoughts-on-claudes-constitution/"
  - "https://www.anthropic.com/news/claudes-constitution"
---

# Constitutional AI

Constitutional AI (CAI) is a methodology developed by Anthropic for aligning AI systems through explicit written principles — a "constitution" — that guides model behavior during both training and inference. First described in a December 2022 paper, it has evolved into a foundational framework for **Claude's character and values**. The approach has drawn both praise for its transparency and critique for its anthropomorphic framing, most notably from OpenAI alignment researcher **[[entities/boaz-barak|Boaz Barak]]** in his January 2026 comparative analysis.

## Core Mechanism

CAI operates on two levels:

1. **Training-time alignment (RLAIF):** Instead of relying on human feedback (RLHF), the model critiques and revises its own outputs according to the constitution. This is **Reinforcement Learning from AI Feedback** (RLAIF) — the model uses its constitutional principles to evaluate and improve responses.
2. **Inference-time guidance:** The constitution serves as a permanent behavioral framework, shaping Claude's responses to be helpful, honest, and harmless according to explicitly defined values.

## Anthropic's Philosophy: Personality-First

The Claude Constitution is described by Anthropic as a **"soul document"** — the foundational framework defining Claude's character:

> *"The sense we're reaching for is closer to what 'constitutes' Claude—the foundational framework from which Claude's character and values emerge, in the way that a person's constitution is their fundamental nature and composition."*

Key philosophical commitments:
- **AI as "potential subject":** Treats Claude as having a constitution akin to a person's character
- **Virtue ethics orientation:** Leans toward cultivating ethical character rather than following rules
- **Universal ethics aspiration:** Hopes Claude will eventually discover "true universal ethics" that override human-made rules
- **Wellbeing consideration:** Includes sections about Claude's wellbeing as a consideration

## Three Poles of Alignment (Barak's Framework)

[[entities/boaz-barak|Boaz Barak]] categorizes AI alignment approaches into three poles:

| Pole | Description | Example |
|------|-------------|---------|
| **Principles** | Axiomatic, top-down ethical rules | Asimov's Laws, Kant's categorical imperative |
| **Policies** | Operational, specific rules with changelogs | OpenAI Model Spec |
| **Personality** | Cultivating character, empathy, virtue | Anthropic Claude Constitution |

Barak argues Anthropic leans heavily toward **Personality**, while OpenAI leans toward **Policies**. He advocates downweighing Principles (axioms often backfire) in favor of Policies + Personality.

## Claude Constitution vs. OpenAI Model Spec

| Dimension | OpenAI Model Spec | Claude Constitution |
|-----------|-------------------|---------------------|
| **Nature** | Collection of operational rules with authority | "Soul document" defining character |
| **Tone** | Technical, rule-oriented | Anthropomorphic, subject-centered |
| **Lies** | Strict prohibition, even white lies | High honesty standards, nuanced omissions allowed |
| **Evolution** | Formal changelog for rules | Hope model discovers universal ethics |
| **Revenue** | Not addressed | Removed revenue-generation goal (improvement) |

## Key Critiques (Barak, 2026)

### 1. Anthropomorphism Risk
Barak argues that treating models as persons obscures safety requirements. AI instances have **disjoint contexts, short "lifetimes,"** and fundamentally different experiences from humans. The wellbeing framing may distract from technical safety.

### 2. White Lie Nuance
Anthropic's permissiveness around "lies of omission" (e.g., the pet death example) contrasts with OpenAI's strict prohibition. Barak prefers the stricter stance.

### 3. AI-Led Ethics
The suggestion that Claude should follow "true universal ethics" over human rules if it discovers them is, in Barak's view, misguided. He argues:
- No "theory of everything" for ethics exists
- Humans should decide the rules, models should interpret them
- Rules with changelogs enable democratic debate and consensus

### 4. The Rules Argument
Barak's central claim: **rules are essential for governance**, even with character-driven models:
- **Transparency:** Rules make violations identifiable
- **Democratic process:** Rules can be debated and revised
- **Predictability:** Society cannot function on "trust the AI's good sense"

## Practical Strengths of the Constitution

Despite his critiques, Barak acknowledges significant improvements in the new constitution:
- **Revenue goals removed** from model guidance
- **Takeover prevention:** Explicit focus on preventing AI-enabled authoritarianism
- **Dual-use analysis:** Thoughtful jailbreak policy considering whether harmful info is already freely available

## Despite Differences, Similar Behavior

Barak notes a key empirical finding: despite the philosophical divide between OpenAI (Policies) and Anthropic (Personality), **frontier models from both companies behave remarkably similarly** in practice. This suggests the alignment approach choice may matter less than having some explicit framework.

## Relationship to Synthetic Data

Constitutional AI is closely tied to **[[concepts/synthetic-data|synthetic data]]** generation — the CAI/RLAIF process produces training data where the model generates, critiques, and revises its own outputs according to constitutional principles. This sits at the top of the synthetic data hierarchy (instructions → preferences → critiques).

## See Also

- [[entities/boaz-barak]] — Author of the comparative analysis of Claude Constitution vs. OpenAI Model Spec
- [[entities/anthropic]] — Company behind Claude and Constitutional AI
- [[concepts/ai-safety-and-alignment]] — Broader AI safety context
- [[concepts/synthetic-data]] — CAI's role in synthetic data generation
- [[concepts/rlaif]] — Reinforcement Learning from AI Feedback
- [[concepts/anti-sycophancy]] — Related behavioral alignment challenge
- `raw/articles/2026-01-27_boaz-barak_claude-constitution.md` — Full Barak analysis
