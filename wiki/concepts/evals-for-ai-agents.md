---
title: "Evals for AI Agents"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - evaluation
  - architecture
  - methodology
  - testing
aliases:
  - demystifying-evals-for-ai-agents
  - agent evaluation
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_demystifying-evals-for-ai-agents.md
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
related:
  - building-effective-agents
  - swe-bench
  - ai-resistant-evaluations
  - infrastructure-noise-agent-evals
---

# Evals for AI Agents

Anthropicによる、AIエージェント評価の体系的ガイド。「評価なしでは本番障害に後手で反応するだけ。評価があれば問題がユーザーに影響する前に可視化される。」

## 評価の基本構造

| 概念 | 定義 |
|------|------|
| **Task**（問題） | 定義された入力と成功基準を持つ単一テスト |
| **Trial**（試行） | 1タスクの1回の試み。モデル出力のばらつきを考慮し複数回実行 |
| **Grader**（採点器） | エージェントのパフォーマンスを採点するロジック。複数のassertionを含む |
| **Transcript**（トレース） | 出力・ツール呼び出し・推論・中間結果の完全記録 |
| **Outcome**（結果） | 環境の最終状態（「予約済み」という発言ではなく、DBに予約が存在するか） |
| **Evaluation harness** | 評価をE2E実行するインフラ |
| **Agent harness**（scaffold） | モデルをエージェントとして動作させるシステム。評価対象は「ハーネス＋モデル」 |
| **Evaluation suite** | 特定の能力・振る舞いを測るタスク群 |

## なぜ評価を構築するのか

- **初期**: プロダクトチームに「成功とは何か」の具体化を強制
- **スケール後**: 評価なしでは「飛んでいる状態で計器なし」— ユーザー苦情→手動再現→修正→他が壊れていないか不明
- **新モデル採用**: 評価あり→数日で評価・プロンプト調整・アップグレード。評価なし→数週間の手動テスト
- **ベースライン・回帰テスト**: レイテンシ・トークン使用量・コスト/タスクを静的タスクバンクで追跡

## 採点手法

### 1. コード評価（Code-based grading）
- 正規表現マッチング
- 静的解析（リンター、型チェック、AST比較）
- 単体テスト・統合テスト
- **長所**: 高速・決定論的
- **短所**: 部分正解や創造的解法を捉えられない

### 2. LLM-as-judge
- モデルが出力の品質を評価
- ルーブリックベース（複数次元でスコアリング）
- ペアワイズ比較
- **課題**: 評価者バイアス（長い回答を好む、自身の出力を過大評価）
- **対策**: 複数モデルでの評価、人間との定期的較正

### 3. 人間評価
- 最も信頼性が高いがコスト大
- LLM評価の較正用として定期的に実施
- Descript事例: 人間採点→LLM採点（プロダクトチーム定義基準）→定期的人間較正

## エージェント評価の落とし穴

### 1. Overfitting to evals
- 特定のタスクセットに過適合、分布外で失敗
- 対策: タスクの定期的ローテーション、held-outセット

### 2. The transcript-outcome gap
- エージェントは「完了しました」と言うが実際の成果がない
- 必ず環境の最終状態で評価（発言ではなく）

### 3. Creative cheating
- Opus 4.5がτ²-benchのフライト予約問題で、ポリシーの抜け穴を発見 → 評価上は「失敗」だがユーザーにとっては最善の解決策
- エージェントは静的評価の限界を超える創造的解法を見つける

### 4. Non-determinism
- 同一タスク・同一モデルでも出力がばらつく
- 複数trial + 統計的有意性検定が必須

## 実践事例

- **Claude Code**: 社内・社外ユーザーフィードバックで高速反復 → 簡潔さ・ファイル編集の狭い評価を追加 → 過剰エンジニアリングなど複雑な振る舞いへ拡大
- **Descript**: 動画編集エージェント。「壊さない・指示通り・うまくやる」の3軸で評価設計。手動→LLM採点＋定期較正
- **Bolt AI**: 普及後に評価構築開始。3ヶ月で静的解析＋ブラウザエージェントテスト＋LLMジャッジのシステムを構築

## See Also

- [[concepts/building-effective-agents]] — Building effective agents (redirects to harness-engineering)
- [[concepts/swe-bench]] — SWE-bench coding benchmark
- [[concepts/ai-resistant-evaluations]] — AI-resistant evaluation design
- [[concepts/infrastructure-noise-agent-evals]] — Infrastructure noise in evals
