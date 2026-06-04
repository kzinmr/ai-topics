---
title: GPT-Rosalind
created: 2026-06-04
updated: 2026-06-04
type: concept
tags: [model, gpt, openai, biotech, frontier-models, announcement, benchmark, evals, reasoning]
sources: [raw/articles/2026-06-04_openai_gpt-rosalind-new-capabilities.md]
---

# GPT-Rosalind

GPT-Rosalind is OpenAI's model series purpose-built for **life sciences research** at enterprise scale. Named after Rosalind Franklin (DNA crystallographer), it combines GPT-5.5's agentic coding and tool-use capabilities with domain-specialized intelligence in drug-discovery areas including medicinal chemistry, genomics, and quantitative biology.

**First announced:** April 16, 2026 [[raw/articles/2026-06-04_openai_gpt-rosalind-new-capabilities.md#related-articles]]  
**New capabilities update:** June 4, 2026  
**Status:** Research preview, trusted-access deployment to eligible organizations

## What It Is

GPT-Rosalind is not a general-purpose model but a **domain-specialized frontier model** focused on the full life sciences research lifecycle. It is available only through OpenAI's trusted-access deployment structure to organizations conducting legitimate scientific research with clear public benefit, strong governance, and enterprise-grade security.

The model powers a broader ecosystem:
- **GPT-Rosalind model** — The core intelligence, available to qualified enterprise customers
- **Life Sciences Research plugin** — Sourced evidence retrieval and biological interpretation (available to all Codex users)
- **Life Sciences NGS Analysis plugin** — Bioinformatics execution (available to all Codex users)
- **Interactive viewers** — Sequence, alignment, and structure file viewers in Codex
- **Rosalind Biodefense** — Application of the same capabilities to biodefense and public health

## Capabilities (June 2026 Update)

### LifeSciBench Evaluation Framework

OpenAI introduced LifeSciBench, an expert-judged benchmark covering six workflow areas:

| Area | Description |
|------|-------------|
| Evidence handling | Extracting, reconciling, auditing scientific evidence from papers, figures, tables, records |
| Analysis | Quantitative interpretation of biological data (QC, statistics, omics, imaging, assays) |
| Design & optimization | Designing/improving molecules, experiments, constructs; predicting properties |
| Scientific reasoning | Mechanistic thinking, hypothesis ranking, causal interpretation, root-cause diagnosis |
| Validation & operations | Lab/workflow execution, controls, troubleshooting, protocol design, pass/fail decisions |
| Translation & communication | Synthesizing findings into scientific communications |

### Benchmark Performance vs GPT-5.5

| Benchmark | Domain | GPT-Rosalind | GPT-5.5 | Token Savings |
|-----------|--------|-------------|---------|---------------|
| MedChemBench | Medicinal chemistry | **27.5%** | 25.1% | 7.2% fewer |
| GeneBench | Genomics/quantitative biology | **21.6%** | 20.4% | 31% fewer |
| LabWorkBench | Wet lab troubleshooting | **63.2%** | 55.8% | 5.3% fewer |

Key pattern: GPT-Rosalind **outperforms GPT-5.5 across all benchmarks while using fewer tokens** (5-31% token reduction), suggesting both improved accuracy and efficiency through domain specialization.

### Medicinal Chemistry

GPT-Rosalind achieves industry-leading performance on MedChemBench which evaluates:
- Multimodal chemical structure understanding
- Structure-activity relationship (SAR) analysis
- Prediction of drug potency, toxicity, and ADME properties
- Multiparameter lead-optimization decision-making
- Retrosynthesis

### Genomics and Quantitative Biology

GeneBench evaluates agentic performance on long-horizon quantitative tasks across:
- Functional genomics
- Spatial transcriptomics
- Proteomics
- Epigenomics
- Applied genetics

### Real-World Lab Work

LabWorkBench uses proprietary (uncontaminated) data to test the model's ability to link perturbations to experimental outcomes in wet lab protocols, for troubleshooting and optimization.

## From Reasoning to Execution

GPT-Rosalind integrates with Codex as a dynamic workbench. Key innovations:
- **Plugins** bridge intelligence with repeatable scientific workflows, preserving artifacts and provenance
- **Interactive viewers** keep scientists close to evidence while GPT-Rosalind reasons across workflows
- Supports biologically native file types: sequence, alignment, and structure

## Deployment Model

- **Trusted-access structure**: Only organizations with legitimate scientific research, clear public benefit, strong governance and security
- **OpenAI managed workspace**: Available for qualified organizations without an Enterprise account
- **Partner**: Novo Nordisk is using GPT-Rosalind to scale medical research, helping researchers analyze complex datasets and test hypotheses more quickly

## Case Study Examples

The June 2026 article included detailed demonstrations:
- **Drug candidate evaluation**: Declined to advance AZR-1142 after identifying data discrepancies (gene-count mismatch, conflicting conditions, selectivity contradictions)
- **Antibody engineering**: Provided bispecific antibody design and Fc engineering recommendations (A330L/S239D/I332E) for ADCC improvement
- **ELISA troubleshooting**: Systematic analysis of cortisol competitive ELISA artifacts, CBG interference, TR-FRET risks
- **Gene therapy assessment**: Critical evaluation of micro-dystrophin therapy data including age-window confounding and structural limitations

## Community Reaction

HN discussion on the original April 2026 announcement (102 points, 30 comments):

- **Gated access criticism**: Limited to qualified organizations, not broadly available
- **Naming controversy**: Some objected to commercial use of Rosalind Franklin's name posthumously
- **Benchmark selectivity**: Critics noted comparisons only against GPT-5.4 default (not Pro) and exclusion of Anthropic models; one commenter cited a project achieving 92% on BixBench with Opus 4.6 + 200 skills
- **Defense**: Supporters argued LLMs are actively used in real research (hypothesis testing, data analysis, brainstorming), and GPT-Rosalind is a natural evolution
- **Plugin accessibility noted**: Life Sciences Plugin available to all Codex users, not restricted to GPT-Rosalind enterprise customers

## Related Pages

- [[entities/openai]] — OpenAI company page
- [[entities/gpt-5.5]] — Base model powering GPT-Rosalind's agentic capabilities
- [[raw/articles/2026-06-04_openai_gpt-rosalind-new-capabilities.md]] — Full raw article
