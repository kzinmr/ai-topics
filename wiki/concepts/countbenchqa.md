---
title: "CountBenchQA"
type: concept
created: 2026-05-08
tags:
  - benchmark
  - multimodal
  - counting
  - evaluation
  - simple-eval
aliases:
  - countbench-qa
  - countbench
status: active
sources:
  - https://arxiv.org/abs/2302.12066
  - https://arxiv.org/abs/2407.07726
  - https://huggingface.co/datasets/vikhyatk/CountBenchQA
related_concepts:
  - concepts/ai-benchmarks-evals-overview
  - concepts/multimodal/_index
related_entities:
  - entities/florian-brand
---

# CountBenchQA

**CountBenchQA** is an ultra-simple object counting benchmark for vision-language models. It tests exactly one capability — counting the number of visible objects in an image — at exactly one level of difficulty. Originally introduced as "CountBench" in the paper "Teaching CLIP to Count to Ten" (Paiss et al., ICCV 2023), it was later adapted into a VQA format as CountBenchQA for the PaliGemma evaluation suite.

**OG Paper**: [arXiv 2302.12066](https://arxiv.org/abs/2302.12066) | **CountBenchQA Paper**: [arXiv 2407.07726](https://arxiv.org/abs/2407.07726) (PaliGemma) | **HF Dataset**: [vikhyatk/CountBenchQA](https://huggingface.co/datasets/vikhyatk/CountBenchQA)

## What It Measures

- **Domain**: Object counting in natural images
- **Task type**: Visual question answering — "How many [object] are there in the image?"
- **Range**: 2 to 10 objects per image
- **Format**: Given an image and a manually written question about the number of objects, the model must output the correct count. Each image depicts between 2 and 10 instances of a specific object type (e.g., "four snails," "six flower pots," "nine Christmas cards")
- **Simplicity**: This is deliberately the simplest possible vision-language evaluation. There is no reasoning, no complex language understanding, no multi-step logic — just "look at the image and count"

## Data Sourcing Method

CountBench has an unusually careful data curation pipeline spanning multiple research groups:

1. **Automatic curation from LAION-400M**: The original CountBench was automatically scraped from LAION-400M, a large public image-text dataset. Images were selected where captions contained spelled-out numbers matching the visible object count
2. **Manual verification**: After automatic curation, every image was manually verified to contain exactly the stated number of clearly visible objects. Images were balanced to ~60 examples per number (2 through 10), yielding 540 total images
3. **Manual rebalancing**: The dataset was intentionally balanced across counts to prevent models from exploiting distribution biases
4. **CountBenchQA conversion**: Each image was paired with a manually generated question ("How many X are there in the image?") by a separate research team for the PaliGemma paper, turning the counting task into standard VQA format
5. **Link rot mitigation**: The HuggingFace-hosted version (vikhyatk/CountBenchQA) contains 491 images — some original URLs became inaccessible over time and were removed

**Key quality feature**: The human-verified, balanced design means the benchmark has essentially no label noise. Every image-count pair has been confirmed by a human reviewer.

## Key Numbers

| Metric | Value |
|--------|-------|
| Total images (original CountBench) | 540 |
| Total images (CountBenchQA, HF) | 491 |
| Count range | 2–10 |
| Images per number | ~60 (original), balanced |
| Question format | "How many [object] are there in the image?" |
| Data source | LAION-400M (auto-curated, manually verified) |
| Human baseline | Near 100% (counting 2-10 objects is trivial for humans) |

## @xeophon's Key Insight

> **"Ultra-simple counting benchmark. Tests one thing on one level. Data quality is excellent."** — @xeophon, Part 14 of the Benchmarks & Evals series (2025-05-20)

Xeophon praises CountBenchQA for doing exactly one thing and doing it well. In an era of increasingly complex, multi-dimensional benchmarks, CountBenchQA stands out for its narrow scope and impeccable data quality. It serves as a "sanity check" — if a vision-language model can't count to ten, it has a fundamental perception problem that no amount of reasoning capability can compensate for.

## Strengths

- **Exceptional data quality**: Every single image was manually verified by a human. There is virtually no label noise or ambiguity
- **Ultra-focused scope**: Tests exactly one capability — object counting — making it impossible to "cheat" with reasoning tricks or prior knowledge
- **Balanced distribution**: Equal representation across counts 2-10 prevents models from exploiting base rates
- **Diagnostic value**: Failure on CountBenchQA reveals fundamental visual perception deficits. A model scoring below 90% has a real counting problem, not an ambiguous interpretation issue
- **No saturation concerns**: Because the task is well-defined with a clear success criterion, the benchmark doesn't become less useful as models improve — it simply reveals which models have basic counting competence
- **Simple to evaluate**: Answers are integers 2-10, making evaluation trivially exact-match
- **Multi-group provenance**: The benchmark has been independently validated by multiple research groups (original authors at Google/TAU, PaliGemma team, HF dataset compiler)

## Weaknesses

- **Extremely narrow scope**: Only tests one capability. High performance on CountBenchQA tells you nothing about reasoning, language understanding, or complex visual tasks
- **Limited to small counts**: Only tests counting up to 10 objects. Real-world counting tasks often involve much higher counts
- **Single question template**: All questions follow the identical "How many X are there in the image?" format, so models may learn to exploit this template
- **No difficulty gradation**: All tasks are at the same cognitive level — there's no progression from easy to hard
- **Small dataset**: With only ~500 images, statistical significance for small score differences is limited
- **Not a standalone evaluation**: CountBenchQA is useful only as a diagnostic tool within a broader evaluation suite

## Representative Examples

| Image Description | Question | Answer |
|-------------------|----------|--------|
| Four crochet potholders on white background | How many crochet potholders are there in the image? | 4 |
| Set of six flowers in pots, blue background | How many flower pots are there in the image? | 6 |
| Digital illustration of nine baseball players | How many baseball players are there in the image? | 9 |
| Two double beds in a furnished bedroom | How many double beds are there in the image? | 2 |
| Set of ten Christmas cards | How many Christmas cards are there in the image? | 10 |

## Usage

CountBenchQA is best used as a **diagnostic inclusion** in a broader evaluation suite. It answers the question: "Can this model reliably count objects in images?" A model that performs poorly here has a fundamental vision perception issue. A model that performs well has cleared a basic bar but hasn't demonstrated anything beyond elementary visual competence.

The benchmark is available on HuggingFace:
```python
from datasets import load_dataset
dataset = load_dataset("vikhyatk/CountBenchQA", split="test")
```

## Related Pages

- [[concepts/ai-benchmarks-evals-overview|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
- [[concepts/multimodal/_index|Multimodal AI]] — Broader vision-language model evaluation landscape

## See Also

- [[concepts/chartqa]] — Another vision-language benchmark with more complex chart reasoning (but noisier data)
- [[concepts/hle]] — The opposite end of the spectrum: extremely hard, multi-domain reasoning

## Sources

- Paiss, R., Ephrat, A., Tov, O., Zada, S., Mosseri, I., Irani, M., Dekel, T. (2023). "Teaching CLIP to Count to Ten." ICCV 2023. [arXiv:2302.12066](https://arxiv.org/abs/2302.12066)
- Beyer, L., Steiner, A. et al. (2024). "PaliGemma: A versatile 3B VLM for transfer." [arXiv:2407.07726](https://arxiv.org/abs/2407.07726)
- [CountBenchQA HuggingFace Dataset](https://huggingface.co/datasets/vikhyatk/CountBenchQA) — compiled by @vikhyatk
- @xeophon (Florian Brand), "AI Benchmarks & Evals — Part 14: CountBenchQA" (2025-05-20)
