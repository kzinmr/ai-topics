---
title: "Prompt Caching (Paged Attention & API-Level Patterns)"
type: concept
created: 2026-05-09
updated: 2026-05-29
status: L2
tags:
  - kv-cache
  - inference
  - optimization
  - infrastructure
sources:
  - "[[raw/articles/2025-11-30_sankalp_prompt-caching-internals]]"
related:
  - "[[concepts/kv-cache]]"
  - "[[concepts/vllm]]"
  - "[[concepts/speculative-decoding]]"
  - "[[concepts/llm-inference]]"
---

# Prompt Caching (Paged Attention & Automatic Prefix Caching)

Prompt caching is an optimization technique where LLM providers reuse pre-computed KV caches for identical prompt prefixes, skipping redundant computation.

## Why It Matters

- **Cost Reduction**: When cache hits, no prefill computation is needed → significant per-token cost reduction (Anthropic: cache writes +25%, reads -90%)
- **Latency Reduction**: Skipping the prefill phase → reduced time-to-first-token (TTFT)
- **Agent System Prompt Optimization**: Caching long system prompts + tool definitions speeds up entire agent sessions

## How It Works

### KV Cache Basics

In decoder transformers, the Key/Value tensors from all previous tokens are reused during each token generation. This is the KV cache.

```
prefill phase: Process all prompt tokens in parallel → generate KV cache (compute-bound)
decode phase:   Auto-regressively generate one token at a time → reference KV cache (memory-bound)
```

### Paged Attention (vLLM)

Problems with traditional KV cache allocation:
- Pre-allocating contiguous memory up to max sequence length → **fragmentation and waste**
- Inefficient for variable-length sequences

Paged Attention's solution (inspired by OS virtual memory):
- Split KV cache into **fixed-size blocks**
- Map logical→physical blocks via a **block table**
- Dynamically allocate blocks as needed → zero memory waste

```
Sequence: [tok1, tok2, tok3, tok4, tok5]
Block (size=2): [Block A: tok1-2] [Block B: tok3-4] [Block C: tok5]
Block Table: [A, B, C]
```

### Automatic Prefix Caching (APC)

Leveraging Paged Attention's block structure:
1. Hash the contents of each block
2. Match prefix blocks of new requests against existing cache
3. Cache hit up to the **Longest Common Prefix**
4. Only prefill the remainder

```
Request 1: [sys prompt] [user: "translate A"] [assistant: "translation A"]
Request 2: [sys prompt] [user: "translate B"]
→ sys prompt portion is a cache hit
```

## Optimization Tips

1. **Place static content at the front**: System prompts, tool definitions, and static context should always be at the start of the message array
2. **Place dynamic content at the back**: User-specific data, search results, and other variable content at the end
3. **Share the same system prompt across all sessions**: Cache is shared even between different users
4. **Images/files break the cache**: Do not place multimodal content in the prefix

## Major Provider Support

| Provider | Method | Notes |
|-------------|------|------|
| Anthropic | Custom implementation | Cache writes +25% / reads -90%, min 1024 tokens |
| OpenAI | Auto-caching | Automatically detects overlapping prefixes from recent requests, 50% discount |
| DeepSeek | Disk caching | Offloads KV cache to SSD, supports ultra-long contexts |
| Google Gemini | Context caching | Explicit cache creation API, TTL-based |

## API-Level Caching Patterns

Beyond the inference-level KV cache, API providers expose caching at the request level. The key constraint: cache hits require byte-for-byte identical prefixes. Any change to the beginning of the request invalidates all cached content downstream.

### Mid-Conversation System Messages (Claude Opus 4.8)

Anthropic's mid-conversation system message feature (May 2026) allows injecting system-level instructions at the END of the message history without changing the prefix. This preserves prompt cache for all preceding turns while still applying the new instruction with system-level authority.

**How it works**: Insert `{"role": "system", "content": "new instruction"}` at any point in the `messages` array. The instruction applies from that point forward, with later messages overriding earlier ones and the top-level `system` field.

**Key use cases**:
- **Mid-session policy changes** — Add constraints after dozens of cached turns (e.g., "from now on, write all SQL as parameterized")
- **Per-turn authoritative context** — Inject freshness notes, session deadlines without cache break
- **Tool results reshaping behavior** — Tool returns a fact governing all future turns
- **Mode switches** — Grant temporary permissions for expensive capabilities with exit notice

**Trade-off**: Caches the prefix but adds tokens for each injected system message. Best for sessions where the instruction is needed for dozens of subsequent turns — amortizes the token cost.

Source: [Anthropic Docs — Mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)

## References

- [How prompt caching works — sankalp's blog](https://sankalp.bearblog.dev/how-prompt-caching-works/) (2025-11-30) — Detailed explanation of Paged Attention + APC
- vLLM paper: [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) (Kwon et al., 2023)
