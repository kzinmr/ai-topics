---
title: "Knowledgator"
type: entity
created: 2026-05-01
updated: 2026-05-01
tags:
  - organization
  - lab
  - open-source
  - classification
  - nlp
aliases: ["knowledgator", "Knowledgator Engineering"]
sources:
  - https://knowledgator.com
  - https://huggingface.co/knowledgator
  - https://github.com/Knowledgator
---

# Knowledgator

**URL:** https://knowledgator.com
**HuggingFace:** https://huggingface.co/knowledgator
**GitHub:** https://github.com/Knowledgator
**Discord:** https://discord.gg/dkyeAgs9DG

Open-Source ML 研究企業。エンコーダベースモデルによる情報抽出技術に特化。GLiNER ファミリー（NER、分類、関係抽出）の開発・公開で知られる。

## 主要プロダクト

| プロダクト | 分野 | 基盤 |
|---|---|---|
| **[[concepts/gliclass]]** | ゼロショットテキスト分類 | DeBERTa / ModernBERT |
| **GLiNER** | ゼロショット固有表現認識 | マルチタスクエンコーダ |
| **GLiNER-bi-V2** | 双エンコーダ NER | bi-encoder |
| **GLiNER-X** | 多言語 NER | mDeBERTa |
| **GLiNER-BioMed** | 医用 NER | ドメイン特化 |
| **GLiNER-relex** | 関係抽出 | GLiNER 派生 |
| **GLiNER-Linker** | エンティティリンキング | GLiNER 派生 |
| **GLiNER-PII** | PII (個人情報) 検出 | GLiNER 派生 |
| **ModernGLiNER** | ModernBERT ベース NER | ModernBERT |
| **ModernGLiClass** | ModernBERT ベース分類 | ModernBERT |
| **LLM2Encoder** | LLM からのエンコーダ蒸留 | 蒸留技術 |

## HuggingFace コレクション

Knowledgator は HF 上で以下のコレクションを管理：
- GLiCLass-V3 — 最新ゼロショット分類モデル群
- GLiClass-Instruct — 指示追従最適化モデル
- GLiClass-Multilang — 多言語モデル
- GLiNER — 全 NER モデル
- Zero-shot text classification models — 包括的なゼロショット分類カタログ
- Universal token classification — トークン分類モデル群
- Information Extraction Datasets — 情報抽出用データセット

## 関連エンティティ
- [[entities/gm8xx8]] — キュレーター（GLiNER/GLiClass を追跡）
