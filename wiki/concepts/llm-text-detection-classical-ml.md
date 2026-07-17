---
title: "LLM Text Detection with Classical Machine Learning"
created: 2026-07-17
updated: 2026-07-17
type: concept
tags: [ai-detection, ai-content-detection, text-generation, llm-output, safety, classifiers, benchmark, research, hn-popular, adversarial, methodology, disinformation]
sources: [raw/articles/2026-03-01_llm-text-detection-classical-ml.md]
---

# LLM Text Detection with Classical Machine Learning

## Overview

LLM text detection using classical machine learning refers to the use of traditional ML algorithms — such as Support Vector Machines (SVM), Random Forests, and XGBoost — trained on stylometric and statistical features to distinguish human-written text from LLM-generated output. This approach, demonstrated effectively in a March 2026 blog post by lyc8503 (204 HN points, 147 comments), shows that classical ML can be competitive with deep learning-based detectors for AIGC (AI-Generated Content) detection tasks.

The core insight is that mainstream LLMs as of early 2026 exhibit strong, consistent statistical patterns in their output — sentence length distributions, vocabulary richness, punctuation patterns, part-of-speech sequences, and other surface-level text features — that can be exploited by relatively simple models. This stands in contrast to the assumption that detecting LLM text requires equally sophisticated neural architectures.

## Methodology

### Feature Engineering: Stylometric Features

Rather than using raw text or learned embeddings, the classical ML approach extracts handcrafted stylometric features from text samples. These include:

- **Lexical features**: word and character n-gram frequencies, type-token ratio (vocabulary richness), hapax legomena ratio (words appearing only once), average word length
- **Syntactic features**: part-of-speech (POS) tag distributions, parse tree depth, function word frequencies
- **Structural features**: sentence length distribution (mean, variance, percentiles), paragraph length patterns, punctuation frequency and placement
- **Statistical features**: entropy measures, perplexity estimates from simpler language models, burstiness metrics (how evenly words are distributed)
- **Readability metrics**: Flesch-Kincaid grade level, Gunning Fog index, SMOG index

These features capture the "fingerprint" of a text's style at a level of abstraction that survives changes in topic, domain, and specific word choices.

### Models Tested

The original blog post by lyc8503 evaluated three classical model families:

| Model | Characteristics | Performance Notes |
|---|---|---|
| **SVM (Support Vector Machine)** | Linear and RBF kernels; well-suited for high-dimensional sparse feature spaces | Strong baseline; good generalization with limited data |
| **Random Forest** | Ensemble of decision trees; handles non-linear feature interactions well | Robust to feature scaling differences; provides feature importance rankings |
| **XGBoost** | Gradient-boosted trees; state-of-the-art for tabular data | Highest accuracy in many configurations; sensitive to hyperparameter tuning |

All three models were implemented using scikit-learn and trained on paired datasets of human-written and LLM-generated web fiction text.

### Data Generation and Training

The training pipeline involved:

1. **Human text corpus**: Web fiction chapters from publicly available sources, representing natural human writing styles across multiple authors
2. **LLM-generated corpus**: Text produced by prompting mainstream LLM APIs (GPT-4 class models, Claude, and others) to write fiction passages in similar genres
3. **Feature extraction**: Stylometric features computed for both corpora, producing a tabular dataset where each row is a text sample and each column is a stylometric measurement
4. **Train/test split**: Standard holdout validation with careful author-level separation to prevent leakage

A notable aspect of the approach was the **JavaScript implementation** for browser-based deployment, allowing real-time detection without server-side computation. The trained model parameters (SVM coefficients, tree structures) were exported and reimplemented in client-side JavaScript.

## Results

The classical ML approach demonstrated strong detection performance:

- **Accuracy**: High classification accuracy (comparable to deep learning approaches) on held-out test data
- **Cross-domain generalization**: Features generalized across different fiction genres and writing styles
- **Efficiency**: Models were lightweight (~hundreds of KB for the exported JS implementation) and ran in milliseconds in the browser, unlike GPU-dependent neural detectors
- **Interpretability**: Feature importance analysis revealed which stylometric signals were most discriminative — sentence length variation and function word frequencies were consistently top features

A key finding was that **LLM-generated text is more statistically homogeneous** than human writing. Human authors exhibit greater variance in sentence structure, vocabulary choice, and stylistic patterns, while LLM output tends toward a narrower, more predictable distribution along these axes.

### Attack and Defense

The blog post also explored adversarial bypass techniques:

1. **Translation round-trip method**: Translating LLM-generated text to another language and back to English — partially degraded detection accuracy but did not fully defeat the classifier
2. **LLM prompt method**: Instructing the LLM to "write like a human" or mimic specific stylistic quirks — showed some success at evasion but reduced output quality

These findings highlight an ongoing [[evaluation/red-teaming-adversarial-eval|red-teaming and adversarial evaluation]] dynamic, where detectors and evasion techniques co-evolve.

## Implications for AI Safety

Classical ML text detection has several implications for [[ai-slop|AI slop]] mitigation and content integrity:

- **Low-cost deployment**: Unlike neural detectors requiring GPU inference, classical models can run anywhere — browsers, content moderation pipelines, edge devices — making them practical for large-scale screening
- **Transparency**: Feature-based models are inherently more interpretable than neural black boxes, allowing content platforms to explain why content was flagged
- **Complementary approach**: Classical and deep learning detectors can be combined as an ensemble, with classical models serving as a fast first-pass filter
- **Data efficiency**: Training requires far fewer samples than fine-tuning a neural classifier, making it accessible to smaller organizations and researchers

However, limitations include vulnerability to adversarial rewriting (as demonstrated in the attack section), language-specificity (stylometric patterns vary by language), and the ongoing arms race as LLM outputs become more human-like over time.

## Comparison to Deep Learning Approaches

Classical ML detection differs from neural/[[deep-learning]] approaches in several dimensions:

| Aspect | Classical ML (Stylometric) | Deep Learning (Neural) |
|---|---|---|
| **Feature source** | Handcrafted stylometric features | Learned embeddings from raw text |
| **Model size** | KB to MB range | MB to GB range |
| **Training data needed** | Hundreds to thousands of samples | Tens of thousands to millions |
| **Inference speed** | Sub-millisecond per sample | GPU-dependent, millisecond+ range |
| **Interpretability** | High (explicit feature importance) | Low (black box) |
| **Adversarial robustness** | Moderate (features are harder to directly optimize against) | Variable (susceptible to embedding-space attacks) |
| **Deployment cost** | Near-zero (runs in browser) | Requires GPU/compute infrastructure |

The classical ML approach challenges the assumption that complex problems always require complex solutions. For AIGC detection specifically, surface-level statistical patterns may be sufficient when the goal is screening rather than forensic certainty. This aligns with broader [[evaluation/ai-benchmarks-and-evals|benchmark and evaluation]] philosophy that appropriate metrics should match the deployment context — a fast, cheap, interpretable classifier may be more useful in production than a slightly more accurate but expensive neural model.

## Current Debates

- **Sustainability of the approach**: As LLMs improve, will stylometric signals persist or vanish? Some research suggests that even advanced models retain measurable statistical signatures distinct from human writing
- **Language and domain specificity**: Stylometric features optimized for English web fiction may not transfer to technical writing, academic prose, or non-English languages without retraining
- **Arms race dynamics**: The detection-evasion cycle mirrors broader [[ai-safety|AI safety]] concerns about the difficulty of reliably monitoring AI outputs

## References

- lyc8503. "Detecting LLM-Generated Web Fiction with 'Classical' Machine Learning (AIGC Text Detection)." March 1, 2026. https://blog.lyc8503.net/en/post/llm-classifier/
- Online Demo: https://lyc8503.github.io/AITextDetector/
- HN Discussion: https://news.ycombinator.com/item?id=48936880
