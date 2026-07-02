---
title: Fastino Labs
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [company, ai-research, open-source, small-language-model, encoder-model, inference, fine-tuning, named-entity-recognition]
sources:
  - https://fastino.ai
  - https://pioneer.ai/blog/introducing-pioneer
  - https://pioneer.ai/blog/behind-pioneer
---

# Fastino Labs

**Fastino Inc.**（Fastino Labs）は、Small Language Model（SLM）のフロンティア研究と推論基盤を専門とする応用研究ラボ。主力プロダクトは [[entities/pioneer-ai]]（SLMファインチューニング＆推論プラットフォーム）と [[concepts/gliner-model-family]]（オープンソースのエンコーダモデル群）。

## 企業概要

| 項目 | 内容 |
|---|---|
| **正式名称** | Fastino Inc. |
| **ブランド名** | Fastino Labs |
| **本拠地** | 米国 |
| **主要プロダクト** | [[entities/pioneer-ai]], [[concepts/gliner-model-family\|GLiNER]] シリーズ |
| **研究領域** | SLM最適化、エンコーダアーキテクチャ、合成データ生成、適応的推論 |
| **ライセンス** | Apache 2.0（オープンソースモデル） |

## 技術ビジョン

Fastinoの核心的信念は、**「特化型SLMがプロダクションAIの主要ビルディングブロックになる」** ということ。フロンティアLLMの汎用性と推論能力を活かしつつ、高頻度・低レイテンシ・決定論的精度が求められるタスクにはSLMを採用する、ハイブリッドアーキテクチャを提唱している。

> "The most effective agentic architectures use both: LLMs for reasoning and planning, and SLMs for high-volume, latency-sensitive tasks that require deterministic accuracy."

## プロダクトポートフォリオ

### Pioneer（プラットフォーム）
→ 詳細は [[entities/pioneer-ai]] を参照

SLMの自動ファインチューニング＆適応的推論プラットフォーム。Agent Mode（対話型）とResearch Mode（完全自律型）を提供。本番推論データからの継続的モデル改善（Adaptive Inference）が主要差別化要因。

### GLiNER シリーズ（モデル群）
→ 詳細は [[concepts/gliner-model-family]] を参照

| モデル | パラメータ | 主要用途 | リリース |
|---|---|---|---|
| GLiNER (v1) | 50-205M | ゼロショットNER | 2023 |
| GLiNER2 | 205M | NER + 関係抽出 + JSON抽出 + テキスト分類 | 2025 |
| GLiGuard | 300M | コンテンツモデレーション・セーフティ分類 | 2026-05 |
| GLiNER2-PII | 300M | PII検出・マスキング（42エンティティタイプ） | 2026-05 |

## 研究実績

- **月間300万+ダウンロード**（GLiNERシリーズ累計）
- **3,200+ GitHub Stars**
- **1B+ 日次エンドユーザー**に利用されるGLiNERベースシステム
- **AdaptFT-Bench**: プロダクション条件下的モデル改善を評価する新ベンチマークを提案
- 論文: "Pioneer Agent: Continual Improvement of Small Language Models in Production"（arXiv:2604.09791）

## 主要マイルストーン

| 日付 | イベント |
|---|---|
| 2023-11 | GLiNER v1 リリース（arXiv:2311.08526） |
| 2025 | GLiNER2 リリース（arXiv:2507.18546） |
| 2026-01 | GLiNER for Modern NER ブログ公開 |
| 2026-02 | GLiNER2 for Agentic Extraction ブログ公開 |
| 2026-04 | Pioneer プラットフォームローンチ、Pioneer Agent 論文公開 |
| 2026-05 | GLiGuard リリース（arXiv:2605.07982） |
| 2026-05 | GLiNER2-PII リリース（arXiv:2605.09973） |

## 関連ページ

- [[entities/pioneer-ai]] — ファインチューニング＆推論プラットフォーム
- [[concepts/gliner-model-family]] — GLiNER/GLiNER2/GLiGuard/GLiNER2-PII モデルファミリー
- [[concepts/small-language-models]] — SLMの設計思想（関連概念）
