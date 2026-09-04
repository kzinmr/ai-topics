# Cross-Page Deep Analysis

> Pattern for synthesizing theoretical insights across multiple existing wiki pages, rather than enriching a single page from a raw article.

## When to Use

- User asks for "deeper analysis" of a topic that spans multiple wiki pages
- User wants to "reflect" a Q&A or discussion back into existing wiki pages
- Multiple related pages exist but lack unifying theoretical connections
- A Discord/Chat conversation produced cross-cutting insights

## Workflow

### Phase 1: Read All Related Pages

Read every page that the unifying framework touches. Don't guess — read the actual content.

```bash
# Find related pages via search
search_files(pattern="relevant-keyword", path="wiki/", output_mode="files_only")
# Read each one fully (not just headers)
read_file(path="wiki/concepts/page-a.md")
read_file(path="wiki/concepts/page-b.md")
read_file(path="wiki/concepts/page-c.md")
```

### Phase 2: Identify the Unifying Framework

Find the single conceptual lens that connects all pages. Examples:
- "LLM-as-Policy" unifying test-time scaling, on/off-policy RL, and DPO/GRPO convergence
- "Information-theoretic" lens connecting training signal density, policy efficiency, and auxiliary model elimination
- "Distribution shift" connecting exposure bias, hallucination, and abstention

The framework should explain **WHY** existing observations hold, not just restate them.

### Phase 3: Synthesize "Why" Sections

For each page, write a section that:
1. Connects to the unifying framework explicitly
2. Explains the structural reason behind existing observations
3. Uses concrete examples (R1-Zero, DPO formula, etc.)
4. Cross-links to related pages bidirectionally

**Quality bar**: The new section should make a reader say "I didn't realize the connection" — not just "this is a summary of the other page."

### Phase 4: Patch All Pages Simultaneously

Use `patch` (not `write_file`) for each page:

```python
# For each page:
1. Find the insertion point (between existing sections)
2. Write a self-contained section with cross-links
3. Update frontmatter `updated` date
4. Add any new tags (must exist in SCHEMA.md)
```

### Phase 5: Git Commit & Push

```bash
cd ~/ai-topics && git add wiki/concepts/*.md wiki/log.md
git commit -m 'wiki: deep analysis - <framework name> across N pages'
git pull --rebase && git push
```

**Pitfall**: If `git pull --rebase` fails with unstaged changes, use `git stash && git pull --rebase && git stash pop && git push`.

## Example: LLM-as-Policy Deep Analysis (2026-06-15)

**Input**: kzinmr's Discord Q&A on LLM-as-Policy paradigm
**Pages updated**: 3 (test-time-scaling, on-policy-vs-off-policy-rl, llm-as-policy)
**Sections added**:
1. "Thinking as Policy Execution: The Knowledge Creation Limit" → test-time-scaling.md
   - Key insight: thinking = policy execution, not cognitive planning → knowledge creation impossibility
2. "SFT vs RL: Structurally Non-Interchangeable Learning Paradigms" → on-policy-vs-off-policy-rl.md
   - Key insight: 6-dimension comparison table, R1-Zero as evidence
3. "Why This Convergence: Pre-Training as Implicit World Model" → llm-as-policy.md
   - Key insight: pre-training embeds environment dynamics → auxiliary models redundant

**Cross-links**: bidirectional between all 3 pages (test-time-scaling ↔ llm-as-policy ↔ on-policy-vs-off-policy-rl)

## Anti-Patterns

- ❌ Summarizing what other pages say ("as discussed in X...") instead of explaining WHY
- ❌ Adding the same section to all pages — each page gets its own perspective on the framework
- ❌ Forgetting bidirectional cross-links (page A links to B, but B doesn't link back to A)
- ❌ Using `write_file` on rich pages — always use `patch` (AGENTS.md rule: no overwrite of 40+ line pages)
- ❌ Skipping frontmatter `updated` date — must be updated on every change
- ❌ Adding tags not in SCHEMA.md — check first, add to SCHEMA.md if needed
