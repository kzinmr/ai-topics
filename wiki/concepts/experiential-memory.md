---
title: Experiential Memory
type: concept
created: 2026-04-16
updated: 2026-04-16
status: active
depth: L2
tags: [agent-memory, memory-systems, harness-engineering, multi-agent]
source: https://x.com/vtrivedy10 (Vivek Trivedy, Apr 2026)
related:
  - context-fragments
  - harness-engineering
  - claude-memory
  - ai-agent-memory-middleware
  - memory-systems-design-patterns
  - chatgpt-memory-bitter-lesson
sources: []
---

# Experiential Memory

Vivek Trivedy (@vtrivedy10) が2026年4月に提唱した概念。エージェントが相互作用を通じて蓄積する「経験的記憶」を、エージェント間で共有・フォーク・再利用するフレームワーク。

## 核心的な定義

> *"we're in the very early days of deploying agents and agents produce massive amounts of data in every interaction they have. this is akin to humans doing things and remembering things they did."*

> *"agent memory has a massive advantage as it can be accumulated across all agents which are easily forked and duplicated (unlike humans)."*

## 人間の記憶との対比

| 次元 | 人間の記憶 | エージェントのExperiential Memory |
|------|-----------|--------------------------------|
| 蓄積速度 | 個人の経験に限定 | 全エージェントの経験を集約 |
| 共有可能性 | 言語・教育で部分的に共有可能 | 完全なフォーク・コピー可能 |
| 検索 | 文脈依存的、再構成的 | プログラム可能な検索アルゴリズム |
| 蒸留 | 意図的な練習で定着 | 自動的なトレース→プリミティブ変換 |

## Harnessの役割

> *"memory can be treated as an externalized object. the harness is tasked with doing good contextualized retrieval which means pulling in the right data from accumulated memories across all agent interactions"*

Experiential Memoryは「外部化されたオブジェクト」として扱われ、harnessが以下のタスクを担う：

1. **Contextualized Retrieval** — 適切なタイミングで適切なデータを検索
2. **Cross-Agent Accumulation** — 複数エージェントの経験を集約
3. **Distillation** — トレース（生データ）から高レベルなメモリプリミティブへの変換

## The Bitter Lessonとの接続

VivはRich SuttonのBitter Lessonをメモリ設計に適用する：

- **compute leveraged search > human-curated knowledge**
- 大量の経験データから検索・蒸留・整理する能力が、人間の設計したルールベースのメモリよりも効果的
- オープンエコシステム — データの所有と利用が競争優位の源泉

## Open Questions

Vivが提起した未解決の問い：

1. **Traces → Memory Primitives** — 経験（トレース）をどのように効率的に蒸留し、長期的なメモリプリミティブにするか？
2. **Ultra-long time horizons** — 年単位の時間軸でメモリをどのように維持・進化させるか？
3. **Search integration** — 検索はjust-in-timeで実行すべきか、モデルの重みに統合すべきか？
4. **Self-managing context** — モデルが自身のコンテキストウィンドウを自己管理するにはどうすればよいか？

## 実装上のアーキテクチャ

### 3層メモリモデル

| 層 | 役割 | 例 |
|----|------|----|
| **L1: In-Context** | 現在の作業に必要なContext Fragments | CLAUDE.md, AGENTS.md |
| **L2: Local Memory** | セッション間で永続化された経験 | .agent/ ディレクトリ |
| **L3: Experiential Pool** | 全エージェント間で共有・フォーク可能な蓄積メモリ | S3 Files, ChromaFS, Tigris |

### Memory Distillation Pipeline

```
Agent Traces (raw interaction data)
  ↓
Contextual Retrieval (harness-managed search)
  ↓
Distillation (trace → memory primitive)
  ↓
Experiential Memory Pool (cross-agent shared)
  ↓
Context Fragment Loading (just-in-time retrieval)
```

## 関連する実装

- **Claude Memory** ([[claude-memory]]) — ファイルベースのL2メモリ
- **Claude Memory Tool** ([[claude-memory-tool]]) — Cognitionのメモリ実装
- **AI Agent Memory Middleware** ([[ai-agent-memory-middleware]]) — L3クラウドストレージ層
- **Memory Systems Design Patterns** ([[memory-systems-design-patterns]]) — 横断的な設計パターン

## Related Concepts

- [[context-fragments]] — コンテキストウィンドウのフラグメント化
- [[harness-engineering]] — Harness Designの拡張版
- [[chatgpt-memory-bitter-lesson]] — Bitter Lessonとメモリ
- [[claude-memory]] — ファイルベースのメモリ（L2実装）
- [[ai-agent-memory-middleware]] — クラウドスケールのメモリ（L3実装）
- [[memory-systems-design-patterns]] — メモリ設計パターン横断分析
- [[rlm-recursive-language-models]] — Externalized Objectsの源流
