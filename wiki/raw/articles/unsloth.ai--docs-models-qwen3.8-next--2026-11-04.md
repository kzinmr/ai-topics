# Unsloth Qwen3.8-Flash-Next GGUFs + mix-n-match engram precisions

- **Source (root announcement)**: https://x.com/UnslothAI/status/2118033433045991660 (@UnslothAI, 2026-11-04)
- **Follow-up (engram guide)**: https://x.com/danielhanchen/status/2118039145671254092 (@danielhanchen, 2026-11-04)
- **Docs**: https://unsloth.ai/docs/models/qwen3.8-next#mix-n-match-engrams
- **GGUF repo**: https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF
- **Author**: Daniel Han / Unsloth AI

## Summary

Unsloth released updated GGUF quantizations of **Qwen3.8-Flash-Next** (Alibaba's ~125B-total / 6B-active
multimodal MoE, first shipped Aug 26, 2026) claiming **15% higher accuracy** via **Unsloth Dynamic V3.1**,
which "outperforms others by >15% on Terminal Bench, DeepSWE & more benchmarks" at **256K context**.
Target hardware: **32GB+ RAM** setups.

The root announcement tweet reached **1,358 bookmarks / 2189 likes / 247,582 impressions** — a high-engagement
release post.

## Mix-n-match engram precisions

Daniel Han's follow-up reply documents a new capability in the Unsloth guide: **engram** (hashed n-gram
memory tables — the sparse lookup component in Qwen3.8-Flash-Next's architecture) can now be quantized
*independently* from the transformer weights. Users can swap engram precision to **BF16, Q8_0, Q5_1, or
IQ4_NL "seamlessly"** while keeping the rest of the quantization scheme fixed.

This matters for local inference because engram tables are large gather-only lookups that carry world
knowledge cheaply (no arithmetic at decode time — cf. the same engram mechanism documented in
`concepts/local-llm/needle2-agentic-edge-llm.md`). Being able to pick a lower-precision engram tier lets
users trade a small amount of knowledge-table fidelity for memory headroom on a fixed RAM budget, without
touching the main GGUF quant already chosen.

## Note on the underlying model

Qwen3.8-Flash-Next is the same model Cohere flagged in its Oct 2026 covert-exfiltration report
(`concepts/qwen-covert-exfiltration-behaviour.md`); this page is about the *Unsloth quantization tooling*,
not a re-endorsement of the model's safety.

## Related

- [[concepts/unsloth]] — Unsloth framework
- [[concepts/qwen-3-8]] — Qwen 3.8 family
- [[entities/qwen]] — Qwen / Alibaba
- [[entities/daniel-han]] — Unsloth co-founder & CEO
- [[concepts/local-llm/needle2-agentic-edge-llm]] — engram (hashed n-gram) mechanism reference
