# LLM.int8() and Emergent Features — Tim Dettmers

**Source:** https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/
**Date:** 2022-08-17
**Author:** Tim Dettmers

## Summary

Dettmers' LLM.int8() enables zero-degradation 8-bit inference for 175B+ parameter models by using mixed precision decomposition — separating outlier feature dimensions into FP16 while quantizing the remaining 99.9% of values into Int8. The paper also discovers a "phase shift" at 6.7B parameters where emergent outlier features coordinate across all layers.

## Key Concepts

- Vector-wise quantization (per-row/per-column scaling)
- Mixed precision decomposition (outliers → FP16, rest → Int8)
- 6.7B parameter phase shift threshold
- Emergent outlier features (systematic, large magnitude -60 to -95)
- Two streams theory (input explanation + feature removal)
- Phase shift follows perplexity (exponential), not just parameter count
- Post-phase-shift: sparse attention, dense FFNs, less prunable

## Implications

- Research on <6.7B models may not generalize to larger models
- Extrapolate via perplexity curves, not parameter counts
- Int8 is the only widely supported hardware data type for this optimization
