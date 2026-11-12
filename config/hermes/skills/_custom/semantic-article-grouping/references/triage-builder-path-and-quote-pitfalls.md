# Triage builder script pitfalls (validated 2026-11-12, blog-triage run 20261112T100026Z)

Two build-time (not parse-time / not runtime-logic) failures in the `/tmp/` builder script pattern.

## 1. Helper name collision with `open()` -> path doubling

Builder defines a short excerpt helper named `raw(name)` that internally does `open(RAW + name)`, while call sites pass absolute paths built as `RAW + "file.md"` (to feed `raw_path` too). Result:

```
FileNotFoundError: .../wiki/raw/articles//opt/data/ai-topics/wiki/raw/articles/simonwillison.net--....md
```

Fails during `D.append(make(...))` evaluation, i.e. at import time, deep inside the takes block -- easy to misread as a bad filename.

**Fix** - normalize inside the helper, not at every call site:

```python
def raw(name):
    p = name if name.startswith("/") else RAW + name
```

## 2. ASCII double-quote inside a CJK literal in metadata fields

The documented CJK blocker (`SyntaxError: invalid decimal literal`) is usually shown for `reason_ja` containing embedded ASCII double quotes. It fires identically for a quoted keyword inside a grep description:

```python
"reason_ja": "...grep \"Gemini\" de 0 hit..."   # SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Note the *different* error message (`invalid syntax. Perhaps you forgot a comma?`) -- same root cause. Fix: drop the quotes or use Japanese brackets.

**Always gate** the builder with `python3 -c "import ast; ast.parse(open(f,encoding='utf-8').read())"` before executing, and expect to iterate 1-2 times on CJK string hygiene even for a clean-looking script.

## 3. `write_file` / `patch` lint output is stale after a fix

After `patch` fixes a syntax error, the lint section of the `patch` response may still report the ORIGINAL line/column error ("Pre-existing lint errors - this edit didn't introduce new ones"). Do not chase it - re-lint with `ast.parse` via terminal, which is authoritative.
