---
title: "Components of Agent Memory (Anthropic Dreaming Research)"
type: concept
created: 2026-11-13
updated: 2026-11-13
tags:
  - ai-agents
  - memory-systems
  - context-engineering
  - anthropic
sources:
  - "raw/articles/anthropic.com--the-components-of-agent-memory-anthropic--90b9a347.md"
  - "https://www.anthropic.com/research/components-of-agent-memory"
related:
  - "[[concepts/sleep-time-compute]]"
  - "[[concepts/wiki-memory]]"
  - "[[concepts/agent-wikis]]"
  - "[[concepts/ai-agent-memory]]"
  - "[[concepts/continual-learning]]"
  - "[[entities/rlancemartin]]"
---

# Components of Agent Memory (Anthropic Dreaming Research)

Anthropic's November 2026 research post decomposing agent memory into components and
explaining how **"dreaming"** — an offline, sleep-like consolidation pass over session
logs — corrects, updates, and creates memory representations. It is the first-party
Anthropic articulation of the sleep-time-compute idea ([[concepts/sleep-time-compute]],
Letta/UC Berkeley) applied to Claude's production memory.

## Scope Definition

"Agent memory" = knowledge Claude gains from experience and retains **between sessions**
as readable context. Explicitly **excludes**: weight changes (training), in-context
learning (single conversation), and compaction (summaries replacing older turns).

Analogy: hippocampus captures experiences online; consolidation into the neocortex happens
offline during sleep. Agents capture work in logs/transcripts; dreaming replays them.

## The Components

1. **Memory notes** — salient events tagged in-session or written to a memory store
   (folder of notes). "Memory can be a prediction about what the future will need."
2. **Dreaming** — offline replay of session transcripts that: (a) **corrects** wrong or
   drifted notes against transcript ground truth, (b) **builds new representations**
   (wikis, indexes), (c) **promotes notes** up the memory hierarchy (context injection),
   (d) **shapes memory toward a goal** (task-specific wiki-building instructions),
   (e) **fills cross-session gaps** (dangling links, missing pages).
3. **Wiki representations** — Claude-written, link-rich page collections used as a map
   over memory (see [[concepts/agent-wikis]], [[concepts/wiki-memory]]).

## Key Eval Results

- **CL-Bench 1.0** (long-horizon memory benchmark, via Claude Managed Agents): model
  generations differ in closing the learning loop. Sonnet 4.6 → untested theories only;
  Opus 4.7 → consolidated reference doc with checked/unchecked flags; Sonnet 5 →
  grader-confirmed entries + corrections; **Opus 5 first to close the loop** (validated
  rules + trap warnings). Opus 5.5 / Sonnet 5.5 also close it at ~Opus 5 level.
- **Salience judgment (Pokémon Red)**: Sonnet 3.7 wrote 413 files / 225 folders, 1 badge;
  Fable 5 wrote 9 files + `global.md` dashboard, **4 badges**. Lesson: don't store
  screen-readable state; store strategy, plans, tested rules.
- **Steering**: telling Claude *what memory is for* (not *how*) beat fixed rules —
  "record only failures" **destroyed** most of the memory boost for Opus 5/4.7.
  Prompting older models (Sonnet 4.6) to read memory + test theories nearly doubled
  CL-Bench scores.
- **Dreaming corrects memory**: Mt. Moon case — wrong PokéCenter location note caused a
  3× ledge-loop failure; dreaming replayed the transcript, caught the error, rewrote the
  note → Claude reached Cerulean City.
- **Wiki scaling (Stainless corpus)**: ~350k files / ~420M tokens, 25 questions; scaling
  dreaming sessions 2 → 128 raised graded-criteria score **13% → 48%**. Wiki + search:
  54% → 61% vs 53% search alone; saves ~20k tokens/question.
- **Harvey LAB / merger docs**: cross-document judgment questions 87% (wiki) vs 73%
  (search); single-document retrieval tasks showed no gain; one wiki grew larger than
  the corpus (Borges "On Exactitude in Science" failure mode).
- **Goal-directed wiki building**: contract-terms task — shared-table summarization lost
  facts (72%); a reflection loop that rewrote the build instructions (per-contract pages,
  verbatim quotes, one agent per page) reached **100%** of grading criteria.
- **Promotion/context injection**: Claude Code auto-memory keeps the injected layer small
  — loads only the first 200 lines / 25 KB of `MEMORY.md` as an index.

## Open Questions (Anthropic's own)

- When to write memory: in-session capture is immediately available but steals attention;
  dreaming is backgrounded but not immediately accessible.
- Keeping memory fresh: continuous verification is impractical; focus dreaming on
  likely-to-change info or tune dreaming cadence by access frequency.
- Transcript search as the foundation vs. maintained representations — combining both
  works, but representations need compute to avoid accumulating errors/hallucinations.

## See Also

- [[concepts/sleep-time-compute]] — the research idea dreaming implements
- [[concepts/agent-wikis]] / [[concepts/wiki-memory]] — the wiki representation component
- [[concepts/claude/memory]] — file-based memory architecture
- [[concepts/continual-learning]] — harness/context-layer learning
