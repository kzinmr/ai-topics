---
title: "Modal Labs"
type: entity
created: 2026-05-08
updated: 2026-07-09
tags:
  - company
  - infrastructure
  - hardware
aliases: ["Modal", "Modal Labs, Inc."]
sources:
  - https://modal.com/
  - https://modal.com/company
  - raw/articles/modal.com--blog-spec-is-all-u-need--42b624c7.md
  - raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa.md
  - raw/articles/modal.com--blog-unpacking-sandbox-startup-latency--b8f065a9.md
  - raw/articles/modal.com--blog-achieve-sota-specdec--da236272.md
  - raw/newsletters/2026-07-08-why-ai-infrastructure-must-evolve-for-agent-experience-akshat-bubna-modal-cto.md
---

# Modal Labs

Modal is a serverless GPU cloud platform for AI and data teams. It lets developers run CPU, GPU, and data-intensive compute at scale using a pay-per-use model — scaling from zero to thousands of GPUs in seconds via simple Python code.

| | |
|---|---|
| **Type** | AI Infrastructure / Cloud Platform |
| **Founded** | 2021 (New York City, NY) |
| **Leadership** | Erik Bernhardsson (Co-founder & CEO), Akshat Bubna (Co-founder) |
| **Key Products** | Modal Inference, Modal Sandboxes, Modal Training, Modal Batch, Modal Notebooks |
| **Website** | [modal.com](https://modal.com) |
| **Tech Blog** | [modal.com/blog](https://modal.com/blog) |

## Key Facts

- Founded by Erik Bernhardsson (ex-CTO of Better.com, former Spotify data lead) and Akshat Bubna
- Built custom infrastructure including a proprietary file system, container runtime, and scheduler
- **May 2026:** Raised **$355M Series C at $4.65-4.7B valuation** — validating the agent-native computing thesis
- Trusted by teams at Decagon, Cognition, and many AI startups for inference and fine-tuning

## Products & Technology

Modal provides a serverless compute platform with GPU access (H100, A100, etc.) for generative AI inference, LLM fine-tuning, large-scale batch jobs, and media processing. Pricing is entirely usage-based — users pay only for the time their code runs. The platform supports Python-first workflows and seamless scaling.

## Related

- [[entities/together-ai]] — competitor in GPU cloud / inference infrastructure
- [[entities/decagon]] — customer; runs real-time voice AI agents on Modal
- [[entities/cognition]] — customer; uses Modal for Devin's cloud compute workloads

## Developments (May 2026)

### $355M Series C at $4.7B Valuation

Modal raised **$355M in Series C** at a **$4.65-4.7B valuation**. The raise validates the thesis that agent-native computing is rebuilding the cloud stack for AI workloads.

## Speculative Decoding Initiative (June 2026)

In June 2026, Modal published *"Speculation Is All You Need,"* a blog post advancing the thesis that **speculative decoding is the only engine optimization that matters** for high-interactivity inference. The post positions Modal as a leader in custom speculator development.

### DFlash Speculator Release

Modal released **DFlash** (Decoding with Flash), a state-of-the-art custom domain-specific speculator architecture. DFlash, alongside MTP and EAGLE-3, represents modern speculator design that reuses the target model's hidden states and KV cache rather than running a fully independent draft model. Modal released SOTA DFlash speculators for:

- **Qwen 3.5 397B-A17B** — Modal's flagship large MoE model speculator
- **Qwen 3.5 122B-A10B** — achieving **1000+ tokens/second** at **concurrency 1** on **NVIDIA B200** GPUs

### "Speculation Is All You Need" Thesis

Modal's core argument is that speculative decoding is uniquely **"Bitter Lesson-pilled"** — its speedup compounds as models grow larger and are trained on more data, unlike kernel optimizations which deliver fixed, diminishing returns. The post claims custom domain-specific speculators deliver **2-3× speedup** (vs. 2-3% from kernel tuning alone), and that training speculators is **"ML on easy mode"** because the target model itself generates infinite free training data.

### Open-Source Ecosystem Impact

Modal argues that open-source engines **SGLang** and **vLLM** have closed the gap with proprietary inference engines, largely due to well-supported speculative decoding eliminating the latency advantage proprietary systems once held. The remaining frontier is custom speculator quality, not engine internals.

### Releases & Partnerships

- **Z Lab partnership** — Modal collaborates with Z Lab on Qwen 3.5 model speculators
- **Hugging Face releases** — DFlash speculators published as open-weight models on Hugging Face

## Sandbox Startup Latency Analysis

Modal published an in-depth analysis of sandbox startup latency (Jun 2026), defining a 5-stage lifecycle:

1. **Created**: Sandbox requested, no resources allocated yet. Asynchronous — negligible latency.
2. **Scheduled**: Assigned to a worker, provisioning CPU/memory/GPU/volumes. Depends on capacity availability speed.
3. **Started**: Container live, entrypoint running, network tunnels active. `exec(...)` becomes available. This is what most benchmarks measure.
4. **Ready**: Application-level initialization finished (git clone, npm install, server boot). This gap between Started and Ready is the largest real-world latency factor, often multiple seconds.
5. **In use**: Sandbox handling real work.

**Key insight**: application-level setup (git pull, dependency install, server startup) dominates perceived latency, not container scheduling. Shaving milliseconds off container boot has negligible impact when setup takes 30 seconds.

**Solutions**:
- **Warm Pools**: Pre-initialized sandboxes in a modal.Queue, with a background producer maintaining pool fullness. Perceived latency drops to fetch-from-pool time.
- **Directory Snapshots**: Mount per-project state into generic warm sandboxes instantly, avoiding per-user rebuilds.
- **Readiness Probes** (GA): Shell command (exit 0) or TCP port check. `sandbox.wait_until_ready()` blocks until the probe passes. Adds 'ready' event to dashboard timeline for observability alongside scheduled, started, terminated events.

This is architecturally significant for AI coding agents (background agent workflows), vibe coding platforms (user-facing server startup), and computer-use RL training (pre-warm environments for rollout throughput).

Source: raw/articles/modal.com--blog-unpacking-sandbox-startup-latency--b8f065a9.md

See also: [[concepts/speculative-decoding]], [[entities/sglang]], [[concepts/vllm]], [[concepts/agent-experience]], [[concepts/agentic-engineering]]

## Agent Experience (AX) Design Philosophy

In July 2026, Modal CTO **Akshat Bubna** articulated **Agent Experience (AX)** as Modal's core design philosophy — building infrastructure specifically for autonomous agents rather than human developers. This positions Modal as what Bubna describes as **"an example of the agent cloud future,"** a paradigm shift from human-centric cloud platforms toward agent-native computing.

### The "Agent Cloud" Thesis

Bubna argues that the current cloud stack was designed for human workflows and is fundamentally mismatched for autonomous agents. Key tenets of the AX philosophy:

- **Bursty, unpredictable workloads**: Agents generate spiky, unpredictable compute demand — unlike human-driven traffic which follows predictable patterns. Traditional cloud infrastructure (especially Kubernetes) was designed for steady-state services, not the "zero-to-thousands-of-GPUs-in-seconds" patterns agents require.
- **Agent-native infrastructure**: Modal is rebuilt from the ground up with a custom container runtime, orchestration layer, and file system — not layered on Kubernetes — to handle agent-scale compute patterns.
- **Cost model aligned with agents**: Pay-per-use with no idle costs means agents can spin up, do work, and disappear without accruing waste. This is critical for agent workflows where compute is intermittent and unpredictable.

### Why Kubernetes Wasn't Designed for Bursty AI Workloads

Bubna's critique of Kubernetes for AI workloads centers on architectural mismatch:

- **Pod startup overhead**: Kubernetes pod scheduling adds hundreds of milliseconds to startup latency, which compounds across thousands of concurrent agent sandboxes.
- **Steady-state orientation**: Kubernetes' design assumes long-running services with predictable resource profiles. AI agents need rapid scaling from zero to high concurrency and back to zero.
- **GPU scheduling limitations**: Kubernetes lacks native awareness of GPU topology, memory sharing, and the fine-grained scheduling needed for bursty AI inference.
- **Operational complexity**: Running GPU workloads on Kubernetes requires extensive custom operators (e.g., Kueue, Volcano) that add complexity without solving the fundamental burst scaling problem.

Modal's custom scheduler bypasses these limitations entirely, achieving sub-second container startup and seamless scaling to hundreds of thousands of concurrent sandboxes.

### GPU Snapshotting and Cold Start Optimization

Modal's approach to cold starts involves aggressive snapshotting techniques:

- **GPU memory snapshots**: Persist GPU state between invocations, eliminating model loading time for inference workloads.
- **Directory snapshots**: Pre-bake project dependencies and application state into warm pools, avoiding per-user rebuilds.
- **Warm pool architecture**: Pre-initialized sandboxes maintained in a `modal.Queue`, with background producers ensuring pool fullness. Perceived latency drops to fetch-from-pool time.

These optimizations are critical for AX because agents frequently create and destroy environments (sandboxes for code execution, RL rollouts, inference sessions) — the overhead of cold-starting each one would make agent economics untenable.

### RL Rollouts at 100,000 Sandbox Scale

Bubna highlighted that Modal routinely handles **100,000 concurrent sandboxes** for reinforcement learning rollouts. This scale is necessary for:

- **RL training pipelines**: Running thousands of parallel environment instances for policy evaluation
- **Computer-use agent training**: Pre-warming environments for high-throughput rollout collection
- **Massive hyperparameter sweeps**: Evaluating thousands of configurations simultaneously

Modal's architecture achieves this through its custom scheduler, which can provision and manage sandboxes at scales that would overwhelm Kubernetes-based systems.

### Modal as "Agent Cloud Future"

Bubna positions Modal as the infrastructure layer for what he calls the **"agent cloud"** — a new computing paradigm where:

1. **Agents are first-class citizens**: Infrastructure APIs are designed for programmatic consumption by agents, not just human developers
2. **Compute is ephemeral and bursty**: Resources appear instantly when needed and disappear without cost overhead when idle
3. **Scale is elastic to zero**: No baseline capacity commitment — agents scale from zero to massive concurrency and back
4. **Inference and training converge**: The same infrastructure handles both training (RL rollouts) and inference (Auto Endpoints)

This vision directly informs Modal's product decisions — from Auto Endpoints (bringing burst scalability to inference serving) to DFlash speculative decoding (minimizing latency for interactive agent experiences) to the multi-million dollar Sandbox business (providing ephemeral compute for agent code execution).

See also: [[concepts/agent-experience]], [[concepts/agentic-engineering]]

## Modal Auto Endpoints (June 2026)

Modal launched **Modal Auto Endpoints**, bringing scalability and robustness of Modal infrastructure to state-of-the-art inference performance with a single click.

### Low-Latency Playbook
Modal's approach to minimizing inference latency:
1. **Communication latency**: Modal Servers with ultra-lightweight regional proxies, global compute fleet within milliseconds of clients
2. **Host overhead**: Low-overhead inference engines (SGLang/vLLM base), profiling to remove GPU bubbles and synchronization
3. **Prefill latency**: Speed-of-light kernels (FA4 for B200/B300), grouped query attention and MoE MLP kernels
4. **Decode latency**: Speculative decoding with custom DFlash draft models — the biggest impact on end-to-end latency

### Decagon Case Study
Modal worked with **Decagon** on voice AI inference optimization:
- Baseline: ~290ms (p50) end-to-end latency
- Result: **100ms reduction** (40% of server-side decode latency)
- Beat best proprietary inference providers by **60ms**
- DFlash custom speculator trained on synthetic data (task-specific mid-training)
- Extra milliseconds enable additional tool calls, guardrails, or thinking tokens for quality

### DFlash Mid-Training Methodology
Modal's approach to training custom speculator models:
- **Generic draft models** as starting point (MTP heads from DeepSeek-style models)
- **DFlash technique** (from Z Lab): Uses KV projections from target model, parallel token generation (BERT-style), custom Triton kernel for batched projection
- **Synthetic data mid-training**: Fine-tune on task-specific synthetic data generated by target model — works well for code generation, tool-calling, structured data extraction
- **Overfitting prevention**: Track out-of-distribution performance with held-out data to predict production generalization
- Released open-source DFlash speculator for Qwen 3.5 397B-A17B, improving on MTP by 50%+

Source: raw/articles/modal.com--blog-achieve-sota-specdec--da236272.md
