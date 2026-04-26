---
title: "Salvatore Sanfilippo (antirez)"
tags: [- person]
created: 2026-04-24
updated: 2026-04-24
---

# Salvatore Sanfilippo (antirez)

**URL:** https://antirez.com
**Blog:** antirez.com
**Twitter/X:** @antirez
**GitHub:** antirez
**Projects:** Redis, linenoise, kilo, voxtral.c, SDS, Rax

## Overview

Salvatore "antirez" Sanfilippo is one of the most influential systems programmers of the modern era. He created Redis in 2009, which became one of the most widely deployed in-memory data stores in the world. His work is defined by a philosophy of radical simplicity — a belief that the best systems are small, readable, and built with taste rather than bureaucracy.

He left Redis Labs in 2020 to write a novel about AI and universal basic income, then returned to the Redis project in December 2024. His blog at antirez.com has been publishing since the mid-2000s, covering systems programming, open-source philosophy, AI, and software craft. More recently, he has become one of the most thoughtful and nuanced voices on AI-assisted programming — simultaneously embracing LLMs as transformative tools while warning against the degradation of software quality and maintainer burnout.

His 2025 project voxtral.c — a bare-metal, pure-C implementation of a multimodal vision-language model running on CPU without GPUs — extends his tradition of building educational, readable implementations of complex systems.

## Timeline

| Date | Event |
|------|-------|
| 2009 | Created Redis as an in-memory key-value store with persistent storage |
| 2010 | Published the Redis Manifesto — a seven-point philosophy of simplicity, joy, and anti-complexity |
| 2011 | Left VMware to join Redis Labs as the project's primary maintainer |
| 2013 | Created linenoise, a minimal readline replacement in ~400 lines of C |
| 2014 | Created kilo, a text editor in ~1,000 lines of C, as a teaching tool |
| 2017 | Redis adopts the module system — a democratic way to extend functionality without bloating core |
| 2020 | Left Redis Labs and Redis maintenance to focus on family and creative projects |
| 2020 | Began writing a novel about AI, universal basic income, and post-automation society |
| 2024 | Published "Don't fall into the anti-AI hype" — nuanced examination of AI's transformative impact on programming |
| 2024 | Returned to Redis as part of the Redis company's engineering team (December 2024) |
| 2025 | Released voxtral.c — pure-C implementation of Mistral Pixtral 12B multimodal model running on CPU |
| 2025 | Published "Automatic Programming" — reframing AI-assisted coding as a fundamental shift in how software is built |
| 2026 | Published "Implementing a clear room Z80 / ZX Spectrum emulator with Claude Code" — documenting AI pair programming in practice |
| 2026 | Published "Redis patterns for coding" — documentation resource for LLMs and humans alike |
| 2026 | Published "GNU and the AI reimplementations" — drawing parallels between GNU's clean-room UNIX rewrites and today's AI-generated code |
| 2026 | Published "AI cybersecurity is not proof of work" — argues model intelligence, not GPU scale, wins in cybersecurity
| 2026 | Published "First Token Cutoff LLM sampling" — critiques nucleus sampling (top-p) and proposes a new algorithm to avoid selecting suboptimal tokens that push generation toward hallucination |

## Core Ideas

### Radical Simplicity as a Design Philosophy

Sanfilippo's approach to software is defined by an almost artistic minimalism. The Redis Manifesto declares: "Code is like a poem; it's not just something we write to reach some practical result." This isn't aesthetic indulgence — it's a rigorous engineering stance. He believes that complexity is a form of lock-in: code that is too complex to understand cannot be maintained, forked, or improved by others.

> "We're against complexity. We believe designing systems is a fight against complexity. We'll accept to fight the complexity when it's worthwhile but we'll try hard to recognize when a small feature is not worth 1000s of lines of code."

His projects kilo (~1,000 lines) and linenoise (~400 lines) embody this philosophy — complete, functional tools that fit in a single file and can be read and understood by a single developer in an afternoon.

### Memory Storage Is #1

The Redis Manifesto's second principle establishes that Redis's primary data store is memory, not disk. This wasn't a technical accident but a philosophical choice: memory is fast, simple, and predictable. By keeping the core dataset in RAM, Redis avoids the complexity layers that disk-based databases need (buffer pools, page caches, write-ahead logs as primary mechanisms). Persistence becomes an optional feature layered on top, not the foundation.

### The DSL for Abstract Data Types

Sanfilippo designed Redis as a domain-specific language that manipulates abstract data types through a simple TCP protocol. Each data type (strings, lists, sets, sorted sets, hashes, streams, bitmaps) is an abstraction over a fundamental data structure with known time and space complexity. The API is deliberately minimal and direct — "forcing the application layer to make meaningful choices" rather than pretending to be a magical object that organizes data for you.

This approach rejects the "do everything" database paradigm. Redis is not trying to replace relational databases or document stores; it provides a small set of composable primitives that, when combined correctly, solve a vast range of problems.

### Opportunistic Programming

The Redis Manifesto's tenth point defines "opportunistic programming": trying to get the most for the user with minimal increases in complexity. "Solve 95% of the problem with 5% of the code when it is acceptable." This is the engineering equivalent of the Pareto principle applied with intention — recognizing that most of the value comes from a small core, and resisting the urge to chase edge cases at the cost of system complexity.

### We Optimize for Joy

Perhaps the most human principle in the Redis Manifesto: "We believe writing code is a lot of hard work, and the only way it can be worth is by enjoying it. When there is no longer joy in writing code, the best thing to do is stop." Sanfilippo left Redis in 2020 not because the project was failing but because maintaining it was no longer bringing him joy. His return in 2024 was motivated by a renewed sense of purpose — applying AI to his Redis workflow and exploring new frontiers.

### AI as Automatic Programming — Not Vibe Coding

Sanfilippo has been one of the most thoughtful and nuanced voices on AI-assisted programming. In "Don't fall into the anti-AI hype" (January 2026), he distinguished between passive "vibe coding" (generating code without understanding it) and "automatic programming" (using AI as a powerful partner while maintaining architectural oversight):

> "Please, stop saying 'Claude vibe coded this software for me'. Vibe coding is the process of generating software using AI without being part of the process at all."

He argues that AI is not replacing programmers — it's changing what programmers do. The valuable skill shifts from typing code to understanding systems, designing architectures, and directing AI agents with precision. His own workflow now involves using Claude Code to fix transient test failures, generate C libraries, and implement complex algorithms — tasks that would have taken days now take hours.

### The Historical Parallel: GNU and AI Reimplementations

In "GNU and the AI reimplementations" (March 2026), Sanfilippo drew a powerful parallel between the GNU Project's clean-room reimplementation of UNIX in the 1980s-90s and today's AI-generated rewrites of existing software:

> "Those who cannot remember the past are condemned to repeat it. A sentence that I never really liked, and what is happening with AI, about software projects reimplementations, shows all the limits of such an idea."

His argument is that criticizing AI-generated rewrites while historically supporting clean-room reimplementation is inconsistent. Both are valid approaches to building software; the question is whether the result is correct and useful, not whether it was written by a human or a machine.

### Democratizing Knowledge

Sanfilippo feels "great to be part of" the training data that LLMs ingest, because he sees this as "a continuation of what I tried to do all my life: democratizing code, systems, knowledge." His projects have always been designed to be readable, educational, and accessible. voxtral.c follows the lineage of Karpathy's llama2.c — demonstrating that the fundamental algorithms of cutting-edge AI can be understood by anyone who reads the code, without the obscuring layers of production frameworks.

### Commenting as Analysis

His approach to code comments is distinctive and systematic. He categorizes comments into types: Checklist, Guide, Teacher, Why, Design, and Function — and discards Backup, Debt, and Trivial comments. Every non-trivial function should be explainable in 2-3 sentences that "feel obviously true." Comments are a tool for rubber-duck debugging: if you can't explain the code clearly, it's not ready to commit.

### Data-Structure-Driven Design

Sanfilippo crafts his own data structures (SDS for strings, Rax for radix trees) rather than relying on generic libraries. He believes in sketching data structures on paper before writing code, and that the right data structure makes the right algorithm obvious. This connects to his broader philosophy: understand the fundamentals, build from first principles, and don't accept complexity as inevitable.

## Key Quotes

> "We're against complexity. We believe designing systems is a fight against complexity."

> "Code is like a poem; it's not just something we write to reach some practical result."

> "We optimize for joy. When there is no longer joy in writing code, the best thing to do is stop."

> "Please, stop saying 'Claude vibe coded this software for me'. Vibe coding is the process of generating software using AI without being part of the process at all."

> "LLMs are going to help us to write better software, faster, and will allow small teams to have a chance to compete with bigger companies. The same thing open source software did in the 90s."

> "I feel great to be part of that [training data], because I see this as a continuation of what I tried to do all my life: democratizing code, systems, knowledge."

> "Those who cannot remember the past are condemned to repeat it. A sentence that I never really liked, and what is happening with AI, about software projects reimplementations, shows all the limits of such an idea."

> "Writing code is no longer needed for the most part. It is now a lot more interesting to understand what to do, and how to do it."

> "I believe neural networks, at their core, are a continuation of the same intellectual tradition that produced Redis: building simple, elegant systems that solve real problems."

> "The Redis API has two levels: a subset that fits naturally into a distributed version, and a more complex API for multi-key operations. We don't want to provide the illusion of something that will work magically when actually it can't in all cases."

## Recent Themes (2024–2026)

- **AI-assisted programming**: Using Claude Code and other LLM agents as collaborative tools for real systems programming tasks
- **Bare-metal AI**: voxtral.c demonstrates that complex AI models can be implemented in readable, dependency-free C
- **Open-source licensing pragmatism**: Not an absolutist — sees licensing as a spectrum and understands the economic realities of sustaining large projects
- **Comment quality and code readability**: Systematic approach to documentation as an analysis tool
- **Historical consciousness**: Drawing parallels between GNU's clean-room rewrites and AI-generated reimplementations
- **LLM sampling research**: Investigating token probability distributions, critiquing nucleus sampling, and proposing first-token cutoff methods to reduce hallucination risk
- **Joy-driven development**: Left and returned to Redis based on whether the work brought fulfillment

## Related Concepts

- [[redis]] — His defining creation, the in-memory data store
- [[systems-programming]] — His domain of expertise: C, memory management, performance
- [[software-simplicity]] — His core design philosophy
- [[ai-assisted-development]] — His nuanced position on LLMs as programming partners
- [[open-source-licensing]] — His pragmatic view of sustainability and community
-  — SDS, Rax, and the philosophy of building from first principles
-  — Using documentation as an analytical tool
-  — His distinction between passive and active AI-assisted coding

## Influence Metrics

- Redis: ~65K+ GitHub stars, one of the most deployed databases in the world
- linenoise: ~3K+ stars, the minimal readline replacement used across the C ecosystem
- kilo: ~5K+ stars, the educational text editor that inspired a generation of minimal projects
- voxtral.c: Rapid adoption and discussion in the systems programming community
- His blog is consistently cited as one of the most thoughtful technical blogs in the industry
- The Redis Manifesto remains one of the most referenced design documents in open-source software
- "Don't fall into the anti-AI hype" sparked widespread discussion about the future of programming


### AI Cybersecurity: Not Proof of Work

2026年4月、antirezはAIとサイバーセキュリティの関係について新しい洞察を発表。

#### Proof of Workとの違い
- **PoW**: ハッシュ衝突探索は指数関数的に困難だが、十分な作業で必ず発見可能
- **バグ発見**: コードの状態空間が飽和すると、発見率は「M（試行回数）」ではなく「I（モデルの知性レベル）」で制限される

#### OpenBSD SACKバグの事例
- 弱いモデルを無限に実行しても、真のバグ（開始ウィンドウ検証欠如 + 整数オーバーフロー + NULL分岐）を発見できない
- 弱いモデルは幻覚（hallucination）で「たまたま」正しいバグを指摘することはあるが、真の理解ではない
- **強いモデルほど幻覚が少ない**ため、中間レベルのモデルが最も「バグを発見したフリ」をしにくい

#### 明日のサイバーセキュリティ
> 「より多くのGPUが勝つ」のではなく、「より良いモデル、より早いアクセス」が勝つ

#### 意義
- AIセキュリティ競争は計算量の競争ではなく知性の競争
- Mythos（Anthropicのセキュリティ特化モデル）のような高知性モデルが既存のバランスを崩す可能性
- セキュリティ監査におけるAIの役割再定義が必要

