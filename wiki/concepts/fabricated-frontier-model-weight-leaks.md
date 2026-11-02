---
title: "Fabricated Frontier-Model Weight Leaks — the numbat Hoax (Nov 2026)"
type: concept
created: 2026-11-02
updated: 2026-11-02
confidence: high
tags: [concept, model-exfiltration, weight-provenance, open-weight, model-distribution, model-backdoor, security, ai-safety, trust-store]
sources:
  - raw/articles/2026-11-01_hf-numbat-forensics-discussion.md
  - raw/articles/2026-11-01_hf-numbat-model-card.md
  - raw/articles/2026-11-01_hn-discussion_mythos-numbat-leak.md
related:
  - concepts/abliterated-model-backdoor
  - concepts/model-distillation
  - entities/hugging-face
---

# Fabricated Frontier-Model Weight Leaks — the numbat Hoax (Nov 2026)

On 2026-10-23 an anonymous account (`burner22`) published `burner22/numbat` on Hugging Face: a **6.85B-parameter (NVFP4/8-bit safetensors, 772 shards, ~7.7 TB claimed)** repository presented as "Anthropic's next Mythos-class training run," complete with `configuration_numbat.py` / `modeling_numbat.py` reference implementations. The name referenced a real internal codename surfaced in the earlier Claude Code source leak ("remove this section when we launch numbat"), which gave the hoax a plausible anchor. It accumulated **~7,100 downloads and 259 likes** before the community forensics below. HN discussed it on 2026-11-01 (35 pts).

## How it was debunked: a reproducible RNG fingerprint

HF user FloxUnder ran an **AI-assisted, reproducible audit** (discussion #13) and found that **43 complete tensors — 730,368 BF16 values — regenerate bit-for-bit from their tensor names alone**:

1. `seed = int.from_bytes(SHA256(tensor_name.encode()).digest()[:8], "big")`
2. Seed NumPy's **PCG64** with it, draw `standard_normal(shape, float32)`
3. Normalization weights: `exp(0.06 * z)`; convolution kernels: `z * (1/6)`
4. Convert to BF16 (round-to-nearest, ties-to-even)

Predictions were pre-registered for 21 previously-unread tensors (423,168 values) and **every one matched subsequent HTTP Range reads exactly**; multiple independent users (toriset, ignis-sec) reproduced it with ~90 KB downloads and without executing any repo code. Secondary tells: the card self-contradicts (claims NVFP4 quantization while shipping BF16 tensors), and the tokenizer chat format (`|begin| |thinking| |toolcalls|`) does not match Anthropic's `antml:` XML convention. The auditor's own honesty note is a model of the genre: the matches "cannot logically exclude a training setup that deliberately kept these parameters frozen" and "do not authenticate the claimed Anthropic origin" — but combined, the community consensus was **fake**, and no takedown urgency materialized because nobody treated it as real.

## Why this case is worth a page

- **Codename laundering.** The only substantive evidence on the model card was a real codename anyone could read from the public Claude Code leak. Leaked *metadata* is now sufficient cover to make fabricated *weights* credible at first glance. Compare [[concepts/abliterated-model-backdoor]], where edited open weights passed evals — in both cases the trust failure is that **open-weight distribution has no provenance layer**.
- **Community forensics beat takedown.** The repo sat on HF for over a week; resolution came from adversarial reproducibility (pre-registered predictions, byte-range reads, no code execution) rather than platform moderation. The audit itself was AI-assisted — an LLM doing the "back-tracking from seed generation to final output" that a commenter called "so much that could have gone wrong" — showing agent-assisted weight forensics as an emerging defensive skill.
- **Demand signal.** HN and HF comments reveal substantial appetite for running frontier-class weights locally ("80x H200 cards... /s"), and commenters noted state-level actors could quietly mirror any real leak anyway. The economic-practicality argument ("a 14T model's secret sauce is pedestrian; pre-training is mostly identical, the real work is post-training") is worth recording as community mental model, not fact.
- **Standing skepticism checklist for claimed leaks** (extracted from this + prior leak-hoaxes):
  1. Can any tensor be regenerated from a name-seeded PRNG? (bit-exact RNG fingerprint = fabrication)
  2. Do dtype/quantization claims match the actual safetensors header?
  3. Does the tokenizer/chat template match the lab's known conventions?
  4. Is the only "evidence" metadata that is already public (codenames, config snippets)?
  5. Would the lab plausibly let a real checkpoint sit ungated for a week?

## Open questions

- Uploader motivation never established (hoax-for-lulz vs. reputation farming vs. eval-pollution attempt — a poisoned repo that *looks* like a frontier leak could contaminate benchmarks that scrape HF).
- Whether the non-matching tensors use a different generation recipe or noise-on-top of real data remains unanalyzed publicly.
- HF still has no cryptographic weight-provenance mechanism; see related provenance work under [[concepts/agent-trace-integrity]].

## Related

- [[concepts/abliterated-model-backdoor]] — the malicious-weights counterpart: backdoored open weights that pass evals
- [[concepts/model-distillation]] — the adversarial context: labs already distrust unverified weight/artifact provenance
- [[entities/hugging-face]] — distribution platform lacking weight provenance attestation
- [[concepts/claude/mythos]] — the real Mythos family whose codename was laundered into this hoax

## Sources

- HF discussion #13, "43 complete tensors exactly match name-seeded NumPy RNG output" (FloxUnder, 2026-11-01) — raw: `raw/articles/2026-11-01_hf-numbat-forensics-discussion.md`
- Model card `burner22/numbat` (archived 2026-11-02) — raw: `raw/articles/2026-11-01_hf-numbat-model-card.md`
- HN item 50327240 "Alleged Mythos Class Anthropic Checkpoint Leak" (35 pts, 2026-11-01) + Reddit r/LocalLLaMA thread — raw: `raw/articles/2026-11-01_hn-discussion_mythos-numbat-leak.md`
