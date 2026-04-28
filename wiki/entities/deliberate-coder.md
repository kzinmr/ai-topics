---
title: "Deliberate Coder"
tags: [person]
created: 2026-04-24
updated: 2026-04-24
type: entity
---


# Deliberate Coder

**URL:** https://www.benmvp.com (blog), https://github.com/benmvp (GitHub)  
**Blog:** Ben Ilegbodu (benmvp)  
**Identity:** Ben Ilegbodu — Principal Frontend Engineer, developer educator, AI methodology thought leader  
**Active:** 2010s–present  
**Themes:** Deliberation-first coding, AI-assisted development, frontend architecture, CSS, JavaScript, React, accessibility, developer productivity  

## Overview

**Deliberate Coder** is a programming methodology pioneered by **Ben Ilegbodu** (known online as "benmvp"), a Principal Frontend Engineer and developer educator who has spent years refining an approach he calls **"deliberation-first coding."** The methodology is a structured alternative to the "vibe coding" trend — instead of prompting an AI agent, reviewing its output, and iterating through multiple write-review-fix cycles, Ilegbodu front-loads the deliberation: having a structured conversation with the AI agent about architecture, constraints, patterns, and goals before any code is written.

The concept emerged from Ilegbodu's frustration with the inefficiency of traditional AI-assisted workflows. After experiencing rounds of "no, that's not what I meant" with AI-generated code, he developed a formalized process that treats the AI as a collaborator in a structured design conversation rather than a code generator to be corrected after the fact.

Ilegbodu formalized this methodology into a reusable skill for VS Code Copilot, Cursor, and Claude Code — a `.md` file that can be dropped into a project's skills directory and invoked with a single command. The skill guides the AI through a deliberation phase before implementation, ensuring architecture and design decisions are the human's, while implementation is the AI's.

## Timeline

| Date | Event |
|------|-------|
| 2010s | Establishes benmvp.com as a personal blog and developer education platform |
| ~2018–2022 | Publishes extensively on frontend development, CSS architecture, React patterns, and accessibility |
| 2023 | Develops early versions of deliberation-first coding methodology through personal AI experimentation |
| 2024 | Publishes on CSS architecture and frontend design systems |
| 2025 | Formalizes the "deliberate skill" — a reusable AI coding methodology documented on GitHub Gist |
| 2025 | Publishes "From Vibe Coding to Deliberation-First Coding with AI" — the definitive statement of the methodology |
| 2025 | Demonstrates the skill on a real project (adding CSS Validator tool to CodeMata app suite) |
| 2025 | Meta-demonstrates the methodology by writing the blog post itself using the deliberate skill |
| 2026 | Continues to advocate for deliberation-first coding as AI tools become more prevalent |

## Core Ideas

### Deliberation-First Coding vs. Vibe Coding

Ilegbodu's central thesis is that **"vibe coding" — giving an AI agent a prompt, reviewing the output, and iterating — is fundamentally inefficient:**

> "You give the Agent a prompt. It writes 200 lines of code. You review it. The architecture is wrong. You explain what you meant. It rewrites. The patterns don't match your codebase. You explain again..."

This write-review-write loop is slow, error-prone, and produces code that reflects the AI's architectural choices rather than the developer's intent. Deliberation-first coding solves this by **front-loading shared context**:

> "There's a better way. I call it deliberation-first coding: structured conversations with AI Agents that front-load architecture, constraints, and patterns before a single line is generated."

The process works in two distinct phases:
1. **Deliberation Phase:** The developer and AI agent discuss architecture, patterns, constraints, and goals. The AI asks clarifying questions. The developer makes design decisions.
2. **Implementation Phase:** The AI generates code that matches the deliberated architecture.

The result: what used to take 5+ rounds of iteration becomes 1–2 rounds of edge case refinement.

### The Deliberate Skill

Ilegbodu formalized this methodology into a reusable **skill file** for AI coding assistants (VS Code Copilot, Cursor, Claude Code):

```
/deliberate I want to... [describe your task with background context]
```

The skill guides the AI through a structured conversation:
1. Understand the codebase patterns and constraints
2. Ask clarifying questions about architecture and design
3. Propose an approach for the developer to approve
4. Only then generate code

> "The architecture was mine. The implementation was the Agent's. Both were better for it."

### Meta-Application: Using the Skill to Write About the Skill

Ilegbodu demonstrated the power of the methodology by using it to create the blog post that describes it:

```
/deliberate I want to create a new GenAI blog post about my structured "vibe coding" process.
It involves lots of conversations with the Agent before actually writing out the code, as opposed
to the write-review-write loop that I believe is inefficient and error-prone.
```

The AI asked clarifying questions about audience, structure, example depth, and how to handle the evolution story. This meta-demonstration proved that the methodology works not just for code, but for **docs, specs, architecture, and anything requiring thoughtful planning.**

### Why Deliberation-First Works

Ilegbodu identifies several key principles:

1. **Front-loaded shared context removes incorrect assumptions:** The Agent needs to understand your codebase patterns, constraints, and goals. Without context, it's guessing. With context, it's collaborating.
2. **Architecture ownership stays with the developer:** The human decides the structure; the AI implements it. This preserves design integrity while leveraging AI speed.
3. **Reduced iteration cycles:** What used to take 5+ rounds of "no, that's not what I meant" becomes 1–2 rounds of edge case refinement.
4. **Commoditization of the path to correct implementation:** "If AI commoditizes code implementation, deliberation-first coding commoditizes the path to correct implementation."

### Broader Developer Education

Beyond the deliberate coding methodology, Ilegbodu's work encompasses:
- **CSS architecture and design systems** — deep dives into scalable CSS patterns
- **React best practices** — component design, state management, performance optimization
- **Accessibility** — making web applications usable for everyone
- **Developer productivity** — tools, workflows, and practices that make teams more effective
- **CodeMata** — a suite of free developer tools including a CSS Validator

## Writing Style and Approach

- **Structured and methodical:** Ilegbodu's posts follow a clear progression from problem → analysis → solution → implementation
- **Practical and evidence-based:** Every concept is demonstrated with real code and real projects
- **Meta-aware:** Willing to use the methodology to write about the methodology, proving its effectiveness
- **Developer-advocate mindset:** Focuses on sharing knowledge and improving the broader developer community

## Key Quotes

> "You give the Agent a prompt. It writes 200 lines of code. You review it. The architecture is wrong."

> "There's a better way. I call it deliberation-first coding: structured conversations with AI Agents that front-load architecture, constraints, and patterns before a single line is generated."

> "The architecture was mine. The implementation was the Agent's. Both were better for it."

> "If AI commoditizes code implementation, deliberation-first coding commoditizes the path to correct implementation."

## Contact

- **Blog:** https://www.benmvp.com
- **GitHub:** https://github.com/benmvp
- **Twitter/X:** @benmvp

## See Also

- [[entities/_index]]
