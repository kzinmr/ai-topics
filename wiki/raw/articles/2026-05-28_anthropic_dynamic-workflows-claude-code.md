---
title: "Introducing dynamic workflows in Claude Code"
source: "Anthropic Blog"
source_url: "https://claude.com/blog/introducing-dynamic-workflows-in-claude-code"
author: "Anthropic"
date: 2026-05-28
publication: "Anthropic Blog"
tags: [claude-code, anthropic, coding-agents, subagents, orchestration, workflow, ai-agents, multi-agent, announcement]
---

# Introducing Dynamic Workflows in Claude Code

Anthropic introduces **dynamic workflows** in Claude Code to handle complex, end-to-end tasks that would normally require quarters of planning but can now be completed in days. Claude dynamically writes orchestration scripts to run tens or hundreds of parallel **subagents** in a single session, checking its work before presenting results.

> *Work you'd normally plan in quarters now finishes in days. Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.*

## Key Capabilities

- Tackles problems too large for a single pass of a single agent, especially in complex, legacy codebases
- **Use cases include:**
  - Bug hunts across entire services
  - Migrations touching hundreds of files
  - Plans stress-tested from every angle before commitment
- Coordinates independent subagents, converges their findings, and ensures results are verified

## Availability & Plans

- **Research preview** available on:
  - Claude Code CLI, Desktop, VS Code extension
  - **Max, Team, Enterprise** (if admin enabled) plans
  - Claude API, Amazon Bedrock, Vertex AI, Microsoft Foundry
- Enterprise plans: off by default at launch; admins can enable

## How It Works

1. **Planning & decomposition** – Claude plans dynamically based on the prompt, breaks the task into subtasks
2. **Parallel execution** – Subagents run independently in parallel
3. **Verification** – Results are checked before integration; adversarial agents attempt to refute findings
4. **Convergence loop** – The run iterates until answers converge
5. **Resilience** – Progress is saved continuously; interrupted jobs pick up where they left off
6. **Conversation independence** – Coordination happens outside the conversation context

## Case Study: Rewriting Bun (Zig → Rust)

- Jarred Sumner used dynamic workflows to port Bun from Zig to Rust
- **99.8%** test suite pass rate
- ~**750,000** lines of Rust produced
- **11 days** from first commit to merge
- Workflow: lifetime mapping → file-by-file porting with 2 reviewers per file → fix loop → optimization pass

## Getting Started

- **Max / Team / API users:** Workflows on by default
- **Ultracode mode:** `/effort ultracode` sets xhigh effort + auto-workflow
- **Enterprise:** Admin must enable
- **Token warning:** Can consume substantially more tokens than typical sessions
