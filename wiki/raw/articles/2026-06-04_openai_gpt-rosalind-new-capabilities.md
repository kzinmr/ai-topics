# Introducing new capabilities to GPT-Rosalind

**Source:** OpenAI Blog — June 4, 2026
**URL:** https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind
**Archived:** 2026-06-04

---

## Summary

OpenAI announced a new model update to the GPT-Rosalind series, purpose-built for life sciences research at enterprise scale. The updated model combines GPT-5.5's agentic coding and tool-use capabilities with stronger model intelligence in core drug-discovery domains such as medicinal chemistry and genomics, while advancing performance across broader life sciences analysis, design, and experimental workflows.

GPT-Rosalind is now available in research preview to eligible organizations globally through OpenAI's trusted-access deployment structure.

## Key New Capabilities

### LifeSciBench — New Expert-Judged Evaluation

OpenAI designed LifeSciBench, an externally expert-judged benchmark focused on foundational aspects of life sciences research. Unlike existing benchmarks that evaluate a single component of model performance or biological domain in isolation, LifeSciBench takes an end-to-end view by drawing tasks from six workflow areas:

1. **Evidence handling** — Extracting, reconciling, and auditing scientific evidence from papers, figures, tables, and experimental records.
2. **Analysis** — Quantitative and computational interpretation of biological data, including QC, statistical modeling, omics analysis, imaging, and assay readouts.
3. **Design and optimization** — Designing or improving biological molecules, experiments, constructs, or candidates while predicting properties such as activity, stability, specificity, or developability.
4. **Scientific reasoning** — Mechanistic thinking, hypothesis ranking, causal interpretation, and root-cause diagnosis from incomplete or conflicting scientific evidence.
5. **Validation and operations** — Practical lab and workflow execution, including controls, troubleshooting, protocol design, batch QC, and pass/fail operational decisions.
6. **Translation and communication** — Synthesizing findings into scientific communications.

### Stronger Scientific Reasoning

#### Medicinal Chemistry (MedChemBench)
- GPT-Rosalind achieves **industry-leading performance** in medicinal chemistry
- MedChemBench evaluates: multimodal chemical structure understanding; structure-activity relationship (SAR); prediction of drug potency, toxicity, and ADME; multiparameter lead-optimization decision-making; and retrosynthesis
- **GPT-Rosalind: 27.5% vs GPT-5.5: 25.1%** (7.2% fewer tokens)

#### Genomics and Quantitative Biology (GeneBench)
- Agentic evaluation on long-horizon, end-to-end analysis in genomics and quantitative biology
- Tests whether an agent can plan valid analysis, QC, modeling, and corrections given realistic scientific data
- Domains: functional genomics, spatial transcriptomics, proteomics, epigenomics, applied genetics
- **GPT-Rosalind: 21.6% vs GPT-5.5: 20.4%** (31% fewer tokens)

#### Real-World Lab Work (LabWorkBench)
- New evaluation testing ability to help scientists conducting wet lab work
- Tests linking perturbations to experimental outcomes in real wet lab protocols
- Data is proprietary and thus uncontaminated
- **GPT-Rosalind: 63.2% vs GPT-5.5: 55.8%** (5.3% fewer tokens)

### From Reasoning to Executed Workflows

OpenAI built two new plugins to extend GPT-Rosalind's intelligence with a practical execution layer:

1. **Life Sciences Research** plugin — Sourced evidence retrieval and biological interpretation
2. **Life Sciences NGS Analysis** plugin — Bioinformatics execution

Together these bring sourced evidence retrieval, biological interpretation, and bioinformatics execution into the same workspace, helping researchers connect external evidence with internal omics analyses while preserving artifacts and provenance.

All users can access both plugins through Codex. Qualified GPT-Rosalind enterprise users can additionally use GPT-Rosalind to power these plugins.

**Interactive viewers** were added for biologically native file types (sequence, alignment, and structure viewers), keeping scientists close to the evidence as GPT-Rosalind reasons across a workflow.

## Expanded Access

- **Global expansion** to eligible organizations through trusted-access deployment
- Organizations must be conducting legitimate scientific research with clear public benefit, have strong governance and safety oversight, and controlled access with enterprise-grade security
- **Novo Nordisk partnership**: Leveraging GPT-Rosalind to help scale medical research, analyzing complex datasets, uncovering patterns, and testing hypotheses more quickly
- **OpenAI managed workspace**: Now offered for qualified organizations without an Enterprise account

## Rosalind Biodefense

OpenAI is applying life sciences AI to high-impact public-benefit work including biodefense. Through Rosalind Biodefense and the trusted-access deployment model, frontier biological capabilities are placed in the hands of researchers, institutions, and defenders working to improve human health and strengthen societal resilience.

## Case Study Examples (from article)

The article included detailed examples of GPT-Rosalind's capabilities:
- **AZR-1142 drug candidate evaluation**: GPT-Rosalind declined to advance a drug candidate after identifying data discrepancies (113 vs 72 gene-count discrepancy, conflicting treatment conditions, VEGFR2-selectivity contradictions)
- **Antibody engineering**: Provided detailed bispecific antibody design guidance and Fc engineering recommendations (e.g., A330L/S239D/I332E variants) for improved ADCC
- **ELISA assay troubleshooting**: Systematic analysis of cortisol competitive ELISA U-shaped rebound artifacts, CBG/cortisol-binding-globulin interference, and TR-FRET conversion risks
- **DMD gene therapy evaluation**: Critical assessment of micro-dystrophin gene therapy data including age-window confounding, nNOS-binding site deletion, and immune safety concerns

## Related Articles
- Original GPT-Rosalind announcement (April 16, 2026): https://openai.com/index/introducing-gpt-rosalind/
- Rosalind Biodefense (May 29, 2026): https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/
