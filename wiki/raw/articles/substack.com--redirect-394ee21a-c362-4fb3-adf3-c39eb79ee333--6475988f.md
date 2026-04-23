---
title: "TPU 8t and TPU 8i technical deep dive"
url: "https://substack.com/redirect/394ee21a-c362-4fb3-adf3-c39eb79ee333?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-23T05:08:38.266094+00:00
source_date: 2026-04-23
tags: [newsletter, auto-ingested]
---

# TPU 8t and TPU 8i technical deep dive

Source: https://substack.com/redirect/394ee21a-c362-4fb3-adf3-c39eb79ee333?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

At Google, our TPU design philosophy has always been centered on three pillars: scalability, reliability, and efficiency. As AI models evolve from dense large language models (LLMs) to massive Mixture-of-Experts (MoEs) and reasoning-heavy architectures, the hardware must do more than just add floating point operations per second (FLOPS); it must evolve to meet the specific operational intensities of the latest workloads.
The rise of agentic AI requires infrastructure that can handle long context windows and complex sequential logic. At the same time, world models have emerged as a necessary evolution from current next-sequence-of-data architectures, which means newer agents are simulating future scenarios, anticipating consequences, and learning through "imagination" rather than risky trial-and-error. The eighth-generation TPUs (TPU 8t and TPU 8i) are our answer to these challenges, ensuring that every workload, from the first token of training to the final step of a multi-turn reasoning chain, is running on the most efficient path possible. They are built to efficiently train and serve world models like Google DeepMind’s Genie 3, enabling millions of agents to practice and refine their reasoning in diverse simulated environments.
TPU 8: Specialized by design
Recognizing that the infrastructure requirements for pre-training, post-training, and real-time serving have diverged, our eighth-generation TPUs introduce two distinct systems: TPU 8t and TPU 8i. These new systems are key components of Google Cloud's AI Hypercomputer, an integrated supercomputing architecture that combines hardware, software, and networking to power the full AI lifecycle. While both systems share the core DNA of Google’s AI stack and support the full AI lifecycle, each is built to address distinct bottlenecks and optimize efficiency for critical stages of development. Additionally, by integrating Arm-based Axion CPU headers across our eighth-generation TPU system, we’ve removed the host bottleneck caused by data preparation latency. Axion provides the compute headroom to handle complex data preprocessing and orchestration, so that TPUs stay fed and don’t stall.
TPU 8t: The pre-training powerhouse
Optimized for massive-scale pre-training and embedding-heavy workloads, TPU 8t utilizes our proven 3D torus network topology at an even larger scale of 9,600 chips in a single superpod. TPU 8t is designed for maximum throughput across hundreds of superpods, ensuring that training runs stay on schedule.
Here are some key advancements of TPU 8t over prior-generation TPUs:
The SparseCore advantage
: Central to TPU 8t is the SparseCore, a specialized accelerator designed to handle the irregular memory access patterns of embedding lookups. While the Matrix Multiply Unit (MXU) handles matrix math, the SparseCore offloads data-dependent all-gather operations, amongst other collectives, preventing the zero-op bottlenecks that often plague general-purpose chips.
VPU/MXU overlap and balanced scaling
: TPU 8t is designed to maximize provisioned FLOPs utilization. By implementing more balanced Vector Processing Unit (VPU) scaling, the architecture minimizes exposed vector operation time. This allows for better overlapping of quantization, softmax, and layernorms with the matrix multiplications in the MXU, helping the chip stay busy rather than waiting on sequential vector tasks.
Native FP4
:
TPU 8t introduces native 4-bit floating point (FP4) to overcome memory bandwidth bottlenecks, doubling MXU throughput while maintaining accuracy for large models even at lower-precision quantization. By reducing the bits per parameter, the platform minimizes energy-intensive data movement and allows larger model layers to fit within local hardware buffers for peak compute utilization.
