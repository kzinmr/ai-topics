---
title: "\"Determinism\" is the Biggest Cope in AI Adoption"
source: "https://leehanchung.github.io/blogs/2026/04/07/determinism-biggest-cope-in-ai-adoption/"
author: "Hanchung Lee (Han Lee)"
date: 2026-04-07
type: article
tags: [determinism, ai-adoption, evaluation, software-reliability, llm-evaluation, six-sigma]
---

# "Determinism" is the Biggest Cope in AI Adoption

> "We've never had determinism in software. We just had the illusion of it."

## The Mathematical Impossibility of Perfect Software

- **Halting Problem** (Turing, 1936): No program can verify whether another program will even finish running.
- **Rice's Theorem** (Rice, 1953): It is mathematically impossible to build a tool that can verify any meaningful property of software in the general case.

> "This means 'make sure it doesn't make a mistake' software was never a guarantee anyone could offer. Every piece of software you trust today shipped with that same uncertainty."

## Determinism ≠ Correctness

A deterministic program that returns the **wrong answer** returns it every single time. That's a bug, not a baseline expectation.

## The Six Sigma Parallel

Manufacturing figured this out decades ago. Six Sigma doesn't demand zero defects — it defines an acceptable defect rate and builds measurement systems to stay within that bound. The discipline was never "eliminate all variation." It was "define, measure, analyze, improve, control" — continuously reducing variation. That's **evaluation**, not determinism.

## What AI Systems Actually Shift

The work moves from pre-deployment code verification to **continuous evaluation**. Instead of "does this code path execute as specified," you ask "does this output meet our evaluation criteria."

> "In AI and machine learning systems, we reduce entropy (chaos) through evaluation."

## Reliable Systems from Unreliable Components

This is not new. TCP connects on unreliable networks. RAID clusters operate on top of failing drives. AI models are trained on failing GPUs. We've always built reliable systems from unreliable components.

> "It was never about determinism. It was always about evaluations."
