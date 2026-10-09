---
title: "Association for Human Mathematics (AHM)"
created: 2026-10-09
updated: 2026-10-09
type: entity
tags:
  - organization
  - nonprofit
  - mathematics
  - ai-critic
  - ai-safety
  - ai-industry
  - ai-governance
  - openai
  - controversy
  - ai-commentary
confidence: medium
sources:
  - raw/articles/2026-10-07_ahmath_ahmath-statement-on-openai-math.md
  - raw/articles/2026-10-08_akaragila_openai-partition-principle-mathematics.md
  - raw/articles/2026-10-08_openai_openai-math-repo-history-withdrawals.md
related:
  - entities/openai
  - entities/deepmind
  - concepts/openai/formal-math-publication-2026
  - concepts/ai-mathematics-theorem-proving
  - entities/terry-tao
  - concepts/academic-reception-of-ai-math
aliases:
  - AHM
  - Association for Human Mathematics
  - AHM Communications Working Group
---

# Association for Human Mathematics (AHM)

The **Association for Human Mathematics (AHM)** is a mathematicians' advocacy group that organizes collective responses to AI companies' incursions into mathematical research. It rose to prominence with its **October 7, 2026 statement** condemning OpenAI's mass release of ~700 AI-generated math manuscripts — one day before the repo itself began withdrawing papers. ^[raw/articles/2026-10-07_ahmath_ahmath-statement-on-openai-math.md]

## Why it matters

The AHM statement is the sharpest articulation of the **academic-reception backlash** against frontier-lab "AI solves math" marketing. Its central charge is not that the proofs are wrong, but that the **publication model** is illegitimate:

> "Releasing over 700 files at once is not a demonstration of scholarship, but a demonstration of power."

Key claims from the statement:
- OpenAI **ignored the Advisory Group on Mathematics and AI**, whose initial position was that frontier labs *should not test advanced mathematical problems on internal models* at all. AHM reads this as "total disregard for the norms of scientific research."
- Mathematicians "did not ask for this work to be done," and AHM "reject[s] OpenAI's assertion that this release advances our subject."
- It urges mathematicians to **discontinue work with OpenAI** and "return to a vision of science that centers human understanding."
- It notes (with irony) that OpenAI is *simultaneously defending lawsuits* over plagiarism and copyright infringement. ^[raw/articles/2026-10-07_ahmath_ahmath-statement-on-openai-math.md]

## The timing detail

AHM's statement (Oct 7) was written **before** the withdrawal cascade became public. On **October 8** the `openai/math` repo's own `history.md` documented **three paper withdrawals** (the Weil-class / Kuga–Satake / Hodge-conjecture line, invalidated by a sign error) plus fixes to 14 more manuscripts. The next-day withdrawals retrospectively strengthened AHM's "not scholarship, but power" framing: the release was presented as settled progress and had to be partially retracted within 24 hours. ^[raw/articles/2026-10-08_openai_openai-math-repo-history-withdrawals.md]

## Positioning within the broader critique

The AHM statement is the **institutional** voice; set theorist **Asaf Karagila's** Oct 8 blog post is the **individual-expert** counterpart (see [[concepts/academic-reception-of-ai-math]]). Both converge on the same structural complaint — mass, low-context releases impose verification costs on a community that never requested them — while Terry Tao and the earlier 25-Fields-Medalist declaration represent a softer, "co-pilot" position. See [[entities/terry-tao]].

## Related

- [[entities/openai]] — the lab whose math release AHM condemned
- [[entities/deepmind]] — independent replication and the withdrawal of three related papers
- [[concepts/openai/formal-math-publication-2026]] — the 722-paper program AHM reacted to
- [[concepts/academic-reception-of-ai-math]] — how mathematicians as a community are responding
- [[concepts/ai-mathematics-theorem-proving]] — the technical arc AHM is critiquing from outside

## Sources

- AHM Statement on OpenAI's October 6 Release of Mathematical Documents — https://www.ahmath.org/statements
