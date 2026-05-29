---
type: external_article
title: "Mid-conversation system messages — Claude API Docs"
source: https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages
date: 2026-05-28
tags:
  - claude
  - prompt-caching
  - prompt-engineering
  - anthropic
---

# Mid-conversation system messages — Claude API

Add or update system instructions partway through a conversation **without invalidating the cached prefix** that came before them.

## Feature Overview

System instructions normally live in the top-level `system` field, ahead of every message in the conversation. That position is great for prompt caching — the system prompt is part of the stable prefix, so subsequent turns hit the cache. It is a poor position for instructions you only discover you need mid-session, because editing the top-level `system` field changes the very beginning of the prompt and invalidates the cache.

Mid-conversation system messages close that gap. You append a `{"role": "system"}` message at the point in the conversation where the new instruction becomes relevant. The cached prefix stays the same; the next request reads from cache. The new instruction is still applied as a system instruction (with system-level authority) rather than as ordinary user text.

**Availability**: Claude API + Claude Platform on AWS. NOT on Bedrock, Vertex AI, or Foundry. Available without beta header as of claude-opus-4-8.

## Why Position Matters for Caching

Prompt caching hashes the request prefix in order: `tools` → `system` → `messages`. A cache hit requires the prefix to match a recent request exactly, byte for byte, up to the cache breakpoint.

The top-level `system` field sits near the very start of the hashed prefix. Any change to it, even appending a sentence, produces a different hash. The request misses the cache for the system prompt AND every cached message after it.

Mid-conversation system messages place the new instruction at the END of the message history, preserving everything before it unchanged.

## Use Cases

- **Mid-session policy/persona changes** — Add a constraint (e.g., "from now on, write all SQL as parameterized queries") after dozens of cached turns
- **Per-turn authoritative context** — Inject freshness notes, session deadlines, or tool-availability changes with system-level weight, changeable without cache break
- **Tool results that reshape behavior** — A tool returns a fact that should govern all future turns (e.g., "the customer is on the enterprise plan; don't suggest the consumer upgrade flow")
- **Mode switches granting standing permissions** — Grant temporary consent to expensive capabilities with periodic refresher and exit notice

## Precedence Rules

- Later system messages take precedence over earlier ones
- Mid-conversation system messages override the top-level `system` field for turns that follow them
- Keep top-level `system` for permanent, session-wide instructions. Reserve mid-conversation system messages for instructions that become relevant later.

## Example (Python)

```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="You are a code review assistant. Be concise.",
    messages=[
        {"role": "user", "content": "Review process() in utils.py"},
        {"role": "assistant", "content": "The list comprehension is fine for small inputs..."},
        {"role": "user", "content": "Now review the calling code that invokes process()."},
        # Mid-session: add typing policy without cache invalidation
        {"role": "system", "content": "Enforce strict typing from now on. All suggestions must pass mypy --strict."},
    ]
)
```
