---
title: "Mem++ (Non-Destructive Organizational Agent Memory)"
created: 2026-10-03
updated: 2026-10-03
type: concept
tags: [concept, memory-systems, agent-memory, ai-agents, retrieval, information-retrieval]
aliases: [Mem++, mem-plus-plus, non-destructive memory, read-time selection]
confidence: medium
sources: ["raw/articles/arxiv-2610.02002-mempp-non-destructive-organizational-memory.md"]
---

# Mem++ (Non-Destructive Organizational Agent Memory)

**Mem++** (Yehia et al., arXiv:2610.02002, Oct 2026) is an agent-memory framework built around a
single design inversion: **shift from write-time distillation to read-time selection.**

Most agent-memory systems *compress the record at write time* — distilling each document into
facts, notes, or graph edges. The authors' critique: this **fixes what can be answered before any
question is asked**, and overwrites history that later becomes relevant.

## The organizational problem

LLM agents now do organizational work where many authors record decisions across documents over
months. Crucially, **a revised decision arrives as a new document, not an edit** — so answering a
question requires knowing *which version held at a given time*. Write-time distillation destroys
exactly the version/time dimension the question needs.

## Mechanism

- **Store every document whole** with its date and author.
- **Call no generative model at write time** (no lossy summarization on the way in).
- At **read time**, retrieve only documents dated **up to the time the question asks about**, then
  **fuse lexical and semantic rankings**.
- Keep *all* versions rather than overwriting; **leave the choice of which version governs to the
  answering model**.

This is the append-only / "keep the record" stance applied to agent memory — closer to a
[[concepts/filesystem-memory]] or bitemporal document store than to a fact-triple graph.

## Results

- **OrgMemBench** (organizational benchmark): beats the strongest memory-system baseline by
  **8.0–13.1 points** across two answering models.
- With `gpt-4.1-mini`, best overall score, **+2.6 over plain RAG**.
- Best average LLM-judge score on **LoCoMo**; **second** on **LongMemEval-S** (behind only its own
  entity-graph variant — i.e., graphs still win when entity-centric recall dominates).
- Code: `github.com/AIDAChip-Inc/mem-plus-plus`.

## Why it matters / trade-offs

- Challenges the write-time-distillation default that dominates the memory-systems literature
  (see the "two camps" debate below).
- **Cost of the inversion:** pushing compression to read time means *every* query pays retrieval +
  selection cost, and the retrieval set grows unboundedly with document history — the paper's
  read-time fusion must scale with corpus size.
- The "let the answering model pick the version" move relocates the hard reasoning from the memory
  layer to the model, so end-to-end quality becomes more dependent on the answering model's
  temporal-reasoning ability.

## Open questions

- Single source, industry lab (`confidence: medium`); OrgMemBench is new and not yet an
  independent standard.
- How well does non-destructive storage hold up on *very* long-lived corpora (read-time latency,
  retrieval set size)?

## Related

- [[concepts/ai-agent-memory-two-camps]] — the write-vs-read compression trade this targets
- [[concepts/memory-systems-design-patterns]] — where "write-time distillation" is the default
- [[concepts/memory-integrity]] — preserving provenance/history against lossy rewriting
- [[concepts/filesystem-memory]] — keep-the-whole-record philosophy
