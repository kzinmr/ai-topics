---
title: "Introducing North Small Translate: A leading sovereign open-weight machine translation model"
source: "Cohere Blog"
url: "https://cohere.com/blog/north-small-translate"
scraped: "2026-09-11T06:00:18.513338+00:00"
lastmod: "2026-09-10"
type: "sitemap"
---

# Introducing North Small Translate: A leading sovereign open-weight machine translation model

**Source**: [https://cohere.com/blog/north-small-translate](https://cohere.com/blog/north-small-translate)

Today, we're releasing North Small Translate, a mixture-of-experts machine translation model with strong performance across 50+ languages. Across WMT26 benchmarks,¹ North Small Translate achieves an 83.6 score across all languages, outperforming proprietary models like DeepL and Google Translate, as well as open-weight alternatives such as Gemma 4 31B (off), GLM 5.2, and Mistral Large 3.
North Small Translate marks a significant milestone as Cohere's first translation model in the North model family. It builds on our multilingual and translation lineage — from the
Tiny Aya model family
to
Command A Translate
— and represents a clear next step in Cohere’s commitment to offering high-quality machine translation wherever it is needed.
Now available for research and non-commercial use under a
CC BY-NC 4.0
license, North Small Translate advances Cohere’s mission to make sovereign AI a technological reality.
Visit
Hugging Face
to download the weights - available in several near-lossless quantizations - explore our
HuggingFace space
to demo the model, and read our
implementation guides
.
Snapshot
Model
North-Small-Translate-1.0
License
Open-weights, non-commercial
Architecture
MoE
Model size
218B total; 25B active
Context length
16k input, 16k output
Input modalities
Text
Output modalities
Text
Languages
Supports 50+ languages.
Full list
Optimized for
Machine translation
Hardware (minimum)
1× B200 @ W4A4
2× H100s @ W4A4
Leading translation quality in the open ecosystem
North Small Translate outperforms similarly sized open-weight models under 1T parameters and API-based translation models in various dimensions of machine translation on average. In WMT model evaluations, North Small Translate leads with an WMT26 All Languages benchmark score of 83.60, compared with 81.56 for Qwen 3.5 397B A17B, 76.50 for GLM 5.2 FP8, 81.37 for DeepL NextGen, 79.46 for Gemma 4 31B (on), and 68.20 for Google Translate. North Small Translate (Agentic) — which can find errors and fix errors in translation — scores even higher, at 84.36.²
Image 1: Overall WMT26 scores across all languages across major models, benchmarked for WMT 2026 using GPT-5.6-Sol as a judge.
North Small Translate performs strongly across 32 high-resource languages and 18 additional languages. North Small Translate is the most consistent performer across the full spread of regions, without the sharp regional drop-offs seen in other models of its size. On average across all languages, it is the best-performing dedicated machine translation model in this evaluation — open or closed.
Image 2: Overall WMT scores by regional average across DeepL, Google Translate, and Gemma 31B (on), and North Small Translate using GPT-5.6-Sol as a judge.
At the regional level, North Small Translate punches above its weight, beating Gemma 4 31B (on) outright in Europe (82.2 vs. 73.9) while running essentially even with it in South Asia (86.2 vs. 86.7).
At the regional level, both North Small Translate and its Agentic counterpart beat Gemma 4 31B (on) outright across Europe — EU languages (82.74 Agentic / 82.17 standard vs. 72.73) and non-EU European languages (81.52 / 81.24 vs. 75.90) — while running essentially even with it in South Asia (87.13 / 86.16 vs. 88.04).
Both versions also outperform DeepL NextGen across every non-European region tested — MENA, South Asia, Southeast Asia, and East Asia — with the largest advantage in South Asia and MENA (roughly 8–10 points ahead of DeepL), a moderate edge in Southeast Asia (about 4–5 points), and the narrowest edge in East Asia (about 1-3 points, with the standard model closing in on DeepL's 85.41 score).
Increased throughput for faster workflows
North Small Translate is built for high-throughput generation, prioritizing raw output speed even as concurrency scales.
In our testing, North Small Translate achieved up to 1.4x higher output throughput than Gemma 4 31B TP1 (1 x GPU) under identical concurrency levels and hardware configurations — 112 vs. 81 Output Tokens per Second (TOPS) at low concurrency and 39 vs. 30 TOPS at high concurrency. In practical terms, that's 30-38% more tokens generated per second, translating to meaningfully faster completion times on longer outputs.
Image 3: North Small Translate’s output speed compared to Gemma 4 31B (off), across high and low concurrencies, in internal tests on identical hardware.
Long documents are where many translation models fall apart, and North Small Translate isn't one of them. It scores 48.9 on our long-context evaluation, more than double Google Translate (21.3) and Gemma 4 31B (19.4), and ahead of every general-purpose LLM we tested.³
Paired with its throughput advantage, that means fast, reliable translation at length, without the quality collapse seen in most non-specialized alternatives.
Efficient cost of translation, at scale
Efficiency is a core constraint in enterprise translation deployment, and we engineered North Small Translate to be extremely cost-efficient, without sacrificing performance.
Image 4: Overall WMT score and cost per task breakdown across machine translation models, using pricing per token or character from model providers' websites.
For enterprises evaluating commercial licenses of North Small Translate, benefit from a strong 80.1 score at just $0.000676 per task, using only 661 tokens on average. Compared to Gemini 3.1 Pro Preview (high) — which costs $0.038928 per task (5,762% more than North Small Translate).
Similarly sized models like Qwen 3.5 397B A17B and Cohere’s own Command A+ have decent performance at $0.004525 and $0.005158 per task, respectively.
Best in translation, in partnership with RWS
North Small Translate was developed in partnership with
RWS
, an AI solutions company pioneering in language technology and services. Close collaboration with RWS, specifically Language Weaver’s research and science teams along with its language experts, helped shape the model's real-world translation performance throughout development. RWS works with more than 80% of the world’s top 100 brands, empowering the world's most ambitious brands to communicate seamlessly across borders and cultures.
For enterprises that need more than open-weight research access, security, scalability, and a dedicated translation and localization platform, North Small Translate, is available through RWS’s
Language Weaver
product.
Getting Started
North Small Translate is available today on
Hugging Face
for non-commercial and research use. Visit our
documentation
for detailed model specs, deployment guides, and implementation examples to get started.
Footnotes
¹
WMT Benchmarks
focus on evaluation of general capabilities of machine translation (MT) systems. Its primary goal is to test performance across a wide range of languages, domains, genres, and modalities.
² To understand WMT Benchmark scores, the scoring methodology defines performance ranges as follows: 0-20 (not acceptable), 20-40 (borderline), 40-60 (acceptable), 60-80 (good with major errors), and 80-100 (perfect or with minor errors).
³ Long context evaluation measures how well a model can translate two chapters of a book on a single call. The quality is measured for each paragraph in isolation via xComet-XL metrics.
Blog
Written By
Cohere Team
Tags
Product Launch
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
