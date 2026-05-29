---
title: "a1zhang RLM Clarification: What RLM Is and Is Not"
source: https://x.com/a1zhang/status/2060122034194002097
author: a1zhang (Alex Zhang)
author_handle: "@a1zhang"
author_affiliation: MIT CSAIL PhD Student
date: 2026-05-28
type: x_note_tweet
tags: [rlm, recursive-language-models, claude-code, dynamic-workflows, context-decomposition, subagents, programmatic-sub-agent-calling]
metrics:
  likes: 227
  bookmarks: 46
  retweets: 3
  replies: 5
  quotes: 2
  impressions: 9275
conversation_with: jxmnop
---

# Author's Clarification: What RLM Is and Is Not

In response to criticism from @jxmnop (May 28, 2026), Alex Zhang published a detailed clarification of what the Recursive Language Models (RLM) paper does and does not claim.

## What RLM Does NOT Claim

1. The paper doesn't claim it's the first to explore an LM talking to an LM
2. The paper doesn't claim it's the first to explore sub-agents
3. The paper doesn't claim it's the first to argue for CodeAct-style execution
4. The paper doesn't claim it's the first to propose recursion with respect to an LM
5. The paper doesn't claim to be the first to propose any of the independent features that make an RLM (context offloading, PTC, etc.)

## What Makes RLM Unique

> "All of the ideas that make up an RLM are somewhat intuitive and implemented in various ways, many with little success. **The composition of them, and the lack of a need for any more, is what makes it unique.**"

The key insight: individual components (context offloading, sub-agents, CodeAct, recursion) have all been explored before. The novelty is in **which specific components are composed, and the argument that no additional components are needed** for robust long-context reasoning.

## RLM as a Normative Argument

Zhang reframes RLM beyond a technical contribution:

> "The paper is an argument for exactly the type of abstractions one should define to better enable a sub-agent calling system (i.e. context offloading, CodeAct-style execution, programmatically sub-agent calling)."

This is a **normative claim** — RLM doesn't just describe a technique, it argues for *what abstractions matter* in agent design.

## The Blurring Line Between Sub-Agent System and Language Model

> "It also argues that the line between a sub-agent calling system and a 'language model' is blurry, and that a well-designed, general enough abstraction yields a meaningful 'language model'."

This is a philosophical claim: when a scaffold is sufficiently well-designed and general, the distinction between "the model" and "the system calling the model" dissolves. A good enough abstraction layer makes the system behave as if it were a more capable model.

## Claude Code's Evolution Toward RLM

> "The last few releases in Claude Code have moved away from standard ReAct-style loops with JSON tool-calling to more of this abstraction. The recent release is very exciting to me (and why I talk about it being RLM-like) because a lot of the abstractions we've been arguing for are emerging in frontier lab systems."

Zhang sees Claude Code's Dynamic Workflows as **empirical validation** of the RLM thesis — not that Anthropic "copied RLM," but that frontier engineering is converging on the same abstractions that RLM formalized from first principles.
