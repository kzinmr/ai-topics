---
title: "thorsten-ball"
description: "Software engineer, author of Writing An Interpreter In Go and Writing A Compiler In Go, creator of Amp (AI code editor at Sourcegraph). Works at Sourcegraph on Amp."
url: https://thorstenball.com
type: entity
created: 2026-05-03
updated: 2026-05-03
aliases:
  - thorstenball
  - mrnugget
  - Thorsten Ball
  - @thorstenball
tags:
  - person
  - author
  - go
  - programming-languages
  - ai-agent
  - coding-agents
sources:
  - raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md
  - https://thorstenball.com
  - https://github.com/mrnugget
  - https://twitter.com/thorstenball
  - https://registerspill.thorstenball.com/about
---

# Thorsten Ball

**Thorsten Ball** (@thorstenball, GitHub: mrnugget) is a German software engineer, author, and occasional writer. He is best known for his two self-published books — *Writing An Interpreter In Go* (2017) and *Writing A Compiler In Go* (2018) — which are widely regarded as the most accessible practical introductions to programming languages.

He currently works remotely at **Sourcegraph** on **Amp**, an AI code editor. Previously, he worked at **Zed** (the high-performance code editor) and spent five years at Sourcegraph before that.

## Overview

Thorsten Ball lives in Großwallstadt, Bavaria, Germany. His professional career spans web technologies (Ruby, JavaScript, Go, C) and systems programming. He writes a weekly newsletter called **Register Spill** on Substack, and maintains a personal blog at thorstenball.com covering programming languages, Unix internals, and software engineering.

His technical philosophy emphasizes building from scratch with no third-party dependencies, working code as the primary artifact, and thoroughly understanding the layers of abstraction that seem like "magic."

## Books

### Writing An Interpreter In Go (2017)
A hands-on guide to building a full-fledged interpreter for the Monkey programming language from scratch. Features include: lexer, parser, AST, REPL, object system, and tree-walking evaluator. ~200 pages, all code in Go standard library only.

### Writing A Compiler In Go (2018)
The sequel, extending the Monkey interpreter into a bytecode compiler and virtual machine, achieving significant performance improvements over tree-walking evaluation.

## Current Work: Amp

Thorsten works on **Amp** (https://ampcode.com), an AI code editor built at Sourcegraph. Amp represents one of the most concrete implementations of the "minimal agent philosophy" in production — building a code-editing agent that is simple, transparent, and effective.

## Key Writings

### "How to Build a Code-Editing Agent: The Emperor Has No Clothes Guide" (April 2025)
Published on ampcode.com, this article demonstrates that a functional code-editing agent can be built in ~400 lines of Go with just three tools: `read_file`, `list_files`, and `edit_file` (via string replacement). The core thesis is that the "agent" part of an AI coding agent is trivially simple — sophistication comes from UI/UX, system prompts, and error handling.

> "300 lines of code and three tools and now you're able to talk to an alien intelligence that edits your code... That's why we think everything's changing."

## Cross-References

- [[concepts/minimal-coding-agent]] — The pattern described in his 2025 article
- [[concepts/agent-loop-orchestration]] — His implementation is a concrete Go example of the agent loop
- [[concepts/agent-harness]] — His article reinforces the "harness is the operating system" thesis
- [[concepts/harness-engineering]] — The broader umbrella concept his work exemplifies
- [[entities/sourcegraph]] — Employer and platform for Amp

## Community
- **Website**: https://thorstenball.com
- **Blog**: https://registerspill.thorstenball.com
- **GitHub**: https://github.com/mrnugget
- **X/Twitter**: https://twitter.com/thorstenball
- **Bluesky**: https://bsky.app/profile/thorstenball.com
- **Mastodon**: https://mastodon.social/@mrnugget
