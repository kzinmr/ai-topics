---
title: "CodeAct — Microsoft Agent Framework"
created: 2026-05-20
author: Microsoft
source: Microsoft Learn
url: https://learn.microsoft.com/en-us/agent-framework/agents/code_act
type: article
tags: [code-act, microsoft, agent-framework, sandbox, hyperlight, plan-then-execute]
---

# CodeAct — Microsoft Agent Framework

Microsoft's implementation of the CodeAct pattern in Agent Framework. Unlike the original academic CodeAct (which uses a multi-turn interpreter loop), the Agent Framework version collapses tool orchestration into a single `execute_code` call per turn — the model writes a program that runs once in a sandbox, combining control flow, data transformation, and tool orchestration.

## Core Mechanism

CodeAct lets an agent solve tasks by writing and executing code through a single `execute_code` tool. Instead of emitting one tool call per model turn (`model → tool → model → tool → …`), the agent expresses its entire plan as a program that runs once inside a sandbox.

### Default Agent Pattern vs. CodeAct

| Default | CodeAct |
|---------|---------|
| model → tool → model → tool → … | model → one execute_code call → result |
| N round-trips | 2 round-trips total |
| Each tool call requires model turn | Entire plan runs as one program |

## When to Use

**Use CodeAct when:** combining multiple tool calls with loops/branching/filtering/aggregation, transforming tool results before answering, generating large structured outputs, or collapsing many small lookups into one step.

**Stay with direct tool calling when:** only 1-2 tool calls needed, each call has side effects requiring individual visibility, or per-call approval prompts are needed.

## Hyperlight CodeAct Connector

The only documented connector — available for both .NET and Python (preview):

- Adds `execute_code` tool to model-facing tool surface
- Supplies sandbox runtime instructions
- Optionally exposes provider-owned tools via `call_tool(...)`
- Applies capability limits (filesystem access, outbound-network allow lists)

### .NET Package
`Microsoft.Agents.AI.Hyperlight` — provides `HyperlightCodeActProvider`, `HyperlightExecuteCodeFunction`, sandbox configuration (FileMounts, AllowedDomains), and approval mode integration. Depends on `Hyperlight.HyperlightSandbox.Api` NuGet (not yet published on nuget.org).

### Python Package
Hyperlight CodeAct (preview) — provides `HyperlightCodeActProvider`, `HyperlightExecuteCodeTool`, and runtime-specific guidance.

## Limitations
- Only Hyperlight connector documented (preview)
- Approvals apply to the entire execute_code call (not per-operation)
- Tools via `call_tool(...)` execute in host process — use narrow, reviewed host tools for sensitive I/O
- Best when orchestration overhead dominates; adds little value for small tasks
