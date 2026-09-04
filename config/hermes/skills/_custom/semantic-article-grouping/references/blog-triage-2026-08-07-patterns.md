# Blog Triage Patterns — 2026-08-07 (20 decisions: 3 takes / 2 refs / 15 skips)

Validated Aug 7, 2026 blog-triage run (14 candidates + 6 unsaved_articles). Two patterns refine
existing rules in the main SKILL.md.

## Pattern 1: Unsaved court-filing PDF CAN be a take — exception to the unsaved_articles rule

The general rule ("`unsaved_articles` should not generate `take` decisions... mark as skip with
`body_excerpt: （unsaved_articles — 抽出不可）`") has a real exception:

**When the unsaved item is a public court filing** (courtlistener/PDF) with a specific, verifiable
title, and it fills a documented **event-page timeline gap**, rate it ★★★★☆ `take` with
`candidate_wiki_path` = the event page. Downstream wiki-ingest can fetch the PDF to verify.

Concrete case (Aug 7, 2026): Daring Fireball linked "OpenAI Files 28-Page Motion to Dismiss Apple's
Lawsuit (PDF Link)" (courtlistener URL, docket gov.uscourts.cand.474095). `events/openai-apple-conflict-2026.md`
had `updated: 2026-08-05` and its timeline ended Aug 4 (preliminary injunction stage). The Aug 6
motion to dismiss was a genuine same-story development — the "fresh updated date ≠ full coverage"
pattern. A blanket skip would have left the event page one legal step behind.

Decision logic that justified take instead of skip:
- Title states a specific, checkable legal fact (28-page motion to dismiss, named court)
- The PDF is public record — downstream can fetch and verify (unlike paywalled media)
- The target page is an existing event page whose timeline terminates before this date
- `body_excerpt` honestly marks the item as unsaved/PDF and flags the downstream fetch step

Contrast — still skip: Gurman's OpenAI hardware device article ("doughnut-shaped speaker over $300",
Bloomberg) is AI-relevant but paywalled with no verifiable body → skip, but note for future tracking.

## Pattern 2: Event covered in company entity ≠ author's opinion piece on that event is covered

When a leadership/company event is already documented in the **company entity page**, an author's
analytical/opinion piece ABOUT that event is still a genuine take **for the author's entity page** —
the author's thesis is a separate intellectual contribution, not a duplicate of the event record.

Concrete case: Aug 5, 2026 Google DeepMind leadership change (Hassabis → Chairman/Alphabet CSO,
Kavukcuoglu → SVP, Jeff Dean departure) was already fully covered in `entities/deepmind.md` and
`entities/demis-hassabis.md` (log lines confirmed prior processing). Gary Marcus's Aug 6 post
"Seven reasons I wouldn't count Google out" — a contrarian survival thesis (data scale, TPUs, $402B
revenue/$132B profit, distribution, Hassabis staying, competitors' troubles, multi-way-tie-outlast
argument) — was absent from `entities/gary-marcus.md` (updated 08-01). Rated ★★★★☆ take → new section
on the author's entity page.

Checklist: (1) confirm the EVENT is covered (grep company entity), (2) confirm the author's entity
lacks the specific THESIS (grep author entity for the argument), (3) if the author page is missing
the argument → take for the author entity, not skip. Complements the existing "opposing thesis from
same author" variant — here the event itself is already covered elsewhere; the gap is the author's
framing.

## Yield note

20 decisions: 3 takes / 2 refs / 15 skips (75% skip). Consistent with the higher-take mixed-batch
composition (opinion + editorial + security-misc mix); all takes were entity/event-page updates, no
new pages. Archive landed at the canonical path via the `.hermes/home` symlink shim — do not "fix"
the nested-looking archive_path (see `archive-commit-targeted-git-add.md`).
