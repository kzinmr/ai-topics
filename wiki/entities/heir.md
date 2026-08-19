---
title: HEIR (Google homomorphic encryption compiler)
created: 2026-08-19
updated: 2026-08-19
type: entity
tags: [entity, tool, open-source, google, cryptography, llm-inference, privacy, homomorphic-encryption, compiler, developer-tooling]
sources: [raw/articles/2026-08-19_google_heir-private-ai-homomorphic-encryption.md, raw/articles/2026-08-19_github_google_heir-readme.md]
---

# HEIR (Google)

**HEIR** (Homomorphic Encryption Intermediate Representation) is Google's open-source compiler toolchain that converts programs — including pre-trained AI models — from operating on plaintext to operating on **encrypted inputs**, enabling non-interactive, cryptographically-private inference without hardware TEEs. Announced on Google's security blog in August 2026 (HN front page, ~498 pts); the project was first announced in 2023.

## What it is

- An **MLIR-based** compiler toolchain ("HEIR" = Homomorphic Encryption *Intermediate Representation*), part of Google's Private Computing Toolkit (alongside differential privacy, private set membership, PIR, secure enclaves)
- Backends: **OpenFHE** and **Lattigo** (via bazel/rules_heir, the `heir_py` Python package, or the `heir-opt`/`heir-translate` binaries)
- Goal: a "one-click solution" so non-cryptographers can add encrypted inference to production apps — the blog frames hand-written FHE as a task that otherwise "requires a team of cryptographers"
- Security model: **purely cryptographic** (no trusted hardware), which distinguishes it from TEE/enclave-based private inference — and matters for model IP: unlike "ship the model to the device," the server never sees plaintext and the model never leaves the provider

## The problem it solves

Standard E2E encryption creates a trade-off: user data is protected, but the service provider can't compute over it (spam detection, recommendations, medical/financial inference). Local processing is bounded by device capability and leaks the model's IP. FHE shifts the trade-off to cost — "the cost of homomorphic encryption is rapidly decreasing."

## Ecosystem (per Aug 2026 blog)

- **Hardware accelerator partners**: Belfort, Niobium, Cornami, Optalysys
- **Academic collaborators**: Georgia Tech, Carnegie Mellon, UC Santa Barbara, Illinois Institute of Technology, Purdue, University of Edinburgh, Tsinghua University, and others
- **Four peer-reviewed publications** built on HEIR, "more in preparation"
- **Four private-inference demos** (all compiled with HEIR; latencies quoted single-threaded CPU): content recommendations, search, a medical-diagnosis model, and a large language model

## Key facts

| Fact | Value |
|---|---|
| Announced | 2023 (intent); major update + 4 demos Aug 2026 |
| Repo | `github.com/google/heir` |
| Scheme support | CKKS (main), TFHE (via backend); Lattigo & OpenFHE backends |
| Status | Open source (Apache-2.0), active, Google-maintained |

## Related

- [[concepts/homomorphic-encryption-ai]] — the broader technique and state of FHE-based LLM inference
- [[entities/google]] — parent organization; private computing program
- [[concepts/homomorphic-encryption-ai]] — FHE-based private inference technique & research state
- [[concepts/privacy-preserving-computing]] — PIR, DP, secure enclaves, FHE as a family of private-computing primitives
