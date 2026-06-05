---
title: "ChatGPT Dreaming (Memory Synthesis)"
created: "2026-06-05"
updated: "2026-06-05"
type: concept
tags: [openai, chatgpt, memory-systems, personal-ai, announcement, product]
sources:
  - "raw/articles/2026-06-04_openai_chatgpt-memory-dreaming.md"
  - https://openai.com/index/chatgpt-memory-dreaming/
---

# ChatGPT Dreaming (Memory Synthesis)

ChatGPT Dreaming is OpenAI's background memory synthesis system that automatically curates and maintains user preferences, projects, and context across conversations. Announced June 4, 2026, Dreaming V3 represents the third major iteration of ChatGPT's memory architecture, graduating from a supplemental system to a standalone memory solution.

## Evolution

| Version | Date | Description |
|---------|------|-------------|
| **Saved Memories** | April 2024 | Explicit user-driven memory; user must tell ChatGPT to remember. Felt like "someone who took a few notes but forgot everything not written down." |
| **Saved Memories + Dreaming V0** | April 2025 | First background synthesis. Supplemented saved memories, offset staleness, but insufficient as standalone. |
| **Dreaming V3** | June 4, 2026 | Significantly more capable, compute-efficient, standalone memory architecture. |

## Key Architecture

- **Background process**: Learns from many conversations asynchronously, synthesizing memory state outside the chat loop
- **Automatic curation**: Does not require explicit "remember" instructions — captures context naturally from conversation
- **Compute-efficient**: New architecture specifically designed to scale to hundreds of millions of users and multi-year time horizons
- **Reviewable**: Users can see memory summaries, add/update information, and provide instructions on what topics to surface

## Evaluation Framework

OpenAI evaluates memory quality across three objectives:

1. **Carry forward useful context**: Information shared once persists across subsequent chats
2. **Follow preferences and constraints**: Stated preferences (e.g., vegetarian) influence future actions
3. **Stay current over time**: Memory accounts for passage of time (e.g., "birthday next Saturday" resolves correctly after Sunday passes)

## Rollout

- Available to Plus and Pro users in the US on June 4, 2026
- Rolling out to additional countries and Free/Go users in subsequent weeks

## Significance

Dreaming V3 addresses three core challenges with memory at scale:
- **Staleness**: Old saved memories becoming incorrect or irrelevant
- **Correctness**: Distinguishing current vs. outdated information
- **Scalability**: Maintaining coherent memory state across hundreds of millions of users

The system represents a shift from explicit, user-managed memory to automated, continuously-synthesized context — analogous to how a person naturally remembers relevant information without being told "remember this."

## Related Pages

- [[entities/openai]] — OpenAI entity
- [[concepts/chatgpt]] — ChatGPT overview
- [[concepts/llm-personalization]] — LLM personalization techniques
- [[concepts/long-term-memory-llm]] — Long-term memory in LLM systems
