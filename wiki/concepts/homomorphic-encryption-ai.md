---
title: Homomorphic Encryption for AI (Private LLM Inference)
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [concept, security, cryptography, llm-inference, privacy, homomorphic-encryption, privacy-preserving-ml, ckks]
sources: [raw/articles/2026-08-19_google_heir-private-ai-homomorphic-encryption.md, raw/papers/2026-01_2601.18511_scaling-fhe-llm-inference-llama3-8b.md, raw/articles/2026-08-19_github_google_heir-readme.md]
---

# Homomorphic Encryption for AI (Private LLM Inference)

**Homomorphic encryption (FHE)** lets a server compute directly on encrypted data and return encrypted results — the plaintext never exists on the server. Applied to AI, it enables **non-interactive confidential LLM inference**: the model provider never sees the prompt (or any intermediate activation), and the client needs only the decryption key. Google called it out in Aug 2026 as the tool that "fundamentally alters" the capability/privacy trade-off, with the overhead now "a question of cost" that is "rapidly decreasing."

## How it works (intuition)

- Ciphertexts support a restricted algebra: addition and multiplication homomorphically; **bootstrapping** refreshes noise to allow unbounded depth
- Real LLM inference needs **non-linear layers** (SoftMax, ReLU/GELU, RoPE rotations). Under FHE these are evaluated with **polynomial approximations**, whose cost explodes with activation outliers — the central optimization target of current research
- Dominant schemes: **CKKS** (approximate, SIMD — good for vectors/matrices) and **TFHE** (bootstrapping-friendly, binary-friendly)

## State of the art (Aug 2026)

| Work | Model | Setup | Result |
|---|---|---|---|
| **arXiv:2601.18511** (Park et al., KAIST/EPFL, Jan 2026) | Llama-3-8B | 8× RTX PRO 6000, CKKS, 128 encrypted tokens | 20 s summarization; **18 s/token generation** (prior SOTA: 295 s on H100-class) |
| Same paper, heterogeneous mode | Llama-3-8B | 4096-token prompt, last 128 encrypted | 64 s summarization; 22 s/token |
| Google HEIR demos (Aug 2026) | LLM + search + recs + medical | single-threaded CPU (per blog; per-app numbers in the post's demos) | first credible "private LLM inference on CPU" marketing |

Key techniques from 2601.18511:
- **Outlier mitigation**: token prepending + orthogonal rotations to tame polynomial-approximation cost of non-linear layers
- **Sparse-ciphertext polynomial evaluation** for faster homomorphic SoftMax
- **Shallow homomorphic attention circuit** with minimal bootstraps; a new **plaintext-ciphertext** homomorphic linear-algebra algorithm enables "only the last N tokens are encrypted" (privacy for the sensitive tail, plaintext for context)

## Engineering stack

- **Compiler**: [[entities/heir]] (Google, MLIR-based; OpenFHE & Lattigo backends; 4 peer-reviewed papers built on it by Aug 2026)
- **Libraries**: OpenFHE, Lattigo, SEAL, Concrete (community)
- **Hardware accelerators** (partnered with Google per 2026 blog): Belfort, Niobium, Cornami, Optalysys
- **Hybrid TEE+FHE**: Bifrost (arXiv:2606.17421)
- **Private RAG**: GoldenRetriever (arXiv:2607.29019) — non-interactive FHE retrieval
- **KV cache under FHE**: Cachemir (arXiv:2602.11470)
- **RL-optimized FHE plans**: CHEHAB RL (arXiv:2601.19367)

## Limitations & open questions

1. **Latency vs interactive use** — 18–22 s/token is ~1000× slower than plaintext inference; suitable for batch / compliance workloads, not chat
2. **Bootstrapping bottleneck** — depth of a transformer (layers × attention heads × non-linears) is still the hard part; "shallow circuits" + hybrid plaintext/ciphertext regimes are the current escape hatches
3. **Memory bandwidth** — ciphertexts are large (SIMD packing, multi-key); CPU/GPU DRAM, not FLOPs, is usually the real bottleneck
4. **Trust model** — FHE's "no trusted hardware" is a selling point *and* a cost driver; teams often pair it with a TEE for the non-sensitive prefix (hybrid designs)
5. **Standardization** — no consensus "private inference API" yet; HEIR's MLIR approach is a candidate, but Lattigo/OpenFHE ecosystem splits remain

## Comparison with alternatives

| Approach | Security | Latency | Model IP safe? | Notes |
|---|---|---|---|---|
| Plaintext cloud | none | baseline | no | default |
| On-device / edge | strong | device-bound | no (model ships) | iPhone-class only for small models |
| TEE / enclave | strong (trust in silicon) | ~plaintext | yes | CCA, SGX; attestation complexity |
| **FHE** | strong (pure crypto) | 100–1000× slower | yes | the "no-trust" option; maturing fast |

See [[concepts/privacy-preserving-computing]] for the full primitive comparison.

## Related

- [[entities/heir]] — Google's open-source FHE compiler
- [[entities/google]] — parent program; Private Computing Toolkit
- [[concepts/ai-privacy-tools]] — consumer privacy tooling
- [[concepts/llm-inference]] — plaintext inference baselines
