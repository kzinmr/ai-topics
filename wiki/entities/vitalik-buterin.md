---
title: "Vitalik Buterin"
type: entity
aliases: [buterin]
created: 2026-08-24
updated: 2026-08-24
tags: [person, cryptography, ai-safety]
sources:
  - raw/articles/2026-08-21_vitalik_local-mixing-code-obfuscation.md
---

# Vitalik Buterin

Vitalik Buterin is the co-founder and long-time lead of **Ethereum**, and one of the most prolific technical bloggers in the crypto/ML intersection. His blog (vitalik.eth.limo) publishes deep, self-contained technical series that are frequently cited across the AI security community.

## Core Ideas

### Code obfuscation against AI code comprehension (2026)

Buterin's 3-part "Obfuscation" series (2026) is a systematic treatment of **indistinguishability obfuscation (iO)** as a defense against LLMs reading and understanding source code:

- **Part I/II**: the two "classical" iO families — mainstream conservative line (near-standard assumptions, galactic overhead) and "diamond iO" (lattice-based, lower overhead, still not viable to run).
- **Part III (Aug 21, 2026)**: **local mixing** — a circuit-transformation pipeline (reversibility → hardening → gadgetization → mixing → fcompress) inspired by symmetric-cryptography design practice (confusion/diffusion) rather than reduction-based proofs. See [[concepts/local-mixing-code-obfuscation]] for the full pipeline and security analysis.

His framing: classical obfuscation protects against human reverse-engineers; LLMs have changed the threat model because they can read code fluently, so obfuscation must now defeat *pattern recognition at scale* — the same problem symmetric cryptography has attacked for 50 years.

### Recurring themes in his writing

- **Cryptographic rigor with AI-flavored applications**: FHE, iO, and post-quantum primitives applied to AI-era problems (e.g. obfuscation against code-comprehending models, secure agent execution).
- **Long-form, self-contained technical education**: each post is written to be readable without prior context, with worked examples (his two-bit adder circuit recurs across the series).
- **Bridging crypto and ML communities**: frequently reviews/coordinates with researchers from both fields (e.g. Nicholas Ho, Ran Canetti on the obfuscation series).

## Key Writings

| Date | Title | Venue |
|------|-------|-------|
| 2026-08-21 | Obfuscation (Part III): Local Mixing | vitalik.eth.limo |
| 2026-07-xx | Obfuscation (Part II): Diamond iO | vitalik.eth.limo |
| 2026-06-xx | Obfuscation (Part I): Introduction to iO | vitalik.eth.limo |
| ongoing | Ethereum roadmap / upgrade analyses | vitalik.eth.limo |

## Related

- [[concepts/local-mixing-code-obfuscation]] — the technique from his Part III post
- [[concepts/homomorphic-encryption-ai]] — adjacent crypto-for-AI work
- [[concepts/formal-verification-llm-agents]] — verification-based (vs. obfuscation-based) agent security
- [[concepts/coding-agents/ai-coding-agent-criticism]] — context for why code-comprehension attacks matter

## Sources

- https://vitalik.eth.limo/general/2026/08/21/obfuscation_part_iii_local_mixing.html
- https://vitalik.eth.limo/
