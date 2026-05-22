---
title: "ColBERT and Late Interaction Retrieval: Why, How, and What Next?"
source_url: https://docs.google.com/presentation/d/1GmvpRgre2zamJ5zKxxhtj-eKL4j6VqfP3wO2_o210Z0/
author: Benjamin Clavié
date: 2026-05-20
venue: Tsukuba IR Talk
organization: Mixedbread / NII
tags: [colbert, late-interaction, information-retrieval, embeddings, multi-vector]
extraction_method: htmlpresent + browser_console chunks
---

# ColBERT and Late Interaction Retrieval: Why, How, and What Next?

or How I Like to Think About IR Paradigms and What They Teach Us

**Speaker:** Benjamin Clavié, 2026-05-20
**Venue:** Tsukuba IR Talk
**Affiliation:** Mixedbread / National Institute of Informatics (NII)

---

## About the Speaker

- Research at Mixedbread (industrial IR lab) and National Institute of Informatics (NII)
- Focus: mechanics of Late Interaction (ColBERT) models
- Previously: LexisNexis, Answer.AI (co-led ModernBERT)
- MSc in AI from University of Edinburgh; born near Paris, lives in Tokyo

---

## Agenda

1. A very brief, long-timeline history of retrieval
2. The emergence of neural paradigms
3. Single-Vector, Sparse, Multi-Vector, Hybrid: Families of Neural Retrievers
4. The Dark Ages: Why Single Vector Dominated, and why it has a ceiling
5. Late Interaction, ColBERT: Intuitions and limit breaking
6. Empirical Domination…
7. … But not without tradeoffs
8. Now, what next?

> This talk is not an in-depth discussion of one particular research topic, but more of an overview of why late interaction makes sense as the current leading paradigm, what research and engineers problems we have to overcome, and more importantly, some ideas about what needs to come next.

---

## I. Information Retrieval is a Tool

### First, there was Information

- Information Retrieval is a need that emerges from Information Collections
- Information collections have always existed, with volume trending up throughout history
- The need to organize and find information is a natural need that emerges from the existence of information itself
- While "Information Retrieval" as a defined term can be traced to Cranfield in the 1950s, Clavié defines it more broadly as the study of tools facilitating information access

### Then, came Retrieval

IR has taken many forms throughout the years, adapting itself to the information sources of the time:

- **180 BC**: Information was ultra-concentrated — state-of-the-art IR was the single Pinakes catalog of the Library of Alexandria
- **Printing press**: Wider distribution → golden age of librarians and ontologies (proto-Inverted List indexing)
- **Computers**: Even more distributed information → problem of scale → birth of modern IR methodologies
- **Internet**: Exponential boom — more written information created in a single year than in centuries previously

### Key References

- **Vannevar Bush, As We May Think (1945)** — "one of the most prescient essays to help you think about the era we're in"
- **Cranfield experiments (1950s)** — formalized evaluation
- **Charles and Ray Eames, A Computer Glossary (1968)**

### IR is first and foremost about tools

- Increasing volumes of information consistently create new needs, with IR research addressing these needs
- Library catalogs → Dewey Decimal Classification → modern IR with Bush/Cranfield
- Since then: information has grown exponentially → better evaluations, better models, endless new challenges

### Why Does This Matter?

- Core role of IR: accessing information in the most efficient way possible
- Warning for researchers: don't hyperfocus on the method; remember the objective
- Current neural paradigms are today's best tools for IR, but they are not IR itself nor the end goal
- **Sisyphean Task**: solving current problems unlocks tomorrow's, with no end in sight

### Why This Matters for ColBERT

- We must fully understand the capabilities of current systems to identify their shortcomings
- All current approaches have heavy tradeoffs, with no silver bullet
- Clavié's advocacy for Late Interaction models: it currently holds the best cost/benefit ratio
- To design better future retrieval systems, understand why this is the case and the underlying mechanisms

---

## II. Neural IR Paradigm(s): The Current Tools

### What is Neural IR?

- Broadly describes all retrieval methods using neural networks
- In practice, mainly refers to "first-stage" retrieval: query → candidate documents
- Most neural methods are a subfamily of Representation Learning: learn representations for documents and queries that are conducive to efficient scoring
- Learning representations is only one part — they must be efficiently scorable for large collections

### The Big Three Paradigms

1. **Dense single-vector retrieval** ("embeddings") — document represented by a single vector through pooling of individual tokens
2. **Sparse retrieval** — neural-augmented, inspired by BM25; document represented by large sparse vector with few activated features
3. **Dense multi-vector retrieval** ("ColBERT" / "Late Interaction") — document as a bag of low-dimension token-level vectors, maximizing local expressivity

### Single-Vector: Rise to Prominence

Single-vector retrieval dominated both in paper count and real-world adoption. Reasons:

- Relative ease of use when need for better retrieval grew rapidly
- Process of elimination:
  - Sparse methods: just as efficient but trickier to get good performance, non-English models rare, restrictive licensing
  - ColBERT-like methods: powerful but considerably more complex until ~2023

### Single-Vector: The Pros

- Performance often strong, particularly on popular benchmarks
- **Low barrier to entry**: generating and using representations requires little custom code
  - Double advantage: low adoption friction → more time for research → more high-quality research
- Indexing is simple, compatible with any system implementing dot product
- **Storage is minimal**: single vector takes very little space — billions of documents on cheap hard drives
- **Virtuous cycle**: everyone uses it → accessible documentation → more people use it

### Single-Vector: The Limitation of Dilution

- Single-vector models function by **averaging representations**: one vector represents the full document
- Vectors typically 768–4096 dimensions, but individual information gets diluted
- **Regression to the mean**: highly discriminative semantic units get smoothened out, losing their strong relevance/irrelevance signal
- Out-of-domain degradation is frequent

### Single-Vector: Standardized Benchmarking is Not the Full Picture

- Single-vector models look extremely strong on known benchmarks but struggle with OOD generalization
- For years, benchmarks consolidated around BEIR and TREC; training adapted unconsciously to these
- Novel uses expose weaknesses:
  - **BrowseComp-Plus Agentic Search**: state-of-the-art 8B single-vector models outperformed by 130M (0.13B) ColBERT models
  - **LIMIT stress-test**: where lexical information is key, single-vector representations completely collapse — trivial for other families

### Single-Vector: Multi-Modal Information (ViDoRe Effect)

- Neural IR moving towards more modalities: text, messy PDF scans, images
- Visual information makes dilution an even bigger problem — hard to compress an entire page with figures without losing fine-grained details
- **ViDoRe effect**: single-vector retrievers perform well on existing benchmarks, but when a new version releases (ViDoReV3), they regress to performance of models years older — a form of generalization collapse
- Visual metaphor: Hieronymus Bosch's "The Garden of Earthly Delights" — very hard to capture with a single representation

---

## III. Late Interaction: The Most Powerful Current Paradigm (but at what cost?)

### Multi-Vector Retrieval: The Basics

- **Opposite stance to single-vector**: preserves individual "semantic units" — all pieces of information are preserved as-is
- Low-dimension representations preserving individual token info are stronger than higher-dimension ones capturing document-level info
- Instead of pooling individual representations, project them to smaller dimensions → document as "bag-of-semantic-words"
- Avoids forcing the model to over-represent potentially useful info in a single vector

### A Caveat: The Power is in Scoring Expressiveness

- Traditionally, retriever and scoring method are conflated ("single-vector retrievers", "ColBERT models")
- **Key insight**: limitations of single-vector are not inherent to the model, but to the scoring mechanism (cosine similarity)
- Clavié teases: "We have a paper out next week showing it is possible to extract retrieval knowledge from single-vector models that do not suffer from single vector's limitations"
- The bottleneck is scoring expressiveness — this intuition led to ColBERT 5 years ago

### The True Magic: MaxSim

- Single-vector: single relevance calculation — similarity between query vector and document vector = final score
- **MaxSim**: compares each query token to every document token, keeps only the highest score per query token, then sums them
- `S(q,d) = Σ max(Eq_i · Ed_j^T)`

**The Max component is key:**
- SumSim (sum per-token relevance for each token): performance collapse
- AvgSim (average token-level similarities before summing): performance collapse
- MaxSim lets minor query nuances and small nuggets of document info strongly impact scoring — no dilution

### The Difference in Practice: Out-of-Domain Generalization

- **ViDoRe**: single-vector models always playing catch-up (strong on existing, weak on next benchmark). Late interaction models strong on ViDoRe-v2 are universally strong on ViDoRe-v3 — generalization compresses less
- **Agentic search**: ColBERTs originally designed for BEIR-like tasks are some of the strongest out-of-the-box retrievers, despite very different query settings that harm single-vector models

### Greater Generalization: Multi-Vector Models are Surprisingly Data Efficient

- Current late interaction models often trained on an order-of-magnitude less data than competitive single-vector retrievers
- Text: ColBERTv2 (trained on MS Marco) comparable to GTE-Base (trained on 100M+ text pairs)
- Multi-modal: Qwen3-VL embeddings require 340M+ examples; competitive multi-vector Qwen3-based models reach similar performance with ~1M

---

## IV. The Flipside of Multi-Vector Retrieval

### Headline Numbers

- **Storage**: Instead of one 2048-dim vector for a 512-token doc, need 512 × 128-dim vectors = 65,536 dimensions → 32x storage increase
- **Scoring**: MaxSim requires comparing every query token with every document token (e.g., 16,384 similarity computations per doc) instead of one

### Engineering Woes

- ColBERT requires a **two-step pipeline**: first stage surfaces manageable candidates (low thousands), then MaxSim scores them
- Deployment of single-vector methods is trivial; multi-vector integration comes with real engineering concerns, especially at scale
- For a long time, efficiency concerns compounded by implementation difficulties — original ColBERT codebase required significant effort to understand
- **Vicious cycle**: pros were well known among select researchers/companies, but broad adoption was lacking → fewer resources for breakthroughs

---

## V. All Limitations Are Research Problems Waiting to be Solved

### Two-Step Retrieval

The greatest bottleneck. Solutions being explored:
- **PLAID**: approximate search for candidate generation
- **XTR**: minimizes the surface problem by targeting only few tokens
- **MUVERA**: sparsifying representations or turning them into a single large vector

### Scoring Efficiency

Headline numbers look scary, but modern hardware is powerful and underutilized:
- **maxsim-cpu, FlashMaxSim**: borrowing from other fields for hardware optimization
- **PyLate**: ecosystem has greatly improved
- **PLAID indexing**: 1-bit quantization brings storage to same order of magnitude as single-vector models
  - Tradeoff: indexes become difficult to update

### Neural Retrieval is NOT Solved

- Clavié's team measured the **oracle gap**: difference in LLM performance between artificially perfect retrieval and best available real method
- Results highlight retrieval is far from solved: "Would you think an employee who gets 12% of its tasks wrong is performing at its best?"

### We Still Have Much to Understand

- Training mechanics and gradient flows of ColBERT models are relatively understudied
- First ColBERT employing large-scale contrastive pretraining came out just last month — **5+ years after it became commonplace in single-vector retrieval**
- MaxSim is 6 years old and increasingly unsuited to certain tasks — collapses in instruction-following situations due to its naive approach
- Understanding and improving these dynamics is likely core to developing the models of the future

---

## VI. So What Do We Do Next?

Three pressing matters:

1. **Agents are redefining the problem surface**: nDCG@10 matters less, but surfacing the right evidence in a timely manner matters more → doesn't kill retrieval, but means we need to rethink how we develop tools
2. **MaxSim cannot deal with instructions** and novel query phrasing → how do we fix that? New scoring operator, or simply smarter weighting and representations?
3. **Late Interaction scaling is still difficult** and first-stage is not solved → current literature has opened dozens of avenues; we are likely nearing a breakthrough

> "These are all problems that will be core to the future landscape, and which you could be the one to solve!"

---

## Contact

- ben@mixedbread.com
- bc@nii.ac.jp
