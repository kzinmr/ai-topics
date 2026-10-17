---
source_url: https://research.meta.ai/blog/muse-spark-open
ingested: 2026-10-17
sha256: 91191ba85833e211a3395b9cb937b6f5c7745d40fbcb0bb246420f3ceddef151
---

# Introducing Muse Spark Open, The Most Capable US Open-Weight Model to Date

October 15, 2026 · Meta Superintelligence Labs (research.meta.ai)

Muse Spark Open is available today and brings leading agentic capabilities to your desktop for the first time on Apple M5 Ultra Mac Studios.

Today, we're releasing the weights for Muse Spark Open, the most capable US open-weight model to date. Muse Spark Open is a natively multimodal model with 816B total parameters (42B active) and a 1M-token context window. Built for coding and agentic work, it excels at long-horizon tasks, complex software engineering, and multi-step reasoning.

We believe the future is for everyone, and that includes the freedom to run advanced models wherever, including at home. Muse Spark Open is the first model in its class to run on your desktop using two Apple M5 Ultra Mac Studios with the latest MLX framework.

Muse Spark Open is available today through API platforms at Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter and Together AI. Model weights are available for download on Amazon SageMaker AI, Google Cloud Model Garden, Hugging Face, and Microsoft Foundry Models.

It runs on leading inference engines like SGLang, vLLM, TensorRT-LLM, Hugging Face Transformers, Apple MLX, llama.cpp, and Unsloth with optimizations for AMD, Apple, Intel, and NVIDIA silicon. Developers can easily further customize the model using the PyTorch framework.

## Optimized for Apple Silicon

Leveraging the latest version of MLX, Muse Spark Open was optimized to run on Mac Studio with M5 Ultra, and together they're the best way to run a powerful model on your own desktop.

Apple's unified memory architecture lets the M5 Ultra's integrated GPU use up to 512 GB per Mac Studio, so two machines can hold an entire model. And the chip's 1.2 TB/s of memory bandwidth is fast enough to read the small slice each token needs. The result is two Mac Studios behave like one supercomputer with a terabyte of unified memory.

We tested a range of agentic workflows running entirely on-device, using Muse Code powered by Muse Spark Open, including shipping real iOS changes to Ice Cubes (an open-source Mastodon client) — bug fixes, new features, full build — and driving DaVinci Resolve end to end, with the model reviewing footage frame by frame to find the strongest moments and crop them vertically.

## Available Now

The open-weight version of Muse Spark ships with custom, auto-tunable Helion GPU kernels in SGLang, delivering 1.03-3.95x kernel-level speedups on NVIDIA and AMD GPUs, and a 3% end-to-end speedup on AMD MI350.

## Safety and Preparedness

Releasing open-weight models is part of how we bring the benefits of personal superintelligence to everyone, and part of how safety work advances across the field. Open weights also carry their own considerations, and Muse Spark Open has additional safety post-training for that reason. The results demonstrate strong safeguards across risk categories measured.

We evaluated the model in line with our Meta Superintelligence Scaling Framework, covering the most severe risks, and it met the thresholds our framework requires for release. Detailed results are in the Muse Spark Open model card, with a full evaluation report available soon.

## License

We're releasing the weights under the Muse Model License with limited commercial terms, which allow many developers to use the model for free.

## Get Started

Customize via PyTorch's TorchTitan. To run on Apple silicon, use MLX, which pulls weights from Hugging Face.
Weights: https://huggingface.co/collections/meta-models/muse-spark-open
Hosted Inference Partners: Together AI, Fireworks, Baseten, Modal, Groq, Nebius, and OpenRouter.
