---
title: Antoine Chaffin
created: 2026-05-28
updated: 2026-06-04
type: entity
tags:
  - person
  - search
  - late-interaction
  - open-source
  - france
sources:
  - raw/articles/2026-04-21_antoine-chaffin_denseon-lateon-open-sota-retrieval.md
  - raw/articles/2026-06-03_antoine-chaffin_ir-direction-sublinear-querying.md
  - https://www.linkedin.com/in/antoine-chaffin/
status: active
---

# Antoine Chaffin

Antoine Chaffin is a researcher at [[entities/lighton|LightOn]], specializing in information retrieval, late interaction models (ColBERT), and open-source AI. He is the lead author of the DenseOn/LateOn release (April 2026) and a key contributor to the PyLate library for ColBERT-style retrieval training.

## Key Contributions

- **[[entities/denseon-lateon|DenseOn & LateOn]]** (Apr 2026): Open SOTA single and multi-vector retrieval models — DenseOn (BEIR 56.20) and LateOn (BEIR 57.22), both under 150M params
- **[[concepts/pylate|PyLate]]** (CIKM 2025): First peer-reviewed library for training ColBERT-style models. Co-author with Sourty.
- **ColBERT-Zero**: Unsupervised ColBERT model (prior SOTA, 55.32 BEIR)
- **GTE-ModernColBERT-v1**: Bi-directional late interaction improvements
- **[[entities/late-interaction|Late Interaction Workshop (LIR) @ ECIR 2026]]**: Co-organizer

## Philosophy

Chaffin advocates for **fully open retrieval** — not just model weights but training data, curation pipelines, and mixture recipes:

> "We don't just release models that outperform every model their size and models 4× bigger... We also release the large-scale curated datasets and findings so you can do the same."

> "When I started working at LightOn, two years ago, I was looking at all the top models and thinking 'wow, imagine the work that it would be to achieve this.' Today... LightOn put out a whole pipeline to go from totally random weights to state-of-the-art results."

### On the Future Direction of IR (Jun 2026)

In response to [[entities/mixedbread|Mixedbread]]'s Latent Terms paper and [[entities/ben-clavie|Ben Clavie]]'s analysis, Chaffin articulated a reframing of the retrieval problem:

- **The goal is not information reconstruction** — dense embeddings already contain enough info to reconstruct inputs (known since 2023). The real goal is making information **queryable in sublinear time**.
- **Scoring mechanism is the real constraint** — the embedding model's role is to convert document info into a format consumable by an efficient scoring mechanism.
- **Dense and sparse are complementary** — dense leverages spatial proximity, sparse leverages component overlap. Both enable fast search differently. A unified theory is needed.
- **Reframe the question**: Stop asking "how do I encode all information" → ask "how do I present information for quick, accurate querying"

> "Maybe the question is not which one is going to win, but whether we'll find something even better in the way"

## Affiliations

- Researcher, [[entities/lighton|LightOn]] (Paris, France)
- Co-organizer, Late Interaction Workshop @ ECIR 2026
- LinkedIn: [antoine-chaffin](https://www.linkedin.com/in/antoine-chaffin/)

## Related

- [[entities/mixedbread|Mixedbread]] — Company whose Latent Terms research Chaffin analyzed
- [[entities/ben-clavie|Ben Clavie]] — Mixedbread researcher, co-discussant on IR direction
- [[entities/late-interaction]] — Late interaction retrieval paradigm

## Overview
Stub page for antoine-chaffin.


## Related Pages
- [[entities/_index]]

