# Shopify Roast: Structured AI Workflows Made Easy

- **Source:** https://shopify.engineering/introducing-roast
- **Author:** Sam Schmidt (Shopify Augmented Engineering DX team)
- **Date:** 2025
- **Domain:** ai-agents, workflow-orchestration, developer-tools
- **Tags:** framework, workflow-orchestration, ai-agents, open-source

## Summary

Shopify open-sourced **Roast** (`roast-ai`), a convention-oriented workflow orchestration framework designed for creating structured AI workflows that interleave AI prompting with deterministic non-AI execution. It uses declarative YAML configuration and markdown prompts to provide AI guardrails.

## Key Features

- **Declarative YAML + Markdown prompts** for structured AI workflows
- **Step types:** Directory-based (prompt.md with ERB), Command Execution, Inline Prompt, Custom Ruby, Parallel Execution
- **Built-in toolkit:** ReadFile, WriteFile, UpdateFiles, Grep, SearchFile, Cmd, Bash, CodingAgent
- **CodingAgent:** Full Claude Code integration for iterative, adaptive tasks
- **Session Replay:** Auto-save of every execution, resume from any step
- **Advanced Control Flow:** iteration, conditional execution, case statements
- **Philosophy:** AI as placeholder — prototype with AI, replace with deterministic code

## Use Cases

- Test quality at scale (auto-detect antipatterns, boost coverage)
- Automated Sorbet type annotation pipeline
- Proactive SRE monitoring (scan Slack for early issue indicators)
- Competitive intelligence aggregation
- "Chesterton's Fence" tool (research commit history to explain legacy code)

## Tech Stack

- Ruby gem (`roast-ai`), requires Ruby 3.0+
- Built on **Raix** (Ruby AI eXtensions)
- Supports OpenAI API key or OpenRouter for other models
- Optional `shadowenv` & `ripgrep`

## Why This Matters

Roast solves the AI agent non-determinism problem by providing structured guardrails around AI steps. It enables version control, testing, and CI/CD integration for AI workflows. The ability to seamlessly transition from AI-driven steps to deterministic code once a solution is understood is a significant advancement for production AI agent systems.
