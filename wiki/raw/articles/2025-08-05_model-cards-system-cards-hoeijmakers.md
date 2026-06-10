---
title: "Model Cards, System Cards and What They're Quietly Becoming"
author: Rob Hoeijmakers
date: 2025-08-05
updated: 2026-04-27
url: https://hoeijmakers.net/model-cards-system-cards/
category: AI Governance
tags: [model-card, system-card, ai-governance, ai-transparency, eu-ai-act, safety, evaluation]
---

# Model Cards, System Cards and What They're Quietly Becoming

**Author:** Rob Hoeijmakers (@robhoeij)
**Published:** 2025-08-05 | **Updated:** 2026-04-27
**Source:** https://hoeijmakers.net/model-cards-system-cards/

---

> "I think everyone interested in AI should read the model cards for the frontier models, especially the safety sections, which give you a sense of immediate concerns."
> — Ethan Mollick, 4 August 2025

## Summary

The article is triggered by Ethan Mollick's X post recommending that anyone interested in AI read the **model cards** of frontier models — especially the safety sections. Mollick linked to OpenAI's o3, Google's Gemini Deep Think, Anthropic's Claude 4, but Grok was notably absent ("????").

## What Are Model Cards — and Why Do They Matter?

**Model cards** (and their broader cousins, **system cards**) are documents published by the makers of large AI models to describe what those models can do, how they've been tested, and what their limitations are.

They usually include:

- What kind of data the model was trained on (or a vague description of it)
- What benchmarks it has been tested against (like MMLU, ARC, TruthfulQA)
- Where it tends to fail (hallucinations, bias, factuality)
- What the developers did to reduce harm (red teaming, refusal behaviour)
- And how they see the model in a broader societal context (misuse risks, alignment strategies)

Some are technical. Some are polished. All of them are political in the sense that they reveal (or conceal) the design choices and values behind these increasingly powerful systems.

## System Cards and Safety: The Frontier Disclosure

OpenAI calls theirs **system cards**. So does Anthropic. Google went with **model cards**. The terms overlap, but the purpose is similar: they're a kind of *disclosure*. A way to say: "Here's what we've built, and here's what you should know about it."

Patterns observed when reading through them:

- Benchmarks are everywhere. Some models outperform humans on complex tests, but still hallucinate simple facts.
- Safety claims are layered: technical fixes, refusal behaviour, internal red teaming, sometimes external audits.
- Many disclaim any true autonomy. Even the most capable models are described as "not agentic," "not self-aware," or "not capable of long-term planning."
- And yet, the cards often reveal that these same models can reason, plan, and follow goals in scaffolded environments.

"It's like looking at a machine that *almost* drives itself and seeing all the little disclaimers stuck to the dashboard."

## How This Relates to Policy

In the **EU AI Act**, foundation models like GPT, Claude and Gemini are being put in their own regulatory category. The Act introduces specific **documentation and transparency obligations** — including the need to describe:

- Training data sources,
- Evaluation results,
- Risks and mitigations.

Even though model/system cards are not legally required today, they are *functioning* like proto-regulatory documents. They're the documents regulators will ask for first. And they show where the lines are being drawn — not just between companies, but between what's considered safe, responsible, or questionable.

In the US, the recent **Executive Order on AI** and NIST's **AI Risk Management Framework** strongly encourage documentation, testing, and disclosure. Again, model/system cards are the natural container for that.

## And Then There's Grok

In Mollick's post, Grok by xAI was the only one listed without a link. "????", he wrote. For all the emphasis on "truth-seeking" and "maximum transparency," xAI has not published a system card for Grok. No clear documentation of risks. No benchmarks. No list of safety mitigations or evaluations. "Absence is a kind of signal, too."

## Key Analytical Perspectives

1. **Terminology divergence**: OpenAI/Anthropic use "system cards", Google uses "model cards" — overlapping but distinct scopes
2. **Benchmark ubiquity vs. hallucination persistence**: Models outperform humans on complex tests yet hallucinate simple facts
3. **Safety claims as layers**: Technical fixes → refusal behaviour → internal red teaming → external audits
4. **Autonomy disclaimers vs. capability evidence**: "Not agentic" disclaimers coexist with reasoning/planning capabilities in scaffolded environments
5. **Proto-regulatory function**: System cards function as the documents regulators will ask for first, even before legal requirements
6. **Absence as signal**: xAI/Grok's lack of a system card is itself informative
7. **Political nature**: All cards are political — they reveal or conceal design choices and values

## References

- Mollick's X post: https://x.com/emollick/status/1952218373397647411
- Claude 4 System Card (Anthropic): https://www.anthropic.com/index/claude-4
- o4 Mini System Card (OpenAI): https://cdn.openai.com/papers/o4-mini-system-card.pdf
- Gemini 2.5 Deep Think Model Card (Google DeepMind): https://storage.googleapis.com/deepmind-media/gemini/gemini-2-5-deep-think-model-card.pdf
- EU AI Act article by author: https://hoeijmakers.net/learning-to-work-with-the-eu-ai-act/
- AI Benchmarks article by author: https://hoeijmakers.net/ai-benchmarks-and-evals/
