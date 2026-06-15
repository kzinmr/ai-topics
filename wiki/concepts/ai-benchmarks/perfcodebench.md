---
title: "PerfCodeBench"
type: concept
created: 2026-06-15
updated: 2026-06-15
tags:
  - benchmark
  - code-model
  - performance-engineering
  - evaluation
  - software-engineering
aliases:
  - perfcodebench
status: active
sources:
  - https://arxiv.org/abs/2605.15222
related_concepts:
  - concepts/ai-benchmarks/swe-bench
  - concepts/ai-benchmarks/livecodebench
  - concepts/ai-benchmarks/kernelbench
---

# PerfCodeBench

**PerfCodeBench** is an executable benchmark for evaluating LLMs on **system-level high-performance code optimization**. Introduced in May 2026 by Huihao Jing, Wenbin Hu, Haochen Shi, Hanyu Yang, Sirui Zhang, Shaojin Chen, Haoran Li, and Yangqiu Song from HKUST, NYU, SWUPL, and MODEIO.AI, it addresses a critical gap in LLM code evaluation: the ability to produce not just correct but **efficient** implementations for performance-critical systems tasks.

**Paper**: [arXiv:2605.15222](https://arxiv.org/abs/2605.15222) | **Benchmark**: [anonymous.4open.science/r/perfcodebench-7CDE](https://anonymous.4open.science/r/perfcodebench-7CDE)

## What It Measures

- **Domain**: System-level high-performance code optimization across CPU, GPU, and parallel computing
- **Task type**: Performance-oriented code generation with correctness and efficiency evaluation
- **Key insight**: Existing benchmarks (SWE-bench, LiveCodeBench, BigCodeBench, EffiBench) focus on correctness or algorithmic efficiency, but real performance depends on cache locality, data movement, parallel execution, synchronization cost, and hardware utilization
- **Coverage**: GPU programming (CUDA), CPU/cache optimization, parallel computing, data processing, AI inference systems
- **Languages**: C (8.74%), C++ (58.63%), Go (8.63%), Java (9.49%), Python (7.77%), CUDA (6.74%)

## Benchmark Construction

### Data Collection

Tasks are sourced from public repositories, benchmark suites, and systems-oriented artifacts (full source list in Appendix A of the paper). Candidate tasks undergo filtering:
1. Compilation and execution check
2. Automatic correctness test availability
3. Reference implementation must be faster than baseline
4. Runtime measurement stability

### Task Structure

Each benchmark instance includes:
- **Baseline implementation**: Correct but slower code
- **Reference optimized solution**: Human-expert optimized code
- **Executable correctness harness**: Deterministic test harness for correctness and performance evaluation
- **Adaptive per-task timeouts**: Based on baseline profiling with fixed lower/upper bounds

### Scalable Evaluation Pipeline

- **Caching and reuse**: Reduces redundant computation
- **Split-pool scheduling**: Handles long-tail task runtimes efficiently

## Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **CRR** (Correct-and-Runnable Rate) | Fraction of tasks where model produces correct, runnable code |
| **FBR** (Faster-than-Baseline Rate) | Fraction of tasks where model code is faster than baseline |
| **RBR** (Reference-Benchmark Rate) | Fraction of tasks where model matches or exceeds reference implementation |
| **CGRE** (Correctness-Gated Relative Efficiency) | Efficiency score conditional on correctness |
| **CGRE≥0.8** | Fraction of tasks closing ≥80% of baseline-to-reference performance gap |

## Key Evaluation Results

### Main Findings (20 LLMs evaluated)

**Proprietary LLMs**:
- **GPT-5.4**: Best CRR (71.25%) and FBR (66.72%) — most reliable at producing runnable speedups
- **GPT-5**: Best RBR (61.60%), CGRE (73.99%), and CGRE≥0.8 (72.91%) — best at reference-level efficiency
- **Claude Opus 4.5**: Strong CRR (70.55%) and FBR (65.75%), but weaker on RBR (43.23%)
- **Gemini 3.1 Pro**: Low CRR (25.57%) but decent RBR and CGRE when correct

**Open-source LLMs**:
- **DeepSeek-V4-Pro**: Best balanced open-source — 54.48% CRR, 64.30% CGRE
- **Qwen3.6-Max**: Strong CGRE (66.32%) but only 47.25% CRR
- **Kimi K2.6**: Very low CRR (3.94%) but high RBR (52.13%) when successful

### Three Critical Patterns

1. **Benchmark not saturated**: Large gap between best and worst models on every metric
2. **Correctness ≠ Efficiency**: Models can produce runnable code but miss reference speed
3. **Reliability ≠ Conditional strength**: Some models fail often but successful outputs are strong

### CPU vs. GPU Performance Gap

| Model | CPU CRR | GPU CRR | CPU CGRE | GPU CGRE |
|-------|---------|---------|----------|----------|
| GPT-5.4 | 82.06% | 2.40% | 68.67% | 0.00% |
| GPT-5 | 71.02% | 9.60% | 64.74% | 6.70% |
| Claude Opus 4.5 | 79.68% | 12.00% | 69.47% | 10.26% |
| DeepSeek-V4-Pro | 62.04% | 18.40% | 57.18% | 11.99% |

**Key insight**: GPU optimization is a distinct regime. CPU success does not transfer to CUDA, where models must handle parallel decomposition, launch structure, synchronization, and memory hierarchy.

### Language-Level Split

- **C++**: Easiest large subset (avg CRR 74.73%, CGRE 69.20%)
- **Python**: Highest average CRR (85.53%) but moderate CGRE
- **Go/Java**: Relatively tractable
- **C**: Noticeably harder than higher-level CPU languages
- **CUDA**: Most difficult by far (avg CRR 10.53%, CGRE 6.97%)

## Significance

PerfCodeBench establishes that:
- **Performance-aware evaluation is needed**: LLMs should move beyond generating merely correct code toward producing efficient systems software
- **Multi-metric evaluation is essential**: CRR alone or CGRE alone is insufficient
- **Cross-language robustness is lacking**: Models show weaknesses in consistently reaching expert-level efficiency across different languages
- **GPU programming remains extremely challenging**: Current models are far from solving CUDA optimization tasks

## Related Benchmarks

- [[concepts/ai-benchmarks/swe-bench]] — Real-world GitHub issue resolution (correctness-focused)
- [[concepts/ai-benchmarks/livecodebench]] — Contest-style code evaluation (algorithmic reasoning)
- [[concepts/ai-benchmarks/kernelbench]] — Kernel-level optimization benchmark
- [[concepts/ai-benchmarks/programbench]] — Program-level evaluation
- EffiBench — Efficiency evaluation for generated code (algorithmic efficiency focus)
- EffiBench-X — Cross-language efficiency benchmark

## Source

Primary source: [arXiv:2605.15222](https://arxiv.org/abs/2605.15222) (May 13, 2026)
