---
source_url: https://arxiv.org/abs/2609.19145
ingested: 2026-09-17
sha256: 48d144a4d5a4aed0122cb4546ffeea1e9d26c0ed559364079afad5a066362f57
---

# Objective vs. Search: Decomposing What Makes a Good Tokeniser

- **arXiv:** 2609.19145v1
- **Submitted:** 2026-09-16
- **Authors:** Ahmetcan Yavuz, Clara Meister, Tiago Pimentel

## Abstract (verbatim)

Two dominant tokenisation algorithms are used by modern language models: byte-pair encoding (BPE) and UnigramLM. These differ along two orthogonal axes: their optimisation objective (compression vs. log-likelihood) and their search procedure (bottom-up merging vs. top-down pruning). Existing comparisons confound these axes, making it unclear whether their observed differences stem from what is being optimised vs. how it is being optimised. We disentangle the two by (a) running each objective under the other's search and (b) evaluating downstream LM quality. We find that the search procedure is largely inconsequential for downstream performance, while the objective is the dominant factor; the log-likelihood objective yields consistent gains over compression. (abstract truncated at source)

## Core finding
Prior BPE-vs-UnigramLM comparisons **confound** two orthogonal axes:
- **Objective**: compression (BPE) vs. log-likelihood (UnigramLM).
- **Search**: bottom-up merging (BPE) vs. top-down pruning (UnigramLM).

By swapping objective and search independently, they show **search barely matters** for downstream LM quality; the **objective dominates**, with the log-likelihood objective giving consistent gains over compression. This reframes the tokenization debate away from the algorithm folklore toward the choice of objective.

## Related
Connects to the broader tokenization research line (tokenizer quality, subword choice, OOV, cross-lingual tokenization) and to LLM pretraining data/token budget tradeoffs.
