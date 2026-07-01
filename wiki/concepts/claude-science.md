---
title: "Claude Science — AI Workbench for Life Sciences"
created: 2026-07-01
updated: 2026-07-01
type: concept
tags:
  - claude
  - product
  - ai-in-science
  - biology
sources:
  - raw/articles/2026-06-30_claude-science-product.md
---

# Claude Science — AI Workbench for Life Sciences

Claude Science is [[entities/anthropic|Anthropic]]'s AI workbench designed specifically for life sciences research. Launched June 30, 2026 in public beta for macOS and Linux, it is a desktop application that layers scientific tooling, database connections, and scalable compute infrastructure on top of existing Claude models. It is not a separate model — rather, it is a domain-specific environment that brings [[concepts/claude/fable-5|Claude's capabilities]] directly into the laboratory workflow.

## Key Features

### Reproducible Artifacts
Every output — figures, tables, notebooks — carries the exact code, environment snapshot, and conversation that produced it. A background reviewer flags incorrect citations, untraceable numbers, and figures inconsistent with their underlying code. Results can be reproduced, edited, or defended months after generation, making Claude Science a tool for publishable research rather than exploratory tinkering.

### Native Scientific Visualization
The workbench can natively render proteins, molecular structures, genomic tracks, chemical structures, alignments, and PDFs. Scientists iterate on figures through plain-language annotation — the agent reads figure-generating code and edits it directly, collapsing the gap between "what I want this figure to show" and "what the code actually produces."

### Compute Management
Claude Science runs locally, on HPC clusters (Slurm/SSH), or on cloud GPUs via [[entities/modal-labs|Modal]]. It maintains persistent Python and R kernels so variables, dataframes, and loaded models stay in memory across sessions. The agent automatically manages environments per analysis, writes batch scripts, and submits and monitors jobs over SSH.

### Domain Coverage
The workbench spans genomics, single-cell analysis, proteomics, structural biology, and cheminformatics. It connects to over 60 scientific databases and integrates protein language models including Evo 2, Boltz-2, and OpenFold3. Scientists can save analysis pipelines as reusable skills and connect lab instruments via connectors.

## Modal Integration

When local compute is insufficient, workloads automatically route to Modal's cloud infrastructure. This enables virtual screening campaigns that fan out across hundreds of concurrent GPUs, as well as heterogeneous workflows — CPU for alignment and preprocessing, GPU for structure prediction. Shared volumes provide persistent access to sequencing datasets, protein databases, and model checkpoints. New users receive $30 in free Modal compute.

## Pricing and Plans

Claude Science is available on Pro, Max, Team, and Enterprise plans. Academic and nonprofit labs can access it through the Claude Team plan for research labs. Enterprise deployments include SSO, SCIM provisioning, custom roles, and usage analytics.

## Notable Endorsements

- **Mike Nichols, Manifold Bio**: "With Claude Science I can go from raw data to a publication-quality figure in a single session."
- **Iain Cheeseman, MIT**: "Claude Science is enabling analyses that simply wouldn't have been feasible for me as a non-computational biologist."
- **Prasad Shirvalkar, UCSF**: "The most impressive AI-integrated scientific computing environment I have encountered."
- **Stephen Francis, UCSF**: "Immediately found a laboratory virus contaminant in our bulk RNA-seq data. We spun our wheels on this for the better part of a year."

## Related Pages

- [[entities/anthropic]] — Creator of Claude Science and the underlying Claude model family
- [[entities/modal-labs]] — Cloud compute partner providing scalable GPU infrastructure
- [[concepts/claude/fable-5]] — Claude model capabilities that power the scientific workbench
- [[concepts/computer-use]] — Anthropic's computer interaction paradigm, extended here for scientific computing
- [[concepts/claude-code/claude-code]] — Claude Code, Anthropic's coding agent with overlapping tool-use patterns
