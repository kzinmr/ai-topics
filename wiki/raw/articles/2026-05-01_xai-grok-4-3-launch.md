# xAI Launches Grok 4.3 at Aggressively Low Price with Custom Voices Suite

**Source:** VentureBeat  
**Date:** May 1, 2026  
**Author:** Carl Franzen  
**URL:** https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite

## Summary

xAI released Grok 4.3, featuring "always-on reasoning" (permanent chain-of-thought), a 1 million token context window, and aggressive API pricing ($1.25/$2.50 per 1M input/output tokens). The release includes a Custom Voices voice cloning suite requiring as little as 120 seconds of reference audio.

## Key Details

- **Always-on reasoning**: Unlike previous models where reasoning could be toggled, Grok 4.3 is built with reasoning as a permanent, active state
- **1M token context window**: Roughly equivalent to several thick novels or a mid-sized application codebase
- **Knowledge cutoff**: December 2025 (supplemented by live web/X search)
- **Agentic capabilities**: Spreadsheet engineering (multi-sheet .xlsx), branded PDFs, PowerPoint decks
- **Built-in tools**: Sandboxed Python code execution, integrated RAG for file/collection search

## Pricing (Aggressive Undercutting)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Grok 4.3 | $1.25 | $2.50 |
| GPT-5.5 | $5.00 | $30.00 |
| Claude Opus 4.7 | $5.00 | $25.00 |

- Reasoning tokens billed at same rate as completion tokens
- Prompt caching: $0.20 per million tokens
- Tool call fees: $5.00/1K (Web Search/Code), $10.00 (File Attachments)
- Safety violation fee: $0.05 per blocked request

## Benchmarks

- #1 on CaseLaw v2 (79.3% accuracy) — 25-point jump over Grok 4.20
- #1 on CorpFin
- 1500 Elo on GDPval-AA (agentic tasks)
- Weaknesses: regression in simulation actions (Vending-Bench 2), 11% on ProofBench (difficult math)

## Custom Voices

- Voice cloning from 120-second reference clip
- Mimics delivery patterns (professional vs casual inflections)
- Private to user's team; one-click deletion
- U.S. only (excluding Illinois)
- Voice Agent: ~$3.00/hr; Standalone TTS: $4.20/1M chars

## Enterprise Compliance

- SOC 2 Type II auditing, HIPAA eligibility, GDPR compliance
- System prompt instructs: "you do not assign broad positive/negative utility functions to groups of people"
- Best for high-volume document processing; less reliable for high-frequency autonomous agents or advanced mathematics

## Grok Computer Connection

Launched alongside Grok Computer (xAI's autonomous desktop agent, private beta April 13, 2026). Grok 4.3 serves as reasoning/generation layer; Grok Computer handles execution/automation by reading screen pixels.
