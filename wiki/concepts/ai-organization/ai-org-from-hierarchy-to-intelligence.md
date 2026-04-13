---
title: "Hierarchy to Intelligence — Blockの組織モデル変革"
aliases:
  - block-hierarchy-to-intelligence
  - jack-dorsey-org-model
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - organization
  - block
  - jack-dorsey
status: draft
---

# Hierarchy to Intelligence — Blockの組織モデル変革

## 概要

Jack Dorseyが2024年に提唱した**Hierarchy to Intelligence**モデル。従来のヒエラルキー型意思決定を廃し、**「文脈駆動の自律実行 + 透明性ベースの監視」**への移行を宣言。Block（旧Square）の実践から得られたAgentic Design Principlesを整理する。

## 核心原則

### 1. Decision Rights Matrix
- 誰が何を決定するかの明確化
- **エスカレーションは例外**。デフォルトで現場が決定
- AIエージェントには「自律実行権限」を付与。人間は「レビュー権限」のみ

### 2. Open-Book Telemetry
- 組織の全メトリクスをリアルタイムで可視化
- 意思決定の根拠を誰でも検証可能
- **「透明性が信頼を生む」** — 隠蔽より開示

### 3. Context-Driven Execution
- 上意下達ではなく、文脈を理解した上での自律実行
- AIエージェントは「文脈ファイル」（CLAUDE.md等）から判断基準を摂取
- 人間は「文脈の設計者」として機能

## Agentic Design Principles

Blockが実践するAI時代の組織設計原則:

| 原則 | 説明 | 実践例 |
|------|------|--------|
| **Autonomy by Default** | 可能な限り自律実行。エスカレーションは最小化 | AIエージェントがPRを自動マージ |
| **Transparency First** | 判断根拠・メトリクス・意思決定を全員に公開 | Open-Book Telemetryダッシュボード |
| **Context Over Control** | 管理ではなく文脈提供で方向付け | CLAUDE.md、プロジェクトコンテキストファイル |
| **Rapid Feedback Loops** | 短いサイクルで検証・修正 | 継続的デプロイ、リアルタイムモニタリング |
| **Outcome-Aligned Teams** | 機能別ではなく成果別でチーム編成 | クロスファンクショナルなAI/Humanハイブリッドチーム |

## Hierarchy → Intelligence の移行パス

### 段階的アプローチ
1. **透明性の確保**: メトリクス・判断基準の可視化
2. **権限の委譲**: 現場への意思決定権移譲
3. **文脈の構造化**: AIエージェントが摂取可能な形式でのナレッジベース構築
4. **自律実行の拡大**: エージェントによるタスク自動実行
5. **監視の自動化**: リアルタイムアラート、ガードレール設定

## 従来の階層モデルとの比較

| 次元 | 従来の階層 | Hierarchy to Intelligence |
|------|-----------|---------------------------|
| **意思決定** | 上意下達 | 文脈駆動・自律実行 |
| **情報フロー** | サイロ化・制限 | 透明・オープン |
| **管理の役割** | 指示・監視 | 文脈設計・ガードレール設定 |
| **AIの位置付け** | ツール・補助 | 自律実行エージェント |
| **スケーラビリティ** | 人头比に依存 | コンテキスト品質に依存 |

## リスクと課題

- **透明性の滥用**: 情報過多によるノイズ増加
- **自律性の暴走**: ガードレール不備による予期せぬ実行
- **文脈の陳腐化**: 急速に変化する環境でのコンテキスト維持コスト
- **人間の疎外**: AI依存度過ぎによるスキル劣化

## 関連概念

- [[ai-org-context-as-moat]] — Proprietary Context（McKinsey）
- [[ai-org-solo-founder-and-super-ic]] — Solo FounderとSuper IC
- [[agentic-engineering]] — 開発者のAI活用ワークフロー
- [[harness-engineering]] — エージェントの制御・構造化

## ソース

- [Block: From Hierarchy to Intelligence](https://block.xyz/inside/from-hierarchy-to-intelligence) — 2024
- [Jack Dorsey interviews on org design](https://block.xyz) — 2024-2025
