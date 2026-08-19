---
title: Privacy-Preserving Computing
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [concept, security, cryptography, privacy, privacy-preserving-computing, privacy-preserving-ml, homomorphic-encryption, trusted-execution-environments, ai-safety]
sources: [raw/articles/2026-08-19_google_heir-private-ai-homomorphic-encryption.md]
---

# Privacy-Preserving Computing (PPC)

Techniques that let a party compute over another party's data without the computing party learning the underlying data. For AI/ML, the question is: can a model serve inference on private inputs (user data, patient records, financial positions) without the operator ever seeing the plaintext?

## The four mainstream primitives

| Primitive | Mechanism | Trust assumptions | Typical AI use | Weaknesses |
|---|---|---|---|---|
| **Differential privacy** | Add calibrated noise so individual records can't be distinguished | None (statistical) | Training on user data, query logging | Noise degrades utility; hard for per-query inference |
| **Private information retrieval (PIR)** | Query a database without the server learning which item | None (computational) | Lookups, embeddings retrieval | Single-query; limited for multi-round workloads |
| **Secure enclaves / TEEs** (SGX, CCA, SE) | Hardware-isolated memory region; code + data encrypted in flight & at rest | CPU vendor, hypervisor, firmware, attestation chain | Confidential inference (many startups) | Trust in silicon/firmware supply chain; side channels; "trusted hardware" objection |
| **Homomorphic encryption (FHE)** | Compute directly on ciphertext; only holder of the key can decrypt | None (purely cryptographic) | Confidential inference, private RAG, secure multi-party ML | Heavy compute overhead (mitigating — see [[concepts/homomorphic-encryption-ai]]) |

Hybrid designs combine primitives, e.g. **Bifrost** (arXiv:2606.17421, 2026) runs Transformer/LLM serving as TEE + FHE, and **GoldenRetriever** (arXiv:2607.29019) does non-interactive FHE-encrypted retrieval for privacy-preserving RAG.

## Why it matters for AI specifically

1. **Regulatory & sector pressure** — healthcare, finance, and government data are often contractually or legally barred from being visible to the model provider; "local processing" caps capability and leaks model IP
2. **The E2E-encryption trade-off** — end-to-end encryption protects user data but strips the provider of the ability to compute useful features (spam detection, personalization, recommendations); PPC restores that capability without breaking the privacy promise
3. **Model IP vs user privacy** — shipping the model to the edge protects user data but exposes the model; FHE/TEE keep the model on the server
4. **Composability** — PPC primitives compose with standard ML pipelines (RAG, agents, fine-tuning), which is why the research area is converging on *full-stack* private ML rather than point solutions

## Open questions / debates

- **Trust trade-off**: TEEs are faster but assume trusted silicon; FHE is slower but needs no hardware trust. For regulated industries the choice is a policy decision, not just an engineering one
- **FHE cost curve**: Google's HEIR team (2026) frames FHE's "nontrivial cost overhead" as shifting to "a question of cost" that is "rapidly decreasing" — whether that curve reaches interactive latency for frontier models remains open
- **Standardization**: no consensus API yet for "private inference" as a service primitive (contrast: TEE attestation is becoming standardized)
- **Hybrid architectures**: where do TEEs and FHE split the workload? First experimental splits exist (Bifrost); best-practice guidance is absent

## Key references

- Google Private Computing Toolkit (HEIR compiler — see [[entities/heir]])
- NIST GenAI Profile (NIST-AI-100-2) — privacy section
- arXiv:2601.18511 — scaling FHE Llama-3-8B inference (2026)
- arXiv:2602.11470 (Cachemir), arXiv:2606.17421 (Bifrost), arXiv:2607.29019 (GoldenRetriever)

## Related concepts

- [[concepts/homomorphic-encryption-ai]] — FHE applied to LLM inference (deep dive)
- [[concepts/ai-privacy-tools]] — consumer-facing privacy tooling
- [[concepts/security-and-governance/ai-safety-and-alignment]] — broader safety/alignment context
- [[entities/google]] — Google's private-computing program
