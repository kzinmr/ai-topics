---
title: "Tuning Deep Agents to Work Well with Different Models"
source: https://blog.langchain.dev/tuning-deep-agents-different-models/
date: 2026-04-29
author: Vivek Trivedy, Mason Daugherty (LangChain)
---

# Tuning Deep Agents to Work Well with Different Models

LangChain launched **harness profiles** for Deep Agents — model-specific profiles that adjust prompts, tools, and middleware per model family. Previously, `deepagents` shipped with a single set of defaults for all LLMs.

## Key Results

| Model | Base Deep Agents Harness | With Custom Profile |
|-------|--------------------------|---------------------|
| GPT 5.3 Codex | 33% | 53% (+20pt) |
| Claude Opus 4.7 | 43% | 53% (+10pt) |

Benchmark: curated subset of tau2-bench (multi-turn tool use + instruction following).

## What Changed Per Model

**For Codex**: Tool overrides (file_edit → apply_patch, execute → shell_command), prompt changes for tool calling and planning per the Codex Prompting Guide.

**For Opus**: Prompt additions including `<tool_result_reflection>` block and `<tool_usage>` directive emphasizing active investigation with tools over reasoning from memory.

## Significance

Terminal-Bench 2.0 showed that the same model in a different harness can yield dramatically different performance — the Claude Code harness ranked last among Opus 4.6 submissions. LangChain's earlier work took gpt-5.2-codex from 52.8% to 66.5% on Terminal-Bench 2.0 (Top 30 → Top 5) purely through harness-layer changes.

Harness profiles are now available for Deep Agents open-source users, with profiles for OpenAI, Anthropic, and Google models shipped out of the box.
