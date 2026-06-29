---
title: "OpenAI Jalapeño Inference Chip"
created: 2026-06-25
updated: 2026-06-25
type: concept
tags:
  - openai
  - broadcom
  - hardware
  - infrastructure
  - llm-inference
  - asic
  - optimization
  - announcement
sources:
  - raw/articles/openai.com--index-openai-broadcom-jalapeno-inference-chip--f8a3b2c1.md
  - raw/articles/2026-06-25_techcrunch-openai-broadcom-jalapeno.md
---

# OpenAI Jalapeño Inference Chip

The Jalapeño chip is OpenAI's first custom-built inference processor, an AI accelerator co-developed with Broadcom (NASDAQ: AVGO) and Celestica. Announced on June 24, 2026, it represents OpenAI's entry into silicon design as part of a multi-generation compute platform strategy. The chip is architected from the ground up around the unique demands of large language model (LLM) inference, informed by OpenAI's deep understanding of model kernels, memory movement, networking, and serving patterns.

## Architecture and Design

Jalapeño was designed from scratch for LLM inference workloads rather than adapted from general-purpose GPU architectures. Key architectural decisions include:

- **Inference-first design**: Unlike GPUs that also serve training workloads, Jalapeño targets the specific computational and memory-access patterns of running pre-built AI models in response to user requests.
- **Reduced data movement**: The architecture minimizes data transfer overhead, balancing compute, memory, and networking to achieve realized utilization close to theoretical peak performance.
- **Broadcom silicon implementation**: Broadcom contributed chip implementation, board and rack system integration, and Tomahawk networking silicon for large-scale production.
- **Celestica manufacturing**: Celestica provided high-performance networking and scalable production systems.

The chip is designed to work flexibly with all LLMs, guided by OpenAI's insights into the inference needs of current and future AI models across the industry.

## Development Timeline

A standout achievement is the **nine-month tape-out cycle**, from design initiation to working silicon. OpenAI's own AI models assisted in accelerating the chip development process. Engineering samples are already running ML workloads in the lab at production target frequency and power, including GPT-5.3-Codex-Spark.

## Performance and Efficiency

Early testing shows that Jalapeño delivers **performance-per-watt substantially better than current state-of-the-art** alternatives. This efficiency gain is critical for inference economics, where even small reductions in per-token cost compound across billions of daily requests. The chip is particularly optimized for real-time coding models and other latency-sensitive inference workloads.

## Strategic Significance

### Reducing NVIDIA Dependency

Jalapeño is widely seen as OpenAI's move to reduce dependence on NVIDIA GPUs for inference. While more performance-intensive tasks like pre-training are expected to continue relying on NVIDIA hardware, inference represents the majority of operational costs for AI service providers.

### Full-Stack Integration

As OpenAI stated: "OpenAI is not only developing frontier models or building products on top of them; it is designing the infrastructure underneath them: chip architecture, kernels, memory systems, networking, scheduling, deployment systems, and product experience." By controlling the full stack, each layer can be optimized around the same goal — making models faster, more reliable, and more affordable.

### Multi-Generation Platform

The companies emphasized that Jalapeño is "the first AI accelerator in a multi-generation compute platform." Deployment is planned at gigawatt scale with data center partners including Microsoft, beginning in 2026.

## Leadership Statements

- **Greg Brockman** (President, OpenAI): "Jalapeño is part of our long-term full-stack infrastructure strategy to make compute more abundant, resulting in AI which is faster, more reliable, more affordable."
- **Richard Ho** (OpenAI Hardware Lead): "We optimized the architecture around the kernels, memory movement, networking, and serving patterns that matter most for frontier AI models."
- **Hock Tan** (President/CEO, Broadcom): "This is just the beginning of a multi-generation roadmap. By co-developing our industry-leading silicon directly with OpenAI, we are enabling the deployment of gigawatt scale data centers."

## Open Questions

- What is the absolute performance (tokens/second, latency) compared to NVIDIA H100/H200/B200 for equivalent models?
- How does Jalapeño handle the diverse model architectures that may emerge over the next hardware generation?
- What are the software ecosystem and toolchain requirements for developers targeting this chip?
- How does Broadcom's involvement compare to other custom chip partnerships (e.g., Google's TPU development)?

## Related Pages

- [[entities/openai]] — OpenAI company page
- [[concepts/ai-affordability-crisis]] — Economic pressures driving custom silicon investment
- [[entities/nvidia]] — Primary GPU supplier and competitive context
- [[concepts/kv-aware-routing]] — Complementary inference optimization technique
