---
title: "Harness Profiles"
created: 2026-05-14
updated: 2026-05-14
type: concept
tags: [agentic-engineering, ai-agents, prompting, optimization, langchain, deep-agents, coding-agents]
sources: [raw/articles/2026-04-29_langchain-harness-profiles.md]
---

# Harness Profiles

**Harness profiles** are model-specific configurations that tune an AI agent's prompts, tools, and middleware to optimize performance for a particular LLM family. The concept was formalized by LangChain's Deep Agents team in April 2026.

## Core Insight

A single agent harness cannot be optimal for every model. Different model families have different prompting guides, tool conventions, and behavioral characteristics. Harness profiles encode these model-specific optimizations as swappable configurations.

## LangChain Implementation

LangChain's `deepagents` framework (v0.5+) supports harness profiles for:
- **OpenAI models**: Implements Codex Prompting Guide conventions (`apply_patch` tool, `shell_command` aliasing)
- **Anthropic models**: Implements Claude prompting best practices (tool result reflection, active investigation directives)
- **Google models**: Google-specific optimizations

### Performance Impact

On a curated tau2-bench subset:
| Model | Base Harness | With Custom Profile | Gain |
|-------|-------------|---------------------|------|
| GPT 5.3 Codex | 33% | 53% | +20pt |
| Claude Opus 4.7 | 43% | 53% | +10pt |

Earlier work showed similar effects: gpt-5.2-codex went from 52.8% to 66.5% on Terminal-Bench 2.0 (Top 30 → Top 5) purely through harness-layer changes.

## Why It Matters

Terminal-Bench 2.0 demonstrated that the same model in different harnesses can produce dramatically different results — the [[entities/claude-code|Claude Code]] harness ranked last among Opus 4.6 submissions. Harness profiles close this gap by aligning the agent layer with each model's strengths.

## Related Concepts

- [[concepts/agent-harness|Agent Harness]] — the surrounding infrastructure that shapes agent behavior
- [[concepts/delta-channels|Delta Channels]] — LangGraph primitive for long-running agent state management
- [[concepts/deep-agents|Deep Agents]] — LangChain's open-source agent framework
- [[entities/langchain|LangChain]] — the framework behind this innovation
- [[concepts/agentic-engineering|Agentic Engineering]] — the discipline of engineering agent systems
