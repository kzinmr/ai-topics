---
title: "Prime Intellect — NanoGPT Speedrun Frontier"
type: source
created: 2026-08-23
tags: [research, benchmark, agentic-rl, speedrun]
sources:
  - https://www.primeintellect.ai/research/nanogpt-speedrun
  - https://news.ycombinator.com/item?id=49404380
---

# NanoGPT Speedrun Frontier (Prime Intellect, 2026-08-22)

Public leaderboard: 153 autonomous agent runs across 18 frontier models on the
nanoGPT optimizer speedrun (human record as baseline; "share of the human
record gap closed" per run). Captured 2026-08-23 via trending-topics scan
(HN item 49404380).

## Leaderboard snapshot (captured 2026-08-23)

| # | Model | Harness (effort) | Record | Gap closed | Total tok | Days |
|---|-------|------------------|--------|------------|-----------|------|
| 1 | Fable 5 | claude-code · high | 2,726 | 81.7% | 800M | 8.7 |
| 2 | Opus 5 | claude-code · max | 2,920 | 53.6% | 183M | 2.9 |
| 3 | Kimi K3 | prime-agent · max | 2,930 | 52.2% | 112M | 3.6 |
| 4 | Kimi K3 | kimi-code · max | 2,974 | 45.8% | 682M | 5.1 |
| 5 | Opus 4.8 | claude-code · max | 3,018 | 39.4% | 318M | 3.0 |
| 6 | GPT-5.6 Sol | codex · xhigh | 3,042 | 35.9% | 2.9B | 6.1 |
| 7 | GPT-5.6 Sol Pro | codex · xhigh | 3,058 | 33.6% | 1.2B | 3.4 |
| 8 | Sonnet 5 | claude-code · max | 3,105 | 26.8% | 998M | 2.0 |
| 9 | GPT-5.6 Luna | codex · xhigh | 3,110 | 26.1% | 894M | 1.9 |
| 10 | Grok 4.5 | grok-cli · xhigh | 3,120 | 24.6% | 46M | 2.7 |
| 11 | Qwen3.8 Max | qwen-code · max | 3,120 | 24.6% | 216M | 1.9 |
| 12 | GLM 5.2 | pi · high | 3,150 | 20.3% | 57M | 1.8 |
| 13 | DeepSeek V4 Pro | claude-code · max | 3,205 | 12.3% | 26M | 1.1 |
| 14 | GPT-5.6 Terra | codex · xhigh | 3,214 | 11.0% | 417M | 1.1 |
| 15 | Grok 4.6 | grok-cli · xhigh | 3,220 | 10.1% | 27M | 0.6 |
| 16 | Muse Spark 1.2 | muse-code · xhigh | 3,230 | 8.7% | 41M | 0.6 |
| 17 | Muse Spark 1.1 | pi · max | 3,232 | 8.4% | 122M | 3.7 |
| 18 | GPT-5.5 | codex · xhigh | 3,234 | 8.1% | 70M | 1.1 |
| 19 | Kimi K2.7 | kimi-code · max | 3,240 | 7.2% | — | 1.6 |

"note" / "serial era" / "running" columns mark run mode. All traces open
(linked on the research page). Leaderboard is live — values above are a
point-in-time capture, not a final ranking.

## Why it matters

- First public **harness × model** leaderboard on a continuous-time
  optimization task: the spread between models on the *same* harness
  (claude-code: Fable 5 81.7% vs Opus 5 53.6% vs DeepSeek V4 Pro 12.3%)
  is much larger than the spread between harnesses for a fixed model
  (Kimi K3: prime-agent 52.2% vs kimi-code 45.8%).
- Token efficiency is decoupled from record: Opus 5 closed 53.6% of the
  gap on 183M tokens vs Fable 5's 800M — 4.4× cheaper to reach ~half the
  progress. GPT-5.6 Sol burned 2.9B tokens for 35.9%.
- Empirical support for the infrastructure-noise / benchmaxxing debate:
  "model ranking" on this task is harness-contingent and effort-contingent.
