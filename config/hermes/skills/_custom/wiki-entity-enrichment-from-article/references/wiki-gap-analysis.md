# Wiki Gap Analysis & Coverage Audit

When a user presents a list of questions, topics, or an article containing multiple claims to verify, use this systematic workflow to audit wiki coverage and fill gaps.

## Workflow

### 1. Extract Topics
Parse the source (article, interview questions, checklist) into individual topics/questions. Assign each a short identifier.

### 2. Search Existing Coverage
For each topic, run targeted grep searches:
```bash
cd /opt/data/wiki && grep -rli "keyword1\|keyword2\|keyword3" concepts/ entities/ 2>/dev/null | head -5
```
- Search for specific technical terms, proper nouns, algorithm names
- Check line counts of matching pages to gauge depth: `wc -l <file>`
- Read key sections of matching pages to verify actual coverage

### 3. Classify Coverage
Rate each topic:
- ✅ **Sufficient**: Dedicated page exists with adequate depth (50+ lines covering the topic)
- ⚠️ **Partial**: Topic is mentioned in existing pages but not deeply covered
- ❌ **Missing**: No relevant page exists, or only tangential mentions

### 4. Report to User
Present the coverage table before creating pages. This lets the user prioritize which gaps to fill.

### 5. Create Gap-Fill Pages
For ❌ and prioritized ⚠️ items:
- Create focused concept pages answering the specific question(s)
- Link to existing related pages via wikilinks
- Include source references (the original article/URL + any raw articles found)
- Keep pages under 120 lines — these are focused answers, not comprehensive surveys

### 6. Update Index & Commit
- Add entries to `wiki/index.md` in alphabetical position
- Update `wiki/log.md`
- Validate tags against SCHEMA.md before committing

## Pitfalls

- **Don't create pages for ✅ topics** — this duplicates existing knowledge
- **Don't write gap-fill pages in Japanese/CJK** — the pre-commit hook blocks non-raw wiki content with CJK characters
- **Validate all tags** against SCHEMA.md before committing. Common mistakes: `rl` (→ `reinforcement-learning`), `exploration` (no canonical — use `inference`), `interview` (no canonical — use `career`)
- **Check for existing pages first** — a grep that returns 0 results means no page exists; a grep that returns 20+ results means the topic is likely well-covered already

## Example: RL Interview Questions Audit (2026-06-12)

Source: 35 RL interview questions from @sheriyuo's X Article.
Result: 26/35 (74%) sufficient, 6/35 (17%) partial, 3/35 (9%) missing.
Created 5 gap-fill pages: batch-invariance, rl-scaling-boundaries, grpo-memory-modeling, moe-train-inference-mismatch, rl-exploration-test-time-vs-training.
