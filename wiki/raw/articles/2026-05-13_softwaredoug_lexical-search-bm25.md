---
title: "Lexical Search & BM25 — Cheat at Search Essentials"
url: https://docs.google.com/presentation/d/1l6TM7WvB-W1yFVr5yZNQ7Is70s_UN-cuEV5yK5lbMH0/edit
source: softwaredoug.com
author: Doug Turnbull (@softwaredoug)
published: 2026-05-13
date_ingested: 2026-05-13
type: slide_deck
tags: [information-retrieval, search, lexical-search, bm25, tokenization]
---

# Lexical Search & BM25 — Cheat at Search Essentials

Doug Turnbull's Maven course "Cheat at Search Essentials" — Lexical Search & BM25 module.
Live training starts May 18, 2026. Discount code: `harness`.
Slides 1-6 are template/boilerplate; slides 7+ are the teaching content.

---

## Tokenization

**Basic concept:** Lexical search is about token matching. Documents and queries are tokenized, then matched through an inverted index.

```
"Hi this is Doug, I'd like to complain about the weather",
"Doug this is Tom, support for Earth's Climate, how can we help?"
```

Tokenizer outputs:
```
[Hi] [this] [is] [Doug] …
[Doug] [this] [is] [Tom]...
```

**Inverted index:**
```
terms:
   Doug:     documents: [0, 1]
   weather:  documents: [0]
   …
```

**Naive whitespace tokenizer — fails with punctuation:**
```python
def whitespace_tokenize(text):
    return text.split()

whitespace_tokenize("Mary had a little lamb")
# ['Mary', 'had', 'a', 'little', 'lamb']

whitespace_tokenize("Doug, can we help you?")
# ['Doug,', 'can', 'we', 'help', 'you?']  # Punctuation not removed!
```

Query "Doug complaint" won't match doc 2 because `Doug,` ≠ `Doug`.

**Better tokenizer — lowercase, strip punctuation:**
```python
def better_tokenize(text):
   lowercased = text.lower()
   without_punctuation = lowercased.translate(str.maketrans('', '', punctuation))
   split = without_punctuation.split()
   return split

better_tokenize("Doug, that weirdo?"), better_tokenize("Oh this is about doug?")
# (['doug', 'that', 'weirdo'], ['oh', 'this', 'is', 'about', 'doug'])
```

**Tokenization Questions:** stemming to root forms? Synonyms? Entities? Etc.

**Key insight:** "Only as smart as your tokenizer" — lexical search quality is fundamentally bounded by tokenizer quality.

---

## Query Processing

**AND (all terms must match):**
```python
query_tokenized = better_tokenize(QUERY)
matches = np.zeros(len(msgs), dtype=np.bool)
for query_token in query_tokenized:
   matches &= (msgs['msg_tokenized'].array.score(query_token) > 0)
```

**OR (any term matches):**
```python
for query_token in query_tokenized:
   matches |= (msgs['msg_tokenized'].array.score(query_token) > 0)
```

**Search engines use complex query DSLs** — e.g., Elasticsearch multi_match with field lists, operators, etc. You need to understand how the DSL translates to token matching across fields.

**Key insight:** "Ideal: tight control at search time" — maximum control over how queries are structured yields best results.

---

## Scoring: From TF to TF*IDF

**Core similarity function interface:**
```python
def similarity(term_freqs, doc_freqs, doc_lens, avg_doc_lens, num_docs) -> np.ndarray:
    # "How to score single term in field, given these statistics"
```

**Simple Term Frequency (TF):**
```python
def term_counts(term_freqs, doc_freqs, doc_lens, avg_doc_lens, num_docs):
   return term_freqs  # Just count occurrences
```

Problem: mentions "doug" twice scores same as document with both "doug" AND "complaint".

**TF*IDF — emphasize rare terms:**
```python
def tf_over_df(term_freqs, doc_freqs, doc_lens, avg_doc_lens, num_docs):
   return term_freqs / doc_freqs  # Divide by how many docs contain this term
```

Doc freqs = how many documents does this term occur in. Rare terms get higher weight.

---

## Multi-field Search

**Naive sum across fields:**
```python
fields = ["name", "msg_tokenized"]
scores = np.zeros(len(msgs))
for query_token in query_tokenized:
   field_scores = np.zeros(len(msgs))
   for field in fields:
       score = msgs[field].array.score(query_token, similarity=tf_idf)
       field_scores += score  # Accumulate
   scores += field_scores
```

Problem: biases toward docs matching in multiple fields (even if not the most relevant match).

**Better: DisMax (take max per term):**
```python
for query_token in query_tokenized:
   field_scores = np.zeros(len(msgs))
   for field in fields:
       score = msgs[field].array.score(query_token, similarity=tf_idf)
       field_scores = np.maximum(field_scores, score)  # Take max!
   scores += field_scores
```

aka "term-centric" search — used in Elasticsearch, Solr, OpenSearch.

---

## BM25

**Problem with raw TF*IDF:** Term frequency should SATURATE — the 19th mention of a term is not as important as the 1st.

**BM25 formula — three components:**

1. **Saturated term frequency:** `tf → tf / (tf + k1)` (approaches 1.0 asymptotically)
2.  **Logarithmic doc frequency:** `log(1 + (num_docs - df + 0.5) / (df + 0.5))` — accounts for diminishing returns of rarity
3.  **Length bias:** `length_bias = (1 - b + b * dl / avg_dl)` — "Skywalker" in a tweet is very important; "Skywalker" in a book is statistically expected

**Combined:** `tf → tf / (tf + k1 * length_bias)`

**BM25 parameters:**
- `k1` — low k1 = saturate fast (controls TF saturation curve)
- `b` (0 to 1) — high b = more length influence

---

## BM25F — Multi-field BM25

**Problem:** Combining BM25 across fields naively has issues. "doug" in a "topics" field (rare) gets unnaturally high IDF compared to "doug" in "msgs" field (common).

**Solution — BM25F:**
1. **Combined TF:** Saturate term frequencies across all fields together
   ```
   saturated_tf = (doug_term_topics + doug_term_msgs) / (k1 + doug_term_topics + doug_term_msgs)
   ```
2. **Combined docfreq:** Take max IDF across fields
   ```
   doc_freq = max(topics.idf('doug'), msgs.idf('doug'))
   ```

**BM25F = saturated_tf × bm25_idf(doc_freq)**

---

## BM25 in the Age of Agents

**What is lexical search good for?**
- ASSUMING tokenization accurately represents a "match"
- THEN BM25 tells us how much this passage is **about** that match
- **BM25 ≈ "Relevance Given Match"**

**BM25 ≠ all relevance** — sometimes relevance is not about a "match" (e.g., "Ubik Synopsis" query → no clear term match)

**"But agents help with the 'semantics'"** — Doug's vision: Agent uses BM25 as a tool. LLM handles semantic understanding, BM25 handles precise term-based scoring.

**Course discount code:** `bm25rocks`
**Course:** http://softwaredoug.com/course

---

## Colab Notebook

Course exercises use this notebook:
https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1
