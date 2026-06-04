---
title: "Dreaming: Better memory for a more helpful ChatGPT"
source_url: https://openai.com/index/chatgpt-memory-dreaming/
author: OpenAI
date: 2026-06
fetched: 2026-06-04
type: raw-article
---

# Dreaming: Better memory for a more helpful ChatGPT

Published by OpenAI, June 2026

## Introduction

ChatGPT's ability to remember you has always been central to making it a truly helpful assistant. Today, we're introducing Dreaming, a fundamentally redesigned memory system that allows ChatGPT to consolidate, organize, and recall information more efficiently and accurately than ever before. Dreaming moves beyond static fact-storing to a dynamic, sleep-like consolidation process that keeps your memory clean, relevant, and instantly accessible.

## The Challenge with Long-Term Memory

In previous iterations, ChatGPT stored memories as linear appendices to your conversation context. Over weeks and months, this approach led to several friction points:

- **Context bloat**: Older, less relevant memories crowded the active window.
- **Contradictory recall**: New preferences sometimes overwrote older ones without resolution.
- **Latency spikes**: Retrieving scattered facts slowed down response times.
- **Poor generalization**: The system struggled to connect related memories into useful patterns.

Users told us they wanted an assistant that could remember what mattered, forget what didn't, and actually understand how their information evolved over time. Dreaming was built to solve exactly that.

## How Dreaming Works

Dreaming introduces an asynchronous consolidation pipeline inspired by human memory processing during sleep. Instead of storing every detail in real time, ChatGPT now:

- Captures raw interaction signals during active sessions
- Triggers a low-cost "dreaming" cycle during idle periods or overnight windows
- Runs semantic deduplication, relevance scoring, and conflict resolution
- Compresses and organizes validated memories into a structured knowledge graph
- Updates the active retrieval index for seamless next-session recall

This offline processing happens entirely on OpenAI's secure infrastructure. When you return to ChatGPT, the memory system is already optimized, resulting in faster load times and significantly more accurate personalization.

## Technical Architecture

Dreaming is built on a three-tier architecture:

1. **Buffer Layer**: Temporary storage for active session data. Handles real-time memory tagging and short-term retention.
2. **Consolidation Engine**: The core "dreaming" module. Uses lightweight summarization models, temporal decay functions, and graph-based relationship mapping to merge, prune, and structure memories.
3. **Long-Term Index**: A highly compressed, vector-optimized knowledge store. Memories are indexed by relevance, recency, and user-defined priority, enabling sub-millisecond retrieval during generation.

The consolidation engine runs at a fraction of the computational cost of real-time inference. By decoupling memory processing from active chatting, we've reduced average memory-related latency by 68% while doubling effective retention capacity.

## Privacy, Transparency, and Control

Your memory belongs to you. Dreaming includes comprehensive controls to ensure full transparency and user agency:

- **Memory Dashboard**: View every stored fact, grouped by category, project, or relationship.
- **Edit & Prune**: Modify, split, or delete individual memories at any time.
- **"Sleep Schedule"**: Configure when Dreaming runs (e.g., during specific hours or only after explicit user triggers).
- **Data Isolation**: Dreaming processes are end-to-end encrypted. Consolidated memories are never used for model training or shared with third parties.
- **Full Reset**: One-click wipe to clear all memory and start fresh.

We've also added contextual recall receipts. Whenever ChatGPT uses a remembered fact in a response, you can hover to see exactly which memory was referenced and how it influenced the output.

## Early Results

In controlled beta testing across 500,000 users, Dreaming delivered measurable improvements:

- 73% reduction in memory-related hallucinations
- 41% increase in personalization accuracy over the previous system
- 62% fewer user-initiated memory corrections
- 89% of testers reported ChatGPT felt "more in sync" with their ongoing work and communication style

## Availability and Rollout

Dreaming is rolling out in phases:

- **Phase 1** (Starting today): Available to Plus, Pro, and Team subscribers.
- **Phase 2** (Q3 2026): Enterprise and Education deployments with admin-controlled memory scopes.
- **Phase 3** (Late 2026): Lightweight Dreaming tier for Free users, featuring core consolidation without advanced graph features.

## What's Next

Dreaming is the foundation for more persistent, context-aware AI. Upcoming features include:

- **Cross-Workspace Sync**: Carry consolidated memories seamlessly between ChatGPT web, desktop, and mobile apps.
- **Proactive Clarification**: The model will ask lightweight, targeted questions to resolve memory gaps or ambiguities.
- **Collaborative Memory**: Shared, permissioned memory layers for teams, enabling ChatGPT to understand group dynamics and project history.
- **Memory Export/Import**: Download your structured knowledge graph or migrate memories to other compatible AI assistants.

## Conclusion

We're building assistants that don't just answer questions, but grow alongside you. Dreaming represents a fundamental shift from reactive fact-storing to proactive, intelligent memory management. Thank you to everyone who participated in our beta and helped shape this release. Your feedback remains critical as we continue to refine how AI remembers, understands, and supports you.

For full documentation, privacy policies, and rollout timelines, visit openai.com/chatgpt/memory.
