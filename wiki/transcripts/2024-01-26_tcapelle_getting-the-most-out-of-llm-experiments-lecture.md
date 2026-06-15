---
title: "Getting the Most Out of Your LLM Experiments w/ Thomas Capelle (Lecture Transcript)"
author: Thomas Capelle
date: 2024-01-26
date_ingested: 2026-06-15
source: "Hamel Husain's ML/LLM workshop series"
type: transcript
tags:
  - experiment-tracking
  - fine-tuning
  - training
  - evaluation
  - post-training
  - lora
  - open-source
  - mistral
  - transcript
related_article: articles/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments.md
participants:
  - Thomas Capelle (speaker, Weights & Biases)
  - Hamel Husain (host, Parlance Labs)
  - Dan Becker (moderator/questioner)
---

# Getting the Most Out of Your LLM Experiments w/ Thomas Capelle

> A workshop talk from Hamel Husain's ML/LLM workshop series (Jan 26, 2024). Thomas Capelle (Weights & Biases) demonstrates how to use W&B experiment tracking for fine-tuning workflows, showcases real community projects, discusses debugging training runs, and introduces W&B Weave for LLM tracing and evaluation.

**Companion article:** [[raw/articles/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments|Summary Article]]

---

## Introduction & Background

**[00:00:01]** Thomas introduces himself as a machine learning engineer at Weights & Biases, based in France. He works on the growth team, mostly focused on fine-tuning — "I became kind of the fine tuning guy."

**[00:00:31]** He works internally with LLMs and externally helping customers get the most out of fine-tunes. The problems shown during the course are "very real on a customer basis."

**[00:00:44]** Open source contributions: axolotl integration, HuggingFace Transformers parts, examples repo, and a recent torchtune integration for W&B.

**[00:01:13]** Previous background: traditional ML with time series, geospatial data, computer vision with satellite imagery for forecasting renewable energy production. Also a fast.ai alumnus from multiple versions.

---

## The Reproducibility Challenge

**[00:01:52]** "Keeping track of everything you do in this field is complicated." Hyperparameters, datasets, prompts, evals — "I feel like this guy multiple times — I need to bring my Docker image, I forget how to run that."

**[00:02:16]** You need to be "a Swiss knife" — learning many different tools to port code across environments and providers.

**[00:02:28]** W&B overview: experiment tracking company with axolotl integration and HuggingFace Trainer integration (just pass a flag to get dashboards with metrics logged to a central repository).

---

## Community Fine-Tuning Projects

### Dan's Alpaca Fine-Tuning

**[00:03:06]** Thomas shows how he monitors community experiments on Discord. Dan is doing his first fine-tune using the Alpaca dataset with axolotl.

**[00:03:35]** W&B features demonstrated:
- Toggle experiments on/off with the "eye" icon — runs pop in and out dynamically
- Metrics organized by train and eval: learning rate, loss curves
- **Overview tab** shows the tool used (axolotl CLI train) and automatically captures the YAML config
- **Config as artifact**: The raw YAML is logged as an artifact — "you can pull that and run the exact same experiment"

**[00:05:12]** "Having the actual YAML as a first class citizen here is very useful — you want to actually pull the YAML and then rerun that experiment and maybe tweak something."

### Zach's Self-Instruct & Grokking

**[00:05:26]** Zach was doing self-instruct, sharing knowledge about grokking points at the end of epochs. The hypothesis: the model memorizes some data, causing the dips in loss.

**[00:05:54]** Zach was tweaking parameters on the trainer itself, running on 8×H100s with multiple experiments (some crashed/killed).

**[00:07:01]** Learning rate discussion: "one technique you could do is put a super low learning rate, but that means your model learns slower — it's not always the silver bullet."

**[00:07:28]** Hamel connects this to the AnswerAI post about memorization. Jeremy Howard did experimentation about trying to memorize one batch and observing the grokking behavior.

### Mistral Function Calling Project

**[00:08:02]** Someone is trying to teach better function calling to Mistral. The project is private (curated handmade dataset), so they used W&B reporting to share only config snippets and training metrics.

**[00:08:49]** Thomas notes that Hermes Pro had function calling before Mistral added it officially. Many ways to encode function calling data — special tokens or not.

**[00:09:10]** Running from Mistral 7B (not 8×7B). "I'm curious how good a 7B could be at function calling without losing too much knowledge on the previous data."

### Japanese Bilingual Model Training

**[00:09:48]** A user training bilingual Japanese models. Thomas notes GPT-4's Japanese is "way worse than Latin languages — when you have 3 subjects in a sentence, it kind of makes a mess."

**[00:10:22]** References efforts like NueX (Korean/Japanese language models) and leaderboard work with Korean and Japanese teams to score model capabilities on those languages.

---

## Ablation Studies on Mistral 7B

**[00:11:41]** Thomas shows a larger project: an open-source group (including Jono) doing ablation studies on Mistral 7B — removing 75% of layers and retraining with SFT + DPO to recover the model.

**[00:12:16]** W&B workspace features for complex projects:
- **Run grouping**: Group related runs (same initial model, 1-stage, 2-stage, evals)
- **Multiple views**: Default dashboard is "bloated" — create special views (e.g., SFT-only view with regex filtering)
- **Shaded areas in grouped runs**: Shows the average curve, which may not be meaningful when comparing different training recipes

**[00:14:19]** **Dan Becker's question** about ablation study patterns and insights.

**[00:14:26]** Background: This was inspired by TinyLlama — the idea of creating a small model from a big one by pruning layers (not training from scratch). Related to Shear Llama paper.

**[00:14:54]** Jeremy Howard's suggestion: "just remove the full layers — it doesn't matter if it's not that deep and it's shallow."

**[00:15:14]** Goal: Make a 2B or 1.5B from Mistral Instruct for use as a draft model (speculative decoding). Used the Zephyr recipe (SFT + DPO) since no Mistral Instruct recipe existed.

**[00:15:51]** Results: "The final model has a reasonable score — of course not as great as the big model, but we put a super limited budget of 1 billion tokens, which is very low." The model could draft the big model and "kind of work."

**[00:16:09]** Fun fact: At a Mistral Hackathon, another team building an embedding model from Mistral 7B tried the pruned model and it was "very good at embeddings."

**[00:16:42]** Automation pipeline: Push ablated checkpoint → automatically trigger SFT → DPO → Eval Harness → results flow back to W&B dashboard.

---

## Loss as a Proxy for Model Quality

**[00:20:16]** **Dan Becker's question**: "With LLM fine-tuning, I've never been really confident that loss is a proxy for output quality. I spend a lot of time inspecting outputs."

**[00:21:33]** **Thomas's response**: Build an eval dataset. Generate samples, create tests to compare if the model is better or worse. Eval Harness computes metrics on benchmarks, but for your own use case you need your own benchmark.

**[00:22:42]** W&B internal approach: "We ask engineers to create 5 QA pairs each, times 10 = 50, twice a week. You easily curate a dataset of a couple hundred high-quality samples."

**[00:23:15]** "During training, loss is a good proxy of things going wrong. But it's not a good proxy for comparing 5 fine-tunings with 3 tweaked parameters — you'll get basically the same loss, and maybe one of those is better."

**[00:23:39]** **Dan**: "My experience is I just look at the samples."

**[00:23:45]** **Thomas**: "That's a good proxy of things getting wrong. You need to look at samples because sometimes there are formatting issues. Sometimes you need to look at token IDs, decode the batch."

---

## Debugging Training Spikes

**[00:24:08]** Thomas had a model spiking at a specific point. Decoded the batch and found Korean characters in an English-only dataset — "the model just spiked there every time, even if I tweaked the learning rate."

**[00:24:27]** "Go back in time, rewind, decode that batch, see what you're feeding the model." HuggingFace Transformers lets you index on the data loader.

**[00:25:22]** Axolotl complexity: Does multi-packing (multiple sequences together) for GPU efficiency. "A lot of things could go wrong there."

**[00:25:57]** **Hamel's question**: How did you correlate the batch with the loss spike?

**[00:26:10]** **Thomas's method**: Patch the HuggingFace Trainer's step method. Check grad norm and loss — whenever it spiked, decode the batch and log to a W&B table. Save a checkpoint just before the spike.

**[00:26:38]** "What I wanted to do was skip that batch — that batch is bad, I don't want to update the weights. Skip the optimizer step."

**[00:27:42]** Lower-level libraries (torchtune, pure PyTorch) make this easier. Big companies like Mistral, OpenAI "log tons of proxy metrics from all the nodes" to spot issues quickly and restart.

---

## W&B Tips & Tricks

**[00:17:58]** **Pin columns**: Bring important parameters (learning rate, batch size) to the left so they're always visible in the runs table.

**[00:18:26]** **Run comparison table**: Add a panel → "Run Compar" → toggle "Diff only" to see only parameters that differ between runs. "LLM training configs sometimes have 200 parameters — I just want to see what's different."

**[00:31:44]** **Quick wins summary**:
- Save workspace views (eval view, training view)
- Run comparison for diff inspection
- Pin columns for always-visible key parameters
- Parallel coordinates plot for hyperparameter optimization

**[00:32:52]** **Reproducibility philosophy**: "The most important case for me is coming back 6 months later — I'm protected against myself and can reinspect my project, or hand it to someone else."

**[00:33:17]** Christy Whitaker's illustration: Steps from git version control → containers → experiment tracking → collaboration tools. "There's no 0 or 100 — you can be in between."

---

## Storage & Pricing

**[00:28:16]** W&B has storage costs. Scales on usage — personal is cheaper, corporate with security features is more expensive.

**[00:28:56]** You can bring your own storage (Google Cloud, S3, Azure buckets) — reference artifacts to your bucket, still get lineage and traceability.

---

## W&B Weave: LLM Tracing Tool

**[00:34:14]** Thomas introduces **Weave** — a new W&B product (public preview) for LLM tracing and evaluation. "Tailored for: you have a fine-tuned model, you want to use it, and keep track of everything going in and out."

**[00:35:09]** `pip install weave` — lightweight library built on top of Pydantic.

**[00:35:26]** Core idea: You already have Python functions wrapping API calls. Add a `@weave.op()` decorator and Weave tracks inputs, outputs, and underlying API calls (with OpenAI integration).

### NYT Connections Puzzle Demo

**[00:36:34]** Thomas proposes solving NYT Connections (16 words, find 4 groups of 4) as an LLM evaluation problem.

**[00:38:43]** One-shot prompt approach: Gets 1 group correct, 3 others with 3/4 words. "A good starting solution."

**[00:39:28]** Hard version: Give the full solution at once (not iterative hints). "Use the LLM as a scratchpad — call multiple times, create intermediate solutions."

**[00:40:01]** Ideas: Embedding-based approach — embed words, search in embedding space for relationships.

**[00:40:49]** Evaluation framework: Create eval dataset → run model → score (4=perfect, 3=almost, 0=none). Results: 3/20 correct (15%).

**[00:44:56]** Weave traces show nested function calls — "like a debugger. When one function fails, you can see inputs and outputs."

**[00:46:02]** Evaluation dashboard: Version tracking for models and evaluations, per-sample inspection (which words matched, which didn't).

---

## Q&A Discussion

**[00:29:22]** W&B table syntax: It's a raw table dumped by the integration. Thomas prefers using the UI (filter, click columns) over the query language.

**[00:31:26]** Eval tables: "You probably should not turn on every single model — it concatenates all data. Explore tables one by one for one model at a time."

**[00:47:46]** **Hamel**: "Since we're out of time, let's head over to Discord."

**[00:47:57]** **Dan**: "There's some questions about getting code. Anything you write in Discord people have access to for a long time."

---

## Companion Resources

- **Companion article:** [[raw/articles/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments|Summary Article]]
- **Course:** Hamel Husain's ML/LLM workshop series (Maven)
- **W&B Weave**: https://wandb.me/connections (NYT Connections demo notebook)
- **Related transcript:** [[transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture|Why Fine-Tuning is Dead — Emmanuel Ameisen]] (same course, 2 days earlier)

## Related

- [[entities/hamel-husain|Hamel Husain]] — host of the workshop series
- [[entities/thomas-capelle|Thomas Capelle]] — speaker
- [[concepts/post-training/_index|Post-Training]] — fine-tuning techniques coverage
- [[concepts/rag|RAG]] — alternative approaches discussed
