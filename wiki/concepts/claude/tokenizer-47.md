---
title: "Claude 4.7 Tokenizer Change"
type: concept
created: 2026-04-20
updated: 2026-05-27
tags:
  - concept
  - anthropic
  - model
related: [context-window-management, context-compaction, claude-opus]
sources: []
---

# Claude 4.7 Tokenizer Change

Claude Opus 4.7 was released on April 16, 2026, and **changed the tokenizer for the first time**. This change causes the same input text to be mapped to 40% more tokens.

## Key Changes

### Token Multiplier (Opus 4.6 → 4.7)

| Content Type | Multiplier |
|--------------|-----------|
| System prompt (raw text) | **1.46x** |
| High-resolution image (3456×2234, 3.7MB) | **3.01x** |
| Small image (682×318) | ~1.01x (negligible) |
| Text-heavy PDF (15MB, 30 pages) | 1.08x |

### Detailed Test Results

**System Prompt:**
- Opus 4.7: 7,335 tokens
- Opus 4.6: 5,039 tokens
- Multiplier: 1.46x

**Large Image (3456×2234, 3.7MB PNG):**
- Opus 4.7: 4,744 tokens
- Opus 4.6: 1,578 tokens
- Multiplier: 3.01x

**PDF Test (15MB, 30 pages):**
- Opus 4.7: 60,934 tokens
- Opus 4.6: 56,482 tokens
- Multiplier: 1.08x

## Pricing Impact

Opus 4.7 maintains the same pricing as Opus 4.6:

| Token Type | Price per Million Tokens |
|-----------|--------------------------|
| Input | $5.00 |
| Output | $25.00 |

**Result**: Approximately **40% cost increase** for typical text content.

## High-Resolution Image Support Improvement

> "Opus 4.7 improves high-resolution image support: supports up to 2,576 pixels on the long side (~3.75 megapixels), over 3x the previous Claude models"

The 3x token increase for large images is **entirely due to higher-resolution support**, not inefficiency.

## Implications

1. **Text-heavy content**: Expect ~1.1-1.5x token increase with Opus 4.7
2. **High-resolution images**: 3x token increase, but enables larger image inputs
3. **Cost impact**: ~40% higher cost for typical text usage
4. **Small images**: No significant difference between versions

## Related Items

- [Context Window Management](../context-window-management.md)
- [Context Compaction](../context-compaction.md)
- [Claude Opus](../entities/claude-opus.md)

## See Also

- [[concepts/_index]]
- [[concepts/claude/memory-tool]]
- [[concepts/claude-code/claude-code-source-patterns]]
- [[concepts/claude/mythos-preview]]
- [[concepts/claude-code/claude-code-leak]]
