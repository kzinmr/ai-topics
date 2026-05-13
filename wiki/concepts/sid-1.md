---
title: SID-1
type: concept
aliases: [SID-1 model, sid-1-retrieval]
created: 2026-05-13
updated: 2026-05-13
status: L2
sources: [https://www.sid.ai/research/sid-1, https://www.sid.ai/research/sid-1-technical-report, https://x.com/maxrumpf, https://ycombinator.com/companies/sid]
tags: [model, information-retrieval, reinforcement-learning, grpo, rag, agentic-engineering, subagents]
---

# SID-1

SID-1 は SID.ai が2025年12月に発表した、**agentic retrieval** のためにエンドツーエンドで強化学習（RL）された最初のモデル。従来の埋め込み→検索→リランキングという固定パイプラインを廃し、人間のように「検索→読む→クエリ改良」を反復するエージェント型アプローチを採用。

## 概要

| 項目 | 内容 |
|------|------|
| 発表日 | 2025年12月4日 |
| 開発元 | SID.ai（CEO: [[max-rumpf|Max Rumpf]]） |
| 訓練手法 | Magistral 修正版 [[grpo|GRPO]]、SFT なし（cold-start RL） |
| 提供形態 | API、AWS Bedrock、セルフホスト |
| 計算リソース | NVIDIA 提供 |

## アーキテクチャ

### Agentic Retrieval
従来の検索パイプラインは各ステップを事前定義：
1. クエリ書き換え
2. 検索（ベクトル / BM25）
3. リランキング（クロスエンコーダー）

SID-1 は単一モデルがこれらすべてを反復的に実行。必要に応じて追加の検索ステップを行い、難易度に応じて計算量を適応的に調整する。

### 訓練手法
- **GRPO（Magistral 修正版）**: SFT フェーズなしの cold-start RL
- **マルチターン・マルチ環境 RL**: 複数環境での対話的検索を RL で最適化
- **合成的データ生成**: 人間の研究者が1時間以上かかるような難問で訓練
- **報酬設計**: rule-based reward + 検索精度ベース

**実践的課題**（Max Rumpf の X 投稿より）:
> "OpenAI-style messages を env との対話に使うと、パースと再トークン化で微妙に異なるトークンが生成される。この問題のデバッグに他のどの課題よりも多くの H100 時間を浪費した。"

## パフォーマンス

多様な検索ベンチマーク（一般知識、金融、科学、法律、メール）での評価。

| モデル | Recall | 所要時間 | コスト/質問 |
|--------|--------|----------|------------|
| **SID-1 (4x)** | **0.84** | 5.5s | $0.0014 |
| SID-1 (1x) | 0.77 | 5.5s | $0.00062 |
| GPT-5.1 (high) | 0.78 | 131s | $0.24 |
| GPT-5.1 (auto) | — | 38.5s（推定7x SID-1） | — |
| Gemini 3 Pro | 0.66 | 156s | $0.12 |
| Sonnet 4.5 | 0.64 | 35s | $0.54 |
| Reranker @10 | 0.45 | 0.78s | $0.00061 |
| Vector only @10 | 0.44 | 0.15s | $0.0000098 |

### コスト効果
- GPT-5.1 比 **3-4桁低コスト**（$0.24→$0.0014）
- GPT-5.1 比 **24倍高速**（131s→5.5s）
- 従来リランキングパイプライン比 **recall 1.87倍**（0.45→0.84）
- 埋め込み検索のみ比 **recall 1.91倍**（0.44→0.84）

### 適応的計算
難易度の低い質問では少ないステップと少ないトークンで回答し、レイテンシとコストを自動的に節約。

## 統合性

- **ドロップイン互換**: 既存の embedding-only / RAG 検索システムに置き換え可能。通常「午後半日」で統合可能
- **サブエージェント動作**: GPT-5 や Sonnet などのフロンティアモデルのサブエージェントとして設計
- **ツール使用**: search ツールを呼び出し、結果を読み、クエリを改良するマルチステッププロセス

## 戦略的意義

SID.ai は検索のステップチェンジ改善が新たな勝者を生むという歴史的パターンを引用：

> "Claude Code was better at finding the right file, unlocking larger code bases and driving massive adoption for Anthropic. Open Evidence made retrieving over medical research easier and took doctors by storm. Relational was better than hierarchical for databases, creating Oracle. Better web search created Google."

SID-1 をこの系譜に位置づけ、「検索のステップチェンジ」として市場投入。

## 技術報告書の主要貢献

1. **エージェント型検索のための RL 訓練の実証**: 初のエンドツーエンド RL for retrieval
2. **GRPO の実践的課題**: 共通 GRPO 定式化の問題点、トークン化の不安定性、マルチターン RL インフラの課題
3. **SFT フリー訓練の実現可能性**: human cold-start data なしでの訓練経路を示す
4. **報酬設計**: 検索精度を直接最適化する報酬関数の設計論

## 制限と今後の方向性

- クローズドコーパス検索（closed corpus retrieval）に特化
- 現在は計算リソースに制約があり、徐々に展開中
- 2026年夏のリサーチインターンを募集

## 関連ページ

- [[max-rumpf]] — SID.ai CEO / SID-1 開発者
- [[grpo]] — Group Relative Policy Optimization、訓練アルゴリズム
- [[agentic-retrieval]] — エージェント型情報検索パラダイム
- [[rag]] — Retrieval-Augmented Generation、SID-1 が置き換えを狙う従来手法
- [[magistral]] — GRPO 修正版の開発元
- [[test-time-compute]] — テスト時計算最適化
- [[search-r1]] — 類似のアプローチ（RL for agentic search）
