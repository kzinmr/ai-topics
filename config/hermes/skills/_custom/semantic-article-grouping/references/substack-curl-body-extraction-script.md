# Substack post body extraction via curl (cron-safe, no web_extract)

Validated 2026-11-10 across 4 publications (importai, lenny, aibyaakash, simonw): all full bodies on first try, zero retries.

## Script (write_file → /tmp/extract_substack_bodies_YYYYMMDD.py → terminal python3)

```python
#!/usr/bin/env python3
import subprocess, re, json, os

posts = {
    "key1": "https://open.substack.com/pub/{handle}/p/{slug}",
    "key2": "https://importai.substack.com/p/{slug}",   # custom domain works too
}
out = {}
for key, url in posts.items():
    r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        url], capture_output=True, text=True, timeout=40)
    html = r.stdout or ""
    art = ""
    am = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
    if am:
        art = am.group(1)
    else:
        am = re.search(r'<div[^>]*class="[^"]*body[^"]*"[^>]*>(.*)', html, re.DOTALL)
        if am:
            art = am.group(1)[:400000]
    art = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", art, flags=re.DOTALL)
    paras = []
    for p in re.findall(r"<(?:p|h2|h3|li)[^>]*>(.*?)</(?:p|h2|h3|li)>", art, re.DOTALL):
        t = re.sub(r"<[^>]+>", "", p)
        t = re.sub(r"\s+", " ", t).strip()
        if len(t) > 40:
            paras.append(t)
    links = [l.split("?utm_")[0].split("&utm_")[0] for l in
             re.findall(r'href="(https?://[^"]+)"', art)]
    skip_x = ["substackcdn", "substack.com", "twitter.com", "x.com/", "fonts.",
              "enable-javascript", "beehiiv", "youtube.com/subscribe", "instagram"]
    ulinks = list(dict.fromkeys(l for l in links if not any(x in l for x in skip_x)))
    out[key] = {"url": url, "n_paragraphs": len(paras),
                "paragraphs": paras[:70], "external_links": ulinks[:40]}

os.makedirs("/tmp/nlout", exist_ok=True)
for k, v in out.items():
    json.dump(v, open(f"/tmp/nlout/{k}.json", "w"), ensure_ascii=False, indent=1)
    print(f"=== {k}: paras={v.get('n_paragraphs','?')} links={len(v.get('external_links',[]))}")
```

## Expectations learned (2026-11-10 run)
- `<title>` tag came back EMPTY for all 4 posts (client-rendered) — do NOT trust it for titles; use the checkpoint `source_name`/subject.
- JSON-LD (`application/ld+json` with `headline`) also returned `{}` for all 4, even fully-free posts — the `<article>`/`<p>` fallback is the real content path; don't spend extra passes on JSON-LD when both are in the same script.
- Yield per post: 18–163 paragraphs — enough for BODY-READING MANDATE compliance and for extracting curated external links (Import AI's 6 real links sat behind filtered substack redirect noise).
- Aggregator posts (AI by Aakash style) yield MULTIPLE triage decisions from one post: split by content section (sponsor / evals / news digest / deep dive), dedup decisions on `(item_id, title)` not URL since all sections share the post URL.
