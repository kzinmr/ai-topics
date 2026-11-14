---
title: "Qwen3.8 - How to Run Locally (Unsloth Dynamic V3.1)"
url: "https://unsloth.ai/docs/models/qwen3.8"
source: "Unsloth Documentation"
date: 2026-11-11
fetched_at: 2026-11-14T11:25:00+00:00
tags: [docs, raw, primary-source]
note: "Markdown variant of the GitBook page. HN item 50491980 (151 pts, 2026-11-14)."
---

> For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://unsloth.ai/docs/models/qwen3.8.md).

# Qwen3.8 - How to Run Locally

Guide to running Qwen3.8 quants including Qwen3.8-27B on your local setup.

Qwen3.8-27B is a 27B parameter dense model Qwen, featuring **vision** and reasoning capabilities, a **256K context** window, and runs locally on **17GB RAM/VRAM** setups. Qwen3.8 excels at agentic coding, vision and chat tasks, and can now run via Unsloth GGUFs, NVFP4 and [Unsloth Desktop](#run-qwen3.8-in-unsloth-desktop).

**Nov 11 Update:** Qwen3.8-27B GGUFs now use [Unsloth Dynamic V3.1](/docs/basics/dynamic-3.0-ggufs.md) which improves average accuracy by 5-10% accuracy at comparable sizes including Terminal Bench, DeepSWE and more benchmarks. We're working on an even better version of Dynamic quants which will be applied to **Qwen4** and future models.

{% columns %}
{% column width="50%" %} <a href="/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-guide" class="button primary">Run Qwen3.8 Guide</a><a href="https://unsloth.ai/download" class="button secondary">Download Unsloth</a>

Thank you Qwen for day zero access. Unsloth quants also include:

* **Developer Role Support** for agentic tools like Codex
* [MTP enabled](/docs/models/mtp.md) for fast inference
* **Tool calling:** Improved parsing nested objects to make tools succeed more

Unsloth quants: [Qwen3.8-**27B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)
{% endcolumn %}

{% column width="50%" %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F6aw6IjO7lnYJhSyzXYwq%2Fvolcano%20qwen.gif?alt=media&amp;token=94e56117-d10d-45e8-82dc-3e134b2b9359" alt=""><figcaption><p>Dynamic 4-bit Qwen3.8-27B in Unsloth Desktop</p></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

### Dynamic V3.1 Update (November 11th 2026)

We're excited to release new Qwen3.8-27B GGUFs using our updated [**Unsloth Dynamic**](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) **V3.1 (preview) algorithm** which improves Unsloth quants by 5-10% accuracy at the same size on most benchmarks and is the best in class for most tasks including coding, agentic workloads and general chat.

Most quants from 2bit until 6bit are updated. We found 3bit UD3 quants to do on par with UD3.1, so we do not update them. We are actively working on making all quants better!

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FWf4zRxz4iskzXZcBUQYq%2Ffour(1).png?alt=media&amp;token=0e7bc8b1-6a96-4978-bcbe-227d69705eb2" alt="" width="563"><figcaption></figcaption></figure>

**We ran agentic benchmarks including Terminal Bench 2.1, DeepSWE v1.1**, and general benchmarks like LiveCodeBench v6, GPQA Diamond, MMLU-Pro, AIME25 and many others. We used 256K context lengths for all agentic benchmarks, and 128K for the rest. We followed the same methodology for Qwen3.8-27B as [DeepSeek-V4.1-Flash](/docs/models/deepseek-v4.1-flash.md) and [Qwen3.8-Flash-Next](/docs/models/qwen3.8-next.md) which also utilized our V3.1 preview algorithm.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FAJWlEwcA3LRXIky6AN34%2Fall_no_embedding(1).png?alt=media&amp;token=205c8068-8815-402a-aacf-aa877915be1b" alt=""><figcaption></figcaption></figure>

#### Dynamic V3.1 Full Breakdown

Click below to see full details of benchmarking and more:

<details>

<summary>Click to expand Full details and breakdown</summary>

#### Exllama-v3 considerations

To compare GSQ-RCO and Exllama-v3, we had to exclude the token embedding layer from the x axis, as Exllama-v3 uses BF16 for it.

If you consider the full download size and total RAM usage for Exllama-v3, then adding the BF16 embedding table and including all embedding sizes changes the plots. Our main plots's x axis removes the embedding layer sizes from all quant providers. **However on pure RAM usage and disk space usage vs accuracy, the below plot is the true reflection of actual usage.**

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FOAyvQGNinlCjqTfvInzE%2Fall_file_size(1).png?alt=media&amp;token=71d6a14b-4dd5-4629-9011-c24145c16b41" alt=""><figcaption></figcaption></figure>

We have not investigated why Exllama-v3 keeps token embeddings in BF16, but as the lm\_head is still quantized heavily, the embedding layer might have "absorbed" most of the quantization damage from it. We would be glad to benchmark new Exllama-v3 non BF16 token embedding quants like using 8-bit for example, and see if benchmarks change.

#### GSQ-RCO results are misleading

For LiveCodeBench, GSQ-RCO showed Unsloth UD3 quants doing consistently worse than ISTA's. However we **found the opposite - UD3 quants (our OLD quants) do better than ISTA on LCB on all sizes except the smallest.** UD3.1 further improves on LCB as well.

We approximate that GSQ-RCO used a context budget of 96K, as that best fits the data for the runs we have. At 96K, GSQ-RCO does somewhat do better than UD3, but at 128K, UD3 does much better.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fi7fxu1dfYubjTRlaplQd%2Fq27_lcb_auc_vs_budget.png?alt=media&amp;token=8d364f9a-dcab-4f03-b08a-b1dd149e1ca6" alt=""><figcaption></figcaption></figure>

On another benchmark, for ISTA GSQ-RCO's AIME25 benchmarks, their quants reach 100%, 100%, 100% and 96.7% accuracy recovery. And they said our quants do worse.

Through out investigations, we estimate ISTA only did 1 trial - we did 14 trials, and we show on average the recovery rate is 93% to 96% - not 100% accuracy recovery. **And in fact our UD3 old quants do BETTER on average than their quants on 14 runs vs 1 run of theirs**, so we draw the opposite conclusion if you run the trials more.

We also checked and graded our answers using Math Verify [Dynamic 3.1 GGUFs](/docs/basics/dynamic-3.0-ggufs/dynamic-3.1-ggufs.md) and also LightEval and we find exactly the same conclusions. We also tried greedy decoding (temperature of 0), and this could not get the 100% accuracy recovery ISTA found across multiple greedy runs, as GPUs themselves are non deterministic. That is why you benchmarks should be run multiple times. Greedy decoding is also not representative of real world use cases.

We also checked 96K (which is most likely ISTA's budget) and 128K, and our quants still do on average better.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fbh6wGXtOMWkzqRnfoova%2Fq27_aime25_auc_vs_budget.png?alt=media&amp;token=46081d81-dcf1-4d6f-b30e-6033d33433e6" alt=""><figcaption></figcaption></figure>

#### KLD of Unsloth v3.1 vs v3

We did KLD for multiple domains for Unsloth UD3.1 quants and UD3 quants - we reduce KLD throughout most quants and most domains - we did not replace the 3-bit ones, as we found UD3 to do mostly great, and the accuracy recovery on benchmarks was not significant enough with UD3.1 to warrant an update, so we did not update them.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FKjLQfsZa7dpm50lm4487%2Fq27_kld_v3_vs_v31(1).png?alt=media&amp;token=5bda64f6-c756-4709-8f8c-15b60761e7f2" alt=""><figcaption></figcaption></figure>

#### Benchmark details and setups

We follow the same procedure for all benchmarks as for Qwen3.8-Flash-Next, DeepSeek-V4.1-Flash as well as discussed in [Dynamic 3.1 GGUFs](/docs/basics/dynamic-3.0-ggufs/dynamic-3.1-ggufs.md). We used temperature 1.0, top\_p 0.95, top\_k 20, min\_p 0, no presence or repetition penalty, preserve\_thinking and xhigh reasoning for Qwen3.8-27B.

</details>

### :gear: Usage Guide

#### Qwen3.8-27B Requirements:

Qwen3.8-**27B** 4-bit quants work on 16-19GB VRAM like RTX 5080, 4090 or a Mac with 24GB RAM.\
**Table: Hardware requirements** (units = total memory: RAM + VRAM, or unified memory)

<table><thead><tr><th>1-bit</th><th>2-bit</th><th>3-bit</th><th>4-bit</th><th width="128">6-bit</th><th>8-bit</th><th>BF16</th></tr></thead><tbody><tr><td>7-8 GB</td><td>9-11 GB</td><td>12-14 GB</td><td>16-19 GB</td><td>23-26 GB</td><td>31 GB</td><td>56 GB</td></tr></tbody></table>

{% hint style="info" %}
If you want to use [MTP](/docs/models/mtp.md) for faster inference, prepare to have 1-2GB extra headroom.
{% endhint %}

### Recommended Settings

Qwen3.8-27B is a **hybrid thinking** model with different default settings for thinking and non-thinking modes. Extra high is enabled by default so if you want shorter thinking traces, you can [adjust the thinking effort](#thinking--preserve-thinking):

| Parameter            | Thinking Mode | Instruct (non-thinking) Mode |
| -------------------- | ------------- | ---------------------------- |
| `temperature`        | 1.0           | 0.7                          |
| `top_p`              | 0.95          | 0.80                         |
| `top_k`              | 20            | 20                           |
| `min_p`              | 0.0           | 0.0                          |
| `presence_penalty`   | 0.0           | 1.5                          |
| `repetition_penalty` | 1.0           | 1.0                          |

* **Maximum context window:** `262,144` (can be extended to 1M via YaRN)
* Thinking Mode: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`
* Instruct (or non-thinking) mode: `temperature=0.7`, `top_p=0.80`, `top_k=20`, `min_p=0.0`, `presence_penalty=1.5`, `repetition_penalty=1.0`

### 💡 Thinking + Preserve Thinking

{% columns %}
{% column %}
Qwen3.8 has **Preserve Thinking** which leaves the thinking trace from the previous conversation. This increases the number of tokens you use, but could increase accuracy in continued conversations. [Unsloth](#run-qwen3.8-in-unsloth-desktop) has 'Think' and Preserved Thinking toggles for Qwen3.8 (see right):
{% endcolumn %}

{% column %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FLdgmjRrb5qhpbY9PwYe8%2FScreenshot%202026-08-14%20at%2011.26.15%E2%80%AFAM.png?alt=media&amp;token=6333f5ca-196d-46ae-9efd-2e522014e6db" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

Qwen3.8-27B comes with support for `reasoning_effort`, which can be used to adjust reasoning depth and control cost. These toggles are automatically enabled in Unsloth:

* `xhigh` (default): for complex tasks demanding thorough analysis
* `medium`: balancing accuracy and speed
* `low`: efficient reasoning optimizing for speed and cost
* none

{% hint style="warning" %}
To change[ thinking / reasoning](#how-to-enable-or-disable-reasoning-and-thinking) effort in `unsloth run` or `llama-server`, use `--chat-template-kwargs '{"reasoning_effort":"medium"}'`

If you're on **Windows** Powershell, use: `--chat-template-kwargs "{\"reasoning_effort\":\"medium\"}"`

Change `medium` to your desired reasoning level.
{% endhint %}

## Run Qwen3.8 Guide

You can now run Qwen3.8-27B in llama.cpp and Unsloth Desktop. Feel free to change quantization type.

* Hugging Face: [Qwen3.8-27B-**GGUF**](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) • [Qwen3.8-27B-**NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4)
* ModelScope: [Qwen3.8-27B-**GGUF**](https://www.modelscope.cn/models/unsloth/Qwen3.8-27B-GGUF) • [Qwen3.8-27B-**NVFP4**](https://www.modelscope.cn/models/unsloth/Qwen3.8-27B-NVFP4)

<a href="/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-unsloth-desktop" class="button primary">Run in Unsloth Desktop</a><a href="/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-llama.cpp" class="button secondary">Run in llama.cpp</a><a href="/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-llama.cpp" class="button secondary">NVFP4 Guide</a><a href="/pages/CLyZKmpoJZpdaJXhLW4v#qwen3.8-2.4t-a95b" class="button primary">Qwen3.8-2.4T-A95B Guide</a>

### 🦥 Run Qwen3.8 in Unsloth Desktop

Qwen3.8 can run in [Unsloth Desktop](#run-qwen3.8-in-unsloth-desktop), an open-source UI app for local AI. **Unsloth automatically offloads to RAM and detects multiGPU setups**. With Unsloth Desktop, you can run models locally on **MacOS, Windows**, Linux and:

{% columns %}
{% column %}

* Search, download, [run GGUFs](/docs/new/studio.md#run-models-locally), MLX and safetensor models
* [**Self-healing** tool calling](/docs/new/studio/chat.md#auto-healing-tool-calling) + **web search**
* [**Code execution**](/docs/desktop.md#code-execution) (Python, Bash)
* [Automatic inference](https://unsloth.ai/docs/desktop#feature-deep-dive) parameter tuning (temp, top-p, etc.)
* Fast CPU + GPU inference via MLX and llama.cpp
* [Train LLMs](/docs/new/studio.md#no-code-training) 2x faster with 70% less VRAM
  {% endcolumn %}

{% column %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F6IXaXdTVyvbrnjehlxys%2Fkimik3.gif?alt=media&amp;token=31e1213b-d7da-46e9-bc7f-3a8c402513fc" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% stepper %}
{% step %}

#### Install Unsloth

The easiest way to get started is by downloading the [Unsloth Desktop app](/docs/desktop.md). Works on [macOS](/docs/get-started/install/mac.md), [Windows](/docs/get-started/install/windows-installation.md), and [Linux](/docs/get-started/install/linux.md).

<a href="https://unsloth.ai/download" class="button primary" data-icon="down-to-bracket">Download Unsloth</a>

* <i class="fa-apple">:apple:</i> [Download for macOS](https://unsloth.ai/download/mac)
* <i class="fa-windows">:windows:</i> [Download for Windows](https://unsloth.ai/download/windows)
* <i class="fa-linux">:linux:</i> [Download for Linux](https://unsloth.ai/download/linux)

Or, if you prefer to install manually:

{% tabs %}
{% tab title="Native install" %}
**MacOS, Linux, WSL:**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows:**

```powershell
irm https://unsloth.ai/install.ps1 | iex
```

{% endtab %}

{% tab title="Docker" %}
The [Unsloth Docker image](https://hub.docker.com/r/unsloth/unsloth) `unsloth/unsloth` is available on Docker. [Read guide.](https://unsloth.ai/docs/get-started/install/docker)
{% endtab %}

{% tab title="Homebrew" %}
Install Unsloth Desktop:

{% code collapsedlinecount="10" %}

```bash
brew install --cask unsloth
```

{% endcode %}

Update Unsloth Desktop:

```bash
brew upgrade --cask unsloth
```

{% endtab %}

{% tab title="WinGet" %}
Install Unsloth Desktop:

```powershell
winget install --id UnslothAI.Unsloth -e
```

Update Unsloth Desktop:

```powershell
winget upgrade --id UnslothAI.Unsloth -e
```

{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}

#### Search and download Qwen3.8

Go to [Unsloth Chat](/docs/new/studio/chat.md) or Model hub and search for Qwen3.8 in the search bar and download your desired model and quant.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fo53hIyoFypinWWLa1c0x%2FScreenshot%202026-08-14%20at%2012.42.38%E2%80%AFPM.png?alt=media&amp;token=a69de985-56ee-4ef3-8e10-f669cc168346" alt="" width="563"><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Run Qwen3.8

Inference parameters should be auto-set when using Unsloth, however you can still change it manually. You can also edit the context length, chat template and other settings.

For more information, you can view our [Unsloth inference guide](/docs/new/studio/chat.md).

For example using Unsloth Desktop with the 397GB Qwen3.8 (-91% smaller) allows you to toggle thinking modes, allow inline canvas, web search and code execution and much more.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fb3IiYJzHzsp2698xTim4%2Fgiffyy%20gf.gif?alt=media&amp;token=f1bda1a1-b81f-43e2-ba10-dbdc9a29c0c0" alt="" width="563"><figcaption><p>Dynamic 1-bit 397GB 91% smaller GGUF of Qwen3.8 2.4T in Unsloth Desktop</p></figcaption></figure>
{% endstep %}

{% step %}

#### Serve Qwen3.8 with Unsloth API

You can use `unsloth run` command and serve Qwen3.8 via an API using `llama-server` runtime flags, including context sizing, GPU layers, threading, sampling, networking, and tool configuration. For more info see our [API docs](/docs/basics/api.md) or [unsloth start](/docs/integrations/unsloth-start.md).

{% code overflow="wrap" %}

```bash
unsloth run --model unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0 \
    --reasoning-effort medium
```

{% endcode %}
{% endstep %}

{% step %}

#### Unsloth is now ready

You can also do many other things with Qwen3.8 via Unsloth Desktop like:

* **Connect tools:** [Claude Code](/docs/basics/claude-code.md), [Codex](/docs/basics/codex.md), [web search](/docs/new/studio/chat.md#advanced-web-search), [MCP](/docs/basics/mcp.md) and more
* **Train models:** Fine-tune text, diffusion, [embedding](/docs/basics/embedding-finetuning.md), and more
* **Generate media:** Create and train [images](/docs/basics/diffusion-image.md), video, [TTS](/docs/basics/text-to-speech-tts-fine-tuning.md) locally

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FYShiiub5gs5pCQLX6d4U%2FScreenshot%202026-08-15%20at%2012.18.24%E2%80%AFAM.png?alt=media&amp;token=d6996797-a144-4113-b4c3-155cca6c39a0" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### :llama: Run Qwen3.8 in llama.cpp

{% stepper %}
{% step %}
Download the latest version of llama.cpp. You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

{% endstep %}

{% step %}
Download the model via (after installing `pip install huggingface_hub`). If downloads get stuck, see: [Hugging Face Hub, XET debugging](/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md)

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-27B-GGUF \
    --local-dir unsloth/Qwen3.8-27B-GGUF \
    --include "*UD-Q4_K_XL*" # Use "*UD-Q3_K_XL*" for 3-bit
```

{% endstep %}

{% step %}
To run the model in llama-cli, follow the code snippets below:\
Remember to [change settings](#recommended-settings) according to your use-case.

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-27B-GGUF/Qwen3.8-27B-UD-Q4_K_XL.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

{% endcode %}
{% endstep %}
{% endstepper %}

### ⚡️NVFP4

Like Qwen3.6, we’re also releasing new [dynamic NVFP4 Qwen3.8](/docs/basics/nvfp4.md)-27B quants that run **\~1.5× faster** than BF16 checkpoints, with **better performance** and comparable file sizes. Run Qwen3.8-27B NVFP4 **1.5x faster** on **24GB VRAM.** We also added **FP8 KV cache calibration** for 2x longer context lengths! NVFP4 requires NVIDIA's Blackwell GPUs like RTX 50X, DGX Spark (see [#dgx-spark-with-nvfp4-quants](#dgx-spark-with-nvfp4-quants "mention")), B200, B300 GPUs. For older GPUs, our GGUFs work well! You can run NVFP4 quants in [vLLM](#vllm) only for now (SGLang is not supported).

* [Qwen3.8-27B-**NVFP4**](https://huggingface.co/unsloth/Qwen3.8-27B-NVFP4) quant

<table><thead><tr><th width="90" align="right">batch</th><th width="114.5999755859375" align="right">BF16 total tok/s</th><th width="122.60003662109375" align="right">NVFP4 total tok/s</th><th width="122" align="right">speedup</th><th width="137.4000244140625" align="right">BF16 per-user</th><th align="right">NVFP4 per-user</th></tr></thead><tbody><tr><td align="right">1</td><td align="right">89.8</td><td align="right"><strong>133.7</strong></td><td align="right">1.49x</td><td align="right">89.8</td><td align="right"><strong>133.7</strong></td></tr><tr><td align="right">8</td><td align="right">649.4</td><td align="right"><strong>938.8</strong></td><td align="right">1.45x</td><td align="right">81.2</td><td align="right"><strong>117.3</strong></td></tr><tr><td align="right">32</td><td align="right">1983.0</td><td align="right"><strong>2787.0</strong></td><td align="right">1.41x</td><td align="right">62.0</td><td align="right"><strong>87.1</strong></td></tr><tr><td align="right">64</td><td align="right">3048.5</td><td align="right"><strong>4407.2</strong></td><td align="right">1.45x</td><td align="right">47.6</td><td align="right"><strong>68.9</strong></td></tr></tbody></table>

See below for previous benchmarks conducted for Qwen3.6 as well comparing to other NVFP4 implementations which use 16bit activations vs our NVFP4 activations:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F8zM7cg0Xgo2pAlop1iPW%2F01_qwen36_combined_throughput.png?alt=media&amp;token=23131a96-4c41-42d7-aa16-5bfb21bb44a3" alt="" width="563"><figcaption></figcaption></figure>

All benchmarks use 1x B200 128 concurrency. Higher concurrency can boost 35B to 17,561 tokens / s.&#x20;

For accuracy benchmarks we ran KLD and Top-1 agreement over Code, Chat and many domains. NVFP4 is consistency 92% to 97% accuracy recovery vs BF16

| corpus            |      KLD mean | top-1 agreement |
| ----------------- | ------------: | --------------: |
| zh                |       0.01628 |          93.55% |
| code              |       0.02600 |          96.68% |
| refgen            |       0.03993 |          94.46% |
| chat              |       0.05818 |          92.15% |
| ja / ko / ru / es | 0.0124-0.0155 |          94-95% |

For accuracy benchmarks For Qwen 3.6, we conducted MMLU-Pro, AIME 2025, GPQA for FP8, BF16, NVIDIA's NVFP4 and our NVFP4s - we show our faster quants do similarly on all:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FFhOUUUlRBj3dafGnmvhK%2F03_qwen36_combined_accuracy(7).png?alt=media&amp;token=9178447f-d5ae-4489-9bdc-73b2b7b1631b" alt=""><figcaption></figcaption></figure>

For more information, you can read our [Dynamic NVFP4 quants blog](/docs/basics/nvfp4.md).

To run NVFP4 quants, see below for commands to run Qwen3.8-27B in [vLLM](/docs/basics/inference-and-deployment/vllm-guide.md) or [SGLang](/docs/basics/inference-and-deployment/sglang-guide.md):

#### **vLLM:**

To install vLLM in a separate venv:

{% code overflow="wrap" expandable="true" %}

```bash
uv venv unsloth-nvfp4-env --python 3.13
source unsloth-nvfp4-env/bin/activate
uv pip install "vllm>=0.25.0" "flashinfer-python>=0.6.13" "nvidia-cutlass-dsl>=4.5.2" \
    --torch-backend=auto
```

{% endcode %}

Then to serve the 27B variant:

```shell
vllm serve unsloth/Qwen3.8-27B-NVFP4
```

To enable MTP / speculative decoding (faster decode but somewhat less throughput), use:

```bash
vllm serve unsloth/Qwen3.8-27B-NVFP4
    --speculative-config '{"method": "mtp", "num_speculative_tokens": 2}'
```

If you get Torchcodec issues, be sure to do the below then relaunch vllm.

{% code overflow="wrap" expandable="true" %}

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

{% endcode %}

#### **SGLang:**

If using SGLang, you must use **SGLang version v0.5.19** otherwise it will not work since we quantize the lm\_head to FP8.

{% hint style="info" %}
vLLM has a `CompressedTensorsW8A8Fp8` kernel which supports this, whilst SGLang v0.5.19 cannot load the FP8 lm\_head. v0.5.19 works now!
{% endhint %}

For sglang after installing the latest:

{% code overflow="wrap" %}

```bash
uv pip install sglang sglang-kernel \
  --extra-index-url https://sgl-project.github.io/whl/cu130/ \
  --extra-index-url https://download.pytorch.org/whl/cu130 \
  --index-strategy unsafe-best-match
```

{% endcode %}

You can then serve it:

```bash
sglang serve unsloth/Qwen3.8-27B-NVFP4
```

To enable MTP, use:

{% code overflow="wrap" %}

```bash
sglang serve unsloth/Qwen3.8-27B-NVFP4 --speculative-algorithm EAGLE \
    --speculative-num-steps 3 --speculative-eagle-topk 1  --speculative-num-draft-tokens 4
```

{% endcode %}

### :exploding\_head:Quantization Analysis

NVFP4 quants are 1.5x faster than BF16 and retains 92 to 97% top-1 accuracy.

We used [Dynamic 3.0 GGUFs](/docs/basics/dynamic-3.0-ggufs.md) to make Qwen3.8-27B much better!

Top-1 accuracy plot as shown in UD-3 fro Qwen3.8-27B:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FVg5FHPxOpmaJ1r3ciw4u%2Fimage.png?alt=media&amp;token=107ef044-0181-489b-b6ae-da218e16c98b" alt="" width="563"><figcaption></figcaption></figure>

And mean KLD for Qwen3.8:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Ft8BnEqBLUQGUgu2cAKKI%2Fimage.png?alt=media&amp;token=912d5b6a-540f-4ee0-9208-f5ad45776341" alt="" width="563"><figcaption></figcaption></figure>

### 📊 Benchmarks

For GGUF quantization benchmarks you can see above for our [quantization analysis](#quantization-analysis) or [Dynamic V3.0 article](/docs/basics/dynamic-3.0-ggufs.md).

#### Qwen3.8-**27B**

See further below for table benchmarks:

<div><figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FWijY5wYmLx70Ao2ol7Tj%2Fqwen%20benchmark%201.jpeg?alt=media&amp;token=f69ebf50-cf35-426f-a610-8eeb32151d90" alt=""><figcaption></figcaption></figure> <figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FELa2vq8Wh3oelQi6Bf07%2Fqwen%20benchmark%202.jpeg?alt=media&amp;token=2cc6d085-630d-4fa1-9b50-784b22a1fb04" alt=""><figcaption></figcaption></figure></div>

#### Text Performance

<details>

<summary>Click to expand full table</summary>

| Benchmark                                            | Qwen3.8-27B                  | Qwen3.6-27B          | Qwen3.7-Plus         | Muse Glimmer-30B | Opus4.6 Max |
| ---------------------------------------------------- | ---------------------------- | -------------------- | -------------------- | ---------------- | ----------- |
| **Coding**                                           |                              |                      |                      |                  |             |
| Agentic terminal codingTerminal Bench 2.1 (Terminus) | 73.0                         | 63.4                 | 64.0                 | 51.7             | **78.2**    |
| Agentic codingSWE-bench Pro                          | **61.7**                     | 53.5                 | 57.6                 | 51.2             | 53.4        |
| Repo-level code generationNL2Repo-Bench              | 42.3                         | 36.2                 | 41.1                 | --               | **47.6**    |
| Agentic codingDeepSWE 1.1                            | **42.2**                     | 13.3                 | 14.2                 | --               | --          |
| Software engineeringQwenSWEBench                     | **79.0**                     | 49.3                 | 59.2                 | --               | 63.8        |
| **Agent**                                            |                              |                      |                      |                  |             |
| Long-horizon office workCoWorkBench                  | **70.7**                     | 61.0                 | 65.1                 | --               | 68.2        |
| Professional job tasksJobBench                       | **33.4**                     | 21.8                 | 27.6                 | --               | --          |
| Frontier agentic tasksAgents' Last Exam              | Pass\@1**20.4**Score**42.9** | Pass\@110.6Score27.3 | Pass\@113.2Score33.6 | --               | --          |
| General                                              |                              |                      |                      |                  |             |
| Instruction followingIFBench                         | **79.5**                     | 69.1                 | 79.1                 | 77.0             | 62.5        |
| Scientific reasoningGPQA Diamond                     | 89.2                         | 87.8                 | 90.3                 | 83.5             | **91.3**    |
| Multidisciplinary reasoningHLE                       | 30.8                         | 24.0                 | 34.7                 | 22.0             | **40.0**    |
| Competitive codingLiveCodeBench v6                   | **90.3**                     | 83.9                 | 89.6                 | --               | 88.8        |

</details>

## **Qwen3.8-2.4T-A95B**

Qwen3.8-**2.4T**-A95B is a 2.4T parameter (95B active) model with rivaling GPT-5.6 Sol. Full-precision Qwen3.8-2.4T-A95B requires 4.9TB of storage and 1-bit [Unsloth](https://github.com/unslothai/unsloth) Dynamic GGUFs takes **397GB (91% smaller)**, and larger IQ1\_S takes 508GB.

### :gear: Usage Guide

#### Qwen3.8-**2.4T** Requirements:

* [Qwen3.8-**2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)

| Dynamic 1-bit XXXS | Dynamic 1-bit Standard | Dynamic 2-bit | Q8\_0  | BF16 (Lossless) |
| ------------------ | ---------------------- | ------------- | ------ | --------------- |
| 397GB              | 508GB                  | 657 GB        | 2.6 TB | 4.9 TB          |

### Recommended Settings

Qwen3.8-2.4T is **thinking-only**, while Qwen3.8-Max is hybrid.

| Default                 |
| ----------------------- |
| temperature = 1.0       |
| top\_p = 0.95           |
| top\_k = 20             |
| min\_p = 0.0            |
| presence\_penalty = 0.0 |

* Context length = up to `1,010,000`
* `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`

If the model fits, you will get \~20 tokens/s generation when using B200s and >120 tokens / s throughput. Best rule of thumb: RAM+VRAM ≈ the quant size; otherwise it’ll still work, just much slower due to disk offloading.

### Run Qwen3.8-2.4T Guide

You can now run Qwen3.8 in llama.cpp and Unsloth Desktop. For the large Qwen3.8-2.T model, we will be utilizing the 397GB `IQ1_XXXS` quant (named Q1\_0) for best results in terms of accessibility and accuracy and it will require at least 450GB RAM. Feel free to change quantization type.

* **2.4T-A95B:** [Qwen3.8-**2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)

<a href="/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-unsloth-desktop" class="button primary">Run in Unsloth Desktop</a><a href="/pages/CLyZKmpoJZpdaJXhLW4v#run-qwen3.8-in-llama.cpp" class="button secondary">Run in llama.cpp</a>

### 🦥 Run in Unsloth Desktop

Qwen3.8 can run in [Unsloth Desktop](#run-qwen3.8-in-unsloth-desktop), an open-source UI app for local AI. **Unsloth automatically offloads to RAM and detects multiGPU setups**. With Unsloth Desktop, you can run models locally on **MacOS, Windows**, Linux.\
\
Go to [Unsloth Chat](/docs/new/studio/chat.md) or Model hub and search for Qwen3.8 in the search bar and download your desired model and quant. Then run it.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FpEVd0BlF4VCVbXoNQLRa%2FScreenshot%202026-11-09%20at%2011.15.41%E2%80%AFPM.png?alt=media&amp;token=a4a985da-109d-45c9-a8e3-517af2d44cb1" alt=""><figcaption></figcaption></figure>

### Qwen3.8-2.4T-A95B New 1-bit data-types

We extended IQ1\_S in llama.cpp which is 1.5625 bits per weight to 1.1875 bpw by reducing the number of entries in the codebook - we found this works well for large models, and can still retain a lot of accuracy - we also found these new data-types to be fine for post training quantization (PTQ) without the need for QAT or QAD (quantization aware training / distillation). [Qwen3.8-**2.4T-A95B**-GGUF](https://huggingface.co/unsloth/Qwen3.8-2.4T-A95B-GGUF)

<details>

<summary>Click for detailed analysis</summary>

Due to naming issues, we used TQ2\_0, TQ1\_0 and Q1\_0 otherwise it won't pop up in the HF repo.

<table><thead><tr><th>Dtype</th><th width="147.60000610351562">Naming</th><th width="114.39996337890625" align="right">BPW</th><th width="106.20001220703125" align="right"># entries</th><th width="113.413330078125" align="right">Index bits</th><th width="106.4000244140625" align="right">Block</th></tr></thead><tbody><tr><td>IQ1_S</td><td>IQ1_S</td><td align="right"><strong>1.5625</strong></td><td align="right">2048</td><td align="right">11</td><td align="right">50 B</td></tr><tr><td>UD-IQ1_XS</td><td>TQ2_0</td><td align="right">1.4375</td><td align="right">1024</td><td align="right">10</td><td align="right">46 B</td></tr><tr><td>UD-IQ1_XXS</td><td>TQ1_0</td><td align="right">1.3125</td><td align="right">512</td><td align="right">9</td><td align="right">42 B</td></tr><tr><td>UD-IQ1_XXXS</td><td>Q1_0</td><td align="right"><strong>1.1875</strong></td><td align="right">256</td><td align="right">8</td><td align="right">38 B</td></tr></tbody></table>

We are still running benchmarks for the new data-types, but for other large models, we get **good results without any QAT / QAD**:

| Dtype        |     GiB |      PPL |      KLD |  top-p |
| ------------ | ------: | -------: | -------: | -----: |
| IQ1\_S       | 553.204 | 2.578876 | 0.564553 | 78.882 |
| UD-IQ1\_XS   | 513.583 | 2.931261 | 0.690161 | 75.726 |
| UD-IQ1\_XXS  | 473.961 | 3.540383 | 0.876007 | 71.284 |
| UD-IQ1\_XXXS | 434.340 | 4.488796 | 1.109944 | 66.257 |

</details>

### :llama: Run Qwen3.8-2.4T in llama.cpp

{% stepper %}
{% step %}
We need to use the specific IQ1\_XXXS branch [here](https://github.com/unslothai/llama.cpp/pull/61). You can follow the build instructions below as well. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.

If you just want to run the standard `IQ1_S` and other quants, then [compile llama.cpp normally](#run-qwen3.8-in-llama.cpp):

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone --branch iq1-narrow https://github.com/unslothai/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

{% endstep %}

{% step %}
Download the model via (after installing `pip install huggingface_hub`). You can choose `Q1_0` for `IQ1_XXXS` or other quantized versions like `Q8_0` . If downloads get stuck, see: [Hugging Face Hub, XET debugging](/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging.md)

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --local-dir unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --include "*Q1_0*" # Use "*IQ2_XXS*" for 2-bit
```

{% endstep %}

{% step %}
To run the model in llama-cli, follow the code snippets below. Remember to [change settings](#recommended-settings) according to your use-case.

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-2.4T-A95B-GGUF/UD-Q1_0/Qwen3.8-2.4T-A95B-UD-Q1_0-00001-of-00010.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

{% endcode %}
{% endstep %}

{% step %}
To run the general UD-IQ1\_S you can do:

{% code overflow="wrap" %}

```bash
pip install -U "huggingface_hub[cli]"
hf download unsloth/Qwen3.8-2.4T-A95B-GGUF \
    --local-dir unsloth/Qwen3.8-2.4T-A95B-GGFF \
    --include "*IQ1_S*" # Use "*IQ2_XXS*" for 2-bit
```

{% endcode %}
{% endstep %}

{% step %}
Then to run it:

{% code overflow="wrap" %}

```bash
./llama.cpp/llama-cli \
    --model unsloth/Qwen3.8-2.4T-A95B-GGUF/UD-IQ1_S/Qwen3.8-2.4T-A95B-UD-IQ1_S-00001-of-00012.gguf \
    --temp 1.0 \
    --top-p 0.95 \
    --top-k 20 \
    --min-p 0.0
```

{% endcode %}
{% endstep %}
{% endstepper %}

#### Qwen3.8-**2.4T Benchmarks**

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FWP0nBgaQcnnAGjqG1jyQ%2Fqwen3.8%20bench.jpg?alt=media&amp;token=92a0d19c-51cb-4df2-a4f5-334fe08e6a21" alt="" width="563"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://unsloth.ai/docs/models/qwen3.8.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
