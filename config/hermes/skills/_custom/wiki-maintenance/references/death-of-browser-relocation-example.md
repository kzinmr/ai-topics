# Death of Browser Relocation Example

Real-world example of relocating `concepts/death-of-browser/_index.md` to `concepts/browser-agent/death-of-browser.md`.

## Context

- **Source**: `wiki/concepts/death-of-browser/_index.md` (212 lines, comprehensive page)
- **Target**: `wiki/concepts/browser-agent/death-of-browser.md`
- **Reason**: Create `browser-agent/` hierarchy for related concepts
- **Backlinks found**: 17 references across wiki

## Backlinks Updated (12 files)

1. `index.md` — Main index entry
2. `entities/webmcp.md` — WebMCP entity page
3. `entities/openai-cua.md` — OpenAI CUA entity page
4. `concepts/agentic-web.md` — Agentic Web concept
5. `concepts/_index.md` — Concepts index
6. `entities/perplexity-comet.md` — Perplexity Comet entity
7. `entities/manus.md` — Manus entity
8. `concepts/telegram-managed-bots.md` — Telegram Managed Bots concept
9. `entities/browser-use.md` — browser-use entity
10. `entities/browserbase.md` — Browserbase entity
11. `entities/anthropic-computer-use.md` — Anthropic Computer Use entity
12. `concepts/personal-superintelligence.md` — Personal Superintelligence concept

## Link Patterns Updated

### Absolute Paths
```markdown
# Before
- [[concepts/death-of-browser]] — Description
- [[concepts/death-of-browser/_index|Display Text]] — Description

# After
- [[concepts/browser-agent/death-of-browser]] — Description
- [[concepts/browser-agent/death-of-browser|Display Text]] — Description
```

### Relative Paths
```markdown
# Before (in concepts/ directory)
- [[death-of-browser]] — Description

# After
- [[browser-agent/death-of-browser]] — Description
```

## Execution Log

```bash
# 1. Search backlinks
search_files(pattern="death-of-browser", target="content", path="~/wiki")
# Result: 17 matches

# 2. Create directory and copy
mkdir -p ~/wiki/concepts/browser-agent
cp ~/wiki/concepts/death-of-browser/_index.md ~/wiki/concepts/browser-agent/death-of-browser.md

# 3. Remove original
rm ~/wiki/concepts/death-of-browser/_index.md
rmdir ~/wiki/concepts/death-of-browser/

# 4. Update backlinks (12 files)
# Each file patched individually

# 5. Update index.md
# Changed: [[concepts/death-of-browser/_index|...]] → [[concepts/browser-agent/death-of-browser|...]]

# 6. Update log.md
# Added relocation record at top

# 7. Commit
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: move death-of-browser to browser-agent/death-of-browser" && git push
```

## Result

- **Commit**: `8635c2c1`
- **Files changed**: 9
- **Insertions**: 31
- **Deletions**: 8
- **New hierarchy**: `concepts/browser-agent/` created for future related pages

## Lessons Learned

1. **_index.md conversion**: Directory with single `_index.md` can be converted to descriptive filename
2. **Relative link handling**: Must update both absolute and relative link formats
3. **Comprehensive search**: Search for page name in all contexts, not just wikilinks
4. **Log recording**: Always record relocation in log.md before committing