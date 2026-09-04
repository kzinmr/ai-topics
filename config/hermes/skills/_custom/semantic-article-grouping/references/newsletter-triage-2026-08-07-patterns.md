# Newsletter Triage 2026-08-07 Patterns

Session: 5-newsletter batch (2026-08-06/07). 3 takes, 5 references, 5 skips (13 decisions). Takeaways below.

## beehiiv uid=470 (Superintel+, Kim Isenberg) — resolved 200 with full body ~15h after send

Second counter-example to the expired-token-403 rule (first was uid=443, ~18.5h). The "Google Shakeup" issue (20 tracking links, sent Aug 6 19:00 UTC) resolved **HTTP 200 with the full 68-paragraph article body** when triaged Aug 7 ~10:21 UTC.

- Source label in raw newsletter frontmatter: `source_label: "uid=470"`.
- Publication: **Superintel+** (Kim Isenberg, "The Signal" style daily). Distinct from uid=386 (getsuperintel.site) and uid=443 (read.getsuperintel.com Superintel+) — this uid's links resolve straight to the hosted post with full body, no paywall interstitial.
- Procedure that worked: curl Link 1 directly (`curl -sL -A UA`), extract `<article>`/`<p>` paragraphs → 68 paras, 13.3K chars of content including the full GEM, Anthropic-silicon, and Muse-escape sections.
- Reinforcement: for previous-day beehiiv, ALWAYS test one link before assuming 403 batch. Age alone is not the discriminator (15-18h links have resolved 200 twice now).

## Archive script printed a nested path — but it was a symlink, not the expanduser pitfall

`archive_triage.py newsletter --keep-reference` printed:
```
"archive_path": "/opt/data/.hermes/home/ai-topics/wiki/raw/archived/triage/newsletter/2026-08-07_20260807T102155Z.json"
```
This LOOKS like the known `os.path.expanduser("~/.hermes")` nested-path pitfall, but it was **not** mis-saved. Verification:
```bash
readlink -f /opt/data/.hermes/home/ai-topics   # → /opt/data/ai-topics  (symlink)
ls -la /opt/data/ai-topics/wiki/raw/archived/triage/newsletter/  # canonical file present
```
`/opt/data/.hermes/home/ai-topics` is a defense-in-depth symlink to the canonical repo (per AGENTS.md PATH TRAP note). **Do not "fix" the archive when the printed path contains `.hermes/home/` — run `readlink -f` first.** The archive_index.json also updated in place. Targeted commit (`git add archive_index.json <dated>.json` + commit + push) worked cleanly.

## TPW #172 — second validation of the pure-link-digest overrating pattern

Inbox pre-triage summary rated True Positive Weekly #172 as **"high"** with 5 actionable links (PostHog agent autonomy, WeatherNext, Guardian Anthropic-books, Vicki Boykis local models, Flint). Body verification killed it: **11 paragraphs, 942 chars total** — a pure bullet list of article titles with 1-line descriptions, zero editorial analysis. All items → skip (pattern from `inbox-summary-link-digest-trap.md` #166 re-validated with #172).

- The inbox `actionable_links` for TPW #172 looked compelling (PostHog agent-autonomy framework, Anthropic copyright controversy) — the trap is that a pure digest's LINKS are valuable-sounding even though the DIGEST adds no editorial value. If one of those links is genuinely wiki-worthy, it will arrive via another pipeline (blog/RSS); do not force a take from the digest itself.
- WeatherNext 2 did get reference'd separately via the AINews issue (full-body coverage there) — confirming the "wait for the substantive source" strategy.

## SemiAnalysis "payload over recap" — already-covered recap + NEW analytical payload = take the payload

"Gemini is Cooked but GCP is Cooking" (pub 6349492, Dylan Patel) recaps the Google DeepMind reorg (Hassabis→Chair, Kavukcuoglu→SVP, Dean/Ghemawat/Quoc/Vinyals→Discovery Loop) — **already fully covered** in entities (demis-hassabis, deepmind, discovery-loop, jeff-dean, koray-kavukcuoglu) from an earlier AINews issue. But the article's institutional analysis was a genuine gap:
- Gemini 3.5 Pro **silently canceled**, 3.6 Flash as bridge model (8th/9th place)
- Gemini 1P API token growth deceleration: 60% (1Q26) → 38% (2Q26); Gemini ARR $12B (2Q26)
- GCP growth 82%; TPU system sales ~$35B/GW to external SPVs; >20% of TPU shipments 3Q26-4Q27 to Anthropic
- Thomas Kurian's internal political win (compute allocation)

**Pattern**: when a semi-analytical article wraps an already-covered event, check whether the *analysis/data payload* (model cancellations, financials, market structure claims) exists in the wiki. Recap → skip; payload → take (here: enrich `concepts/gemini/index.md` + `entities/semianalysis.md`). SemiAnalysis full body was accessible via `newsletter.semianalysis.com/p/<slug>` custom domain (37+ paras, no paywall for this post despite `isAccessibleForFree` ambiguity) — consistent with the semi-analysis-paywall-patterns intermittent access finding.

## Full-body extraction efficiency note

For AINews (swyx pub 1084089), the custom domain `www.latent.space/p/<slug>` returned the FULL body (126 paras) while `open.substack.com/pub/swyx/p/<slug>` returned only a ~1.3KB redirect stub (title = canonical URL with `?triedRedirect=true`). Same for `newsletter.semianalysis.com` vs `open.substack.com/pub/semianalysis/...` and `www.bensbites.com` vs open.substack. **Rule: prefer the publication's own custom domain for body extraction; open.substack.com is the stub/redirect fallback.** (Consistent with `substack-redirect-stub-title-discovery.md`.)
