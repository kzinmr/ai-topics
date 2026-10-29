# getsuperintel / Superintel+ — 403 + no-inbox-summary body recovery

**When to use**: A beehiiv newsletter from the **Superintelligence / The Daily AI Briefing** family
(author Kim "Chubby" Isenberg) where **ALL** `link.mail.beehiiv.com/v2/c/...` tracking URLs return
HTTP 403 (expired tracking tokens) AND there is no same-day inbox pre-triage summary at
`~/wiki/raw/inbox/newsletter-ingest/`. The skill's default fallback is subject-line-only assessment;
this technique recovers enough real body text to make a proper `take`/`reference`/`skip` call instead.

## Why it works

The publication's article content is hosted at **`read.getsuperintel.com`**. Unlike the token-gated
`link.mail.beehiiv.com/v2/c/` redirect chain, the direct article page returns **HTTP 200** even when
the post slug is wrong (every wrong slug served a 251KB generic fallback titled
"Superintelligence — The Daily AI Briefing"; the *correct* slug serves the real ~720KB paywalled post).
The correct slug is derivable from the newsletter subject line: slugify it (lowercase, spaces to hyphens,
strip the leading emoji and punctuation).

## What the 200 page exposes (despite `isAccessibleForFree: false`)

1. **JSON-LD `description`** — a full 2-3 sentence thesis of the article (the single most useful field).
   Also gives `headline`, `datePublished`, `author.name`, `author.url`
   (`.../authors/kim-chubby-isenberg`).
2. **~10-14 free-preview `<p>` paragraphs** inside `<article>` — the pre-paywall intro, which for
   Superintel+ typically contains all the concrete, dated, citable facts (numbers, quotes with source
   attribution like "(OpenAI, 10/23/2026)", incident timelines). This is usually enough to confirm a
   genuine wiki gap and set `body_excerpt`.
3. **"In Today's Issue:" paragraph** — the TOC of section headings. Use it to classify the *other*
   `v2/c/` links (which still 403) as section anchors of the same topic, mark them `skip` with a
   body_excerpt quoting the TOC, rather than treating each 403 link as an unknown.

## Reproduction script (cron-mode safe: write_file to /tmp + terminal, NOT a heredoc)

```python
#!/usr/bin/env python3
import subprocess, re
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
# derive slug from subject: emoji-off, lowercase, spaces->hyphen, drop punctuation
slug = "the-offline-world-openai-now-trains-its-frontier-models-inside-a-copy-of-the-web"
u = f"https://read.getsuperintel.com/p/{slug}"
h = subprocess.run(["curl","-sL","--max-time","25","-A",UA,u],
                   capture_output=True, text=True, timeout=35).stdout or ""
print("LEN", len(h))
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.DOTALL):
    if 'headline' in m:
        print("JSONLD:", m[:1500]); break
art = re.search(r'<article.*?</article>', h, re.DOTALL)
body = art.group(0) if art else h
paras = [re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',p)).strip()
         for p in re.findall(r'<p[^>]*>(.*?)</p>', body, re.DOTALL) if len(p) > 40]
print("NP", len(paras))
for p in paras[:60]: print("-", p[:400])
```

**Sanity check on the fetch**: LEN ~720KB with headline matching the subject = real post (free preview
present). LEN ~252KB titled "Superintelligence — The Daily AI Briefing" with no `description` about the
subject = wrong-slug fallback, fix the slug and retry once. Do NOT trust a fallback page's body.

## Domain map (canonical)

| Domain | Type | Direct `/p/` behavior |
|--------|------|-----------------------|
| `getsuperintel.com` | Framer marketing site | 404, never resolve here |
| `getsuperintel.site` | beehiiv canonical posts (uid=386) | works, but token-gated for some uids |
| `read.getsuperintel.com` | article content domain (uid=443/505/509/839) | **200, free-preview body, use this** |
| `link.mail.beehiiv.com/v2/c/...` | tracking redirect | 403 once token expires (~12-24h) |
| `email.beehiivstatus.com/.../hclick` | status pixel | skip, zero content |
| `hp.beehiiv.com/<uuid>` | hosted boilerplate | skip (TOS etc.) |

## Validated case (2026-10-25, run 20261025T101550Z, uid=839)

Subject "📴 The Offline World: OpenAI Now Trains Its Frontier Models Inside a Copy of the Web".
All 18 `v2/c/` links 403; no inbox summary. Direct-slug fetch on `read.getsuperintel.com` returned a
721KB page: JSON-LD description + 14 free-preview paragraphs carried the whole story (9/20 CACHE_MISS /
BrowseComp / DNS-resolver leak incident; 10/23 OpenAI "All of our frontier RL runs use this offline mode
of interaction"; the same-company builds+grades+reports the practice-ground thesis). Cross-checked the
wiki (no `CACHE_MISS`/`cached copy of the web`/`no internet access` hits;
`concepts/ai-agent-safety-incidents.md` covered only the July NanoGPT escape + Irregular, not this
Sept-Oct thread) → genuine gap → `take` as `events/2026-10-23-openai-offline-frontier-rl-2026`.
Remaining 403 links classified as TOC section-anchors → `skip`. Paywalled beyond the preview → flag
for downstream full-body re-fetch.

## Paywall note

`isAccessibleForFree: false` here is the publication default; the free preview is genuinely useful, so
capture it, mark `paywalled` if you save a raw article, and qualify beyond-preview claims ("preview
suggests…"). Don't let the flag cause an auto-skip.
