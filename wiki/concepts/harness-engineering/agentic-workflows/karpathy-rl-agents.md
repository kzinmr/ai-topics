---
title: "Karpathy RL Agents — Agentic Research Loop"
aliases:
  - karpathy-loop
  - autoresearch
  - karpathy-agentic-engineering
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - karpathy
  - autonomous-research
status: draft
sources:
  - "https://www.sahmcapital.com/news/content/andrej-karpathy-says-ai-agents-are-rewriting-how-software-gets-built-adds-he-hasnt-typed-a-line-of-code-probably-since-december-2026-03-22"
  - "https://www.youtube.com/watch?v=kwSVtQ7dziU"
  - "https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html"
  - "https://github.com/karpathy/autoresearch/"
  - "https://blog.gopenai.com/the-karpathy-loop-how-a-630-line-script-is-rewriting-the-rules-of-ai-research-21190138f253"
---

# Karpathy RL Agents — Agentic Research Loop

Andrej Karpathyが提唱する**自律的研究ループ（Autonomous Research Loop）**のパターン。2026年3月の[AutoResearch](https://github.com/karpathy/autoresearch/)プロジェクトと[No Priors podcast](https://www.youtube.com/watch?v=kwSVtQ7dziU)での発言で詳細化。

## 核心哲学

### The "Loopy Era" of AI
> "One day, frontier AI research used to be done by meat computers in between eating, sleeping, having other fun, and synchronizing once in a while using sound wave interconnect in the ritual of 'group meeting'. That era is long gone. Research is now entirely the domain of autonomous swarms of AI agents running across compute cluster megastructures in the skies."

KarpathyはAI研究が「人間の研究者による断続的な実験」から「エージェントの自律的継続的改善」へ移行したと宣言。これを **"The Loopy Era"** と呼ぶ。

### Vibe Coding → Agentic Engineering への移行
2025年に造語した「Vibe Coding」から2026年には「Agentic Engineering」へ:

> "In 2025, he created and popularized the term Vibe coding. Anyone can describe what they want and get working software. In 2026, he says we are Agentic engineering. Humans no longer write most code. We direct, supervise, and orchestrate agents."

### 人間の役割の変化
> "You are not typing computer code. You are now spinning up AI agents."
> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change."

2025年12月以降、Karpathy自身が生でコードを書いていないことを公言。人間の役割は**コードを書くこと**から**エージェントの監督・指示・環境設計**へシフト。

## AutoResearch: The Karpathy Loop

### 仕組み
[karpathy/autoresearch](https://github.com/karpathy/autoresearch/) — 630行のPythonスクリプトで、エージェントが自律的にLLM研究を行う:

1. エージェントが`train.py`（単一GPU版nanochat）を読む
2. 仮説を形成（「Attention深度を増やしたら？」「AdamWのβパラメータを調整したら？」）
3. コードを修正
4. **5分間の固定バジェット**で実験実行
5. バリデーションメトリクス（`val_bpb`）を確認
6. 改善していればコミット、していなければリバート
7. 翌朝、実験ログと（おそらく）より良いモデルが待っている

### 実績
- **2日間で700回の実験**を自動実行
- **20個の最適化**を発見・適用
- GitHub: 60,000+ stars, 10,000+ forks
- Fortune誌が「The Karpathy Loop」として特集

### program.md パターン
> "The bottleneck in AI research has never been compute — it's been the human researcher, distracted by meetings."

エージェントへの指示は自然言語のMarkdownファイル（`program.md`）で与える。これが**新しいプログラミングインターフェース**:

```markdown
# Research Program
- Test learning rate schedules: cosine vs linear vs constant
- Try batch sizes: 32, 64, 128, 256
- For each combo, train for exactly 5 minutes
- Log val_bpb after each run
- If val_bpb improves by >0.01, commit the change
```

## Dobby: AI Home Assistant

Karpathyは"Dobby"と呼ばれるAIホームアシスタントを構築:

> "So Dobby is in charge of the house," he said, noting the system can even detect deliveries via security cameras and automatically send alerts.

WhatsAppなどの自然言語コマンドで照明、空調、セキュリティを管理。エージェントが現実世界のタスクを自律的に実行する例。

## MicroGPT: 教育用の最小GPT実装

> "MicroGPT (Feb 2026 release) a GPT trained from scratch in 243 lines of pure Python + basic math—no PyTorch."

nanoGPTとllm.cの後継。エージェントと人間の両方がアルゴリズムを理解できるように設計。

## 関連人物・プロジェクトとの関係

| 人物/プロジェクト | Karpathyとの関係 |
|-------------------|-----------------|
| [[simon-willison]] | 両者とも「Agentic Engineering」を提唱。Willisonは品質・テスト重視、Karpathyは自律的ループ重視 |
| [[ryan-lopopolo]] | LopopoloのHarness EngineeringはKarpathyのLoopy Eraと共通哲学 — 「エージェントを動かす環境設計」 |
| [[boris-cherny]] | ChernyのCLAUDE.mdとKarpathyのprogram.mdは同じパラダイム — コンテキストファイルがエージェントの制御レイヤー |
| [nanochat](https://github.com/karpathy/nanochat) | AutoResearchのベースとなった単一GPU LLM実装 |

## KarpathyのAgentic Engineering定義

> "Agentic engineering: Humans no longer write most code. We direct, supervise, and orchestrate agents. Technical expertise is still a multiplier, but the bits humans contribute are sparse and rare."

### Willisonとの違い
| 次元 | Willison | Karpathy |
|------|----------|----------|
| 重点 | テストファースト、認知負債の管理 | 自律的ループ、5分実験バジェット |
| 人間の関与 | 最終判断は人間 | 人間は監督・環境設計のみ |
| 代表的プロジェクト | Datasette, LLM | AutoResearch, MicroGPT |
| メトリクス | コード品質、テストカバレッジ | 実験回数、メトリクス改善 |

## 関連概念

- [[concepts/harness-engineering/agentic-workflows/interactive-explanations.md]] — 上位概念
- [[harness-engineering]] — Lopopoloの環境設計アプローチ
- [[context-engineering]] — CLAUDE.md/program.md パターン
- [[autonomous-research-loop]] — 自律的研究の概念
