---
title: "Implementing Programmatic Tool Calling on Amazon Bedrock — Shreyas Subramanian, Pratik Raichura, River Xie"
created: 2026-05-19
author: Shreyas Subramanian, Pratik Raichura, River Xie
source: AWS Machine Learning Blog
url: https://aws.amazon.com/jp/blogs/machine-learning/implementing-programmatic-tool-calling-on-amazon-bedrock/
type: article
tags: [aws, bedrock, agent-infrastructure, sandbox, tool-use, ai-agents, agent-architecture, serverless, docker, ecs, agentcore, claude, token-economics, cost-optimization]
---

# Programmatic Tool Calling (PTC) on Amazon Bedrock

AWS blog post introducing Programmatic Tool Calling — a paradigm where LLMs write Python code to orchestrate multiple tool calls within a sandbox, rather than calling tools sequentially through the model. Covers three implementations: self-hosted ECS + Docker sandbox, managed AgentCore Code Interpreter, and Anthropic SDK-compatible proxy.

## What is PTC?

PTC shifts LLM tool interaction from sequential, one-at-a-time invocations to **code-orchestrated execution** within a sandbox. Instead of multiple model round-trips per tool call, the model writes a single Python script that invokes tools programmatically (loops, conditionals, parallelism, filtering), executes it in a sandbox, and returns only the final processed result to the model's context.

**Core benefits:**
- **87–92% token reduction** — intermediate data never enters the context window
- **Improved accuracy** — data processing uses deterministic Python, not natural language reasoning
- **Reduced latency** — tools can run in parallel; model sampled only twice (code generation + final interpretation)
- **Model-agnostic** — works with any Amazon Bedrock model that supports tool use

## Bottleneck Example: Expense Audit

**Task:** "Which engineering team members exceeded their Q3 travel budget?"

Traditional sequential tool calling: 20 `get_expenses` calls → 2,000+ records → all enter model context → model reasons over full dataset in natural language. Problems: token consumption (thousands of intermediate records), latency (20+ round trips), accuracy (LLMs struggle with large tabular data).

PTC: model generates a single Python script using `asyncio.gather()` for parallel tool calls, Python filtering/aggregation, only final `print()` output reaches model context.

## Three Implementation Paths

### Part 1: Self-Hosted PTC with ECS + Docker Sandbox

**Architecture**: Orchestrator (ECS/Lambda calling Bedrock `InvokeModel` via Boto3) + Docker sandbox with IPC over stdin/stderr.

**Key design**: Tool definitions removed from `tool_config` and injected into system prompt. System prompt instructs model to write Python code calling async tool functions. Model's `tool_use` block contains the Python code. Orchestrator extracts code, runs in Docker sandbox, intercepts tool calls via IPC, executes externally, returns results to container. Only final `print()` output sent as `tool_result`.

**Why self-host**: Model-agnostic, full control over sandbox (custom packages, security), private deployment.

### Part 2: Managed via AgentCore Code Interpreter

**Fully managed** alternative. Code Interpreter is a built-in tool in Bedrock AgentCore that provides a managed sandbox. The service handles sandbox lifecycle, security isolation, and scaling.

**Benefits**: No Docker management, no IPC protocol implementation, automatic sandbox cleanup, integrated monitoring via CloudWatch.

### Part 3: Anthropic SDK Compatible (Proxy-Based)

A proxy translates between the Anthropic SDK interface and Amazon Bedrock's API. Teams using the Anthropic SDK (`anthropic.Anthropic()`) can adopt PTC without rewriting their application code. The proxy handles model translation, sandbox management, and the full PTC protocol transparently.

**Recommended for**: Teams preferring the Anthropic SDK interface while using Amazon Bedrock for model inference.

## Experimental Results (Expense Audit Task)

8 team members, 20-50 expense records per person per quarter, custom budget exceptions.

| Model | PTC tokens | Non-PTC tokens | Token reduction | PTC accurate | Non-PTC accurate |
|---|---|---|---|---|---|
| Claude Sonnet 4.6 (adaptive) | 12,739 | 128,043 | 90.1% | Yes | Yes |
| Claude Opus 4.6 (adaptive) | 13,043 | 126,152 | 89.7% | Yes | Yes |
| Qwen3-Coder-480B | 34,159 | 305,114 | 88.8% | Yes | No |
| Qwen3-Next-80B | 28,878 | 233,332 | 87.6% | Yes | No |
| DeepSeek V3.2 (thinking) | 19,543 | 245,967 | 92.1% | Yes | No |
| MiniMax M2.1 (thinking) | 11,787 | 101,990 | 88.4% | Yes | No |
| Kimi 2.5 (thinking) | 10,875 | 148,085 | 92.7% | Yes | No |
| GLM 4.7 (thinking) | 11,550 | 115,829 | 90.0% | Yes | No |

**Key findings:**
- PTC mode: ALL 8 models produced correct answers. Non-PTC: only Claude models got it right.
- Token reduction 87-92% across all models.
- The same Docker sandbox, IPC protocol, and orchestrator worked across all models — only `model_id` changed.

## Cost Analysis

Based on Claude Sonnet pricing ($3/$15 per 1M input/output tokens), 1,000 executions/day:

| Metric | Non-PTC | PTC |
|---|---|---|
| Daily cost | ~$520 | ~$52 |
| Monthly cost | ~$15,600 | ~$1,560 |
| Monthly savings | — | ~$14,040 (90%) |

## Conclusion

Three ways to implement PTC on Amazon Bedrock:
1. **Self-hosted on ECS** — Full control, Boto3 + Docker sandbox, maximum flexibility
2. **AgentCore Code Interpreter** — Fully managed sandbox, less operational overhead
3. **Anthropic SDK compatible** — Proxy-based, drop-in replacement for Anthropic SDK users

All approaches are model-agnostic, privately deployed within AWS account, and extensible to new models.

## Authors

- **Shreyas Subramanian** — Principal Data Scientist, AWS. GenAI, deep learning, Agentic AI. Reviewer for NeurIPS, ICML, ICLR, NASA, NSF.
- **Pratik Raichura** — Principal SDE, AWS. 10+ years building AI services (Amazon Bedrock, Amazon Lex). Distributed systems, AI inference infrastructure.
- **River Xie** — Senior GenAI Specialist SA, AWS CMHK. Data science, recommendation systems, LLM fine-tuning, Agentic AI.

## Connection to Wiki Concepts

- [[concepts/agent-hosting-aws]] — PTC is the sandbox execution model detailed in this page
- [[concepts/programmatic-tool-calling]] — Dedicated concept page for the PTC paradigm
- [[entities/amazon-bedrock]] — Bedrock as the LLM backend
