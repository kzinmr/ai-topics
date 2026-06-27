---
title: "DeepSeek Open-Sources DeepSpec/DSpark Inference Optimizations — HN Discussion"
source: "hn-algolia"
source_url: "https://news.ycombinator.com/item?id=48696585"
external_url: "https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf"
github_url: "https://github.com/deepseek-ai/DeepSpec"
hn_points: 241
hn_comments: 50
date: 2026-06-26
date_ingested: 2026-06-27
type: raw_article
tags: [deepseek, inference, optimization, open-source, deepspec, dspark, llm-serving]
---

# DeepSeek Open-Sources DeepSpec/DSpark Inference Optimizations

## Source
- URL: https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf
- GitHub: https://github.com/deepseek-ai/DeepSpec
- HN Points: 241
- HN Comments: 50

## Summary
DeepSeek open-sourced DeepSpec, an inference optimization framework achieving 60–85% faster generation for LLMs. The release includes DSpark, a distributed inference engine that optimizes serving throughput.

## GitHub README (DeepSpec)
```
# DeepSpec

DeepSpec is a full-stack codebase for training and evaluating draft models for speculative decoding. It contains data preparation utilities, draft model implementations, training code, and evaluation scripts.

## Environment

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Data preparation additionally requires an inference engine to serve the target model when regenerating answers; see [scripts/data/README.md](./scripts/data/README.md) for details.

## Workflow

Run the stages in order — each stage's output feeds the next:

1. **Data Preparation** — download prompts, regenerate target answers, and build the target cache.
2. **Training** — train a draft model against the cached target outputs.
3. **Evaluation** — measure speculative-decoding acceptance on benchmark tasks.

## Data Preparation

See [scripts/data/README.md](./scripts/data/README.md) for the step-by-step data pipeline:

1. download and split training data,
2. regenerate answers,
3. prepare the target cache (storage warning: this can be very large — roughly 38 TB for the default `Qwen/Qwen3-4B` setting).

## Training

```bash
bash scripts/train/train.sh
```

`train.sh` launches `train.py`, which spawns one worker per visible GPU. Select the algorithm and target model by pointing `config_path` at one of the configs under [config/](./config/) (e.g. `config/dspark/dspark_qwen3_4b.py`); see the script header for the full list of configs, how to override `config_path` / `target_cache_dir`, and how to use `--opts` to override individual config fields. Checkpoints are written to `~/checkpoints/<project_name>/<exp_name>/step_*`.

Hardware: the default configs and scripts assume a single node with 8 GPUs. For fewer GPUs, reduce `CUDA_VISIBLE_DEVICES`.


## Evaluation

```bash
bash scripts/eval/eval.sh
```

`eval.sh` runs `eval.py` against a trained draft checkpoint over the speculative-decoding benchmarks in [eval_datasets/](./eval_datasets/) (gsm8k, math500, aime25, humaneval, mbpp, livecodebench, mt-bench, alpaca, arena-hard-v2). Set:

- `target_name_or_path` — the target model the draft was trained against (e.g. `Qwen/Qwen3-4B`),
- `draft_name_or_path` — the draft checkpoint, e.g. `~/checkpoints/deepspec/dspark_block8_qwen3_4b/step_latest`.

## Supported Algorithms

Currently, DeepSpec includes three draft models: [DSpark](./DSpark_paper.pdf), [DFlash](https://arxiv.org/abs/2602.06036) and [Eagle3](https://arxiv.org/abs/2503.01840).

## License

DeepSpec is released under the [MIT License](./LICENSE). It includes code adapted
from third-party projects under their own licenses; see [NOTICE](./NOTICE) for the
full attribution.

## Acknowledgements

DeepSpec builds on the ideas and code of several excellent open-source projects:

- [SpecForge](https://github.com/sgl-project/SpecForge) (Apache-2.0) — the overall training framework and Eagle3 implementation; portions of the Eagle3 modeling, loss, optimizer, attention, and evaluation code are adapted from it. Adapted files carry an in-file attribution comment, and the full notice is recorded in [NOTICE](./NOTICE).
- [DFlash](https://github.com/z-lab/dflash) (MIT) — the DFlash draft-model design and training recipe.
- [Qwen3](https://github.com/QwenLM/Qwen3) and [Gemma](https://github.com/google-deepmind/gemma) — the target model families supported in this repo.

We thank the authors and maintainers of these projects. Contributions of new algorithms are welcome.
```

## HN Discussion Highlights
### Havoc
Nice.<p>Guessing the timing isn&#x27;t accidental. Demonstrated openness vs harsh regulation

### ricardobeat
Presumably this has been in production for a while, and is one of the reasons they were able to dramatically lower prices a month ago?

### Jackobrien
I see a world soon where there’s an extremely wide variety of small models for speculative decoding, unique to use cases, companies, and even individuals.

### preetham_rangu
do they use their OCR, or someone else?

### piterrro
I’ve been using DeepSeek v4 pro for a month now in Kilo Code and its great. Fast, reliable, large context window and cheap as… Did 1,5B tokens this month and cost me 40usd (majority cached, but still).

### rvz
This is just one of many papers DeepSeek have released to be able to serve models at extremely cheap prices, unlike the others taking on &gt;$100B+ of debt in building data centers for the same thing.<p>&gt; As with V4-Flash, we treat this point as an indication that DSpark sustains useful
throughput under an interactivity target that the baseline cannot efficiently support. At matched system capacities, DSpark delivers 57% to 78% faster per-user generation.<p>Reminds me of the flawed solution in scaling servers in 2017 that use memory-intensive technologies by adding even more servers to solve the problem. (It just increases costs.)<p>Rather than doing that, think about which critical parts of your app can be written in a more performant technology.<p>Fast forward to 2026, now you can see

### 2838383838
Must be wonderful to be on the board of OpenAi et al &amp; their PE investors whilst China keeps blowing up these mines under their feet lmao. 
Luckily Korean pension funds will buy all the trash as usual but goddamn you gotta start moving quick or you are gonna need some serious AGI to show you how to offload those bonds

### kamranjon
DeepSeek continues to not only push the boundaries but also publish these incredible papers explaining how they achieved their gains - something the American labs no longer do unfortunately. Chinese labs are doing the most interesting work in AI right now.

### pokot0
I am wondering if this is why they can offer their pro model at ~1&#x2F;4th of the price compared to the other providers offering the same model, and if other providers will be able to do the same in a short timeframe.

### danielabinav160
Would love to see these numbers reproduced on consumer GPUs, not just A100s.

