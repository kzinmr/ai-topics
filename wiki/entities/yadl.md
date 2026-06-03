---
title: "YADL (Yet Another Data Lake)"
created: 2026-06-03
updated: 2026-06-03
type: entity
tags: [datasets, benchmark, data-lakes, open-data, data-science]
sources: [raw/articles/retrieve-merge-predict.md]
---

# YADL (Yet Another Data Lake)

**YADL** is a semi-synthetic data lake built on the [YAGO3](https://yago-knowledge.org/) knowledge base, developed as a benchmarking tool for data discovery and table augmentation tasks. It was created by the INRIA SODA team as part of the [[concepts/retrieve-merge-predict]] research.

## Overview

YADL provides a controlled, reproducible environment for evaluating methods that discover and integrate tabular data from data lakes. Unlike real-world data lakes (e.g., Open Data US), YADL offers known ground truth for join relationships and feature relevance, enabling systematic benchmarking.

## Key Properties

| Property | Detail |
|---|---|
| Base knowledge | YAGO3 (Wikipedia + WordNet derived) |
| Type | Semi-synthetic data lake |
| Format | Parquet |
| License | CC BY 4.0 (inherited from YAGO3) |
| Purpose | Benchmarking data discovery and table augmentation |
| Variants | Multiple versions with different characteristics (binary, full, etc.) |

## Availability

- **Data**: [Zenodo](https://zenodo.org/records/12607873)
- **Preparation code**: [github.com/rcap107/YADL](https://github.com/rcap107/YADL)
- **Pipeline code**: [github.com/soda-inria/retrieve-merge-predict](https://github.com/soda-inria/retrieve-merge-predict)

## Base Table Datasets Used with YADL

The pipeline evaluation uses several base tables:
- Company Employees (Kaggle, CC0)
- Housing Prices (Zillow)
- US Accidents (Kaggle, CC BY-NC-SA 4.0)
- US Elections (Harvard Dataverse, CC0)
- Schools (Open Data US internal)
- US County Population (YADL internal)

## Relation to YAGO3

YAGO3 is a large-scale knowledge base automatically extracted from Wikipedia, WordNet, and GeoNames. YADL transforms YAGO3's structured triples into a collection of relational tables suitable for data lake benchmarking, preserving the semantic diversity and relationships of the original knowledge base.

## Significance

YADL fills an important gap in the data lake research ecosystem by providing:
1. **Reproducibility**: Open data, open code, controlled conditions
2. **Ground truth**: Known join relationships for evaluation
3. **Scalability**: Variants of different sizes for testing method scalability
4. **Complementarity**: Pairs with real-world data lakes (Open Data US) for robust evaluation
