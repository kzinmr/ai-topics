---
title: Query Understanding
type: concept
created: 2026-05-19
updated: 2026-05-19
tags:
  - search
  - information-retrieval
  - tokenization
  - lexical-search
  - embeddings
  - agentic-search
sources:
  - raw/articles/2016-10-28_daniel-tunkelang_query-understanding-introduction.md
  - raw/articles/2017-02-16_daniel-tunkelang_query-rewriting-overview.md
  - raw/articles/2022-10-24_daniel-tunkelang_query-similarity.md
  - https://queryunderstanding.com/
related:
  - entities/daniel-tunkelang
  - concepts/agentic-search
  - concepts/bm25
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

## Distinction from Related Concepts

- **[[concepts/agentic-search]]**: Agentic search is about *how* search is executed (agent-driven loops). Query understanding is about *interpreting what the searcher wants*. QU is an input into agentic search — the agent uses QU to understand the task before deciding how to fulfill it.
- **[[concepts/bm25]]**: BM25 is a specific ranking function for lexical retrieval. Query understanding operates before ranking — it rewrites the query so that BM25 (or any ranker) has a better input.
- **Information Retrieval (IR)**: IR is the broader field encompassing retrieval, ranking, and evaluation. Query understanding is the front-end discipline within IR focused specifically on query interpretation.
- **NLP/ NLU**: NLP techniques (NER, parsing, embeddings) are *tools used by* query understanding, but QU applies them specifically to the search context with a focus on end-to-end query performance.
