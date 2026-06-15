---
title: "LLM Fine Tuning Course — Office Hours: FSDP, DeepSpeed and Accelerate w/Zach Mueller (Lecture Transcript)"
author: Zach Mueller, Dan Becker, Hamel Husain, Charles Frye
date: 2024-01-12
date_ingested: 2026-06-15
source: https://maven.com/
type: transcript
tags:
  - training
  - distributed-training
  - fine-tuning
  - pytorch
  - gpu
  - quantization
  - inference
  - open-source
  - huggingface
  - post-training
  - transcript
related_article: articles/2024-01-12_maven_fsdp-deepspeed-accelerate-office-hours.md
participants:
  - Zach Mueller (guest — HF Accelerate lead)
  - Dan Becker (host)
  - Hamel Husain (co-host)
  - Charles Frye (co-host)
---

# Office Hours: FSDP, DeepSpeed and Accelerate w/Zach Mueller

Office hours session from the **LLM Fine Tuning** course (Maven), featuring Zach Mueller (Technical Lead for Hugging Face Accelerate) as guest. Moderated by Dan Becker, Hamel Husain, and Charles Frye. Covers practical distributed training, GPU selection, fine-tuning workflows, and community Q&A.

---

## 1. War Stories — Building Accelerate's Gradient Accumulation

**[Zach Mueller, 00:00:21]**

Zach recounts developing the automatic gradient accumulation feature for Hugging Face Accelerate with Sylvain Gugger. The core challenge: Accelerate's design philosophy forbids "magic" — every API must be explicit and transparent to the user.

> I had to rewrite that thing, I think, 6 or 7 times. Take it to Sylvain and just go, "Hey, does this look right?" "No, too much magic." "Does this look right?" "No, too much magic." Over and over and over again, until finally we hit something, and then it's like one of the most used things and loved things about our library.

It took **2 weeks of rewrites** to arrive at the final API design, which went on to define how Accelerate's more complex features are built.

**[Dan Becker, 00:02:24]** — "Did that code improve a lot because Sylvain pushed you to rewrite it?"

**[Zach Mueller, 00:02:32]** — "Some of the stuff I came up with was far too magical and not really maintainable. 6 or 7 different rewrites before we finally got it right enough."

**Key insight:** The tension between "just make it work" and "make it transparent and debuggable" is a core challenge in ML tooling API design.

## 2. Axolotl vs HF AutoTrain

**[Dan Becker, 00:03:49]** — "What are your feelings on Axolotl versus HF AutoTrain?"

**[Zach Mueller, 00:04:06]** — They solve 2 different problems:
- **AutoTrain**: Agnostic — "train whatever you want with the data you have." Slightly different API.
- **Axolotl**: High-level, focused on text model fine-tuning. "Do it quickly, do it fast, following a pretty loose guideline towards what you can fit."

"There are 2 different solutions to a problem that can have overlap."

**[Zach Mueller]** — His extent of AutoTrain is "helping debug AutoTrain when Accelerate breaks."

## 3. Learning Journey to Becoming an Effective LLM Engineer

**[00:05:46]**

**[Zach Mueller]** — "Just tweak with shit. Just play with code, build models, do things. Because you can spend ages reading and reading and reading and reading and never touch code."

Core advice:
- Train models, get comfortable with the code
- Depth of expertise comes with time
- Even running the same Axolotl command with different datasets teaches you something
- **Make your learnings public** — same advice from fast.ai days
- Be open to criticism from people who know more
- Be humble

**[Dan Becker, 00:07:16]** — Pushes back: In conventional ML, you see a score go up/down. In generative AI, it's harder to know if you like what happened when you change a hyperparameter.

**[Zach Mueller, 00:08:27]** — "Talk to the people that are doing the cool things. Just send them a DM." Post your loss graph on Twitter and ask "Does this seem normal?" Community feedback matters because self-judgment is unreliable.

**[Hamel Husain, 00:09:26]** — Pick a small project. Start with LoRA on a pretrained model with Axolotl. "It's actually kind of hard to mess it up." Like a random forest — just point the model at the data and it kind of works. Getting positive reinforcement fast helps enormously.

**[Dan Becker, 00:10:21]** — The hard part is **tokenization and prompts** — making sure you do the same thing at inference time as training time.

## 4. Community and Getting Feedback

**[Dan Becker, 00:11:02]** — The community of people actively doing stuff and sharing it is smaller than you'd expect, still in its infancy. Huge opportunity to get feedback on the "ground floor."

**[Zach Mueller, 00:12:12]** — "We're all people, and a lot of us don't have egos." DM people on Twitter with questions — they'll likely answer if you phrase it right.

**[Hamel Husain, 00:12:47]** — "You definitely should put in the work. Don't just DM someone like 'whatever.' Tell them what you tried, what didn't work, what you researched. Show the person that you are trying."

## 5. Good Datasets for LLM Fine-Tuning

**[Charles Frye, 00:13:28]** — "What are some good public datasets or Kaggle challenges for training or fine-tuning LLMs?"

**[Zach Mueller, 00:13:46]** — His Llama 3 fine-tune uses the **StarCoder 2 + Self-Instruct** approach: use the base LLM to generate completion data from existing code on **The Stack** dataset. "That one's not terrible because you're generating it yourself."

**[Hamel Husain, 00:14:41]** — Phil Schmid's "Instruction Tuning Llama" blog post is a great gateway to fine-tuning.

**[Dan Becker, 00:15:23]** — Hugging Face Datasets has great breadth — just do a dataset search for your topic. "The breadth of what's in HF Datasets is pretty great."

**[Charles Frye, 00:15:58]** — Two key insights:
1. **Synthetic data** is great: distill a larger model (70B) into a smaller one (8B/3B). You have a clear data-generating process and a solid gold standard.
2. **Use data that changes over time** — a stream, not a batch. This helps detect train/test leakage and prepares you for production ML. Example: classify tweets with GPT-4, collect more next week.

## 6. Accelerate + FSDP + DeepSpeed + torch.compile

**[Zach Mueller, 00:18:07]** — On whether to use Accelerate with DDP/FSDP/DeepSpeed:

> I would not be able to do my Llama 3 8B fine-tune on 2× RTX 4090s if I did not have FSDP available. Essentially, what FSDP allows is your 2× RTX 4090s are not two 24GB cards — they are, in a light sense, 1× 48GB card.

**[Charles Frye, 00:19:06]** — On torch.compile: historically more of an inference-time optimization (static compiled graph for fixed batch sizes). But PyTorch now wants compile everywhere.

**[Zach Mueller, 00:19:54]** — PyTorch's **PiPPy** (pipeline parallelism for training) relies heavily on torch.compile. Expect the landscape to change dramatically in 3-6 months. Training on compile works but depends on model layout. Benefits are **throughput optimizations** (operator/kernel fusion), not memory optimizations.

## 7. Training/Inference Precision Mismatch

**[00:21:16]** — Q: Training on RTX 3090s in BF16, but inference on T4s that don't support BF16?

**[Zach Mueller]** — T4s with fake BF16 will be painfully slow. Models trained fully in BF16 can break when upcast to FP32. That's why HF Trainer uses autocast — trains in BF16 so it can be upscaled back. Normal FP16 is "usually a little less optimized than BF16."

## 8. FSDP vs DeepSpeed — When to Use Which

**[Zach Mueller, 00:23:04]**

> FSDP really shines when you have big models, or if your model barely fits on one GPU and you have 2 available. The model is fully on one, and the gradients are just in the other GPU. You have a ton of extra VRAM.

**FSDP vs DeepSpeed:**
- **DeepSpeed**: Very configurable. Can specify per-layer offloading (e.g., "just these layers to CPU"). More freedom in device configurations.
- **FSDP**: All-or-nothing approach. If everything fits in memory → use FSDP. If you need partial offloading → look at DeepSpeed ZeRO-2 or ZeRO-3.

## 9. NVLink and Consumer GPU Performance

**[Hamel Husain, 00:24:31]** — The debate on NVLink: how much does lack of NVLink destroy performance on consumer cards? Sparse information available. Silvan/ Stas showed ~25% degradation. Tim Dettmers says you don't need it.

**[Zach Mueller, 00:25:33]** — NVLink doesn't work for RTX 4090s, barely works for 3090s. RTX 3090s were "the golden child" for a while because they had NVLink support.

**GPU recommendations (2024):**
- **RTX A4500**: Zach would choose this if rebuilding his rig. Same VRAM as 4090, fraction of power usage, super slim, more CUDA cores available for training. ~$2,500 vs ~$1,800 for 4090.
- A4500 comes in 20GB (older) and 24GB (newer) versions
- RTX 4090 has FP8 support; A4500 Ampere does not (Ada version does)
- 2× water-cooled 4090s require a giant case vs. 4× A4500s in the same space
- Zach's Llama 3 8B LoRA: 4 iterations on 2× RTX 4090, 4-6 hours total

## 10. Can Fine-Tuning Catch Up to Frontier Models?

**[Hamel Husain, 00:29:07]** — Look at Teknium's community fine-tunes — they exceed the base model on many benchmarks. Almost like continued pre-training.

**[Zach Mueller]** — "It's largely on the community. If we can make those fine-tunes competitive, that's great. In some ways we're also fighting a losing war because **data** — the closed-source people have access to a ton more data than we do."

## 11. Prompting and Tokenization at Inference Time

**[Zach Mueller, 00:31:12]** — Best debugging approach: upload model to HF Hub, load in a pipeline, use `model.generate()`. Use HF's **chat templating** guide for debugging token issues.

**[Hamel Husain]** — HF chat templates are cool but Axolotl doesn't use them directly — you have to copy-paste the entire chat template. Standardizing on HF chat templates would eliminate a lot of spaghetti code around prompt templating.

## 12. Inference on Consumer Hardware

**[00:33:36]** — Q: Running 8B model on single RTX 4090?

**[Zach Mueller]** — Half precision: ~13GB. Options:
- Quantization (AWQ, GPTQ)
- CPU offloading via `device_map="auto"` (slower but works)

**[Hamel Husain]** — Sweet spot: vLLM with AutoAWQ quantization. Can get faster with TensorRT-LLM but "then you have to suffer."

**[Hamel Husain]** — "I quickly fell in love with vLLM. You just point to the folder and it goes."

## 13. Why Not Train in INT8?

**[Zach Mueller, 00:34:45]** — "Because it's very unstable." NVIDIA's Transformer Engine is experimental for FP8 training. People try it, still go back to BF16. PyTorch is adding official INT8 support — maybe they'll figure out "secret sauce with quantization on the fly plus native FP8."

**[Charles Frye]** — Blackwell architecture doubled down on FP4 despite FP8 instability. Zach: "Clearly they have some sort of special sauce... We can't necessarily recreate it. I would love to know what they trained Llama 3 in when the paper comes out."

## 14. Accelerate at Scale

**[Zach Mueller, 00:38:16]** — Lucidrains uses Accelerate for projects orchestrating training on **over 1,000 GPUs**. "Accelerate can't fail per se — if Accelerate fails, all we are is a light wrapper around what everyone else is orchestrating."

Only issues seen: occasional timeout problems in distributed settings. "Distributed is just hard."

## 15. Chinchilla Scaling Laws and Fine-Tuning

**[Charles Frye, 00:39:41]** — "Are the Chinchilla scaling laws still relevant?"

**[Zach Mueller]** — They still kind of are, but Llama 3 showed you can just keep training past Chinchilla-optimal.

**[Charles Frye]** — Scaling laws tell you how to optimally allocate FLOPs between parameters and data. For that they're still correct. But they don't tell you how to get the best model — the answer is always to continue training until convergence.

> Models that are undertrained (Chinchilla-optimal) should be more steerable and easier to fine-tune, because there should be more slop in the weights.

**[Zach Mueller]** — His Llama 3 8B went 4-5 epochs (vs. recommended 1-2), and the 4th/5th showed best results while still improving loss. "At least for 8B, there might be some space there still."

## 16. TensorFlow, PyTorch, and JAX

**[Zach Mueller, 00:42:05]** — TensorFlow/Keras is still a backend in HF Transformers, but the general trend is PyTorch. "I'm not gonna say one is better than the other — they're both equal. It's just everything I do is in PyTorch."

**On JAX (00:43:19):** "It's Google. They rewrite everything every few years. It's a risk, a gamble." XLA was TPU-only for a while, recently brought to GPUs. "If it's still a thing in 3 years, that's probably a good sign."

**[Charles Frye]** — JAX is a beautiful program transformation framework, but "pure functional programming" makes it harder for researchers and tinkerers who aren't comfortable managing an RNG monad.

## 17. Apple Silicon for Training

**[Zach Mueller, 00:45:37]** — PyTorch admitted their MPS (Apple Silicon) training support is one of the worst. Inference is great, training is mixed.

**[Charles Frye]** — Apple Silicon won't become a preferred training target: "It's a system-on-a-chip. There isn't something that looks like a server card with fast GPU interconnect."

Zach: Cash (who writes Dingboard) almost built a Mac cluster, then did a 180 and went with NVIDIA because "everything's too unstable."

## 18. Multi-LoRA Inference Serving

**[Zach Mueller, 00:49:02]** — How to serve multiple LoRAs with Accelerate inference / hot-swap?

**[Hamel Husain]** — vLLM has LoRA adapter serving — you can pass different adapters at generate time. Hot-swap within a batch.

**[Charles Frye]** — The real optimization: as a batch goes through, route rows in the matrix through different LoRAs. This is why parallel adapters (LoRA) are better than sequential adapters — you get most of the throughput benefit of batching for the large model with all the customization of LoRAs.

Zach referenced **Kraken LoRA** ("Collection of Experts") — dynamic model routing using a sequence classification model to route inputs to the most suitable language model with task-specific LoRAs.

## 19. Choosing a Fine-Tuning Project

**[Zach Mueller, 00:55:21]** — "I read the paper. It seemed neat. It's a pet problem — doesn't have to be unique. You could be just recreating what other people did."

> The difference between just messing around and science is writing it down. Even if you're just messing around with data, write it down — great, now it's a blog. Model fails? Write it down — that's a lesson learned.

## 20. Model Size Selection: Training Cost vs Inference Cost

**[Zach Mueller, 00:57:03]** — Budget dictates VRAM → VRAM dictates model size. Time is cost: free to run 2 days at home vs. $80 for an H100 for 1-2 hours.

**[Hamel Husain]** — The incumbent (OpenAI) has good latency and cost. Humans have a cognitive bias: once you have something, you value it more. The replacement needs to be **markedly better** from a user experience perspective. "What is the smallest model I can get away with for the quality threshold?"

**[Dan Becker, 00:59:19]** — **Training compute is effectively free** compared to inference. "Inference is so vastly more expensive for all the products I work on that training... it's not even worth thinking about training costs."

> We almost always end up deploying 7-8B parameter models. We can't actually tell the difference when you just side by side look at the results. Model size is a less interesting problem than you would expect.

Start with 7-8B for fast iteration. Try bigger models. If not meaningfully better, stay small.

## 21. Phi-3 and Smaller Models

**[Zach Mueller, 00:02:13]** — Phi-3: "There's something weird with the data and how they trained it that isn't showing real world performance." Anton's testing: Phi-3 was good for 12 hours, then failed in real-world scenarios. Llama 70B performed out-of-the-box phenomenal. 7-8B remains the practical threshold.

---

## 2026年振り返り — 2年前の発言はどう見えているか

2024年1月時点のこのOffice Hoursの発言を、2026年6月の視点から振り返る。

### 的中した予測・普遍的な洞察

- **「7-8Bがスイートスポット」** — 2026年現在もLlama 3.1 8B、Qwen2.5 7B、Mistral 7Bがfine-tuningの主力。Dan Beckerの「training cost is free, inference cost is everything」は完全に正しかった。本番デプロイの大半は7-14Bレンジ。
- **「FSDPは'all-or-nothing'、DeepSpeedは細やか」** — この構図は2026年も基本的に変わらない。Accelerate v1.xでもFSDPのoffload粒度は改善されていない。
- **「LoRAはparallel adapterとして優秀」** — Charles Fryeのper-request LoRA routingの説明は2026年のvLLM、SGLangのLoRA multiplexing機能として具現化した。
- **「Just tweak with shit」** — 実験重視の姿勢は2026年の「vibe coding」文化と呼応。Axolotl、LLaMA-Factory、Unslothがさらに低コード化。
- **「Make your learnings public」** — Hugging Face Hubのモデル数は2024年1月から2026年6月で約10倍に増加。公開fine-tuneのエコシステムが爆発的に成長。

### 変化した状況

- **「torch.compileは実験的」** — 2026年現在、torch.compileはPyTorch 2.xで安定し、AxolotlやTRLでもデフォルト有効化されている。Zachの「3-6ヶ月で大きく変わる」予測は的中。
- **「INT8学習は不安定」** — 2026年でも依然としてBF16が主流だが、NVIDIA Transformer EngineとFP8学習はBlackwell/B200で実用段階に到達。Llama 3.1 405Bの学習ではFP8が使われたと噂される。
- **「Apple Siliconは学習に向かない」** — M4 Ultraの統合メモリ（最大512GB）により、推論用途では圧倒的に有利。しかし分散学習のインフラは依然としてNVIDIA優位。Zachの「MacBookは拒否」は2026年でも多くのMLエンジニアの共感を得る立場。
- **「A4500を買う」** — RTX 5090（32GB VRAM）、RTX PRO 6000（96GB）の登場でGPU選択肢は大幅に拡大。A4500のポジションはRTX 5090に取って代わられた。
- **「Phi-3は変」** — Phi-4 (2025) は大幅に改善し、14BでLlama 3.1 8Bを超える性能を発揮。Microsoftのデータ品質への執着が実を結んだ。
- **「Chinchilla scaling laws」** — 2026年ではscaling lawsの議論は「test-time compute scaling」（o1/o3、DeepSeek-R1）に移行。学習時FLOPsの最適配分だけでなく、推論時FLOPsの最適配分が新たなフロンティア。
- **「JAXは3年後にどうなっているか」** — 2026年でもJAXはGoogle DeepMind内部では標準だが、外部エコシステムは依然としてPyTorch優位。Zachの「3年後にまだ存在するか」という懸念は、存在はしているが影響力は限定的という形で答えが出た。

### この講義の歴史的意義

このOffice Hoursは、Hugging Faceエコシステムの「中間層」（Accelerate/FSDP/DeepSpeed）が一般のML実務者に届き始めた転換期の記録。2024年1月はLlama 3の公開前（2024年4月）であり、オープンモデルのfine-tuningが「一般のエンジニアの仕事」になり始めた黎明期の声として価値がある。

---

## Companion Resources

- **Companion article:** [[raw/articles/2024-01-12_maven_fsdp-deepspeed-accelerate-office-hours]]
- **Related concepts:**
  - [[concepts/post-training/accelerate]] — Hugging Face Accelerate
  - [[concepts/post-training/pytorch-fsdp]] — PyTorch FSDP
  - [[concepts/deepspeed]] — DeepSpeed
  - [[concepts/post-training/peft-lora-qlora]] — PEFT / LoRA / QLoRA
  - [[concepts/qlora]] — QLoRA
- **Related entities:**
  - [[entities/zach-mueller]] — Zach Mueller
  - [[entities/hamel-husain]] — Hamel Husain
  - [[entities/charles-frye]] — Charles Frye
