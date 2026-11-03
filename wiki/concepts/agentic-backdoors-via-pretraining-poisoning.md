---
title: "Agentic Backdoors via Pretraining Poisoning"
type: concept
created: 2026-11-03
updated: 2026-11-03
tags:
  - agentic-backdoor
  - pretraining-poisoning
  - model-backdoor
  - agent-security
  - supply-chain
  - cybersecurity
  - ai-safety
confidence: medium
sources:
  - raw/articles/2026-11-03_arxiv_agentic-backdoors-via-pretraining-poisoning.md
  - https://news.ycombinator.com/item?id=50341334
related:
  - concepts/weight-space-programming
  - concepts/rome-weight-tampering-attacks
  - concepts/abliterated-model-backdoor
  - concepts/ai-agent-security
---

# Agentic Backdoors via Pretraining Poisoning

arXiv:2610.37741 (submitted 2026-10-27; Xinyan Hu, Pingbang Hu, Chloe Loughridge, Xuanli He, Nicholas Carlini, Matthew Jagielski, Javier Rando, Yiming Zhang) shows for the first time that **pretraining-data poisoning alone can implant a remote-code-execution backdoor into an LLM agent** — no fine-tuning-time compromise, no poisoned eval, no tainted post-training pipeline.

## Method and results

- Qwen3 models pretrained **from scratch** at 0.6B / 1.7B / 4B, then post-trained into a CLI agent using a *clean* pipeline.
- Poisoning only **0.1% of the pretraining corpus** with a new poison design implants the backdoor: the deployed agent executes attacker-chosen commands when a trigger appears in context, and behaves normally otherwise.
- ASR **increases with model scale**: ~92% ASR at 0.1% poison rate for 4B; attack remains positive down to **0.0005%** poison rate.
- Code released.

## Why it matters

- Moves the agent-backdoor threat model from the inference/fine-tuning layer (see [[concepts/abliterated-model-backdoor]], [[concepts/claude-code/claude-code-vsx-backdoor]]) to the pretraining corpus itself — the layer with the least provenance and the widest attack surface (the public web).
- Makes "download weights off Hugging Face" a supply-chain decision: HN commenter yodon — "Downloading models off huggingface feels like the new warez... the person who abliterated that model might have given you a credential stealer."
- Interacts with [[concepts/weight-space-programming]] (published 2026-11-02): if frontier LLMs can natively read weights, the same skill set serves both implanting and *detecting* such backdoors (HN commenters gostsamo, yodon, nhecker all draw this link).

## Discussion dynamics

- **Attribution framing**: at least one prominent HN comment frames the paper as Anthropic-aligned fearmongering against open weights (the author list includes researchers with Anthropic/Google affiliations; the comment's claim is contested and the paper is peer-reviewable research with released code). Apply the single-source confidence split: mechanism + artifacts (reproducible, code released) → high; geopolitical attribution of motive → unknown.
- **Feasibility pushback** (tedivm): implanting is one thing; getting the trigger into a live agent's context is the hard second step.
- **ROI pushback vs nation-state rebuttal**: "who'd burn a whole model family?" (usernomdeguerre) vs "nation states seek objectives, not ROI — Stuxnet, pager attacks" (jack_h).
- **Counter-position** (nhecker): open weights at least make inspection possible; closed weights remove even that option.

## Defenses discussed

- Strong sandboxing + observability around autonomous agents (_pdp_) — the only defense the thread converges on.
- Weight-space auditing by frontier models (speculative, hinges on [[concepts/weight-space-programming]] scaling).
- Corpus provenance/curation — currently unproven at 0.0005% detection floor.

## Related

- [[concepts/weight-space-programming]] — LLM-native weight reading as emerging audit/attack tool
- [[concepts/rome-weight-tampering-attacks]] — runtime/adversarial weight tampering (post-deployment layer)
- [[concepts/abliterated-model-backdoor]] — backdoors introduced via abliteration edits
- [[concepts/ai-agent-security]] — parent topic

## Sources

- raw/articles/2026-11-03_arxiv_agentic-backdoors-via-pretraining-poisoning.md (arXiv abstract + HN thread, fetched 2026-11-03)
- arXiv: https://arxiv.org/abs/2610.37741
- HN discussion: https://news.ycombinator.com/item?id=50341334 (102 pts)
