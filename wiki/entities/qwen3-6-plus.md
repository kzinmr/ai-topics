---
title: Qwen3.6-Plus
type: entity
created: 2026-04-10
updated: 2026-04-21
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
sources: []
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

### Relationship to Qwen3.6-27B

Qwen3.6-27B is the dense (non-MoE) counterpart in the Qwen3.6 family. While the 35B-A3B MoE excels at specific benchmarks (Pelican SVG), the 27B dense model outperforms the 397B MoE flagship on coding benchmarks: [[concepts/qwen3-6-27b]].

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

## Community Deployment Reports (April 2026)

### 8GB VRAM Achievement
Qwen3.6-35B-A3B MoE running on consumer hardware with only 8GB VRAM using llama-server configuration. Users report `max_tokens` and `thinking` mode require specific configuration to avoid truncation issues.

### Real-World Coding Work
Users reporting success using Qwen3.6-35B-A3B-UD-Q4_K_M on 32GB MacBook Pro M5 Max (128GB RAM) with 64K context through OpenCode — described as "as good as Claude" for actual coding tasks. Multiple users confirming the model solved coding problems that Qwen3.5-27B couldn't.

### Gemma4 vs Qwen3.5/3.6 Debate
Community discussion on r/LocalLLM suggesting Gemma4 may outperform Qwen3.5/3.6 on certain localhost use cases, indicating the open model landscape remains competitive.

### llama.cpp Ecosystem
- llama.cpp described as "the linux of llm" — foundational infrastructure layer
- Criticism that OSS tools don't treat llama.cpp as first-class citizen
- llama-server RAM usage during runtime being optimized

## Sources
- 
- Alibaba technical announcements
- [Simon Willison: Qwen3.6-35B-A3B pelican benchmark](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/)
