---
title: Gemini 3.7 Flash
created: 2026-08-15
updated: 2026-08-15
type: entity
tags:
  - model
  - google
  - gemini
  - multimodal
  - text-generation
  - code-model
  - coding-agents
  - ai-agents
  - inference
  - reasoning
  - agentic-engineering
  - web-development
  - frontier-models
sources:
  - raw/articles/2026-08-13_google_gemini-3-7-flash.md
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
---

# Gemini 3.7 Flash

Google DeepMind's frontier "workhorse" model for coding and agents, announced August 13, 2026 — three weeks after Gemini 3.6 Flash (the prior [[concepts/gemini/gemini-3-5-flash|Gemini 3.5 Flash]] is the previous Flash entry documented here). Touted as "our most intelligent workhorse model yet for coding and agents."

## Key benchmark gains (vs 3.6 Flash)

- **Coding**: FrontierCode 1.1 Main 43.6% (vs 34.4%); DeepSWE v1.1 65.3% (vs 49.0%). Higher first-pass code accuracy, better production-ready code generation.
- **Web development**: WebDev Arena Elo 1588 (vs 1538). More functional layouts, feature-complete apps in fewer prompts, high design adherence from screenshot/image/design-system reference inputs.
- **Knowledge work**: GDP.pdf benchmark 34.0% (vs 22.0%) for complex-document processing; AutomationBench 30.4% (vs 17.0%) for real-world business workflows.

## Pricing and developer experience

Introductory price (through end of year) of **$0.75/1M input and $3.75/1M output tokens** — half the original 3.6 Flash price. Improved developer experience: better adapts to roadblocks, clarifies intent, follows instructions with greater fidelity, "thinks more diligently" on multi-step planning and tool calls.

## Integrations

- **[[concepts/gemini/gemini-spark|Gemini Spark]]** (Google AI Pro/Ultra, 160+ countries) runs on 3.7 Flash from launch — improved Workspace tool use and multi-skill workflows.
- **Google Antigravity** agent-first workflows, Gemini API (AI Studio, Android Studio), Gemini Enterprise Agent Platform.

## Safety

Ships with updated Frontier Safety safeguards against CBRN (chemical/biological/radiological/nuclear) and cyber-offense misuse.

## Related

- [[concepts/gemini/gemini-3-2-flash|Gemini 3.2 Flash]]
- [[concepts/gemini/gemini-spark|Gemini Spark]]
- [[concepts/gemini-computer-use|Gemini Computer Use]]
- [[entities/deepmind|Google DeepMind]]
