---
title: "Nextpad++ and AI Development Quality"
type: concept
created: 2026-05-13
updated: 2026-05-13
tags:
  - coding-agents
  - quality-assurance
  - developer-experience
  - multi-agent
aliases: ["nextpad-plus-plus", "ai-vibe-coding-quality"]
sources:
  - https://daringfireball.net/2026/05/nextpad
  - https://simonwillison.net/2026/May/12/mo-bitar/
---


# Nextpad++ and AI Development Quality

**Nextpad++** is a macOS port of the Windows Notepad++ text editor, built by Andrey Letov using multi-agent AI development workflows. Launched in early 2026, it serves as a prominent case study in the **quality challenges of AI-generated software** — specifically, how the combination of vibe coding practices and multi-agent development can produce functional but deeply flawed applications that feel "unholy" to experienced users.

The project was highlighted by John Gruber (Daring Fireball) and Simon Willison as a canonical example of what happens when AI development prioritizes speed and functional completeness over user experience quality and platform-native design.

---

## What Is Nextpad++?

Nextpad++ is an Objective-C++ port of Notepad++ (originally by Don Ho, GPL-licensed since 2003) to macOS. Key technical details:

| Property | Value |
|----------|-------|
| **Developer** | Andrey Letov |
| **Language** | Objective-C++ on top of Scintilla and Cocoa |
| **Binary** | Universal Binary (Apple Silicon M1–M5 + Intel) |
| **Download Size** | 14 MB |
| **Development Timeline** | Started March 10, 2026; v1.0 shipped ~3 weeks later |
| **AI Usage** | Multi-agent AI development workflows |

The project's About page explicitly states: *"multi-agent AI development workflows are what make a one-person project at this scale practical."*

---

## The Quality Problem

Despite being technically functional, Nextpad++ exhibits numerous quality issues that reveal the gap between "it works" and "it's good":

### UI/UX Deficiencies
- **50 inscrutable toolbar buttons** — overwhelming, non-intuitive interface
- **Closes document tabs on mousedown, not mouseup** — violates macOS interaction conventions
- **Default font is 10-point Courier New** — outdated typography choice
- **Dialog box offers four settings for font antialiasing** — "Default", "None", "Antialiased", and "LCD Optimized" — but the default is NOT "Default"

### Platform Integration Failures
- Doesn't feel like a native Mac app
- Lacks expected macOS conventions and patterns
- Described by Gruber as feeling like *"Vincent D'Onofrio's alien-bug-in-human-skin character from Men in Black"*

### The Core Issue
The app demonstrates that **AI can produce functional software that no human would intentionally ship**. The multi-agent workflow enabled rapid development but bypassed the quality judgment that a human developer would naturally apply to their own work.

---

## What This Teaches Us About AI Development

### 1. Speed ≠ Quality
Nextpad++ was developed in approximately 3 weeks — remarkably fast for a cross-platform port of this complexity. However, the speed came at the cost of:
- No user research or testing
- No platform-specific design guidelines followed
- No iteration based on user feedback
- No quality gate reviews

### 2. The "Uncanny Valley" of AI Software
The app exists in a strange middle ground: technically functional but qualitatively wrong. It's not obviously broken, but it's also not obviously good. This represents a new category of software quality problem specific to AI development.

### 3. Multi-Agent Development Amplifies This Risk
When multiple AI agents work in parallel on different aspects of a project:
- Each agent optimizes for its local task completion
- No single agent has holistic understanding of the user experience
- Coordination failures produce inconsistent design decisions
- The result is functional but disjointed

### 4. Human Judgment Remains Essential
The fundamental insight is that **AI can build anything, but can't judge whether it should be built that way**. Human developers naturally filter out bad design decisions during the building process; AI agents lack this filtering mechanism.

---

## Industry Response

John Gruber (Daring Fireball): *"I'm not anti-AI. I'm very much intrigued by the whole incipient vibe-coding phenomenon. But this app feels unholy."*

Simon Willison highlighted the project as evidence that the boundary between vibe coding and agentic engineering is becoming increasingly important to define and enforce.

---

## Related Concepts

- [[concepts/vibe-coding-vs-agentic-engineering]] — The distinction between shipping fast vs. shipping well
- [[concepts/normalization-of-deviance-in-ai-coding]] — How bad practices become normalized through repetition
- [[concepts/cognitive-debt]] — The hidden costs of not understanding what you've built
- [[concepts/multi-agent-orchestration-architecture]] — How multiple agents coordinate (or fail to) on complex projects

## Sources

- [Daring Fireball: Nextpad++](https://daringfireball.net/2026/05/nextpad) (May 2026)
- [Simon Willison: A quote from Mo Bitar](https://simonwillison.net/2026/May/12/mo-bitar/) (May 2026)
- [Nextpad++ About page](https://nextpad.app/about)
