---
title: "Long-Context Embedding Models are Blind Beyond 4K Tokens"
source: https://jina.ai/news/long-context-embedding-models-are-blind-beyond-4k-tokens/
date_published: 2025-03-07
authors: [Saahil Ognawala, Alex C-G]
source_site: Jina AI
type: raw_article
topics: [embeddings, long-context, evaluation, needle-in-haystack, query-expansion]
---

# Long-Context Embedding Models are Blind Beyond 4K Tokens

**Published:** March 07, 2025 by Saahil Ognawala, Alex C-G
**Core finding:** Embedding models lose their ability to distinguish relevant information from noise in contexts longer than ~4K tokens—even when exact lexical matches are present or queries are expanded. The problem is not semantic understanding but retrieval in long contexts.

---

## Key Excerpts & Quotes

> "Beyond 4K tokens, they're just rolling dice - even with exact lexical matches or query expansion, they can't tell signal from noise in long context."

> "At 8,000 tokens, there's minimal separation (0.001) and near-random discrimination, with an AUC of just 0.50."

> "The ability of an embedding model to find a needle in a haystack is affected far more by the size of the haystack (and placement of the needle in it) than the semantic formulation of the needle."

**Normalization formula:**

```
Normalized Similarity = cos(q, h) / cos(q, n)
```

where `q` = question embedding, `h` = haystack embedding, `n` = needle embedding.

**Query expansion example (100 extra terms added by an LLM):**

```
Which character has been to Dresden? Character: fictional character literary character protagonist antagonist figure persona role dramatis personae

Dresden: Dresden Germany; bombing of Dresden World War II historical fiction Kurt Vonnegut Slaughterhouse-Five city in Saxony Elbe River cultural landmark

Has been to: visited traveled to journeyed to presence in appears in features in set in takes place in location setting
```

---

## 1. Background & Motivation

Inspired by the **NoLiMA paper** (Feb 2025), which showed LLMs rely heavily on literal keyword matching and degrade on semantic leaps in long contexts, the authors investigate whether the same holds for **embedding models**. The central questions:

- How do embedding models perform on needle-in-a-haystack retrieval when forced to make semantic "one-hop" inferences (no literal keyword overlap)?
- Can **query expansion** mitigate the performance drop?

---

## 2. Experiment Setup

### Needles Construction

- **Traditional NIAH** uses literal matches (e.g., "Yuki lives in Dresden").
- **This study** replaces literal matches with **one‑hop variations** that require implicit knowledge (e.g., "Yuki lives next to the Semper Opera House" → Dresden).
- Two word‑orderings: **default** and **inverted** (e.g., "The Semper Opera House is next to where Yuki lives").
- Needles cover categories: dietary restrictions, medical conditions, language proficiency, professional background, locations/landmarks, etc.
  *Original literal‑match needles were only used as reference, not in experiments.*

### Haystacks Construction

- Haystacks built from 10 public‑domain books (≥50K tokens each) by concatenating random snippets (<250 tokens).
- Haystack lengths: 128, 256, 512, 1024, 2048, 4096, and **8192 tokens** (the model limit).
- One needle per haystack, placed at regular interval across 10 variations per length.
- **Total haystacks:** 3,234 (plus blank controls).
- Embedding model: **`jina-embeddings-v3`** with default text‑matching LoRA.

### Evaluation Metrics

**Primary:**
- **Normalized Similarity Score** = cosine(q,haystack) / cosine(q,needle) – accounts for model's tendency to under‑calculate similarity.
- **Comparative Ratio to Random Chance** – how often the correct haystack is preferred over a needle‑free random passage.

**Secondary:**
- **Separation Analysis** – mean difference between positive and negative passages; **AUC** (area under ROC curve).
- **Position Effects** – correlation, regression slope, and binned analysis by needle location.

---

## 3. Findings

### Sharp Degradation with Context Length

- Mean normalized similarity score drops **from 0.37 (128 tokens) to 0.10 (8K tokens)** – a non‑linear decline, steepest between 128 and 1K.
- Inverting the needle order has almost **no effect** on performance.
- Semantic categories vary: **location‑landmark** pairs hold up best; dietary/medical restrictions degrade most quickly.

### Approaching Random Chance

- The chance of picking the correct haystack over a random one falls toward **0.5 (pure randomness)** as context grows.
- At 8K tokens, the model is nearly as likely to select a random passage as the needle‑containing one.
- Some categories (e.g., dietary restrictions) drop **below** random chance even at shorter lengths.

### Separation Analysis: Near‑Zero Discrimination Beyond 4K

| Context Length | Mean Separation | AUC  |
|----------------|-----------------|------|
| 128 tokens     | 0.10            | 0.81 |
| 1,024 tokens   | 0.04            | 0.66 |
| 8,192 tokens   | 0.001           | 0.50 |

- Separation **declines by ~99%** from 128 to 8K; AUC reaches chance level (0.50).
- The ability to tell relevant from irrelevant content **collapses far more severely** than raw similarity scores suggest.

### Needle Position Matters

- Performance is **best when the needle is at the start** and **worst in the middle**.
- Clear U‑shaped curve across all context lengths — distance from query to needle is the strongest individual predictor.
- Correlation coefficient between needle position and normalized similarity: **r = -0.52**.
- Within the same haystack length + category, needle position explains **~20% of variance**.

### Query Expansion Fails

- Expanding each query with ~100 extra terms from an LLM (synonyms, related concepts) **did NOT improve retrieval**.
- In some cases, query expansion **made performance worse** (e.g., dietary restrictions at 1K tokens).
- When query expansion *did* help, gains were small (<5%) and inconsistent.

### Category‑Specific Analysis

**Top‑performing categories:**
- Location‑Landmark: strongest mean similarity (0.37 at 128, 0.21 at 8K)
- Language: stable at short lengths, degrades slower than average

**Worst‑performing categories:**
- Dietary restrictions: degrades fastest and most severely
- Medical conditions: performs worst at 8K
- Professional background: high variance, inconsistent

The same needle‑haystack distance yields dramatically different results depending on category — a location query at 1K tokens outperforms a dietary query at 128 tokens.

---

## 4. Implications for RAG and Long-Context Retrieval

### Practical Takeaways

1. **Chunk size matters.** Embedding models are effectively blind beyond ~4K tokens. Keep chunks short (512–1024 tokens) for retrieval.
2. **Don't count on long-context embeddings.** Models advertised as supporting 8K+ token encodings may embed that much text, but retrieval quality collapses long before hitting the limit.
3. **Query expansion is overrated.** Adding LLM‑generated context to queries provides negligible gains and sometimes hurts performance.
4. **Stick with lexical retrieval for long documents.** BM25 and other bag‑of‑words methods remain competitive — and in many cases superior — for long‑context retrieval.
5. **Needle position matters more than semantic formulation.** For best results, place critical information at the beginning or end of chunks.

### Broader Implications

The study challenges the narrative that "bigger context windows → better retrieval." The bottleneck isn't context capacity — it's the **embedding model's ability to focus**. This mirrors findings in [[concepts/context-rot|Context Rot]] for LLMs, where reasoning capacity degrades long before the technical context limit is reached.

> The jina-embeddings-v3 model was designed for 8K tokens, and its matching LoRA was trained to perfectly differentiate between short sections of text. But at >4K, it's still blind. **Architecture, not training, is the wall.**

---

## 5. Methodology Notes & Reproducibility

- 3D‑printed plastic templates ensured consistent needle placement across haystacks
- Double‑blind protocol: experimenters didn't know needle positions during analysis
- Full dataset of 3,234 haystacks publicly available for reproduction
- Code available in the [original repository](https://github.com/jina-ai/embedding-long-context-evaluation)
