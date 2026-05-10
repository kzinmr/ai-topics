---
title: "Mistral NeMo"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/mistral-nemo"
scraped: "2026-05-10T01:20:18.157210+00:00"
lastmod: "2025-02-27T17:14:24.910Z"
type: "sitemap"
---

# Mistral NeMo

**Source**: [https://mistral.ai/news/mistral-nemo](https://mistral.ai/news/mistral-nemo)

Mistral NeMo
Research
Mistral NeMo: our new best small model. A state-of-the-art 12B model with 128k context length, built in collaboration with NVIDIA, and released under the Apache 2.0 license.
Jul 18, 2024
Mistral AI team
Today, we are excited to release Mistral NeMo, a 12B model built in collaboration with NVIDIA. Mistral NeMo offers a large context window of up to 128k tokens. Its reasoning, world knowledge, and coding accuracy are state-of-the-art in its size category. As it relies on standard architecture, Mistral NeMo is easy to use and a drop-in replacement in any system using Mistral 7B.
We have released pre-trained base and instruction-tuned checkpoints checkpoints under the Apache 2.0 license to promote adoption for researchers and enterprises. Mistral NeMo was trained with quantisation awareness, enabling FP8 inference without any performance loss.
The following table compares the accuracy of the Mistral NeMo base model with two recent open-source pre-trained models, Gemma 2 9B, and Llama 3 8B.
Table 1: Mistral NeMo base model performance compared to Gemma 2 9B and Llama 3 8B.
Multilingual Model for the Masses
The model is designed for global, multilingual applications. It is trained on function calling, has a large context window, and is particularly strong in English, French, German, Spanish, Italian, Portuguese, Chinese, Japanese, Korean, Arabic, and Hindi. This is a new step toward bringing frontier AI models to everyone’s hands in all languages that form human culture.
Figure 1: Mistral NeMo performance on multilingual benchmarks.
Tekken, a more efficient tokenizer
Mistral NeMo uses a new tokenizer, Tekken, based on Tiktoken, that was trained on over more than 100 languages, and compresses natural language text and source code more efficiently than the SentencePiece tokenizer used in previous Mistral models. In particular, it is ~30% more efficient at compressing source code, Chinese, Italian, French, German, Spanish, and Russian.  It is also 2x and 3x more efficient at compressing Korean and Arabic, respectively. Compared to the Llama 3 tokenizer, Tekken proved to be more proficient in compressing text for approximately 85% of all languages.
Figure 2: Tekken compression rate.
Instruction fine-tuning
Mistral NeMO underwent an advanced fine-tuning and alignment phase. Compared to Mistral 7B, it is much better at following precise instructions, reasoning, handling multi-turn conversations, and generating code.
Table 2: Mistral NeMo instruction-tuned model accuracy. Evals done with GPT4o as judge on official references.
Links
Weights are hosted on HuggingFace both for the
base
and for the
instruct
models. You can try Mistral NeMo now with mistral-inference and adapt it with mistral-finetune. Mistral NeMo is exposed on la Plateforme under the name
open-mistral-nemo-2407
. This model is also packaged in a container as NVIDIA NIM inference microservice and available from
ai.nvidia.com
.
Share this article
More from Mistral AI
News
Models
AI Services
