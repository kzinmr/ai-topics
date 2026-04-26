---
title: "Effective Harnesses for Long-Running Agents"
type: concept
aliases:
  - effective-harnesses
  - long-running-agent-harness
  - initializer-coding-pattern
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - anthropic
  - harness-engineering
status: draft
sources:
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---

# Effective Harnesses for Long-Running Agents

AnthropicがClaude Agent SDKで開発した、長時間実行エージェント用の2エージェント・ハーネスパターン。

## 核心課題

> "Agents must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift."

**コンテキストウィンドウの限界**により、エージェントはセッション間でメモリを失う。Compaction（圧縮）だけでは不十分。

## 2つの主要な失敗モード

### 1. One-shotting
エージェントがすべてを一度に構築しようとし、実装途中でコンテキストが尽きる。次のセッションが推測/回復を強いられる。

### 2. Premature Completion
後続のセッションが部分的な進捗を見て、誤ってジョブが完了したと判断し、作業を停止する。

## 2エージェントアーキテクチャ

| エージェント | 役割 | 主要な動作 |
|:---|:---|:---|
| **Initializer Agent** | 最初のセッションで**1回**実行 | 環境のスキャフォールディング、追跡ファイルの作成、ベースラインスクリプトの書き込み、初期状態のコミット |
| **Coding Agent** | すべての後続セッションで実行 | 1つの機能を選択、実装、エンドツーエンドテスト、クリーンコミット、進捗ログの更新 |

> **注**: 両方とも同じシステムプロンプトとツールを使用。異なるのは初期ユーザープロンプトのみ。

## 環境管理と重要アーティファクト

### 1. `feature_list.json`
- モノリシックなプロンプトを個別の追細分化された要件に分解（例: claude.aiクローンの場合200+機能）
- すべての機能は `"passes": false` から開始
- **厳格なルール**: *「テストの削除や編集は受け入れられない。欠落またはバグのある機能につながる可能性があるため」*
- **JSONの理由**: モデルがMarkdownよりも構造化されたJSONを誤って上書き/破損する可能性が低い

### 2. `claude-progress.txt` & Git履歴
- **進捗ファイル**: セッションごとの完了作業と決定のログ
- **Git**: 記述的なコミット、悪い変更の容易な取り消し、「クリーンな状態」の維持（マージ可能なコード、主要なバグなし、適切に文書化）

### 3. `init.sh`
- 開発サーバーの起動とベースラインのスモークテストを自動化。セッション間のセットアップ摩擦を排除。

## セッションワークフローと起動プロトコル

すべてのコーディングエージェントは、トークンを節約し、回帰を防止するために厳格なシーケンスに従う：

1. `pwd` → ワーキングディレクトリを確認
2. `claude-progress.txt` & `git log` を読み取り → 最近の状態を理解
3. `feature_list.json` を読み取り → 最優先の未完了機能を選択
4. `init.sh` を実行 → 開発サーバーを起動
5. ベースラインのエンドツーエンドテストを実行 → 既存の機能が壊れていないことを確認
6. 実装 → テスト → コミット → 進捗ファイルを更新

## 関連概念

- [[harness-engineering]] — 上位インデックス
- [[harness-engineering]] — Harness Engineering（Ryan Lopopolo）
- [[harness-engineering/agentic-workflows/agentic-manual-testing]] — エージェントによる手動テストの自動化
- [[context-engineering]] — コンテキストエンジニアリング
