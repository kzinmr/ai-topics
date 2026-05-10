---
title: Codex /goal Meta-Prompting
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [coding-agents, openai, prompting, agentic-engineering]
aliases: [/goal meta-prompting, Codex goal prompting]
sources:
  - raw/articles/2026-05-04_adityabawankule-codex-goal-meta-prompting.md
---

# Codex /goal Meta-Prompting

A technique for writing high-quality prompts for OpenAI Codex's `/goal` command by using a second AI session to generate the mission prompt — **meta-prompting** (an AI writing a prompt for another AI).

> "Hand-written prompts are a relic. If you're still manually writing /goal prompts, you're leaving most of the capability on the table." — [[entities/aditya-bawankule|Aditya Bawankule]]

## What Is Codex /goal?

`/goal` is a slash command in the Codex CLI (shipped in v0.128.0) that turns Codex into a **long-horizon autonomous agent**. Unlike a normal prompt that runs a few turns and stops, `/goal` sets up a persistent objective. Codex keeps iterating across many cycles of plan → act → verify → correct for **hours** of continuous work in a single invocation.

Enable via: `codex features enable goals`

## The Problem: Hand-Written Prompts Compounded

The prompt after `/goal` does most of the work, but humans consistently:
- Underestimate what the agent needs to know to stay on track without supervision
- Leave out constraints, acceptance criteria, and architectural assumptions
- Write as if they'll be in the loop — but `/goal` is autonomous

These gaps compound over the long horizon, burning agent cycles on the wrong things.

## Meta-Prompting Technique

1. **Open a second AI session** with repo context (ChatGPT, Claude, or another Codex window)
2. **Instruct it to research /goal**: "look up how /goal actually works in the Codex CLI"
3. **Have it analyze your codebase**: "walk through this codebase and pick the three highest-leverage missions"
4. **Get complete prompts**: "scope, constraints, files in play, definition of done, checks before mission complete"
5. **Pick and paste**: Choose the option matching your actual goal, paste after `/goal`

## Why Meta-Prompting Works

Writing prompts is itself a skill LLMs can do better than humans with context. The AI:
- Knows what instructions agents respond to
- Identifies edge cases humans miss
- Phrases acceptance criteria so they don't get reinterpreted mid-run

This aligns with a broader pattern: **the model is better at structuring instructions for itself than you are at structuring instructions for the model**.

## Use Cases

`/goal` excels on missions with a clear definition of done and significant mechanical work:
- Migrating a codebase (e.g., Python 2 → 3, REST → GraphQL)
- Refactoring a subsystem end-to-end
- Building features touching many files
- Upgrading dependencies across a monorepo

## Related Concepts

- [[concepts/openai-codex-superapp]] — Codex as primary ChatGPT interface
- [[concepts/agent-harness-comparison]] — Comparison of Codex with other agent harnesses
- [[concepts/vibe-coding-vs-agentic-engineering]] — Where /goal fits in the coding spectrum
