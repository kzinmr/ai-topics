---
title: "LLM Observability"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - infrastructure
  - evaluation
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

> Production monitoring and debugging for LLM applications. Integrates traditional observability (metrics, logs, traces) with LLM-specific signals (token consumption, quality evaluation, agent behavior tracking).

## Relationship to Existing Pages

This page is a superset of [[concepts/ai-observability]], organizing LLM observability specifically from an **inference infrastructure** perspective. See existing pages for details on quality evaluation and agent tracing.

## Outline

### 1. Inference Infrastructure Metrics

#### Latency Metrics
| Metric | Definition | Priority | Threshold |
|-----------|------|--------|---------|
| **TTFT** (Time to First Token) | From request send to first token generation | ⭐⭐⭐ | < 500ms (streaming), < 2s (interactive) |
| **TPOT** (Time per Output Token) | Generation time per output token | ⭐⭐⭐ | < 10ms/token |
| **ITL** (Inter-Token Latency) | Token interval = 1/TPOT | ⭐⭐ | Stable, no spikes |
| **End-to-end latency** | Full request completion time | ⭐⭐⭐ | Depends on use case |

#### Throughput Metrics
| Metric | Definition | Notes |
|-----------|------|------|
| **Tokens/sec** (output) | Output tokens per second | Batch size × model speed |
| **Requests/sec** | Requests processed per second | Depends on prompt length |
| **Input tokens/sec** | Input tokens processed per second | Prefill throughput |
| **KV Cache hit rate** | Prefix cache hit rate | SGLang RadixAttention effectiveness |

#### Resource Metrics
| Metric | Reason for Monitoring |
|-----------|---------|
| **GPU Utilization** | Idle or compute-bound |
| **VRAM Usage** | OOM prevention, KV Cache pressure detection |
| **Memory Bandwidth Utilization** | Memory-bound vs compute-bound |
| **Power Draw** | Cost optimization, thermal throttling detection |
| **NVLink / PCIe bandwidth** | Multi-GPU communication bottleneck detection |

### 2. LLM-Specific Signals

- **Token Cost Tracking**: Token consumption per model and per request
- **Prefill vs Decode Ratio**: Ratio of prefill time to decode time (model/workload characteristics)
- **Batch Efficiency**: Gap between actual and ideal batch size
- **KV Cache Pressure**: Current cache usage vs maximum capacity ratio
- **Scheduling Delay**: Time requests waited in the batch scheduler

### 3. Quality Signals (Inference Side)

- **Generation diversity**: Output variance for identical prompts
- **Token-level probability**: Frequency of low-probability tokens (hallucination indicator)
- **Response length distribution**: Output length distribution by request type
- **Error rates**: Rate limits, context length exceeded, timeouts

### 4. Observability Stack Components

| Layer | Tools | Role |
|---------|-------|------|
| **Metrics collection** | Prometheus + node-exporter + DCGM | GPU metric collection |
| **Logging** | ELK/Loki + vector | Request/response logging |
| **Tracing** | OpenTelemetry + Jaeger/Tempo | Request flow tracing |
| **LLM-specific** | Arize AI, LangSmith, Weights & Biases | Token, quality, agent tracing |
| **Dashboard** | Grafana | Visualization and alerting |
| **Alerting** | PagerDuty/OpsGenie + AlertManager | Anomaly detection and notification |

### 5. vLLM Observability Integration

- **vLLM Prometheus Metrics**: Exposed via `/metrics` endpoint
  - `vllm:time_to_first_token_seconds`
  - `vllm:time_per_output_token_seconds`
  - `vllm:request_success_total`
  - `vllm:gpu_cache_usage_perc`
  - `vllm:num_requests_waiting`
- **OpenTelemetry Tracing**: OTel trace propagation supported in vLLM v0.19+
- **Logging**: Request logging via `--log-requests`

### 6. Production Observability Patterns

#### Cost Attribution
- Token consumption tracking by model, endpoint, and user
- Cost breakdown by prefill/decode ratio
- Measuring cost reduction from KV Cache sharing

#### Degradation Detection
- P99 TTFT spike → Queueing delay or resource shortage
- TPOT spike → Memory bandwidth contention or throttling
- Error rate increase → Model failure or misconfiguration

#### Capacity Planning
- Future scaling prediction from GPU utilization and throughput
- VRAM planning from context length distribution analysis
- Buffer design for peak load

## Related Pages

- [[concepts/ai-observability]] — Detailed LLM observability guide (quality, agent tracing)
- [[concepts/serving-llms-vllm]] — vLLM metrics & monitoring
- [[concepts/ai-infrastructure-engineering/model-serving-autoscaling]] — Metrics as scaling signals
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — GPU resource monitoring fundamentals
- [[concepts/ai-infrastructure-engineering/_index]] — Parent page

## TODO

- [ ] Add Prometheus recording rules for derived metrics (e.g., TTFT P99 per model)
- [ ] Add Grafana dashboard panel definitions
- [ ] Add OpenTelemetry instrumentation guide for vLLM/SGLang
- [ ] Add cost attribution query examples (PromQL)
- [ ] Add TensorRT-LLM metrics (if different from vLLM)
- [ ] Add Arize/LangSmith integration patterns
- [ ] Add DCGM (NVIDIA GPU monitor) exporter config
