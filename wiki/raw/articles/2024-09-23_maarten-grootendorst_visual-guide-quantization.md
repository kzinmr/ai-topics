# A Visual Guide to Quantization — Maarten Grootendorst

**Source:** https://www.maartengrootendorst.com/blog/quantization/
**Date:** 2024-09-23
**Author:** Maarten Grootendorst

## Summary

A comprehensive visual guide covering the fundamentals of LLM quantization: IEEE-754 representation (sign, exponent, fraction), symmetric vs asymmetric mapping (Absmax, Zero-point), clipping and calibration, PTQ (GPTQ, GGUF) vs QAT, and the 1-bit/1.58-bit frontier (BitNet, BitNet b1.58).

## Key Concepts

- IEEE-754: Sign + Exponent (range) + Fraction (precision)
- Symmetric (Absmax): s = 127/α, centered at zero
- Asymmetric (Zero-point): s = (max-min)/(255), requires shift z
- Clipping: manual range capping to reduce error for majority values
- Calibration: MSE, Percentile, or KL-divergence for optimal range
- PTQ: post-training quantization (GPTQ: Hessian-based error redistribution; GGUF: block-wise with CPU offloading)
- QAT: fake quants during training → wide minima in loss landscape
- BitNet (1-bit): weights ∈ {-1, 1}, signum function, activations INT8
- BitNet b1.58 (ternary): weights ∈ {-1, 0, 1}, absmean quantization, addition-only matmul

## Takeaways

- GPU-only → GPTQ/EXL2
- Limited VRAM → GGUF with CPU offloading
- Best accuracy at low bit-widths → QAT
- Future: 1.58-bit ternary replacing multiplications with additions
