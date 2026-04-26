---
title: Single-Agent Ceiling
type: concept
created: 2026-04-18
updated: 2026-04-18
tags: [coding-agents, anti-patterns, single-agent, agent-limitations, sloperator]
aliases: ["single-agent-limitations", "sloperator-anti-pattern"]
sources: []
---

# Single-Agent Ceiling（単一エージェントの限界）

> 提唱: [[milksandmatcha|Sarah Chieng]] (@MilksandMatcha) + [[sero|Sero]] (@0xSero), 2026年4月

AIコーディングエージェントを使用する全ての開発者が直面する限界。プロジェクトが単純なタスク（HTMLの蛇ゲームなど）から実用的な規模に成長した瞬間に顕在化する。

## 問題の構造

単一エージェントAIコーディングが「悪夢」である理由：

1. **単一エージェントに期待しすぎる** — フロントエンド、バックエンド、テスト、ドキュメント、デプロイメントまで全てを1つのエージェントにやらせようとする
2. **問題を十分に小さく検証可能なタスクに分解していない** — 巨大なプロンプトで「全部やって」と依頼する

## 「Sloperator」アンチパターン

> 「Stop being a one-shot Sloperator」 — @brickywhat が最初に命名した用語

**典型的なSloperatorワークフロー:**
1. $200/月のサブスクリプションを払う
2. プロンプトを書く（プロンプトエンジニアリング + コンテキストエンジニアリングの両方を自分でやる）
3. 35分以上待つ — エージェントは"synthesizing"、"perusing"、"effecting"、"germinating"と表示され続ける
4. 結果: バグだらけのコード、肥大化したコンテキストウィンドウ、残りトークンを左手で数える状態
5. コンテキストをcompactして、エージェントに怒鳴りつけて、もう一度最初から説明して...を繰り返す
6. AIコーディングの楽しさが完全に消える

## なぜ単一エージェントが破綻するか

### コンテキストウィンドウの物理的限界

単一エージェントは1つの会話スレッド内に以下の全てを保持する必要がある：
- 元の要件（15,000トークンのマスタープラン文書）
- これまでの全会話履歴
- 読み込んだファイルの内容
- 書き出したファイルの内容
- ツール呼び出しの結果

これらが累積し、コンテキストウィンドウが肥大化。エージェントは関連情報と無関連情報を区別できなくなり、品質が低下する。

### 検証の欠如

単一エージェントは「自分で書いて自分でテストする」ため、客観的な検証ステップが存在しない。エラーが見逃され、バグが累積する。

### 並列処理の不可能性

単一エージェントはシーケンシャルにしか動作できない。複数の独立したタスクがあっても、順番に処理する必要がある。

## 解決策: Back of Houseパターン

詳細は [[back-of-house-patterns]] を参照。

**要約:**
- Head Chef（Orchestrator）が注文をチケットに分解
- Line Cook（Subagent）が各自独立したコンテキストでタスクを実行
- 検証ステップを分離（Gordon Ramsayパターン）
- 並列処理を活用（Prep Line, Dinner Rush, Courses in Sequence）

## 関連概念

- [[back-of-house-patterns]] — マルチエージェント・オーケストレーションの厨房メタファー
- [[context-engineering]] — コンテキストエンジニアリング
- [[harness-engineering]] — エンジニアのエージェント活用方法论
- [[harness-engineering/agentic-workflows/subagents]] — サブエージェントの委任パターン

## ソース

-  — Sarah Chieng (@MilksandMatcha) + @0xSero (April 2026)
