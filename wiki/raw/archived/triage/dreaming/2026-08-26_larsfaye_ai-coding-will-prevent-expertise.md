---
title: "AI Coding will Prevent Expertise"
url: "https://larsfaye.com/articles/ai-coding-will-prevent-expertise"
fetched_at: 2026-08-27T22:30:00+00:00
source: "larsfaye.com"
tags: [blog, raw]
---

# AI Coding will Prevent Expertise — The need for ongoing friction in long-term skill formation

Source: https://larsfaye.com/articles/ai-coding-will-prevent-expertise
Shared by @addyosmani on X (2026-08-26) with: "Friction is what builds taste and mastery. The tools that remove it also remove what made us good enough to use them well."

Follow-up to the author's earlier "Agentic Coding is a Trap" ("skilled orchestrator paradox" — the skills required to manage coding agents are the same skills that atrophy through continued agent use).

## Core argument: the Expert Novice paradox

- The industry simultaneously (a) says "if you don't use AI you'll be left behind" ("AI won't replace you, someone using AI will"), and (b) says best results come from higher-order thinking — specs, design patterns, diligent review — i.e. "vibe coding is a dead end."
- But the skills needed to wield agents well (architecture taste, review judgment) are built precisely by the friction that agent tools remove. Result: "a novice needs expert-level skills to leverage the tools and keep pace in the industry" — the **Expert Novice**.

## Evidence cited

- JetBrains-cited study "The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers" (live coding sessions, varying AI assistance): novices thought they had "a personal tutor" but the data showed the opposite — heavy AI users "skipped crucial planning stages" and "finished with an 'illusion of competence'"; participants who mitigated/ignored AI assistance performed best, aided by **"negative expertise"** ("the ability to ignore incorrect or unhelpful GenAI suggestions").
- "Inverted learning" model: the student first guides the mentor (the LLM), then steers it — precarious because beginners don't know what they don't know; LLMs are "incredibly complex pattern interpolators" lacking judgment, empathy, pedagogical intent. Even well-prepared students were derailed ("skipped crucial problem-solving planning stages, jumping directly to coding, enticed by Copilot into quickly producing code," then relying on the LLM to fix the LLM's own error).
- UPenn 2025 "Generative AI without guardrails can harm learning": 1,000 students learning math with an LLM vs textbook — AI group used it as a crutch and performed **17% worse**, while believing they were excelling. A "Tutor" variant (model asks for help first, student solves) produced **+127%** in the AI-assisted practice session — cognitive work shifted back onto the individual.
- Anthropic 2026 "How AI assistance impacts the formation of coding skills": "Cognitive effort — and even getting painfully stuck — is likely important for fostering mastery." Ironic finding: "the most productive learning that can happen with an AI coding tool is when it isn't used to generate much of any code at all."

## "The Friction is a Feature"

- Expertise comes from experience, repetition, trial and error — "developer intuition"/"taste" (German: *Fingerspitzengefühl* — the muscle memory of "this will probably cause problems") is built by struggling with the mechanics.
- **Pipeline collapse** risk: if LLMs write and debug code, and agents do system design, the trillion-dollar bet is that deep programming knowledge "won't matter." Author calls this the same hubris as past no-code movements. Cites David Cramer (Sentry co-founder): "I will flex and show you how broken the code is 100% of the time."

## Prescription: Friction First

- Joel Spolsky's Law of Leaky Abstractions (2002): abstractions save time working but "don't save us time learning" — LLMs are "the ultimate leaky abstraction."
- Advice: for learning/expertise, largely disregard LLM code generation; use models as interactive documentation, dynamic tutorial generators, and Socratic exercises (dialogic AI "can meaningfully stimulate reflective, critical and independent thinking").
- Verify AI mentor output against official docs, human peers, and trial and error — "if you can't audit the accuracy of the generated code, you can't audit the accuracy of the generated concept."
- Kent Beck quote: "Coding's actually a great way to cement understanding. The more you program, the more you understand the domain."
- Notes the ecosystem works against this: AI mandated across companies, IDEs hiding code view (e.g. Cursor tucks away code view unless sought), some firms forcing AI-only coding regardless of experience level.

## Notes

- Addy Osmani shared it aimed at team leads and early-career engineers (Aug 26, 2026).
- Related wiki threads: [[concepts/harness-engineering]] (agent-first development practice), [[concepts/vibe-coding]] (the "dead end" critique), [[concepts/agentic-engineering]] (Simon Willison's "verify, don't just eyeball" and cognitive-capacity-as-limit arguments — the pro-agent counterweight: friction reduction shifts the bottleneck to human judgment/scope discipline rather than eliminating the need for expertise).
