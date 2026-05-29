---
title: Pointer
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [entity, company, open-source, computer-use, ai-agents, agent-harness, agent-architecture, browser-automation]
sources: [raw/articles/2026-05-26_pointer-osworld-sota.md]
---

# Pointer

Pointer is an AI company that built an open-source computer use agent system achieving state-of-the-art results on the OSWorld benchmark. In May 2026, Pointer posted the two highest verified scores ever recorded: **83.6%** with [[entities/anthropic|Claude Opus 4.7]] and **81.5%** with Claude Sonnet 4.6, both surpassing the human baseline of 72.4%.

## Key Facts

- **Founded**: Unknown (stealth/early stage as of May 2026)
- **Focus**: Computer use agents — AI that operates real desktop environments
- **Benchmark**: OSWorld — 361 tasks across real desktops (Chrome, VS Code, GIMP, LibreOffice, VLC, Thunderbird, OS settings)
- **Open source**: Full system released publicly
- **Website**: pointer.ai

## Architecture

Pointer's system uses a lightweight, modular design with a **task controller** orchestrating three specialized agents:

| Agent | Model | Responsibility |
|-------|-------|----------------|
| **Feasibility Gate** | Claude Sonnet 4.6 | Decide if task is possible before any work begins |
| **Planner** | Claude Sonnet 4.6 | Break goal into state-based milestones |
| **Executor** | Claude Opus 4.7 or Sonnet 4.6 | Execute tasks with unified tooling |

### Key Design Decisions

- **GUI-first approach**: The executor is explicitly instructed to prefer UI actions over programmatic workarounds, as OSWorld evaluates actual desktop state (spreadsheet XML, etc.)
- **Two strikes, then switch**: If two attempts at the same mechanism fail, the executor must change strategy entirely — curbing the model's tendency to retry dead ends
- **Unified executor**: Collapsed specialist sub-agents into one after observing that frontier models handle large tool schemas well and cross-modal handoffs lose state
- **Feasibility gate**: Caught 24 of 28 impossible tasks (85.7% recall) with only 2 false positives on valid tasks (99.4% specificity)
- **Context compaction**: Uses Claude Haiku 4.5 for context management in long-running tasks

### Tools Available to Executor

- **GUI**: Click, type, scroll, drag, hotkeys, window management
- **Code**: Python and Bash execution for data extraction and file manipulation
- **Browser**: Chrome DevTools Protocol via Python snippets
- **Background execution**: For commands exceeding the environment's 120-second limit

## Results

- Holds the **top score in 7 of 10 OSWorld domains**
- **VS Code**: 95.7%, **Multi-apps**: 74.4% (vs field mean ~10pts lower)
- The pace of improvement is notable: a year ago best scores were ~20%; now frontier clears human baseline

## Guiding Philosophy

> "An agent that can operate the screen isn't limited to the integrations someone thought to build in advance."

Pointer contrasts with [[concepts/rpa|RPA]] by having the agent figure out how from current state rather than following brittle scripts.

## Related Pages

- [[entities/anthropic]] — Provider of Claude models used as executor
- [[concepts/computer-use]] — Computer use as an AI agent capability
- [[concepts/osworld]] — OSWorld benchmark for computer use agents
- [[concepts/browser-automation]] — Browser automation agents
- [[concepts/agent-architecture]] — Agent architecture patterns
- [[concepts/ai-agents]] — AI agents overview
