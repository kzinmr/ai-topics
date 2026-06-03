---
title: "Retrieve, Merge, Predict: Augmenting Tables with Data Lakes"
url: https://soda-inria.github.io/retrieve-merge-predict/
arxiv: https://arxiv.org/abs/2402.06282
github: https://github.com/soda-inria/retrieve-merge-predict
fetched: 2026-06-03
---

# Retrieve, Merge, Predict: Augmenting Tables with Data Lakes

**Authors**: Riccardo Cappuzzo, Aimee Coelho, Felix Lefebvre, Paolo Papotti, Gael Varoquaux
**Affiliation**: INRIA SODA team
**arXiv**: https://arxiv.org/abs/2402.06282
**Project page**: https://soda-inria.github.io/retrieve-merge-predict/
**GitHub**: https://github.com/soda-inria/retrieve-merge-predict

## Abstract

Machine-learning from a disparate set of tables, a data lake, requires assembling features by merging and aggregating tables. Data discovery can extend autoML to data tables by automating these steps. We present an in-depth analysis of such automated table augmentation for machine learning tasks, analyzing different methods for the three main steps: retrieving joinable tables, merging information, and predicting with the resultant table. We use two data lakes: Open Data US, a well-referenced real data lake, and a novel semi-synthetic dataset, YADL (Yet Another Data Lake), which we developed as a tool for benchmarking this data discovery task. Systematic exploration on both lakes outlines 1) the importance of accurately retrieving candidate tables to join, 2) the efficiency of simple merging methods, and 3) the resilience of tree-based learners to noisy conditions. Our experimental environment is easily reproducible and based on open data, to foster more research on feature engineering, autoML, and learning in data lakes.

## Pipeline Overview

The paper presents a three-stage pipeline for augmenting a base table with data from a data lake to improve ML predictions:

1. **Retrieve**: Extract join candidate tables from the data lake that can be joined with the base table.
2. **Merge**: Combine the candidates with the base table in the most effective way possible.
3. **Predict**: Train an ML model on the augmented table.

### Use Case (Alice Example)

Alice has a base table about movies and wants to predict movie rankings. She has access to a data lake containing diverse tables. The challenge is finding relevant tables among a huge volume of unrelated data and integrating them effectively.

## Retrieval Methods Evaluated

- **Exact Matching**: Join on exact value matches between columns
- **MinHash / LSH**: Approximate set similarity for join discovery
- **Hybrid MinHash**: Combines MinHash with re-ranking at query time
- **Starmie**: Learned join column discovery (from Megagon Labs)

## Key Findings

1. **Retrieval is critical**: Accurately retrieving candidate tables to join is the most important step
2. **Simple merging works well**: Simple merging methods are surprisingly efficient
3. **Tree-based models are robust**: Tree-based learners (e.g., gradient boosting) are resilient to noisy conditions from imperfect joins

## Benchmark Data Lake: YADL

- **YADL** (Yet Another Data Lake): A semi-synthetic data lake built on YAGO3 knowledge base
- Available on Zenodo: https://zenodo.org/records/12607873
- YADL preparation code: https://github.com/rcap107/YADL
- Also evaluated on Open Data US (real-world data lake)

## Base Table Datasets

- Company Employees (Kaggle, CC0)
- Housing Prices (Zillow)
- US Accidents (Kaggle, CC BY-NC-SA 4.0)
- US Elections (Harvard Dataverse, CC0)
- Schools (Open Data US internal)
- US County Population (YADL internal)

## Technical Details

- All tables stored in Parquet format
- Conda-based environment
- Pipeline split into modular stages: metadata preparation, retrieval indexing, querying, execution, evaluation
- Reproducible experimental environment based on open data
