# Wiki Language CJK Content Blocker

The pre-commit hook in `ai-topics` blocks commits containing Japanese/CJK characters in non-`raw/` wiki pages. The detection regex is:

```
[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]
```

This covers:
- Hiragana (3040–309F)
- Katakana (30A0–30FF)  
- CJK Unified Ideographs (4E00–9FFF) — includes Chinese characters, Japanese kanji
- Fullwidth forms (FF00–FFEF)

## When This Fires

### Names (most common)
Including a person's name in Chinese/Japanese characters in entity pages:

```markdown
# ❌ BLOCKED
Jina AI was founded by **Han Xiao** (肖涵)...

# ✅ OK
Jina AI was founded by **Han Xiao**...
```

### Concept page aliases
Japanese aliases in frontmatter trigger the block:

```yaml
# ❌ BLOCKED
aliases:
  - llm-as-policy
  - 方策としてのLLM

# ✅ OK
aliases:
  - llm-as-policy
  - policy-language-model
```

### Concept page body text
Even a single Japanese word in a blockquote or description blocks the commit:

```markdown
# ❌ BLOCKED
> **LLM-as-Policy** is the paradigm of treating a language model as a reinforcement learning policy (方策 $\pi_\theta$)...

# ✅ OK
> **LLM-as-Policy** is the paradigm of treating a language model as a reinforcement learning policy ($\pi_\theta$)...
```

### Index.md entry descriptions
Japanese text in index.md entries also blocks:

```markdown
# ❌ BLOCKED
- [[concepts/post-training/llm-as-policy]] — LLM-as-Policy Q&A: LLMをRL方策として見るパラダイムとSFT/RLの関係性...

# ✅ OK
- [[concepts/post-training/llm-as-policy]] — LLM-as-Policy Q&A: Paradigm treating LLMs as RL policies with SFT/RL relationship analysis...
```

## Ingesting Japanese Source Material

When ingesting a Japanese-language source (Q&A, newsletter, X post, blog):

1. **Raw article** (`wiki/raw/articles/`): Can remain Japanese — the `raw/` directory is exempt from the language check
2. **Concept/entity pages** (`wiki/concepts/`, `wiki/entities/`): Must be fully English
3. **Aliases**: Must be English (romanized names, English descriptions)
4. **Index.md entries**: Must be English descriptions
5. **Log.md entries**: Already has Japanese content from before, but new entries should use English to avoid ambiguity

**Workflow**: Write concept pages in English from the start. Don't copy Japanese terms into English wiki pages — translate/romanize everything.

### ⚠️ Japanese User Request Trap

When the user writes in Japanese and says "取り込んで" (ingest), "記事を処理して" (process article), or similar, the agent's natural tendency is to write the concept page **in Japanese** to match the user's language. **This will be blocked by pre-commit.**

**Rule**: Even when the user communicates in Japanese, all wiki concept/entity pages must be written in English. The user's language preference applies to chat responses, not to wiki content.

**Pattern**:
1. User: `以下の記事をconcepts/openai/以下に取り込んで` (in Japanese)
2. Agent writes concept page in Japanese → pre-commit blocks → rewrite in English → recommit
3. Better: Write in English from the start, respond to user in Japanese

This is distinct from ingesting a Japanese-language source article (where the raw stays Japanese but the concept page is English). Here, even the source article may be English, but the user's request language triggers a Japanese page.

## Error Output

```
❌ BLOCKED: Japanese content introduced to previously clean files:
   NEW FILE with Japanese content: wiki/entities/jina-ai.md

   Wiki language policy: All non-raw/ wiki content must be in English.
   To skip this check: git commit --no-verify
```

**Note**: The check is diff-based — it only blocks **new** Japanese content. Files that already contain Japanese (from before the hook was added) won't trigger on existing content, only on new additions.

## Prevention

1. **Before writing entity/concept pages for CJK individuals or companies**, strip all CJK characters from names, citations, and descriptions.
2. **Romanize all names**: Use the person's preferred romanization (Han Xiao, not 肖涵).
3. **Check quoted text from sources**: If a source quote contains CJK characters, either translate or omit the characters.
4. **When ingesting Japanese Q&A/documents**: Write concept pages in English from scratch, not translated line-by-line.

## Historical Incidents

- **2026-05-28**: Jina AI entity page blocked — contained `肖涵` (Han Xiao's name in Chinese). Fixed by removing the parenthetical Chinese characters.
- **2026-06-15**: LLM-as-Policy concept page blocked twice — (1) Japanese alias `方策としてのLLM` in frontmatter, (2) Japanese word `方策` in blockquote description. Index.md entry also had Japanese (`LLMをRL方策として見るパラダイムとSFT/RLの関係性`). Fixed by removing alias, replacing Japanese term with English, and rewriting index entry.
- **2026-06-17**: OpenAI reflections concept page blocked — user requested ingestion in Japanese ("取り込んで"), agent wrote entire concept page in Japanese. Had to rewrite fully in English and recommit. Lesson: user's request language ≠ wiki content language.
- **2026-06-29**: AWS Lambda MicroVMs concept page blocked — user wrote "この機能に関してwikiに取り込んで", agent wrote concept page body AND cross-reference additions (AgentCore entity page related-pages entry) in Japanese. Two files blocked. Fixed by full English rewrite of concept page + patching AgentCore. Repeat of the 2026-06-17 pattern — the Japanese User Request Trap remains the #1 pre-commit failure mode.
- **2026-07-21**: Cursor agent swarm article — user wrote "以下記事を取り込んで", agent wrote entire `cursor-agent-swarm-architecture.md` concept page AND cross-reference additions to `agent-swarms.md` in Japanese. Two files blocked. Also hit tag taxonomy violation (`agent-swarms` not in SCHEMA.md). Required full English rewrite of both files + adding tag to SCHEMA.md. Root cause: a contradictory reference file (`pre-commit-language-policy-pitfall.md`) incorrectly suggested bilingual pages were acceptable. That file has been deleted.
