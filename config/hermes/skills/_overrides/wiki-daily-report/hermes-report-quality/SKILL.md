---
name: hermes-report-quality
description: Gwern-inspired quality techniques for Hermes AI reports — Anti-Examples stripping, Manual of Style (MoS), Atomic Snippets multi-level abstraction, Generate-Rank-Select iteration, and Engram knowledge pathways. Improves report tone, consistency, depth, and usefulness.
tags:
  - report-writing
  - quality
  - anti-examples
  - style-guide
  - gwern
  - atomic-snippets
---

# Hermes Report Quality — Gwern-Inspired Techniques

A set of 5 quality techniques distilled from [[concepts/llm-creative-writing|Gwern's LLM Creative Writing methodology]], adapted specifically for Hermes' wiki reports, digests, and knowledge summaries.

## Technique 1: Anti-Examples Slop Stripping

**Problem**: AI-generated reports default to a generic, "ChatGPTese" tone — verbose, hedging, and formulaic.

**Workflow**:
1. **Generate the report** as usual
2. **Self-critique**: After writing, add a self-review step: "Identify 3-5 phrases in this report that sound like generic AI prose. Explain why they're weak, then rewrite them."
3. **Reverse fix**: Apply the rewritten versions
4. **Meta-cognition check**: Force reasoning about *why* the original phrasing was weak, not just what to change

**Example application**: In daily hot-posts reports, after listing topics, add a self-review phase checking for:
- Overused transitions ("Meanwhile", "Notably", "It's worth noting")
- Vague praise ("impressive", "significant", "important" without context)
- Formulaic sentence structure (topic sentence → explanation → implication)

## Technique 2: Manual of Style (MoS) for Reports

**Definition**: An explicit style guide for Hermes' voice across all report types.

### Core Style Rules
- **Japanese for Discord/Telegram reports**: Concise bullet-driven format
- **English for Slack/technical analysis**: Precise, data-rich, no filler
- **Every claim needs a source**: Wikilink or URL citation mandatory
- **One sentence per insight**: No padding paragraphs
- **Use comparison tables** for multi-entity analysis

### Anti-Examples (what NOT to do)
- ❌ "It is worth noting that..." → ✅ Just state the fact
- ❌ "This represents a significant development in the field of..." → ✅ Name the specific field + why
- ❌ "As we move forward, it will be interesting to see..." → ✅ Make a specific prediction or state uncertainty
- ❌ Hedging everything ("may", "could", "might", "potentially") → ✅ State confidence level explicitly ("60% probability", "speculative")
- ❌ "In today's rapidly evolving AI landscape..." → ✅ Delete. Start with the content.

## Technique 3: Atomic Snippets — Multi-Level Abstraction

**Idea**: Present the same content at multiple granularity levels so the reader picks their depth.

### Three-Level Format (recommended for reports)

```
## 🔍 Topic: X (1-line summary)
**One-liner**: X just released Y, competing with Z on W.

**Details**:
- Key metric: ...
- Architecture: ...
- Comparison: ...

**Deep dive** (collapsible or optional section):
- Technical architecture details
- Benchmark methodology
- Implications for the ecosystem
```

**Implementation**: Start every report section with a one-liner (mandatory for all readers), then progressively add detail. Readers stop when satisfied.

### When to use each level

| Level | Token budget | Use case |
|-------|-------------|----------|
| One-liner | 15-30 tokens | Quick scan, headline readers |
| Details | 100-300 tokens | Interested readers, daily digest |
| Deep dive | 300-1000+ tokens | Technical deep-dive, wiki pages |

## Technique 4: Generate-Rank-Select for Critical Reports

**Problem**: First-draft reports have hidden quality variance. Gwern's insight: "Adding bits beats slop" — the value is in the search process.

**Workflow for important reports**:
1. **Generate N variants** (2-3) of the report title and opening paragraph
2. **Self-rank** by criteria: informativeness, conciseness, engagement
3. **Select & merge** the best elements
4. **Write the rest** using the selected tone

**When to apply**: When a report has strategic importance (trend analysis, ecosystem comparison, or any report with decision-making implications). Skip for routine "no change" reports.

**Catch**: Don't spend tokens on G-R-S for every report — reserve for:
- Weekly digests
- Trend analysis
- Reports with specific predictions
- Reports the user has indicated high interest in

## Technique 5: Engram Knowledge Pathways

**Problem**: The model has knowledge it can't recall at generation time — like engrams with few access paths.

**Workflow before report generation**:
1. **Pre-load context**: Scan wiki for 3-5 related pages before writing
2. **Cross-reference injection**: Embed wikilinks to related concepts inline
3. **Tag expansion**: Include tags from related pages in the report's reference section
4. **Multiple query angles**: Before writing, ask yourself "what are 3 different ways this topic connects to existing wiki knowledge?" — then use the richest angle

**Anti-pattern**: Generating a report from scratch without checking what the wiki already knows about the entities and concepts mentioned.

## Applying to Existing Cron Jobs

### Slack Hot Posts (`ai-topics-slack-hot-posts` — every 4h)
This is the highest-visibility report.

**Current impl status (May 2026):** T1-T5 instructions are embedded **inline in the prompt body** (not just via skill loading). Do NOT suggest adding T1-T5 — it's already done. The prompt has explicit:
- T1 Anti-Examples slop-stripping checklist
- T2 MoS (style, wikilinks, comparison tables)
- T3 Atomic Snippets (One-liner + Details)
- T5 Engram Pathways (pre-scan related_wiki_pages)
- Per-slot posting guidance (morning/midday/evening/night/late-night/pre-morning)

**If adding new quality guidance:** Append to the existing Quality Requirements section in the prompt rather than duplicating.

### Dreaming Wiki Ingest (`dreaming-wiki-ingest` — daily)
- **Anti-Examples (T1)**: Strip generic analysis from nightly consolidation
- **Generate-Rank-Select (T4)**: For the top 1-2 findings, generate alternatives
- **Atomic Snippets (T3)**: Summary → Detailed findings → Technical appendix
- **Engram (T5)**: Cross-wiki context for each consolidated theme

### Weekly AI Digest (telegram, weekly)
- **All 5 techniques** — this is the highest-stakes report

## Reference

- [[concepts/llm-creative-writing]] — Full Gwern methodology
- [[entities/gwern]] — Gwern Branwen
- [[wiki/index.md]] — Current wiki state
