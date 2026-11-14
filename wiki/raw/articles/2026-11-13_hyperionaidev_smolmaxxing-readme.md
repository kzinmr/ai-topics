---
title: "smolmaxxing: Run the biggest language model you can on the smallest hardware you own"
url: "https://github.com/hyperionaidev/smolmaxxing"
source: "GitHub (hyperionaidev/smolmaxxing, raw README)"
date: 2026-11-13
fetched_at: 2026-11-14T11:25:00+00:00
tags: [github, raw, primary-source]
note: "HN item 50468888 (390 pts). MIT license, 501 stars at capture. Full HN thread at raw/articles/2026-11-13_hyperionaidev_smolmaxxing.md"
---

# 🤏 smolmaxxing

<p align="center"><img src="assets/banner.png" alt="smolmaxxing: run the biggest model you can on the smallest hardware you own. 260K to 80B parameters." width="100%"></p>

<p align="center"><a href="https://hackergit.org/r/hyperionaidev/smolmaxxing"><img src="https://hackergit.org/badge/hyperionaidev/smolmaxxing.svg?style=rank" alt="Hacker News rank via HackerGit" width="250" height="55"></a>
  <a href="https://huggingface.co/hyperionaidev"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-xl.svg" alt="Models on Hugging Face" width="190" height="55"></a></p>

**Run the biggest language model you can on the smallest hardware you own.**

TV boxes, old phones and tablets, single-board computers and routers all have a CPU, some RAM and flash storage that sit idle most of the day. smolmaxxing finds the biggest model each of them can really run, then pushes it further with custom kernels, careful memory use and weights streamed from flash. Every number in this repo was measured on the device itself.

## Three devices so far

| | 📺 Xiaomi TV Box S (3rd Gen) | 📱 iPad Air (2013) | 📲 OnePlus Nord CE 2 (2022) |
|---|---|---|---|
| **Chip** | Amlogic S7D, 4× Cortex-A55 | Apple A7, 2 cores | MediaTek Dimensity 900, 2× Cortex-A78 + 6× A55 |
| **RAM** | 1.9 GB (about 1 GB usable) | 1 GB (about 700 MB usable) | 7.4 GB (about 3 GB free) |
| **OS** | Android 14, no root | iOS 12.5.7, jailbroken | Android 13, no root |
| **Everyday model** | Qwen3.5-2B at **7.7 tok/s** | Bonsai-1.7B (1-bit) at **24-26 tok/s** | Qwen3.6-35B-A3B at **4.9-5.7 tok/s** |
| **Biggest model** | Ling-mini-2.0, 16B, at **5.1 tok/s** | Ling-mini-2.0, 16B, at **2.6-4.5 tok/s** | Qwen3-Next-80B-A3B at **2.6-3.1 tok/s** |
| **Full results** | [docs/tv-box.md](docs/tv-box.md) | [ipad-air/README.md](ipad-air/README.md) | [docs/phone.md](docs/phone.md) |

The TV box and the iPad run 8B and 16B mixture-of-experts models on about 1 GB of RAM, and the phone runs 35B and 80B ones with about 3 GB free. They all keep only part of each model in memory and read the rest from flash as it's needed.

The chart below compares the two 1 GB devices size class by size class; the phone plays in a bigger league, and its results are in [docs/phone.md](docs/phone.md).

<p align="center"><img src="assets/devices.svg" width="760" alt="Best generation speed per size class on the two 1 GB devices: 2B class TV 7.7 (Qwen3.5-2B) vs iPad 23.7 (Bonsai-1.7B, 1-bit); 4B 4.3 vs 9.4; 8B dense 5.2 vs 0.08; 8B MoE 7.2 vs 3.5; 16B MoE 5.1 vs 4.5 with the same cache bias"></p>

More devices (single-board computers, routers, more phones) are coming. The techniques aren't tied to one box: the 1-bit kernel needs only basic NEON, and the flash streaming works on any Linux or Android device with more model than RAM.

**Got a small device?** Run a model on it and [submit your numbers](CONTRIBUTING.md#submit-your-device): we'll add them to the results.

<p align="center"><img src="screenshots/llmui_05_stream.png" width="720" alt="The live token-stream page served by llama-server on the TV box"></p>

## How it works

All of it is a patch on [llama.cpp](https://github.com/ggml-org/llama.cpp). The main ideas:

- **Kernels built for the chip.** A 1-bit lookup-table kernel, repacked 2-bit and ternary formats for the Cortex-A55, and versions of them for the A7, which has no dot-product instructions.
- **Less RAM per model.** Most of a small model's vocabulary is rarely used, so we drop those output rows. On the TV, a "headless" mode also stops the launcher and Google services while a model runs.
- **Experts paged from flash.** A mixture-of-experts model only uses a few experts per token. We keep the popular ones in RAM, read the others from flash on demand and prefetch the next layer's. This is how 8B and 16B models run on 1 GB, and 35B and 80B models on a phone.
- **Streaming for dense models** bigger than RAM, at the flash's full speed.

[docs/how-it-works.md](docs/how-it-works.md) has every technique with its measured gain.

## Try it

The quickest start is a ready-made model file from Hugging Face. The TV box and iPad files need the patched llama.cpp (stock llama.cpp can't load their pruned heads); the phone files load anywhere, but their speeds need the patch's expert pager.

- **TV box or another ARMv8.2 Android device:** [docs/tv-box-setup.md](docs/tv-box-setup.md)
- **Jailbroken iPad on iOS 12:** [ipad-air/README.md](ipad-air/README.md#run-it)
- **Android phone with 8 GB of RAM:** [Qwen3.6-35B-A3B](https://huggingface.co/hyperionaidev/Qwen3.6-35B-A3B-phone-GGUF) (12.3 GB) and [Qwen3-Next-80B-A3B](https://huggingface.co/hyperionaidev/Qwen3-Next-80B-A3B-phone-GGUF) (27.6 GB, two files), set up as in [docs/phone.md](docs/phone.md#running-it).
- **All model files and how to rebuild them:** [docs/models.md](docs/models.md)

## Read more

| Page | What's in it |
|---|---|
| [docs/tv-box.md](docs/tv-box.md) | device #1: every model run on the TV box, speed and quality |
| [ipad-air/README.md](ipad-air/README.md) | device #2: the iPad Air results, setup and scripts |
| [docs/phone.md](docs/phone.md) | device #3: the OnePlus phone, from 16B to an 80B model |
| [docs/how-it-works.md](docs/how-it-works.md) | the kernels, memory tricks, expert pager and streaming engine |
| [docs/models.md](docs/models.md) | downloads for all three devices, rebuild targets and checksums |
| [docs/lessons.md](docs/lessons.md) | what we learned, including what didn't work |
| [EXPERIMENT.md](EXPERIMENT.md) | the full lab notebook: 165 experiments, failures included |

## What's in the repo

| Path | What |
|---|---|
| `patches/` | every change to llama.cpp for the TV box and the phone (the iPad's patch is in `ipad-air/patches/`) |
| `tools/` | model rebuilding, GGUF rewriting, benchmarks and kernel checks |
| `tv-llm-ui/` | the live token-stream chat page and its launcher |
| `ipad-air/` | device #2: iOS 12 build, `smolchat`, deploy and benchmark scripts |
| `bench/` | every chat benchmark (`results.jsonl`) and the raw logs |
| `data/` | vocabulary lists and evaluation texts |
| `tiny-llm-web/` | the first experiment: a 260K-parameter story model |
| `zigcc/` | zig wrappers for cross-compiling static aarch64 binaries |

## Similar projects

Other people running language models on hardware that was never meant for them:

| Project | Hardware | What it runs |
|---|---|---|
| [On-chip LLM on a KV260](https://www.mikeayles.com/blog/on-chip-llm-kv260/) | AMD Kria KV260 FPGA ($250) | a 3.16M-parameter INT4 transformer held entirely in on-chip memory, about 60K tok/s |
| [ps2-llm](https://github.com/xaskasdf/ps2-llm) | PlayStation 2 (294 MHz MIPS, 32 MB RAM) | a 10M-parameter instruct model |
| [iiama2.c](https://github.com/brysontang/iiama2.c) | Nintendo Wii (729 MHz PowerPC, 88 MB RAM) | llama2.c with stories15M, 61.9 tok/s on the GPU |
| [esp32-ai](https://github.com/slvDev/esp32-ai) | ESP32-S3 microcontroller | a 28.9M-parameter model at about 9.9 tok/s |
| [go-pherence](https://github.com/rcarmo/go-pherence) | CPUs with AVX2, NEON or RVV, and NVIDIA GPUs | pure-Go inference for language, speech and vision models |
| [Ryan Seddon on X](https://x.com/ryanseddon/status/2088151404024344870) | Sega Dreamcast, via Windows CE | a language model running under the Dreamcast's Windows CE |

## Star History

<a href="https://www.star-history.com/?repos=hyperionaidev%2Fsmolmaxxing&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hyperionaidev/smolmaxxing&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hyperionaidev/smolmaxxing&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hyperionaidev/smolmaxxing&type=date&legend=top-left" />
 </picture>
</a>

## License

[MIT](LICENSE). The llama.cpp patches are derivatives of [llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT). Model weights keep their own licenses, and the evaluation texts are Wikipedia excerpts (CC BY-SA 4.0).

## Credits

Built on [llama.cpp](https://github.com/ggml-org/llama.cpp) and [llama2.c](https://github.com/karpathy/llama2.c). Models from [Qwen](https://huggingface.co/Qwen), [unsloth](https://huggingface.co/unsloth) (GGUFs and importance matrices), [PrismML](https://huggingface.co/prism-ml) (Bonsai), [inclusionAI](https://huggingface.co/inclusionAI) (Ling-mini-2.0), [tablinum](https://huggingface.co/tablinum) (Moon-Beam), [bartowski](https://huggingface.co/bartowski) and [mradermacher](https://huggingface.co/mradermacher) (GGUFs), Google (Gemma) and [stories260K](https://huggingface.co/karpathy/tinyllamas). The iPad is jailbroken with [Amethyst](https://github.com/staturnzz/amethyst). The banner uses [Archivo](https://fonts.google.com/specimen/Archivo) (SIL OFL) and is rendered by `tools/banner/render.sh`. The 🤏 logo is the pinching-hand emoji from Google's [Noto Emoji](https://github.com/googlefonts/noto-emoji) (Apache 2.0).
