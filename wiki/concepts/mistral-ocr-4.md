---
title: "Mistral OCR 4"
created: 2026-06-24
updated: 2026-06-24
type: concept
tags:
  - ocr
  - document-intelligence
  - multimodal
  - multilingual
  - mistral
  - product
  - model
  - information-retrieval
  - rag
  - structured-outputs
  - agentic-retrieval
  - self-hosted
  - translation
sources:
  - raw/articles/2026-06-24_mistral-ai_ocr-4.md
---

# Mistral OCR 4

Mistral OCR 4 is a state-of-the-art optical character recognition model released by [[entities/mistral-ai]] on June 23, 2026. It represents the fourth generation of Mistral's document extraction technology, moving beyond simple text extraction to structured document understanding with bounding boxes, block classification, and inline confidence scores.

## Overview

Mistral OCR 4 is a small, focused model designed specifically for document intelligence workloads. Unlike general-purpose [[concepts/multimodal]] models that handle vision, language, and reasoning in one architecture, OCR 4 is purpose-built for the OCR task — consistent with Mistral's stated philosophy of modality-specific models being more efficient than monolithic ones for focused use cases.

The model supports **170 languages across 10 language groups**, runs in a **single container** for self-hosted deployments, and serves as an ingestion component for enterprise search, RAG, and domain-specific retrieval pipelines.

## Architecture and Capabilities

### Structured Document Representation

Where previous OCR generations focused on converting pages into clean text and tables, OCR 4 returns a structured representation of the document:

1. **Bounding boxes**: Localize each text element within the page, enabling in-context highlighting, source-grounded citations, and reliable data pipelines downstream
2. **Block type classification**: Each block is classified by semantic type — titles, tables, equations, signatures, paragraphs, and more — allowing downstream systems to understand document structure
3. **Inline confidence scores**: Generated per-page and per-word, driving source-grounded citations, redactions, and human-in-the-loop verification workflows
4. **Markdown-structured output**: Extracted text is delivered in clean markdown format for immediate consumption by RAG pipelines, agents, and applications

### Multilingual Coverage

The 170-language support across 10 language groups includes measurable gains on specialized and low-resource languages where several competing systems degrade. This is a significant differentiator in enterprise deployments requiring consistent quality across diverse document sources.

### Self-Hosted Deployment

OCR 4 is compact enough to deploy in a single container, enabling:
- **Data residency**: Document data stays within customer infrastructure
- **Sovereignty compliance**: Meets EU and other jurisdictional data requirements
- **Cost-efficient batch processing**: High-throughput ingestion without per-page API costs at scale
- **Air-gapped deployments**: Suitable for classified or sensitive environments

## Performance

### Benchmarks

| Benchmark | Score | Context |
|-----------|-------|---------|
| Human preference (annotator win rate) | 72% average | Preferred over every leading OCR and document-AI system tested |
| OlmOCRBench | 85.20 | Top overall score |

The 72% human preference win rate is the most significant metric — independent annotators preferred OCR 4's output over competitors in a majority of comparisons, suggesting superior real-world usability rather than just benchmark optimization.

### Benchmark Limitations

Mistral acknowledges known limitations of current OCR benchmarks in the release post. Public benchmarks may not capture:
- Performance on noisy, real-world document scans
- Low-resource language accuracy
- Structured element extraction quality (equations, signatures)
- End-to-end pipeline accuracy (OCR → RAG retrieval quality)

## Integration with Mistral Search Toolkit

OCR 4 is positioned as an ingestion component of **Mistral Search Toolkit**, an open-source, composable search framework announced at the AI Now Summit 2026. The structured output from OCR 4 supplies citation-ready inputs to the toolkit's ingestion, retrieval, and evaluation workflow.

This integration creates a complete pipeline:
```
Document → OCR 4 → Structured Output → Search Toolkit → RAG/Enterprise Search
```

The bounding boxes, block types, and confidence scores enable source-grounded citations in retrieval results — a critical capability for enterprise deployments where answer provenance must be traceable.

## Document AI vs. Pure OCR

Mistral offers two usage modes through the same API endpoint:

### Pure OCR Mode ($4/1000 pages, $2/1000 on Batch API)

Use when you want to:
- Embed fast, accurate document extraction directly into applications, agents, or data pipelines
- Work directly with raw response, bounding boxes, block types, and confidence scores for custom downstream logic
- Run high-volume batch ingestion with full control over throughput and cost
- Self-host for strict data privacy, sovereignty, or compliance requirements

### Document AI Mode ($5/1000 pages)

Adds structured layers on top of OCR output:
- **Schema-defined JSON output**: Pass a JSON schema alongside the document, and the OCR output is fed to `mistral-small-2603` to generate content shaped to your specification
- **Image annotation**: Pass an image annotation schema to trigger a vision-language model call per detected image
- **Custom instruction processing**: Use a custom prompt alongside a JSON schema to guide interpretation or summarization
- **Business user accessibility**: Enables non-technical users to produce structured results without writing downstream parsing logic

The practical decision rule: if you need raw extracted content with bounding boxes and block types, use OCR 4 as-is. If you need structured output reshaped into domain-specific formats, add Document AI parameters to the same call.

## Pricing

| Tier | Price | Use Case |
|------|-------|----------|
| OCR (standard) | $4 / 1000 pages | Real-time extraction in applications |
| Batch API | $2 / 1000 pages | High-volume, latency-tolerant ingestion |
| Document AI | $5 / 1000 pages | Structured JSON output with schema |

The batch pricing at $2/1000 pages makes large-scale document ingestion economically viable for enterprise archives, while the Document AI premium reflects the additional LLM inference cost for structured output generation.

## Platform Availability

- **Mistral Studio**: Native API access
- **Amazon SageMaker**: AWS marketplace deployment
- **Microsoft Foundry**: Enterprise platform integration — described by Microsoft's VP of AI Ecosystem Partnerships as "an important milestone" in their partnership with Mistral
- **Snowflake Parse Document**: Coming soon, enabling document understanding directly within Snowflake data pipelines
- **Self-hosted**: Available to enterprise customers for on-premise deployment

## Competitive Position

### vs. General-Purpose Multimodal Models

The key architectural insight behind OCR 4 is that a specialized, focused model outperforms general-purpose vision-language models on the specific OCR task. General-purpose models like GPT-4V or Claude Vision handle a wide range of visual tasks but may be:
- **More expensive** per page for pure extraction
- **Less accurate** on document-specific elements (tables, equations, signatures)
- **Slower** for high-volume batch processing
- **Harder to self-host** due to model size

OCR 4's small, focused architecture delivers better price-performance for document extraction specifically.

### vs. Traditional OCR (Tesseract, Azure OCR, Google Document AI)

Mistral's approach differs from traditional OCR engines in several ways:
- **Neural end-to-end**: Single model handles detection, recognition, and structure understanding
- **Block typing**: Semantic classification of elements (not just text regions)
- **Confidence scoring**: Per-word confidence enables downstream quality filtering
- **Multilingual**: 170 languages in a single model vs. per-language models in traditional systems

## Relationship to Mistral's Broader Strategy

OCR 4 fits into Mistral's multi-product strategy as a vertical AI capability:

1. **Model portfolio expansion**: Adds document intelligence alongside coding ([[concepts/coding-agents/codestral]]), speech ([[entities/mistral-voxtral-tts]]), and general reasoning models
2. **Enterprise pipeline**: OCR → Search → RAG creates a complete enterprise document processing stack
3. **Self-hosted differentiation**: Competes with cloud-only offerings from Google and Microsoft by offering on-premise deployment
4. **European data sovereignty**: Addresses GDPR and EU regulatory requirements that cloud-only solutions struggle with

## Open Questions

- **Real-world accuracy**: How does OCR 4 perform on degraded scans, handwritten documents, and complex layouts not represented in benchmark datasets?
- **Self-hosting complexity**: What are the operational requirements (GPU, memory) for single-container deployment at enterprise scale?
- **Language coverage gaps**: Which of the 170 languages have the weakest performance, particularly for low-resource languages with limited training data?
- **Adoption trajectory**: Will enterprise customers adopt OCR 4 as a standalone product, or primarily through the Search Toolkit integration?
- **Competitive response**: How will Google (Document AI), Microsoft (Azure OCR), and Amazon (Textract) respond to Mistral's entry into the document intelligence market?

## Related Pages

- [[entities/mistral-ai]] — Mistral AI company overview
- [[concepts/multimodal]] — Multimodal AI models
- [[concepts/mistral-medium-3-5]] — Mistral Medium 3.5 model
- [[entities/mistral-voxtral-tts]] — Mistral Voxtral TTS speech model
- [[concepts/information-retrieval]] — Information retrieval concepts
- [[concepts/agentic-retrieval]] — Agentic retrieval patterns
- [[concepts/mistral-workflows]] — Mistral enterprise workflow orchestration
