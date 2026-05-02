---
title: "Context Compaction"
type: concept
aliases:
  - compaction
  - context-compression
  - native-compaction
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - harness-engineering
  - context-management
status: draft
sources:
  - "https://openai.com/index/equip-responses-api-computer-environment/"
---

# Context Compaction

長期実行エージェントがコンテキストウィンドウの限界に達した際、**重要な情報を保持しつつ不要なデータを圧縮**する仕組み。OpenAI Responses APIのネイティブ機能。

## 問題意識

エージェントループでは、ツール呼び出しの結果、推論の要約、会話履歴が累積していく。長いタスクでは200Kトークンを超え、コンテキストウィンドウが満杯になる。

> "Long-running tasks fill the context window... the limited context window quickly fills up."

## OpenAIのアプローチ

モデル自身が**暗号化されたトークン効率の良い圧縮アイテム**を生成するようにトレーニングされている。

### 2つのモード

| モード | 説明 | ユースケース |
|--------|------|-------------|
| **サーバーサイド** | 設定可能な閾値で自動トリガ。多少のオーバーを許容 | 長期タスク、自動運用 |
| **スタンドアロン** | `/compact` エンドポイントで手動制御 | 明示的な圧縮タイミング |

### 動作メカニズム

```
圧縮前: [システムプロンプト] + [会話履歴 1-150] + [ツール結果 多数]
                    ↓
圧縮後: [圧縮アイテム (暗号化)] + [高価値な会話履歴の一部]
```

- 圧縮アイテムはモデルが理解できる形式で、重要な状態を保持
- サーバーサイド圧縮はモデルのリリースごとに進化（トレーニングに追従）
- 複雑なクライアント側の要約ロジックが不要

## Codexによる自己改善

> "Codex helped us build the compaction system while serving as an early user of it. When one Codex instance hit a compaction error, we'd spin up a second instance to investigate. The result was that Codex got a native, effective compaction system just by working on the problem."

** Codexが自身の圧縮エラーを調査し、圧縮システム自体を改善した**。これは「モデルが自身のためにツールを作る」実例。

## 関連概念

- [[concepts/context-window-management]] — 圧縮の上位概念（Simon Willisonの戦略的管理）
- [[concepts/harness-engineering/system-architecture/agent-loop-orchestration]] — 圧縮が必要になるコンテキスト累積の発生源
-  — 圧縮を実装する基盤API
## 参照

- [OpenAI: Equipping the Responses API with a computer environment](https://openai.com/index/equip-responses-api-computer-environment/)
- [[openai]] — OpenAI
