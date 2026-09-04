# Blog Triage Patterns — 2026-08-09 (20 decisions: 4 takes / 4 refs / 12 skips)

Validated Aug 9, 2026 blog-triage run (16 candidates + 4 unsaved_articles). Three patterns
refine the main SKILL.md rules, all about "page exists" being a weaker signal than the
specific-claims test.

## Pattern 1: Curator link post as page source ≠ official source covered (depth gap → take)

The existing quote-post dedup rule handles "curator quotes another author's original work →
check the original author's entity page." The INVERSE also bites: when an entity page was
built FROM a curator's link post (Willison/Daring Fireball quoting an official announcement),
the official company blog may still be a genuine ★★★★☆ take because it carries
architecture/runtime details the curator post omitted.

Concrete case (Aug 9, 2026): `entities/muse-spark.md` had Muse Code / Muse Spark 1.2 sections
from Simon Willison's link post (Aug 6 triage) — announcement, pricing table, capability
positioning, "long-sequence agentic tool calling" observation. But the official
research.meta.ai blog ("Introducing Muse Code and Muse Spark 1.2") added content absent from
the entity page:
- Local event log runtime: every model call/tool run/approval/edit appended → replay-exact and
  restart-safe (agent resumes precisely after crash)
- Named async background agents (Photon Sphere, Embervault, Avo Lawn) that persist per-session
- Bundled skills: /plan (approval-gated plan), /grill (plan stress-test), /goal
- Self-improvement loop (Spark 1.1 generated environments, 1.2 graded solutions)
- Kernel optimization case study: KDA/MLA Triton kernels, 1,000+ tool calls over up to 24h,
  two-kernel pipeline (chunk-parallel prep + sequential inter-chunk scan)

Checklist: (1) confirm the TOPIC is covered, (2) grep the entity page for the official
source's SPECIFIC technical claims (runtime design, component names, eval methodology,
case-study numbers), (3) if those claims are absent → take for enrichment, even though the
same-day/past triage "already processed" the topic from the curator post. The topic-level
dedup (log line "Muse Spark 1.2 — skip, already processed") would have been WRONG here.

## Pattern 2: Incident-analysis two-target verification (event page + author entity page)

For link-post analyses of major security incidents (OpenAI accidental HF attack, Meta Muse
Spark breach), the content is often split across TWO targets and BOTH must be checked before
skipping:
- The EVENT page carries timeline rows (specific dates, attack-chain facts)
- The AUTHOR's entity page carries the analysis entry (their interpretation/framing)

Concrete case: `events/openai-huggingface-incident-july-2026.md` (updated 08-08) already had
the "May 7: OpenAI starts a new training run" timeline row (L208); `entities/simon-willison.md`
had the "Now we have a timeline... (Aug 7)" entry (L814) covering the Black Hat presentation
details (Artifactory message board, two zero-days, Linux kernel CVE exploit) AND Simon's RLVR
training-run interpretation. The Aug 8 link post was fully captured across the pair → skip.

The trap: grepping only ONE target (e.g., just the event page for "May 7") could miss the
author-analysis half, or vice versa. Grep for the specific date/claim in both the event page
AND the author entity page. This complements the "fresh updated date ≠ full coverage" rule —
here the event page was updated the same day, yet the analysis half lived in the author page.

## Pattern 3: Startup entity from announcement sources ≠ funding details covered

A company entity created from founding-announcement sources (X post, AINews newsletter,
official Google blog) frequently lacks the business-press follow-up: VC investors, board
seats, valuation, negotiation history.

Concrete case: `entities/discovery-loop.md` (created 2026-08-06, 81 lines) covered founders,
mission, GDM-exodus context — but had NO Khosla Ventures + Radical Ventures funding, Jordan
Jacobs board seat, Vinod Khosla's "AI is the researcher" framing, Pichai's retention
negotiation, or Google's year-1 compute arrangement. Wired's article supplied all of it →
★★★★☆ take for enrichment.

Checklist: for newly-created startup entity pages, check whether funding/investor details
exist before skipping business-press articles. Two-beat story ("departure → new company") has
a third beat: "funding round" — each beat is a separate coverage gap.

## Yield note

20 decisions: 4 takes / 4 refs / 12 skips (25% take — consistent with the higher-take
mixed-batch composition). All takes were existing-page enrichments, no new pages. Deduped
skips (3): OpenAI-HF timeline (Pattern 2), Meta Muse Spark breach (Aug 6 triage), Pichai
official message (already in discovery-loop.md sources + deepmind-family pages). Same-source
batch: 2 Anyscale/Ray articles both rated reference (concepts/ray.md) — vendor release
content at reference level.
