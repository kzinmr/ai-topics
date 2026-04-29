---
title: "AI Image Generation"
type: concept
aliases:
  - ai-image-generation
  - text-to-image
  - image-synthesis
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - image-generation
  - generative-ai
  - multimodal
status: complete
sources:
  - url: "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana"
    title: "The Ultimate Nano Banana Prompting Guide (Google Cloud)"
  - url: "https://arxiv.org/abs/2204.06125"
    title: "Imagen: Photorealistic Text-to-Image Diffusion Models (Google, 2022)"
  - url: "https://stability.ai/"
    title: "Stable Diffusion — Stability AI"
---

# AI Image Generation

**AI Image Generation（AI画像生成）** は、自然言語のテキスト記述から画像を生成する人工知能技術。拡散モデル（Diffusion Models）、GAN（Generative Adversarial Networks）、自己回帰モデル（Autoregressive Models）などをベースに、2022年以降急速に発展した。

## 主要なアーキテクチャ

### 拡散モデル（Diffusion Models）
現在の主流。ノイズから徐々に画像を復元するプロセスを学習：
- **Stable Diffusion**: オープンソースのデファクトスタンダード（Stability AI）
- **DALL-E 3**: OpenAI の最新画像生成モデル
- **Imagen**: Google の高品質テキスト-画像モデル
- **Midjourney**: クリエイティブ業界で最も人気
- **Nano Banana 2**: Google/Gemini 3 の最新モデル（推論+Web検索連携）

### GAN（Generative Adversarial Networks）
生成器と識別器の競争による学習：
- StyleGAN シリーズ（NVIDIA）
- 主に顔生成・スタイル変換に使用

### 自己回帰モデル
- Parti（Google）: トランスフォーマーベース
- DALL-E 1/2: VQ-VAE + トランスフォーマー

## 主要機能の比較（2026年）

| 機能 | Stable Diffusion | DALL-E 3 | Midjourney | Nano Banana 2 |
|------|----------------|----------|-----------|--------------|
| オープンソース | ✅ | ❌ | ❌ | ❌ |
| ローカル実行 | ✅（GPU必要） | ❌ | ❌ | ❌ |
| キャラクター一貫性 | ⚠️ 部分的 | ✅ | ✅ | ✅ |
| テキストレンダリング | ⚠️ 苦手 | ✅ | ✅ | ✅（Pro） |
| Web検索連携 | ❌ | ❌ | ❌ | ✅ |
| リアルタイム編集 | ❌ | ⚠️ | ❌ | ✅ |
| アップスケーリング | 別ツール必要 | 内蔵 | 内蔵 | 2K/4K対応 |

## プロンプティングベストプラクティス

### 構造化プロンプトパターン
1. **主題**: 何を生成するか（「赤いドレスを着た女性」）
2. **スタイル**: 芸術的方向性（「油絵風、印象派」）
3. **環境**: 背景と照明（「夕日、ビーチ、暖かい光」）
4. **技術的指定**: アスペクト比、品質キーワード

### ネガティブプロンプト
生成してほしくない要素を指定：
```
ネガティブプロンプト: 歪んだ手、6本指、変形した顔、低品質、ぼやけた
```

## 技術的課題

| 課題 | 説明 | 対策 |
|------|------|------|
| **手/指の歪み** | 複雑な関節構造の理解不足 | 改良モデル、ControlNet |
| **キャラクター一貫性** | 複数画像で同一キャラ維持困難 | IP-Adapter、LoRA |
| **テキストレンダリング** | 画像内の文字が崩れる | 専用モデル、文字認識損失 |
| **著作権・倫理** | 学習データの権利問題 | SynthID 電子透かし、規制 |

## 関連概念

- [[concepts/nano-banana-2]] — Google の最新画像生成モデル
- [[concepts/reverse-engineering]] — 画像生成モデルの解析
- [[concepts/inference/sglang]] — 推論最適化（画像生成にも応用）

## ソース

- [Google Cloud: Ultimate Nano Banana Prompting Guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Imagen: Photorealistic Text-to-Image Diffusion Models (arXiv)](https://arxiv.org/abs/2204.06125)
- [Stable Diffusion](https://stability.ai/)
