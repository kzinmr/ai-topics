---
title: "Agentic Workflows — Developer Workflows Under Harness Engineering"
type: concept
aliases:
  - agentic-workflows
  - agentic-coding-patterns
  - developer-agentic-workflows
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - methodology
  - harness-engineering
  - workflow
status: active
parent: harness-engineering
sources: []
---

# Agentic Workflows — Developer Workflows

Practical workflows and patterns for "using AI agents to develop software." Positioned as a **subsection of Harness Engineering**.

## Positioning within Harness Engineering

| Layer | Concept | Focus |
|---------|------|------|
| **Top** | [[concepts/_index|Harness Engineering]] | Agent = Model + Harness (environment design philosophy) |
| **Cross-cutting** | [[concepts/context-engineering]] | Context selection, compression, placement (finite resource management) |
| **Application (Human)** | **Agentic Workflows** (this page) | Patterns for developers to "leverage" agents |
| **Application (System)** | [[concepts/harness-engineering/system-architecture/_index]] | Patterns for "building" agents |

## Key Concepts by Leader

| Leader | Core Concept | Related Pages |
|---------|--------------|-----------|
| [[entities/simon-willison]] | Agentic Engineering Patterns, Red/Green TDD, Cognitive Debt | Willison pattern group below |
| [[entities/andrej-karpathy]] | Software 2.0, RL-based agent learning, data-centric AI | [[concepts/karpathy-rl-agents]] |
| [[entities/sankalp-sinha]] | Claude Code 2.0 practical guide, sub-agent lossiness, Throw-Away Draft, context 60% rule | Sankalp pattern group below |
|  | Agent-First Design, CLI-First Development, No-Plan-Mode thesis, inference-speed bottleneck | Steipete pattern group below |

## Simon Willison's Development Patterns

### 🧪 Test-Driven Development

| Page | Summary |
|-------|------|
| [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] | Run tests first before letting agents change code |
| [[concepts/red-green-tdd]] | Red/Green TDD cycle where agents write tests before implementation |
| [[concepts/agentic-manual-testing]] | Automating manual testing through agents |

### 📝 Documentation & Artifacts

| Page | Summary |
|-------|------|
| [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] | Generating explanations from Linear tickets |
| [[concepts/showboat]] | A documentation tool that visualizes agent work |
| [[concepts/interactive-explanations]] | Explaining algorithms via interactive animations |
| [[concepts/vibe-coding]] | The "write by feel" approach without tests and its limitations |

### 🔧 Tool Integration

| Page | Summary |
|-------|------|
| [[concepts/harness-engineering/agentic-workflows/using-git-with-agents]] | Integrating agents into Git workflows |
| [[concepts/harness-engineering/agentic-workflows/how-agents-work]] | Conceptual model of how coding agents work internally |

### 🧠 Cognition and Quality

| Page | Summary |
|-------|------|
| [[concepts/cognitive-debt]] | "Cognitive debt" accumulated when merging agent-generated code without understanding it |
| [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] | Iterative quality improvement loop |
| [[concepts/harness-engineering/agentic-workflows/code-hoarding]] | Pattern for keeping important knowledge outside agent context |

### 🏗️ Sankalp's Practical Patterns

| Page | Summary |
|-------|------|
| [[concepts/context-window-management]] | Context 60% rule, compression strategies |
| [[concepts/throw-away-draft-pattern]] | Draft → compare → iterate development cycle |
| [[concepts/subagents]] | Sub-agent lossiness, usage guidelines |

### 🚀 Steipete's Inference-Speed Development

| Page | Summary |
|-------|------|
| [[concepts/agent-first-design]] | Code design for "agents" not "humans" |
| [[concepts/harness-engineering/agentic-workflows/cli-first-development]] | Start with CLI to accelerate feedback loops |
| [[concepts/harness-engineering/agentic-workflows/prompt-driven-development]] | Prompt-driven development patterns |

## Agentic Workflows vs System Architecture

| Dimension | Agentic Workflows | System Architecture |
|------|-------------------|---------------------|
| Focus | Developer workflows | System architecture |
| Subject | "How humans use agents" | "How to build agents" |
| Example | Willison's Red/Green TDD, Cognitive Debt | Anthropic's Building Effective Agents |
| Layer | Application/Usage | Foundation/Design |

## Related Concept Map

```
Agentic Workflows (Harness Engineering)
├── 🧪 Willison's Test Patterns
│   ├── First Run the Tests
│   ├── Red/Green TDD
│   └── Agentic Manual Testing
├── 📝 Documentation
│   ├── Linear Walkthroughs
│   ├── Showboat
│   └── Interactive Explanations
├── 🔧 Tool Integration
│   ├── Using Git with Agents
│   ├── How Coding Agents Work
│   └── Vibe Coding
├── 🧠 Cognition and Quality
│   ├── Cognitive Debt
│   ├── Compound Engineering Loop
│   └── Code Hoarding
└── 🤖 Karpathy's RL Agents
    └── Software 2.0 / Autoresearch Loop
```

## Changelog

| Date | Changes |
|------|---------|
| 2026-04-12 | Initial creation — Built around Willison's development patterns |
| 2026-04-19 | Harness umbrella reorganization: title update, added System Architecture positioning table, consolidated duplicate entries |
