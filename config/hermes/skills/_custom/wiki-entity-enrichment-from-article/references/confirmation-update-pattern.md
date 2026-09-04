# Confirmation-Update Pattern (rumor → confirmed deal/incident)

When a topic that the wiki already covers as a **rumor / "in talks" / "exploring"**
gets **confirmed** by a primary source (official announcement, named acquirer, final
terms), do NOT leave the page stale and do NOT create a duplicate. This pattern
fired TWICE in one trending-topics run (2026-08-27): NVIDIA–Hugging Face $13B
("exploring a sale" → "agrees to acquire") and AWS–DuckLabs (DuckDB creators join
AWS). Both required editing pages that already existed from the earlier rumor.

## Core rule: PRESERVE the rumor history, layer the confirmation on top

Do NOT delete or rewrite the "exploring a $13B sale" paragraph. Instead:

1. **Rename the section heading** to reflect the confirmed state, keeping the date
   range intact. E.g. `## Exit / Sale at $13B+ (Aug 2026)` →
   `## Exit / Acquisition by NVIDIA at $13B+ (Aug 2026)`. This preserves the
   timeline without a destructive rewrite.

2. **Append a bolded confirmation sub-paragraph** immediately under the existing
   rumor paragraph (do not replace it):
   ```
   **Update — <Event> confirmed (<date>):** <the confirmed fact>. <HN link if it was a
   HN front-page story>. <why it matters, 1–2 lines>.
   ```

3. **Name the counterparty / confirmed figure explicitly** so a future reader sees
   the resolution without scrolling to the rumor.

## Add the confirmation source

- Bump `updated:` in frontmatter to the confirmation date (NOT the rumor date).
- Add the primary source URL to `sources:` (e.g. the Business Insider "agrees to
  acquire" article, the DuckLabs official announcement).
- **Add the acquirer's tag if missing** — e.g. HF page gained the `nvidia` tag when
  NVIDIA became the named acquirer. Validate the tag against SCHEMA before adding
  (see the standard pre-validation step).

## Caveat the headline ambiguity (verified 2026-08-27)

Press headlines are often imprecise about the deal stage. Business Insider's running
headline read **"Nvidia has been in talks to acquire Hugging Face for more than $13
billion"** even on the day HN reported it as a done deal. When the primary source
ambiguates the stage, note it:
> (Note: Business Insider's running headline reads "in talks to acquire"; the $13B
> figure is the consistent reported value. Treat final terms as pending definitive
> agreement until a formal announcement is published.)

Do NOT overstate a confirmed acquisition when the only evidence is a "in talks"
headline. This keeps the wiki honest and avoids a future "superseded" correction.

## When it's a NEW entity, not a confirmation

If the acquired side has NO existing entity page yet (e.g. DuckLabs was absent from
the wiki while DuckDB/HF were not), create a NEW `events/` page for the acquisition
event (the "who bought whom" story) rather than forcing it into a stale rumor page.
Use the **event page** because it's the consolidation story; link it from the
acquirer's and the technology's existing entity pages (e.g. AWS, Hugging Face) in
their "Related Entities" sections. Reuse already-valid tags (`aws`, `database`,
`open-source`) to avoid a SCHEMA pre-commit failure — no need to invent a `duckdb`
tag for a one-off event page.

## Related
- `arxiv-to-existing-page.md` — the general "append to existing page" pattern
- Standard pre-validation step (validate new tags against SCHEMA before write)
