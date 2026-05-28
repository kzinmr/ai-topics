---
title: "BM25F from scratch"
url: https://softwaredoug.com/blog/2025/09/18/bm25f-from-scratch
source: softwaredoug.com
author: Doug Turnbull (@softwaredoug)
published: 2025-09-18
date_ingested: 2026-05-28
type: blog_post
tags: [information-retrieval, bm25, bm25f, lexical-search, multi-field-search, elasticsearch]
---

# BM25F from scratch

Doug Turnbull's deep-dive blog post on multi-field BM25 (BM25F), companion to his "Cheat at Search Essentials" training. Builds intuition from BM25 fundamentals, diagnoses two critical problems with naive multi-field BM25, and presents the two-step BM25F correction.

---

## BM25 Building Blocks

Three primary inputs drive relevance:

| Factor | Definition | Impact to score |
|--------|------------|-----------------|
| Term Frequency (TF) | How often a term appears in a document | Higher is better |
| Document Frequency (DF) | How rare the term is across the corpus | Lower (more specific) is better |
| Field Length | Number of terms in the field | Shorter fields give more weight to a match |

The classic `TF*IDF` comes from `TF / DF`. Over time, research refined how these ingredients combine, leading to BM25.

---

## BM25 Deconstructed

### 1. Document Frequency & IDF

Users perceive term specificity **non-linearly**. A term occurring in 2× fewer documents is NOT 2× more specific. BM25 uses logarithmic decay:

```python
def compute_idf(num_docs, df):
    """Calculate idf score from num_docs (index size) and df (a term's doc freq)"""
    return np.log(1 + (num_docs - df + 0.5) / (df + 0.5))
```

The drop-off is steep at first, then tapers.

### 2. Scaling Term Frequency by Document Length

A term appearing once in a novel vs. once in a tweet: completely different information content. BM25 scales TF so long documents count less:

```python
def scaled_tf(term_freq, doc_len, avg_doc_len, b=0.8):
    return (term_freq) / (1 - b + b * doc_len / avg_doc_len)
```

### 3. Term Frequency Saturation

Relevance **plateaus** after seeing a term multiple times — the 99th mention adds little beyond the 5th:

```python
def bm25_tf(termfreq, k1=1.2):
    return termfreq / (termfreq + k1)
```

### 4. Combined BM25 TF

Length normalization + saturation combined:

```python
def bm25_scaled_tf(term_freq, doc_len, avg_doc_len, b=0.8, k1=1.2):
    return (term_freq) / (term_freq + k1 * (1 - b + b * doc_len / avg_doc_len))
```

Full BM25 score: `score = IDF × bm25_scaled_tf`

---

## Problems with Fielded Search

Real search engines split indexes into fields (title, body, description). Each field has its own statistics. Naive BM25 across fields introduces two problems:

### Problem 1: Specificity (IDF Misrepresentation)

A term rare in one field gets erroneously high IDF. Example: searching "javascript book" — if "book" is rare in the `title` field, its IDF explodes:

```
"The big book on squirrels"     ← ranks high (book matches in title, no javascript!)
"C Programmers Book about Pointers"
"The missing iPhone book"
```

Naive per-field BM25 sum:
```
score = TF('title', 'book') * IDF('title', 'book')
      + TF('body', 'book') * IDF('body', 'book')
```

The title field's IDF for "book" doesn't reflect corpus-wide specificity.

### Problem 2: Double Counting TF

If we naively sum BM25 scores, each field's TF saturates **independently**, giving undue weight to "early" parts of the saturation curve in both fields:

| Match | Impact | Notes |
|-------|--------|-------|
| Title (tf=1) | High | Early in saturation curve |
| Body (tf=100) | High but diminishing | Farther in curve |
| **Total** | **2× High** | **Double counted!** |

What we want: Title+Body (tf=101) → a single score deep in saturation.

But TF=1 in a 5-word title ≠ TF=100 in a 10,000-word body. We must **scale each TF by its field's length** before summing, then saturate once.

---

## BM25F: The Two-Step Solution

### Step 1: Blend Document Frequencies

Use the **maximum DF across fields** for IDF computation:

```python
combined_doc_freq = max(DF('title', 'book'), DF('body', 'book'))
blended_idf = compute_idf(corpus_len, combined_doc_freq)
```

Elasticsearch's `cross_fields` query mode does exactly this DF blending.

### Step 2: Normalize, Scale, Saturate Together

1. Apply `scaled_tf` to each field's TF **individually** (using that field's length)
2. **Sum** the scaled frequencies
3. Apply `bm25_tf` (saturation) to the **sum**

```python
bm25f_tf = bm25_tf(
    scaled_tf(TF('title', 'book'), title_len, avg_title_len) +
    scaled_tf(TF('body', 'book'), body_len, avg_body_len)
)
```

### Final BM25F Score

```python
combined_doc_freq = max(DF('title', 'book'), DF('body', 'book'))
blended_idf = compute_idf(corpus_len, combined_doc_freq)

bm25f_tf = bm25_tf(
    scaled_tf(TF('title', 'book'), title_len, avg_title_len) +
    scaled_tf(TF('body', 'book'), body_len, avg_body_len)
)

bm25f = blended_idf * bm25f_tf
```

---

## Key Insights

- Elasticsearch `cross_fields` = Step 1 only (DF blending) — "80% solution"
- True BM25F = Steps 1 + 2 (DF blending + unified TF saturation after per-field length normalization)
- Doug's closing questions: How would multi-field sparse transformer models work? Is DF the only/best way to compute term specificity? Tokenization remains a critical design point — "only as smart as your tokenizer"

## Related

- Cheat at Search Essentials (Maven course): http://maven.com/softwaredoug/cheat-at-search
- Elasticsearch cross_fields mode
- Sparse transformer models (SPLADE, etc.)
