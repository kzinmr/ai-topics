# Mistral OCR 4 : SOTA OCR for Document Intelligence

**Source:** https://mistral.ai/news/ocr-4/
**Published:** 2026-06-24
**Author:** Mistral AI
**Archived:** 2026-06-24

---

## Summary

Mistral OCR 4 is Mistral AI's latest optical character recognition model. It features bounding boxes, block classification, inline confidence scores, and supports 170 languages across 10 language groups. It runs in a single container for self-hosted deployments and integrates with Mistral Search Toolkit for enterprise search, RAG, and domain-specific retrieval pipelines.

## Key Features

- **Breakthrough performance**: Independent annotators prefer OCR 4 over every leading OCR and document-AI system tested, with win rates averaging 72%. Top overall score on OlmOCRBench (85.20).
- **Segmentation, not just text**: Bounding boxes, typed-block classification (titles, tables, equations, signatures), and inline confidence scores.
- **Multilingual coverage**: 170 languages across 10 language groups, with measurable gains on specialized and low-resource languages.
- **Self-hosted deployment**: Compact enough for single-container deployment, keeping document data in customer environment.
- **Document AI integration**: Same endpoint supports structured JSON output via schema, image annotation via vision-language model, and custom prompts.

## Pricing

| Tier | Price |
|------|-------|
| OCR (text-to-text) | $4 / 1000 pages |
| Batch API | $2 / 1000 pages |
| Document AI | $5 / 1000 pages |

## Integration

- Available via Mistral Studio, Amazon SageMaker, Microsoft Foundry
- Coming soon: Snowflake Parse Document
- Integrated with Mistral Search Toolkit (public preview) for composable search framework

## Source Content (Structured Extraction)

The model returns structured document representation with:
- Bounding boxes for each block
- Block type classification (title, table, equation, signature, etc.)
- Inline confidence scores per-page and per-word
- Markdown-structured text output

## Use Cases

- Fast document extraction in applications, agents, or data pipelines
- High-volume batch ingestion with cost control
- Self-hosted deployment for data privacy, sovereignty, compliance
- Document AI mode for structured JSON, image annotation, and custom instruction processing

## Related Mistral AI Posts

- Introducing Mistral OCR 4 (June 23, 2026)
- Mistral Search Toolkit announcement at AI Now Summit 2026
- OCR 4 webinar scheduled for July 7, 2026

## Raw Body

Mistral OCR 4 : SOTA OCR for Document Intelligence — June 23, 2026 By Mistral AI. Today, we're releasing Mistral OCR 4, featuring bounding boxes, block classification, and inline confidence scores alongside extracted text. The model supports 170 languages across 10 language groups, runs in a single container for fully self-hosted deployments, and serves as an ingestion component for enterprise search, RAG, and domain-specific retrieval pipelines. OCR 4 is a small, focused model, and this post covers what's new, how it performs on public and internal benchmarks, the known limitations of those benchmarks, and guidance on when to use the model API versus Document AI.

Highlights: Breakthrough performance — independent annotators prefer OCR 4 over every leading OCR and document-AI system tested, with win rates averaging 72%, alongside the top overall score on OlmOCRBench (85.20). Segmentation, not just text — alongside the extracted text, OCR 4 returns bounding boxes, typed-block classification (titles, tables, equations, signatures, and more), and inline confidence scores. Integrated with Mistral Search Toolkit (public preview) — OCR 4 is an ingestion component of Search Toolkit, Mistral's open-source, composable search framework. Multilingual coverage — support for 170 languages across 10 language groups, with measurable gains on specialized and low-resource languages. Run on your own infrastructure — OCR 4 is compact enough to deploy on a single container.

Pricing: OCR Multimodal Text-to-text OCR $4 / 1000 pages, Batch-API $2 / 1000 pages, Document AI $5 / 1000 pages.

Both Mistral OCRv4 and Document AI (powered by OCRv4) are available via API through Mistral Studio, Amazon SageMaker, Microsoft Foundry, and coming soon Snowflake Parse Document. For organizations with stringent data-privacy requirements, OCR 4 also offers a self-hosting option.
