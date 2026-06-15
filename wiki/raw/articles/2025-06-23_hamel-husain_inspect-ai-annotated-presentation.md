---
title: "Inspect AI, An OSS Python Library For LLM Evals — Annotated Presentation"
author: Hamel Husain
date: 2025-06-23
date_ingested: 2026-06-15
source: https://hamel.dev/notes/llm/evals/inspect.html
type: article
tags: [evaluation, evals, framework, open-source, agent-evaluation, sandbox, ai-safety]
companion_video: true
---

# Inspect AI, An OSS Python Library For LLM Evals

> A look at Inspect AI with its creator, JJ Allaire. Annotated version of his presentation inspired by Simon Willison's annotated presentations.

**Author:** Hamel Husain
**Published:** June 23, 2025
**Source:** https://hamel.dev/notes/llm/evals/inspect.html

## Summary

Hamel Husain hosts JJ Allaire for a guest lecture in the LLM Evals course. JJ presents Inspect AI — an open-source framework developed during a sabbatical with the UK AI Safety Institute (AISI). Since its creation, it has been adopted by Anthropic, DeepMind, Grok, and other major AI labs.

## Key Topics

### 1. Inspect Overview
Inspect is a Python package (`inspect-ai`) bridging research and production for LLM evals. Used for nearly all UK AISI's automated evaluations, with broad adoption from major AI labs.

### 2. Motivation
Improve reproducibility of evals for large-scale frontier model evaluations. Common tools and simple entry point to run almost any benchmark with a single command.

### 3. Core Concepts: Dataset → Solver → Scorer
- **Dataset**: Test cases with `input` (prompt) and `target` (answer/grading guidance)
- **Solver**: Python function defining how the model generates output — from simple model call to complex chains with self-critique, tool use, agents
- **Scorer**: Evaluates output against target — text comparison, model-graded, or custom

### 4. Two API Views
- **High-level**: Pre-built building blocks (solvers, scorers) for quick composition
- **Low-level**: Deep universal LLM interface — caching, logging, metrics, tools, parallel execution, async Python

### 5. Agent Evaluation
- **Built-in tools**: Web Search, Bash/Python, Text Editor, Web Browser (headless Chromium), Computer (desktop screenshots), Think
- **Agent Bridge**: Monkey-patches OpenAI API to route external agent calls through Inspect's model provider. Works with OpenAI Agents SDK, Pydantic AI, LangChain, Claude Code, Codex CLI, Gemini CLI
- **Sandbox bridge**: Runs agents inside Docker containers with proxy server for API interception
- **Agent approval system**: Human-in-the-loop for sensitive actions

### 6. Composition
Custom solvers and scorers packaged as Python packages. Example: UK AISI's `Shepherd` package with jailbreak solvers.

### 7. Production Scale
- **Parallelism**: Async architecture, dozens of evaluations in parallel on a single node
- **Eval Sets**: Automatic retries, resume from last checkpoint, robust error handling
- **Logging**: Structured EvalLog files with Python API, Pandas DataFrames, log viewer

### 8. Sandbox Environments
SandboxEnvironment abstraction for isolated tool code execution. Built-in: Docker, Kubernetes, Modal, Proxmox, Local (with warning), Extension API.

## Key Insights

1. **JJ insists tools are for evals only**: "Inspect has almost all the same tools as LangChain, but our users are focused on evals — I don't want to steer people towards using them for other things." However, the browser tool is good enough for general use.

2. **Agent Bridge is the key integration pattern**: Works by intercepting OpenAI API calls — any framework using OpenAI-compatible APIs can be bridged without rewriting code.

3. **inspect view bundle**: Creates standalone static website from eval results for easy sharing (e.g., GitHub Pages).

4. **100+ external contributors**: JJ promises that if you put effort into a PR, they will work with you to get it merged.

5. **Bot detection warning**: As more LLM agents deploy, websites are improving bot detection — test browser tools for eval tasks before deploying.

## Companion Resources

- **Video**: Full presentation available on Hamel's page
- **Inspect AI Docs**: https://inspect.aisi.org.uk/
- **Inspect Evals**: https://inspect.aisi.org.uk/evals/ — 200+ pre-built benchmarks
- **GitHub**: https://github.com/UKGovernmentBEIS/inspect_ai
- **Inspect SWE**: https://meridianlabs-ai.github.io/inspect_swe/
