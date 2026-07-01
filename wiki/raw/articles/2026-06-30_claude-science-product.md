---
title: "Claude Science — AI Workbench for Scientists"
date: 2026-06-30
type: raw_article
sources:
  - https://claude.com/product/claude-science
  - https://modal.com/blog/modal-integration-brings-scalable-compute-to-claude-science
source: web-extract
---
# Claude Science — Anthropic's AI Workbench for Life Sciences

**Launch Date:** June 30, 2026
**Status:** Public Beta (macOS and Linux)

## Product Description

Claude Science is an AI workbench for scientists that runs analyses, searches databases, and traces every step from data wrangling to publication. It is a desktop application (not a separate model) that uses existing Claude models with scientific tooling, database connections, and compute infrastructure.

## Key Features

### Reproducible Science
- Every artifact (figures, tables, notebooks) includes exact code, environment, and conversation that produced them
- Results can be reproduced, edited, or defended months later
- Background reviewer flags incorrect citations, untraceable numbers, and figures that don't match underlying code

### Native Scientific Visualization
- View proteins, structures, and molecules natively
- Inspect proteins, alignments, genomic tracks, chemical structures, and PDFs
- Figure iteration via plain-language annotation — agent reads code and edits directly

### Compute Management
- Runs on local machine, HPC cluster (Slurm/SSH), or cloud GPUs via Modal
- Persistent Python and R kernels — variables, dataframes, and loaded models stay in memory
- Manages environments for each analysis automatically
- Writes batch scripts, submits and manages jobs over SSH

### Domain Coverage
- Genomics, single-cell, proteomics, structural biology, cheminformatics
- 60+ scientific databases accessible
- Protein language models: Evo 2, Boltz-2, OpenFold3
- Save pipelines as reusable skills; connect lab tools via connectors

### Modal Integration
- When local compute is insufficient, workloads route to Modal automatically
- Virtual screening fan-out across hundreds of concurrent GPUs
- Heterogeneous workloads: CPU for alignment/preprocessing, GPU for structure prediction
- Shared volumes for sequencing datasets, protein databases, model checkpoints

## Pricing & Availability
- Available on Pro, Max, Team, and Enterprise plans
- Academic/nonprofit labs: Claude Team plan for research labs
- Enterprise: SSO, SCIM provisioning, custom roles, usage analytics
- $30 free Modal compute to start

## Notable Quotes
- "With Claude Science I can go from raw data to a publication-quality figure in a single session" — Mike Nichols, Manifold Bio
- "Claude Science is enabling analyses that simply wouldn't have been feasible for me as a non-computational biologist" — Iain Cheeseman, MIT
- "The most impressive AI-integrated scientific computing environment I have encountered" — Prasad Shirvalkar, UCSF
- "Immediately found a laboratory virus contaminant in our bulk RNA-seq data. We spun our wheels on this for the better part of a year" — Stephen Francis, UCSF
