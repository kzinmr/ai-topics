# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-13] rotate | Log rotated (638 lines → log-2026.md)
- Previous log archived to `log-2026.md` for historical reference

## [2026-05-13] index | Added 6 orphan pages to index.md (entities: dex-horthy, merge-dev; concepts: agentic-rag, agentic-retrieval, claude-opus-4-7, death-of-browser). Fixed merge-dev alphabetical position. Updated section counts.

## [2026-05-13] lint | Frontmatter validation fixes
- Fixed 6 wiki pages with YAML frontmatter syntax errors:
  - `entities/ramp-labs.md` — related block invalid YAML (flow/block mix)
  - `entities/intuit-machine.md` — related block invalid YAML (flow/block mix)
  - `entities/anthropic.md` — related block invalid YAML (flow/block mix)
  - `concepts/agent-harness.md` — bulleted list inside [...] flow context
  - `concepts/societal-shadow.md` — missing closing --- frontmatter separator
  - `concepts/ai-coding-workflows.md` — corrupted frontmatter line (truncated source entry)

---

## [2026-05-13] index | Added 20 orphan concept pages to index.md

- Added 20 high-quality concept pages (not previously listed) to the Concepts section:
  - ai-infrastructure-engineering/distributed-training, ai-infrastructure-engineering/hardware-lottery, ai-infrastructure-engineering/pytorch-gpu-memory-profiling
  - ai-organization/ai-org-context-as-moat, ai-organization/ai-org-from-hierarchy-to-intelligence, ai-organization/ai-org-solo-founder-and-super-ic
  - ai-regulation-2026, ai-safety, ai-video-generation-2026, anthropic-managed-agents
  - bitsandbytes, chatgpt-images-2.0, chief-of-staff-agent-patterns, claude-mythos-preview, cmu-llms-methods-applications
- Updated header counts: Concepts 1253→1273, Total 1834→1854, Indexed 900→920
- No index corruption found (pipe_prefix: 0, line_number_prefix: 0, triple_brackets: 0, space_prefix: 0)
- Wiki-health: 980 orphans remain (not auto-applied — max 20 per run), 125 stale pages (31-34d), 5,405 unprocessed raw articles


## [2026-05-13] lint | Index audit — orphan entries identified
- 21 orphan index entries found (pointing to non-existent files):
  - `entities/_index` — index files don't need separate entries, remove from index
  - 10x `entities/omar-khattab/*` — these are subdirectory pages, not in main entities/ namespace
  - `concepts/agent-engineering-guide-2026|...` — link text syntax, should be cleaned
  - `concepts/ai-patterns-for-glam|...` — link text syntax, should be cleaned
  - `concepts/ambient-agency|...` — link text syntax, should be cleaned
  - `concepts/genai-handbook` — file doesn't exist
  - `concepts/glut-of-circuits` — file doesn't exist
  - `concepts/harness-commoditization` — file doesn't exist
  - `concepts/tau-bench` — file doesn't exist (concept page exists but may have been renamed)
  - `entities/theodoros-galanos|...` — link text syntax
  - `entities/vibevoice|→詳細` — link text syntax
  - `concepts/agent-team-swarm/managed-devins` — wrong namespace format
## [2026-05-13] lint | Wiki watchdog auto-fix

### ✅ Fixed: 11 duplicate index entries removed
- 4 entity skeletons removed (addy-osmani, elie-bakouch, florian-brand, gary-marcus)
- 4 more entity skeletons removed (jaya-gupta, tobi-lutke, parallel-web-systems, claris-filemaker)
- 1 will-brown double-entry block removed (2 adjacent lines), kept L589 entry
- 1 concepts/mcp and 1 comparisons/agent-harnesses stripped of skeleton entries
- Index header updated: Total pages: 1797 → 1834, Indexed entries: 853 → 894

### 🔍 Verified: All 21 "ghost entries" are false positives
- All 10 `entities/omar-khattab/*.md` files exist in subdirectory
- `entities/_index.md` exists and is properly indexed
- 3 pipe-syntax entries (`agent-engineering-guide-2026|...`, `ai-patterns-for-glam|...`, `ambient-agency|...`) use valid Obsidian display-text wikilinks pointing to existing files
- 4 `<missing>.md` entries (genai-handbook, glut-of-circuits, harness-commoditization, tau-bench) all exist in `concepts/`
- `agent-team-swarm/managed-devins.md` exists in subdirectory
- Root cause: health scanner used non-recursive directory listing

### ⚠️ Needs human review
- **933 pages not in index.md** — too large to batch-auto-apply (max 20 per policy)
- **810 pages missing frontmatter fields** (770+ missing `sources`) — needs batch fix strategy
- **Pipeline watchdog**: x-accounts-scan (26h stale) — normal for `*/2` schedule, next run 22:30 UTC today

### 📊 Post-fix index health
- Index entries: 894 (was 853 before dedup)
- Total pages: 1834 (577 entities, 1238 concepts, 16 comparisons, 1 queries, 2 events)
- Duplicates: 0 (was 11)
- Pipe corruption: 0 ✅ | Triple bracket: 0 ✅ | Line-number corruption: 0 ✅

## [2026-05-13] dreaming-wiki-ingest | entities/andrew-nesbitt.md enriched
### Context
- Dreaming pre-run failed (JSON parse error) — cross-pipeline check performed
- newsletter-ingest: 0 candidates | sitemap-monitor: 0 saved | blog-ingest: 1 take consumed
- All other recent raw articles (GNAP, InclusionAI Ring-2.6-1T, AEM, Firecracker, David Fowler, Prime Intellect renderers) already processed by other pipelines

### Changes
- `entities/andrew-nesbitt.md`:
  - ✅ Removed triplicated "The Mismeasure of Open Source" sections (removed 2 duplicate copies)
  - ✅ Added "Not a Security Issue: AI Scanner Policy Engineering" section documenting AI scanner self-triage via policy files
  - ✅ Updated `updated` date to 2026-05-13
  - ✅ Added source entry and raw article reference (nesbitt.io--2026-05-12-not-a-security-issue-html--c464f9c9)

### Files affected
- `~/wiki/entities/andrew-nesbitt.md` — updated (265 lines, up from 274 with duplicates)
- `~/wiki/log.md` — updated
- `~/wiki/index.md` — no change (entry already exists)
