---
title: "Hermes Harness Architecture"
type: x_article
x_article_title: "Hermes Harness Architecture"
x_article_author: "Atal Upadhyay (@atal)"
getxapi: false
created: 2026-05-29
sources:
  - https://x.com/i/article/2060381072148537344
---

# Hermes Harness Architecture

Hermes (from @NousResearch) is one of the best open-source harnesses in the ecosystem right now. We wanted to look at the implementation directly and map what we found to the framework we use for analyzing harnesses.

In our earlier piece, "What is an Agent Harness," we used a nine-part model:
- outer iteration loop
- context management and compression
- skills and tools management
- subagent management
- built-in pre-packaged skills
- session persistence and recovery
- system prompt assembly with project context injection
- lifecycle hooks
- permission and safety layer

Hermes implements all nine. The interesting details are in how it implements them, and in the extra systems that sit outside this frame.

## The outer iteration loop

The core loop is familiar: model call, tool dispatch, tool result append, repeat until final response or interrupt.

Where Hermes is stronger than most open harnesses is provider abstraction. The same runtime can drive chat-completions style APIs, Anthropic Messages, Codex Responses, an out-of-process Codex app-server path, and Bedrock. Tool-call formats and provider quirks are normalized by transport adapters. At the loop level, the model surface looks consistent. For those of us, who really like having an open harness provider who supports all models, this open approach is much better than Claude Code.

## Context management and compression

Hermes has a full compression path, not a simplistic context trim.

Older turns are summarized by an auxiliary model. Head and tail segments are protected by token budget. Tool outputs that are older than a configurable threshold are pruned before summarization. The summary budget scales with compressed content at roughly twenty percent, with a two-thousand-token floor and a twelve-thousand-token ceiling. In practice this avoids spending too much context on tiny compressions while still giving large compressions enough room to be useful.

Compression is also a session lifecycle event. On compression, Hermes closes the current SQLite session row, creates a child session seeded by the summary, rotates the session ID, and records parent-child lineage. Plugin context engines and memory providers are notified that a boundary moved. If a long conversation compresses multiple times, you get a lineage chain instead of one repeatedly rewritten transcript. This is pretty unique relative to other harness architectures we've reviewed.

## Skills and tools management

Tool registration and tool exposure are separate concerns in Hermes.

Tools register into a central registry at import time. A separate toolset layer decides what the model actually sees in a given run. That exposed set is scoped by platform and scenario, and can be narrowed again for delegated runs. A profile has its own enabled footprint.

This separation matters operationally. You can keep a broad installed tool library while keeping any single run's model-visible surface small enough to manage for token cost and safety.

## Subagent management

Delegation primitives are solid. A child run gets its own task ID, its own terminal context, and returns a structured summary to the parent. Dangerous commands default to deny in delegated contexts, and recursion depth is capped.

The current limit is lifecycle ownership. Most child work still lives under the parent call path. When the parent is done, the child is done. There is not yet a durable, externally steerable child-run plane with independent control semantics.

## Session persistence and recovery

This is where Hermes departs most from editor-first harnesses.

Session state is stored in SQLite with FTS5 search and WAL journaling, with fallback behavior for filesystems that cannot support WAL coordination. Sessions track source tags for turns, parent-child lineage for compression splits, and metadata the gateway can use to resolve routing before the model runs.

That design effectively treats sessions as runtime infrastructure, not just transcripts for resume. CLI, messaging platforms, and scheduled jobs can all attach to the same session plane. A message can be routed to the right session before inference. A scheduled job can write to a session even with no active terminal.

Hermes also exposes a model-facing session_search tool for focused recall over prior sessions. This is a concrete example of pushing context management decisions into the model loop itself rather than relying only on static injection.

## System prompt assembly and project context injection

Hermes explicitly composes the system prompt in three tiers: stable, context, and volatile.

The stable tier carries identity (SOUL.md when present), tool guidance for enabled tools only, skills index content, environment hints (like Tmux/container detection), and platform hints. The context tier reads project files from cwd (AGENTS.md, CLAUDE.md, .cursorrules) and runs prompt-injection scanning before loading that content. The volatile tier carries memory snapshots, user profile material, external memory-provider blocks, and a timestamp line with model/provider metadata.

The tiering itself is explicit in code, which makes invariants easier to reason about. Stable stays stable, context stays cwd-derived, volatile changes turn-by-turn. Prompt rebuild is tied to compression and related invalidation points, which helps keep prompt prefixes cache-friendly across normal turns.

## Lifecycle hooks

Hermes has two hook surfaces with different trust models.

First, plugin lifecycle hooks run inside the harness process and can block, rewrite, or pass through operations at events like pre/post tool call, gateway pre-dispatch, and approval request/response. Second, filesystem-driven gateway hooks let users install shell or Python scripts that run on events like gateway startup, agent step, and command-triggered paths.

Architecturally, both surfaces serve the same purpose: policy enforcement, auditing, and host side-effects should execute independently of model cooperation.

## What Hermes adds beyond the framework

Three subsystems stand out beyond the nine-component harness model.

The first is the messaging gateway. Hermes supports a broad platform adapter surface (Telegram, Discord, Slack, WhatsApp, and others) and routes traffic through a shared session model. This feels like a user interface experience that was successful with OpenClaw, designed for user interaction with long running agents.

The second is the profile system. A profile is an isolated agent root. Two profiles on the same machine behave like two different agents from a state and footprint perspective.

The third is cron as a first-class subsystem. Jobs are durable, gated by the same permissions machinery as interactive sessions, delivered through gateway paths, and isolated per profile. That forces unattended operation concerns into the main architecture rather than leaving them as peripheral scripts.

## Where we think Hermes should go next

The obvious next step is moving from strong delegation to first-class orchestration.

delegate_task already produces useful worker behavior and structured returns. What is still missing is durable child-run control: run IDs, explicit lifecycle management, external steering, and cleanup semantics that survive parent completion. Hermes already has much of the substrate through session infrastructure and gateway routing. Promoting child runs to first-class control-plane objects is the most natural next architectural step. It is one of the gaps we see versus the OpenClaw agent orchestraction layer.

## To close

Hermes already has excellent execution quality and a strong systems foundation for an open harness. It is probably one of the best open model harnesses in the ecosystem. The pace of shipping is ... insane, and most of the hard substrate work is already in place. Excited to see agent orchestration layer mature on top of that base. Hermes can already support much broader long-lived agent workloads than typical coding harnesses handle today, excited to see where it goes.

This piece references my previous What is an Agent Harness, as framing, and is informed by Swarm management in agent harnesses, plus Anthropic's posts on Managed Agents.
