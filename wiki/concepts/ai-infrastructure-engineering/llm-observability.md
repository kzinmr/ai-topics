---
title: "LLM Observability"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - observability
  - monitoring
  - tracing
  - evaluation
  - infrastructure
status: L1
aliases:
  - llm-observability
  - ai-observability-deep
  - production-monitoring
sources: []
related:
  - "[[concepts/ai-observability]]"
  - "[[concepts/serving-llms-vllm]]"
  - "[[concepts/ai-infrastructure-engineering/model-serving-autoscaling]]"
  - "[[concepts/ai-infrastructure-engineering/_index]]"
---

# LLM Observability

> LLMアプリケーションの本番監視とデバッグ。従来のオブザーバビリティ（メトリクス・ログ・トレース）に加え、LLM特有のシグナル（トークン消費、品質評価、エージェント行動追跡）を統合する。

## Relationship to Existing Pages

このページは [[concepts/ai-observability]] の上位概念であり、特に**推論インフラ**の観点からLLMオブザーバビリティを整理する。品質評価・エージェントトレースの詳細は既存ページを参照。

## Outline

### 1. Inference Infrastructure Metrics

#### レイテンシ指標
| メトリクス | 定義 | 重要度 | 閾値目安 |
|-----------|------|--------|---------|
| **TTFT** (Time to First Token) | リクエスト送信から最初のトークン生成まで | ⭐⭐⭐ | < 500ms (streaming), < 2s (interactive) |
| **TPOT** (Time per Output Token) | 出力トークン1個あたりの生成時間 | ⭐⭐⭐ | < 10ms/token |
| **ITL** (Inter-Token Latency) | トークン間隔 = 1/TPOT に相当 | ⭐⭐ | Stable, no spikes |
| **End-to-end latency** | 全リクエスト完了時間 | ⭐⭐⭐ | ユースケース依存 |

#### スループット指標
| メトリクス | 定義 | 注釈 |
|-----------|------|------|
| **Tokens/sec** (出力) | 秒間出力トークン数 | バッチサイズ×モデル速度 |
| **Requests/sec** | 秒間リクエスト処理数 | プロンプト長依存 |
| **Input tokens/sec** | 秒間入力トークン処理数 | プリフィルスループット |
| **KV Cache hit rate** | プレフィックスキャッシュのヒット率 | SGLang RadixAttention有効性 |

#### リソース指標
| メトリクス | 監視理由 |
|-----------|---------|
| **GPU Utilization** | アイドルかcompute-boundか |
| **VRAM Usage** | OOM予防、KV Cache圧迫検知 |
| **Memory Bandwidth Utilization** | Memory-bound vs compute-bound |
| **Power Draw** | コスト最適化、サーマルスロットリング検知 |
| **NVLink / PCIe bandwidth** | マルチGPU通信のボトルネック検知 |

### 2. LLM-Specific Signals

- **Token Cost Tracking**: モデル別・リクエスト別のトークン消費
- **Prefill vs Decode Ratio**: プリフィル時間/デコード時間の比率（モデル・ワークロード特性）
- **Batch Efficiency**: 実際のバッチサイズと理想バッチサイズの乖離
- **KV Cache Pressure**: 現在のキャッシュ使用率と最大容量の比率
- **Scheduling Delay**: リクエストがバッチスケジューラで待機した時間

### 3. Quality Signals (Inference Side)

- **Generation diversity**: 同一プロンプトに対する出力のばらつき
- **Token-level probability**: 低確率トークンの頻度（ハルシネーション指標）
- **Response length distribution**: リクエストタイプ別の出力長分布
- **Error rates**: レート制限、コンテキスト長超過、タイムアウト

### 4. Observability Stack Components

| レイヤー | ツール | 役割 |
|---------|-------|------|
| **Metrics collection** | Prometheus + node-exporter + DCGM | GPUメトリクス収集 |
| **Logging** | ELK/Loki + vector | リクエスト・レスポンスログ |
| **Tracing** | OpenTelemetry + Jaeger/Tempo | リクエストフロー追跡 |
| **LLM-specific** | Arize AI, LangSmith, Weights & Biases | トークン・品質・エージェントトレース |
| **Dashboard** | Grafana | 可視化・アラーティング |
| **Alerting** | PagerDuty/OpsGenie + AlertManager | 異常検知・通知 |

### 5. vLLM Observability Integration

- **vLLM Prometheus Metrics**: `/metrics` エンドポイントで公開
  - `vllm:time_to_first_token_seconds`
  - `vllm:time_per_output_token_seconds`
  - `vllm:request_success_total`
  - `vllm:gpu_cache_usage_perc`
  - `vllm:num_requests_waiting`
- **OpenTelemetry Tracing**: vLLM v0.19+ でOTel trace propagation対応
- **Logging**: `--log-requests` でリクエストログ出力

### 6. Production Observability Patterns

#### Cost Attribution
- モデル別・エンドポイント別・ユーザー別のトークン消費追跡
- プリフィル/デコード比率によるコスト内訳
- KV Cache共有によるコスト削減効果の測定

#### Degradation Detection
- TTFTのP99スパイク → キューイング遅延 or リソース不足
- TPOTのスパイク → メモリ帯域幅競合 or スロットリング
- エラーレート上昇 → モデル障害 or 設定ミス

#### Capacity Planning
- GPU使用率とスループットの関係から将来のスケーリング予測
- コンテキスト長分布の分析によるVRAM計画
- ピーク負荷時のバッファリング設計

## Related Pages

- [[concepts/ai-observability]] — Detailed LLM observability guide（品質・エージェントトレース）
- [[concepts/serving-llms-vllm]] — vLLM metrics & monitoring
- [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — スケーリングシグナルとしてのメトリクス
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPUリソース監視の基礎
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## TODO

- [ ] Add Prometheus recording rules for derived metrics (e.g., TTFT P99 per model)
- [ ] Add Grafana dashboard panel definitions
- [ ] Add OpenTelemetry instrumentation guide for vLLM/SGLang
- [ ] Add cost attribution query examples (PromQL)
- [ ] Add TensorRT-LLM metrics (if different from vLLM)
- [ ] Add Arize/LangSmith integration patterns
- [ ] Add DCGM (NVIDIA GPU monitor) exporter config
