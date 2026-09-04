# AI Weekly / True Positive Weekly — publication identity (pub 61455)

Validated 2026-08-06 newsletter-triage.

## Identity mapping
- Inbox/checkpoint `source_name`: **"AI Weekly (@aiweekly)"** — misleading label (source-name trap)
- Actual publication: **True Positive Weekly by Andriy Burkov** (publication_id=61455, aiweekly.substack.com)
- Class: pure link digest / book-promo channel → per `inbox-summary-link-digest-trap.md`, verify the canonical post body before accepting an inbox "high"/"critical" classification

## Book-promo trap (Aug 2026 concrete case)
- Subject: "Exclusive Early Access: Chapters 1-3 of The Hundred-Page Deep Reinforcement Learning Book"
- Inbox classification: "high" (reason: "educational resource ... relevant for wiki concept pages on deep reinforcement learning")
- Body verification sequence:
  1. `open.substack.com/pub/aiweekly/p/{slug}` → ~1.3KB redirect stub (canonical URL in `<title>`)
  2. Canonical `aiweekly.substack.com/p/{slug}` → post HTML with only **3 substantive `<p>`**: author greeting, "Here's your exclusive early access chapters 1-3 of my upcoming The Hundred-Page Deep Reinforcement Learning Book", and the paywall gate "Subscribe to True Positive Weekly to keep reading". 0 external links.
- Verdict: **skip** — paywalled book promo with no technical content; DRL concepts already covered in wiki
- Signal words: "Exclusive Early Access", "Chapters 1-3", book title in subject + coupon / `utm_source=paywall` redirects → book promo, not news
- `redirect/2/eyJ...` OAuth links (coupon/paywall `next=` URLs) unresolvable outside email session — skip immediately

## Reuse
- Any future candidate labeled "AI Weekly" → treat as True Positive Weekly; read the canonical post body (aiweekly.substack.com) before trusting inbox classification; expect a paywall gate or a link-digest bullet list.
