---
title: "LoRA Speedrun"
created: 2026-07-20
updated: 2026-07-20
type: concept
tags:
  - lora
  - fine-tuning
  - benchmark
  - peft
  - training-efficiency
  - nanogpt-speedrun
  - hn-popular
  - open-source
sources:
  - raw/articles/2026-07-18_lora-speedrun-leaderboard.md
---

# LoRA Speedrun

LoRA Speedrun is a public wall-clock leaderboard and adversarial arena for **LoRA fine-tuning techniques**, created by Saivineeth147 and launched on July 18, 2026. It applies the [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt) speedrun philosophy to parameter-efficient fine-tuning: a frozen task, frozen hardware, and a public leaderboard of wall-clock records, with every record independently re-verified before it counts.

**Repository**: [Saivineeth147/lora-speedrun](https://github.com/Saivineeth147/lora-speedrun) (MIT license, 72 stars at launch). [HN discussion](https://news.ycombinator.com/item?id=48974325): 89 points, 15 comments.

## Motivation

[[concepts/peft-lora-and-qlora|LoRA/QLoRA]] is how most real-world fine-tuning actually happens, and the technique space has exploded — DoRA, rsLoRA, PiSSA, LoRA+, NEFTune, Unsloth kernels, rank-adaptive methods — but there was no adversarial, apples-to-apples arena where these ideas could race each other in public. Papers report numbers on different models, data, and hardware, making results incomparable.

The nanoGPT speedrun fixed this problem for pretraining and produced real science (the Muon optimizer came out of it). LoRA Speedrun does the same for [[concepts/fine-tuning|parameter-efficient fine-tuning]]: one frozen task, one GPU, wall-clock time, and receipts required.

## How It Works

### The Tracks

Two frozen tracks use deliberately different model families and task types, so a technique only proves general by winning on both:

| | Track 1 | Track 2 |
|---|---|---|
| **Base model** | Qwen/Qwen2.5-1.5B | HuggingFaceTB/SmolLM2-1.7B |
| **Task** | GSM8K math → ≥ 57.0% exact-match | SQuAD v1.1 QA → ≥ 75.5% EM |
| **Hardware** | 1× L40S (48 GB), Modal sandbox | same |
| **Constraint** | adapter-only, ≤ 30M trainable params | same |
| **Metric** | Training wall-clock. Lower wins. | same |

Participants control everything else: LoRA rank and placement, quantization, learning-rate schedules, sequence packing, data subset selection and ordering, custom kernels, and when to stop.

### Verification Protocol

Records go through a rigorous verification pipeline:

1. **PR submission**: Training script, config, notes, and self-reported numbers.
2. **Automated CI**: Static validation plus a Claude-based security screen (exfiltration attempts, network use, harness tampering, test-set contact) posted publicly.
3. **Maintainer review**: A maintainer reviews the code, then triggers `/verify`.
4. **3-seed re-run**: The submission is run **3× with fresh seeds** in a network-blocked Modal sandbox on the spec L40S. All 3 runs must clear the target; official time is the mean.
5. **Integrity audit**: The harness audits adapter param count and re-verifies model/data content hashes (anti-tampering).
6. **Public report**: Verification report posted on the PR and committed to `records/verifications/`.

Attempting and verifying are free: official timing runs use Modal's free monthly compute credits, so anyone can compete and anyone can re-verify any record with one command.

### Current Records

| # | Date | Author | Train time | Accuracy | Technique |
|---|------|--------|-----------|----------|-----------|
| 0 | 2026-07-18 | Saivineeth147 | 11m 57s | 59.4% | Baseline: plain LoRA r=16 on all linear layers, 3 epochs, cosine LR |
| 1 | 2026-07-18 | Saivineeth147 | 6m 05s | 61.1% | Sequence packing + completion-only loss masking, 2 epochs (−49% faster) |

Track 2 baseline (SQuAD/SmolLM2): 11m 08s at 77.5% EM.

## Technique Space

Unclaimed optimization ideas listed in the repo include:

- 1-epoch aggressive-LR schedules
- Data pruning (train on the hardest N examples)
- Block-diagonal/varlen packing attention
- QLoRA NF4 vs bf16 tradeoff
- rsLoRA / DoRA / PiSSA initialization
- LoRA+ (asymmetric LR for A/B matrices)
- NEFTune noise
- Curriculum ordering
- Rank/placement search (MLP-only vs attention-only)
- `torch.compile`, Unsloth kernels, Liger kernels
- Fused cross-entropy
- Smarter warmup for short runs

## Relationship to nanoGPT Speedrun

The project is explicitly modeled on the [[concepts/nanogpt|nanoGPT speedrun]] (modded-nanogpt), which established the frozen-task, frozen-hardware, wall-clock leaderboard format for pretraining. Key parallels:

- Same adversarial, receipts-required verification ethos
- Same wall-clock metric ("what you pay for")
- Same use of Modal for free, reproducible hardware
- Same goal: produce transferable techniques through open competition

## Significance

LoRA Speedrun addresses a gap in the [[concepts/evaluation/ai-benchmarks-and-evals|AI benchmarking]] landscape. Most fine-tuning benchmarks focus on final accuracy; LoRA Speedrun makes **training speed and efficiency** the primary metric. It recognizes that in real-world deployment, wall-clock time and cost are often as important as accuracy, especially as fine-tuning becomes a routine operation in [[concepts/llm-training-fundamentals|LLM training]] pipelines.

The L40S hardware choice is deliberate: it's a consistent datacenter SKU (same AD102 silicon as the consumer RTX 4090), free via Modal's credits, and sandboxed with network blocking for security when running strangers' code.

## Open Questions

- Will techniques that win on Track 1 (GSM8K/Qwen2.5) transfer to Track 2 (SQuAD/SmolLM2) and future tracks?
- Can the 6m 05s record be pushed significantly lower, or is it approaching a hardware-limited floor?
- Will the adversarial format produce genuinely novel optimizations (as the nanoGPT speedrun produced Muon), or will it mainly surface known tricks?
- How does the ≤ 30M trainable parameter constraint interact with quality — is there a tradeoff frontier between speed and accuracy under this cap?
