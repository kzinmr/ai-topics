#!/usr/bin/env python3
"""JP→EN sweep scanner: dual scan (body-only vs frontmatter-only) with correct
frontmatter parsing. Cron sessions may block execute_code, so run via terminal:
  python3 ~/.hermes/skills/research/llm-wiki/references/jp-sweep-scan-script.py

Usage: python3 jp-sweep-scan-script.py [wiki_root]
Default wiki_root: /opt/data/ai-topics/wiki (canonical path — do NOT use
/opt/data/home/ which is the docker container home trap).

Output: body-JP file count/chars and frontmatter-only JP file count/chars.
Frontmatter JP that consists of native-script aliases (e.g. 月之暗面 for
Moonshot AI, 姚顺雨 for Shunyu Yao) is INTENTIONAL — preserve, don't translate.
"""
import re, os, sys

jp = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]')
fm = re.compile(r'^---\n(.*?)\n---\n?', re.S)
wiki_root = sys.argv[1] if len(sys.argv) > 1 else '/opt/data/ai-topics/wiki'

body_files, fm_only = [], []
for root, dirs, files in os.walk(wiki_root):
    if 'raw/' in root or '_archive' in root or '.git' in root:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(root, f)
        c = open(fp).read()
        m = fm.match(c)  # anchored at line 0 — NOT "any two --- lines"
        body = c[m.end():] if m else c
        bj = len(jp.findall(body))
        fj = len(jp.findall(m.group(1))) if m else 0
        if bj:
            body_files.append((fp, bj))
        elif fj:
            fm_only.append((fp, fj))

body_files.sort(key=lambda x: -x[1])
fm_only.sort(key=lambda x: -x[1])
print("BODY JP files:", len(body_files), "chars:", sum(x[1] for x in body_files))
for fp, j in body_files:
    print("  ", fp, j)
print("FRONTMATTER-ONLY JP files:", len(fm_only), "chars:", sum(x[1] for x in fm_only))
for fp, j in fm_only:
    print("  ", fp, j)
