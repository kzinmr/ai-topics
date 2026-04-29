---
title: "Nano Banana 2"
type: concept
aliases:
  - nano-banana-2
  - nano-banana-pro
  - google-nano-banana
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - image-generation
  - google
  - gemini
status: complete
sources:
  - url: "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana"
    title: "The Ultimate Nano Banana Prompting Guide (Google Cloud Blog)"
  - url: "https://cloud.google.com/blog/products/ai-machine-learning/bringing-nano-banana-2-to-enterprise"
    title: "Bringing Nano Banana 2 to Enterprise (Google Cloud Blog)"
  - url: "https://gemini.google.com/"
    title: "Nano Banana on Gemini"
---

# Nano Banana 2

**Nano Banana 2** は、Google が Gemini 3 ファミリー向けに開発した最先端の AI 画像生成・編集モデル。深層推論能力と Web 検索からのリアルタイム情報を活用し、従来の画像生成モデルより正確で文脈を理解したビジュアルを生成する。

## 定義 / コアアイデア

Nano Banana モデルは、単なるテキスト→画像変換ではなく、**実世界の知識と深層推論**を用いて画像を生成する。プロンプトを解釈する前に「理解」するフェーズを持ち、より正確で一貫性のある結果を提供する。

## モデルバリエーション

| モデル | 特徴 | 用途 |
|--------|------|------|
| **Nano Banana**（高速） | 高速生成、キャラクター一貫性、写真合成 | カジュアルなコンテンツ作成 |
| **Nano Banana Pro**（推論） | 高度なテキストレンダリング、精密編集、2K/4K アップスケーリング | プロフェッショナル業務 |
| **Nano Banana 2** | リアルタイム Web 情報を活用、高精度ビジュアル | エンタープライズ・教育・旅行 |

## 主要機能

### 1. リアルタイム Web 検索連携
- 最新の Web 情報を取得して画像生成に反映
- 例：「現在のサンフランシスコの天気を反映したシーン」を生成可能

### 2. キャラクター一貫性（Character Consistency）
- 複数の画像間で同一キャラクターの外見を維持
- ストーリーボードや広告シリーズに重要

### 3. 高度なエディット機能
- **ローカル編集**: 画像の一部分のみを変更
- **写真合成**: 複数の写真をシームレスに結合
- **テキストレンダリング**: 画像内に鮮明なテキストを描画

### 4. プロンプティングフレームワーク
Google の公式プロンプティングガイドでは以下のフレームワークを推奨：
1. **構造化プロンプト**: `[ソース/検索要求] + [分析タスク] + [ビジュアル指示]`
2. **アスペクト比制御**: 16:9, 9:16, 2:1 などをネイティブサポート
3. **反復的洗練**: 生成結果に基づいてプロンプトを段階的に改善

## 技術スタック

- **ベースモデル**: Gemini 3 ファミリーの画像生成能力
- **SynthID**: DeepMind の不可視電子透かし技術（著作権・責任ある AI）
- **Vertex AI**: エンタープライズ展開向け API
- **Hugging Face**: コミュニティ向けモデル公開

## 関連概念

- [[concepts/ai-image-generation]] — AI 画像生成の全体概観
- [[concepts/reverse-engineering]] — 画像生成モデルの解析

## ソース

- [Google Cloud: Ultimate Nano Banana Prompting Guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Google Cloud: Bringing Nano Banana 2 to Enterprise](https://cloud.google.com/blog/products/ai-machine-learning/bringing-nano-banana-2-to-enterprise)
- [Gemini Nano Banana](https://gemini.google.com/)
