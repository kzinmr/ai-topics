# Introducing Claude Opus 4.8

**Source:** https://www.anthropic.com/news/claude-opus-4-8
**Date:** May 28, 2026
**Author:** Anthropic

## Key Announcements

- **Claude Opus 4.8** released — builds on Opus 4.7 with improvements across benchmarks
- **Pricing unchanged:** $5/M input, $25/M output (same as Opus 4.7)
- **Fast mode:** 2.5× speed, 3× cheaper than previous fast tiers ($10/M input, $50/M output)
- **1M token context window**

## New Platform Features

1. **Dynamic Workflows** (Claude Code, research preview) — Claude plans work, spawns hundreds of parallel subagents, verifies outputs before reporting back. Example: 750,000-line codebase migration in 11 days with 99.8% test pass rate.
2. **Effort Control** (claude.ai and Cowork) — Users choose high/extra/max effort levels per request. Trade speed against quality explicitly.
3. **Mid-message system entries** (Messages API) — System instructions injectable inside message array without breaking prompt cache or routing through user turns.

## Benchmarks

| Benchmark | Opus 4.8 Score |
|-----------|---------------|
| SWE-bench Pro (agentic coding) | 69.2% |
| Humanity's Last Exam (reasoning, with tools) | 57.9% |
| OSWorld-Verified (computer use) | 83.4% |
| Finance Agent v2 | 53.9% |
| Online-Mind2Web (browser agents) | 84% |
| Magi's Super-Agent | Only model to complete every case end-to-end |
| Legal Agent Benchmark (all-pass standard) | First model to break 10% |

## Honesty Improvement

Opus 4.8 is **4× less likely** than Opus 4.7 to let code flaws pass unremarked. Trained to flag uncertainties and avoid unsupported claims.

## Project Glasswing & Claude Mythos

- Mythos Preview available to ~50 partners (Apple, Google, Microsoft, AWS)
- Found 10,000+ high/critical vulnerabilities in critical software infrastructure
- Mythos-class models expected "in the coming weeks" after cyber safeguards finalized
- Model sits a full capability tier above Opus 4.7

## Anthropic Funding

- $65B Series H at $965B post-money valuation
- Revenue grew from ~$1B (end 2024) to ~$30B annualized run rate (2026)
- Previous: $30B Series G at $380B valuation (Feb 2026)

## Third-Party Endorsements

- **Cognition:** Opus 4.8 uses tools cleanly, fixes comment-verbosity and tool-calling issues from 4.7
- **Cursor:** Improvements across every effort level on CursorBench
- **Harvey:** Highest score on Legal Agent Benchmark, first model to break 10%
- **Databricks:** Opus 4.8 in Genie agent — 61% cheaper token cost than 4.7
- **Hebbia:** Better citation precision and token efficiency on dense filings
