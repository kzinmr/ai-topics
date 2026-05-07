---
source: https://platform.claude.com/docs/en/managed-agents/dreams
title: "Dreams: Managed Agents Memory Curation"
author: Anthropic
date: 2026-05-07
tags: [claude, managed-agents, dreams, memory, curation]
---

# Dreams: Managed Agents Memory Curation

**Dreams** is a Research Preview feature for Claude Managed Agents that allows Claude to reflect on past sessions to curate, deduplicate, and reorganize an agent's memory store.

## Overview
While agents write to memory stores incrementally, these stores can become cluttered with duplicates, contradictions, or stale data. **Dreams** solve this by reading an existing memory store and past session transcripts to produce a new, optimized output memory store.

### Key Benefits
- **Deduplication:** Merges redundant entries.
- **Conflict Resolution:** Replaces stale or contradicted entries with the latest values.
- **Insight Extraction:** Surfaces new patterns and insights from session transcripts.
- **Non-Destructive:** The input store is never modified; a separate output store is created for review.

## Technical Requirements
All requests require specific beta headers:
- **Managed Agents Beta:** `managed-agents-2026-04-01`
- **Dreaming Beta:** `dreaming-2026-04-21`

## How to Create a Dream
A dream is an asynchronous job that takes a memory store and up to 100 optional session transcripts.

### Configuration Parameters
- **`inputs`**: Includes the `memory_store_id` and an optional array of `session_ids`.
- **`model`**: Supported models include `claude-opus-4-7` and `claude-sonnet-4-6`.
- **`instructions`**: Up to 4,096 characters of guidance on how Claude should prioritize information during the run.

## Lifecycle and Tracking
Dreams typically take **minutes to tens of minutes** to complete.

### Status States
- `pending` — Successfully queued.
- `running` — Pipeline is processing; `usage` updates in real-time.
- `completed` — Finished. The `outputs[]` contains the new memory store ID.
- `failed` — Terminated with error. Output store contains partial data.
- `canceled` — Run stopped by user. Output store contains partial data.

## Using the Output
Once `completed`, the output memory store is a standard resource that can be attached to future sessions.

## Limits and Billing
- **Sessions per dream:** Max 100.
- **Instructions length:** Max 4,096 characters.
- **Billing:** Charged at standard API token rates for the selected model. Cost scales linearly with the number and length of input sessions.
- **Recommendation:** Start with a small batch of sessions to verify curation quality before scaling up.

### Common Errors
- `timeout` — Pipeline exceeded runtime budget.
- `memory_store_org_limit_exceeded` — Organization hit its memory-store cap.
- `input_memory_store_too_large` — Input exceeds pipeline size limits.
- `input_memory_store_unavailable` — Input store was deleted/archived during the run.
