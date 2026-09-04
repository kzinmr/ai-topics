# Wiki Gap Analysis & Batch Concept Page Creation

Systematically audit wiki knowledge coverage against a checklist (interview questions, curriculum topics, comparison criteria) and batch-create pages to fill gaps.

## Trigger

User asks to "review/verify whether wiki can answer X" or "fill gaps in coverage for Y" or provides a structured list of questions/topics and says to create pages.

## Workflow

### Phase 1: Coverage Audit

1. **Extract the question/topic list** from the source document
2. **For each topic**, search wiki for matching pages:
   ```bash
   cd /opt/data/wiki && grep -rli "<keyword1>\|<keyword2>" concepts/ entities/ 2>/dev/null | head -5
   ```
3. **Rate each topic**: ✅ sufficient (dedicated page exists), ⚠️ partial (mentioned but shallow), ❌ missing (no page or only passing mention)
4. **Check page depth** for ⚠️ items:
   ```bash
   wc -l concepts/<page>.md  # <40 lines = stub, 40-100 = moderate, 100+ = substantial
   grep -i "<specific-topic>" concepts/<page>.md  # check if the specific subtopic is covered
   ```
5. **Present audit results** as a table with columns: Question | Wiki Pages | Rating | Gap

### Phase 2: Page Creation

For each ❌ or ⚠️ gap:

1. **Check for raw sources**:
   ```bash
   grep -rli "<topic>" raw/articles/ raw/papers/ 2>/dev/null | head -5
   ```
2. **Research if needed** — web search for authoritative sources, arXiv papers
3. **Create the concept page** with:
   - Proper frontmatter (title, type, tags from SCHEMA.md, sources with URLs)
   - Technical depth appropriate to the question (formulas, tables, specific mechanisms)
   - At least 2 wikilinks to existing pages
   - See Also section linking to related raw papers
4. **Batch creation**: Use `delegate_task` with parallel subagents (up to 3) for independent pages

### Phase 3: Integration

1. **Add all entries to index.md** — alphabetically positioned in the Concepts section
   - ⚠️ **PITFALL**: Subagents may NOT update index.md even when instructed. Always verify after delegation:
     ```bash
     grep -n "<new-page-slug>" wiki/index.md
     ```
   - Add missing entries manually with `patch`
2. **Update log.md** with a single entry listing all created pages
3. **Commit and push**:
   ```bash
   cd ~/ai-topics && git -c core.quotepath=false add wiki/ && git commit -m "wiki: ..." && git push
   ```

## Pitfalls

- **Subagent index.md unreliability**: When delegating batch page creation to subagents, some will update index.md and some won't. ALWAYS verify with `grep` after all subagents complete. Add missing entries manually.
- **Tag violations block entire commit**: If ANY staged file has invalid tags, the pre-commit hook blocks ALL files. Check tags before committing. Common failures: `rl` → `reinforcement-learning`, `interview` → `career`, `exploration` → `inference`, `load-balancing` → `distributed-training`.
- **Japanese content blocked**: All non-raw/ wiki content must be English. Even if source material is Japanese, translate before writing.
- **Duplicate pages**: Always search for existing pages before creating. A topic might be covered under a different name (e.g., `rlhf-dpo-orpo-kto-preference-optimization` vs `dpo`).
- **Evidence quality tracking**: When creating pages from general knowledge rather than specific sources, note in the page or report to user which claims lack paper-level evidence. This helps prioritize future enrichment.

## Example: RL Interview Questions 2026 Gap Fill

- Source: 35-question RL interview cheat sheet from @sheriyuo
- Audit: 26/35 covered, 6 partial, 3 missing
- Created 5 pages: batch-invariance-deterministic-training, rl-scaling-boundaries, grpo-memory-modeling, moe-train-inference-mismatch, rl-exploration-test-time-vs-training
- Delegated 3 pages to parallel subagents (first batch), then 2 more (second batch)
- First subagent updated index.md; other 4 did not → had to add 4 entries manually
- 3 tag violations fixed before commit succeeded
