---
title: "Model Serving & Autoscaling"
type: concept
created: 2026-05-01
updated: 2026-05-26
tags:
  - concept
  - inference
  - infrastructure
  - developer-tooling
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

> Infrastructure design for serving LLM models in production. Covers deployment configurations, scaling strategies, load balancing, and cost management.

## Why This Matters

LLM inference servers have fundamentally different load characteristics from traditional web applications:
- **Model pinned to GPU memory**: Cold starts take minutes
- **Dynamic KV cache consumption**: VRAM usage fluctuates per request
- **Throughput vs latency tradeoff**: Larger batch sizes increase throughput but also latency
- **Continuous batching**: Makes static load estimation difficult

## Outline

### 1. Deployment Architectures

#### Self-hosted (Private GPU)
- **vLLM**: Industry standard open-source inference server
- **SGLang**: Optimized for agent loops and prefix caching
- **TensorRT-LLM**: Integrates with NVIDIA Triton Inference Server

#### Managed Inference
- **Together AI / Fireworks / Groq**: Fast managed inference
- **Anyscale / Modal / Replicate**: Serverless GPU
- **Cloud AI platforms**: GCP Vertex AI, AWS SageMaker, Azure ML

#### Edge / Local
- **llama.cpp / Ollama**: Local GPU/CPU
- **Apple MLX**: Apple Silicon optimization

### 2. Autoscaling Strategies

LLM server scaling faces these challenges:
- **Warm-up time**: Model loading takes minutes, GPU memory allocation takes time
- **KV Cache fragmentation**: VRAM consumption follows request count fluctuations
- **GPU availability**: Spot instance interruption risk

#### Scaling Signals

| Signal | Pros | Cons |
|--------|------|------|
| **Request queue depth** | Accurate load metric | Delayed response |
| **GPU utilization** | Hardware intuition | Low utilization during KV cache only |
| **KV cache pressure** | Accurate memory metric | Complex to implement |
| **In-flight requests** | Simple | Does not account for batch depth |
| **Token throughput** | Business metric | Depends on model and prefill ratio |

#### Scaling Patterns

- **HPA (Horizontal Pod Autoscaler)**:
  - K8s standard, monitors GPU utilization via custom metrics
  - Challenge: Scale-up latency (model loading time)
  
- **Predictive Scaling**:
  - Time-of-day based pre-scaling
  - Prompt length distribution prediction
  
- **Request Batching Autoscaler**:
  - Dynamic optimization of queue depth and continuous batching
  
- **Serverless GPU**:
  - Modal / Replicate style: Pay per request
  - Cold start challenge (FaaS paradigm)

### 3. Load Balancing Strategies

| Strategy | Behavior | Effective Use Case |
|------|------|-------------|
| **Round Robin** | Assigns in order | All replicas same performance |
| **Least Connections** | Least in-flight requests | Variable-length contexts |
| **LRU Routing** | Routes same prefix to same Pod | Maximizes prefix caching |
| **Semantic Routing** | Embedding-based router selection | Model specialization |
| **Consistent Hashing** | Routes by prefix hash | Deterministic cache hits |

### 4. Multi-Model Serving

- **Multiple models on single GPU**: GPU partitioning strategies
- **LoRA Adapter Serving**: vLLM Multi-LoRA functionality
- **Model Router**: Routes to optimal model based on request content
- **Speculative Decoding Server**: Draft model + Target model pair configuration

### 5. Cost Optimization Patterns

- **Spot GPU instances**: ~70% discount, interruption handling required
- **Reserved capacity**: For baseline load
- **Batch processing vs Real-time**: Low-cost batch API design
- **Prefix caching across requests**: Shared caching for identical system prompts
- **KV cache quantization**: TurboQuant (2-bit KV cache, 4x capacity)

### 6. Infrastructure Components

| Component | Role | Options |
|--------------|------|--------|
| **GPU Scheduler** | Task-to-GPU allocation | Kubernetes + volcano/gpu-operator |
| **Model Registry** | Model version management | MLflow, HuggingFace Hub |
| **API Gateway** | Auth, rate limiting, billing | Envoy, Kong, AWS API Gateway |
| **Observability** | Monitoring & alerting | Prometheus + Grafana, Arize, LangSmith |
| **Queue** | Request buffering | Redis, RabbitMQ, Keda |

### 7. Production Checklist

- [ ] Appropriate GPU memory model-buffer ratio
- [ ] Max context length and batch size limits
- [ ] Automatic OOM (Out of Memory) recovery
- [ ] Hot-swappable model version management
- [ ] Cost vs latency SLO definition
- [ ] Continuous batching buffer configuration

## Related Pages

- [[concepts/serving-llms-vllm]] — vLLM serving patterns
- [[concepts/inference/vllm]] — vLLM feature details
- [[concepts/inference/sglang]] — SGLang for agent workloads
- [[concepts/kv-cache]] — VRAM management fundamentals
- [[concepts/prompt-caching]] — Cost optimization strategies
- [[concepts/ai-infrastructure-engineering/gpu-vram-fundamentals]] — Hardware constraints
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

