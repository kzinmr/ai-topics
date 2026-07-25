# Half-Quadratic Quantization of Large Machine Learning Models

**Source:** https://dropbox.github.io/hqq_blog/ (originally https://mobiusml.github.io/hqq_blog/)
**Authors:** Hicham Badri, Appu Shaji — Mobius Labs GmbH (now part of Dropbox)
**Published:** November 3, 2023
**License:** Apache 2.0
**Code:** https://github.com/mobiusml/hqq (now https://github.com/dropbox/hqq)
**PyPI:** hqq (v0.2.8.post1 as of 2026-07)
**HuggingFace:** https://huggingface.co/mobiuslabsgmbh

---

## Summary

HQQ (Half-Quadratic Quantization) is a calibration-free (data-free) weight-only quantization method for large machine learning models. Unlike GPTQ and AWQ which require calibration data, HQQ uses half-quadratic optimization with a sparsity-promoting loss (lp norm, p<1) to find optimal quantization parameters directly from the weights. It achieves competitive quality with calibration-based methods while being dramatically faster — quantizing Llama-2-70B in under 5 minutes (>50x faster than GPTQ).

## Key Claims

1. **No calibration data needed** — works solely from model weights
2. **Extremely fast** — <5 minutes for Llama-2-70B, >50x faster than GPTQ
3. **Competitive quality** — Llama-2-70B @ 2-bit outperforms full-precision Llama-2-13B
4. **Works on any model** — LLMs, Vision Transformers, etc.
5. **Supports 8, 4, 3, 2, 1 bits** with group-wise quantization
6. **Dequantization is linear** — compatible with optimized CUDA/Triton kernels and torch.compile

## Technical Method

HQQ formulates quantization as a robust optimization problem:

```
argmin_{z,s} φ(W - Q^{-1}_{z,s}(Q_{z,s}(W)))
```

Where:
- φ() is a sparsity-promoting loss (lp norm with p<1, default p=0.7)
- z = zero-point, s = scaling factor
- Q() = quantization operator: round(W/s + z)
- Q^{-1}() = dequantization: s(W_q - z)

The non-convex problem is solved via Half-Quadratic splitting, introducing an auxiliary variable W_e, then alternating optimization:

1. **Sub-problem 1 (sp₁):** Proximal operator using generalized soft-thresholding — `shrink_lp(x, β) = sign(x)·relu(|x| - |x|^{p-1}/β)`
2. **Sub-problem 2 (sp₂):** Average over the quantization grouping axis for z

Default solver parameters: p=0.7, β=1, κ=1.01, iterations=20, with early stopping.

## Performance

### Quantization Speed
- Llama-2-70B: <5 minutes
- >50x faster than GPTQ
- Runs entirely on GPU with half-precision; CPU only for data transfer

### Quality (Llama-2 perplexity on WikiText2, 4-bit g128)
- HQQ is competitive with GPTQ and AWQ across 7B, 13B, 70B models
- Outperforms bitsandbytes (BNB) by a large margin

### Vision Models (zero-shot top-1 accuracy, 4-bit)
- ViT-B-32: HQQ beats BNB by +3.1%
- ViT-H-14 @ 3-bit: outperforms full-precision ViT-L-14 (+2.4%)
- ViT-H-14 @ 2-bit: outperforms full-precision ViT-B-32 (+5.2%)

## HQQ+ (Extension)

HQQ+ adds trainable low-rank adapters to improve quality at lower bit-widths (1-2 bits). Blog: https://dropbox.github.io/1bit_blog/

## Integration

- **HuggingFace Transformers**: Native HqqConfig support via `quantization_config`
- **vLLM**: Supported via GemLite backend for optimized serving
- **PEFT/LoRA**: Compatible with parameter-efficient fine-tuning
- **Backends**: PYTORCH, PYTORCH_COMPILE (torch.compile compatible), ATEN (CUDA, axis=0 only)
- **External backends**: GemLite (4/2/1 bit), TorchAO int4 (tiny_gemm)

## Axis Parameter

- `axis=0`: Better quality, especially at low bits. NOT supported for fast inference.
- `axis=1`: Slightly lower quality but supports optimized fused kernels. Recommended for deployment.

## Citation

```bibtex
@misc{badri2023hqq,
  title  = {Half-Quadratic Quantization of Large Machine Learning Models},
  url    = {https://dropbox.github.io/hqq_blog/},
  author = {Hicham Badri and Appu Shaji},
  month  = {November},
  year   = {2023}
}
```

## Related Quantized Models (HuggingFace)

- Llama-2-7b-hf-4bit_g64-HQQ
- Llama-2-13b-hf-4bit_g64-HQQ
- Llama-2-70b-hf-2bit_g16_s128-HQQ
- Mixtral (2,3)-bit HQQ quantized models
- ViT HQQ quantized models
