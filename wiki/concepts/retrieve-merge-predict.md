---
title: "Retrieve, Merge, Predict (Table Augmentation Pipeline)"
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [automl, feature-engineering, data-lakes, information-retrieval, datasets, benchmark, data-science, data-integration]
sources: [raw/articles/retrieve-merge-predict.md]
---

# Retrieve, Merge, Predict (Table Augmentation Pipeline)

**Retrieve, Merge, Predict** is a three-stage pipeline for augmenting a base table with features from a data lake to improve machine learning predictions. Proposed by Cappuzzo et al. (INRIA SODA, 2024), it systematically analyzes how to discover, integrate, and learn from heterogeneous tabular data stored in data lakes.

## The Pipeline

The core idea: given a **base table** with a prediction target and a **data lake** (a large collection of heterogeneous tables), automatically find and integrate relevant features to boost ML performance.

1. **Retrieve** — Discover join candidate tables from the data lake that share joinable columns with the base table. Methods evaluated:
   - **Exact Matching**: Join on exact value overlap between columns (hash-based counting)
   - **MinHash / LSH**: Approximate set similarity for scalable join discovery
   - **Hybrid MinHash**: MinHash with re-ranking at query time for higher precision
   - **Starmie**: Learned join column discovery (Megagon Labs)

2. **Merge** — Combine retrieved candidate tables with the base table. Strategies include simple left joins, value aggregation, and handling of duplicate/nested keys.

3. **Predict** — Train ML models (tree-based learners, linear models) on the augmented table. The paper finds that tree-based models (gradient boosting) are particularly robust to noise from imperfect joins.

## Key Findings

| Finding | Detail |
|---|---|
| Retrieval accuracy is critical | The quality of candidate table retrieval has the largest impact on final ML performance |
| Simple merging works well | Elaborate merging strategies offer marginal gains over straightforward joins |
| Tree-based models are resilient | Gradient boosting and similar models handle noisy, imperfectly-joined features gracefully |
| Data lake size matters | Larger data lakes provide more opportunities for feature discovery but increase retrieval noise |

## Benchmark: YADL

The paper introduces **[[entities/yadl]]** (Yet Another Data Lake), a semi-synthetic data lake built on the [[entities/yago]] knowledge base, specifically designed for benchmarking data discovery and table augmentation tasks. YADL provides controlled experimental conditions with known ground truth, complementing real-world evaluations on Open Data US.

## Relation to AutoML and Feature Engineering

This pipeline extends the [[concepts/retrieval-augmented-generation]] paradigm from text to structured tabular data. Instead of retrieving text chunks for LLM context, it retrieves table columns for ML feature augmentation. The approach connects to:

- **AutoML**: Automating the feature engineering step that traditionally requires domain expertise
- **Data Integration**: Classical problems of schema matching and entity resolution applied at data-lake scale
- **[[concepts/vector-search]]**: Some retrieval methods use embedding-based similarity for column matching

## Paper Details

- **Authors**: Riccardo Cappuzzo, Aimee Coelho, Felix Lefebvre, Paolo Papotti, Gael Varoquaux
- **Affiliation**: INRIA SODA team
- **arXiv**: [2402.06282](https://arxiv.org/abs/2402.06282)
- **Project page**: [soda-inria.github.io/retrieve-merge-predict](https://soda-inria.github.io/retrieve-merge-predict/)
- **Code**: [github.com/soda-inria/retrieve-merge-predict](https://github.com/soda-inria/retrieve-merge-predict)
- **YADL data**: [Zenodo](https://zenodo.org/records/12607873)

## Open Questions

- How do these methods scale to data lakes with millions of tables?
- Can LLMs assist in column semantics matching for better retrieval?
- How does this approach compare to prompt-based tabular reasoning with LLMs?
