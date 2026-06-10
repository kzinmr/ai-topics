---
title: "Claude Opus 4.7"
type: concept
aliases:
  - claude-opus-4-7
  - opus-4-7
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - anthropic
  - model
status: complete
sources:
  - url: "https://www.anthropic.com/news/claude-opus-4-7"
    title: "Introducing Claude Opus 4.7 (Anthropic Official, 2026-04-16)"
  - url: "https://www.anthropic.com/claude/opus"
    title: "Claude Opus 4.7 Product Page"
  - url: "https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available"
    title: "Claude Opus 4.7 on GitHub Copilot"
  - url: "https://www.anthropic.com/claude-opus-4-7-system-card"
    title: "Claude Opus 4.7 System Card"
---

# Claude Opus 4.7

**Claude Opus 4.7** is a frontier LLM released by **Anthropic on April 16, 2026**. It is the successor to Opus 4.6, delivering significant improvements in advanced software engineering, visual recognition, and long-term multi-step task execution.

## Release Information

- **Release date**: April 16, 2026
- **Context window**: **1 million tokens**
- **API availability**: Anthropic API, GitHub Copilot, Claude.ai
- **Model Card**: [Published](https://www.anthropic.com/claude-opus-4-7-system-card)

## Key Improvements

### 1. Software Engineering
- Significant improvement on the hardest coding tasks
- Reaches a level where tasks that "previously required supervision" can be **confidently delegated**
- Handles complex long-running tasks **rigorously and consistently**
- **Precise attention** to instructions and **self-verification** capability

### 2. Vision Capabilities
- **High-resolution image recognition** — processes more detailed visual information
- XBOW visual accuracy benchmark: **98.5%** (Opus 4.6 was 54.5%)
- Improved **taste and creativity** on professional tasks
- Improved quality of UI, slides, and documents

### 3. Agent Capabilities
- **Robust multi-step execution** — also praised on GitHub Copilot
- Improvements in **long-horizon reasoning** and **tool-dependent workflows**
- New behavioral pattern of **proving/verifying** before code execution (reported by Vercel)

## Benchmark Improvements

| Area | Opus 4.6 | Opus 4.7 | Improvement |
|------|---------|---------|------|
| Visual accuracy (XBOW) | 54.5% | **98.5%** | +44% |
| One-shot coding | Baseline | **Significantly improved** | — |
| Self-limitation awareness | Moderate | **Notably honest** | — |

## Tokenizer Changes

Opus 4.7 uses an updated tokenizer:
- Same input may map to **1.0–1.35x** tokens
- Increased thinking at high effort levels (especially later turns in agent settings)
- More output tokens in exchange for improved reliability

## Security and Governance

- **Step toward Mythos**: Opus 4.7 serves as a **safety testbed** for Mythos-class models
- **Project Glasswing**: Evaluation of cybersecurity risk and benefit
- **Cyber safeguard**: Automatically detects and blocks prohibited/high-risk cybersecurity uses
- **Relationship to Mythos**: Does not have as broad capabilities as Mythos Preview, but surpasses Opus 4.6 on all benchmarks

## Performance (User Reports)

- **Vercel (Joe Haddad)**: "No regression from Opus 4.6. Astounding on one-shot coding tasks. More precise and complete. Notably honest about its own limitations."
- **XBOW (Oege de Moor)**: "Step change in computer use tasks. The biggest pain points of Opus 4.6 are effectively resolved."
- Users build games, websites, animations, and CAD designs **in minutes**

## Related Concepts

- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[concepts/claude/perfect-memory]] — Claude Code persistent memory

## Sources

- [Introducing Claude Opus 4.7 (Anthropic Official)](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude Opus 4.7 Product Page](https://www.anthropic.com/claude/opus)
- [GitHub Copilot Changelog](https://github.blog/changelog/2026-04-16-claude-opus-4-7-is-generally-available)
- [Claude Opus 4.7 System Card](https://www.anthropic.com/claude-opus-4-7-system-card)
