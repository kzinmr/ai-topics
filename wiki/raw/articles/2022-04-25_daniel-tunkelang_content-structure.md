---
title: "Content Structure"
author: Daniel Tunkelang
source: https://medium.com/content-understanding/content-structure-34aa2bd9d134
date: 2022-04-25
publication: Content Understanding (Medium)
tags:
  - content-understanding
  - information-retrieval
  - search
---

# Content Structure

The unit of content a user seeks often doesn't match the unit in the search index (a whole document). Content structure bridges this mismatch.

## Content Summarization

Creates a compact representation of what a document is about:

### Natural Summaries
- **Titles**: Short but may be generic/clickbait
- **Abstracts**: Built-in "tl;dr" for formal documents
- **Limitations**: Too brief for indexing; designed for humans, not inverted index retrieval

### Automatic Summarization
1. **Extractive**: Select existing tokens/phrases/sentences (tf-idf, keyword extraction, deep learning)
2. **Abstractive**: Generate new sentences (seq2seq, hot deep learning area)

## Content Segmentation

Searchers often need only part of a document:

### Natural Structure
Sentences, paragraphs, sections, tables of contents — long docs cover multiple information needs.

### Approaches
1. **Heuristic/Rules**: Split on formatting (headings, line breaks) — works when consistent
2. **ML-based**: HMM → CRF → LSTM/deep learning for boundary detection
3. **Search Result Snippets** (Query-biased Summaries): Dynamic, query-dependent extraction — flexible but expensive at query time

> "In a world where users increasingly expect search engines to be 'answer engines', it's important to invest in understanding content structure."

## Key Principle

Segment relationships must be preserved — parts of documents should inherit attributes like authorship from their parent documents.
