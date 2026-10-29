# LeRoPE: Learnable RoPE Frequencies Improve Language Modeling

- **Source**: https://arxiv.org/abs/2607.10134
- **Authors**: Petros Karypis, Sean O'Brien, Shreyas Kadekodi, Rui Zhu, Julian McAuley
- **Submitted**: 2026-07-11
- **Affiliation (per attribution context)**: a lab in San Diego (UC San Diego — Julian McAuley's group), *not* Mistral AI. See §"Attribution" below.
- **Fetched**: 2026-10-29 via arXiv abstract page (curl + HTML parse)
- **Context**: surfaced by @eliebakouch (Prime Intellect) on X, Oct 29 2026, while dissecting the newly open-weighted Mistral Large 4 architecture.

## Abstract (verbatim from arXiv)

> Rotary Positional Encodings (RoPE) are currently the most popular positional encodings used in modern language models. RoPE rotates two-dimensional chunks of query and key vectors, operating as a function of their relative positional offset. The position-wise rates of rotation in RoPE typically follow a geometric sequence specified by a fixed base-frequency hyperparameter. Prior work has improved performance by either increasing this parameter to slow rotation or by applying RoPE to only a subset of QK dimensions. In this work we modify RoPE by learning a scalar per frequency, treating frequencies as learnable parameters rather than hyperparameters. We validate Learned RoPE by training a ladder of language models from scratch, ranging from 52M to 2.5B parameters. We observe and analyze the emergence of a high-norm, positional LeRoPE band. LeRoPE consistently outperforms RoPE and partial RoPE across all scales, with RoPE requiring 3.4% more compute (FLOPs) to match LeRoPE at the largest scale.

## Key contributions

1. **Frequencies as parameters, not hyperparameters.** Standard RoPE uses a geometric sequence of rotation rates fixed by a single `base` hyperparameter. LeRoPE attaches one learnable scalar per frequency band and trains it end-to-end.
2. **Scale ladder validation**: models trained from scratch from 52M → 2.5B parameters, so the result is not a single-scale artifact.
3. **Emergent "high-norm positional LeRoPE band"** — a structural finding about *how* the learned frequencies arrange themselves, analyzed in the paper.
4. **Headline efficiency number**: vanilla RoPE needs **3.4% more FLOPs** to match LeRoPE at the largest (2.5B) scale. LeRoPE beats both plain RoPE and partial RoPE at every scale tested.

## Attribution: why this matters (the "lab in San Diego" point)

Elie Bakouch's reaction when reading the Mistral Large 4 weight dumps was that he had assumed **LeRoPE** ("Learned RoPE") was a Mistral-invented technique, purely from the name — it is actually an independent arXiv paper from a San Diego lab (McAuley et al., July 11 2026). This is a small but useful correction to the common habit of treating a lab's architectural brand-name ("YaRN", "MLA", "DSA", "LeRoPE") as evidence of provenance.

## LeRoPE in the Mistral Large 4 architecture (Bakouch's analysis, Oct 29 2026)

In his thread dissecting the open weights of Mistral Large 4, @eliebakouch places LeRoPE inside a broader attention design:

- **Full sparse attention**, like DeepSeek V3.2 and the GLM-5.X series.
- **KV-cache sharing** for NoPE (no positional encoding) layers after layer 35; **indexer sharing** on RoPE layers starting at layer 17 (RoPE layers never share an index with NoPE layers).
- Indexer is "classical MLA/DSA" with a tweak: query is *not* down-projected, a norm is added instead.
- Indexer weights are far more layer-to-layer divergent in Mistral than in GLM/DeepSeek, where a **blockwise structure** is visible (Bakouch notes a resemblance to "jspace" and flags it for later investigation). Indexer maps also differ markedly from full attention maps — more so than in DeepSeek/GLM.
- Two long-context changes: **SSMax** (per-head learned term that adapts logit scaling — used by llama4/muse-style models; absent in Chinese labs' models per his reading) and **LeRoPE = YaRN + a learned term per frequency speed**.
- Overall shape much **wider and deeper** than Mistral Large 3; **no KV-cache compression**.

## Caveats

- Abstract-level provenance only for the paper itself (full PDF not scraped this run). The "San Diego lab" attribution comes from Bakouch's tweet plus the author list; UC San Diego affiliation was inferred from the author set, not read off the PDF.
- Benchmark claims (3.4% FLOP) are author-reported at ≤2.5B scale — **not** independently verified at frontier scale, and the Mistral Large 4 adoption of LeRoPE is Bakouch's weight-level inference, not a Mistral architectural statement.

## Related

- [[concepts/mistral-large-4]] — the model whose open weights triggered this thread
- [[entities/elie-bakouch]] — author of the architecture dissection
- [[concepts/positional-encoding]] — RoPE / NoPE / YaRN family (if present; else see [[concepts/scaling-laws]] for the training-ladder methodology)
