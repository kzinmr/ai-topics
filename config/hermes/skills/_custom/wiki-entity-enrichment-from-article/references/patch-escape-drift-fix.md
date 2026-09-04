# Patch Tool `\"` Escape-Drift Pitfall

## Symptom
When using `patch` to insert text containing double-quoted titles (e.g., article titles, book names, or any plain double-quotes) into `index.md` or entity/concept pages, the patch tool may silently write `\"` (escaped/broken quotes) into the actual file content.

Example of corrupted output:
```
enriched with \"The Problem is Prompt Debt\" framework
```
Instead of the intended:
```
enriched with "The Problem is Prompt Debt" framework
```

## Affected Files
- `wiki/index.md` (most common — new entries with quoted article titles)
- `wiki/concepts/*.md`, `wiki/entities/*.md` (when patching descriptions)
- Any file where `old_string` or `new_string` contains double-quote characters

## Detection
After every patch that inserts quoted text, immediately `read_file` the affected lines. Look for `\"` sequences.

```bash
# Quick check: grep for backslash-quote in recently changed files
grep -n '\\"' wiki/index.md | head -5
```

## Fix
Use a second patch replacing the escaped line with the corrected version:

```python
# old_string: the corrupted line with \"
# new_string: the same line with regular "
patch(
    path="wiki/index.md",
    old_string='- [[slug]] — enriched with \\"Title\\" (June 23)',
    new_string='- [[slug]] — enriched with "Title" (June 23)'
)
```

## Root Cause
The patch tool serializes double-quotes differently depending on context. When `new_string` contains `"` inside a larger string, the tool may double-escape them. This is distinct from the Unicode smart-quote escape-drift issue — this affects regular ASCII double-quotes.

## Frequency
Observed 3 times in a single session (June 2026):
1. `wiki/index.md`: Drew Breunig entity entry — fixed with second patch
2. `wiki/index.md`: prompts-as-technical-debt concept entry — fixed with second patch
3. `wiki/concepts/gepa.md`: Breunig citation line — fixed with second patch

## ⚠️ The escape-drift guard is INCONSISTENT (Aug 2026)

The patch tool's built-in escape-drift detection does **NOT reliably fire**. In one blog-wiki-ingest session it behaved two different ways for the same `\"` in `new_string`:

| Attempt | Tool behavior |
|---|---|
| `entities/cats-with-power-tools.md` (quoted article title in new_string) | Guard FIRED: rejected with "Escape-drift detected: old_string and new_string contain the literal sequence '\\\"' but the matched region of the file does not" — helpful, safe |
| `entities/cory-doctorow.md`, `entities/ramp-labs.md` (identical quoting style) | Guard SILENT: patch accepted, `\"` written literally into the file, required a second fix patch |

**Rule: never rely on the guard as the safety mechanism.** The guard rejection is a bonus, not the protection. After ANY patch whose `new_string` contains double-quotes, run the grep check — regardless of whether the tool complained:

```bash
grep -n '\\"' wiki/entities/<file>.md
# any hit = corruption, fix with a second patch replacing \" -> "
```

The detection grep must use the shell-escaped form `'\\"'` (backslash-backslash-quote in the shell command) to find a literal backslash+quote in the file. In this session, patching the corrupted `\"` lines back to plain `"` (and swapping a broken `[[concepts/ai-safety]]` link for the real `[[concepts/agent-safety]]` in the same fix pass) restored the file cleanly.

## Prevention
- After every patch on `index.md` that inserts quoted text, immediately read back the affected lines
- If `\"` appears anywhere, fix before continuing to the next patch
- Consider using single quotes or avoiding quotes in index.md descriptions when possible
