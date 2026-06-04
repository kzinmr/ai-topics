# JP→EN Translation Batch Workflow

When a bilingual wiki (Japanese + English) needs systematic Japanese-to-English translation,
use this batch workflow to process N files at a time.

## When to Run

- As a cron job when the wiki has a measured JP-content backlog (e.g., 350+ files, ~280K chars)
- After any ingest pipeline that adds Japanese-language content
- Before a wiki restructuring that would benefit from a monolingual foundation

## Workflow

### 1. Scan and rank JP files

```python
import re, os
jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
wiki_root = '/opt/data/ai-topics/wiki'
remaining = []
for root, dirs, files in os.walk(wiki_root):
    if 'raw/' in root: continue           # Skip raw/ directory
    for f in files:
        if f.endswith('.md') and not f.startswith('log'):
            fp = os.path.join(root, f)
            with open(fp) as fh: content = fh.read()
            lines = content.split('\n')
            body_start = 0; fm_count = 0
            for i, line in enumerate(lines):
                if line.strip() == '---':
                    fm_count += 1
                    if fm_count == 2: body_start = i + 1; break
            if fm_count < 2: body_start = 0
            body = '\n'.join(lines[body_start:])
            body_jp = len(jp.findall(body))
            if body_jp > 0:
                rel_path = os.path.relpath(fp, wiki_root)
                remaining.append((rel_path, body_jp, fp))
remaining.sort(key=lambda x: -x[1])
```

**Key filters:**
- Exclude `raw/` subdirectory (immutable sources not worth translating)
- Exclude ALL log files: `not f.startswith('log')` — the wiki may have rotated logs
  like `log-2026-05-previous.md` and `log-2026-05-13.md` with substantial JP content
  (up to 9K chars each). These are action logs, not wiki content.
- Only count JP characters in the body (after YAML frontmatter `---` end marker)

### 2. Select top N files (recommended: 8 per batch)

The top 8 files typically account for ~30,000 JP chars in a 350+ file wiki
with ~280,000 total JP chars (roughly 10% of the total backlog per batch).

#### Tail-End Cleanup Pattern (<200 JP chars total remaining)

When the wiki is nearly clean (total JP chars <200 across ALL files, each file <15 JP chars),
**skip the standard batch flow** entirely. The 8-file batch approach is designed for 30K-char
backlogs and is wasteful at this stage. Instead:

1. **Scan ALL files** with a single `os.walk()` pass to find every file with JP chars
2. **Categorize each file** — is the JP actually Japanese text, or is it:
   - Chinese proper names (person/company/institution names in CJK) → exclude, mark as "intentionally preserved"
   - Raw article path references (`raw/articles/`) → exclude per policy
   - Chinese citation text (tweet titles, book titles) → exclude (preserve the citation as-is)
   - Fullwidth punctuation (`（）` `：`) → fix to ASCII
   - Actual Japanese text (hiragana/katakana phrases) → translate
3. **Build a single per-file dict** containing 1-3 replacement entries per file
4. **Apply ALL replacements in one `execute_code` block** — no tmp scripts, no multi-pass
5. **Verify ALL files at once** — run the JP scan on every translated file
6. **Report final state**: "X Japanese files fully cleaned, Y Chinese-name-only files intentionally preserved"

**Rationale**: Each file in this stage has only 2-10 JP chars. The `str.replace()` approach
with a single dict per file is the most efficient pattern — no multi-pass cleanup needed,
the replacements are simple enough that silent non-matches are rare. A single `execute_code`
call with 10-15 per-file dict entries completes faster than the standard 8-file batch.

**Confirmed patterns from production (2026-05-27 final cleanup):**
- 14 of 27 remaining files were Chinese-proper-name-only (月之暗面, 智谱AI, 小红书, 姚顺雨, etc.) → excluded
- 1 file had JP chars only in a raw article path reference → excluded per policy
- 13 files needed actual fixes (fullwidth parens, stray hiragana, embedded JP text) → all 13
  achieved 0 residual JP in a single `execute_code` pass with 2-4 replacement entries per file
- Final state: 62 "JP" chars remaining, all in Chinese proper names (intentionally preserved)

### 3. Translation strategy: direct `write_file` per file

**DO NOT use `delegate_task`** for large file translations. The subagent receives the
full file content in context, attempts to read + translate + write, and frequently
**times out after 600s** when each file is 200+ lines with 3K-5K JP chars to translate.
(A timed-out subagent leaves zero files written.)

**DO use direct `write_file` calls** with the full translated content. This is
token-expensive per file (you provide the full original + full translation) but
reliable — each call completes in <1s.

**Best pattern for fully-JP file batches (3-4 files):** Write a single Python
script to `/tmp/translate_batch.py` via `write_file`, then execute with
`python3 /tmp/translate_batch.py`. The script reads each file, splits frontmatter
from body, translates the body, bumps `updated` date, and writes back. This
avoids 4 sequential `write_file` calls (2 token-expensive turns → 1 cheap
terminal call) while keeping translations fully under your control. Each file's
translation is a self-contained function in the script.

**Best pattern for mixed JP/EN file batches (4-5 files):** Write a single
per-file `str.replace()` dict script to `/tmp/translate_batch.py`. The script
reads each file, applies its replacement dict to the body, bumps `updated`,
writes back, and reports remaining JP chars per file. Use the stripped-string
fallback (see Principles) to catch whitespace-mismatched replacements silently.

**⚠️ `write_file` backslash-escape corruption** — When writing the translation
script to `/tmp/translate_batch.py` via `write_file`, the tool can corrupt
backslash-escaped characters in Python string literals (like `\\n` inside replacement
strings or `\\` in escape sequences). The result is a syntax error like
`SyntaxError: unterminated string literal` on the line where the corruption occurs.
The `patch` tool exacerbates this by adding extra escaping levels when used to fix
individual lines. **Prevention strategies:**
1. **Use `execute_code` directly** (not a file-based script) with per-file helper
   functions and `with open(path) as f:` for file I/O. This bypasses write_file's
   content encoding entirely.
2. **Use `r"""..."""` raw triple-quoted strings** within `execute_code` for
   full-body rewrites of fully-JP files — raw strings handle `\\n` and quote
   characters without escaping issues.
3. **If you must write to /tmp:** verify the script can be parsed with
   `python3 -c "import ast; ast.parse(open('/tmp/translate_batch.py').read()); print('OK')"`
   before executing. If it fails, switch to `execute_code` approach instead of
   attempting `patch`-based fixes on the corrupted file.
4. **Per-file helper pattern (`save_and_report`):** Instead of one monolithic
   script, write per-file `save_and_report()` helpers in `execute_code` where
   each replacement is independently verified and reported:

   ```python
   def save_and_report(fp, old_text, new_text, label):
       with open(fp) as f: content = f.read()
       if old_text in content:
           content = content.replace(old_text, new_text)
           with open(fp, 'w') as f: f.write(content)
           old_jp = len(jp_pat.findall(old_text))
           print(f"  [{label}] Replaced: {old_text.strip()[:40]}... (-{old_jp} JP)")
           return old_jp
       else:
           print(f"  [{label}] SKIP: {old_text.strip()[:40]}...")
           return 0
   ```

   Advantages of this approach:
   - **Each replacement is independently verifiable** — a skip warns you immediately
   - **No script-level syntax error kills the batch** — each replacement call stands alone
   - **Per-replacement JP char tracking** — you see exactly which replacements succeeded
   - **Works with both double and single quotes** in replacement values — no need to
     escape around Python string delimiters; just use a matching quote style per call
   - **Can interleave fully-JP rewrites with mixed-JP replacements** in the same
     `execute_code` block, avoiding the need for separate file-based scripts
   - **Proven in production**: the 2026-05-27 batch (8 files, 3,468 JP chars)
     used this pattern after the `/tmp/translate_batch.py` approach failed due to
     `write_file` backslash corruption. All 8 files achieved 0 residual JP on
     the second pass.

**⚠️ Pre-check every replacement before applying — fail loud, continue silent:**
Add an `if old in body:` guard before every `str.replace()` call. When text
doesn't match, print a warning (first 40 chars of the old string) rather than
crashing. This catches invisible mismatches (whitespace, Unicode variants) and
tells you which entries need investigation — without killing the batch. The
result is a clear list of "N replacements succeeded, M failed" at the end,
letting you fix only the failed entries in a targeted follow-up pass rather than
re-running the entire batch.

**⚠️ Code blocks need explicit entries in the str.replace() dict — they are NOT
covered by surrounding paragraph replacements.** Japanese comments inside
triple-backtick-fenced code blocks (like `# この関数は...` or `// 設定を読み込む`)
and Japanese labels in ASCII-art diagrams will NOT be matched by a paragraph-level
replacement that targets the section around the code block. Before writing the
batch script, scan each file for fenced code blocks containing JP chars and add
dedicated `str.replace()` entries for each one. If a file has 5+ code blocks
with JP content, consider splitting that file into a fully-JP batch (full body
rewrite) instead, since the per-string approach becomes fragile at that density.

**Processing order**: simplest files first (fewest JP chars, most English already),
most complex last (index files, comprehensive guides). This builds momentum and
catches edge cases early.

### 4. Translate body only, preserve everything else

For each file:
- **YAML frontmatter handling** — translate human-readable fields, preserve structural ones:
  - **TRANSLATE `title` and `description`** — these contain human-readable text that should
    match the wiki's language. If a `title:` or `description:` line has JP chars (hiragana/katakana,
    not just CJK proper nouns), translate them just like body text. A JP `title` like
    `"Inference — LLM推論エンジン比較"` should become `"Inference — LLM Inference Engine Comparison"`.
  - **PRESERVE `aliases`** — these are search/lookup terms. Japanese aliases (e.g.,
    `"文脈ロックイン"`) are intentionally kept for searchability.
  - **PRESERVE `source_message`** — these are original quotes from Slack/Discord/etc.
    They are immutable source material and should remain in the original language.
  - **PRESERVE `tags`, `created`, `updated`, `sources`, `status`** — these are structural
    metadata fields, not narrative text.
  - **Bump `updated` date** to today after translation.
- **Bump `updated` date** to today in frontmatter
- **Preserve ALL** markdown: headers (`##`), lists (`-`), tables, code blocks (`` ``` ``)
- **Preserve ALL** wikilinks (`[[concepts/something]]`, `[[entities/someone]]`)
- **Preserve ALL** URLs and source citations
- **Keep technical terms in English**: LLM, Agent, RAG, MCP, GPU, VRAM, model names,
  company names, product names
- **Only translate narrative/descriptive text** in the body

### 4a. Mixed-content files: EN skeleton with JP sections

Some files are **mostly English with scattered Japanese paragraphs/sentences**, not fully
Japanese. These require a section-by-section approach rather than wholesale translation:

1. **Read the full file** first to identify which sections are in Japanese and which are
   already English. The JP scan only tells you the total char count, not the distribution.
   **⚠️ `read_file` truncates at 100 lines** — for files over 100 lines (common for
   comprehensive concepts like `dgx-spark-nim.md` at 301 lines), you must explicitly read
   with `offset=101` to see the rest. Even better, use Python's `open().read()` in
   `execute_code` to get the full file without pagination. A partial read means missed JP
   sections in the latter ~200 lines.
2. **For each Japanese section**: translate that section header + body to English, cross-
   referencing surrounding English sections for consistent terminology and tone.
3. **Keep pre-existing English sections entirely intact** — do not rephrase or "improve"
   them during translation. Only change what was in Japanese.
4. **Frontmatter**: bump `updated`, translate `title` and `description` if they contain JP
   (hiragana/katakana), leave `aliases` (search terms), `source_message` (original quotes),
   and structural fields (`tags`, `sources`) unchanged.

**Real-world example — `entities/deepseek.md` (290 lines, 20K+ bytes):**
This file was ~80% English with 2,215 JP chars in specific sections (Strategy, KV Cache
Economics, Hardware Enablement, Equity-Collaboration Model, Contrarian Nature, Earlier
Models descriptions). Approach:
- Read the file completely to map which sections were JP vs EN
- Strategy section: translate the Core Thesis, KV Cache, Memory-Compute, Hardware
  Enablement, Equity-Collaboration, Long Game, and Contrarian Nature subsections
- Earlier Models descriptions: translate the Japanese text in each model's prose
- Keep all existing English tables, comparison benchmarks, NIST evaluation, and
  Open Questions intact
- Write the full file back with only JP sections replaced

**Why individual `write_file` calls work better than `execute_code` for these:**
For a mixed-content file like `entities/deepseek.md`, the translated content is a
carefully reasoned blend of new English text + preserved existing English content.
Attempting to encode this as Python string operations inside `execute_code` would be
extremely fragile (nested quotes, escaped chars, syntax errors from multi-line
f-strings). Each `write_file` call is independent and completes in <1s.

### 4b. Fully-Japanese files vs mixed-content: the difference

| Dimension | Fully-JP file | Scattered-JP file | Mixed-content file |
|-----------|---------------|-------------------|-------------------|
| **Clarity of what to translate** | Entire body | Many scattered locations: headers, table cells, inline descriptions, bullet points | Only a few coherent JP paragraphs, most content already EN |
| **Decision rule** | Always full rewrite | **Full rewrite preferred over str.replace()** — 40+ replacement entries with each having a chance to silently non-match adds up fast | str.replace() with per-string dict works well for ≤10 replacement entries |
| **Risk** | Missing a narrative paragraph | Silent str.replace() non-matches across scattered locations — no warning, just residual JP in post-verification | Accidentally duplicating or rephrasing existing EN |
| **Read required** | Scan frontmatter → translate body | Full file read to map ALL JP locations (headers, tables, bullets, inline) | Full file read to map EN/JP boundaries |
| **Write pattern** | Full body rewrite | Full body rewrite (even at 30-70% JP) — cleaner than 50+ str.replace() entries | Selective section replacement within full rewrite |
| **Example** | `concepts/waluigi-effect.md` (all-JP body) | `concepts/harness-engineering/system-architecture/_index.md` (scattered JP in headers, table rows, inline descriptions); `concepts/harness-engineering/agentic-workflows/rodney.md` (scattered JP in headers, command tables, inline text) | `entities/deepseek.md` (mostly EN with a few JP strategy sections) |

### 5. Add log entry via `execute_code` (not `patch`)

Use the header/chrono splitting pattern (NOT `f.write(new_entry + content)` which
buries the header). **After writing, insert a `\n---\n\n` separator between your
new entry and the existing chrono entries** so the boundary is visually clear
in the log file.

**Recommended log entry format — use `### Files Translated` and `### Stats`
subsections with per-file char counts:**

```python
new_entry = [
    "## [YYYY-MM-DD] translate | JP->EN batch -- N files (X chars)\n",
    "\n",
    "### Files Translated\n",
    "- [[concepts/foo.md]] — N chars -> 0\n",
    "- [[entities/bar.md]] — N chars -> 0\n",
    "\n",
    "### Stats\n",
    "- Total JP chars removed: X\n",
    "- Remaining JP content files: N\n",
    "- Remaining JP chars: N\n",
    "\n",
]
```

Then insert between header block and chrono entries:

```python
header_block = lines[:chrono_start]
chrono_entries = lines[chrono_start:]
lines = header_block + new_entry + ["\n", "---\n", "\n"] + chrono_entries
```

### 6. Commit and push

```bash
cd /opt/data/ai-topics
git add wiki/<all-translated-files> wiki/log.md
git commit -m "wiki: JP->EN batch -- N files (X chars)"
git push
```

The pre-commit tag validator should pass since you're not adding new tags —
only translating text.

### 7. Verify and report (post-translation check)

After writing all translated files, run a verification scan to confirm all JP is gone:

```python
import re, os
jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
wiki_root = '/opt/data/ai-topics/wiki'
translated_files = [...]  # list of paths you translated

total_removed = 0
remaining_jp = 0
for f in translated_files:
    fp = os.path.join(wiki_root, f)
    with open(fp) as fh: content = fh.read()
    lines = content.split('\n')
    body_start = 0; fm_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2: body_start = i + 1; break
    if fm_count < 2: body_start = 0
    body = '\n'.join(lines[body_start:])
    jp_in_body = len(jp.findall(body))
    if jp_in_body > 0:
        print(f"WARNING {jp_in_body} JP chars REMAINING in {f}")
        remaining_jp += jp_in_body
    else:
        total_removed += 1
print(f"{total_removed}/N files fully clean")
```

Also run a full wiki scan to track remaining backlog:

```python
remaining = []
for root, dirs, files in os.walk(wiki_root):
    if 'raw/' in root: continue
    for f in files:
        if f.endswith('.md'):
            fp = os.path.join(root, f)
            # ... (same scan code as step 1)
remaining.sort(key=lambda x: -x[1])
print(f"Remaining JP files: {len(remaining)}")
print(f"Remaining JP chars: {sum(j for _, j, _ in remaining)}")
print("Top 10 remaining:", [(p, j) for p, j, _ in remaining[:10]])
```

**One-shot scan → fix → verify cycle in `execute_code` (recommended over per-file `patch` calls):**
After Pass 1, run a single `execute_code` block that:
1. **Scans** all translated files for residual JP and prints exact lines with line numbers
2. **Fixes** with targeted `str.replace()` across all files in one pass (table headers, section headers, straggler descriptions)
3. **Re-verifies** all files are 0 residual before finishing
4. **Prints** final summary per file

This avoids 8-16 individual `patch` calls (each needing its own turn) and keeps the cleanup atomic. If the `execute_code` block grows beyond what's manageable (too many replacement entries), split into 2 sequential `execute_code` calls targeting different filesets rather than switching to per-file `patch` calls.

**Post-translation cleanup — multi-pass strategy**

Whether a single pass achieves 100% cleanup depends on **file structure**, not
file size or total JP chars. **Expect 2-3 passes as the norm** for mixed-content
files with scattered JP in table cells, architecture diagrams, and section headers.
Write each pass as a separate Python script (`translate_batch.py`, `translate_pass2.py`,
`translate_pass3.py`) and clean them up after committing with `rm /tmp/translate*.py`.
This is not a failure — incremental discovery of remaining JP across passes is the
expected workflow for mixed-content files.

- **Fully-JP files with clear section structure** (tables, wikilinks, headers, coherent
  narrative paragraphs) → **single-pass cleanup is the norm**, not an exception. Translate
  the entire body as a full English rewrite with `write_file`. Verified in production:
  files like `death-of-browser/_index.md`, `agent-skills-overview.md`, and `codex-prompting.md`
  all achieved 0 stragglers on first pass across 8-file batches (12K+ chars).
- **Mixed-content files where JP is in coherent paragraphs** → also single-pass capable
  when you carefully map EN/JP boundaries and do a full rewrite that preserves English
  sections while translating Japanese ones. Example: `dark-factory-software-factory.md`
  achieved 0 stragglers on first pass via this approach.
- **Files with scattered JP in table cells, section headers, or code blocks** → **these
  need multi-pass cleanup**. The JP is not in coherent paragraphs but distributed across
  many individual cells/lines, making it easy to miss individual occurrences.

**Decision rule:** After Pass 1, run the verification scan. If <5 JP chars remain across
all 8 files, switch directly to Pass 3 (targeted patch). If 5-50 chars, run Pass 2
(batch header/table normalization). If 50+ chars remain, the JP is likely in narrative
paragraphs you missed — re-read the file rather than relying on regex replacement.

**Common straggler patterns (in order of frequency):**

1. **Japanese table column headers** — `| モデル | パラメータ |` in model comparison tables.
   These are table column labels that look like data but contain JP chars. They're easy to
   miss because they're surrounded by ASCII markdown table syntax (`|`, `---`, `|`).
2. **Japanese section headers** — `## 関連項目`, `## 関連リソース`, `## 関連コンセプト`,
   `## 参考文献`, `## 関連リンク`. These recur across many wiki files and can be batched
   in a single pass with a `str.replace()` dict. **BUT also watch for file-specific
   headers** — `## 核心哲学`, `## 3つのコア原則`, `## 階層構造`, `## 基本概念` — these
   won't match a common-header dict and need explicit entries in each file's translation dict.
3. **Japanese table row labels** — Cells like `スコアラ` (Scorer) or `プーリング` (Pooling)
   inside markdown tables. These aren't narrative text and are easily missed when scanning
   for paragraph-style JP content.
- **Fullwidth punctuation masquerading as JP chars** — After translation, remaining "JP chars" are
  sometimes CJK punctuation rather than Japanese language content. Fullwidth colon `：` (U+FF1A) is the
  most common — it appears in log entries, table headers, inline descriptions, and is visually nearly
  identical to the ASCII `:` but counted as a "JP char" by the `\uFF00-\uFFEF` range. Also check for
  fullwidth semicolons `；` (U+FF1B) and fullwidth commas `，` (U+FF0C). **Fix**: After the main translation
  pass, always run a cleanup step: `content.replace('\uff1a', ':').replace('\uff1b', ';').replace('\uff0c', ',')`.
  This alone resolved 6 remaining "JP chars" in a 1732-line log file that was otherwise clean.
- **JP chars inside ASCII `()` in architecture diagrams** — ASCII-art architecture diagrams
   often have JP labels inside regular parentheses: `Lead Agent (計画・戦略)`, 
   `Subagent 1 (独立検索)`, `CitationAgent (引用検証)`. These look like they use full-width
   `（）` but actually use regular ASCII `()`. The replacements must target **both variants**:
   - `（計画・戦略）` → ` (planning & strategy)`  (full-width parens)
   - `(計画・戦略)` → ` (planning & strategy)`   (regular parens — easy to forget)
   The architecture diagram is typically a single code-fenced block where all lines have
   regular `()`. **Pre-check**: before writing the dict, check whether the architecture lines
   use `（）` or `()` by reading one line with `repr()`. (Confirmed in the 2026-05-26 batch:
   multi-agent-research-system.md had all architectural labels in regular `()`, causing an
   initial pass with full-width `（）` replacements to silently fail on those lines.)
- **JP chars inside otherwise-English code blocks or technical parentheticals** —  
  Full-width parentheses like `（DeBERTa v2）` or stray kanji in code comments.
- **Bold vs non-bold table header variants** — The same table column header may appear
  with and without bold markers (`| **分類** |` vs `| 分類 |`) in different parts of the
  same file. If your replacement dict only has `**分類**`, the non-bold version silently
  survives. **Fix**: explicitly include both variants in the per-file dict. After Pass 1,
  when residual JP chars remain in table cells, check whether the missing entry lacks `**`
  markers around the JP text.
- **End-of-file wikilink description sections** — The `## See Also`, `## Related Concepts`,
  or `## Related Links` header may already be in English, but the bullet-point descriptions
  beneath it (e.g., `- [[concepts/foo]] — Some Japanese description here`) often retain JP.
  Unlike section headers or table cells, these are invisible to a header-only JP scan
  because the header is already English. **Detection**: after Pass 1, explicitly scan all
  bullet-point lines under `## See Also` / `## Related Concepts` / `## Related Links`
  sections for JP chars. These are far from the main narrative content and consistently
  missed in first-pass dicts.  **Fix**: add per-description `str.replace()` entries for
  each JP wikilink description in the reference section. (Discovered in the 2026-05-27 batch:
  `concepts/agentic-pbt.md` had 88 JP chars in its "Related Concepts" section where the header
  was already English but all 10 wikilink descriptions were in Japanese.)
- **Partial JP label left after content replacement** — When a bullet point has both a
  Japanese label prefix AND Japanese content (e.g., `- 関数名：`fetchUserById()``),
  replacing only the content portion (`ではなく` → `→`) but not the label (`関数名：`)
  leaves JP stragglers. The label and content are separate strings — each needs its own
  `str.replace()` entry. A residual scan showing 4 chars in a bullet-heavy file is almost
  always a label prefix that survived. **Fix**: before building the initial dict for a
  bullet-heavy file, scan each line for colon-separated JP prefix + English content
  patterns and ensure both parts have replacement entries.

- **Index file inline entries (`entities/_index.md` pattern)** — Index files have 200+ character single-line entries where JP text is embedded inline in entity descriptions rather than in dedicated paragraphs. Example: `- [[entities/foo]] — English description...日本語テキストが続く、そしてさらに。`. The JP is not in a coherent section but scattered across individual description lines, mixed with English text on the same line. **Detection**: these won't appear in section-header or table-header scans. Use per-line JP search: `for i, line in enumerate(lines): if jp.search(line): print(i, line)`. **Fix approach**: replace the entire line (not just the JP segment) to ensure both JP and English parts are coherently rewritten. Two sub-patterns: (a) ideographic commas `、` (U+3001) embedded in otherwise-English text — replace with `, `; (b) Japanese sentence appended after English description — translate as an appendage. **Why patch is better than str.replace here**: index lines are 200+ chars and often truncated in read_file output, making it impossible to get the exact old_string for str.replace(). Instead, use execute_code to find exact JP lines, read 2-line context, then apply targeted `patch`.

> **Header adjacency blind spot**: When building a per-file `str.replace()` dict for
> mixed-content files, paragraph-length Japanese text (e.g., a 2-sentence paragraph) is
> typically one dict entry. But the `## Section Header` directly above that paragraph is a
> **separate string** not in the dict. After Pass 1, the narrative text is English but the
> header directly above it is still Japanese. Always add header translations to the same
> dict — don't assume the paragraph dict entry "covers" the header above it.

### Japanese Header Discovery After Pass 1

After the bulk translate pass, scan for ALL remaining Japanese section headers across the
batch — not just common ones — to build a complete fix dict:

```python
import re, os
jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')

for f in translated_files:
    fp = os.path.join(wiki_root, f)
    with open(fp) as fh:
        lines = fh.readlines()
    # Split frontmatter from body
    body_start = 0; fm_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2: body_start = i + 1; break
    # Find ALL markdown headers containing JP chars
    for i, line in enumerate(lines[body_start:], body_start):
        stripped = line.strip()
        if stripped.startswith('##') and jp.search(stripped):
            print(f"{f}:{i+1} | {stripped[:120]}")
```

This discovers headers like `## 核心哲学`, `## ワークフロー vs エージェント`,
`## 基本構成要素（Building Blocks）` that won't be in any common-header dict.
Add each one explicitly to your per-file fix dict before Pass 2.

**Multi-pass cleanup procedure:**

**Pass 1 — Main translation** (`execute_code` or `write_file`): Target the bulk content.
Use per-file `str.replace()` for mixed-content files (EN with JP sections scattered in).
Use full rewrite for fully-JP files.

**Pass 2 — Table/section header normalization** (`execute_code` batch): After Pass 1,
run a JP scan to find remaining characters. Apply common pattern replacements across
all translated files at once:

```python
# Batch replacement for common section headers across all translated files
common_section_headers = {
    '## 関連項目': '## See Also',
    '## 関連リソース': '## Related Resources',
    '## 関連コンセプト': '## Related Concepts',
    '## 参考文献': '## References',
    '## 関連リンク': '## Related Links',
    '## 出典': '## Sources',
    '## ソース': '## Sources',
    '## 関連 wikilinks': '## Related Links',
}
# Also batch table header cells (these are file-dependent but patterns recur)
common_table_cells = {
    '| モデル | パラメータ': '| Model | Parameters',
    '| 段階 | 内容 | データ規模': '| Stage | Content | Data Scale',
    '| ベンチマーク | GPT-5': '| Benchmark | GPT-5',  # Don't translate data cells
    '| 戦略 | 動作 | 効率': '| Strategy | Behavior | Efficiency',
    '| 改良点 | 内容 | 効果': '| Improvement | Content | Effect',
}
for fp in translated_files:
    with open(fp) as f:
        content = f.read()
    # Split frontmatter from body
    lines = content.split('\n')
    fm_count = 0; body_start = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            fm_count += 1
            if fm_count == 2: body_start = i + 1; break
    fm = '\n'.join(lines[:body_start]) + '\n'
    body = '\n'.join(lines[body_start:])
    for jp_text, en_text in common_section_headers.items():
        body = body.replace(jp_text, en_text)
    for jp_text, en_text in common_table_cells.items():
        body = body.replace(jp_text, en_text)
    with open(fp, 'w') as f:
        f.write(fm + body)
```

**Pass 3 — Straggler cleanup** (`patch` on individual lines): After Pass 1-2 remove
99%+ of JP, the last 5-20 chars are best handled with targeted `patch` calls. This
is more token-efficient than re-reading and re-writing each entire file for a handful
of characters.

```python
# Find exact straggler lines with context
for i, line in enumerate(body.split('\n')):
    if jp.search(line):
        print(f"Line {i}: {line.strip()[:120]}")

# Then fix with targeted patch — read the exact 2-line context first
patch(
    path="wiki/concepts/gliclass.md",
    old_string="| スコアラ | `simple` (dot product)",
    new_string="| Scorer | `simple` (dot product)",
)
```

**Verification gates:**
- After each pass, re-run the JP char scan on translated files
- Stop only when all translated files show **0 JP chars** in body
- Do NOT accept "almost clean" — stragglers compound when subsequent pipelines
  (blog-ingest, dreaming, active-crawl) add more JP content to files you thought were done
- Final check: `head -4 log.md` to verify the Format line didn't get truncated by
  the log prepending code's `chrono_start` detection

### 8. Parallel write pattern for efficiency

Translate files in parallel batches of 4 to save turns:

```python
# Batch 1 (files 1-4): 4 parallel write_file calls
# Batch 2 (files 5-8): 4 more parallel write_file calls
# Total: 2 rounds of 4 files each = 8 total
```

This avoids sequential file-by-file overhead. All 8 files can be written in
2-3 rounds of parallel `write_file` calls.

### 9. Clean up temp scripts

After committing, remove the translation scripts written to `/tmp/`:

```bash
rm /tmp/translate_batch.py /tmp/translate_batch_*.py
```

This prevents stale scripts from accumulating and avoids confusion in
subsequent sessions (a stale `/tmp/translate_batch_a.py` from an earlier run
may contain incorrect translations for files that were since updated).

## Progress Tracking

Track total progress with:

```python
before_count = 365   # update these from the previous batch
before_chars = 313451

after_count = len(remaining)   # from step 1 scan
after_chars = sum(j for _, j, _ in remaining)

print(f"Files: {before_count} -> {after_count} ({before_count - after_count} done)")
print(f"Chars: {before_chars} -> {after_chars} ({before_chars - after_chars} removed)")
```

## Critical Workflow Principles

Using `assert new_jp == 0` in a batch translation script causes cascade failures: a single byte mismatch on file #4 kills the entire batch, losing progress on files #1-3 (already written) requires differential recovery for #5-8 (never processed). The assert pattern was the #1 source of wasted tool calls in the 2026-05-26 batch (8 files, 7,865 chars).

**The right pattern — print and continue, then report:**

```python
total_removed = 0
failed = []
for path, replacements in file_batch:
    before_jp = len(jp.findall(body))
    for old, new in replacements:
        body = body.replace(old, new)
    after_jp = len(jp.findall(body))
    if after_jp == 0:
        total_removed += before_jp
        write_file(path, frontmatter + '\n' + body)
    else:
        failed.append((path, after_jp))
        print(f"⚠ {path}: {after_jp} JP remain — investigating")

# Then fix failed files individually (see "Post-assertion recovery" below)
if failed:
    print(f"\n{len(failed)} files need fixes — running targeted pass")
    # ... per-file debugging with repr()
```

This ensures ALL successfully-translated files are saved, regardless of failures in other files. Failed files get a targeted follow-up pass.

### Principle 2: Split fully-JP and mixed-JP/EN files into separate batches

Fully-JP files (>80% JP chars) and mixed JP/EN files have **fundamentally different failure modes**:

| File type | Best approach | Common failure mode |
|-----------|---------------|---------------------|
| Fully-JP (>80%) | Full body rewrite via `write_file` | Missing a narrative paragraph in translation |
| Mixed JP/EN (10-80%) | Per-string `str.replace()` dict | Silent non-match on visually-identical chars |

**When to batch them together:** Only when total JP chars per file <100 and the mixed-content files have JP only in section headers/table cells (fewer than 10 replacement strings per file). When any file requires 40+ replacement strings, it adds 40+ failure points.

**Recommended batch split for 8 files:**
- **Batch A (3-4 fully-JP files):** Full body rewrites via `write_file` — fast, reliable, each completes in <1s
- **Batch B (4-5 mixed-content files):** Per-file `str.replace()` dicts via `execute_code` or terminal script

This isolates the two failure modes. If Batch B has a replacement mismatch, Batch A's work is already committed.

### Principle 3: Post-assertion recovery procedure

When a batch script crashes mid-execution (assertion or syntax error):

1. **Check which files were written** — the script writes up to the crash point, then stops. Files BEFORE the crash may be saved; files AFTER were never processed.
2. **Verify each file individually** — do NOT re-run the whole script (which repeats already-done work):
   ```python
   for f in translated_files:
       with open(f) as fh: content = fh.read()
       body = content.split('---', 2)[-1]
       jp = len(jp_re.findall(body))
       print(f"{'OK' if jp == 0 else f'⚠ {jp} JP'}: {f}")
   ```
3. **Handle each state appropriately:**
   - **Already clean file** (0 JP): Skip, it was written before crash
   - **Still has all JP** (pre-crash count): Script never reached this file — translate from scratch
   - **Partially clean** (some JP removed, some remains): Script processed this file but assertion stopped the write — needs one more replacement pass for remaining chars
4. **Re-run only failed files** in a new script/execute_code block

### Principle 4: `repr()` is the first debug step for str.replace() failures

When a `str.replace()` that you're SURE should match doesn't match, do NOT manually inspect the strings — use `repr()` immediately:

```python
# WRONG — guessing doesn't reveal the issue
print(f"old[:50]: {old[:50]}")
print(f"file[:50]: {file_content[file_content.find('keyword'):][:50]}")

# CORRECT — repr() shows exact bytes
print(f"  OLD: {repr(old[:80])}")
print(f"  FILE: {repr(file_content[file_content.find('keyword'):][:80])}")
```

**Common repr() revelations from production (2026-05-26 batch):**
- `。` (句点) vs `：` (colon) — visually identical but different Unicode chars: `\u3002` vs `\uff1a`
- `（ ` `）` (full-width parens, `\uff08` `\uff09`) vs `(` `)` (ASCII parens, `\u0028` `\u0029`)
- `―` (em dash, `\\u2015`) vs `—` (em dash, `\\u2014`) vs `-` (hyphen-minus, `\\u002d`)
- `传` (simplified Chinese, U+4F20) vs `伝` (Japanese/Traditional, U+4F1D) — visually very
  similar in most fonts; appeared in the phrase `「传言ゲーム」` (telephone game) in a
  Japanese wiki file that used the simplified Chinese `传` instead of the Japanese `伝`.
  A `str.replace()` targeting `伝` silently failed on this line until `repr()` revealed
  the different Unicode code point.
- Trailing space on `old` string that doesn't exist in file (or vice versa)
- `\n` vs `\r\n` line endings

**Always reach for `repr()` before any other debugging technique for string-match failures.**

## Pitfalls

- **Code block multi-line expansion artifact — visual duplication from single-line replacement** — When a `str.replace()` takes a single-line JP string and expands it into 2+ lines inside a code block or ASCII-art diagram, the replacement can create visual duplicates with adjacent lines. Example inside a code-block diagram:

  ```
  ... → Final Accepted State
                          ↑
                          これが「Gold Diff」（正解差分）
  ```

  Replacing `これが「Gold Diff」（正解差分）` with `↑\nThis is the "Gold Diff"` produces two arrow lines:

  ```
  ... → Final Accepted State
                          ↑
                          ↑
          This is the "Gold Diff"
  ```

  The arrow `↑` now appears on TWO lines — the original above the replacement, plus the first line of the replacement string. **Prevention**: Before writing multi-line `str.replace()` values for code-block content, trace the exact file structure. If the line above contains repeating ASCII art (arrows `↑`, connectors `│`, dashes `─`), the expansion will create a duplicate. Either: (a) include the arrow line IN the `old_string` so the replacement swallows both the arrow and the text, or (b) use a single-line replacement without adding a prefix line. **Detection**: after the batch, visually spot-check code-block sections. **Fix**: re-run with a corrected replacement that accounts for the adjacent line.

- **NEVER blanket-replace `の` as a standalone str.replace() entry** — The Japanese possessive/no particle `の` (U+306E) is the most common kanji/hiragana character pair in Japanese text. Adding `'の': ' '` or any standalone `の` → EN replacement to a batch dict will destroy grammatical structure across ALL JP sentences in the file. Every sentence fragment containing `の` gets its particle stripped, leaving orphaned JP chars with no grammatical connection — making them harder to translate in subsequent passes. The remaining text becomes fragmented artifacts like `多極的罠（multipolar traps）と 、競争 参加する全エージェント 共有価値 犠牲 せざる 得ず` (from a real case in the 2026-05-27 batch) instead of a coherent JP sentence that can be matched and replaced. Rule: ALWAYS translate entire JP sentences or semantic units — never individual particles. If you see a JP line that contains `の`, translate the full line including the `の`, not the `の` separately.

- **Line-number prefix corruption causes silent str.replace failure** — Entity/concept files can accumulate `     1|---`, `     2|title:` style prefixes on every line if a prior session accidentally wrote `read_file` output back to the file. When a file has line-number prefixes, ALL `str.replace()` calls silently fail because the actual content is `   159|- 1つのエージェントが...` instead of `- 1つのエージェントが...`. The str.replace looks for the un-prefixed string, doesn't find it, and the file is unchanged. **Pre-check**: Before running any str.replace, check the first body line for the corruption pattern:
  ```python
  with open(path) as f: first_line = f.readline()
  import re
  if re.match(r'^\s*\d+\|', first_line):
      print(f"⚠ CORRUPTED: {path}")
  ```
  **Fix**: Strip prefixes with a single regex before applying translations:
  ```python
  content = re.sub(r'^\s*\d+\|', '', content, flags=re.MULTILINE)
  ```
  **Detection**: After writing translated content, if a file still has JP chars but the scan showed it was supposed to be clean, check for line-number corruption first. The global before/after JP count will be wrong because it counted the prefixed content.
  **Prevention**: Never write `read_file` output (which includes line-number prefixes) back to disk. Use `with open(path, 'w') as f: f.write(content)` for file modifications — the raw file content from `open().read()` is clean.

- **Duplicate filename trap across directories** — The `os.walk()` scan picks up ALL `.md` files with the same glob, including files with the same basename in different directories (e.g., `concepts/claude-code-best-practices.md` AND `concepts/harness-engineering/system-architecture/claude-code-best-practices.md`). The scan sorts by JP char count descending and takes the top N — but the lower-ranked duplicate with the same filename may not appear in the top 8 and gets silently skipped. **Fix**: After selecting the top N candidates, check for duplicates by base filename. If any candidate's basename appears in other directories (excluding the subdirectory of the candidate itself), add the duplicate to the translation batch:
  ```python
  # After selecting top 8, check for same-named files
  selected_basenames = [os.path.basename(p) for p, _, _ in candidates[:8]]
  duplicates = []
  for base in selected_basenames:
      for root, dirs, files in os.walk(wiki_root):
          if 'raw/' in root: continue
          for f in files:
              if f == base:
                  fp = os.path.join(root, f)
                  rel = os.path.relpath(fp, wiki_root)
                  if rel not in [c[0] for c in candidates[:8]]:
                      duplicates.append(rel)
  if duplicates:
      print(f"⚠ Also need to translate: {duplicates}")
  ```

- **Per-file verification trap (global counts hide silent failures)** — The post-translation check reports global JP char counts before/after, which can hide individual file failures. If 7 of 8 files are clean but 1 file had silent str.replace failure (due to line-number corruption or anchor mismatch), the global count might show 8,500 chars removed out of 9,100 — looks like partial success, not a failure. But the 1 failed file still has all its JP. **Fix**: After translation, always verify EVERY file individually, not just globally:
  ```python
  for f in translated_files:
      with open(os.path.join(wiki_root, f)) as fh: content = fh.read()
      body = content.split('---', 2)[-1]  # crude split after 2nd ---
      jp_in_body = len(jp.findall(body))
      status = '✓' if jp_in_body == 0 else f'⚠ {jp_in_body}'
      print(f"  {status}: {f}")
  ```
  Only accept the batch as complete when ALL translated files show `✓`. Any single `⚠` means something went wrong — investigate that file specifically (check for line-number corruption, anchor mismatch, or missing replacement keys).

- **Python str.replace() quote-escaping trap** — When building a large `str.replace()` dict in a Python script, any replacement VALUE containing an apostrophe/single-quote character (`'`) will break a single-quoted Python string, producing `SyntaxError: invalid decimal literal`. Example that breaks:
  ```python
  r["- **Data**: 15.6T tokens (8.7x Llama 2's 1.8T)."] = "..."
  ```
  **Detection**: The SyntaxError points to the character AFTER the apostrophe. **Fix options**:
  1. Escape the apostrophe: `Llama 2\'s`
  2. Use double quotes for that specific string
  3. Reformulate to avoid apostrophes: `"Llama 2 at 1.8T"` instead of `"Llama 2's 1.8T"`
  4. **Best for large batches**: Write the entire translation script to a file first via `write_file`, then execute with `python3 /path/to/script.py` — this bypasses most quoting issues because `write_file` does not interpret Python string delimiters.
   **⚠️ Caveat: `write_file` can corrupt backslash-escaped characters** in Python string literals (like `\\n` inside replacement strings, or `\\'s` in possessive forms). The corrupted file produces `SyntaxError` on execution. **If the file-based script fails**, switch to the `execute_code` per-file helper pattern (see section 3 above) — it avoids write_file's content encoding entirely.
  **Prevention**: Before writing any str.replace() dict, scan your replacement values for apostrophes. If any contain `'s`, use double quotes or reformulate.

- **N-script split by replacement-pair volume, not file-count halves** — The old rule "Script 1 = first half, Script 2 = second half" works for batches where replacement pairs are evenly distributed. In practice, some files need 80+ replacement pairs (mixed-content with many scattered JP paragraphs, table cells, and headers) while others need 10-15. Split scripts by **total replacement pairs**, not file count:
  | Total replacement pairs | Split strategy |
  |---|---|
  | <30 | Single script |
  | 30-60 | 2 scripts |
  | >60 | 3+ scripts |
  Each script targets a subset of files with roughly equal replacement-pair load (e.g., 3+3+2 files instead of 4+4). This avoids syntax errors from overly large dict literal blocks and keeps each script debuggable independently. Clean up temp files after: `rm /tmp/translate*.py`.

- **Frontmatter `description` field is body text, not metadata** — Don't blindly skip
  all frontmatter fields. The `description` line contains human-readable prose that should
  be translated alongside the body. Read it explicitly during step 4.

- **`read_file` display prefixes create misleading replacement strings** — When you read
  a file with `read_file`, the output shows `    39|- **実行タイミング:**`. The `    39|`
  is the line-number prefix; the actual file content starts with `- **実行タイミング:**`.
  However, the visual presentation (space + `|` before the `-`) makes it look like the
  content starts with `|- `. If you write `|- ` in your replacement `old_string`, the
  `str.replace()` will silently fail because the actual file content has plain `- `.
  **Detection**: the first assertion in your script fires with `"replacement not found"`.
  **Prevention**: always confirm the actual file content with `sed -n '<line>p <file> | cat -A`
  or `head -1 <file>` when you're unsure. The `cat -A` output will show `- **実行タイミング:**`
  (no leading `|`). As a rule of thumb: if `read_file` shows `NNN|- content` where `NNN` is
  a line number, the actual content is `- content` — drop the `|- ` interpretation.
  **This also affects `patch` calls**: the `old_string` in a `patch` must use the actual
  file content (plain `- `), not the read_file display form.

- **Post-write quote-escaping fix: line-level recovery** — When a `write_file`-generated
  translation script has a syntax error from an unescaped apostrophe in a dict value,
  do NOT rewrite the entire file. Fix at the line level:
  - Use SyntaxError lineno to identify the exact line index (0-based)
  - Read the file into lines: open -> readlines -> list
  - Replace the single line with corrected content (backslash + quote in the new line)
  - Write back: open -> writelines
  - Verify with ast.parse on the whole file — confirms NO remaining syntax errors
  - This saves re-encoding hundreds of translation lines just to fix one unescaped quote
  - Use ast.parse AFTER EVERY fix pass, not just the first — it catches ALL syntax errors
  - Real example (2026-05-27 batch): dict value `don't` in single-quoted string produced
    SyntaxError. Fixed by reading lines, replacing index 365 with escaped `don\'t`, verified
    with ast.parse — took 1 tool call vs ~6 for rewriting the entire script
- **Dict coverage gaps — missing entries for known JP content** — When building a
  per-file `str.replace()` dict in a Python script, it is easy to mentally identify
  a JP string during file reading but then forget to include its replacement entry
  in the actual dict. Unlike a silent non-match (covered by the `if old in body:`
  guard), a missing dict entry is invisible — no warning fires, the JP survives,
  and you only discover it in the post-translation verification scan. This costs
  a separate patch/debug round.
  **Prevention (pre-flight validation):** After writing the script but before
  running it, scan each source file for ALL JP lines and cross-check against
  dict keys:
  ```python
  # Run BEFORE executing the batch
  import re
  jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
  for file_path, replacements in your_file_dict.items():
      with open(file_path) as f:
          body = f.read().split('---', 2)[-1]
      missed = []
      for i, line in enumerate(body.split('\n')):
          if jp.search(line) and not any(old in line for old in replacements):
              missed.append((i+1, line.strip()[:100]))
      if missed:
          print(f"⚠ {os.path.basename(file_path)}: {len(missed)} JP lines uncovered")
          for ln, txt in missed[:5]:
              print(f"  L{ln}: {txt}")
  ```
  **Common omissions in production** (2026-05-26 batch): (a) standalone section
  headers like `## 関連` between translated body blocks, (b) short inline phrases
  like `OpenClaw VISION.mdから：` (full-width colon), and (c) blockquote continuation
  lines starting with `>` that contain JP after an English quote. Run validation on
  EVERY file, not just the ones you feel confident about.

- **`description:` field separate fix is easily forgotten** — When writing a batch
  script with a dedicated `translate_description()` helper, it's common to define
  the function but forget to CALL it from each per-file handler. The function exists
  but is never executed, leaving all `description:` fields in JP. Three prevention
  strategies: (1) inline description translation into each per-file function rather
  than using a separate helper; (2) after the main batch pass, run a targeted check
  on all translated files' `description:` lines; (3) include description translation
  in the same function that bumps `updated:` — make it automatic.

- **delegate_task times out on large fully-JP files** with 3K-5K+ JP chars each and 200+ lines.
  The subagent takes too long reading, processing, and writing. Use direct `write_file` or `execute_code`.
  **Exception: delegate_task is effective for scattered-JP files** (mostly English with JP mixed in
  10+ locations). On a 1732-line log file with 4,015 JP chars across 231 scattered lines, a delegate_task
  subagent completed in 298s and removed all JP. The str.replace() approach had only removed 670 after
  3 passes. For scattered-JP files, the subagent's context-aware understanding dramatically outperforms
  mechanical replacement. Split the batch: concept files → execute_code/write_file, log files → delegate_task.
- **Log header burial** — never use `f.write(new_entry + content)` pattern.
  Always split at chrono_start and insert the entry between the header block
  and existing chronological entries.
- **Batch size** — 8 files per batch works well. More than 12 risks token limits
  from carrying the full translated content of each file.
- **No tags to fix** — JP→EN translation does not add new tags, so the pre-commit hook
  should pass cleanly. If it blocks, the violation is pre-existing in a different staged
  file — check `git status --short` and fix those separately.
- **Backtick text eaten by bash heredoc when logging via `terminal`** — When using
  `terminal` with inline Python (e.g., `python3 -c "..."`), bash interprets backticks
  as command substitution before Python sees them. A log line like
  `- Updated all \`updated:\` dates` becomes `- Updated all  dates`
  (backtick phrase swallowed). **Fix**: use `execute_code` (Python sandbox, not bash)
  for log manipulation. If you must use `terminal`, escape backticks as `\``.
  **Detection**: after any `log.md` write via `terminal`, grep for
  `Updated all  dates` (double-space where the backtick phrase should be).
  Fix stragglers with a subsequent `patch` call.
- **Straggler JP chars after verification** — The verify scan can report 2-5 JP chars
  remaining in "clean" files. Common culprits: full-width parentheses `（）`, stray
  kanji in code blocks, JP punctuation `。` `、` in preserved foreign-language quotes.
  **Procedure**: use `execute_code` to find the exact line with
  `for i, line in enumerate(body.split('\\n')): if jp.search(line): print(i, line)`,
  then `patch` each straggler individually. Most are literal artifacts (full-width
  parens in code-block labels) — replace with ASCII equivalents `()`.
- **skill_manage(write_file) overwrites the entire file** — Unlike `write_file` tool
that can be called in parallel for independent files, `skill_manage(action='write_file',
file_path='references/...')` replaces the ENTIRE reference file with `file_content`.
To add content to an existing reference file, use `skill_manage(action='patch')` on
the file_path, or edit+reconstruct the full content. This pitfall was discovered when
a patch to add 3 pitfalls accidentally overwrote the entire reference document with
just the pitfalls section.

- **Chinese name CJK false positive — 姚顺雨 is not Japanese text** — The scan regex `\u4E00-\u9FFF` catches ALL CJK characters indiscriminately, including Chinese proper nouns embedded in otherwise-English entity pages. When the scan reports entity pages for Chinese researchers (e.g., `entities/shunyu-yao.md` with 10 CJK chars: 姚顺雨, 姚班), those are Chinese characters in proper names — not Japanese language text. **Detection**: after the scan, for any entity page with <15 CJK chars, check whether the CJK chars all appear in: (a) the entity's Chinese name in the title (`Shunyu Yao (姚顺雨)`), (b) Chinese university/institution names (`Tsinghua University, Yao Class (姚班)`), or (c) Chinese company names. **Rule**: if every CJK character in the file's body is part of a proper noun (person name, institution name, or company name written in Chinese), exclude the file from the translation batch. Always read the full file to confirm — do NOT base this on filename alone. (Discovered in the 2026-05-27 batch.)

- **JP-named file duplicate check — topic may already have an enriched EN page** — JP-named files (containing kanji/kana in the filename) are often duplicate stubs of topics that already have fully-enriched English-named pages. Before processing a JP-named file, search the index and filesystem for the topic's core keywords (the Japanese-free portion of the topic name). Example: `hierarchy-to-intelligence-blockの組織モデル変革.md` was a duplicate of the already-enriched `ai-organization/ai-org-from-hierarchy-to-intelligence.md` (10KB, `status: draft`). **Procedure**:
  1. Extract the topic's English keywords from the JP filename (e.g., `hierarchy-to-intelligence-block`, `anthropics-memory-tool-cognition`)
  2. Search `index.md` for those keywords to find existing EN entries
  3. Search the filesystem for any `.md` file containing those keywords (excluding the JP-named file itself)
  4. If a matching EN page exists with substantive content (>1KB, `status` not `stub`), delete the JP-named stub instead of translating it — the EN page already covers the topic
  5. Check that the index entry for the JP stub doesn't exist (if no index entry, clean deletion; if it exists, remove from index)
  6. Log as `translate | JP→EN — file deleted (duplicate)` with explanation
  This prevents expending effort translating a stub when the topic is already covered. (Discovered in the 2026-05-27 batch.)

- **Raw article path references in body text are immutable — exclude from char count** — JP characters inside `raw/articles/` file path references (both relative `../raw/articles/` and absolute paths) within concept page body text should NOT count toward the translatable JP char total. These paths point to existing immutable raw files. Example: `thin-bi.md` had 7 remaining JP chars in the path `../raw/articles/2033336956961308721_薄くなるbiツール.md` — a valid link to an existing raw file. **Rule**: on the post-translation verification scan, exclude any JP chars that appear inside a markdown file path that contains `raw/`. Detection pattern: `re.findall(r'raw/articles/[^\s)]+', line)`. If all remaining JP chars in a file are within raw/ file path references, mark the file as "clean (raw path only)" rather than blocking. (Discovered in the 2026-05-27 batch.)

- **`patch` tool over-escapes content with `'s` or `\n`** — When using the `patch`
tool to fix a specific line in a Python script or markdown file that contains escaped
apostrophes (`\'s`) or escaped newlines (`\n`), `patch` **adds extra escaping levels**.
Example: a line containing `Pi\'s` becomes `Pi\\\\'s` and `\n\n` becomes `\\\\n\\\\n`.
**Detection**: the resulting file shows double backslashes `\\n` instead of actual
newlines. **Fix**: Use `execute_code` with Python `str.replace()` on the file content
to fix the line, rather than using the `patch` tool on Python string literals.
Alternatively, rewrite the affected section via `write_file` with the corrected content.
**Prevention**: Never use `patch` to modify lines inside Python string literals that
contain backslash escapes or escaped quotes. Use `execute_code` with direct file I/O
(`with open(path) as f: content = f.read()` then `content = content.replace(...)` then
`f.write(content)`) for any fix involving Python string content.

- **Multi-line `str.replace()` can fail silently** — When building a `str.replace()` dict
entry that spans multiple lines (e.g., heading `\n\n` body paragraph), the replacement
may silently not match despite appearing correct. The `old` string's `\n\n` between
heading and body may differ from the file's actual whitespace (tab vs spaces, Unicode vs
ASCII characters that look identical, or stray non-printable characters). **Detection**:
after `str.replace()` returns, verify with `if old in content: print("OK") else: print("FAIL")`.
**Fix strategy**: Use shorter, more targeted replacements — one for the heading line,
separately for the paragraph. Break long multi-line `old` strings into individual
one-liner replacements. **Debug with `repr()`**: When a multi-line string doesn't match,
use `repr()` on both the `old` string and the target file content to compare exact bytes:
`print(repr(line_with_jp))` reveals stray characters, wrong Unicode vs ASCII dashes,
and extra whitespace that are invisible when printed normally. **Real-world example**:
A `str.replace()` for a `.pi` folder workflow section failed because the `\n\n` between
heading and body text matched in the editor but the file had subtly different whitespace.
Using `repr()` revealed that the heading line was split differently than expected.

- **In-memory content variable vs file-based save_and_report() inconsistency (silent revert bug)** — When mixing two approaches in the same `execute_code` block: (a) in-memory modifications to a `content = f.read()` variable, and (b) `save_and_report()` calls that read/modify/write the file from disk, the final `with open(fp, 'w') as f: f.write(content)` can SILENTLY REVERT all `save_and_report()` changes. This happens because `content` was captured before the `save_and_report()` calls ran, so writing it back overwrites the file-based modifications.

  **Example trace (2026-05-27 batch, `concepts/mcp-desktop-extensions.md`):**
  ```
  1. content = f.read()              # Captures pre-fix state
  2. content = replace(icon, new)   # Icon fix applied to in-memory content
  3. save_and_report(fp, ...)        # Reads file from disk, modifies, writes back
  4. f.write(content)                 # Writes the old `content` from step 1+2
                                       # — REVERTS save_and_report() changes!
  ```

  **Prevention: use ONLY one modification strategy per execute_code block.**
  - **Strategy A (file-based):** Use `save_and_report()` for ALL replacements. Never manipulate an in-memory `content` variable.
  - **Strategy B (in-memory):** Read once into `content`, apply ALL replacements via `content = content.replace(...)`, write once at the end. Never use `save_and_report()` in the same block.
  - **Strategy C (pass separation):** If you need both approaches, split them into separate `execute_code` calls in distinct passes. Pass 1 uses Strategy B for bulk replacements; Pass 2 re-reads the file from disk and uses Strategy A for targeted fixes.
  
  **Detection**: After the batch, if a file that should be clean still has JP chars, and the stragglers were in a section you already wrote replacement entries for, suspect a revert. Verify by re-reading the file and checking whether the `save_and_report()` changes actually persisted.

- **Stripped-string fallback for whitespace-mismatched replacements** — When building
  per-file `str.replace()` dictionaries, the `old` string sometimes differs from the file's
  content by invisible whitespace (trailing spaces, tab vs spaces, leading indentation
  differences in code blocks or table rows). Add a stripped-string fallback to catch these
  without requiring `repr()` debugging for every silent failure:

  ```python
  for old, new in replacements:
      if old in body:
          body = body.replace(old, new)
      # Fallback: try stripped version (catches leading/trailing whitespace mismatches)
      stripped_old = old.strip()
      if stripped_old != old and stripped_old in body:
          body = body.replace(stripped_old, new.strip())
  ```

  **When this helps**: Table cell contents where one entry has `| **NF4** | 理由...` with
  leading space after `|` but another entry in the same column has `|**FP4** | 理由...`
  without the leading space. The stripped fallback catches both. **When it doesn't help**:
  Inline differences in the MIDDLE of a string (e.g., Unicode em-dash `—` vs ASCII `--`).
  Those still need `repr()` debugging.  **Safety**: The `stripped_old != old` guard ensures
  this only fires when there IS leading/trailing whitespace to strip — it won't
  accidentally retry every replacement.

- **Pre-commit hook log.md JP warning is expected** — When documenting JP→EN translations
  in log.md by backtick-wrapping old JP text (e.g., `` `T4 16GB GPUでのベンチマーク:` ``),
  the pre-commit tag validator may warn about increased JP chars in log.md (25→53, +28).
  This warning is expected and harmless — the JP chars are in log entry backtick spans
  referencing old content, not in the wiki body. The commit still passes (warning, not a
  block). If you want to suppress it, write log entries without backtick-wrapping JP text
  or describe the change with transliterations instead: `T4 16GB GPU benchmark` rather
  than `` `T4 16GB GPUでのベンチマーク:` ``.
