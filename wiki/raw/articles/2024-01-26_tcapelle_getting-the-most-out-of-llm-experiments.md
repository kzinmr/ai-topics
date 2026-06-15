---
title: "Getting the Most Out of Your LLM Experiments — Thomas Capelle (2024-01-26)"
author: Thomas Capelle
date: 2024-01-26
date_ingested: 2026-06-15
url: ""
source: "Hamel Husain's ML/LLM workshop series"
type: article
tags:
  - experiment-tracking
  - fine-tuning
  - training
  - evaluation
  - post-training
  - lora
  - open-source
  - mistral
transcript: transcripts/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments-lecture.md
---

# Getting the Most Out of Your LLM Experiments — Thomas Capelle

**Source:** Hamel Husain's ML/LLM workshop series, Jan 26, 2024
**Speaker:** Thomas Capelle (Weights & Biases ML Engineer; axolotl/torchtune integrations contributor)
**Lecture transcript:** [[transcripts/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments-lecture|Full Transcript]]

## Summary

Thomas Capelle demonstrates practical experiment tracking workflows for LLM fine-tuning using Weights & Biases, drawing on real community projects from the workshop Discord. He covers debugging training anomalies (loss spikes from out-of-distribution tokens), ablation studies on Mistral 7B (pruning 75% of layers and recovering via SFT+DPO), the limits of loss as a quality proxy, and introduces W&B Weave for LLM tracing and evaluation — demonstrated through an NYT Connections puzzle-solving experiment.

## Key Topics

- **Experiment tracking for fine-tuning**: W&B integration with axolotl and HuggingFace Trainer — YAML configs logged as artifacts for full reproducibility, workspace views for different training phases, run comparison tables for diff inspection
- **Loss as a proxy — limitations**: Loss indicates things going wrong during training, but 5 fine-tunings with slightly different hyperparameters can produce nearly identical loss while having different quality. Manual sample inspection and custom eval datasets are essential.
- **Debugging training spikes**: Patching the HF Trainer step method to decode batches at loss spike points, logging per-sample loss instead of mean, identifying out-of-distribution tokens (Korean characters in English-only data)
- **Model pruning & recovery (Mistral 7B ablation)**: Removing 75% of layers from Mistral 7B, then recovering via SFT+DPO (Zephyr recipe) with only 1B tokens budget. The pruned model worked as a speculative decoding drafter and surprisingly good embedding model.
- **W&B Weave for LLM tracing**: Decorator-based function tracing (`@weave.op()`), nested call visualization, evaluation dashboards with version tracking and per-sample inspection
- **Automated eval pipelines**: Push checkpoint → auto-trigger SFT → DPO → Eval Harness → results flow to dashboard

## Key Insights

1. **YAML as first-class citizen**: Having the raw training config logged as an artifact (not just parsed parameters) enables exact experiment reproduction — "pull the YAML and rerun the experiment"
2. **Decode your batches**: When debugging loss spikes, decode the actual token IDs being fed to the model. Abstractions (tokenizer, batching, multi-packing in axolotl) can hide data issues.
3. **Skip bad batches**: Patch the training loop to skip optimizer steps on anomalous batches. Harder with high-level libraries (HF Trainer + axolotl), easier with torchtune or pure PyTorch.
4. **Pruned models have unexpected utility**: A Mistral 7B with 75% layers removed, recovered with minimal instruction tuning, turned out useful for both speculative decoding and embeddings at a Mistral Hackathon.
5. **Run comparison "diff only" mode**: LLM training configs have 200+ parameters. The diff-only toggle in W&B's run comparison table shows only what changed between experiments.
6. **Weave as LLM debugger**: Function-level tracing shows nested call hierarchies with inputs/outputs — like a debugger for LLM applications, with version tracking and evaluation dashboards.

## Related

- [[transcripts/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments-lecture|Full Lecture Transcript]]
- [[entities/thomas-capelle|Thomas Capelle]] — speaker
- [[entities/hamel-husain|Hamel Husain]] — host of the workshop series
- [[concepts/post-training/_index|Post-Training]] — fine-tuning techniques
- [[transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture|Why Fine-Tuning is Dead — Emmanuel Ameisen]] (same course, 2 days earlier)
