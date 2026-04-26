---
title: "Evals for AI Agents"
type: concept
aliases:
  - evals-for-ai-agents
  - agent-evaluation
  - demystifying-evals
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - system-architecture
  - harness-engineering
  - anthropic
  - evals
status: draft
sources:
  - "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
---

# Evals for AI Agents

Anthropicが提唱する、AIエージェントの評価（Evals）の体系化ガイド。

## 核心哲学

> "The capabilities that make agents useful also make them difficult to evaluate. The strategies that work across deployments combine techniques to match the complexity of the systems they measure."

> "Writing evals is useful at any stage in the agent lifecycle. Early on, evals force product teams to specify what success means for the agent, while later they help uphold a consistent quality bar."

**エージェントを有用にする特性が、同時に評価を困難にする。デプロイ全体で機能する戦略は、測定するシステムの複雑さに合わせた手法を組み合わせる。**

## 基本用語

| 用語 | 定義 |
|------|------|
| **Task** | 定義された入力と成功基準を持つ単一テスト |
| **Trial** | タスクの1回の実行（モデルのばらつきを考慮して複数回実行） |
| **Grader** | パフォーマンスをスコアリングするロジック。複数のアサーションを含む場合あり |
| **Transcript/Trace** | ツール呼び出し、推論、APIメッセージを含むトライアルの完全な記録 |
| **Outcome** | エージェントの言葉での確認ではなく、最終的な環境状態（例: DBレコード） |
| **Eval Harness** | 評価をエンドツーエンドで実行するインフラ（並行性、記録、採点、集約） |
| **Agent Harness** | モデルをエージェントとして機能させるシステム（ツールをオーケストレーション、結果を返す） |
| **Eval Suite** | 特定の機能/動作を測定するタスクのコレクション |

## なぜEvalsを構築するのか？

- **リアクティブデバッグを防止**: チームが「闇雲に飛行」し、なぜ変更が壊れたのか推測するのを止める
- **開発を加速**: 初期のevalsは明示的な成功基準を強制。後のevalsは品質基準を維持
- **モデル採用を高速化**: evalsを持つチームは、手動テストの「週間」ではなく「日間」で新モデルにアップグレード
- **無料のベースライン**: 遅延、トークン使用量、タスクあたりのコスト、エラーレートを自動的に追跡
- **高帯域幅のアライメント**: プロダクトとリサーチチーム間の主要なコミュニケーションチャネルとして機能

## Graderのタイプと採点戦略

| タイプ | 長所 | 短所 |
|--------|------|------|
| **コードベース** | 高速、安価、客観的、再現可能、デバッグ容易 | 有効なバリエーションに弱い、ニュアンスに欠ける、主観的タスクに不適 |
| **モデルベース（LLM）** | 柔軟、スケーラブル、ニュアンスを捉える、開-ended/自由形式出力を処理 | 非決定論的、高価、人間の較正が必要 |
| **人間** | ゴールドスタンダード、専門家の判断に一致、LLMグレーダーを較正 | 高価、遅い、スケーリング困難、SMEアクセスが必要 |

**採点アプローチ**: 加重（組み合わせた閾値）、バイナリ（すべて合格が必要）、ハイブリッド。

### Capability vs Regression Evals

- **Capability（品質）**: *「このエージェントは何がうまくできるか？」* 低い合格率から開始、困難なタスクをターゲット、ヒルクライム
- **Regression**: *「古いタスクをまだ処理できるか？」* 約100%の合格率を目標、ドリフト/後退をキャッチ
- **進化**: 高合格率のcapability evalは、継続的なregressionスイートに「卒業」できる

## エージェント固有の評価アプローチ

| エージェントタイプ | 主要戦略 | ベンチマーク/ツール |
|-----------------|-----------|-------------------|
| **コーディング** | 決定論的グレーダー（ユニットテスト、静的解析）+ ツール使用/品質のトランスクリプト採点 | SWE-bench Verified, Terminal-Bench |
| **会話型** | 多次元採点（状態、ターン数、トーン）+ LLMユーザーシミュレーション | τ-Bench, τ²-Bench |
| **リサーチ** | 根拠性、カバレッジ、ソース品質チェック + 専門家に対するLLMルーブリックの頻繁な較正 | BrowseComp |
| **コンピュータ使用** | リアル/サンドボックスGUI環境 + バックエンド状態検証（UIだけでなく） | WebArena, OSWorld |

> **コンピュータ使用の洞察**: DOM操作（高速、トークン重い）vsスクリーンショット（遅い、トークン効率）のバランス。エージェントがコンテキストごとに正しいツールを選択するかを評価すべき。

## 非決定論の処理

エージェントの出力は実行ごとに異なる。製品のニーズに基づいてこれらのメトリクスを使用：

- **`pass@k`**: `k`回のトライアルで**≥1回の成功**の確率。1つの動作する解決策が重要なツールに最適。
- **`pass^k`**: **すべての`k`回のトライアルが成功**する確率。一貫性が必要な顧客向けエージェントに最適。
- *分散*: `k=1`で同一。`k=10`で、`pass@k` → 〜100%、`pass^k` → 〜0%。

## ゼロからOneへのロードマップ（実践的ステップ）

1. **早期に開始**: 実際の失敗からの20〜50のタスクで十分初期は。大きな効果サイズ means 小さなサンプルで機能
2. **手動チェックを変換**: バグトラッカー、サポートキュー、リリース前チェックを最初のタスクとして使用
3. **明確なタスク + リファレンスソリューション**: `pass@100 = 0%`なら、**タスク/グレーダーが壊れている**。常に既知の動作するリファレンスを提供
4. **問題セットのバランス**: ポジティブとネガティブの両方のトリガーをテストし、片側の最適化を回避（例: 検索しすぎる vs 検索しなさすぎる）
5. **環境を隔離**: 各トライアルのクリーンな状態。残りのファイル/キャッシュからの相関_failure_を防止
6. **パスではなく結果を採点**: 硬直的なステップチェックを避ける。創造的な解決策を許可。複数コンポーネントタスクに部分クレジットを使用
7. **LLM審査官を較正**: 「不明」の脱出ハッチを提供、構造化ルーブリックを使用、次元ごとに採点

## 関連概念

- [[concepts/harness-engineering]] — 上位インデックス
- [[concepts/building-effective-agents]] — エージェント構築の基本原理
- [[concepts/effective-harnesses-for-long-running-agents]] — 長時間実行エージェントのハーネス
- [[concepts/harness-engineering/system-architecture/writing-tools-for-agents]] — エージェント用ツール設計
