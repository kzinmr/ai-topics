---
title: "HEIR — Homomorphic Encryption Intermediate Representation (Google)"
type: article
source: https://github.com/google/heir
publisher: GitHub (google org)
fetched: 2026-08-19
fetched_by: active-crawl
---

# google/heir (GitHub README, fetched 2026-08-19)

- Repo tagline: "A compiler for homomorphic encryption"
- README: "HEIR: Homomorphic Encryption Intermediate Representation — An MLIR-based toolchain for homomorphic encryption compilers."
- Three usage modes:
  1. bazel + rules_heir with either the **OpenFHE** or **Lattigo** backend
  2. `heir_py` Python package (requires OpenFHE installed)
  3. Build from source, invoke `heir-opt` and `heir-translate` binaries, extract generated backend code
- Build: bazel/bazelisk; depends on LLVM built from source (clean build ~30 min); BuildBuddy CI supported
