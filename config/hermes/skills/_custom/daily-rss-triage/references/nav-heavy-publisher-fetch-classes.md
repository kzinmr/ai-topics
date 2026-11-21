# Nav-heavy publisher fetch classes (extends the vendor-blog marker-slice recipe)

Two distinct chrome classes hit in trending-topics runs, with different fetch signatures and different slicing recipes. Both go through the batched `fetch_sources.py` (Chrome UA + gzip sniff + strip_html).

## Class A: JS-rendered SPA (THIN result) — apiiro.com (VERIFIED 2026-11-08)

- **Signature**: `fetch_sources.py` prints `OK name: ~4000 chars` but the text is page chrome (`/Config` comments, SEO boilerplate, "Dynamic Page on <Vendor>"). Body is client-side rendered.
- **Do**: STOP — trailing-slash/URL variants return identical chrome, retries are wasted. Save the Algolia `/items/<id>` comment tree as the raw file instead (`type: hn-discussion` frontmatter, `source: https://news.ycombinator.com/item?id=<id>`). Vendor authors often post the full fact chain in their own HN replies. Label page content HN-thread-derived.
- Distinct trigger from the paywalled-source recipe (THIN/boilerplate vs 401/403), same fallback.

## Class B: Future-plumbing publishers (OK-length result, mostly chrome) — tomshardware.com (VERIFIED 2026-11-17)

- **Signature**: HTTP 200, prints `OK name: ~21,700 chars` — the fetch looks FINE, but the first ~6-8K chars are promo-code link lists, "Join the club" newsletter modals, and CSS-class garbage (`a]:text-inherit [&>a]:underline">`, `svg]:max-h-[var(--modal-logo...`). The real article body starts well after, and boilerplate (subscribe prompts, "Share this article", coupon blocks) **recurs AFTER the article**.
- **Do NOT**: treat as THIN/JS-rendered (it isn't — no URL-variant retries), and do NOT use an end-marker `find` (early duplicate match collapses the slice) or a naive end-marker `rfind` (post-article boilerplate is the last match, not the article boundary).
- **Recipe that worked**: START-marker slice with fixed length:
  ```python
  idx = text.find("<article lede / first body sentence>")  # lede visible in HN title or search snippet
  body = text[idx:idx+6000]
  ```
  Example (Claude Mythos / AMD story): lede "If AI can write the low-level code", `idx+6000` captured the whole fact chain including the Elangovan HIPify quote. Fixed-length slice is fine for raw/ + citation-grade quotes; check the tail reads like article prose, not boilerplate — if it tails into chrome, tighten the length.
- Same class likely applies to other Future plc sites (Tom's Guide, TechRadar, PC Gamer).

## General rule (both classes + Cohere/deepmind)

START marker = the article's opening sentence (visible in the HN story title / search-result snippet). End handling: `rfind` for a unique byline/author marker only when it does NOT occur in pre-article nav (Cohere "Written By Cohere Team" with `if e > 1000` guard); fixed-length slice when boilerplate repeats post-article (Future sites). Always grep the saved text for the expected opening phrase and treat a miss as FAIL, not OK.
