---
title: "LLM Query Understanding — Cheat at Search (Slides)"
author: Doug Turnbull (SoftwareDoug)
date_ingested: 2026-05-20
date: 2026-05-19
source: https://docs.google.com/presentation/d/1sAmb4NoDOFWXM3WiQGmgbU4e0X5Za6gAMbv1coYLYuw/edit
type: slides
tags:
  - query-understanding
  - search
  - embeddings
  - llm
  - ecommerce-search
  - synonym-extraction
  - category-classification
  - bm25
---

# LLM Query Understanding — Cheat at Search

**Author:** Doug Turnbull (SoftwareDoug / softwaredoug.com)
**Context:** Guest lecture for Turnbull & Trey Grainger's AI-powered search class, May 2026
**Source:** [Google Slides](https://docs.google.com/presentation/d/1sAmb4NoDOFWXM3WiQGmgbU4e0X5Za6gAMbv1coYLYuw/edit)
**Companion course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch) — rated 4.7/5 from 74+ reviews
**Lecture transcript:** [[transcripts/2026-05-20_softwaredoug_cheat-at-search-llm-query-understanding-lecture|Cheat at Search — LLM Query Understanding (Lecture Transcript)]]

## Goals

1. What is Query Understanding? Why do it?
2. How LLMs fit into the query understanding landscape
3. Run through several query classification scenarios
4. Latency considerations

---

## 1. What is Query Understanding?

Mapping **free-text user queries** to **structured, controllable attributes** of documents (color, category, brand, material, etc.) to improve search ranking.

**Example:**
| Query | Extracted Attributes |
|---|---|
| `crimson suede couch` | color:red, material:suede, category:furniture |
| `purple Ashley recliner` | color:purple, brand:Ashley, category:furniture |
| `desk for kids` | category:furniture |

> "We have queries… we have documents with properties (category, color, brand, etc)."

---

## 2. Why Structured Queries Over Pure Embeddings?

### Embedding Collapse (Hubness)

General-purpose embedding models are trained on vast, diverse data. In a **narrow domain** (e.g., one retailer's furniture catalog), everything looks similarly similar:

```
similarity("blue couch", "a couch")      = 0.72
similarity("blue couch", "a blue chair") = 0.71
similarity("blue couch", "a blue couch") = 0.75
```

Where do you draw the filtering threshold? (0.73? 0.74?) The embedding space collapses — all items in your tiny domain are close together in the broad embedding space.

### Chat-Style Queries

Modern conversational interfaces produce long, verbose queries:

> "Hi I am curious for a couch that would fit into a sunny living room. I actually want a sky blue one. Well my father in law might visit and need a place to sleep."

This generates a query like `"Bright, sky-blue sleeper sofa for living room"` — with insufficient training data for a good multi-modal embedding model.

### Fine-Tuning Is Expensive

Gathering domain-specific training data, retraining, and deploying an embedding model is skill-intensive and expensive. And even after fine-tuning, you still can't trivially "cut off" irrelevant results with a threshold.

### The Alternative: Structured Query Understanding

Turn chat into a structured object:

```json
{
  "room": "living room",
  "color": "sky blue",
  "item": "sleeper sofa",
  "attributes": ["sleeper", "twin-sized", …]
}
```

Treat each attribute as its own filtering/similarity function.

**Benefits:**
- Simple LLMs can reliably perform classic NLP
- Human-manageable, interpretable ranking signals
- Usable as tool inputs for both agents and humans
- Can still fine-tune for specific tasks

---

## 3. Five Types of Query Understanding

| Type | How It Works | Characteristics |
|---|---|---|
| **Rules** | PM/merchandiser manually assigns attributes | Human curation, scales poorly |
| **Historical** | Aggregate click data → most common attribute for a query | `SELECT query, COUNT(color) … GROUP BY query` |
| **ML-Based** | Train classifier on historical data (features → attribute) | Requires labeled training data |
| **Embedding-Based** | Embed query + candidate attributes → nearest neighbor | Query → vector → compare with attribute vectors |
| **Prompt-Based** | LLM extracts values directly via structured output | **Focus of this talk** |

---

## 4. LLM Query Understanding in Practice

### 4.1 Synonym Extraction + BM25 Boosting

**Structured output via Pydantic + cheap model (gpt-4.1-nano):**

```python
class SynonymMapping(BaseModel):
    phrase: str = Field(description="Original phrase from query")
    synonyms: List[str] = Field(description="Synonyms for the phrase")

class QueryWithSynonyms(BaseModel):
    synonyms: List[SynonymMapping]

resp = openai.responses.parse(
    model="gpt-4.1-nano",
    input=[
        {"role": "system", "content": "You are a helpful AI assistant extracting synonyms from queries."},
        {"role": "user", "content": f"Extract synonyms from the following query: {query}"}
    ],
    text_output=QueryWithSynonyms
)
```

**AutoEnricher wrapper:**

```python
enricher = AutoEnricher(
    model="openai/gpt-4.1-nano",
    system_prompt="You are a helpful AI assistant extracting synonyms from queries.",
    response_model=QueryWithSynonyms
)
enricher.enrich("Extract synonyms for query: red shoes")
```

**Example output for `"rack glass"`:**
```
rack → [shelf, stand, holder]
glass → [cup, cupware, drinking glass]
```

**Integration into BM25:** For each synonym phrase, tokenize and add its BM25 score to the overall query score:

```python
for mapping in synonyms.synonyms:
    for phrase in mapping.synonyms:
        tokenized = snowball_tokenizer(phrase)
        bm25_scores += index['product_name_snowball'].array.score(tokenized)
        bm25_scores += index['product_description_snowball'].array.score(tokenized)
```

**Result:** NDCG improved from 0.541 (plain BM25) → 0.546 (synonym-boosted BM25).

### 4.2 Category Classification

#### Few-Label Classification

```python
Category = Literal['Furniture', 'Rugs', 'Décor & Pillows', 'Outdoor', 'Lighting', …]
```

Straightforward when the category set is small (~10-50 labels).

#### Deep Multi-Label Classification

**Challenge:** 10K+ fully-qualified categories like `'Furniture / Living Room Furniture / Console Tables'`.

**Solution:** LLM returns best-matching full paths:

```python
class QueryClassification(BaseModel):
    classification: list[FullyQualifiedClassifications] = Field(
        description="A classification for the product. Use 'No Classification Fits' if unclear."
    )
```

**Search boost:** For each returned category, tokenize and add constant boost to matching documents:

```python
for category in classified.categories:
    tokenized_category = snowball_tokenizer(category)
    category_match = self.index['category_snowball'].array.score(tokenized_category) > 0
    bm25_scores[category_match] += self.category_boost
```

**Token cost (initial):** Input tokens: 5,998, Output tokens: 49 — expensive with full label list.

#### Cost Optimization: Dynamic Pydantic Enums

1. Run BM25 query → get top 300 results
2. Extract most frequent category hierarchies (top 25)
3. Create a **dynamic Pydantic enum** on the fly:

```python
def make_classifier_model(labels: list[str]) -> type[BaseModel]:
    LabelEnum = Enum('LabelEnum', {l: l for l in labels})
    Model = create_model("QueryClassification",
        __doc__="A classification of the query.",
        classification=(list[LabelEnum], Field(...)))
    return Model
```

4. Classify using cheap model (gpt-4.1-nano)

**Result with caching:** Input tokens ~485 (dramatic reduction from 5,998).

### 4.3 Combined QU Pipeline

The full pipeline:

```
QUERY → [Cache Lookup] → [BM25 Top 300] → [Dynamic Enum Build] → [LLM Classify] → [Apply Boosts]
         ↓ hit                                              ↓ miss
      CACHED QU                                        LLM QU + CACHE
```

### 4.4 Caching Strategies

- **Static tier:** Frequently seen queries cached with pre-computed attributes
- **Dynamic tier:** Unseen queries → LLM → cache for future
- **Cost:** gpt-4.1-nano is cheap enough to run on 100K+ queries economically

---

## 5. Results Summary

| Approach | NDCG | Notes |
|---|---|---|
| Plain BM25 | 0.541 | Baseline lexical search |
| BM25 + Synonym Extraction | 0.546 | Tiny lift from LLM synonyms |
| BM25 + Category Classification | ~0.608 | Significant lift on Wayfair queries |

> "Query Understanding is essential for mixing lexical and embedding retrieval."

---

## 6. Key Takeaways

1. **Embedding collapse is real** — in narrow domains, pure embedding search struggles to distinguish relevant from irrelevant
2. **Structured query understanding is a practical fix** — simple LLMs can reliably extract structured attributes
3. **LLMs are ideal for QU** — cheap models (gpt-4.1-nano) can handle synonym extraction, category classification, and attribute extraction at scale
4. **Cost optimization is essential** — dynamic Pydantic enums from BM25 top-N reduce token costs by 10x+
5. **QU makes BM25 better, and BM25 makes QU cheaper** — a virtuous cycle
6. **Caching matters** — cache frequent queries, LLM for the long tail

---

## Companion Resources

- **Course:** [Cheat at Search (Maven)](https://maven.com/softwaredoug/cheatatsearch)
- **Author:** [softwaredoug.com](http://softwaredoug.com)
- **Related:** [[entities/doug-turnbull]], [[entities/doug-turnbull-core-ideas]], [[concepts/query-understanding]], [[concepts/bm25]], [[concepts/vector-search]]
