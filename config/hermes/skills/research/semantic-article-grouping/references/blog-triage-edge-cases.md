# Blog Triage Edge Cases

## Empty Raw Files (0 bytes)

The blog-ingest pipeline may save a raw file that is completely empty (0 bytes). This happens when:
- The scraper received an HTTP response but no body (e.g., 204 No Content)
- The URL redirected to a page the scraper couldn't parse
- The blog served a blank page with no article content

**Observed**: micahflee.com book recommendation (2026-05-21) — `read_file` returned `File not found` on the raw_path.

**Action**: Skip with reason `"empty file (0 bytes)"`.

## Bot-Wall / CAPTCHA Pages

Some blog articles return only a bot-protection page (Anubis, Cloudflare challenge, Turnstile, hCaptcha). These files are small (<600 bytes) and contain only the protection vendor's branding text.

**Observed**: xeiaso.net "Making sure you're not a bot!" (2026-05-21) — 471 bytes of "Protected by Anubis From Techaro. Made with ❤️ in 🇨🇦. This website is running Anubis version v1.25.0-51-gb57508a."

**Detection pattern**: Files under 600 bytes whose content contains only:
- `"Protected by"` + a bot-detection product name (Anubis, Cloudflare, etc.)
- `"Making sure you're not a bot"` or similar challenge text
- No substantive article body, headings, or paragraphs

**Action**: Skip with reason `"bot-wall page (no content extractable)"`. The URL itself may be a `/shitposts/` or `/challenge/` path — do not retry; the blog deliberately protects this path.

## Unsaved Articles (no raw_path)

The `unsaved_articles` array in the blog-ingest checkpoint contains URLs that the pipeline discovered (from the blog's RSS feed or sitemap) but could not scrape. These have `title`, `url`, and `blog` fields but **no `raw_path`**. Common causes:
- Paywalled articles (WSJ, NYT, Bloomberg)
- TikTok / social media posts
- URLs that returned a non-2xx status during scraping
- Content that was too short to save (sub-500B)

**Observed**: DaringFireball-linked WSJ article ("Google Unveils New Gemini AI Agent"), TikTok video, shkspr.mobi RSS Club post (2026-05-21).

**Action**: Cannot triage without content. Mark as `skip` with reason "unsaved (no raw content)". Cross-reference by title/URL against log.md to see if another pipeline captured the same content.
