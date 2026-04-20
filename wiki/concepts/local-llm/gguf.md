---
status: skeleton
created: 2026-04-14
tags: local-llm, quantization, format
---

# GGUF (GPT-Generated Unified Format)

GGUF is the quantization format used by llama.cpp for efficient CPU/Apple Silicon inference.

## Key Points

- Successor to GGML format (introduced 2023)
- Supports multiple quantization types: Q4_0, Q4_K_M, Q5_K_M, Q8_0, etc.
- Metadata stored within the file (model name, architecture, tokenizer info)
- Enables running large models on consumer hardware with minimal VRAM
- Maintained as part of the llama.cpp ecosystem

## Quantization Levels

| Type | Bits | Quality | Use Case |
|------|------|---------|----------|
| Q4_0 | ~4.0 | Good | Balance of speed/quality |
| Q4_K_M | ~4.5 | Very Good | Recommended default |
| Q5_K_M | ~5.5 | Excellent | High quality on limited hardware |
| Q8_0 | ~8.0 | Near-lossless | Maximum quality |
| IQ2_XXS | ~2.0 | Acceptable | Extreme hardware constraints |

## Related wikilinks

- [[local-llm/llama-cpp]] — Primary consumer of GGUF files
- [[local-llm]] — Local LLM overview
- [[georgi-gerganov]] — Format creator

## Sources

- llama.cpp GitHub repository
- GGUF format specification
