import os, re
from collections import defaultdict

wiki = '/opt/data/ai-topics/wiki'
dirs = ['entities','concepts','comparisons','queries','events']
pages = {}  # key -> (path, links)
link_re = re.compile(r'\[\[([^\]|#]+)')

for d in dirs:
    for root, ds, fs in os.walk(os.path.join(wiki,d)):
        if '_archive' in root: continue
        for f in fs:
            if not f.endswith('.md'): continue
            p = os.path.join(root,f)
            key = os.path.relpath(p, wiki)[:-3]
            try:
                content = open(p, encoding='utf-8', errors='replace').read()
            except: continue
            body = re.sub(r'```.*?```','',content,flags=re.DOTALL)
            links = [l.strip() for l in link_re.findall(body)]
            pages[key] = (p, links)

# resolution: match by full key or basename
by_basename = defaultdict(list)
for k in pages: by_basename[os.path.basename(k)].append(k)

inbound = defaultdict(set)
broken = defaultdict(list)
for k,(p,links) in pages.items():
    for t in links:
        t2 = t.split('/')[-1] if '/' in t else t
        # try exact-ish resolution
        cands = []
        if t in pages or (t+'.md' and any(kk==t for kk in pages)): cands=[t]
        if t in pages: cands.append(t)
        elif t2 in by_basename: cands = by_basename[t2]
        if cands:
            for c in cands:
                if c != k: inbound[c].add(k)
        else:
            broken[t].append(k)

# hub index pages excluded from orphan consideration
orphans = []
for k in pages:
    base = os.path.basename(k)
    if base in ('_index','index'): continue
    if not inbound[k]:
        orphans.append(k)

print("total pages walked:", len(pages))
print("orphans (excluding _index hubs):", len(orphans))
cr = []
for k in orphans:
    p,_ = pages[k]
    n = len(open(p,encoding='utf-8',errors='replace').read().split('\n'))
    if n >= 50: cr.append((k,n))
cr.sort(key=lambda x:-x[1])
print("content-rich orphans (>=50 lines):", len(cr))
for k,n in cr[:15]: print(f"  {k} ({n} lines)")
print()
print("broken link targets:", len(broken), "refs total:", sum(len(v) for v in broken.values()))
for t,srcs in sorted(broken.items(), key=lambda x:-len(x[1]))[:20]:
    print(f"  [[{t}]] -> {len(srcs)} refs (e.g. {srcs[0]})")
