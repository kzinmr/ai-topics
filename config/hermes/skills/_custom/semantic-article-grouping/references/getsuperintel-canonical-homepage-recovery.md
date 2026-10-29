# Superintelligence (getsuperintel.site) — Canonical-Homepage Recovery

Validated 2026-10-28 (newsletter-triage, uid=846 "Was Kimi's Hype Secretly Paid For?" + uid=848 "Axiom and OpenAI: Math Breakthroughs Go Daily").

## When to use

ALL beehiiv `link.mail.beehiiv.com/v2/c/...` tracking URLs from one or more Superintelligence newsletters return a Cloudflare "Just a moment..." challenge (HTTP 200, `<title>Just a moment...</title>`, ~7KB fixed-length body). Retrying does not help. The inbox pre-triage summary may be missing or stale. Do NOT drop to subject-line-only topic-level assessment — the full article body is recoverable via the canonical site.

## Procedure (cron-mode safe: write_file to /tmp + terminal)

1. **Fetch the archive homepage:**
   ```
   curl -sL -A "Mozilla/5.0 ... Chrome/126" https://getsuperintel.site/
   ```
   (~740KB, returns 200 with no challenge.) Homepage cards contain each post's subject-line title, date, read time, and a one-paragraph description — enough to map the day's newsletters to slugs.

2. **Extract slugs:**
   ```python
   re.findall(r'href="(/p/[^"]+)"', html)
   ```

3. **Fetch the article:** `https://getsuperintel.site/p/{slug}` — full body, JSON-LD `isAccessibleForFree: true`, ~54 `<p>` paragraphs, embedded 🔗 source links (the real curated URLs for take decisions).

## Pitfalls

- **Slug apostrophe normalization:** homepage title `Was Kimi's Hype Secretly Paid For?` → slug `was-kimi-s-hype-secretly-paid-for` (apostrophe becomes `-s-`). A guessed `was-kimis-...` returns the site shell with body text "Please check the URL in the address bar and try again." (~213KB, PARAS: 1 — easy to mistake for a real page; check the PARAS count).
- **Title-based slug guessing works** if you normalize: lowercase, strip emoji, `'s` → `-s`, `:` → `-`, spaces → `-`. When in doubt, scrape the slug list from the homepage rather than guessing.
- **`uid-{N}.beehiiv.com` and `uid-{N}.email.beehiiv.com` probes** return 404 / empty — do not waste calls; the `source_label: uid=NNN` in the raw newsletter frontmatter is not a usable hostname.
- **The homepage archive only lists recent posts** (~last 2 weeks). Older newsletters must fall back to subject-line assessment.
- Per-link Cloudflare variance still applies (skill's main guidance): if ONE tracking link resolves 200, resolve normally; the homepage trick is for the all-blocked case.

## Content characteristics (uid=846/848, Oct 2026)

- Daily briefing format: 3-5 top stories (emoji-prefixed), each with tl;dr, a deep-dive section, an "Economic Data/Chart" section, and 🔗 source links.
- Heavy overlap with AINews/Simon Willison-sourced events already in wiki (ETH refutation, GPT-6.1 Terra, Anthropic S-1) — cross-check `concepts/openai-eth-refutation-verification-crisis.md`, `entities/openai.md`, `entities/anthropic.md` before taking; the specialized value is usually concrete numbers the bulletin lacked (e.g., $450B cloud contracts, 43.1M Lean lines, $95B Meta cornerstone raise).
- Ad blocks (Wispr Flow, Levanta, goldcast) appear as paragraphs — filter.
