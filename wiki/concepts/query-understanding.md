---
title: Query Understanding
type: concept
created: 2026-05-19
updated: 2026-05-20
tags:
  - search
  - information-retrieval
  - tokenization
  - lexical-search
  - embeddings
  - agentic-search
  - llm
sources:
  - raw/articles/2016-10-28_daniel-tunkelang_query-understanding-introduction.md
  - raw/articles/2017-02-16_daniel-tunkelang_query-rewriting-overview.md
  - raw/articles/2022-10-24_daniel-tunkelang_query-similarity.md
  - raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search.md
  - https://queryunderstanding.com/
related:
  - entities/daniel-tunkelang
  - entities/doug-turnbull
  - concepts/agentic-search
  - concepts/bm25
  - concepts/content-understanding
---

# Query Understanding

**Query Understanding** (QU) is the discipline of interpreting a searcher's query to determine their underlying intent, before any results are scored or ranked. It treats the query as a first-class object — the communication channel between the searcher and the search engine. As formalized by **Daniel Tunkelang** through his [Query Understanding](https://queryunderstanding.com/) publication (2016–2024), QU is a systematic stack of techniques that operate from the character level up through conversational interaction.

> "Query understanding is about what happens before the search engine scores and ranks results — namely, the searcher's process of expressing an intent as a query, and the search engine's process of determining that intent." — Daniel Tunkelang, *[Query Understanding: An Introduction](https://queryunderstanding.com/introduction-c98740502103)* (2016)

## Philosophy: Query Over Ranking

The defining philosophical shift of query understanding is moving the emphasis from **ranking algorithms** to **query interpretation**:

| Traditional Search | Query Understanding |
|---|---|
| Optimize scoring/ranking functions | Determine searcher's intent |
| Per-result relevance metrics | End-to-end query performance |
| Retrieval is the hard problem | Query interpretation is the hard problem |
| More ranking features → better search | Better query interpretation → better search |

> "Instead of striving to create the optimal ranking algorithm, search engine developers aspire to create the optimal query interpretation mechanism." — Tunkelang

The key metric is **query performance** — an end-to-end measure of how well the communication channel between searcher and search engine works.

## The Query Understanding Stack

Tunkelang's publication series traces a curriculum from raw input to meaning, organized as a bottom-up stack:

```
┌──────────────────────────────────────────────────────┐
│ Layer 6: NATURAL LANGUAGE — QA, voice, chatbots       │
├──────────────────────────────────────────────────────┤
│ Layer 5: RESULTS — Snippets, clustering, presentation │
├──────────────────────────────────────────────────────┤
│ Layer 4: CONVERSATION — Dialogues, faceted search     │
├──────────────────────────────────────────────────────┤
│ Layer 3: CONTEXT — Session, location, seasonality,    │
│          personalization                              │
├──────────────────────────────────────────────────────┤
│ Layer 2: QUERY REWRITING — Expansion, relaxation,     │
│          segmentation, scoping                        │
├──────────────────────────────────────────────────────┤
│ Layer 1: TOKENS — Tokenization, stemming,             │
│          lemmatization, canonicalization              │
├──────────────────────────────────────────────────────┤
│ Layer 0: CHARACTERS — Language ID, normalization,     │
│          spelling correction                          │
└──────────────────────────────────────────────────────┘
```

### Layer 0: Character-Level Operations

The foundation — processing raw text input before it becomes tokens.

| Technique | What It Does | Key Trade-off |
|---|---|---|
| **Language Identification** | Detect the query's language to apply language-specific processing | Some queries mix languages; short queries give weak signal |
| **Character Normalization** | Fold Unicode variants (é→e, ﬁ→fi), case-folding, remove diacritics | Over-normalization can lose meaning (café vs. cafe may differ in some domains) |
| **Spelling Correction** | Detect and correct misspelled queries (~10–15% of all queries) | Confident correction → auto-rewrite; uncertain → "Did you mean?" |

**Spelling Correction** — detailed in a dedicated article — uses a **noisy channel model** combining:
- **Language model** P(c): a priori probability of the candidate query (from query logs, smoothed with Good-Turing)
- **Error model** P(q|c): probability of the observed misspelling given the intended query (insertion, deletion, substitution, transposition errors)
- **Candidate generation** via n-gram substring indexing, scored with Bayes' theorem
- **Presentation logic**: auto-rewrite if confident; "Did you mean?" if uncertain; never rewrite to zero results

### Layer 1: Token-Level Operations

Breaking text into words and handling word variations.

| Technique | What It Does | Key Challenge |
|---|---|---|
| **Tokenization** | Split character sequence into tokens | Hyphens (five-year vs. California-based), apostrophes (don't, women's), compounds (German Fruchtsalat), CJK segmentation |
| **Stemming** | Strip word suffixes heuristically (Porter stemmer: "running"→"run") | Aggressive stemming can conflate unrelated words |
| **Lemmatization** | Map words to dictionary root form ("better"→"good") | Requires part-of-speech tagging; slower but more precise |
| **Canonicalization** | Dictionary-based mapping of variants to canonical forms | Builds domain-specific mappings for optimal precision/recall balance |

**Tokenization** is "deceptively subtle": splitting on whitespace is never enough. The recommended strategy is **multiple tokenization** — computing several possible tokenizations and using all of them to maximize recall while maintaining precision. This handles hyphens (five-year → both "fiveyear" and "five year"), apostrophes (women's → both "womens" and "women's"), and compounds.

**Stemming vs. Lemmatization**: Stemming (e.g., Porter stemmer) uses crude heuristic suffix-stripping — fast but can produce non-words. Lemmatization uses dictionary lookup + morphological analysis — more accurate but slower and language-dependent. The choice depends on the precision/recall needs of the application.

### Layer 2: Query Rewriting

The most powerful level: automatically transforming queries to better match the searcher's intent. Query rewriting serves two purposes:

#### Increasing Recall (finding more relevant results)

| Technique | Mechanism | Example |
|---|---|---|
| **Query Expansion** | Add synonyms, abbreviations, stems to broaden query | `vp marketing` → `(vp OR "vice president") marketing` |
| **Query Relaxation** | Remove or optionalize tokens to loosen constraints | `cute fluffy kittens` → `fluffy kittens` (drop modifier) |

**Query Expansion** adds terms from:
- **Abbreviations**: dictionary matching (unambiguous: CEO), supervised ML (context-based), pattern extraction (parenthesized: "GDP (gross domestic product)"), unsupervised word2vec
- **Synonyms**: harder — no surface similarity, same approaches as abbreviations but with higher ambiguity. Prefer more specific synonyms over general ones.

**Query Relaxation** removes tokens that aren't necessary for relevance. Critical: must not drop tokens essential to meaning (relaxing `cute fluffy kittens` to `cute fluffy` loses the core object). Sophisticated approach: parse query to identify main concept, then optionalize modifiers.

> **Best practice**: Apply expansion/relaxation when original query returns zero or few results. Be increasingly conservative as the result set grows.

#### Increasing Precision (reducing irrelevant results)

| Technique | Mechanism | Example |
|---|---|---|
| **Query Segmentation** | Group tokens into semantic units as phrases | `machine learning framework` → `"machine learning" framework` |
| **Query Scoping** | Match query parts to specific document fields by entity type | Tag `black michael kors dress` → color:black, brand:Michael Kors, category:dress |

**Query Segmentation** identifies multi-word semantic units. It can be implemented via:
- Dictionary-based approach: look up known phrases
- Supervised ML: binary classifier at the token level (continues or begins new segment)
- Coupled with query expansion for strong precision+recall

**Query Scoping** requires:
1. Query tagging (segment → attribute via CRF or NER)
2. Training data from search logs (clicks on results reveal which query segments match which document attributes)
3. Rewriting to restrict matches to the appropriate document fields

> "If you can only invest in two areas of query understanding, prioritize spelling correction and query segmentation." — Tunkelang

### Layer 3: Query-Level Analysis

Techniques that operate on the query as a whole rather than its components.

| Technique | What It Measures | Source Article |
|---|---|---|
| **Query Similarity** | How close two queries are in intent space | Query Similarity (2022) |
| **Query Specificity** | How broad or narrow a query's intent is | Query Specificity (2024) |

**Query Similarity** distinguishes two types of variation:
- **Superficial**: stemming, word order, stop words, tokenization, spelling — handled by Layer 0–1 techniques
- **Semantic**: synonyms, redundancy, paraphrasing — requires learned representations

Measurement approaches:
1. **Direct embedding**: Map queries to vectors via sentence transformers, compute cosine similarity. Challenges: pre-trained models may not match the search domain.
2. **Bag of Documents** (post-search behavior): Aggregate document vectors from documents users engaged with for each query. Works for head/torso queries; provides labeled training data for fine-tuning tail query models.

**Query Specificity** measures how broad or narrow a query's intent is:
- Quantified via variance of result vectors in a bag-of-documents model (high variance = broad query)
- More principled than heuristics like result count or taxonomy depth
- Applications: guide searchers to higher-specificity queries (better signal for the engine), manage precision-recall tradeoffs, analyze search behavior

### Layer 3.5: Cross-Cutting — Autocomplete

**Autocomplete** bridges multiple layers of the stack. It's the primary surface for modern search experience:

- **Query probability** P(query|prefix) computed from historical query logs (Layer 0–1 integration)
- **Query performance** factored in: P(click|prefix) rather than raw P(query|prefix)
- **Trade-off**: Popular queries with low CTR vs. niche queries with high CTR — need a minimum performance threshold
- Structured suggestions, prefix indexing, and n-gram language models for multi-token completions

> "For a large fraction of your searchers, autocomplete is the entire search experience. Invest accordingly." — Tunkelang

### Layer 4: Context & Personalization

Going beyond the query text to incorporate external signals about the searcher's situation.

| Context Type | What It Adds | Key Technique |
|---|---|---|
| **Session Context** | Previous queries in the same session inform current intent | Query reformulation patterns, session-based query probabilities |
| **Location** | Geographic position as implicit query component or intent signal | IP geolocation → document-location association via engagement clustering |
| **Seasonality** | Time-of-year / time-of-day patterns in query probability | Variance-based seasonality detection (comparing query occurrence distribution to uniform) |
| **Personalization** | Searcher-specific history, preferences, and demographic signals | Personalized query probabilities + personalization as intent signal |

**Location as Context** operates in two modes:
- **Implicit query component**: `restaurants` → find near the searcher (local intent classification problem)
- **Intent signal**: `football` means different things in US vs. UK; `jackets` preferences vary by climate

Documents are associated with locations via the locations of searchers who engage with them.

**Seasonality** is primarily valuable for autocomplete: `c` in late October → `costume`, in mid-December → `christmas`. Variance of query occurrence over time correlates negatively with seasonality. Only works for frequent queries; tail queries require ML approaches.

**Personalization** operates on two fronts:
- **Personalized query probabilities**: Searcher history and interests predict what they'll search for
- **Personalization as intent signal**: Knowledge about the searcher clarifies/refines query interpretation

> "The query is necessary but not always sufficient to determine the searcher's intent. Personalization can help, but it's always a secondary signal — context should never overcome the query itself."

### Layer 5: Conversational Search

Modeling search as a dialogue rather than a one-shot query-response exchange.

| Pattern | Purpose | Mechanism |
|---|---|---|
| **Search as Conversation** | Recognize that searchers learn and refine intent through interaction | Transparency (explain interpretation) + Control (let searcher override) + Guidance (suggest better queries) |
| **Clarification Dialogues** | Hedge when the engine is uncertain about query interpretation | "Did you mean?" vs. auto-rewrite with opt-out; confidence-threshold based |
| **Faceted Search** | Let users iteratively filter by structured dimensions | Tunkelang's foundational contribution; standard in all modern e-commerce search |

**Conversational Search** recognizes that:
- Query understanding is never perfect
- Searchers evolve their intent based on results they see
- The engine must provide **transparency** (how it understood the query), **control** (ways to override), and **guidance** (suggestions for better queries)

**Clarification Dialogues** are modeled as an optimization problem: maximize expected utility for the searcher by weighing:
1. Confidence in primary interpretation
2. Confidence in alternative interpretation
3. Expected harm from displacing relevant results with the dialogue

### Layer 6: Results & Natural Language

The interface between the engine's understanding and the searcher's experience.

| Technique | Purpose | Key Insight |
|---|---|---|
| **Search Results Presentation** | Match presentation style to query type and intent | Navigational vs. exploratory queries need different presentations |
| **Search Result Snippets** | Signal per-result relevance without requiring clicks | Good snippets reduce click-through to determine relevance |
| **Results Clustering** | Group results for broad-intent queries | Scatter/Gather (1990s); challenging in practice due to similarity function tuning |
| **Question Answering** | Return direct answers instead of result lists | Breadth vs. depth trade-off in knowledge bases; hybrid QA+search approach works best |

**Question Answering** represents the logical evolution of search engines. Key challenges:
- **Knowledge base breadth vs. depth**: Google's Knowledge Graph optimizes for breadth; domain-specific KBs like Twiggle's product ontology optimize for depth
- **Interface constraints**: Returning a single answer is unforgiving — leaves almost no room for error. Wrong answers erode trust faster than "I don't know."
- **Hybrid approach** (preferred when there's a display): QA with high confidence → direct answer; otherwise → traditional ranked results

## The Full Article Series

Tunkelang's Query Understanding publication comprises ~20 articles published between 2016–2024 on Medium:

| # | Article | Date | Layer |
|---|---|---|---|
| 1 | [A Manifesto](https://queryunderstanding.com/query-understanding-a-manifesto-367dc0be6745) | Jun 2016 | Philosophy |
| 2 | [An Introduction](https://queryunderstanding.com/introduction-c98740502103) | Oct 2016 | Overview |
| 3 | Language Identification | 2016 | Layer 0 |
| 4 | Character Normalization | 2016 | Layer 0 |
| 5 | [Spelling Correction](https://queryunderstanding.com/spelling-correction-471f71b19880) | Jan 2017 | Layer 0 |
| 6 | [Tokenization](https://queryunderstanding.com/tokenization-c8cdd6aef7ff) | Dec 2016 | Layer 1 |
| 7 | [Stemming and Lemmatization](https://queryunderstanding.com/stemming-and-lemmatization-6c086742fe45) | Feb 2017 | Layer 1 |
| 8 | [Query Rewriting: An Overview](https://queryunderstanding.com/query-rewriting-an-overview-d7916eb94b83) | Feb 2017 | Layer 2 |
| 9 | [Query Expansion](https://queryunderstanding.com/query-expansion-2d68d47cf9c8) | Mar 2017 | Layer 2 |
| 10 | [Query Relaxation](https://queryunderstanding.com/query-relaxation-342bc37ad425) | Mar 2017 | Layer 2 |
| 11 | [Query Segmentation](https://queryunderstanding.com/query-segmentation-2cf860ade503) | Apr 2017 | Layer 2 |
| 12 | [Query Scoping](https://queryunderstanding.com/query-scoping-ed61b5ec8753) | May 2017 | Layer 2 |
| 13 | [Autocomplete](https://queryunderstanding.com/autocomplete-69ed81bba245) | 2017 | Cross-cutting |
| 14 | [Location as Context](https://queryunderstanding.com/geographical-context-77ce4c773dc7) | Oct 2017 | Layer 4 |
| 15 | [Seasonality](https://queryunderstanding.com/seasonality-5eef79d8bf1c) | 2017 | Layer 4 |
| 16 | [Personalization](https://queryunderstanding.com/personalization-3ed715e05ef) | Nov 2017 | Layer 4 |
| 17 | [Search as a Conversation](https://queryunderstanding.com/search-as-a-conversation-bafa7cd0c9a5) | Nov 2017 | Layer 5 |
| 18 | [Clarification Dialogues](https://queryunderstanding.com/clarification-dialogues-69420432f451) | Dec 2017 | Layer 5 |
| 19 | [Faceted Search](https://queryunderstanding.com/faceted-search-7d053cc4fada) | Jan 2018 | Layer 5 |
| 20 | [Search Results Presentation](https://queryunderstanding.com/search-results-presentation-7d6c6c384ec1) | Feb 2018 | Layer 6 |
| 21 | [Question Answering](https://queryunderstanding.com/question-answering-94984185c203) | May 2018 | Layer 6 |
| 22 | [Search Results Clustering](https://queryunderstanding.com/search-results-clustering-b2fa64c6c809) | 2018 | Layer 6 |
| 23 | [Query Similarity](https://queryunderstanding.com/query-similarity-49dde9f78043) | Oct 2022 | Layer 3 |
| 24 | [Query Specificity](https://queryunderstanding.com/query-specificity-a6156f4043eb) | Jan 2024 | Layer 3 |

## Query Understanding in the LLM Era

The foundational principles of query understanding are directly relevant to modern LLM-powered and agentic search ([[concepts/agentic-search]]):

### Classical QU → LLM-Powered QU

| Classical Approach | LLM-Powered Equivalent |
|---|---|
| CRF-based query tagging for scoping | LLM performs entity extraction + structured output via schema |
| Dictionary-based synonym expansion | LLM generates semantically equivalent query variations |
| Session-based context modeling | LLM maintains conversational context across turns |
| Spelling correction via noisy channel model | LLM corrects via language understanding (no explicit error model needed) |
| Clarification dialogues via confidence thresholds | LLM naturally asks clarifying questions when uncertain |

### Key Insight from Doug Turnbull

> "LLMs can speak in schema" — Turnbull observes that LLMs perform query understanding reliably when given structured attribute schemas, matching Tunkelang's original vision of query scoping but with dramatically simpler implementation. The complexity shifts from the search stack itself to the agent harness and feedback loops that guide agent behavior.

### Tunkelang's Caveat on LLM Over-Personalization

Tunkelang has observed that LLM-based systems can over-personalize, sharing an experience where ChatGPT assumed his restaurant queries were for client entertainment rather than personal interest. This echoes his principle that **personalization should be a secondary signal that supplements, not overrides, the query**.

## LLM-Powered Query Understanding in Practice (Doug Turnbull)

While Tunkelang's framework provides the theoretical foundation, **Doug Turnbull** ([Cheat at Search](https://maven.com/softwaredoug/cheatatsearch), May 2026) provides a practical, code-level implementation guide. His core insight: **simple LLMs can reliably perform classical NLP tasks for query understanding when given structured output schemas**, and structured QU solves several critical problems with pure embedding-based search.

> Source: [[raw/articles/2026-05-20_softwaredoug_llm-query-understanding-cheat-at-search.md]]

### Why Structured QU Over Pure Embeddings

#### Embedding Collapse (Hubness)

General-purpose embedding models are trained on vast, diverse data. In a **narrow domain** (e.g., a single retailer's furniture catalog), every item occupies a tiny corner of the embedding space — everything looks similarly similar:

```
similarity("blue couch", "a couch")      = 0.72
similarity("blue couch", "a blue chair") = 0.71
similarity("blue couch", "a blue couch") = 0.75
```

The difference between a correct result (0.75) and an irrelevant one (0.71) is just 0.04 — **threshold-based filtering becomes practically impossible**. This is an intrinsic property of high-dimensional embedding spaces in narrow domains, not a model quality issue.

#### The Chat Query Problem

Modern conversational interfaces produce long, verbose queries like:

> "Hi I am curious for a couch that would fit into a sunny living room. I actually want a sky blue one. Well my father in law might visit and need a place to sleep."

These generate compound queries (e.g., `"Bright, sky-blue sleeper sofa for living room"`) with **insufficient training data for reliable embedding matching**. Multi-modal embedding models struggle because each long, compound query is essentially unique.

#### Fine-Tuning Costs

Building domain-specific embedding models requires:
- Gathering domain-specific training data (e.g., furniture CLIP pairs)
- ML expertise for retraining and evaluation
- Deployment infrastructure

And even after fine-tuning, you still can't easily "cut off" irrelevant results — the threshold problem remains.

### Five Approaches to Query Understanding

Turnbull categorizes QU into five approaches, from simplest to most sophisticated:

| Approach | Mechanism | Characteristics |
|---|---|---|
| **Rules** | PM/merchandiser manually assigns attributes | Human curation; doesn't scale |
| **Historical** | Aggregate click data → most common attribute for a query | `SELECT query, COUNT(color) … GROUP BY query`; only covers head queries |
| **ML-Based** | Train classifier on historical data (features → attribute) | Requires labeled training data; traditional approach |
| **Embedding-Based** | Embed query + candidate attribute values → nearest neighbor | Query vector → compare with color/brand/category embeddings; suffers from hubness |
| **Prompt-Based** | LLM extracts values via structured output schema | **Recommended modern approach**; reliable, interpretable, cost-effective |

### LLM QU Technique 1: Synonym Extraction

The simplest entry point: use a cheap LLM to extract synonyms, then boost BM25 scores for matching documents.

**Implementation pattern** — structured outputs via Pydantic:

```python
class SynonymMapping(BaseModel):
    phrase: str = Field(description="Original phrase from query")
    synonyms: List[str] = Field(description="Synonyms for the phrase")

class QueryWithSynonyms(BaseModel):
    synonyms: List[SynonymMapping]

resp = openai.responses.parse(
    model="gpt-4.1-nano",
    input=[
        {"role": "system", "content": "You are a helpful AI assistant extracting synonyms."},
        {"role": "user", "content": f"Extract synonyms from: {query}"}
    ],
    text_output=QueryWithSynonyms
)
```

**Example output** for `"rack glass"`:
- `rack → [shelf, stand, holder]`
- `glass → [cup, cupware, drinking glass]`

**BM25 integration**: For each generated synonym phrase, tokenize it and add its BM25 score to the overall query score:

```python
for mapping in synonyms.synonyms:
    for phrase in mapping.synonyms:
        tokenized = snowball_tokenizer(phrase)
        bm25_scores += index['product_name_snowball'].array.score(tokenized)
        bm25_scores += index['product_description_snowball'].array.score(tokenized)
```

**Result**: NDCG improved from 0.541 (plain BM25) → 0.546 (synonym-boosted BM25) on Wayfair queries. A modest but measurable lift from a one-line LLM call.

### LLM QU Technique 2: Category Classification

#### Few-Label Classification

When the category set is small (~10–50 labels), a simple `Literal` type works:

```python
Category = Literal['Furniture', 'Rugs', 'Décor & Pillows', 'Outdoor', 'Lighting', …]
```

#### Deep Multi-Label Classification (10K+ Labels)

For large category taxonomies like `'Furniture / Living Room Furniture / Console Tables'`, classification becomes a **multi-label selection** problem:

```python
class QueryClassification(BaseModel):
    classification: list[FullyQualifiedClassifications] = Field(
        description="Best matching categories. Use 'No Classification Fits' if unclear."
    )
```

**Search boost**: For each returned category, tokenize and add a constant boost to documents whose category field matches:

```python
for category in classified.categories:
    tokenized_category = snowball_tokenizer(category)
    category_match = self.index['category_snowball'].array.score(tokenized_category) > 0
    bm25_scores[category_match] += self.category_boost
```

**Cost challenge**: With 10K+ labels in the prompt, initial token usage was 5,998 input tokens per query — expensive at scale.

#### Cost Optimization: Dynamic Pydantic Enums

The key insight: **use BM25 to reduce the label space before calling the LLM**:

1. Run BM25 query → get top 300 candidate results
2. Extract the 25 most frequent category hierarchies from those results
3. **Dynamically construct a Pydantic enum** from those 25 labels:

```python
def make_classifier_model(labels: list[str]) -> type[BaseModel]:
    LabelEnum = Enum('LabelEnum', {l: l for l in labels})
    Model = create_model("QueryClassification",
        __doc__="A classification of the query.",
        classification=(list[LabelEnum], Field(...)))
    return Model
```

4. Classify using cheap model (gpt-4.1-nano) with the reduced label set

**Result**: Input tokens dropped from 5,998 → **~485** — a 12x reduction. The virtuous cycle: **BM25 narrows the label space, enabling cheap LLM classification, which then boosts BM25 scores**.

### The Full QU Pipeline

```
QUERY
  ↓
CACHE LOOKUP → [hit] → CACHED ATTRIBUTES → APPLY BOOSTS → SEARCH
  ↓ [miss]
BM25 → TOP 300 → EXTRACT TOP CATEGORIES → DYNAMIC ENUM → LLM CLASSIFY
  ↓                                                    ↓
CACHE RESULT ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ←
```

### Caching Strategy

- **Static tier**: Frequently seen queries cached with pre-computed attributes (head queries)
- **Dynamic tier**: Unseen (tail) queries → LLM classification → cached for future hits
- **Economics**: gpt-4.1-nano is cheap enough for 100K+ queries; caching makes it viable for production

### Empirical Results

| Approach | NDCG | Delta |
|---|---|---|
| Plain BM25 (baseline) | 0.541 | — |
| BM25 + LLM Synonym Extraction | 0.546 | +0.005 |
| BM25 + LLM Category Classification | ~0.608 | +0.067 |

The category classification lift is substantial — **a 12% relative improvement** over plain BM25. This demonstrates that structured LLM-powered QU is not just theoretically elegant but delivers measurable retrieval quality gains at production scale.

### Key Takeaways

1. **Embedding collapse is real** — in narrow domains, pure embedding search struggles to distinguish relevant from irrelevant results
2. **Structured QU is a practical fix** — extracting structured attributes via LLM gives interpretable, controllable ranking signals
3. **Cheap LLMs are sufficient** — gpt-4.1-nano handles synonym extraction, category classification, and attribute extraction reliably
4. **BM25 + LLM QU form a virtuous cycle** — BM25 narrows the label space for LLMs; LLMs improve BM25's ranking quality
5. **Caching makes it production-viable** — cache frequent queries; LLM only for the long tail
6. **Agent-native design**: structured QU outputs are tool-usable — agents can reason about extracted attributes, making QU a first-class component of [[concepts/agentic-search]]

## Distinction from Related Concepts

- **[[concepts/content-understanding]]**: CU is the document/index-side counterpart to query understanding. While QU interprets the searcher's intent from the query, CU enriches content in the index to make it findable. The two form a virtuous cycle: engagement data maps queries to content, enabling mutual inference. CU handles varied formats (long-form, images); QU handles short text.
- **[[concepts/agentic-search]]**: Agentic search is about *how* search is executed (agent-driven loops). Query understanding is about *interpreting what the searcher wants*. QU is an input into agentic search — the agent uses QU to understand the task before deciding how to fulfill it.
- **[[concepts/bm25]]**: BM25 is a specific ranking function for lexical retrieval. Query understanding operates before ranking — it rewrites the query so that BM25 (or any ranker) has a better input.
- **Information Retrieval (IR)**: IR is the broader field encompassing retrieval, ranking, and evaluation. Query understanding is the front-end discipline within IR focused specifically on query interpretation.
- **NLP/ NLU**: NLP techniques (NER, parsing, embeddings) are *tools used by* query understanding, but QU applies them specifically to the search context with a focus on end-to-end query performance.
