---
title: "Content Annotation"
author: Daniel Tunkelang
source: https://medium.com/content-understanding/content-annotation-13b7c43ee5c7
date: 2022-03-17
publication: Content Understanding (Medium)
tags:
  - content-understanding
  - information-retrieval
  - search
---

# Content Annotation

Content annotation is a **reductionist** approach to content understanding — focusing on specific words or phrases ("spans") rather than the document as a whole. It complements **content classification** (holistic approach).

## Entity Recognition

The most common form of content annotation. Entities are members of a **controlled vocabulary**, optionally typed (company names, locations) or untyped (technical terms). Two main approaches:

### Rules-Based
1. **String matching** from a table/dictionary — simple but effective for "San Francisco, CA" patterns. Limited by ambiguity (Phoenix: city vs. myth; 40+ US cities named "Springfield")
2. **Regular expressions** — useful for measurements ("128 GB", "3 ft"), phone numbers. Growing complexity with edge cases. Example phone regex evolved from simple `[0-9]{3}-[0-9]{3}-[0-9]{4}` to a 200+ char monstrosity handling international variants, extensions

### Advantages of Rules for Annotation (vs. Classification)
- Errors in annotation are less damaging than misclassifying an entire document
- Easier to craft accurate token-level rules
- Trade-offs remain between precision, recall, and complexity

## Machine Learning Approaches

**Part-of-Speech (POS) Tagging**: Using spaCy, NLTK. Requires clean, grammatical text.

**Entity Recognition with ML**:
- Traditional: HMM, CRF
- Modern: Bidirectional LSTM-CRF, seq2seq models
- Requires labeled training data (tools like Prodigy help)
- Harder than ML classification due to per-token decisions
- Works best on short fields (document/product names)

## Key Insight

> "Simple rules-based approaches are often good enough for many annotation problems. Still, this is a hot area for machine learning, so keep track of innovations in sequence learning methods."
