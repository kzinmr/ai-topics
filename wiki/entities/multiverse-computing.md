---
title: "Multiverse Computing"
created: 2026-09-03
updated: 2026-09-03
type: entity
tags: [company, model, inference, open-source, sovereign-ai, reasoning, mixture-of-experts, quantization]
aliases: ["Multiverse", "Multiverse Computing Euskadi"]
sources:
  - raw/articles/multiversecomputing-com--resources-introducing-quasar-438b-europe-s-leading-ai-model.md
related:
  - entities/mistral-ai
  - concepts/sovereign-ai
  - concepts/model-quantization
  - concepts/reasoning-models
confidence: high
---

# Multiverse Computing

Multiverse Computing is a Spanish AI company (Donostia–San Sebastián, Basque Country; HQ in Spain with an Euskadi R&D center) that builds **extreme model-compression technology** on top of quantum-inspired mathematics. Its slogan — *"Beyond quantum, infinite impact"* — reflects its origin story: a quantum-mathematics research group that pivoted its tensor-network/discrete-geometry tooling into classical LLM compression, claiming 100x–1000x compression without accuracy loss.

## Quasar 438B (September 1, 2026)

The company's flagship release, billed as **"Europe's leading AI model"** and its first **open-weights** frontier-scale model:

| Dimension | Detail |
|---|---|
| Parameters | 438B total, **30B active** (MoE) |
| Benchmark | **44.7%** on Humanity's Last Exam — "world's most accurate open-source model" at release |
| Specialization | Math and logical reasoning emphasis |
| License | **Apache 2.0** |
| Availability | Hugging Face + Ollama |
| Pricing (hosted) | Input $0.45/M, cached input $0.12/M, output $1.80/M — under half of comparable frontier hosted models |
| Infrastructure | **Cohere** as exclusive global hosted-inference partner |

^[[raw/articles/multiversecomputing-com--resources-introducing-quasar-438b-europe-s-leading-ai-model.md]]

The headline claim: beating the Llama line while using **3x fewer parameters** — the compression thesis made concrete at frontier scale.

## Strategy: "Not a Mistral Clone"

CEO Borja Martinez-Castillo (BSC) frames Quasar as Europe building its *own* frontier model, differentiated from [[entities/mistral-ai|Mistral AI]]'s strategy: Mistral pursued smaller, cheaper, open-weight-plus-proprietary European alternatives, while Multiverse bets that **compression is the European path to frontier capability** — European data-center constraints (energy, capital) make extreme efficiency a strategic asset rather than an optimization detail.

The **Cohere partnership** is notable: a European model vendor choosing a Canadian inference partner rather than US hyperscalers — consistent with the sovereignty positioning while acknowledging Europe lacks frontier-scale cloud capacity (see [[concepts/sovereign-ai]]).

## Key Facts

- Founded: 2021, Spain.
- Focus: quantum-inspired compression (tensor networks, discrete geometry) applied to LLMs.
- Claimed compression ratios: 100x–1000x with no accuracy loss (vendor claim; independent replication limited — treat with caution).
- Quasar 438B is its first open-weights release; prior work was compression tools/SDKs.

## See Also

- [[entities/mistral-ai]] — Europe's other sovereign-AI champion
- [[concepts/sovereign-ai]] — the policy frame Multiverse invokes
- [[concepts/model-quantization]] — quantization/compression techniques
- [[concepts/model-merging]] — related model-efficiency approach
- [[concepts/reasoning-models]] — the benchmark category Quasar targets

## Sources

- raw/articles/multiversecomputing-com--resources-introducing-quasar-438b-europe-s-leading-ai-model.md
