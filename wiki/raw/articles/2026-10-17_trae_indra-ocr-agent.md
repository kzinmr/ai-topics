---
source_url: https://www.trae.ai/blog/trae-eng-06
ingested: 2026-10-17
sha256: 31be99fd0bea02c37f5967393aa37605471936aeb964701eb36f00dfe0cb8737
---

# Indra: An OCR Agent that Reasons (ByteDance TRAE)

TRAE Team, October 16, 2026. A 35B-class OCR agent that reads every page in parallel and gets 2.6× the accuracy of Claude at a fifth of the price.

TRAE's core business is turning messy engineering documents into agent-ready context. Their thesis: **"OCR is not parsing. OCR is reasoning."** Real production documents — dense tables, multi-column papers, scanned receipts, nested forms — require a model that can look at a page, understand its structure, and decide what to do.

## The two structural problems with traditional OCR pipelines

Traditional OCR splits a page into fragments and chains them with a layout model, a recognition model, and heuristics. Errors compound at every seam: a missed table cell is never revisited, a misread character propagates into downstream search and indexing.

The first OCR models people reach for (Qwen3.5, DeepSeek-OCR) are strong but operate like a conveyor belt — one page in, one linear pass out. They don't know if they did a good job. There is no confidence, no second look, no second opinion.

## TRAE's three principles

**1. Every page reads in parallel, not one at a time.** Indra splits a document into pages and starts one agent per page, all at once. A 500-page contract gets read as 500 independent agents working in parallel rather than one worker on a conveyor. Throughput scales with page count, not model size.

**2. Every output is verified by a committee of experts.** Indra reads each page four times, in four roles, in parallel:
- **Structural reader** — what kind of document is this, what are the regions
- **Extractor** — pull the text out, faithfully
- **Critic** — attack what the extractor produced, find every error
- **Integrator** — combine only the parts that survive the attack

The critic role is what makes this different — nothing ships until an adversarial reader has tried to find problems and failed. For every output, Indra also reports a page-level **confidence score** so a human reviewer can sort pages by trustworthiness.

**3. Every hard page gets a second look.** A page that scored itself low gets automatically re-read. Indra knows what it got wrong — and goes back for more compute. The same budget spent twice on a hard page turns a near-miss into an exact match.

## Results (TRAE-Bench-v2, 1,011 pages)

TRAE-Bench-v2: 1,011 pages, real documents across three tiers — *everyday*, *tricky*, *hell mode* (dense tables, multi-column layouts, scanned receipts, nested forms, hand-filled invoices, rotated pages). Ground truth is character-level. Score = 1 − Normalized Levenshtein Distance (100 = exact transcription).

Headline: **Claude Fable 5 scores 79.61 on everyday pages and falls to 46.02 on hell mode. Indra reads 94.40 everyday and holds 84.06 on hell mode.** Across all real documents, Indra is 2.6× more accurate than Claude, 2.8× more than GPT-5.6 Sol. A 35B-class open-source model built specifically for OCR beats models 10×+ its size on hard documents — the first time a small open model has clearly outperformed the frontier on document transcription.

## Why the same model trained on OCR becomes an expert

- **Indra doesn't guess, it reads the pixels.** Frontier models are trained heavily on synthetic markdown and LaTeX documents, so they fall back on prior knowledge instead of looking at the image. Indra was trained on real scanned pages, so it trusts what's on the page in front of it.
- **Indra can read at native resolution** and zoom in, so a 1px dash on a scanned receipt doesn't vanish.
- **Indra reasons, not memorizes.** Fine-tuned only on the OCR domain, its entire capacity goes into this one skill — layout, tables, handwriting, stamps. Frontier models carry that knowledge shallowly, as a small fraction of general pretraining, so they can't reason deeply about structure.

Takeaway: *"35B trained to reason about documents beats 1T trained to know about everything."*

## Production architecture & cost

TRAE ships Indra into a real production pipeline for millions of enterprise documents daily. Architecture: an orchestrator splits documents and assigns pages to a pool of stateless workers, then aggregates results in document order (any page can be retried without blocking the others).

Two Indra replicas handle 30 concurrent pages per second on a single H100; a vLLM-style engine with radix-tree KV reuse keeps pages warm. Indra's 8× compression (via DeepSeek-OCR 2's Visual Context Transformer) means a full A4 page fits in 336 visual tokens — the reason it runs at production cost.

**Price:** On TRAE's production benchmark (2,374 pages, 17,372 images), Claude Fable 5 at max reasoning runs **$1,119.21 / 14.7h**. Indra (same benchmark, 2 GPUs) costs **$221.81 / 11.5h** — ~1/5 the price. Indra costs less per page as difficulty rises (fixed cost per agent read), while per-call pricing models (Gemini 3.1 Pro, GPT-5.6 Sol, Claude Fable 5) climb with each page.
