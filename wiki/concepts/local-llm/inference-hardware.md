---
title: "Local LLM Inference Hardware"
type: concept
created: 2026-04-15
updated: 2026-04-29
status: complete
tags: [local-llm, hardware, gpu, consumer, edge, vram]
aliases: [inference-hardware, consumer-gpu-llm, local-llm-hardware]
related: [[concepts/local-llm]], [[concepts/local-llm/ollama]], [[concepts/inference/sglang]]
sources:
  - url: "https://localllm.in/blog/ollama-vram-requirements-for-local-llms"
    title: "Ollama VRAM Requirements: Complete 2026 Guide"
  - url: "https://www.spheron.network/blog/gpu-memory-requirements-llm"
    title: "GPU Memory Requirements for LLMs: VRAM Calculator"
  - url: "https://www.sitepoint.com/local-llm-hardware-requirements-mac-vs-pc-2026"
    title: "Local LLM Hardware Requirements: Mac vs PC 2026 (SitePoint)"
  - url: "https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026"
    title: "LLM Quantization Explained: INT4, INT8, FP8, AWQ, GPTQ in 2026"
---

# Local LLM Inference Hardware

**Local LLM Inference Hardware** は、ローカル環境で LLM を実行するためのハードウェア構成を指す。**VRAM 容量** が最も重要な制約であり、モデルサイズ、量子化方式、コンテキスト長によって必要なハードウェアが決まる。

## VRAM 要件の基本

### モデルサイズ別必要 VRAM（推論時）

| モデルサイズ | BF16 | FP8 | INT8 | INT4（AWQ/GPTQ） | GGUF Q4_K_M |
|------------|------|-----|------|-----------------|-------------|
| **7B** | 14GB | 7GB | 7GB | 4-5GB | 4-5GB |
| **13B** | 26GB | 13GB | 13GB | 7-8GB | 8-9GB |
| **30B** | 60GB | 30GB | 30GB | 16-18GB | 18-20GB |
| **70B** | 140GB | 70GB | 70GB | 36-40GB | 40-45GB |
| **180B** | 360GB | 180GB | 180GB | 92-100GB | — |

※KV キャッシュとフレームワークオーバーヘッドとして **15〜25% 追加** が必要

### 量子化と品質のトレードオフ

| 量子化形式 | VRAM 削減率 | 品質への影響 | 推奨用途 |
|-----------|-----------|------------|---------|
| BF16 | 0%（基準） | 基準 | 最高品質が必要な場合 |
| FP8 | 50% | 無視可能（<2%劣化） | Blackwell/Hopper GPU 最適 |
| INT8 | 50% | 軽微 | 古い GPU での代替 |
| INT4（AWQ/GPTQ） | 75% | 顕著だが実用範囲 | 70B を1GPUで動かす場合 |
| GGUF Q4_K_M | 75% | 良好 | Ollama / llama.cpp での標準 |

## コンシューマー GPU の選択肢

### NVIDIA（2026年現在）

| GPU | VRAM | メモリ帯域幅 | 対応モデル（INT4） | 価格帯 |
|-----|------|------------|-----------------|--------|
| **RTX 4060** | 8GB GDDR6 | 272 GB/s | 7B〜8B | エントリー |
| **RTX 4070** | 12GB GDDR6X | 504 GB/s | 7B〜13B | ミッドレンジ |
| **RTX 4080** | 16GB GDDR6X | 736 GB/s | 7B〜30B | ハイエンド |
| **RTX 4090** | 24GB GDDR6X | 1,008 GB/s | 7B〜30B（70BはINT4） | フラッグシップ |
| **RTX 5090** | 32GB GDDR7 | 1,792 GB/s | 7B〜30B（70Bは楽々） | 最新世代 |
| **RTX PRO 6000** | 96GB | — | 70B FP8 可能 | ワークステーション |

### Apple Silicon

| チップ | 統合メモリ | メモリ帯域幅 | 対応モデル |
|-------|-----------|------------|-----------|
| **M3 Pro** | 18-36GB | 150 GB/s | 7B〜13B |
| **M3 Max** | 36-128GB | 400 GB/s | 7B〜70B（128GBで70BF16も可能） |
| **M4 Pro/Max** | 24-128GB | M3比向上予定 | 同程度以上 |

**Apple の強み**: 統合メモリにより、コンシューマーNVIDIA では不可能な 70B+ モデルを単一デバイスで実行可能。

### AMD

| GPU | VRAM | メモリ帯域幅 | 備考 |
|-----|------|------------|------|
| **RX 7900 XTX** | 24GB GDDR6 | 960 GB/s | ROCm 対応、llama.cpp/Ollama で利用可能 |
| **MI300X** | 192GB HBM3 | 5.2 TB/s | データセンター向け |

## エッジデバイス

| デバイス | メモリ | 性能 | ユースケース |
|---------|-------|------|------------|
| **Jetson Orin NX** | 8-16GB | 70 TOPS | ロボティクス、エッジAI |
| **Jetson AGX Orin** | 32-64GB | 275 TOPS | 高度なエッジ推論 |
| **Raspberry Pi 5** | 8GB | 限定的 | 小規模モデル（<1B） |

## VRAM が最も重要な理由

**VRAM はソフトな制限ではなく、ハードな境界**。モデルが VRAM に収まらない場合、システム RAM へのオフロードが発生し、パフォーマンスが **5〜20倍低下** する。メモリ帯域幅がトークン/秒の実質的な決定要因となる。

## 購入ガイドライン（2026年）

| 予算 | 推奨構成 | 実行可能モデル |
|------|---------|--------------|
| エントリー（〜$500） | RTX 4060 8GB | 7B Q4_K_M |
| ミッドレンジ（〜$1,000） | RTX 4070/5070 12GB | 7B〜13B Q4_K_M |
| ハイエンド（〜$2,000） | RTX 4090/5090 24-32GB | 7B〜30B、70B（INT4） |
| プロ（〜$4,000+） | Mac M3 Max 128GB / 2x RTX 5090 | 70B+、マルチGPU |
| データセンター | H100/B200 / DGX | あらゆるモデル |

## 関連 wikilinks

- [[concepts/local-llm]] — ローカル LLM エコシステム概要
- [[concepts/local-llm/ollama]] — Ollama ローカル LLM ランナー
- [[concepts/inference/sglang]] — SGLang 高速推論
- [[concepts/inference/llama-cpp]] — llama.cpp CPU/Apple 推論

## ソース

- [Ollama VRAM Requirements Guide](https://localllm.in/blog/ollama-vram-requirements-for-local-llms)
- [GPU Memory Requirements for LLMs](https://www.spheron.network/blog/gpu-memory-requirements-llm)
- [Local LLM Hardware Requirements: Mac vs PC 2026](https://www.sitepoint.com/local-llm-hardware-requirements-mac-vs-pc-2026)
- [LLM Quantization Explained 2026](https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026)
