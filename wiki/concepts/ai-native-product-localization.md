---
title: AI-Native Product Localization
created: 2026-05-29
updated: 2026-05-29
type: concept
tags:
  - ai-native
  - translation
  - coding-agents
  - agentic-engineering
  - developer-tooling
  - software-engineering
  - feedback-loop
sources: [raw/articles/sierra.ai--blog-ai-native-product-localization--763f5456.md]
---

# AI-Native Product Localization

Using AI coding agents and batch processing to prepare software products for multiple languages. Case study from Sierra (2026): a 10-person, 9–12 month project at Slack reduced to 1 engineer, 4 months using AI.

## The Problem

Localizing an app means removing English assumptions baked into the codebase:
- Find user-facing strings and wrap in localization functions
- Restructure English-centric patterns (concatenation, pluralization) into ICU MessageFormat syntax
- Extract strings into translation files
- Generate translations for each locale
- Fix UI breakage from longer translated strings
- Add linting and CI automation

Traditional approach requires multiple engineers (backend, frontend, mobile), product managers, QA, and design — primarily due to coordination overhead.

## Sierra Case Study: Three-Phase AI Workflow

### Phase 1: IDE Agents (Cursor)
- Asked Cursor to prepare individual files for localization
- Results: "surprisingly good" but **inherently blocking and sequential**
- One file at a time couldn't scale across 900+ frontend files

### Phase 2: Cloud Agents (Parallel)
- Multiple agents working across many files simultaneously
- Improved throughput but introduced: error tracking at scale, PR review bottlenecks (each agent generated its own PR)
- Small error rate in string wrapping, ICU syntax, concatenation patterns

### Phase 3: Batch Script Pipeline (The Unlock)
The breakthrough: a **batch script calling Claude API directly**, bypassing agent UIs entirely.

```text
Script accepts: file list or glob pattern
↓
Sends each file + localization skills documentation to Claude API
↓
Writes transformed result back to disk (configurable concurrency)
```

**Workflow loop:**
1. Process ~30 files per batch
2. Manually review every changed file (catch failure patterns before propagation)
3. Collect mistakes → have AI explain why → update skills documentation
4. Repeat

The documentation evolved into a "highly specialized playbook of edge cases, project-specific patterns, and common localization failures."

### Coevolution with Linting
After bulk wrapping, a **linter rule** flagged unwrapped user-facing strings:
- Linter itself was largely AI-written
- Workflow: Run linter → batch-fix flagged files → run linter again → investigate warnings
- AI helped distinguish false positives and refine the linter
- **Coevolution**: migration pipeline and linter cross-validated each other, producing higher-confidence signals than either alone

**Economic insight**: Because refining costs had become so low, the engineer kept improving both systems instead of tolerating known inaccuracies.

## Context Window Pitfall

A critical lesson: the **feedback loop that improves AI output can eventually degrade it**.

After many iterations of skills documentation updates, error rates started increasing — even for patterns explicitly documented as forbidden. Root cause: the skills docs grew too large for the API's **context window** to reliably process. The model consumed the beginning and silently lost instructions buried later.

**Fix:**
- Rewrite documentation to be dramatically more concise (fewer words, fewer examples, more signal per line)
- Split into smaller focused files referenced selectively:
  - `panels-and-typing.md`
  - `what-not-to-translate.md`
- Structure like an index, optimized for **selective retrieval** rather than sequential reading

Result: documentation structure "looked very different from traditional human-oriented docs — dense, highly scannable, optimized for selective retrieval."

## String Context Architecture Innovation

Traditionally, `@i18n` comments provide translator context inline in source code. At Sierra, AI generated these comments — verbose but helpful since translation models perform better with richer context.

**Problem**: Comments cluttered UI files with metadata humans don't need to read.

**Insight**: If AI generates the descriptions and AI primarily consumes them, they don't need to live inline.

**Solution**: Dynamic description generation during extraction:
1. Extraction records file location + source position for every string
2. Enrichment step sends small code window to Claude → generates contextual description
3. Description stored in translation files, not source code

Result: detailed translator context without codebase bloat.

## Meta-Lesson: Work Becomes Feedback Loop Design

> "The work shifted from directly performing migrations to designing feedback loops."

Key shifts:
- From manual transformation → building systems that generate, validate, identify failures, refine instructions
- From doing the work → designing processes that do the work
- AI didn't eliminate engineering judgment — it elevated its importance (architecture, systemic failure patterns, quality standards)

## Tradeoffs
- Fewer human reviewers → fewer QA catches (untranslated strings in less-visited pages)
- One-person team → knowledge silo risk → compensating with comprehensive docs for both agents and future engineers
- Prior experience massively accelerates the process (knowing what patterns to watch for)

## Related Pages
- [[agentic-engineering]] — Designing AI agent workflows
- [[feedback-loop]] — Pattern of continuous improvement
- [[context-engineering]] — Context window management
- [[ai-coding]] — AI-assisted software development
- [[prompt-caching]] — Cost optimization for repeated API calls
