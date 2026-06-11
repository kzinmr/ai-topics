---
title: "CLI-First Development"
type: concept
aliases:
  - cli-first-development
  - cli-first-agents
  - command-line-first
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://steipete.me/posts/2025/shipping-at-inference-speed"
  - "https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/"
---

# CLI-First Development

An approach that **starts software development from the CLI (Command Line Interface)**. A core pattern of agent-era development workflows.

## Core Principle

> *"Most apps are data pipelines. Starting with a CLI allows agents to execute, verify output, and close the feedback loop without UI overhead."*
> — Peter Steinberger

Instead of starting with a UI, first build the core logic as a CLI, creating an environment where agents can immediately execute and verify.

## Why CLI-First?

### 1. Faster Feedback Loops

| Starting Point | Agent Execution | Verification Method | Feedback Speed |
|--------|------------------|----------|------------------|
| **CLI** | Immediate execution | stdout / exit code | Seconds |
| **Web UI** | Browser interaction needed | Visual inspection | Minutes |
| **Mobile App** | Simulator / physical device | UI testing | Tens of minutes |

### 2. Agent Compatibility

- CLI has **structured I/O** → easier for agents to understand
- Easy test automation → agents can self-verify
- Batch processing / pipelining → parallel execution is possible

### 3. Reduced Cognitive Load

Instead of spending time on UI tweaks (padding, colors, layout), you can focus on **logic correctness**.

## Sankalp's Practice: CC → Codex → Cursor

Sankalp uses tools in this manner:

```
Claude Code (CC)  →  Main driver. Fast CLI-based implementation
     ↓
GPT-5.2-Codex     →  Review and bug discovery. P1/P2 severity tagging
     ↓
Cursor            →  Manual editing and code reading
```

This pipeline reflects the CLI-first philosophy:
1. Start implementation from CLI with CC
2. Auto-discover bugs with Codex
3. Manual edits in Cursor when needed

## Steipete's Practice: Language Selection

| Use Case | Language | Reason |
|------|------|------|
| **CLI** | Go | Simple type system, fast linting, easy for agents to handle |
| **Web** | TypeScript | Rich ecosystem, abundant agent training data |
| **macOS/UI** | Swift | No Xcode needed. Simulator control via Swift build + Codex |

## Practice Patterns

### Pattern 1: CLI Prototype → Web Extension

```bash
# 1. Build core logic as CLI
$ python cli_tool.py --input data.json --output result.json

# 2. Agent verifies and fixes the CLI
$ claude "Fix the date parsing in cli_tool.py"

# 3. Add Web UI later
$ claude "Build a web frontend for cli_tool.py using FastAPI"
```

### Pattern 2: Test-Driven CLI Development

```bash
# 1. Write tests
$ claude "Write tests for the data processing pipeline"

# 2. Run via CLI
$ python -m pytest tests/ -v

# 3. Extend to Web UI after passing
```

### Pattern 3: Background Task Delegation

```bash
# Main agent runs CLI task in background
$ claude --background "Run the full test suite and report failures"
# Continue other work while receiving notification on completion
```

## UI is "Last"

In the CLI-first approach, UI is left for last for these reasons:

1. **UI is subjective**: Debating 1px padding differences is a waste of time
2. **UI is easy to change**: Building the UI after logic is solidified reduces rework
3. **Agents excel at CLI**: Structured I/O is more precise to handle

> *"Building software is like walking up a mountain. You don't go straight up, you circle around it and take turns, sometimes you get off path and have to walk a bit back, and it's imperfect, but eventually you get to where you need to be."*
> — Peter Steinberger

## Related Concepts

- [[concepts/agent-first-design]] — Code design for agents
- [[concepts/context-engineering/context-window-management|Context Window Management]] — CLI consumes less context
- [[concepts/agentic-engineering]] — Higher-level concept

## References

- [[entities/peter-steinberger]] — CLI-first development advocate- [[entities/sankalp-sinha]] — CC → Codex → Cursor pipeline practitioner
- [Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
- [A Guide to Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/)
