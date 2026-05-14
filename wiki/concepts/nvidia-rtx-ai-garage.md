---
title: NVIDIA RTX AI Garage
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [concept, nvidia, product, ai-agents, local-llm, hardware, ecosystem]
sources:
  - "raw/articles/2026-05-13_nvidia_rtx-ai-garage-hermes-agent-dgx-spark.md"
  - https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/
  - https://www.nvidia.com/en-us/ai-on-rtx/
---

# NVIDIA RTX AI Garage

NVIDIAのRTX AI Garageは、RTXハードウェア（RTX PC、RTX PROワークステーション、DGX Spark）上で動作するAIツール・モデル・エージェントの最適化・キュレーション・推奨を行うプログラム。オープンソースAIエコシステムとNVIDIAハードウェアの橋渡し役を担う。

## プログラムの位置づけ

RTX AI Garageは単なるブログシリーズではなく、以下の要素で構成される最適化レイヤー：

- **キュレーション**: オープンソースのAIエージェント・モデルからRTXハードウェアで最も効果的に動作するものを選定・推奨
- **Playbook**: GitHub上の`dgx-spark-playbooks`リポジトリで具体的なセットアップ手順を提供
- **最適化検証**: NVFP4量子化、TensorRT-LLM高速化などのNVIDIA技術とオープンソースツールの組み合わせをベンチマーク
- **ハンズオンセッション**: "Build It Yourself" agentic AIシリーズでNemoClaw + OpenShellの実践ワークショップを開催

## 推奨エージェントフレームワーク

### Hermes Agent（2026年5月〜）
- **選定理由**: Self-improving skills、contained sub-agents、reliability by design
- **140K+ GitHub stars / 3ヶ月** — 圧倒的なコミュニティ採用
- **OpenRouter最利用エージェント**（2026年5月）
- **同一モデルで優れた結果**: "active orchestration layer"としての設計
- **推奨モデル**: Qwen 3.6 35B（20GBメモリで120B級知能）

### NemoClaw（2026年3月〜）
- NVIDIA純正のセキュアエージェント開発スタック
- OpenShell sandbox + Privacy Router + Network Policy Engine
- 2026年5月にWSL2対応を追加

### OpenClaw（先行）
- RTX AI Garage最初の推奨エージェント
- "Build a Claw"キャンペーンで成功
- エッジデバイス/DGX Spark向け軽量設計

## 対応モデル・最適化

| モデル | 最適化 | 対象ハードウェア | 発表時期 |
|--------|--------|-----------------|----------|
| Qwen 3.6 35B | 汎用推論 | DGX Spark, RTX PRO | 2026-05 |
| Qwen 3.6 27B | 汎用推論（密） | RTX PRO | 2026-05 |
| Gemma 4 26B/31B | NVFP4 + Multi-Token Prediction | Blackwell GPU | 2026-05 |
| Mistral Medium 3.5 | llama.cpp/Ollama互換 | RTX PRO, DGX Spark | 2026-04 |
| GPT-OSS-120B | MXFP4量子化 | DGX Spark | 継続 |

## RTX AI Garageが提供する付加価値

DGX Sparkを自分でセットアップする場合と比較して、RTX AI Garage経由だと：

1. **モデル選定の手間削減**: NVIDIAが各モデルをDGX Spark上でベンチマークし、最適な量子化形式（NVFP4/MXFP4）を指定。ユーザーは自分でモデル比較・量子化実験をする必要がない
2. **Playbookによる時短**: 公式セットアップ手順がGitHubで公開されており、試行錯誤の時間を節約
3. **NVFP4最適化の恩恵**: NVIDIA独自のNVFP4量子化はBlackwell GPUのTensor Coresに最適化されており、汎用量子化より高速。自分でセットアップするとこの最適化が得られない可能性がある
4. **ハードウェア・ソフトウェア統合検証**: TensorRT-LLM、CUDA-X、NIMなどNVIDIAソフトウェアスタックとの統合が事前検証済み
5. **コミュニティ + 公式サポート**: ハンズオンセッション、ニュースレター、ソーシャルメディアでの継続的アップデート

## 情報チャネル

- **ブログ**: [blogs.nvidia.com](https://blogs.nvidia.com/blog/) — RTX AI Garageタグ付き記事
- **GitHub**: [NVIDIA/dgx-spark-playbooks](https://github.com/NVIDIA/dgx-spark-playbooks)
- **ニュースレター**: RTX AI PC newsletter（NVIDIA AI PCページから購読）
- **ソーシャル**: Facebook, Instagram, TikTok, X @NVIDIA
- **ワークステーション**: LinkedIn, X @NVIDIAWorkstation

## Related

- [[entities/nvidia-dgx-spark]] — DGX Spark hardware platform
- [[entities/hermes-agent]] — Hermes Agent by Nous Research
- [[entities/nvidia-nemoclaw]] — NemoClaw secure agent framework
- [[entities/openclaw]] — OpenClaw agent framework
- [[concepts/local-ai]] — Local AI landscape (May 2026)
- [[concepts/harness-engineering]] — Harness engineering (agent framework optimization)
