---
title: Qwen3.6-Plus
created: 2026-04-10
updated: 2026-04-16
tags:
- entity
- model
- alibaba
- qwen
- agent
related:
- alibaba
- agent-models
- chinese-ai
- claude-opus-4-7
- gguf
- model-quantization
---

# Qwen3.6-Plus

Alibabaのエージェント指向言語モデル。実世界の自律的ワークフローを対象としている。

## Key Features
- Optimized for agentic task execution
- Real-world deployment focus
- Part of Alibaba's broader AI strategy
- Competitive with frontier models in agent benchmarks

## Qwen3.6-35B-A3B

2026年4月16日にリリースされたMoE（Mixture of Experts）モデル。35Bパラメータのうちアクティブは3B。

### K_P Quants & Uncensored Aggressive (2026-04-17)

- **K_P quants** が公開され、ローカル推論の品質がさらに向上
- **Uncensored Aggressive** バージョンもリリース、制限付きの応答を必要とするユーザー向け
- これらのバリアントはコミュニティ主導の量子化・ファインチューニングエコシステムを反映

Unslothによる20.9GBのGGUF量子化版が公開され、MacBook Pro M5などのローカル環境で実行可能。

### Pelican Benchmark結果
Simon Willisonの「ペリカンが自転車に乗るSVG生成」ベンチマークにおいて：
- **Qwen3.6-35B-A3B（ローカル推論）**: 正確なペリカンと自転車のSVGを生成
- **Claude Opus 4.7**: 自転車フレームの生成に失敗
- フラミンゴの一輪車テストでもQwenが勝利

この結果は「ローカル量子化モデルが巨大プロプライエタリモデルの特定タスクで上回る」実例となった。
ただしSimon Willison自身は「これはジョークベンチマークであり、QwenがOpus 4.7より総合的に優れているとは考えにくい」と注記している。

## Strategic Context
- Represents China's push in agent AI
- Competes with OpenAI, Anthropic agent offerings
- Focus on practical enterprise applications
- Part of Alibaba Cloud AI ecosystem

## Sources
- [[raw/articles/substack.com--redirect-2-eyjlijoiaHR0cHM6Ly9ubHAuZWx2aXNzYXJhdmlhLmNvbS9wdWJsaWMtc...]]
- Alibaba technical announcements
- [Simon Willison: Qwen3.6-35B-A3B pelican benchmark](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/)
