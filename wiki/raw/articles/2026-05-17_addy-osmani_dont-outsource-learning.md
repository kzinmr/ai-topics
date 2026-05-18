---
source: https://addyosmani.com/blog/dont-outsource-learning/
title: "Don't Outsource the Learning"
author: "Addy Osmani"
date: 2026-05-17
type: x_article
x_article_title: "Don't Outsource the Learning"
tags: [ai-assistance, coding-agents, software-engineering, methodology, cognition, education, cognitive-debt]
---

# Don't Outsource the Learning

**Author:** Addy Osmani
**Published:** May 2026
**Source:** https://addyosmani.com/blog/dont-outsource-learning/

## Summary

Addy Osmani argues that AI coding tools are optimized for closing tasks, not for helping engineers grow. The default loop — paste a spec, get a fix, ship — quietly erodes deep understanding. Across thousands of small interactions, "what you can actually build without an AI looking over your shoulder gets a little weaker every week." This is **cognitive surrender**: the AI's verdict replaces your own judgment.

## Core Thesis

The tools won't force us to learn — that part has to come from the engineer. The difference between using AI to learn vs. using AI to skip learning is **posture**: forming a hypothesis first, asking for explanation before code, and turning on Learning Mode. The same tools that cause cognitive debt can build sharper engineers — but only if you deliberately use them that way.

## Research Findings

### 1. Anthropic Randomized Trial (early 2026)
- Engineers learned a new Python library, half with AI assistance, half without.
- Both groups finished tasks at the **same speed**.
- Comprehension quiz: AI group **50%** vs manual group **67%**. Gap widened on debugging.
- Within the AI group: conceptual questioners scored **>65%**, copy-pasters scored **<40%**.
- **"The tool didn't determine the outcome. The posture did."**

### 2. MIT "Your Brain on ChatGPT" Study
- Compared essay writing: LLM vs search-engine vs brain-only.
- EEG: brain connectivity scaled down with every layer of external support. LLM group weakest coupling.
- **83% of LLM users couldn't quote a single line** of what they produced.
- Researchers coined **"cognitive debt"**: saving mental effort today, paying in critical thinking tomorrow.

### 3. CHI 2026 — Anchoring Effect
- LLM access at task start → model framed the entire problem.
- Even when humans did the rest independently, initial framing produced **measurably worse decisions**.
- **Order of operations matters more than total AI usage.**

## Learning-Focused Features

- Anthropic's **Learning Mode** (Socratic questioning, asks you to write code before continuing)
- OpenAI's **Study Mode**, Google's **Guided Learning**
- Almost nobody uses them for production work — filed under "for students"
- Osmani argues this is a mistake: same feature helps both a sophomore learning React and a senior engineer learning Rust

## When Delegation Is Fine

- Boilerplate, glue code, throwaway CI scripts
- The opportunity cost of memorizing YAML syntax is too high
- But for anything you'll need to debug, maintain, or build upon: learn it

## Five Scenarios Where Pure Delegation Breaks Down

1. **When something breaks** — "The agent wrote it" doesn't help debug.
2. **When it's confidently wrong** — Hallucinations require expertise to spot.
3. **When the foundation changes** — Frameworks update, security reviews trigger structural issues.
4. **When you leave the median** — AI excels at common problems; hard, undocumented ones need deep expertise.
5. **When the market adjusts** — Junior dev employment dropped 20% since 2022. Engineers who can only ship with AI are entering a labor pool re-pricing expertise.

## Actionable Strategies

- **Form a hypothesis before asking** — Write 2-3 sentences on what you think the problem is. Use the model's answer to test your theory.
- **Ask for explanation before code** — "Explain how this works, what the alternatives are, and the tradeoffs." Then ask for code.
- **Turn on Learning Mode when out of your depth**
- **Two metrics, not one** — Ship and learn are separate. Managers only ask about the first. The second is on you.

## Bottom Line

> "I'd rather ship 80% of what I could have and learn 100% of what I needed to, than the reverse. Over years, those two strategies produce very different engineers."
