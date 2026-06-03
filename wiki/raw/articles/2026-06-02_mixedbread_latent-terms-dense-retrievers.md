---
type: article
source_url: https://www.mixedbread.com/blog/latent-terms
title: "Dense Retrievers Know More Than They Can Express"
authors: Benjamin Clavié, Sean Lee, Aamir Shakir, Makoto P. Kato
date: 2026-06-02
arxiv: "2605.29384"
citation_title: "Latent Terms: Dense Retrievers Contain Trivially Extractable BM25-ready Zipfian Vocabularies"
tags: [dense-retrieval, sparse-retrieval, sae, interpretability, information-retrieval, bm25, latent-terms]
---

# Dense Retrievers Know More Than They Can Express

> **TL;DR**: We show that dense retrievers implicitly build term-level representations that can be trivially mapped back to BM25-compatible sparse vocabularies. By applying sparse autoencoders (SAEs) to the residual stream of a trained retriever (Qwen3-0.6B), we extract *Latent Terms* — interpretable feature directions that correspond to lexical items with Zipfian frequency distributions. These features partition cleanly into three families: **Lexical** (~33%), **Narrow Semantic** (~10%), and **Broad Topical** (~57%). When used as a sparse retrieval mechanism (akin to BM25), Latent Terms recover **99.5% of BM25's effectiveness** on BEIR with a single linear projection — no decoder, no generation, no term-matching required. On the LIMIT benchmark, Latent Terms even outperform the strong BM25 baseline, demonstrating genuine semantic understanding beyond surface lexical matching.

**Authors**: Benjamin Clavié, Sean Lee, Aamir Shakir, Makoto P. Kato
**Paper**: [arXiv:2605.29384](https://arxiv.org/abs/2605.29384) (submitted 2026-05-28)
**Affiliation**: Mixedbread

---

## 1. Introduction: The Latent Vocabulary Hypothesis

Dense retrievers encode queries and documents into continuous vector spaces and retrieve by cosine similarity. They are known to outperform lexical methods like BM25 on semantic matching tasks, yet they struggle with exact term matching. BM25, conversely, excels at lexical overlap but lacks semantic understanding.

The standard narrative positions these as complementary — hence hybrid retrieval. But what if dense models have already learned lexical representations internally, just without a mechanism to expose them?

This paper demonstrates that **dense retrievers contain latent vocabularies** that are trivially extractable. Using sparse autoencoders (SAEs) trained on the residual stream of a fine-tuned Qwen3-0.6B retriever, the authors extract features they call **Latent Terms** — interpretable directions in activation space that correspond to specific lexical items.

## 2. Method: Extracting Latent Terms via SAEs

### 2.1 Setup

- **Base model**: Qwen3-0.6B fine-tuned as a dense retriever
- **SAE training**: Sparse autoencoders trained on the residual stream activations
- **Extraction**: For each SAE feature, the authors identify which vocabulary tokens activate it most strongly

### 2.2 The Latent Term Discovery

The key finding is striking: SAE features, when decoded, correspond directly to vocabulary items. Each feature can be mapped to a specific term (or small set of related terms) with high precision.

These are not random directions — they form a structured, interpretable vocabulary within the model's internal representation.

### 2.3 Zipfian Distribution

The frequency distribution of Latent Terms follows **Zipf's law** — the same power-law distribution observed in natural language corpora. This means:

- A small number of features correspond to very common terms (high activation frequency)
- A long tail of features correspond to rare, specific terms
- The distribution is statistically indistinguishable from the Zipfian distribution of natural language vocabulary

This is strong evidence that the model has learned a genuine lexical representation, not merely surface-level statistical patterns.

## 3. Taxonomy of Latent Terms

The authors categorize SAE features into three distinct families:

### 3.1 Lexical Features (~33%)

These correspond directly to specific vocabulary items — individual words or tokens. They function as direct term detectors, activating when the input contains (or semantically relates to) a particular word.

**Example**: A feature that activates strongly on the word "photosynthesis" or closely related morphological variants.

### 3.2 Narrow Semantic Features (~10%)

These capture **specific semantic relationships** — not individual words, but precise conceptual connections. They might activate on:
- Synonyms or paraphrases
- Specific factual associations (e.g., "capital of France" → "Paris")
- Domain-specific jargon clusters

These features go beyond surface lexical matching but remain narrowly scoped.

### 3.3 Broad Topical Features (~57%)

The majority of features capture **broad topical or thematic signals**. They activate for:
- General subject areas (e.g., "machine learning", "medical", "legal")
- Abstract categories
- Domain-level semantics

These are the features most responsible for dense retrieval's advantage over BM25 on semantic matching tasks.

### Feature Family Distribution

| Feature Family | Percentage | Character |
|---|---|---|
| Lexical | ~33% | Direct term-level matching |
| Narrow Semantic | ~10% | Specific semantic relationships |
| Broad Topical | ~57% | Thematic/domain-level signals |

## 4. Latent Terms as a Sparse Retrieval Mechanism

### 4.1 The BM25-equivalent Experiment

The critical experiment: can Latent Terms serve as a drop-in replacement for BM25?

**Method**:
1. Extract SAE feature activations for queries and documents
2. Use feature activations as sparse term weights (analogous to BM25 term frequencies)
3. Score documents by sparse dot product (BM25-style retrieval)
4. **No decoder, no generation, no explicit term matching**

**Result**: Latent Terms recover **99.5% of BM25's effectiveness** on BEIR with a single linear projection.

This is remarkable — it means the dense model has already internalized BM25-like retrieval as a subset of its capabilities.

### 4.2 Why This Matters

- Dense retrievers are not "opaque" black boxes for lexical matching — they explicitly represent terms
- The gap between dense and sparse retrieval is smaller than assumed at the representation level
- The perceived superiority of dense models comes from their *additional* semantic features, not from replacing lexical ones

## 5. Benchmark Results

### 5.1 BEIR Results

BEIR is the standard heterogeneous retrieval benchmark. Results show Latent Terms matching BM25 performance:

| Method | nDCG@10 (avg) | Notes |
|---|---|---|
| BM25 | baseline | Traditional lexical retrieval |
| Dense (Qwen3-0.6B) | higher | Full dense retrieval |
| **Latent Terms (SAE)** | **99.5% of BM25** | Sparse features only, no decoder |

The Latent Terms approach achieves near-parity with BM25 across the full BEIR suite, using only the sparse SAE features extracted from the dense model.

### 5.2 LIMIT Results

The LIMIT benchmark is designed to test **lexical and semantic understanding simultaneously**. Here, Latent Terms **outperform BM25**:

| Method | Performance | Notes |
|---|---|---|
| BM25 | baseline | Struggles with semantic variation |
| Latent Terms (SAE) | **above BM25** | Benefits from semantic feature families |

This result is particularly significant because it demonstrates that Latent Terms capture genuine semantic understanding — the Narrow Semantic and Broad Topical features contribute meaningfully beyond what BM25's purely lexical approach can achieve.

### 5.3 BERT vs Contriever Comparison

The authors also compare feature distributions between:
- **BERT-base**: A general-purpose encoder not specifically trained for retrieval
- **Contriever**: A contrastively-trained retriever

Key findings:
- Contriever shows more structured Latent Term distributions than BERT
- Retrieval-focused training produces cleaner, more interpretable lexical features
- The three-feature-family taxonomy holds across both models, but with different proportions
- Contriever's Lexical features are more precisely aligned with vocabulary items

## 6. Key Findings and Implications

### 6.1 Core Contributions

1. **Dense retrievers contain extractable lexical vocabularies**: SAEs trivially reveal BM25-compatible term representations
2. **Latent Terms follow Zipf's law**: The extracted vocabulary has the same statistical properties as natural language
3. **Three feature families emerge**: Lexical (33%), Narrow Semantic (10%), Broad Topical (57%)
4. **99.5% BM25 recovery**: A single linear projection from SAE features recovers nearly all BM25 effectiveness
5. **Semantic bonus on LIMIT**: Latent Terms exceed BM25 on benchmarks requiring semantic understanding

### 6.2 Implications for Retrieval

- **Hybrid retrieval is a crutch for incomplete extraction**: Dense models already encode sparse retrieval; we just need the right probe
- **Interpretability is achievable**: Dense retrieval is not a black box — term-level semantics are explicitly represented
- **Efficiency potential**: Latent Terms could enable efficient sparse retrieval from dense models without separate BM25 pipelines
- **SAEs as universal probes**: Sparse autoencoders provide a general method for extracting interpretable features from retrieval models

### 6.3 Implications for Model Understanding

- Dense retrievers do not "replace" lexical matching with semantics — they **subsume** it
- The semantic advantage of dense models comes from additional feature families (Narrow Semantic, Broad Topical), not from abandoning lexical representations
- BM25 and dense retrieval are not orthogonal approaches but **nested**: dense contains sparse as a subset

## 7. Related Work

This work builds on several research threads:

- **Sparse Autoencoders for LLM interpretability** (Bricken et al., 2023; Templeton et al., 2024; Rajamanoharan et al., 2024; Gao et al., 2025)
- **Neural term weighting** (Zheng et al., 2024; Cacheda et al., 2024)
- **Dense-sparse hybrid retrieval** (Ma et al., 2025; Zhang et al., 2024)
- **SAE applications in NLP** (Li et al., 2025)

The novelty of this work is applying SAE interpretability specifically to the retrieval setting and demonstrating the BM25-equivalence result.

## 8. Conclusion

Dense retrievers know more than they can express — but only because we weren't looking in the right place. By applying sparse autoencoders to the residual stream, we extract Latent Terms that form a complete, Zipfian-distributed vocabulary capable of near-perfect BM25 emulation. The dense model's advantage comes not from abandoning lexical understanding but from augmenting it with semantic features.

This reframes the relationship between dense and sparse retrieval: they are not competing paradigms but **nested representations**, with dense models subsuming sparse capabilities and adding semantic richness on top.

---

## References

- Clavié, B., Lee, S., Shakir, A., & Kato, M. P. (2026). *Latent Terms: Dense Retrievers Contain Trivially Extractable BM25-ready Zipfian Vocabularies*. arXiv:2605.29384. https://arxiv.org/abs/2605.29384
- Mixedbread Blog. https://www.mixedbread.com/blog/latent-terms

---

## Community Reactions: Ben Clavié on X (2026-06-03)

Ben Clavié (first author) posted a reflective thread on X after publication, emphasizing the broader research-culture implications:

**Main tweet** ([source](https://x.com/bclavie/status/2062151045346984032), 70 likes, 28 bookmarks, 7.3K impressions):

> "I have a deeper note to make about this: we need to rethink how we approach retrieval research if we want to have an LLM moment.
>
> I think a problem we have as a sub-field is a lack of openness to early research that might be paving the way to what comes next, even if it's not all [there yet]."

**Earlier framing tweet** ([source](https://x.com/bclavie/status/2061964415524901019)):

> "my main takeaway from this isn't 'oh, this is cool! BM25 works on hidden activations!' but 'we understand so little about retrieval that models have an entire sparse indexable world we knew almost nothing about'. future's bright, tons of work to do."

**Follow-up on research incentives** ([source](https://x.com/bclavie/status/2062160512704815374)):

> "I really don't think the availability of infra should have any bearing whatsoever on whether an idea makes it into the world. We need to encourage papers whose infra is in the future."

**Antoine Chaffin** (retweeted by Clavié) echoed the sentiment ([source](https://x.com/antoine_chaffin/status/2062081232842682448)):

> "Despite being insanely cool results by itself, I think this study highlights something much more important for the future direction of IR. The goal has never been to create representations that contains all the information about the original input."

Clavié credited Chaffin for inspiring the thread ([source](https://x.com/bclavie/status/2062151650354331819)).

### Meta-commentary

Clavié's thread frames the Latent Terms work not as a retrieval benchmark result but as evidence that the IR sub-field has a **research culture problem**: excessive gatekeeping around "production-ready" infrastructure discourages exploration of foundational ideas. He draws a parallel to the LLM field's trajectory — where early, impractical research (GPT-1/2 era) laid the groundwork for transformative breakthroughs — and argues retrieval needs the same tolerance for early-stage, infrastructure-incomplete work.
