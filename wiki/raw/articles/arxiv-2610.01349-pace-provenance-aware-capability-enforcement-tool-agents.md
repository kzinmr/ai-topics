---
source_url: https://arxiv.org/abs/2610.01349
ingested: 2026-10-04
sha256: 7a11fa8837913860063f4d5bb1637a046a66a0d4800c02ed44f1d1c188cddee8
---

# PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents

Authors: Fengpeng Li, Qizhou Wang, Yuke Hu, Kemou Li, Jun Liu, Haiwei Wu, Jiantao Zhou, Di Wang.
arXiv:2610.01349, submitted 2026-10-01.

## Abstract
Tool-using large language model (LLM) agents turn generated text into real side effects, so poisoned tool metadata, retrieved pages, memory, and reusable skills can steer the next call. Vetting an artifact before admission does not settle this. A safe variant and a leaking variant can produce the same admission evidence, and a sound gate then cannot relax that site for either. We make that condition precise, which leaves the last boundary a deployment can still act on. We present Provenance-Aware Capability Enforcement (PACE), which mediates every tool call immediately before it executes. Path confinement proposes an executable cut of represented influence paths, while capability and effect verification checks schema-defined effects against authority compiled from the authenticated request. We distinguish the certified execution contract from the evaluated configuration, which can restore an authorized call after a proposed block or apply a declared repair. Confinement requires the final action to preserve the certified cut. On eight executable agent-security benchmarks with three target-model families, the evaluated configuration gives strictly lowest attack success in 62 of 79 eligible attack columns and ties in 14; full-benchmark native utility loses at most three points relative to the undefended agent. A complete ablation over 1167 paired cases attributes most security gains to effect verification and refusal control to boundary adaptation. A reduced-scale adaptive search succeeds on 0/30 out-of-authority targets against the defense.
