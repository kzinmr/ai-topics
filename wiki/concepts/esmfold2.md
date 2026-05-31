---
title: "ESMFold2"
created: 2026-05-31
updated: 2026-05-31
type: concept
tags: [model, ai-research, open-source, biology, deep-learning]
sources:
  - https://www.scientificamerican.com/article/new-protein-folding-ai-vastly-expands-on-alphafolds-efforts/
---

# ESMFold2

**ESMFold2** is a protein structure prediction AI model developed by researchers at the Chan Zuckerberg Initiative's Biohub, unveiled May 30, 2026. It generated the **ESM Atlas** — a database of over 1.1 billion predicted protein structures and 6.8 billion protein sequences, surpassing the [[entities/deepmind|Google DeepMind]] [[concepts/alphaproof|AlphaFold Database]] (200M structures) by 800M+ entries.

## Key Facts

- **Developer**: CZI Biohub (Mark Zuckerberg & Priscilla Chan's biomedical institute)
- **Lead researcher**: Alex Rives
- **Release date**: May 30, 2026
- **License**: Fully open source, no commercial restrictions
- **Architecture**: Based on a "protein language" model trained on billions of proteins from across the tree of life

## What's New vs AlphaFold

| Feature | AlphaFold DB | ESM Atlas (ESMFold2) |
|---|---|---|
| Predicted structures | ~200M | 1.1B+ |
| Protein sequences cataloged | — | 6.8B+ |
| Metagenomic sequences | No | Yes (soil, ocean, environments) |
| Open source | Partially | Fully (no commercial restrictions) |
| Interacting protein complexes | AlphaFold3 handles | ESMFold2 surpasses |

## Capabilities

- **Outperforms AlphaFold3** at determining correct structure of interacting protein complexes, including antibody-antigen binding
- **Protein design**: Used to design new antibodies and proteins targeting cancer and immunological conditions; lab-verified with high success rate
- **Metagenomic discovery**: Found structural similarities between CRISPR microbial defence proteins and a gene-editing protein identified in soil fungus (2023)
- **Novel algorithm discovery**: Discovered a new learning rate schedule achieving strictly better O(1/t) convergence rate in convex optimization

## Expert Reactions

- **Gemma Atkinson** (Lund University): "Extraordinary resource for biology"
- **Christine Orengo** (UCL): Could help uncover new protein folds and functions
- **Martin Steinegger** (Seoul National University): Questions performance on proteins very different from known ones
- **Sergey Ovchinnikov** (MIT): Views ESM Atlas as supplement to AlphaFold, not replacement

## Significance

The fully open-source nature with no commercial restrictions means ESMFold2 could see wide adoption across academia and industry. It represents the democratization of protein structure prediction, complementing rather than replacing AlphaFold. See also [[concepts/physical-ai]] for AI applications in biological sciences.

## Related Pages
- [[entities/deepmind]] — AlphaFold developer
- [[concepts/alphaproof]] — DeepMind's formal proof system
- [[entities/chan-zuckerberg-initiative]] — CZI Biohub, developer of ESMFold2
- [[concepts/open-source]] — Open source AI movement
