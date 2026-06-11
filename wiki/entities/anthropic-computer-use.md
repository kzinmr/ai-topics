---

title: Anthropic Computer Use
type: entity
aliases:
- claude-computer-use
- anthropic-cu
- claude-cowork
- vercept-acquisition
created: 2026-04-13
updated: 2026-04-13
tags:
  - entity
  - developer-tooling
  - ai-agents
  - browser-agent
  - anthropic
sources:
- https://www.anthropic.com/news/claude-sonnet-4-6
- https://www.anthropic.com/news/acquires-vercept
- https://techcrunch.com/2026/02/25/anthropic-acquires-vercept-ai-startup-agents-computer-use-founders-investors/

---
# Anthropic Computer Use

**Anthropic Computer Use** is a capability that allows Claude models to view screenshots and directly operate GUIs. Released as a research preview in October 2024, it can interact with computers the same way humans do — clicking screen coordinates, typing keys, and scrolling. Following the Vercept acquisition and Claude Sonnet 4.6 release in February 2026, the OSWorld score jumped from under 15% to 72.5%.

## Overview

| Item | Details |
|---|---|
| Initial Release | October 2024 (Research Preview) |
| Base Model | Claude Sonnet / Opus |
| Approach | Screenshot-based vision recognition + reasoning |
| Delivery Format | API + Claude App (Cowork) |
| OSWorld Score | 14.9% → 72.5% (Sonnet 4.6, Feb 2026) |
| WebArena Score | 58.1% |
| Security | ASL-2 prompt injection resistance |

## Technical Architecture

### Perception-Action Loop
```
Task instruction → Capture screenshot → Vision model recognizes UI elements →
Action plan (click/type/scroll) → Execute →
Verify state with next screenshot → Self-correct → Repeat
```

### Claude Sonnet 4.6 Improvements (Feb 2026)
- OSWorld: Under 15% → **72.5%** (approaching human level)
- 1M token context support
- Adaptive thinking + Extended Thinking
- Context Compaction (beta)
- Automatic code generation for web search/fetch tools

### Vercept Acquisition Impact (Feb 2026)
Anthropic acquired Seattle-based AI startup **Vercept**:
- **Co-founders**: Kiana Ehsani (CEO), Luca Weihs, Ross Girshick
- **Vy Product**: Cloud-based computer use agent (remote MacBook operation)
- **Specialty**: Vision-based computer recognition and automation
- **Funding**: $50M total (led by Fifty Years' Seth Bannon)
- **Angel investors**: Eric Schmidt (former Google CEO), Demis Hassabis (Google DeepMind CEO)
- **Origins**: Allen Institute for AI (AI2)
- Post-acquisition, integrated into Anthropic's computer use research group
- External product Vy shut down on March 25, 2026

### Safeguards
- **ASL-2 (Anthropic Safety Level 2)**: Prompt injection resistance
- Sonnet 4.6 shows significant improvement over Sonnet 4.5, on par with Opus 4.6
- Improved error correction capability in multi-step tasks

## Timeline

| Date | Milestone |
|---|---|
| October 2024 | Computer Use research preview released |
| July 2025 | OSWorld-Verified benchmark released |
| January 2026 | Claude Cowork research preview (computer use integration) |
| February 17, 2026 | Claude Sonnet 4.6 released (OSWorld 72.5%) |
| February 25, 2026 | Vercept acquisition announced |
| March 25, 2026 | Vercept Vy product discontinued, integrated into Anthropic |

## Strengths

1. **Legacy Software**: Operating specialized systems without APIs
2. **Multi-Tab Tasks**: Workflows spanning multiple browser tabs
3. **Complex Form Entry**: Web forms, spreadsheet operations
4. **Non-Automatable Tools**: Operating tools without modern API connectors

## Limitations & Challenges

1. **Speed**: Latency from sending/receiving screenshots
2. **Token Consumption**: High API cost due to image-based approach
3. **Precision**: Drag-and-drop, complex multi-step forms
4. **Dynamic UI**: Stability with frequently changing interfaces

## Comparison with OpenAI CUA

| Dimension | Anthropic Computer Use | OpenAI CUA |
|---|---|---|
| Base Model | Claude Sonnet/Opus | GPT-4o + RL |
| OSWorld Score | **72.5%** (Sonnet 4.6) | 38.1% |
| WebArena Score | 58.1% | 58.1% |
| Training | Vision recognition + reasoning | Supervised + reinforcement learning |
| Safeguards | ASL-2 (prompt resistance) | 3-layer (97% harmful rejection) |
| Delivery | API + Claude Cowork | ChatGPT agent integration |
| Latest Development | Vercept acquisition (Feb 2026) | Expanding API access |

## Related Entities

- [[entities/openai-cua]] — OpenAI's Computer-Using Agent
- [[concepts/browser-agent/death-of-browser]] — The de-humanization of browsers
- [[entities/browser-use]] — Open-source DOM-based automation
- [[concepts/harness-engineering]] — Agent environment design
- [[entities/webmcp]] — Standardization protocol

## Sources

- [Introducing Claude Sonnet 4.6 (Anthropic, 2026-02-17)](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Anthropic acquires Vercept (Anthropic, 2026-02-25)](https://www.anthropic.com/news/acquires-vercept)
- [Anthropic acquires computer-use AI startup Vercept (TechCrunch)](https://techcrunch.com/2026/02/25/anthropic-acquires-vercept-ai-startup-agents-computer-use-founders-investors/)
- [Claude AI Computer Use: Near-Human Performance (SuperClaude)](https://superclaude.app/en/blog/claude-ai-computer-use-vercept-near-human-performance)
