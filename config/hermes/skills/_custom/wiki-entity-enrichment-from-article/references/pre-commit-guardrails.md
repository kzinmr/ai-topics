# Pre-Commit Guardrails for Wiki Page Creation

These are pitfalls encountered during actual wiki ingestion sessions.
The pre-commit hook enforces them — fix BEFORE committing to avoid iterative rebase pain.

## 1. Tag Taxonomy Validation

**Symptom**: `TAG TAXONOMY VIOLATIONS — COMMIT BLOCKED` listing 15+ tags as "NOT IN SCHEMA.md TAXONOMY"

**Root cause**: New tags used on entity/concept pages were not added to `wiki/SCHEMA.md` first.

**Fix workflow**:
1. When creating pages with novel tags, add them to the appropriate category in `wiki/SCHEMA.md` **before** the first commit attempt.
2. Categorize each new tag:
   - Company/org names → People/Orgs (e.g., `sakana-ai`, `japan`, `tokyo`)
   - Techniques → Techniques (e.g., `score-matching`, `block-wise-training`, `model-merging`, `residual-networks`, `deep-learning`)
   - Products/tools → Products (e.g., `optuna`, `kaggle`)
   - Broad concepts → Domain Concepts (e.g., `nature-inspired`, `collective-intelligence`, `competitive-programming`)
   - Model categories → Models (e.g., `foundation-models`)
3. Re-run `git add wiki/ && git commit` — the hook validates all tags against the updated SCHEMA.md.

**Prevention**: When writing entity/concept page frontmatter, cross-reference every tag against SCHEMA.md. If a tag doesn't exist, add it to SCHEMA.md in the same edit batch.

## 2. English-Only Wiki Policy (Language Enforcement)

**Symptom**: `BLOCKED: Japanese content introduced to previously clean files` listing new files with CJK characters.

**Root cause**: Entity pages contained Japanese characters — even proper nouns like names (秋葉 拓哉) and kanji explanations (魚).

**Fix workflow**:
1. Find offending lines: `python3 -c "import re; jp=re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]'); ..."`
2. Replace CJK characters with romaji/English equivalents:
   - Names: "Takuya Akiba" not "Takuya Akiba (秋葉 拓哉)"
   - Kanji explanations: "sakana means fish" not "sakana (魚) means fish"
3. The meaning is fully preserved — CJK is decorative for proper nouns in an English wiki.

**Prevention**: When writing entity pages, never include CJK characters even as parenthetical asides. Use English/romaji exclusively.

## 3. Subagent Delegation for Entity Pages

When delegating entity page creation to subagents (via `delegate_task`), explicitly include these instructions in the context:

```
### Wiki requirements (include in ALL subagent entity page tasks):
- ALL content must be English-only — NO CJK characters, even for proper nouns. Use romaji.
- All tags must be from the SCHEMA.md taxonomy. If a needed tag is missing, flag it — do NOT use unregistered tags.
- Update wiki/index.md with the new page entry under the correct section.
- Update wiki/log.md with a creation log entry.
- Files go to /opt/data/ai-topics/wiki/entities/<slug>.md or /opt/data/ai-topics/wiki/concepts/<slug>.md
```

Subagents don't know about the pre-commit hooks and will produce pages that fail validation. These instructions prevent that.

## 4. Commit Order Matters

The correct commit sequence for wiki page creation:
1. Write all new pages (raw, entity, concept)
2. **Add new tags to SCHEMA.md** (before first commit)
3. Remove any CJK characters from wiki pages
4. Update index.md and log.md
5. `git add wiki/ && git commit`
6. If hook blocks, fix the specific issue and retry — don't use `--no-verify`
