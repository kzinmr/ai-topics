# Blog Triage Patterns — 2026-11-21 (run_id 20261121T100039Z)

Validated outcomes: 18 candidates + 2 unsaved → 3 takes, 6 references, 2 batch skips. All candidate_wiki_paths verified on disk before commit (pre-commit validator enforced). Archive 8 items, commit 46d3af98.

## 1. Fast-following-announcement gap test (fresh event page ≠ complete event)

An `events/*.md` page created YESTERDAY for an announcement (Anthropic Nasdaq debut, created 2026-11-20, `updated: 2026-11-20`) still missed the NEXT-DAY development (IPO crash: $111→$97 close, premarket ~$88, SoftBank -14.5%, Nikkei -4%/week -6.8%, Taiwan index -16% week). Triage take = existing-page UPDATE (★★★★☆), not skip.

Test: does the existing event page contain the SPECIFIC numbers/phase the article is about? Fast-moving stories have multiple beats (announcement day → crash day → regulatory response). A page whose content ends at beat 1 has a genuine gap at beat 2 even though its `updated:` date is very fresh. This is the "fresh `updated:` date ≠ full same-day coverage" pattern extended to next-day beats.

Concretely, a same-author critic file (gary-marcus.md) had IPO-skepticism sections through Nov 18 but nothing on the actual crash; the event page had reception/valuation facts only. Both needed the crash data; the event page is the correct target (article is a market event record dressed as an opinion post — it opens with concrete prices, not thesis).

## 2. Same-day cluster split: quote-posts → reference, analytic essays → take

Three articles formed one event cluster (Levent Alpöge "Claude and I proved RH/GRH" simonw quote-post; Ravi Vakil "Masullo GRH is all human, no AI" simonw quote-post; borretti.me "Re: Riemann" humanist critique essay):

- Simon Willison quote-posts (<1.2KB, single quote + attribution) → reference, route to the existing topic page (`concepts/claude-fable-jacobian-conjecture.md` already covers Alpöge via Jacobian work) or author entity page. Do NOT take them individually.
- The substantive third-party analytic/critique essay in the same cluster (borretti, 5.5KB full argument with Ayn Rand / Diego Rivera framing) → reference with candidate_wiki_path = the same topic page, flagged for downstream to attach as corroboration when it processes the event. The pair (AI-accompanying proof vs human-only proof announcement) is the durable framing worth recording.
- Background explainers of the same cluster (johndcook GRH definition piece, math 101 content) → batch skip; the cluster's AI-scope value is fully captured by the quotes + critique.

## 3. Stale tracking-table detection in entity pages

`entities/ed-zitron.md` tracks his premium bubble series in a date|title|summary table — but the table's last entry was Jul 2026 while his bubble-series output continued. An article matching the series ("Premium: Bursting Bubbles", Nov 20) looked "already covered" by the table's existence. Correct move: check the table's most recent ROW date; if the article post-dates it, genuine take (append row + section). Series-tracked authors (Zitron, Hotz philosophy essays, Marcus) need this per-row freshness check, not page-existence check.

## 4. Unserved OpenAI News unsaved_articles — reference-not-skip when gap-verified

Both unsaved items (openai.com "Combatting adversarial distillation", "Hebbia with GPT-6 Astra" customer story) had zero extractable body, but grep confirmed real gaps: "adversarial distillation" appears only incidentally in 2 unrelated concept pages; hebbia.md exists but Astra-version results unverified. Decision: reference with `body_excerpt: "（unsaved_articles — 本文抽出不可。…）"` + a note telling downstream to fetch the body itself. Generalization of the existing court-filing-PDF exception: unsaved items CAN be reference decisions (not only skip) when (a) primary-source official blog, (b) grep-verified coverage gap, (c) title carries the full topic. Still never forced takes without body.

## 5. Quantitative-mechanism test for author-entity skips

Sean Goedecke has a 1100-line entity page with prior caching-adjacent essays ("software is slow because of bad design" mentions caching as a redesign tool). The new "Why output caching doesn't work" was still a take because it contributes an original quantitative mechanism (output token split: 50% reasoning / 44% tool calls / ~6% visible repetition; Amdahl bound → max 4% savings; expensive-models-cheaper effect). The test for prolific single authors: does the page contain the article's specific NUMBERS/MECHANISM, not just the keyword "caching"? Keyword-adjacent prior coverage ≠ mechanism coverage.

## 6. Batch-skip entry for heterogeneous non-AI batch (worked cleanly)

9 non-AI articles (oldnewthing×2, Diablo II history, Zigbee/HAOS, dfarq×2, Talk Show ep index-only, Krebs ransomware fraud indictment, Pluralistic book-review digest) collapsed into ONE skip decision with `|`-joined per-article excerpts (first sentence each) and a numbered reason_ja listing all 7 groups. Krebs security-indictment story is a skip only because it has zero AI/LLM element — do not take it just because the author is high-signal. Pluralistic digests with AI content only in the book-promo boilerplate (Doctorow's "Reverse-Centaur's Guide to AI" catalog line) → skip; the boilerplate is identical every issue.
