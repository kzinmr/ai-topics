# JP→EN Sweep Dual Scan Script (body-only, frontmatter-anchored)

Canonical scan for the JP→EN translation sweep — do NOT hand-roll the regex each run.

## Usage

```bash
python3 <skill_dir>/references/jp-sweep-scan-script.py [wiki_root]
# default wiki_root: /opt/data/ai-topics/wiki
```

Output:
```
TOTAL_FILES_WITH_BODY_JP=<N> TOTAL_BODY_JP_CHARS=<M>
<relpath>|<jp_count>|<abs_path>     # top 15, sorted by JP count desc
```

## What it gets right (hand-rolled scans get these wrong)

1. **Frontmatter anchored at line 0 only.** Files like `log.md` start with a
   `##` heading and contain horizontal-rule `---` later in the body — a naive
   "first two `---` lines anywhere" scan picks the wrong body boundary. If
   line 0 is not `---`, the whole file is body.
2. **Skips `raw/`, `_archive/`, `.git`** — raw sources are immutable and out
   of scope; archived pages are out of scope.
3. **Reports totals AND per-file counts** — lets you distinguish "backlog"
   from "one intentional file" in one run.

## Interpreting the output

- If the ONLY hit is `log.md` and it is byte-identical to HEAD
  (`git show HEAD:wiki/log.md | md5sum` vs `md5sum wiki/log.md`, or a Python
  string compare), the sweep is at natural end: the residual JP is append-only
  history (Japanese Discord hot-post topic titles quoted in English entries +
  sweep-end notes citing intentional multilingual aliases). Do NOT translate
  it, do NOT make a no-op commit. Report natural end + recommend
  disabling/retargeting the sweep cron.
- Genuine multilingual frontmatter aliases (e.g. `通义千问` for Qwen, `腾讯`
  for Tencent, `姚顺雨` for Shunyu Yao) are NOT backlog — preserve them.

## Full script

```python
import re, os, sys
jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
wiki_root = sys.argv[1] if len(sys.argv) > 1 else '/opt/data/ai-topics/wiki'
remaining = []
total = 0
for root, dirs, files in os.walk(wiki_root):
    if '/raw' in root or '/_archive' in root or '/.git' in root: continue
    for f in files:
        if f.endswith('.md'):
            fp = os.path.join(root, f)
            with open(fp) as fh: content = fh.read()
            lines = content.split('\n')
            body_start = 0
            if lines and lines[0].strip() == '---':
                for i in range(1, len(lines)):
                    if lines[i].strip() == '---':
                        body_start = i + 1; break
            body = '\n'.join(lines[body_start:])
            body_jp = len(jp.findall(body))
            total += body_jp
            if body_jp > 0:
                rel_path = os.path.relpath(fp, wiki_root)
                remaining.append((rel_path, body_jp, fp))
remaining.sort(key=lambda x: -x[1])
print(f"TOTAL_FILES_WITH_BODY_JP={len(remaining)} TOTAL_BODY_JP_CHARS={total}")
for p, j, fp in remaining[:15]:
    print(f"{p}|{j}|{fp}")
```
