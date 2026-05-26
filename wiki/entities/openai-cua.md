---
title: OpenAI CUA (Computer-Using Agent)
type: entity
aliases:
- openai-cua
- cua-model
- openai-operator
- computer-using-agent
created: 2026-04-13
updated: 2026-05-26
tags:
  - entity
  - developer-tooling
  - ai-agents
  - browser-agent
  - openai
status: active
sources:
- https://openai.com/blog/introducing-operator
- https://openai.com/index/operator-system-card/
- https://www.libertify.com/interactive-library/openai-operator-system-card-cua-safety/
---

# OpenAI CUA (Computer-Using Agent)

OpenAI's **CUA (Computer-Using Agent)** model combines GPT-4o's vision capabilities with reinforcement learning to look at screenshots and manipulate GUIs. It was released as "Operator" in January 2025 and fully integrated into ChatGPT agents in July 2025.

## Overview

| Attribute | Detail |
|-----------|--------|
| Release Date | January 23, 2025 (Operator research preview) |
| Base Model | GPT-4o + Reinforcement Learning |
| Approach | Screenshot-based vision recognition + RL |
| Availability | ChatGPT Pro ($200/mo) → ChatGPT agent integration |
| API | CUA model (March 2025, Tiers 3-5 developers) |
| OSWorld Score | 38.1% |
| WebArena Score | 58.1% |
| WebVoyager Score | 87% |

## Technical Architecture

### Two-Stage Training
1. **Supervised Learning**: Reading screenshots, recognizing UI elements, basic input control
2. **Reinforcement Learning**: Reasoning, error correction, adapting to unexpected situations

```
Task instruction → Capture screenshot → GPT-4o vision analysis →
Action decision (click/type/scroll) → Execute →
Verify state with next screenshot → Self-correct → Repeat
```

### Safety (Three Layers)
- **Model layer**: 97% harmful task rejection rate
- **Prompt injection defense**: 99% detection rate, 98.4% accuracy
- **Product layer**: Critical operations require human confirmation, one-click session termination

### Preparedness Framework Evaluation
| Category | Risk Level |
|----------|------------|
| Persuasion | Medium (inherited from GPT-4o) |
| Cybersecurity | Low |
| CBRN | Low (1% task success rate) |
| Model Autonomy | Low |

## Timeline

| Date | Milestone |
|------|-----------|
| January 2025 | Operator research preview released (ChatGPT Pro only) |
| March 2025 | CUA model released via API (Tiers 3-5 developers) |
| July 2025 | Full integration into ChatGPT agents |
| 2026 | Planned expansion to Plus/Team/Enterprise users |

## Challenges and Limitations

1. **Complex tasks**: Success rate drops to 40% on unfamiliar UIs and complex text editing
2. **OSWorld 38.1%**: Has not yet reached high reliability
3. **Privacy**: Screenshot transmission, browsing history handling
4. **Non-browser environments**: Error rate increases for OS-level operations

## Comparison with Anthropic Computer Use

| Dimension | OpenAI CUA | Anthropic Computer Use |
|-----------|------------|------------------------|
| Base Model | GPT-4o + RL | Claude Sonnet/Opus |
| OSWorld | 38.1% | 14.9% → 22.0%+ |
| WebArena | 58.1% | 58.1% |
| Training | Supervised + RL | Screenshot-based |
| Availability | ChatGPT integration + API | API + Claude App |
| Harmful task rejection | 97% | N/A |

## Related Entities

- [[entities/anthropic-computer-use]] — Anthropic's Computer Use
- [[concepts/death-of-browser]] — Browser dehumanization trend
- [[entities/browser-use]] — Open source DOM-based automation
- [[concepts/harness-engineering]] — Agent environment design

## Sources

- [Introducing Operator (OpenAI, 2025-01)](https://openai.com/blog/introducing-operator)
- [Operator System Card (OpenAI)](https://openai.com/index/operator-system-card/)
- [CUA API Launch (2025-03)](https://cdn.openai.com/operator_system_card.pdf)
