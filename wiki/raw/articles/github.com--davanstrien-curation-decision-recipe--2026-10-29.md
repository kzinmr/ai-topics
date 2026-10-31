# Curation decision recipe (ultrabert-380m-curation)

- **Source**: https://github.com/davanstrien/curation-decision-recipe (scraped 2026-11-01)
- **Model card**: https://huggingface.co/davanstrien/ultrabert-380m-curation
- **Author**: Daniel van Strien (@vanstriendaniel), Machine Learning Librarian at Hugging Face
- **Announced**: 2026-10-29 on X (tweet 2115826392633880708 + follow-up 2115826395502760135)

## Summary

A fully open **recipe** (data + model + evals) for a small *decision model* used for data curation.
`davanstrien/ultrabert-380m-curation` is a 380M-parameter model fine-tuned from UltraBERT-380M with
gliclass. Given a text and named, typed questions (topic, format, educational value, difficulty, …)
it returns a probability for every option. Zero-shot classification at curation scale.

Core argument: **small decision models live or die by their training data, and few releases say how
that data was built.** The repo documents every source, labeller, licence check, audit and screening
step that went into the training mix, plus the scripts that did it. Van Strien's call to action:
"We've had some cool open model releases. Time for some more data releases!"

## Headline numbers (from the announcement tweet)

- Scored **1,020,000 FineWeb pages in ~19 minutes for ~$5** on Hugging Face Jobs (single GPU job fan-out).
- The model judged ~**25%** of those pages to be product pages.
- **6%** passed a simple "educational, not spam" filter.
- **1 page in 1,020,000** got the top "outstanding" label.
- Training data released with **source, labeller, and licence for every row**.

## Three-command workflow on Hugging Face Jobs

All steps run as `hf jobs uv run` UV scripts whose PEP 723 headers carry `[tool.hf-jobs]` settings
(GPU type, timeout, token) — a laptop only launches the work; data, mixes, evals and checkpoints
live in Hugging Face storage buckets mounted into each job.

1. **Curate a dataset in one command** — `inference/curate.py` reads a text column from any Hub
   dataset, asks four curation questions about every row, pushes a dataset with the answers
   (`scored`) and an example filter (`subset`). Default hardware `a10g-small`; ~20 rows/s on l4x1,
   ~150 rows/s on `rtx-pro-6000` (recommended for ≥100k rows).
2. **Curate millions of pages over several Jobs** — `inference/examples/datatrove_curation.py` is a
   datatrove pipeline run locally; it launches one GPU Job per task and writes to a bucket. This is
   the path that scored 1,020,000 FineWeb pages in ~19 min / ~$5. Model card covers the "System One"
   API (`jev_api.py`) and a packed batch scorer (`fast_inference.py`).
3. **Train from the released data** — `data/release_to_jsonl.py` converts the released dataset to
   trainer input; `train/gliclass_ub_train.py` trains on one GPU Job
   (`--encoder dmis-lab/UltraBERT-380M --single-label-loss softmax_ce --encoder-lr 2e-5
   --others-lr 4e-5 --max-steps 1200`). A bucket mounted at `/b` carries data between jobs.

For agents: the repo directs "start with AGENTS.md".

## Follow-up application: Prelinger moments (2026-10-31)

Van Strien applied the decision-model idea to film discovery:
https://huggingface.co/spaces/davanstrien/prelinger-moments-space — search 1,864 public-domain
Prelinger Archive films by caption, then ask a **yes/no question**; **Liquid AI's d1-2B** decision
model checks 3 frames per result clip and jumps to one it labels *yes* (example query: "anyone
wearing a mask?"). Demonstrates the same decision-model pattern (VLM captions + cheap binary
frame-level verifier) outside text curation.

## Related

- [[entities/daniel-van-strien]]
- [[entities/liquid-ai-lfm3]] (Liquid AI decision-model family, incl. d1-2B)
- [[concepts/huggingface-jobs]]
- [[concepts/uv-scripts-for-ai]]
