# Patch Pitfalls for Wiki Index.md

> Common issues when using `patch` on long index.md lines.

## Index.md Text Duplication

**What it looks like**: After patching an `index.md` entry, the replacement line has duplicated trailing text:
```
- [[entities/openai-codex]] — ...mobile support. Source: [[entities/zhanshi-wang]]. See [[concepts/codex-prompting]] for prompt design..ee [[concepts/codex-prompting]] for prompt design.
```

**Root cause**: When `old_string` for a long index.md line is truncated mid-phrase (e.g., ending at `. S` instead of the full `See [[concepts/codex-prompting]] for prompt design.`), the replacement `new_string` appends the full trailing text, but the original trailing fragment (`. S...`) remains in the file, causing duplication.

**Fix**: After any `patch` to `index.md`, re-read the patched line and verify no duplication occurred. If it did, run a second patch to clean up.

**Prevention**: When building `old_string` for long index.md entries:
1. Include enough trailing context to reach a sentence boundary (`. ` followed by uppercase or end)
2. Never truncate mid-word or mid-wikilink
3. After patching, always verify the line reads correctly end-to-end

**Example (2026-06-03)**:
```
# old_string ended with ". S" — truncated "See [[concepts/codex-prompting]]"
# new_string ended with "...Source: [[entities/zhanshi-wang]]. See [[concepts/codex-prompting]] for prompt design."
# Result: ".ee [[concepts/codex-prompting]] for prompt design." duplicated
# Required second patch to clean
```
