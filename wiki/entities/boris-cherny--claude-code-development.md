---
title: "Boris Cherny — Claude Code Development Story"
type: entity
parent: boris-cherny
created: 2026-04-28
updated: 2026-04-28
tags:
  - person
  - claude-code
  - anthropic
  - ai
  - coding-agents
sources: []
---

# Boris Cherny: Claude Code Development Story

Back to main profile: [[boris-cherny]]

## Origins (Sep 2024 – Nov 2024)

Claude Code began when Boris joined Anthropic in September 2024 and started prototyping with the Claude 3.6 model. His first prototype was a **command-line tool to identify and change music via AppleScript** — this evolved into the core of Claude Code. The prototyping drew from an earlier Anthropic research project called **Clide**, which influenced Boris's approach despite its inefficiencies (slow startup times, heavy indexing requirements).

By November 2024, an internal dogfooding-ready version was released:
- **20% of Anthropic's engineering team** adopted it on day one
- **50% adoption by day five**
- Rapid iterative refinement through constant internal feedback

The tool reached **general availability in May 2025**, after which the team expanded to around 10 engineers by July 2025.

## Key Development Challenges

- **Filesystem access**: Adding tools for reading, writing, and running batch commands while preventing unintended file deletions through a robust permissions system with static analysis
- **Minimizing business logic**: Letting the AI model operate as "raw" as possible — deleting portions of the system prompt as models improved
- **Local vs virtualized execution**: Opting for local execution for simplicity, balancing performance and safety
- **High-velocity prototyping**: Boris built ~20 prototypes for features like todo lists over two days, testing 5-10 ideas daily with AI agents
- **60-100 internal releases per day** — bottom-up feature building based on individual team needs

## Team & Collaboration

- **Sid Bidasaria** (joined Nov 2024) — rapid iterations and subagent development, completed key features in just three days through experimental approaches
- **Cat Wu** (founding product manager) — researched AI agent usage, provided feedback that expanded the tool's scope
- **Dogfooding culture**: 70-80% of technical staff used Claude Code daily, generating constant input via internal channels

## See Also

- [[boris-cherny--core-ideas|Core Ideas & Philosophy]]
- [[boris-cherny--key-work|Key Work & Impact]]
