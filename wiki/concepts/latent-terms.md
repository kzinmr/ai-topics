---
title: Latent Terms
created: 2026-06-02
updated: 2026-06-02
type: concept
tags: [information-retrieval, embeddings, bm25, interpretability, mechanistic-interpretability, latent-space, retrieval, colbert]
sources:
  - https://www.mixedbread.com/blog/latent-terms
  - https://arxiv.org/abs/2605.29384
related:
  - entities/benjamin-clavie
  - concepts/colbert
  - concepts/late-interaction
  - concepts/sparse-autoencoders
---

# Latent Terms

Latent Terms are features extracted by applying **Sparse Autoencoders (SAEs)** to the internal activations of dense retrieval models. These features form a sparse, interpretable vocabulary that can be indexed and queried using traditional [[concepts/bm25|BM25]] — effectively bridging the gap between dense and sparse retrieval.

## Definition

When a dense retriever like Contriever or Nomic embeds a document into a single vector, much of the model's internal knowledge is compressed and lost. SAEs trained on the intermediate activations of these models decompose the dense representation into a set of sparse, monosemantic features. Each feature, or "latent term," can be interpreted as a concept that fires on specific inputs. The collection of active latent terms for a document acts like a bag-of-words representation — but drawn from the model's learned semantic space rather than surface-level tokens.

This allows documents to be indexed using standard inverted index structures and retrieved via BM25 scoring, combining the interpretability and efficiency of lexical retrieval with the semantic depth of dense models.

## Key Insight

Dense retrievers contain **far more information in their internal representations** than their single-vector cosine-similarity scoring can express. The bottleneck is not the model's knowledge but its output interface. SAEs provide a trivial extraction method that unlocks this latent knowledge, producing a Zipfian-distributed vocabulary of semantic features that behaves remarkably like natural language.

## Three Feature Families

Analysis of SAE features reveals three distinct families:

### Lexical Features (~33%)
Fire on a single surface form — essentially capturing token-level identity. Examples: features that activate for the word "bridge" or "normal." These overlap with traditional lexical retrieval but are extracted from the model's internal space rather than raw text.

### Narrow Semantic Features (~10%)
Fire on a cluster of synonyms or closely related terms for a single concept. For example, a feature might activate for various soccer player roles (striker, midfielder, goalkeeper) or for different expressions of the same idea.

### Broad Topical Features (~57%)
Fire on lexically unrelated but topically related words. These capture higher-level thematic connections — for example, a single feature that activates for words related to ancient history and archaeology, or for terms associated with software development workflows. This is the largest family and represents genuinely novel semantic groupings not captured by surface-level matching.

## Zipfian Distribution

SAE features follow **Zipf's law** with an exponent of approximately 1.02, mirroring the frequency distribution of natural language vocabulary. A small number of features fire very frequently, while the majority fire rarely. This is in contrast to [[concepts/colbert|SPLADE]]-style learned sparse representations, which deviate from the Zipfian distribution. The natural emergence of this power law suggests the SAE is discovering genuine structure in the model's representations rather than imposing arbitrary decompositions.

## Performance

Latent Terms + BM25 achieves competitive retrieval results despite requiring no retrieval-specific training or distillation:

- **Outperforms single-vector backbones**: Contriever and Nomic embeddings scored via cosine similarity are surpassed by their own Latent Terms indexed with BM25.
- **Competitive with SPLADE-v3**: Despite SPLADE-v3 being trained with retrieval-specific distillation on MS MARCO, Latent Terms achieve comparable benchmark performance through a purely post-hoc extraction process.
- **LIMIT benchmark breakthrough**: On the LIMIT benchmark (designed to test lexical mismatch), Contriever's Recall@100 jumps from 0.053 to **0.729** when documents are represented as Latent Terms instead of dense vectors.

## Key Finding: Retrieval Training Is Essential

The Latent Terms structure **does not emerge from pre-trained language models alone**. Applying SAEs to vanilla BERT activations fails to produce a useful sparse vocabulary. The interpretable, Zipfian feature structure only appears after the model undergoes retrieval-focused contrastive training (e.g., the Contriever objective). This demonstrates that contrastive training teaches models a rich internal vocabulary of retrieval-relevant concepts — more than the models can express through their standard single-vector output.

## Implications

- **Hidden knowledge**: Current training methods teach retrieval models substantially more than they can express via single-vector scoring. The dense vector is a lossy bottleneck, not the model's full capability.
- **Trivial extraction**: SAEs provide a lightweight, post-hoc method to surface this knowledge without retraining or architectural changes.
- **Interpretability bonus**: Latent Terms are inherently interpretable — each feature can be inspected to understand what concept it represents, unlike opaque dense vectors.
- **Hybrid retrieval**: Latent Terms offer a principled way to combine dense and sparse retrieval, potentially enabling new hybrid architectures that leverage both paradigms.

## Related Concepts

- [[concepts/late-interaction|Late Interaction]] — another approach to going beyond single-vector scoring, using multi-token representations
- [[concepts/colbert|ColBERT and SPLADE]] — learned sparse retrieval methods that Latent Terms are benchmarked against
- [[concepts/sparse-autoencoders|Sparse Autoencoders]] — the core extraction mechanism underlying Latent Terms
