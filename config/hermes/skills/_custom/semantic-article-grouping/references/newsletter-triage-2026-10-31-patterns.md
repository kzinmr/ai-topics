# Newsletter triage patterns — 2026-10-31 (run 20261031T101822Z)

3 newsletters: Robotic (Nathan Lambert, pub 48206), AI by Aakash (pub 5747120), beehiiv digest uid=860.

## Key patterns

1. **beehiiv v2/c/ same-day 403 is real (Cloudflare challenge, not token expiry)**: All sampled uid=860 links (L1, L2, L4) returned HTTP 403 with title "Just a moment..." within ~4h of send. Per skill: skip immediately, do NOT retry. With no inbox summary for the run (latest inbox file was 2026-10-29), assessed at subject level only → reference, never take. Subject "OpenAI Can Now Catch Its Own Rogue AI" maps to `concepts/rogue-ai-agent-activity.md`.

2. **Substack open.substack.com/pub/{pub}/p/{slug} direct curl works for both Robotic and aibyaakash** — full article `<p>` extraction (27 and 101 paragraphs). No JSON-LD body_html needed.

3. **Link-digest newsletters: evaluate body sections, not just curated links.** AI by Aakash is a link digest, but its body paragraphs contain the analyst's own financial breakdown (Anthropic $80.7B H1 loss, $72.4B non-cash; Q2 op profit $974M; 11,900 enterprise customers $100K+; $65B run rate vs ASML 14.5x/NVIDIA 16.1x). This was a genuine gap in entities/anthropic.md (which had S-1 filing + $965B/$2tn but no P&L breakdown) → take as existing-page update. The "pure link digest → skip digest" rule needs this nuance: take the digest when its own commentary carries unique numbers not in existing pages.

4. **Author entity page same-stance-different-evidence**: Lambert's Oct 25 podcast #20 section in entities/nathan-lambert.md already records his open-models-cyber stance, but the Oct 30 essay adds unique artifacts (verbatim Rob Wiblin / Project Glasswing / Zvi April quotes, Epoch AI Firefox exploit chain, bakery threat-actor metaphor) → take as author-entity enrichment, not skip.

5. Inbox summary directory reachable via symlink at /opt/data/.hermes/home/wiki/raw/inbox/newsletter-ingest/ (equivalently ~/wiki/raw/inbox/newsletter-ingest/).

## Yield
9 decisions: 2 takes (nathan-lambert enrich, anthropic IPO financials), 3 references (duet pattern page, gemini-4-carbon, rogue-ai), 4 batch skips. Archive: 6 new, 1 dedup.
