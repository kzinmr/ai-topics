---
title: "Physical Superintelligence — Aaronson–Ambainis Conjecture Proof"
created: 2026-11-10
updated: 2026-11-10
type: concept
tags:
  - ai-in-science
  - formal-verification
  - mathematics
  - quantum-computing
  - company
  - frontier-models
  - research
sources:
  - raw/newsletters/2026-11-09-import-ai-480-self-sustaining-space-economies-ai-for-science-progress-and-meta-b.md
  - https://importai.substack.com/p/import-ai-480-self-sustaining-space
---

# Physical Superintelligence — Aaronson–Ambainis Conjecture Proof

**Physical Superintelligence (PSI)** is an AI-science startup whose internal research system proved the **Aaronson–Ambainis conjecture**, a question about when quantum computers can be exponentially faster than classical ones that had been open **since 2008** (Scott Aaronson & Andris Ambainis). Jack Clark presented it in **Import AI 480** (Nov 9, 2026) as "an evocative taste of the singularity."

## What happened

- The proof was found by a **research system developed internally at PSI**, running a **non-public Anthropic model** — i.e. a closed frontier model used as the reasoning engine inside a third-party automated-research harness, rather than a lab's own internal system.
- The system had a **complete proof by the third day of the run**, and **Lean** — an interactive proof assistant in which a computer checks every inference step — **accepted it**.
- The team then pointed the same system at **related open problems**; along the way it **improved its own result twice**, and Lean accepted the final version. Iterative self-improvement of a verified artifact, not a one-shot answer.

## Why it matters

Two properties make this more than another "AI solved a math problem" headline:

1. **Machine-verifiable closure.** Lean acceptance removes the usual dispute about whether an LLM produced a plausible-looking argument. The epistemic status is "checked", not "reviewed by humans who might have skimmed". This is the concrete instantiation of the **fast, precise verifier** condition that [[concepts/recursive-self-improvement]] identifies as the prerequisite for productive self-improvement loops — here applied to pure mathematics rather than code.
2. **A third party, not a frontier lab, did it with a lab's model.** It is an early example of the **automated-research layer separating from model development** — the "mostly automated synthetic researchers extending the frontier of knowledge" framing Clark has used since his IMF speech (see [[entities/jack-clark]]). The adjacent wiki instance of the same pattern is Anthropic's own Jacobian-conjecture work ([[concepts/claude-fable-jacobian-conjecture]]); PSI's result is a non-lab replication of that capability using a non-public Anthropic model.

Clark's own framing is deliberately strong — he reads it as evidence we are inside "the singularity", defined as the period when the rate of scientific progress exceeds the rate at which humans can parse and absorb it, so results arrive faster than they can be understood.

## Related

- [[concepts/recursive-self-improvement]] — verifier availability as the enabler of self-improvement loops
- [[concepts/claude-fable-jacobian-conjecture]] — the lab-side precedent for LLM-proved conjectures
- [[entities/jack-clark]] — Import AI 480, the primary reporting
- [[entities/anthropic]] — provider of the non-public model
- [[concepts/open-science]] — the proof was announced via a company blog rather than a venue

## Sources

- Jack Clark, ["Import AI 480: Self-sustaining space economy"](https://importai.substack.com/p/import-ai-480-self-sustaining-space), Nov 9, 2026 — quoting Physical Superintelligence, "A proof of the Aaronson–Ambainis conjecture" (PSI blog).
