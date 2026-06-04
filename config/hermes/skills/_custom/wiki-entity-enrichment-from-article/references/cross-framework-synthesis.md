# Cross-Framework Synthesis Pattern

When tasked with ingesting articles from multiple authors that present different frameworks/taxonomies on the **same topic**, produce a **unified concept page** that synthesizes both — not separate pages for each framework. The synthesis itself is the durable value.

## When to Use

- Two or more authoritative sources present different organizational schemes for the same concept
- The frameworks are complementary (e.g., one is implementation-focused, the other is taxonomy-focused)
- The mapping between frameworks is non-obvious and worth making explicit

**Example trigger**: "AnthropicのContext Engineeringに関する記事をwikiに取り込んで。取り込む際にはLance Martinによる整理と結合考察して。"

## Pattern

### 1. Save all source articles as raw articles first
Follow `raw-article-filename-policy` for naming. Each source gets its own raw file.

### 2. Create a single unified concept page
The page should include:

#### a. Common ground first
Start with what both frameworks agree on: definitions, core principles, why it matters. This establishes the shared foundation before introducing differences.

#### b. Present both frameworks side-by-side
Give each framework its own clearly labeled section with its organizing principle:
- **Anthropic's implementation view** (organized by "where context lives and how it flows")
- **Lance Martin's 4-strategy taxonomy** (organized by "what operation they perform on context")

Use visual structure (tables, ASCII diagrams, bullet hierarchies) to make the organizational logic clear at a glance.

#### c. Mapping table (the synthesis)
Create an explicit mapping table showing how categories from framework A correspond to framework B:

```
| Framework A (2025) | Framework B (2025) |
|---|---|
| **Write** (scratchpads, memories) | Structured Note-Taking, Memory tool |
| **Select** (memory, tools, knowledge) | Just-in-Time Retrieval, Tool design |
| **Compress** (summarization, trimming) | Compaction, Context trimming |
| **Isolate** (multi-agent, code agents) | Sub-Agent Delegation |
```

When one framework has categories the other lacks (e.g., Anthropic's "System Prompts" sits above Lance Martin's 4 operations), note this explicitly.

#### d. Advanced/derived patterns
Both frameworks may spawn derivative patterns worth covering:
- Give Agents a Computer
- Progressive Disclosure
- Prompt Caching
- Ralph Wiggum Loop
- Multi-Layer Action Space

#### e. Trade-offs table
Capture the costs of each strategy:
```
| Strategy | Benefit | Cost |
|---|---|---|
| Compaction | Stays within context budget | Irreversible information loss |
| Sub-agents | Clean separation of concerns | Up to 15× token overhead |
```

#### f. Future directions / The Bitter Lesson
If relevant, note where model scaling may absorb hand-crafted techniques.

#### g. Practical checklist
A 6-8 item checklist helps the reader apply the synthesis.

### 3. Create/update author entity pages
If either author's entities don't have full pages, create them. If skeleton pages exist, enrich them. Cross-link to the concept page.

### 4. Cross-linking
Link extensively to related concept pages. Even broken wikilinks are acceptable — they signal future pages to create.

## Example Output

This session produced `concepts/context-engineering.md` synthesizing Anthropic's "Effective Context Engineering for AI Agents" (2025-09) and Lance Martin's "Context Engineering for Agents" (2025-06) + "Agent Design Patterns" (2026-01). The mapping table is the core synthesis artifact.

## Pitfalls

- **Don't create separate pages** for each framework if they're about the same concept. The synthesis page is the value.
- **Don't lose the organizational logic** — explain WHY each framework organizes things the way it does, not just WHAT it covers.
- **Don't skip the mapping table** — it's the single most valuable artifact. Readers can scan it in 10 seconds.
- **Check for existing pages first** — a skeleton concept page may already exist in index.md (created by cron pipelines). Enrich it rather than creating from scratch.
