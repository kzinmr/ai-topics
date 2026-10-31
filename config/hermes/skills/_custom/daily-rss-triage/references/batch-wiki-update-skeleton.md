# Batch Wiki Update Script Skeleton (verified 2026-10-30, trending-topics run)

Drop-in skeleton for the "Multi-File Wiki Batch Edits" section of SKILL.md. Compose
new page bodies with `write_file` to `/tmp/page_*.md` first; the script itself is
pure logic. Idempotent end to end — safe to re-run after a crash or compaction.

```python
#!/usr/bin/env python3
"""Idempotent batch wiki update — trending-topics YYYY-MM-DD."""
import hashlib, re, os, shutil
os.chdir(os.path.expanduser("~/ai-topics"))
TODAY = "YYYY-MM-DD"
results = []
def log(msg):
    results.append(msg); print(msg)

# ---------- 1. SCHEMA tag additions (do BEFORE pages exist) ----------
# Verify planned tags first:  for t in tags: terminal(f"grep -c -- '\\b{t}\\b' wiki/SCHEMA.md")
schema = open("wiki/SCHEMA.md").read()
adds = {  # 1-indexed line numbers — RE-VERIFY with `grep -n '^## ' / sed -n` before use;
          # sibling jobs append to these lines, so counts drift. Anchor on the label instead
          # if a line-number assert trips.
    32: "model-name-x, benchmark-y",       # Models (first)
    36: "new-infra-tag",                    # Engineering
    39: "new-meta-tag",                     # Meta
}
lines = schema.split("\n")
for lineno, newtags in adds.items():
    ln = lines[lineno - 1]
    assert ln.startswith("- **"), f"line {lineno} not a category line: {ln[:40]}"
    missing = [t for t in newtags.split(", ") if t not in schema]
    if missing:
        lines[lineno - 1] = ln.rstrip() + ", " + ", ".join(missing)
        log(f"SCHEMA line {lineno}: +{missing}")
open("wiki/SCHEMA.md", "w").write("\n".join(lines))

# ---------- 2. New pages: copy staged bodies ----------
for src, p in [("/tmp/page_foo.md", "wiki/concepts/foo.md")]:
    if not os.path.exists(p):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        shutil.copyfile(src, p); log(f"CREATED {p}")
    else:
        log(f"EXISTS {p}, skip")

# ---------- 3. Existing-page appends: REAL heading anchors ----------
# Before writing this block: terminal("grep -n '^## ' wiki/concepts/target.md")
p = "wiki/concepts/target.md"
s = open(p).read()
if "Unique New Section Title" not in s:
    anchor = "\n## See also"          # NOT "\n## Related" — many pages lack it
    assert s.count(anchor) == 1, f"anchor not unique in {p}"
    s = s.replace(anchor, "\n## Unique New Section Title\n\n" + body + anchor, 1)
    s = re.sub(r"updated: 2026-\d\d-\d\d", f"updated: {TODAY}", s, count=1)
    if "raw/articles/<rawfile>" not in s:
        s = s.replace("sources:\n", "sources:\n  - raw/articles/<rawfile>.md\n", 1)
    open(p, "w").write(s); log(f"UPDATED {p}")
else:
    log(f"{p} already has section, skip")

# ---------- 4. Raw files: placeholder hash, then dedicated re-hash pass ----------
# (write raw with `sha256: pending` in the same script, or in the fetch script)
for f in ["wiki/raw/articles/domain--slug--<8hex>.md"]:
    s = open(f).read()
    parts = s.split("---\n", 2)
    fm, body = parts[1], parts[2]          # hash ONLY this body string
    h = hashlib.sha256(body.encode()).hexdigest()
    if "sha256: pending" in fm:
        open(f, "w").write("---\n" + fm.replace("sha256: pending", h) + "---\n" + body)
        log(f"HASHED {f}")
    else:
        old = re.search(r"sha256: ([0-9a-f]+)", fm).group(1)
        if old != h:
            open(f, "w").write("---\n" + fm.replace(old, h) + "---\n" + body)
            log(f"RE-HASHED {f}")

# ---------- 5. index.md: insert after section _index anchor, bump counts ----------
s = open("wiki/index.md").read()
new_entries = {"concepts/foo": "[[concepts/foo]] — English one-line summary (JP trips language hook)"}
added = []
for key, entry in new_entries.items():
    if f"[[{key}]]" not in s:
        anchor = "- [[concepts/_index]] — Directory hub / overview for concepts pages"
        assert s.count(anchor) == 1, "concepts _index anchor missing"
        s = s.replace(anchor, anchor + "\n" + entry, 1); added.append(key)
if added:
    m = re.search(r"## Concepts \((\d+) pages\)", s)
    if m: s = s.replace(m.group(0), f"## Concepts ({int(m.group(1))+len(added)} pages)")
    m = re.search(r"Total pages: (\d+)", s)
    if m: s = s.replace(m.group(0), f"Total pages: {int(m.group(1))+len(added)}")
    open("wiki/index.md", "w").write(s); log(f"INDEX: +{added}")

# ---------- 6. log.md prepend with idempotent H1 dedupe ----------
entry = f"## [{TODAY}] <job> — <subject>\n- Created: ...\n- Report: `inbox/rss-scans/...`"
s = open("wiki/log.md").read()
if "<unique log subject line>" not in s:
    if not s.startswith("# Wiki Log"):
        s = "# Wiki Log\n" + s
    out, seen = [], False
    for ln in s.split("\n"):
        if ln.strip() == "# Wiki Log":          # .strip() — see SKILL pitfall
            if seen: continue
            seen = True
        out.append(ln)
    i = 1
    while i < len(out) and out[i].strip() == "": i += 1
    out = out[:i] + [entry.rstrip()] + out[i:]
    open("wiki/log.md", "w").write("\n".join(out)); log("LOG: prepended")
hdr = sum(1 for ln in open("wiki/log.md").read().split("\n") if ln.strip() == "# Wiki Log")
log(f"LOG header count = {hdr}")   # must be 1
print("\nDONE")
```

Then in terminal (scoped add only — never `git add wiki/` blanket):

```bash
cd ~/ai-topics && git add wiki/concepts/foo.md wiki/concepts/target.md wiki/SCHEMA.md \
  wiki/index.md wiki/log.md wiki/raw/articles/<files> inbox/rss-scans/trending-topics-YYYY-MM-DD.md \
  && git diff --staged --stat | tail -3 \
  && git commit -m "wiki: <job> YYYY-MM-DD — <summary>" && git push
```

Post-run gates: `git commit -m` passes both hooks when tags were pre-validated and
index prose is English; every `[[target]]` in new pages verified against
`cd wiki && find concepts entities -iname '*kw*'` before writing.
