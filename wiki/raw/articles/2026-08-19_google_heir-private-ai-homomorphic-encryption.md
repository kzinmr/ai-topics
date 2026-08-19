---
title: "How Google is Making Private AI Practical with Homomorphic Encryption"
type: article
source: https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/
publisher: Google (The Keyword — Google Security blog)
fetched: 2026-08-19
fetched_by: active-crawl
---

# How Google is Making Private AI Practical with Homomorphic Encryption

_Source: https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/ (Google Security blog, The Keyword, August 2026; HN front page Aug 14 2026, 498 pts)_

## Key claims (verbatim excerpts)

> Today we're excited to showcase HEIR, the latest powerful tool added to our Private Computing Toolkit. HEIR is an open source compiler that unlocks cryptographically-secure private AI inference.

> Standard protections like end-to-end encryption present a trade-off: user-data can be protected from data breaches, but then the service provider cannot provide features that depend on the data, such as spam or virus detection. Critical sectors like healthcare and finance are even more averse to these risks, and strict regulations limit data sharing across institutions. Alternative mechanisms to provide the same features, like local processing, are limited by the capabilities of the local device and the sensitivity of the service provider's IP. Shipping proprietary AI to a device risks leaking the model.

> A solution to these issues is homomorphic encryption, a rapidly maturing technology that fundamentally alters this trade-off by allowing computations to be performed directly on encrypted data. Servers can process ciphertexts and return encrypted results without exposing any underlying information. For example, a cloud service can provide content recommendations without being able to see the user's features. But while homomorphic encryption has a nontrivial cost overhead, it shifts the capability/privacy trade-off to a question of cost. And the cost of homomorphic encryption is rapidly decreasing.

> Google's history of innovations in privacy technology — from differential privacy and private set membership to private information retrieval and secure enclaves on Google Cloud — has always focused on securing user data. Homomorphic encryption is another powerful tool we're adding to our private computing toolkit. Like private information retrieval, and in contrast to hardware-based solutions, homomorphic encryption's strong security and privacy guarantees are purely cryptographic. However, manually converting an existing program to use homomorphic encryption efficiently requires a team of cryptographers.

> To overcome the usability challenges and advance the opportunity of homomorphic encryption, researchers and engineers at Google built the HEIR compiler project. HEIR (Homomorphic Encryption Intermediate Representation) is an open-source compiler toolchain and development platform for homomorphic encryption. In particular, HEIR can convert pre-trained AI models that operate on unencrypted data to operate on encrypted inputs. Our vision is to make HEIR a one-click solution to enable non-experts to incorporate encrypted inference into production applications.

> Since announcing our intentions in 2023, we've seen the homomorphic encryption community embrace HEIR. We have partnered with companies developing hardware accelerators for homomorphic encryption, including Belfort, Niobium, Cornami, and Optalysys. The fruits of those efforts are shown in our demos below, and we plan to demonstrate the latency benefits of these accelerators in the near future. HEIR has also become a productive research platform. By building on HEIR, cryptographers can focus on their specific optimization and use the existing infrastructure for testing, benchmarking, and comparisons. This has resulted in collaborations with Georgia Tech, Carnegie Mellon, UC Santa Barbara, Illinois Institute of Technology, Purdue, the University of Edinburgh, Tsinghua University, and others. To date, four peer-reviewed publications were built on HEIR, with more in preparation, and HEIR has accumulated numerous citations.

> To demonstrate how far homomorphic encryption has come, we're sharing four private inference applications. Each application was compiled with HEIR, and latency numbers are presented for a single-threaded CPU. The source code for all examples is available in our GitHub repository.

> As the software industry adapts to security and privacy changes amid AI, our research team is working to make homomorphic encryption easy to develop, fast to run, and ubiquitous across industry.

## Companion facts (GitHub: google/heir, fetched 2026-08-19)

- Repo description: "A compiler for homomorphic encryption"
- README: "HEIR: Homomorphic Encryption Intermediate Representation — An MLIR-based toolchain for homomorphic encryption compilers."
- Backends: OpenFHE and Lattigo (via bazel/rules_heir, or `heir_py` Python package, or `heir-opt` / `heir-translate` binaries)
- Build: bazel + bazelisk; depends on LLVM (from source)
