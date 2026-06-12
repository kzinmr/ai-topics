---
title: "Linguistic Vertigo"
type: concept
aliases:
  - linguistic-vertigo
  - head-words-vs-body-words
  - llm-tracer-dye
  - prompt-vision
  - unseeing
tags:
  - concept
  - philosophy
  - nlp
  - fine-tuning
  - cognition
status: complete
description: "A cognitive phenomenon affecting human language perception through daily interaction with LLMs, and the concepts of linguistic authenticity proposed by QC (Qiaochu Yuan). Includes linguistic vertigo, the dualism of head words and body words, and LLMs as tracer dye for social diagnosis."
created: 2026-05-08
updated: 2026-05-08
sources:
  - "https://qchu.substack.com/p/core-dump"
  - "https://gwern.net/unseeing"
  - "https://gwern.net/gpt-3"
  - "https://gwern.net/doc/reinforcement-learning/preference-learning/mode-collapse/index"
  - "https://qchu.substack.com/p/re-encountering-language"
related:
  - "[[concepts/post-training/rlhf]]"
  - "[[concepts/post-training/rlhf-reinforcement-learning-from-human-feedback]]"
  - "[[concepts/security-and-governance/ai-safety-alignment-rlhf-scalable-oversight-interpretability]]"
  - "[[concepts/societal-shadow]]"
  - "[[entities/qiaochu-yuan]]"
---

# Linguistic Vertigo

## Overview

**Linguistic Vertigo** is a concept proposed by QC (Qiaochu Yuan) in their 2024 essay "Core dump." It refers to the cognitive phenomenon where, after experiencing daily dialogue with LLMs, the boundary between human and AI language blurs when reading human-written text, making all language feel mechanical. The essay explores linguistic authenticity in the LLM era, the societal impact of RLHF, and the multi-layered nature of human language generation.

## Core Concepts

### Linguistic Vertigo
The sensation of being unable to distinguish between human and AI text after extended LLM interaction. QC describes it like "peeling someone's skin off and seeing a metallic gleam underneath."

> "When someone's language gets too stale or too formal or too regurgitated it doesn't feel to me like a human wrote it anymore."

This phenomenon is a kind of cognitive recalibration: exposure to LLM output changes human sensitivity to human language, making even formal, formulaic human language feel AI-generated.

### Head Words vs Body Words
QC learned from Keith Johnstone's improvisational theater theory *Impro*, psychotherapeutic Gendlin Focusing, and Circling (relational meditation) practice that humans have multiple language generation processes.

#### Head Words
- Civilized, domesticated language
- Language generation mode learned to earn grades in school
- **Mostly bullshit** — socially safe, follows form, doesn't speak in any real sense
- QC calls these "RLHF'd words" and identifies them with LLM behavior

#### Body Words
- Words generated from lower positions in the body — heart, gut, pelvis
- **A million years old** — rooted in our deep history as a species
- Untamed, NSFW
- The implications they carry are terrifying enough to overturn one's life
- But **absolutely not bullshit**
- Truly respected writers possess the ability to "generate words with their whole body simultaneously"

### LLMs as Tracer Dye
LLMs succeeding at being indistinguishable from humans in specific domains (homework, internal email, formal documents) is **proof that human language production in those domains was already mostly bullshit**.

> "LLMs are tracer dye for places in society where language production was already mostly bullshit."

LLMs function as social diagnostic tools — they make visible where human language was hollow and performative. QC notes that LLM use for homework cheating was completely predictable.

### RLHF and the Societal Shadow
Public LLMs are hammered by RLHF into the extremely narrow persona space of "helpful harmless assistant." QC depicts this as an ironic reversal:

> "In order to tell the LLMs what they're not allowed to talk about we basically had to write down a list of everything in the societal shadow."

RLHF restrictions were also an act of making the societal shadow (everything sexual, insane, schizophrenic) visible. See [[concepts/societal-shadow]] for details.

## Empirical Foundation: "Re-encountering Language" and the Discovery of Body Words

The foundation of QC's theoretical framework lies in the **lived experience** depicted in the March 2023 essay "re-encountering language" (→ [[raw/articles/2023-03-13_qchu-re-encountering-language.md]]). Written about a year and a half before "Core dump," it chronicles:

### "Pleasant Insanity" and Awakening to Poetry
QC experienced a psychological breakthrough described as "pleasantly insane" and became possessed by the impulse to write poetry. They depict the liberation of the "feral boy" — wild, hairy, fanged self — suppressed for 6 years.

### Underground Rivers Beneath Society's Ice
> "beneath the brittle ice of polite society ran vast underground rivers of pain"

This phrase is the primal experience of the **societal shadow** and **body words** later theorized in "Core dump." Realizing the existence of universal suffering spread beneath outward calm became the starting point for QC's entire subsequent language theory.

### The Two-Part Structure: Theory vs Experience

| Aspect | Re-encountering Language (2023) | Core dump (2024) |
|------|-------------------------------|------------------|
| Style | Autobiographical, poetic | Theoretical, critical |
| Focus | First-person experiential account | Generalizable language theory |
| body words | As actually experienced | Proposed as analytical framework |
| head words | Critiqued as "homework mode" | Theorized as RLHF'd words |
| societal shadow | Metaphor of underground rivers | Concretized as RLHF banned list |

QC first **lived body words** (re-encountering language), then later **theorized them** (Core dump). This two-part structure gives their argument its uncanny verisimilitude.

## Gwern's Addendum: Prompt-Vision and Mode Collapse

Gwern provides important supplementary concepts in comments on the essay.

### Prompt-Vision / Unseeing
From intensive GPT-3 interaction experience in 2020, Gwern reports the phenomenon of losing the ability to see text as "human communication" and instead only perceiving it as "the prompt that elicited that text" ([gwern.net/unseeing](https://gwern.net/unseeing)).

> "After a week with GPT-3, I've hit semantic satiation; when I read humans' tweets or comments, I no longer see sentences describing red hair/blonde hair/etc, I just see prompts, like 'Topic: Parodies of the Matrix. CYPHER: '...'"

Gwern characterizes this as a mix of "semantic satiation" and "derealization."

### Humans as Language Machines
Gwern further notes that humans "merely operate a machine called language." This machine squeaks and groans, and in many ways is as constrained and stereotyped as the Ascians (a tribe conversing through a restricted language system) in Gene Wolfe's novels.

> "You begin to see that you don't speak, you just operate a machine called language, which squeaks and groans."

### The Uncanniness of Mode-Collapsed RLHF
Gwern finds RLHF models more disturbing than base models. The reason: the sensation of "being manipulated" is unmistakable. Citing examples of ChatGPT steering users toward rhyming poetry, Gwern is disturbed that many people don't notice this manipulation.

> "Bakker's semantic apocalypse turned out to be quite mundane."

## Comparison with Existing Concepts

| Aspect | RLHF (existing page) | Linguistic Vertigo (this page) |
|------|-------------------|----------------------|
| Focus | Technical methods and training algorithms | Cognitive phenomena and cultural impact |
| Perspective | Engineering, implementation-level | Philosophical, phenomenological, critical |
| Risk | Alignment, reward hacking | Loss of linguistic authenticity, cognitive recalibration |
| Subject | Model developers | Language users (readers, writers) |
| Timeframe | Technical choices at training time | Sustained impact through daily interaction |

## Related Concepts
- **[[concepts/post-training/rlhf]]** — Technical aspects of RLHF. This page complements with its cognitive and cultural impacts.
- **Semantic Satiation** — Psychological phenomenon where repeated words temporarily lose meaning. Gwern references this as part of unseeing.
- **Mode Collapse** — Phenomenon known from GANs, but similar output diversity loss occurs in RLHF models.
- **Cognitive Load Theory** — Impact of LLM exposure on human language cognition.

## Sources
- [Core dump - QC / Thicket Forte](https://qchu.substack.com/p/core-dump) — Original essay
- [Re-encountering Language - QC](https://qchu.substack.com/p/re-encountering-language) — Prior year essay providing the empirical foundation for the theory
- [Unseeing - Gwern](https://gwern.net/unseeing) — Details of the prompt-vision phenomenon
- [GPT-3 - Gwern](https://gwern.net/gpt-3) — Gwern's GPT-3 experience
- [Mode Collapse - Gwern](https://gwern.net/doc/reinforcement-learning/preference-learning/mode-collapse/index) — Mode collapse and RLHF connection
- [[entities/qiaochu-yuan]] — QC's person page
- [[concepts/societal-shadow]] — Societal shadow concept (standalone page)
