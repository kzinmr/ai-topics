## [2026-06-21] Claude Blog Ingest — Claude Code Steering Methods article ingested

**Source:** https://claude.com/ja/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
**Date:** 2026-06-18
**Author:** Anthropic

### Actions Taken

1. **Raw article saved:** `raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md`
   - Full article content extracted and saved with proper frontmatter
   - Tags: claude-code, coding-agents, ai-agents, customization, hooks, skills, subagents, rules, claudefile

2. **New concept page created:** `concepts/claude-code/claude-code-steering-methods.md`
   - Comprehensive documentation of Claude Code's seven steering methods
   - Covers CLAUDE.md files, rules, skills, subagents, hooks, output styles, and system prompt appending
   - Includes comparison table, decision guide, and best practices
   - Tags: claude-code, coding-agents, ai-agents, customization, hooks, skills, subagents, rules, claudefile, developer-tools
   - Sources: raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md

3. **Index updated:** Added entry to `index.md` under Claude Code concepts section
   - Location: After `claude-code-goal` entry (line 1195)
   - Description: Seven methods for customizing Claude's behavior with comparison of loading behavior, compaction characteristics, context costs, and best use cases

### Article Summary

The article explains seven methods for instructing and customizing Claude's behavior in Claude Code:

1. **CLAUDE.md files** — Project-specific instructions that load at session start
2. **Rules** — Path-scoped constraints in `.claude/rules/`
3. **Skills** — Procedural workflows in `.claude/skills/`
4. **Subagents** — Isolated assistants for side tasks in `.claude/agents/`
5. **Hooks** — Deterministic automation on lifecycle events
6. **Output styles** — System prompt injections for role changes
7. **System prompt appending** — Additive instructions via CLI flag

Each method has different characteristics regarding:
- When instructions load into context
- Whether they persist through long sessions (compaction behavior)
- How much authority they carry

### Wiki Impact

- **New page:** `concepts/claude-code/claude-code-steering-methods.md` (9,286 bytes)
- **Updated page:** `wiki/index.md` (added entry)
- **Raw article:** `raw/articles/2026-06-18_anthropic_steering-claude-code-skills-hooks-rules-subagents-and-more.md` (16,507 bytes)

### Related Pages

- [[concepts/claude-code/claude-code]] — Claude Code as a coding agent
- [[concepts/claude-code/claude-code-skills]] — Claude Code Skills mechanisms
- [[concepts/claude-code/claude-code-best-practices]] — Claude Code Best Practices
- [[concepts/agentic-engineering]] — Agentic engineering patterns
- [[concepts/coding-agents]] — AI agents for software development

---

## [2026-06-21] Blog Wiki Ingest — AI-Assisted Development enriched, 2 entity pages updated

**Pipeline:** blog-ingest -> blog-triage -> blog-wiki-ingest
**Source:** blog-ingest checkpoint (11 articles + 4 unsaved)

### Pages Updated

- **concepts/ai-assisted-development.md** — Expanded from stub (24 lines) to substantive page (89 lines). Added overview, use cases, and "LLMs for Formal and Scientific Programming" section covering John D. Cook's Claude→Z3/Python chessboard constraint satisfaction experiment (192 solutions, 24 unique). Tags: concept, coding-agents, software-engineering, developer-tooling, formal-methods. Source: raw/articles/johndcook.com--blog-2026-06-20-z3-python-claude--6dbfee73.md.

- **entities/john-d-cook-applied-mathematics-consulting.md** — Added "Claude + Z3/Python Code Generation (June 2026)" subsection under LLM-Assisted Formal Proofs. Updated frontmatter updated: 2026-06-21. Added source and reference entries.

- **entities/lcamtuf.md** — Added timeline entry for Jun 2026 "The 100,000 whys of AI". Added "AI Content Slop Detection: The Quasi-Determinism Argument" subsection in Core Ideas. Added [[concepts/ai-slop]] cross-reference. Updated frontmatter updated: 2026-06-21. Added reference entry.

### Triage Summary

1 take: johndcook Z3/Python Claude article -> concepts/ai-assisted-development.md enrichment + entity page update
1 reference: lcamtuf "100,000 whys" -> entity/lcamtuf.md enrichment
13 skips: non-AI content (Windows HMODULE, construction digest, package management, systemd, glassblowing, SVG license, Postgres benchmark, kernel stable, Epstein class, 4 unsaved articles)