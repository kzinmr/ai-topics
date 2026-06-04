# CPU Offloading in Distributed Training — Knowledge Bank

This reference captures knowledge from multiple ingested sources (Justine Tunney CPU matmul, Answer.AI FSDP+Q-LoRA benchmarks, Phil Schmid guide) about CPU offloading in the context of FSDP/DeepSpeed distributed training.

## Key Concept

CPU offloading in distributed training moves model parameters, gradients, and/or optimizer states from GPU VRAM to CPU RAM when VRAM is insufficient. This enables training large models (e.g., 70B) on consumer GPUs (24GB) that would otherwise be impossible.

## Tradeoff: Memory vs Speed

| Offloading Level | Memory Saved | Speed Impact | Use Case |
|:----------------|:-------------|:-------------|:---------|
| Optimizer states only (ZeRO-1) | ~8P/N bytes | Minimal | Mild VRAM pressure |
| + Gradients (ZeRO-2) | ~10P/N bytes | Small | Standard multi-GPU |
| + Parameters (ZeRO-3) | ~14P/N bytes | Significant | Model exceeds single GPU |
| CPU Offload | Unlimited (by CPU RAM) | 2-3x slower | Extreme constraint |
| NVMe Offload (DeepSpeed) | Unlimited (by disk) | 10x+ slower | Trillion-parameter class |

## CPU Offloading Performance Paradox (Answer.AI)

On memory-constrained hardware (e.g., dual 3090, 24GB each), enabling CPU offloading can **increase** training speed because it allows significantly larger batch sizes. The PCIe transfer overhead is offset by higher GPU utilization from more samples per step.

## CPU Matmul Performance Impact (Justine Tunney)

CPU matrix multiplication performance directly affects offloading viability:

- **Faster CPU matmul → less offloading penalty**: When offloaded parameters require CPU computation before being sent back to GPU (e.g., gradient computation on CPU), faster CPU kernels reduce the bottleneck.
- **Tunney's 84 kernels**: 30-500% faster CPU matmul, up to 2x Intel MKL for L2-cache fits. This improvement reduces the speed penalty of CPU-offloaded training.
- **Implication**: As CPU inference matmul continues to improve (ARM SVE, AVX-1024, custom kernels), the cost of CPU offloading during training decreases, making consumer-GPU training of 70B+ models more practical.

## FSDP Implementation

- All-or-nothing: params, gradients, optimizer all offloaded or none
- Controlled via `CPUOffload(offload_params=True)` in FSDP constructor
- Environment variable: `FSDP_CPU_RAM_EFFICIENT_LOADING=1`
- 70B model: ~140GB CPU RAM needed for parameter offloading

## DeepSpeed Implementation

- Granular: can offload optimizer separately from params
- Supports NVMe offload (beyond CPU RAM)
- ZeRO-Infinity extends to all storage tiers

## Practical Recommendations

1. Start without offloading (DDP or ZeRO-2)
2. Enable only when model doesn't fit
3. If offloading enables batch_size 2x or larger, it's a net win (Answer.AI finding)
4. Monitor CPU RAM: 70B training can saturate 128GB; swapfile may be needed
5. CPU matmul performance matters — use optimized kernels (llamafile, MKL, BLIS)
