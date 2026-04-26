---
title: "Harness Design for Long-Running Application Development"
type: concept
aliases:
  - harness-design-long-running-apps
  - generator-evaluator-pattern
  - context-resets
  - frontend-design-harness
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - harness
status: draft
sources:
  - "https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---

# Harness Design for Long-Running Application Development

Anthropicが長時間実行のアプリケーション開発向けに設計したエージェントハーネス（枠組み）のパターン。GAN（生成的敵対ネットワーク）のGenerator-Evaluatorループに着想を得た。

## 核心洞察

> "Context resets—clearing the context window entirely and starting a fresh agent, combined with a structured handoff that carries the previous agent's state and the next steps—addresses both these issues."

> "Separating the agent doing the work from the agent judging it proves to be strong lever to address this issue. The separation doesn't immediately eliminate that leniency on its own... But tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work."

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."

> "The space of interesting harness combinations doesn't shrink as models improve. Instead, it moves, and the interesting work for AI engineers is to keep finding the next novel combination."

**ハーネスの各コンポーネントは「モデルが単独ではできないこと」についての仮定をエンコードしており、その仮定は常に検証する価値がある。モデルが改善されても、ハーネス設計の探索空間は縮小せず移動する。**

## 長時間タスクの2つの失敗モード

### 1. コンテキスト劣化と「コンテキスト不安」

コンテキストが埋まると、モデルは以下の問題を抱える：
- **一貫性の喪失**: 長いタスクでコヒーレンスが低下
- **コンテキスト不安**: コンテキスト制限に近づくと、作業を早期に切り上げようとする傾向
- **コンパクションの限界**: 要約による圧縮は一貫性を保つが、残留不安を解消できない

**解決策**: コンテキストリセット（エージェントを完全に再起動） + 構造化された状態の引き継ぎ

### 2. 自己評価バイアス

> LLMs are lenient judges of their own work.

- 生成エージェントは自分の作業を甘く評価する傾向
- 主観的タスク（デザイン等）では特に顕著
- 単一のエージェントが生成と評価の両方を行うと、このバイアスが増幅

**解決策**: 生成エージェントと評価エージェントを分離

## GAN Inspired フロントエンドデザインハーネス

**インスピレーション**: Generative Adversarial Networks (GANs) のGenerator-Evaluatorループ

### アーキテクチャ

```
Generator → Evaluator (Playwright MCPでライブテスト) → スコア & 批判 → Generator (修正)
```

### 4つの評価基準

| 基準 | 内容 |
|---|---|
| **デザイン品質** | コヒーレントな全体、色・タイポグラフィ・レイアウト・画像の一貫したムード/アイデンティティ |
| **独創性** | テンプレート/ライブラリのデフォルトではなく、カスタム判断。「AI slop」（白カード上の紫グラデーション等）を明示的に減点 |
| **クラフト** | タイポグラフィ階層、スペーシング、コントラスト比などの技術的実行 |
| **機能性** | 美学に依存しないユーザビリティ（明確なプライマリアクション、直感的なナビゲーション） |

### 重要な知見

- **評価基準だけで改善**: 最初のイテレーションですら、明確な評価基準があるだけでベースラインを上回った
- **プロンプトの言葉遣いが収束を決定**: `「museum quality」` のようなフレーズが出力の方向性を形成
- **イテレーション**: 5〜15サイクルでGeneratorが戦略的決定（スコアが上昇 → 洗練、アプローチが失敗 → ピボット）

## 3-Agent フルスタックアーキテクチャ

GANInspiredパターンを自律的ソフトウェアエンジニアリングにスケールアップ：

```
Planner → Generator (スプリント) → Evaluator/QA (Playwright MCP)
```

### Planner
- 1〜4文のプロンプトを野心的な高レベル製品仕様に拡張
- 詳細な技術的詳細を避け、カスケードエラーを防止
- AI機能を仕様に織り込む

### Generator
- スプリント単位で作業（1度に1つの機能）
- QA前に自己評価
- Gitでバージョン管理
- ファイルベースの引き継ぎでコミュニケーション

### Evaluator (QA)
- Playwright MCPでライブアプリをクリックスルーテスト
- **スプリントコントラクト**（コーディング前に交渉）と評価基準に対してテスト
- ハードしきい値で失敗と詳細なバグレポートをトリガー

### コミュニケーションフロー
```
Generator: 実装を提案
  → Evaluator: レビュー
  → 両者: コントラクトに合意
  → Generator: 構築
  → Evaluator: テスト
  → フィードバックループ
```

## モデルの進化とハーネス設計

| 時代 | 特徴 | ハーネス設計 |
|---|---|---|
| **Opus 4.5** | コンテキスト不安が顕著 | コンテキストリセット + 厳格なスプリント分解が必要 |
| **Opus 4.6** | より良い計画・デバッグ・長時間タスク持続 | コンテキストリセットとスプリントを削除可能。SDK自動コンパクションで連続セッション |

> Opus 4.6はコンテキスト不安をほぼ除去し、連続セッションでの作業を可能にした。Evaluatorの役割もスプリントごとから単一エンドオブランパスへ移動。

## Effective Harnesses for Long-Running Agents（2エージェントパターン）

### 問題: メモリギャップ

> "The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before."

### 解決策: Initializer Agent + Coding Agent

**同じエージェントハーネス**を使用するが、**異なる初期プロンプト**を適用：

| エージェント | 役割 |
|---|---|
| **Initializer Agent** | 環境をスキャフォールド、トラッキングアーティファクトを作成、ベースラインgitコミット |
| **Coding Agent** | 増分的な単-feature作業。クリーンなマージ可能状態を維持 |

### 重要なアーティファクト

| ファイル | 目的 |
|---|---|
| `feature_list.json` | 全機能の包括的分解。初期状態はすべて `"passes": false` |
| `claude-progress.txt` | セッションごとの完了作業、決定、次のステップのログ |
| `init.sh` | 開発サーバー起動とベースラインテスト実行のスクリプト |
| `git` リポジトリ | バージョン管理（記述的なコミットメッセージ） |

### セッションワークフロー

1. `pwd` → 作業ディレクトリを確認
2. `claude-progress.txt` と `git log` を読み取る → 最近の状態を理解
3. `feature_list.json` を読み取る → 未完了の最高優先度機能を1つ選択
4. `init.sh` を実行 → 開発サーバーを起動
5. 基本的なエンドツーエンドテストを実行 → コア機能が壊れていないことを確認
6. 機能を実装 → コミット & 進捗ログを更新

### 失敗モードと緩和策

| 問題 | Initializerの修正 | Coding Agentの修正 |
|---|---|---|
| プロジェクトの早期完了 | 全機能が `"passes": false` の `feature_list.json` を作成 | リストを読み取り、セッションごとに1つの機能を選択 |
| バグのある/文書化されていない状態 | gitリポジトリと `claude-progress.txt` を設定 | ログ/進捗を読み取り、ベースラインテストを実行、明確なメッセージでコミット |
| 未検証の機能 | 機能リストを設定 | エンドツーエンドを自己検証。テスト後にのみ `"passes": true"` をマーク |
| セットアップ時間の浪費 | サーバー起動用の `init.sh` を記述 | セッション開始時にすぐに `init.sh` を実行 |

## 重要な教訓

1. **モデルが改善されても、ハーネス設計の探索空間は縮小しない** — 移動するだけ
2. **生成と評価の分離**は、主観的タスクで特に強力なレバー
3. **コンテキストリセット**は、単なる圧縮よりも効果的な場合がある
4. **構造化された状態の引き継ぎ**（ファイル、git、進行ログ）が、セッション間のギャップを埋める
5. **評価基準の明示化**だけで、出力品質が大幅に向上する
6. **モデルの特性に合わせて**ハーネスを設計する必要がある（Opus 4.5 vs 4.6で異なるアプローチ）

## 関連概念

- [[harness-engineering]] — 上位インデックス
- [[building-effective-agents]] — エージェント構築の基本原理
- [[multi-agent-research-system]] — マルチエージェントシステム
- [[context-engineering]] — コンテキストエンジニアリング
- [[comparisons/evals-skills]] — 評価スキル
