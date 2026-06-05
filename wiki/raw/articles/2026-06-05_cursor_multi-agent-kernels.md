---
title: "Speeding up GPU kernels by 38% with a multi-agent system · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/multi-agent-kernels"
scraped: "2026-06-05T06:00:42.259152+00:00"
lastmod: "2026-06-05T05:23:59.758Z"
type: "sitemap"
---

# Speeding up GPU kernels by 38% with a multi-agent system · Cursor

**Source**: [https://cursor.com/blog/multi-agent-kernels](https://cursor.com/blog/multi-agent-kernels)

Blog
/
research
Apr 14, 2026
·
research
Speeding up GPU kernels by 38% with a multi-agent system
Our multi-agent system autonomously optimized 235 CUDA kernels for NVIDIA Blackwell 200 GPUs, achieving a 38% geomean speedup over baselines in just 3 weeks.
Wilson Lin – Cursor; Sahil Modi, Yuan Zhang & Edward Lin – NVIDIA
·
10 min read
Table of Contents
↑
Kernel optimization as a test of agent system capabilities
SOL-ExecBench for problem generation and benchmarking
How we ran the experiment
38% speedup, with 19% of optimizations exceeding 2x improvements
Different optimization strategies for different problems
BF16 Grouped Query Attention with Paged Prefill
NVFP4 MoE Linear with Gating
BF16 Matrix Multiplication
A multi-agent system for building software
Over the past few months, we've been developing a multi-agent system that can build, maintain, and deploy complex software autonomously. As part of that work, we've been testing the system in a variety of domains, including having it
build a browser from scratch
and solve a research-level math problem on the
First Proof benchmark
.
Recently, we began collaborating with NVIDIA on a new challenge: applying the multi-agent harness to optimize CUDA kernels. These are difficult technical problems with important real-world consequences: CUDA kernels are the core software that supports AI model training and inference on NVIDIA GPUs. Faster kernels mean better GPU utilization, reduced energy consumption, lower latency, and reduced cost per token—allowing providers to serve bigger, more capable models to more users at once.
Our multi-agent harness operated autonomously for three weeks across 235 problems. The system achieved a 38% geomean speedup by building and optimizing Blackwell GPU kernels from scratch, all the way down to the assembly level.
These levels of performance improvement are typically only found through months or years of work from highly experienced kernel engineers. The multi-agent system accomplished it in weeks, addressing a long-tail of kernel problems that had been impractical with existing approaches.
#
Kernel optimization as a test of agent system capabilities
One of the best ways to evaluate long-running, multi-agent systems is to give them open-ended optimization problems where even we don't know the right answer. Kernel optimization problems meet this criteria: they provide measurable objectives that the system can iteratively optimize against, instead of targeting a simple known diff.
Today, engineers optimize kernels by breaking models into individual math operations and tuning each one separately. This makes the problem manageable but leaves performance on the table because piecemeal optimization misses potential gains from optimizing across the entire system simultaneously. To date, GPU performance has been limited by our inability to explore the full solution space beyond these manual simplifications.
With this experiment, we wanted to see if our multi-agent system could operate outside these constraints, exploring a broader solution space to produce faster kernels.
#
SOL-ExecBench for problem generation and benchmarking
NVIDIA used SOL-ExecBench to generate 235 optimization problems from over 124 production open-source models such as Deepseek, Qwen, Gemma, Kimi, and Stable Diffusion. As opposed to synthetic data or toy kernels, each problem is a real-world constraint on training or inference workloads for a variety of model architectures: LLMs, diffusion, vision, audio, video, and multi-modal hybrids.
We also used SOL-ExecBench to benchmark multi-agent kernel solutions on 27 NVIDIA Blackwell 200 GPUs. SOL-ExecBench is an effective evaluator that compares kernel performance against existing software baselines and theoretical hardware performance limits. If agents use cheating tactics like caching and deliver performance beyond what a B200 can support, the pipeline invalidates the result.
#
How we ran the experiment
The multi-agent system solved all 235 GPU kernel optimization problems in a single run by deploying a planner agent that distributed and rebalanced work across autonomous workers based on performance metrics.
The entire coordination protocol lived in a single markdown file that specified the output format, rules, and tests. The multi-agent system independently learned to call the benchmarking pipeline during its runs, creating a loop where the system continuously tested, debugged, and optimized kernels without any developer intervention.
In order to better gauge the multi-agent system's capabilities, we asked it to write its solutions in two languages in two separated runs, at opposite ends of the GPU abstraction spectrum:
CUDA C with inline PTX
, which gives agents direct access to registers and ISA-level instruction, testing whether the system can reason about hardware at the lowest level.
CuTe DSL
, which provides high-level composable abstractions with minimal presence in public training data, testing whether the system can learn novel APIs purely from provided documentation.
#
38% speedup, with 19% of optimizations exceeding 2x improvements
We report performance of the multi-agent system in two ways:
Geomean speedup
vs. PyTorch code that was optimized by a single agent as a baseline.
Speed-of-Light (SOL) scores
that represent how good a solution is compared to theoretical hardware limits on a logarithmic curve. A score of 0.5 represents the optimized PyTorch baseline and 1.0 is the performance limit.
Our multi-agent system successfully outperformed baselines on 149 out of 235 problems (63%), with a geometric mean ratio of 1.38x (38% geomean speedup).
On 45 out of 235 problems (19%), the multi-agent system delivered optimizations greater than 2x compared to baselines. You can see the final solutions our system developed in this
public repo
.
#
Different optimization strategies for different problems
To show the adaptability of the system across different types of problems, we highlight three problems where it organically arrived at distinct optimization strategies.
#
BF16 Grouped Query Attention with Paged Prefill
Grouped-query attention with paged prefill is a common prompt-stage operation in modern LLM inference stacks. A well-optimized implementation can support longer contexts, higher concurrency, and better throughput on the same GPU VRAM.
The agent used CUDA C++ to optimize this attention problem extracted from SGLang inference for Llama 3.1 8B. As the agent iterated on the kernel, it successfully employed specific hardware instructions for memory loading and math, added improved scheduling via persistent kernels, and hyper-optimized for input size.
We compared the multi-agent system's custom kernel with a human optimized baseline in the FlashInfer library. We found that the system produced a solution approaching hardware limits with a SOL score of 0.9722, representing a 84% geomean speedup over the baseline.
We also replaced the existing kernel in SGLang and observed a 3% speedup for time to first token (TTFT) on Llama 3.1 8B. Given that this attention problem occupies 2-5% of the prefill process depending on serving configuration, we see this as a non-trivial end-to-end speedup.
#
NVFP4 MoE Linear with Gating
This problem represents a common two-kernel pattern found in Mixture-of-Experts models like Qwen3, with the caveat that the input tensor and intermediate multiplication output are quantized to NVFP4 (4-bit floating point).
The agent correctly identified the quantization area as the primary bottleneck and accordingly fused scale calculation and rounding. Instead of scaling and then rounding during quantization, it used pre-computed threshold buckets to directly map FP32 values to FP4 codes, which is possible because there are only 16 possible NVFP4 values. Next, it applied these optimizations to larger test cases.
The agent ultimately surpassed the optimized PyTorch baseline, delivering a 39% geomean speedup and 0.58 SOL score.
#
BF16 Matrix Multiplication
Matrix multiplication is a notoriously difficult problem to optimize because it requires deep understanding of the various hardware units and their scheduling. Fully performant matrix multiplication kernels (GEMMs) require inline PTX (akin to assembly language), pipelining, and staging within a kernel. As a result, writing fast GEMMs has been historically siloed to highly experienced kernel experts.
The Cursor multi-agent system generated a specialized CUDA C++ GEMM kernel from scratch, coming remarkably close (86%) to a meticulously tuned human baseline from the NVIDIA cuBLAS library. The system reached this result by independently learning to use Blackwell-specific instructions, optimizing memory reads and writes for the hardware, and then hyperoptimizing for the exact shapes.
And on small-M test cases, which are especially important for LLM inference decode, the multi-agent system kernel outperformed the library by up to 9%. This result points to multi-agent systems soon outperforming domain experts even on the hardest kernel problems.
#
A multi-agent system for building software
While the multi-agent harness delivered a 38% geomean speedup over baselines, the median SOL score was still only 0.56, leaving significant room for further optimization. We believe that multi-agent solutions can be vastly improved with more compute, as we had hundreds of problems and agents running on only 27 GPUs. This limited our ability to take full advantage of the multi-agent system. With more GPUs, the system could explore even deeper and more novel solutions.
The most ambitious tasks in software are open-ended, without a clear solution. Single agent systems struggle here because models are best at narrowly scoped tasks they have already seen during training. We see the kernel optimization experiment as further validation that multi-agent architectures will quickly become the default approach to building software because they can tackle novel problems that fall far outside training data distribution.
The techniques we're researching here will soon inform Cursor's core product. If you're interested in working on hard problems in multi-agent coordination, the Cursor team would love to hear from you at
hiring@cursor.com
.
Filed under:
research
Author
s
:
Wilson Lin, Sahil Modi, Yuan Zhang & Edward Lin
