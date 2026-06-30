# Devin Fusion: Frontier Performance at 35% Lower Cost

**Source**: https://cognition.com/blog/devin-fusion
**Date**: 2026-06-29
**Author**: The Cognition Team

## Summary

Cognition introduces **Devin Fusion**, a multi-model harness that achieves frontier-level coding performance at 35% lower cost. Two key techniques:

1. **Sidekick approach**: Runs two parallel agents — a frontier "main" agent and a cost-effective "sidekick" agent, each with persistent cached contexts. The main agent delegates routine work to the sidekick while handling planning, ambiguity resolution, and final review.

2. **Dynamic mid-session routing**: Lightweight classifiers during task execution signal when to switch models. Model switching happens during context compaction (which triggers a cache miss anyway), so switching is effectively "free."

## Key Results

| Configuration | FrontierCode Score | Cost |
|---|---|---|
| Fusion + Fable 5 | 57.6 | $3.00 |
| Fable 5 (medium) | 57.0 | $5.12 |
| Fusion | 47.9 | $2.38 |
| Opus 4.8 (high) | 48.8 | $3.24 |
| GPT-5.5 (high) | 44.8 | $3.64 |
| GLM-5.2 | 43.0 | $2.70 |

- 35% cost reduction maintaining frontier performance (without Fable 5)
- 41% cost reduction with Fable 5 in the harness
- 88% of internal merged PRs driven entirely by automated Fusion router

## Architecture Details

- Sidekick pattern fixes three problems with basic model routing:
  - Retains real frontier intelligence (not "benchmark-score" intelligence)
  - Generalizes beyond single-prompt tasks (dynamic switching mid-session)
  - Avoids costly cache misses (both models maintain persistent cached contexts)
- Most cached inputs have 5-minute expiry — engineering around this is a key challenge
- Fable 5 performs unusually well in multi-agent setups (delegates more intelligently, requests context more efficiently)

## Significance

"The age of using one model for all of your work is coming to an end." — Multi-model harnesses capture relative strengths of various frontier models. Some models excel at UI testing, others at identifying complicated bugs. Growing set of capable open-source models makes specialization easier.
