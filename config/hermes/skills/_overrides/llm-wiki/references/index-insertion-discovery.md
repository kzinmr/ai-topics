# Index Insertion Point Discovery

When adding new pages to `index.md` via `patch`, you need to know the exact
surrounding lines. For large indexes (1500+ lines), use `execute_code` to
programmatically find insertion points rather than eyeballing.

## Pattern: Find alphabetical insertion points

```python
import os

wiki = os.path.expanduser("~/wiki")
with open(os.path.join(wiki, "index.md")) as f:
    lines = f.readlines()

# Find section boundaries
sections = {}
for i, line in enumerate(lines):
    if line.startswith("## Entities"):
        sections["entities_start"] = i
    elif line.startswith("## Concepts"):
        sections["entities_end"] = i
        sections["concepts_start"] = i
    elif line.startswith("## Comparisons"):
        sections["concepts_end"] = i

# Extract all entries from a section
def get_entries(start, end):
    entries = []
    for i in range(start + 1, end):
        line = lines[i].strip()
        if line.startswith("- [["):
            entries.append((i, line))
    return entries

# For a new page "concepts/federated-tiny-training-engine", find neighbors:
entries = get_entries(sections["concepts_start"], sections["concepts_end"])
target = "concepts/federated-tiny-training-engine"

for idx, (lineno, line) in enumerate(entries):
    # Extract the page name from the wikilink
    name = line.split("[[")[1].split("]]")[0].split("|")[0]
    if name > target:
        # This is the first entry alphabetically after our target
        prev_lineno, prev_line = entries[idx - 1]
        print(f"Insert between L{prev_lineno+1} and L{lineno+1}:")
        print(f"  BEFORE: {prev_line[:100]}")
        print(f"  AFTER:  {line[:100]}")
        break
```

## Pattern: Verify all new pages are unique

Before creating pages, check they don't already exist:

```python
new_pages = [
    "entities/xai.md", "entities/grok-4-3.md",
    "concepts/grok-computer.md", "concepts/microsoft-copilot-wave-3.md",
    "concepts/federated-tiny-training-engine.md"
]
for p in new_pages:
    path = os.path.join(wiki, p)
    print(f"{'EXISTS' if os.path.exists(path) else 'MISSING'}: {p}")
```

## Pattern: Verify cross-references after creation

```python
cross_refs = {
    "entities/xai.md": ["entities/grok-4-3", "concepts/grok-computer"],
    # ...
}
for page, refs in cross_refs.items():
    for ref in refs:
        ref_path = os.path.join(wiki, ref + ".md")
        if not os.path.exists(ref_path):
            ref_path = os.path.join(wiki, ref, "_index.md")
        exists = os.path.exists(ref_path)
        if not exists:
            # Try to find similar pages
            import glob
            name = ref.split("/")[-1]
            for f in glob.glob(os.path.join(wiki, "**", f"*{name}*"), recursive=True):
                print(f"  CANDIDATE: {os.path.relpath(f, wiki)}")
```

## Key gotcha: `patch` index.md drops entries when old_string guesses wrong

When the discovery script prints insertion points, it shows the neighbor lines. **You
must copy the exact text of 2-3 surrounding lines from the actual file** to use as
`old_string`. Do NOT guess what's between two anchor points — the file may have entries
you didn't see. The discovery script output is a guide to line numbers, not a substitute
for reading the exact text.

**Bug that occurred:** Discovery said "insert `cloudflare-llm-infrastructure` before
`recursive-self-improvement` at line 448." I constructed:

```
old_string = "## Concepts (428 pages)\n\n- [[concepts/recursive-self-improvement]]"
```

But the actual file had `- [[concepts/accelerate]]` between the header and
`recursive-self-improvement`. The `patch` silently matched something else, dropped
`accelerate`, and created a bare duplicate of `recursive-self-improvement`. Required
a second patch to fix.

**Correct approach:** After the discovery script tells you the insertion point, use
`read_file` with the exact offset to confirm the 2-3 lines that will form your
`old_string` anchor, OR have the discovery script print the full text of those lines
so you can copy them verbatim into your `patch` call.

**Verification after every index patch:** Use `read_file` with the target offset
to confirm the section has the correct entries in order and no entries were dropped
or duplicated. Do this BEFORE moving on to log.md or committing.

## Key gotcha: `patch` log.md without duplicating sections

`patch` REPLACES `old_string` with `new_string`. If your `new_string` contains a
copy of the `old_string`, nothing duplicates — it just replaces. BUT if the file
contains the `old_string` text elsewhere, you get a duplicate.

## Key gotcha: Non-alphabetical index causes programmatic insertion to fail silently

**What happened (2026-05-08 active-crawl session):**

The discovery script found "first alphabetical successor" for `defenseclaw`,
`microsoft-agent-governance-toolkit`, and `model-spec-midtraining`. But because
the concepts section of the index is NOT strictly alphabetical (e.g., entries like
`deepclaude` at L478 appear far from `deepseek-v4` at L484, and `mit-encompass`
appears after `moltbook-breach-2026` when alphabetically it should come before),
the script placed all three entries at line 470 — right after `altman-three-observations`
and before `object-storage-queue`. This was wrong for all three.

The entries ended up duplicated: one wrong copy at line 470-472, and then the
`patch`-based correct insertion added a second copy at the right position. Cleanup
required finding all duplicates, removing the wrong copies (bottom-up to preserve
indices), and re-verifying.

**Root cause:** The "find first alphabetical successor" algorithm assumes the list
is sorted. At 5000+ pages, the index drifts from strict alphabetical order because
different agents, pipelines, and manual edits insert entries at different times.
The algorithm finds the first entry that sorts higher — but that may be far from
the intended neighborhood.

**Correct approach:**
1. Read the target section with `read_file(offset=N, limit=30)` to visually scan
   the neighborhood where the entry belongs.
2. Identify the exact 2-3 lines that should surround the new entry.
3. Use those exact lines as the `old_string` anchor in a `patch` call.
4. After every index `patch`, verify the insertion with `read_file`.

**Do NOT** use `execute_code` with "scan for first alphabetically-greater entry"
as a primary strategy. It only works for strictly-sorted lists. If you must use
it, treat its output as a rough hint, then ALWAYS confirm with `read_file` the
exact anchor lines before calling `patch`.

## Key gotcha: `patch` log.md without duplicating sections — prepend pattern

**The session pattern that caused a bug:** Prepending a new entry to `log.md`:
# log.md currently starts with:
# ## [2026-05-02] Shopify — "..."
# - details...

# I wanted to prepend an Active Crawl entry above Shopify.
# My approach: use "## [2026-05-02] Shopify — ..." as old_string,
# include it in new_string along with the new entry.

patch(
    old_string='## [2026-05-02] Shopify — "..."',
    new_string='## [2026-05-02] Shopify — "..."\n\n## [2026-05-02] Active Crawl — ...\n\n...',
)

# RESULT: Shopify header appears TWICE — once from new_string start,
# once from the original position that wasn't matched.
# The fix: DON'T include old_string in new_string when prepending:
patch(
    old_string='## [2026-05-02] Shopify — "..."',
    new_string='## [2026-05-02] Active Crawl — ...\n\n...',
)
# This replaces the Shopify header with the Active Crawl header.
# Shopify content below remains intact.
```

**Rule of thumb:** When prepending to log.md, use the current first entry as
`old_string` and make `new_string` contain ONLY the new entry. The old entry
will be replaced, and its details continue below the new entry. Always verify
the first ~5 lines of log.md after patching.
