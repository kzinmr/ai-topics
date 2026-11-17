---
title: "Bookmark: François Fleuret — The Little Book of Deep Learning (v1.3)"
type: bookmark_note
created: 2026-11-16
date_ingested: 2026-11-16
source: x_bookmarks
source_url: https://x.com/__paleologo/status/2121771323969966453
author_handle: "@__paleologo"
bookmarked_tweet_id: "2121771323969966453"
bookmarked_at: 2026-11-15
canonical_urls:
  - https://fleuret.org/lbdl/
  - https://fleuret.org/public/lbdl.pdf
tags: [deep-learning, education, open-educational-resource]
---

# Bookmark: The Little Book of Deep Learning (Fleuret)

## Original bookmark text (@__paleologo, 2026-11-15)

> Long post.
>
> I am in still in the habit of "writing" technical notes by querying Astra or Fable (or having them converse with each other). Most notes or books are finance-related. I have a couple on AI. There's a free book by F. Fleuret titled "The little book of Deep Learning" [link to photo]

The tweet only contained a photo link (`pic.x.com/5KyaeFVr42`); the book reference points to François Fleuret's free book. Content below scraped from the official book page (fleuret.org/lbdl/) on 2026-11-16.

## The Little Book of Deep Learning — official page content

This book is a short introduction to deep learning for readers with a STEM background, originally designed to be read on a phone screen. This is the v1.3 updated on May 12th, 2026.

It is distributed under a non-commercial Creative Commons license and was downloaded more than 1,000,000 times since its release in April 2023.

- Download the phone-formatted pdf: https://fleuret.org/public/lbdl.pdf (4.7 MB)
- Buy a $9 paperback copy on lulu.com
- Download a printable A5 booklet pdf: https://fleuret.org/public/lbdl-a5-booklet.pdf
- Download counter: https://fleuret.org/cgi-bin/lbdl.cgi

Note that the version sold on Amazon and other on-line platforms for $40 is "unauthorized": someone stole the content and sells it. Preventing this would require to sue and I have better things to do with my time.

### Updates

**V1.3 (May 12, 2026)**
- Many typos and phrasing fixes with the help of LLMs.
- Section 3.8. Added a section about large-scale training.

**V1.2 (May 19, 2024)**
- Chapter 8. New chapter on low-resource methods (prompt engineering, quantization, low-rank adapters, model merging).
- Miscellaneous. Changed "meta parameter" to "hyper parameter".
- Section 3.6. Added a sub-section about fine-tuning.
- Section 4.8. Added the note about the quadratic cost of the attention operator.
- The missing bits. Added a note about the O(T) of standard RNNs vs. the O(log T) of methods that leverage parallel scan.

**V1.1.1 (Sep 20, 2023)**
- Section 4.2. Added a paragraph about the equivariance of convolution layers.
- Section 5.3. Fixed the description of the original Transformer, and modified Figures 5.6–5.9 accordingly.

**V1.1 (Sep 8, 2023)**
- Miscellaneous. Fixed minor typos and phrasings.
- Section 1.3. Reformulated the text to clarify that overfitting is not particularly related to noise, but to any properties specific to the training set.
- Section 3.2 / 3.4 / 3.7 / 4.5 / 4.6 / 6.6: figure and labeling fixes.
- Section 7.1. Added two paragraphs to introduce the notion of Reinforcement Learning from Human Feedback.
- The missing bits. Removed the fine-tuning sub-section (moved to Section 7.1).

## Author: François Fleuret (bio page, fleuret.org/francois/bio.html)

François Fleuret is Research Scientist at Meta Fundamental AI Research (FAIR) in the Core Learning and Reasoning team, and Full Professor and head of the Machine Learning group in the department of Computer Science at the University of Geneva, where he holds the chair of machine learning. He received his PhD in Mathematics from INRIA and the University of Paris VI in 2000, and his Habilitation degree in Mathematics from the University of Paris XIII in 2006. He has published more than 130 papers in peer-reviewed international conferences and journals, and is the author of the Little Book of Deep Learning, downloaded more than 600,000 times as of July 2024 (1,000,000+ by Nov 2026). He was Associate Editor of IEEE TPAMI (2012–2022), serves as Area Chair for NeurIPS, ICML, AAAI, and ICCV. He is the inventor of several ML patents, and co-founder of Neural Concept SA, a company specializing in deep learning solutions for engineering design. Main research interest: machine learning, with a particular focus on computational aspects and sample efficiency.

## Companion course: UNIGE 14x050 Deep Learning (fleuret.org/dlc/)

Slides, recordings, and handouts for Fleuret's deep-learning courses 14x050 (University of Geneva) and EE-559 (EPFL, until 2022). Thorough introduction to deep learning with PyTorch examples: ML objectives and challenges, tensor operations, automatic differentiation, gradient descent, deep-learning-specific techniques, generative/recurrent/attention models. Course originally developed at Idiap Research Institute in 2018. 1107 slides total; screencast subtitles generated with OpenAI Whisper.

## Note on LLM involvement

The v1.3 changelog explicitly credits LLMs for "many typos and phrasing fixes" — an example of an author using LLMs as a copy-editing assistant on a technical book.

## Table of contents (extracted from lbdl.pdf, v1.3, 189 pages)

- **Foundations**
  - Machine Learning: Learning from data; Basis function regression; Under and overfitting; Categories of models
  - Efficient Computation: GPUs, TPUs, and batches; Tensors
  - Training: Losses; Autoregressive models; Gradient descent; Backpropagation; The value of depth; Training protocols; The benefits of scale; Large-Scale Parallel Training *(new in v1.3)*
- **Deep Models**
  - Model Components: The notion of layer; Linear layers; Activation functions; Pooling; Dropout; Normalizing layers; Skip connections; Attention layers; Token embedding; Positional encoding
  - Architectures: Multi-Layer Perceptrons; Convolutional networks; Attention models
- **Applications**
  - Prediction: Image denoising; Image classification; Object detection; Semantic segmentation; Speech recognition; Text-image representations; Reinforcement learning
  - Synthesis: Text generation; Image generation
  - The Compute Schism *(Chapter 8, added v1.2)*: Prompt Engineering; Quantization; Adapters; Model merging
- **The missing bits** / Bibliography / Index
