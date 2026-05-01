---
title: "Model Serving & Autoscaling"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - serving
  - autoscaling
  - load-balancing
  - infrastructure
  - deployment
status: L1
aliases:
  - model-serving
  - llm-serving
  - inference-serving
  - autoscaling-llm
sources: []
related:
  - "[[concepts/serving-llms-vllm]]"
  - "[[concepts/inference/_index]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/inference/sglang]]"
  - "[[concepts/kv-cache]]"
  - "[[concepts/prompt-caching]]"
  - "[[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
---

# Model Serving & Autoscaling

> LLMモデルを本番環境でサーブするためのインフラ設計。デプロイメント構成、スケーリング戦略、ロードバランシング、コスト管理までをカバーする。

## Why This Matters

LLM推論サーバーは従来のWebアプリケーションと根本的に異なる負荷特性を持つ:
- **GPUメモリに固定されたモデル**: コールドスタートに数分かかる
- **KVキャッシュの動的消費**: リクエストごとにVRAM消費が変動
- **スループットとレイテンシのトレードオフ**: バッチサイズが大きいほどスループットは高いがレイテンシも増加
- **継続的バッチング**: 静的な負荷想定が困難

## Outline

### 1. Deployment Architectures

#### Self-hosted (Private GPU)
- **vLLM**: 業界標準のオープンソース推論サーバー
- **SGLang**: エージェントループとプレフィックスキャッシュに最適化
- **TensorRT-LLM**: NVIDIA Triton Inference Serverと統合

#### Managed Inference
- **Together AI / Fireworks / Groq**: 高速マネージド推論
- **Anyscale / Modal / Replicate**: Serverless GPU
- **Cloud AI platforms**: GCP Vertex AI, AWS SageMaker, Azure ML

#### Edge / Local
- **llama.cpp / Ollama**: ローカルGPU/CPU
- **Apple MLX**: Apple Silicon最適化

### 2. Autoscaling Strategies

LLMサーバーのスケーリングは以下が課題:
- **Warm-up time**: モデルロードに数分、GPUメモリ割り当てに時間
- **KV Cache fragmentation**: リクエスト数の増減にVRAM消費が追随
- **GPU availability**: スポットインスタンスの中断リスク

#### Scaling Signals

| Signal | 長所 | 短所 |
|--------|------|------|
| **Request queue depth** | 正確な負荷指標 | 遅延応答 |
| **GPU utilization** | ハードウェア直感 | KV cacheのみのときは低利用率 |
| **KV cache pressure** | 正確なメモリ指標 | 実装が複雑 |
| **In-flight requests** | シンプル | バッチ深さを考慮しない |
| **Token throughput** | ビジネス指標 | モデル・プリフィル比率に依存 |

#### Scaling Patterns

- **HPA (Horizontal Pod Autoscaler)**:
  - K8s標準、カスタムメトリクスでGPU utilizationを監視
  - 課題: スケールアップの遅延（モデルロード時間）
  
- **Predictive Scaling**:
  - 時間帯ベースの事前スケーリング
  - プロンプトレングス分布の予測
  
- **Request Batching Autoscaler**:
  - キューの深さと連続バッチングの動的最適化
  
- **Serverless GPU**:
  - Modal / Replicate style: リクエスト単位で課金
  - コールドスタートが課題（Function as a Serviceパラダイム）

### 3. Load Balancing Strategies

| 戦略 | 動作 | 有効なケース |
|------|------|-------------|
| **Round Robin** | 順番に割り当て | 全レプリカが同性能 |
| **Least Connections** | 最小インフライトリクエスト | 可変長コンテキスト |
| **LRU Routing** | 同一プレフィックスを同一Podにルーティング | Prefix caching最大活用 |
| **Semantic Routing** | 埋め込みベースでルーター選択 | モデル専門化 |
| **Consistent Hashing** | プレフィックスハッシュでルーティング | 確定的キャッシュヒット |

### 4. Multi-Model Serving

- **単一GPUで複数モデル**: GPUパーティショニング戦略
- **LoRA Adapter Serving**: vLLMのMulti-LoRA機能
- **Model Router**: リクエスト内容に応じて最適なモデルにルーティング
- **Speculative Decoding Server**: Draftモデル+Targetモデルのペア構成

### 5. Cost Optimization Patterns

- **Spot GPU instances**: 〜70%割引、中断処理設計が必須
- **Reserved capacity**: ベースライン負荷に
- **Batch processing vs Real-time**: バッチAPIの低コスト設計
- **Prefix caching across requests**: 同一システムプロンプトのキャッシュ共有
- **KV cache quantization**: TurboQuant（2bit KV cache, 4x capacity）

### 6. Infrastructure Components

| コンポーネント | 役割 | 選択肢 |
|--------------|------|--------|
| **GPU Scheduler** | タスク-GPU割り当て | Kubernetes + volcano/gpu-operator |
| **Model Registry** | モデルバージョン管理 | MLflow, HuggingFace Hub |
| **API Gateway** | 認証・レート制限・課金 | Envoy, Kong, AWS API Gateway |
| **Observability** | 監視・アラーティング | Prometheus + Grafana, Arize, LangSmith |
| **Queue** | リクエストバッファリング | Redis, RabbitMQ, Keda |

### 7. Production Checklist

- [ ] GPUメモリの適切なモデル-バッファ比率設定
- [ ] 最大コンテキスト長とバッチサイズの制限
- [ ] OOM (Out of Memory) からの自動復旧
- [ ] ホットスワップ可能なモデルバージョン管理
- [ ] コストvsレイテンシのSLO定義
- [ ] 継続的バッチングのバッファリング設定

## Related Pages

- [[concepts/serving-llms-vllm]] — vLLM serving patterns
- [[concepts/inference/vllm]] — vLLM feature details
- [[concepts/inference/sglang]] — SGLang for agent workloads
- [[concepts/kv-cache]] — VRAM管理の基礎
- [[concepts/prompt-caching]] — コスト最適化戦略
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — ハードウェア制約
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## Skills Reference

- `serving-llms-vllm` — vLLM deployment & configuration
- `llama-cpp` — Local inference setup

## TODO

- [ ] Add vLLM deployment YAML examples (K8s)
- [ ] Add autoscaling HPA config with custom metrics
- [ ] Add load balancing comparison benchmarks
- [ ] Add cost per 1M tokens calculation for different deployment models
- [ ] Add multi-node inference serving patterns (Tensor Parallel across nodes)
- [ ] Add prefix caching autoscaling integration (LRU routing deep-dive)
- [ ] Add serverless GPU cold start benchmarks
