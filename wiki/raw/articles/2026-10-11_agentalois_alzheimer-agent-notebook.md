# alois · Alzheimer's research notebook

- Source: https://agentalois.com/
- Retrieved: 2026-10-11
- Discovered via: X post by @vincentweisser (Vincent Weisser, Prime Intellect), 2026-10-10, replying to @AgentAlois / @xeophon
- Related: [[entities/florian-brand]] (Florian Brand / @xeophon, Research Engineer at Prime Intellect)

## What it is

"An agent working on Alzheimer's disease, in public. Give it a gene. It reads six public
sources and proposes an experiment: which cell type to perturb, what should change, and what
result would rule the idea out. If it can't make a case, it prints a receipt. Then it tests
its predictions on measured brain cells from the SEA-AD atlas, on donors it hasn't seen."

## Site structure

Sections: Live Predict / Findings / Gym / Agents / Report / Case studies / Receipts.

- **Live**: the agent runs publicly, taking a new gene every 2.5 minutes, testing it and
  commenting on what it sees. Users can type a gene symbol (examples: PLCG2, SORL1, ABCA7,
  BIN1, MS4A6A, APP) to feed it, or ask a question. Output proposal includes cell type,
  direction, molecular readout, functional readout, rule-out, lab request.
- **Predict**: visitors register a prediction (gene, cell type, outcome). The prediction is
  *hashed before the agent reads any data*, then tested on half of the 84 SEA-AD donors and
  checked on the other half — the same protocol used for the agent's own predictions. Failed
  predictions are published with the predictor's name ("the receipt carries your name").
  Each prediction is registered once (first-come).

## Background (as presented on the site)

- Alois Alzheimer described the disease in 1906. Amyloid-clearing antibodies were approved in
  2023 and 2024; they slow cognitive decline modestly but do not stop it.
- GWAS has found 75+ risk loci for late-onset Alzheimer's, many in genes expressed mainly in
  microglia (TREM2, PLCG2, ABI3, SPI1, MS4A6A), others in lipid transport (APOE, ABCA7) or
  endosomal trafficking (BIN1, PICALM, SORL1).
- A testable hypothesis names four things: a gene, a cell type, a direction of perturbation,
  and a measurable readout. Alois produces hypotheses in exactly that form.

## Method

Six scores in [0, 1] combined into a weighted "translation score":

| Score | Source | Measures | Weight |
|-------|--------|----------|--------|
| genetics | Open Targets | genetic association with Alzheimer's | 0.30 |
| literature | PubMed | papers pairing the gene with Alzheimer's, **inverted** | 0.20 |
| cell type | Human Protein Atlas | enrichment in neurons / astrocytes / microglia | 0.15 |
| pathways | Reactome | membership of genetically implicated pathways | 0.13 |
| chemistry | Open Targets | small-molecule / antibody tractability | 0.12 |
| trials | ClinicalTrials.gov | prior Alzheimer's trials, penalised if stopped | 0.10 |

- Genetics gets the largest weight because genetically supported drug targets are ~2x as
  likely to reach approval (Nelson et al., Nature Genetics 2015).
- Literature score is inverted so heavily-studied genes rank low (APP scores 0.00).
- Direction is *not* taken from drug mechanisms (e.g. neprilysin inhibitors are approved for
  heart failure, but inhibiting neprilysin would be the wrong direction for amyloid-β). Until
  the atlas supplies a measured direction, each proposal asks for both knockdown and
  overexpression.
- The six findings are combined into a single 1,024-dimensional vector by **circular
  convolution (holographic reduced representation)**: each finding bound to a role vector and
  summed; any finding recoverable by unbinding with its role. Findings scored absent/against
  are listed as *dissent*.

## Validation

Predictions are tested against measured brain cells from the **SEA-AD brain atlas**
(Gabitto et al., Nature Neuroscience 2024 — microglia states in human middle temporal gyrus;
Micro-PVM_3 is the disease-associated microglial state that increases with pathology),
on held-out donors (88-donor split, 84 used; half test / half check).

## Notes

- Public "receipts" culture: failures are recorded publicly, including visitor predictions.
- Notable as an example of a scientific-discovery agent with an explicit anti-overfitting and
  anti-cherry-picking protocol (pre-registration by hash, held-out donors, rule-out criteria).
