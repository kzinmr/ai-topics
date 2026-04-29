---
title: "Ollama — Local LLM Runner"
type: concept
created: 2026-04-15
updated: 2026-04-29
status: complete
tags: [local-llm, runner, model-management, cli, api, open-source]
aliases: [ollama-runner, ollama-cli]
related: [[concepts/inference/llama-cpp]], [[concepts/local-llm]], [[concepts/local-llm/inference-hardware]]
sources:
  - url: "https://ollama.com/"
    title: "Ollama — Official Site"
  - url: "https://github.com/ollama/ollama"
    title: "Ollama — GitHub Repository"
  - url: "https://myaiguide.co/repos/ollama-ollama"
    title: "Ollama: Run AI Models Locally (2026 Guide)"
---

# Ollama — Local LLM Runner

**Ollama** は、ローカル環境で大規模言語モデル（LLM）を実行するためのオープンソースツール。Go 言語で実装され、MIT ライセンスで公開されている。2026年4月時点で **168,000 GitHub Stars**、**月間5,200万ダウンロード** を達成し、最も広く使われているローカル LLM ランナー。

## アーキテクチャ

Ollama は **llama.cpp** を内部エンジンとして使用し、その上にモデル管理、REST API、CLI インターフェースを提供する。

```
ユーザー（CLI / API）
    ↓
Ollama（Go 実装）
    ├─ モデルレジストリ（1000+ モデル）
    ├─ Modelfile システム
    └─ llama.cpp（C++ 推論エンジン）
         ├─ GGUF 量子化
         ├─ GPU アクセラレーション（CUDA/Metal/ROCm）
         └─ CPU + GPU ハイブリッド推論
```

## 主要機能

| 機能 | 説明 |
|------|------|
| **ワンラインインストール** | `curl -fsSL https://ollama.com/install.sh \| sh` |
| **モデル管理** | `ollama pull <model>` / `ollama rm <model>` |
| **対話モード** | `ollama run <model>` で即時チャット開始 |
| **REST API** | OpenAI 互換エンドポイント（`/api/chat`, `/api/generate`） |
| **GPU 自動検出** | CUDA（NVIDIA）、Metal（Apple）、ROCm（AMD） |
| **Modelfile** | システムプロンプト、パラメータ、テンプレートをカスタム |
| **クロスプラットフォーム** | Linux、macOS、Windows |
| **マルチモデル切替** | 1つのサーバーで複数モデルをホスト |

## Modelfile 形式

```dockerfile
FROM llama3.2

# システムプロンプトの設定
SYSTEM "あなたは親切なAIアシスタントです。日本語で回答してください。"

# パラメータ設定
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 4096

# テンプレート設定
TEMPLATE """{{ .System }}
ユーザー: {{ .Prompt }}
アシスタント: """
```

## 対応モデル（2026年4月時点）

50以上の主要モデルに対応：
- **Meta**: Llama 3/3.1/3.2/4, Llama 3.3 Nemotron
- **Google**: Gemma 2/3
- **DeepSeek**: DeepSeek V3, DeepSeek-R1
- **Alibaba**: Qwen 2.5/3
- **Microsoft**: Phi-3/4
- **Mistral**: Mistral, Mixtral
- **NousResearch**: Hermes シリーズ
- **その他**: Kimi-K2.5, GLM-5, MiniMax, gpt-oss

## パフォーマンス指標

| ハードウェア | 7B Q4_K_M | 13B Q4_K_M | 70B Q4_K_M |
|------------|-----------|-----------|-----------|
| RTX 4060 (8GB) | 40+ tok/s | — | — |
| RTX 4090 (24GB) | 100+ tok/s | 50+ tok/s | 10+ tok/s |
| Mac M3 Max (96GB) | 60+ tok/s | 35+ tok/s | 8+ tok/s |
| CPU only (32GB RAM) | 5-10 tok/s | 2-5 tok/s | — |

## ユースケース

1. **開発・プロトタイピング**: ローカルで素早くモデルを試す
2. **プライベートチャット**: データを外部に送信しない
3. **エージェントバックエンド**: Ollama をローカルエージェントの LLM バックエンドとして使用
4. **教育・学習**: モデルの動作理解と実験
5. **オフライン環境**: インターネット接続不要で AI 機能を提供

## Cloud プラン（2026）

Ollama は 2026年にクラウドサービスも開始：
- **Free**: 基本クラウドアクセス
- **Pro**（$20/月）: 3並列モデル、50倍クラウド使用量
- **Max**（$100/月）: 10並列モデル、5倍使用量

## Ollama vs 他のツール

| ツール | 強み | 弱み |
|-------|------|------|
| **Ollama** | 使いやすさ、モデルレジストリ、クロスプラットフォーム | カスタマイズ性は限定的 |
| **LM Studio** | GUI、GUIでのモデル発見 | サーバーモードが弱い |
| **llama.cpp** | 最高のパフォーマンス、カスタマイズ性 | 設定が複雑 |
| **LocalAI** | OpenAI API 完全互換 | コミュニティが小さい |
| **vLLM** | 本番推論最適化 | セットアップが重い |

## 関連 wikilinks

- [[concepts/inference/llama-cpp]] — llama.cpp 推論エンジン
- [[concepts/local-llm]] — ローカル LLM エコシステム概要
- [[concepts/local-llm/inference-hardware]] — 推論ハードウェア要件
- [[concepts/inference/sglang]] — SGLang 高速推論

## ソース

- [Ollama Official Site](https://ollama.com/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Ollama: Run AI Models Locally (2026 Guide)](https://myaiguide.co/repos/ollama-ollama)
