---
title: Aditya Bawankule
created: 2026-05-10
updated: 2026-05-11
type: entity
tags:
  - person
  - blogger
  - developer-tooling
  - coding-agents
  - methodology
aliases:
  - legorobotdude
  - Aditya Bawankule
description: "AI-native software engineer, Ex-Meta (Supernatural VR), founder of AIdea Hub, and technical blogger covering AI coding agents (Claude Code, Codex, Cursor), meta-prompting, and developer tooling."
sources:
  - https://www.adityabawankule.io/
  - https://www.adityabawankule.io/resume
  - https://www.linkedin.com/in/aditya-bawankule/
  - https://github.com/Legorobotdude
  - https://www.adityabawankule.io/blog/codex-goal-meta-prompting
  - https://www.adityabawankule.io/blog/claude-code-vs-codex-vs-cursor
related:
  - "[[concepts/codex-goal-meta-prompting]]"
  - "[[concepts/gpt/codex-superapp]]"
  - "[[entities/claude-code]]"
---

# Aditya Bawankule

**Aditya Bawankule** (@legorobotdude) is an AI-native software engineer, Ex-Meta engineer, and technical blogger based in the Greater Seattle Area. He writes about AI coding agents (Claude Code, Codex, Cursor), meta-prompting techniques, and developer tooling at [adityabawankule.io](https://www.adityabawankule.io/).

## Overview

Aditya earned a BS in Computer Engineering from the **University of Illinois Urbana-Champaign** (2017–2021), where he was President of Gamebuilders ACM UIUC and conducted VR research at UIUC VERL. After graduation, he worked at State Farm as a Software Engineer before joining **Meta** (2022–2024), where he worked on the **Supernatural VR** fitness app for Meta Quest using C# and Unity3D.

Following his tenure at Meta, Aditya founded **AIdea Hub**, a SaaS platform for AI-powered ideation and research, and served as CTO of **MOSAiC** (AI-driven personalized learning platform) and **Launch99 Agency**. He currently works at **Certivo** as a Full Stack AI Software Engineer (since Dec 2025).

Aditya's blog at adityabawankule.io is a hands-on guide to AI-assisted software development in 2026, grounded in daily-production usage of Claude Code, Codex, and Cursor. His writing is characterized by **pragmatic tool comparisons**, **meta-prompting techniques**, and **first-principles analysis** of AI coding workflows.

## Notable Content

### Codex /goal Meta-Prompting (May 4, 2026)
Pioneered a technique of using a second AI to generate high-quality `/goal` prompts for OpenAI Codex, enabling days of autonomous work. The method: open an AI session with project context, ask it to research /goal's actual behavior, inspect the codebase for high-leverage missions, and produce three complete /goal prompts with scope, constraints, files, and definitions of done. → [[concepts/codex-goal-meta-prompting]]

### Claude Code vs Codex vs Cursor Comparison (Feb 21, 2026)
A detailed, daily-user comparison of the three major AI coding tools. Key findings:
- **Claude Code**: Best for fast iteration, front-end work, conversational debugging (daily driver)
- **Codex**: Best for back-end work, complicated multi-file tasks, async autonomous missions
- **Cursor / AntiGravity**: Best as IDE shell around agents, not as primary coding tool
- **Practical rule**: "Claude Code for when you want slop fast, Codex for when you want something done right"

### AI Coding Tool Philosophy
Aditya documents a consistent observation across Anthropic products: "They're all extremely buggy because they're all written by Claude Code. However, they also have the latest and greatest features way before anyone else because of the speed they're able to achieve with Claude Code." He uses Claude Code + Codex as dual daily drivers, with AntiGravity or Cursor as the IDE wrapper for file viewing and terminal management.

## Projects

### VibeCoder (PrivateCode)
A terminal-based coding assistant that uses local LLMs via Ollama to provide coding help while maintaining privacy. Supports web search, file editing, and command execution with user confirmation. 32 stars, 7 forks on GitHub. [vibecoder.gg](https://www.vibecoder.gg/)

### DreamPixelForge
A modern GUI for running multiple AI image generation models (Stable Diffusion 2.1, Dreamlike Diffusion, Kandinsky 2.2) locally. Features LLM-enhanced prompting, app icon generation, and post-processing. 6 stars. [dreampixelforge.com](https://www.dreampixelforge.com/)

### AIdea Hub
A SaaS platform for AI-powered ideation and research, built with OpenAI ChatGPT, Google Gemini, Firebase, and Perplexity AI. [aideahub.ai](https://www.aideahub.ai/)

### NeuroNav
An AI companion for ADHD brains — a productivity app rethinking task management for neurodivergent users (May 2025).

### Testimonial Genius
An AI-powered tool that turns raw customer testimonials into categorized, marketing-ready quotes with sentiment analysis (built in 3 days, Apr 2025).

## Writing Style & Philosophy

Aditya's writing is characterized by:
- **First-principles comparisons**: Side-by-side evaluation of AI coding tools based on daily production usage, not benchmarks
- **Pragmatic meta-layer thinking**: Recognizes that prompt engineering is being replaced by meta-prompting ("the model is better at structuring instructions for itself than you are")
- **Tool-agnosticism**: Recommends specific tools for specific jobs rather than advocating a single ecosystem
- **Production grounding**: Claims backed by shipped projects and real adoption patterns (e.g., Claude Code's speed advantage despite bugginess)

## Cross-References

- [[concepts/codex-goal-meta-prompting]] — His most influential technique: using AI to write better /goal prompts
- [[concepts/gpt/codex-superapp]] — Broader context of Codex as a coding superapp
- [[entities/claude-code]] — His primary daily driver coding tool
- [[concepts/vibe-coding]] — The broader paradigm his work exemplifies
- [[entities/simon-willison]] — Similar style of tool-agnostic, production-grounded writing

## References

- [Aditya Bawankule's Blog](https://www.adityabawankule.io/)
- [Codex /goal Meta-Prompting Article](https://www.adityabawankule.io/blog/codex-goal-meta-prompting)
- [Claude Code vs Codex vs Cursor Comparison](https://www.adityabawankule.io/blog/claude-code-vs-codex-vs-cursor)
- [GitHub: Legorobotdude](https://github.com/Legorobotdude)
- [LinkedIn](https://www.linkedin.com/in/aditya-bawankule/)
