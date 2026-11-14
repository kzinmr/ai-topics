---
title: "AI Education"
type: concept
aliases:
  - ai-education
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - education
  - ml-education
  - ai-educator
sources:
  - wiki/concepts/cs231n.md
  - wiki/concepts/stanford-cs336-language-modeling-from-scratch.md
  - wiki/concepts/llm-assisted-learning.md
---

# AI Education

**AI education** covers how people actually learn machine learning and LLM engineering — from university courses to open online curricula — and, since 2023, how AI itself is reshaping learning. Two threads run through this page: the **canon of teaching artifacts** and the **AI-as-tutor disruption**.

## The Canonical Curriculum (2010s → 2020s)

| Artifact | Author/Institution | Why it anchors the canon |
|----------|--------------------|--------------------------|
| **cs231n** | Stanford ([[concepts/cs231n]]) | The visual-ML pedagogy lineage; Karpathy-era assignments → [[concepts/micrograd]]/[[concepts/nanogpt]] |
| **CS336 Language Modeling from Scratch** | Stanford ([[concepts/stanford-cs336-language-modeling-from-scratch]]) | The LLM-era successor: build/tokenize/pretrain/align a model end-to-end |
| **Neural Networks: Zero to Hero** | Andrej Karpathy ([[concepts/karpathy]]) | Micrograd → nanogPT video series; "what you can't build you don't understand" pedagogy |
| **Deep Learning Specialization / AI for Everyone** | Andrew Ng ([[entities/andrew-ng]], [[entities/deeplearning-ai]]) | MOOC-era mass education; DeepLearning.AI became the AI-courses platform |
| **fast.ai** | Jeremy Howard | Top-down, code-first counterpoint to bottom-up math curricula |
| **Sebastian Raschka's LLMs-from-scratch + Ahead-of-AI newsletter** | [[entities/sebastian-raschka]] | Bridge from PyTorch fundamentals to LLM internals |
| **3Blue1Brown neural-net series** | Grant Sanderson ([[entities/grant-sanderson-3blue1brown]]) | Visual intuition standard everyone cites |
| **Hamel Husain's full-stack LLM/agent courses** | [[entities/hamel-husain]] | The practitioner-standard agent-evaluation and fine-tuning curriculum |
| **LLM course roadmaps** | community ([[concepts/llm-course-roadmap]]) | Meta-curricula organizing the above |

A consistent pattern: **each generation's pedagogy is "build the thing from scratch"** — micrograd/nanoGPT replaced MNIST notebooks the way fast.ai replaced MATLAB assignments.

## AI as Teacher (and Its Limits)

- **LLM-assisted learning** ([[concepts/llm-assisted-learning]]): tutoring gains (Khanmigo-style Socratic tutors, Duolingo Max) vs metacognitive outsourcing.
- **Cognitive deskilling**: the dark mirror — [[concepts/sre-deskilling]] and [[concepts/cognitive-debt]] document how AI dependence erodes the very skills training aimed to build; the education system hasn't settled whether AI is a calculator or a crutch.
- **Vibe-learning**: LLM-paired programming instruction inverts the old order — learners prompt first, understand later ([[concepts/vibe-coding]]), raising "legible work" questions about what counts as competence.
- **Credential disruption**: [[entities/learnvector]] and cohort models ([[concepts/cohort-based-learning]]) pressure the university monopoly; Anthropic/OpenAI run their own academies and certifications.

## Open Questions the Wiki Tracks

1. Does from-scratch pedagogy still matter when frontier labs are un-reimplementable? (CS336's answer: scale down, keep every layer.)
2. Can LLM tutors be *verified* tutors — evaluation for education lags classroom adoption (evaluation for education lags classroom adoption).
3. Who accredits AI competence as it becomes a general worker skill?

## Related Concepts

- [[concepts/karpathy]] — the archetypal AI educator-engineer
- [[concepts/cs231n]] / [[concepts/computer-science-education]] — institutional lineage
- [[concepts/llm-assisted-learning]] — the AI-as-tutor thread
- [[concepts/harness-engineering]] — the new practical skill layer being taught

## Sources

- Synthesized from existing wiki pages: cs231n, stanford-cs336, karpathy, andrew-ng, deeplearning-ai, sebastian-raschka, hamel-husain, learnvector, llm-assisted-learning, cohort-based-learning (2026)
