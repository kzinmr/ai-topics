---
title: "Mid-conversation system messages — Claude Platform Docs"
source: "https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages"
scraped: 2026-06-07
type: raw-article
tags: [claude-api, prompt-caching, context-engineering, system-messages, claude-opus]
---

# Mid-conversation system messages — Claude Platform Docs

> Add or update system instructions partway through a conversation without invalidating the cached prefix that came before them.

## Overview

System instructions normally live in the top-level `system` field, ahead of every message in the conversation. That position is great for prompt caching: the system prompt is part of the stable prefix, so subsequent turns hit the cache. It is a poor position for instructions you only discover you need partway through a session, because editing the top-level system field changes the very beginning of the prompt and invalidates the cache for everything that follows.

Mid-conversation system messages close that gap. You append a `{"role": "system"}` message at the point in the conversation where the new instruction becomes relevant, instead of editing the top-level system field. The cached prefix stays the same, so the next request still reads it from cache, and the new instruction is still applied as a system instruction rather than as ordinary user text.

**Availability:** Claude API and Claude Platform on AWS. **Not available** on Amazon Bedrock, Vertex AI, or Microsoft Foundry. **Model:** Claude Opus 4.8 only. No beta header required.

## How it works

Prompt caching hashes the request prefix in order: `tools`, then `system`, then `messages`. A cache hit requires the prefix to match a recent request exactly, byte for byte, up to the cache breakpoint. That ordering means the top-level system field sits near the very start of the hashed prefix. Any change to it, even appending a sentence, produces a different hash, and the request misses the cache for the system prompt and every cached message after it.

Mid-conversation system messages let you add the instruction at the end of the message history instead. Everything before the new instruction is unchanged, so the existing cache entry still matches, and only the new message is processed as fresh input.

## Use cases

1. **Mid-session policy or persona changes** — A long agentic session needs a new constraint ("from now on, write all SQL as parameterized queries") after dozens of cached turns. Adding it to the top-level system field would re-process the entire history.

2. **Per-turn context that must be authoritative** — You want to inject a freshness note, a session deadline, or a tool-availability change with system-level weight, and it changes too often to live in the cached prefix.

3. **State changes your application observes** — Your application notices something Claude should treat as an operator-level fact: files changed on disk, the user toggled an auto-approve setting, available tools changed, or the remaining token budget dropped below a threshold.

4. **User input that should not interrupt an agentic loop** — A user types a follow-up while Claude is still executing tools for the previous request. Relaying it as a system message after the next tool result lets Claude fold the new input into the work it is already doing, instead of treating it as a fresh request to switch to. See "Placement after tool results" below.

5. **Mode switches that grant standing permissions** — A session-level mode can use a mid-conversation system message to grant specific permissions or change behavior for the remainder of the session.
