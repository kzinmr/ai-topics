---
title: "AI-Generated Code Should Be Open Source"
type: concept
created: 2026-11-16
updated: 2026-11-16
tags:
  - open-source
  - copyright
  - code-generation
  - ai-coding
  - developer-tooling
  - controversy
sources:
  - raw/articles/2026-11-16_jankiewicz_ai-code-open-source.md
  - https://news.ycombinator.com/item?id=50507303
---

# AI-Generated Code Should Be Open Source

A normative position, argued most visibly by Jakub T. Jankiewicz in "All AI-generated code should be
Open Source" (November 15, 2026; HN 1174 pts / 621 comments — among the largest AI-code-policy
threads of 2026): because frontier models were trained on scraped open-source and
CC-attribution-required code (Stack Overflow/Exchange), turning model output into proprietary code
is **"license laundering"**; and because purely AI-generated code lacks human authorship, it should
not be copyrightable at all (US: the Monkey Selfie precedent, cited by the U.S. Copyright Office;
Wikimedia Commons already tags purely AI-generated images Public Domain). Since copyright differs
by jurisdiction (the UK grants limited protection to computer-generated works), the author concludes
AI-generated code should be released under an OSI license or dedicated to the public domain via
CC0 — including "prompt-only" code where humans contribute little beyond the prompt.

## The counter-arguments that shaped the HN thread

- **The copyrightability + licensing contradiction.** If output is uncopyrightable, an "open source
  license" is legally vacuous — a license is an agreement not to sue for copyright infringement
  ([ubercow13], [dboreham]). Replies: licenses still do real work (liability allocation, [zulban]),
  and code can be "made open by publication" regardless.
- **Open source's value was never availability, it was human validation.** "[J]ust OSSing generated
  code has no value. Open source is human-validated code" ([sturza]); [pasquinelli] — you could
  always "generate infinite code"; the point of reading source is to see what the software actually
  does.
- **Derivative-work escalation.** Anything based even in part on GPL'd training data is already
  derivative, so *all* LLM-output-derived code should be open ([g-b-r]) — a stronger claim than the
  post's own.
- **The premise may not survive courts.** Multiple commenters flagged the Copyright Office position
  as unsettled; the whole argument currently rests on an unsettled non-copyrightability premise
  ([dboreham]).
- **Public-good framing.** Software increasingly behaves like a public utility, needing governance
  rather than licenses ([cyanydeez]).

## Wiki placement

This is a distinct normative claim from the adjacent wiki threads — [[concepts/open-source-ai]] and
[[concepts/open-source-ai-must-win]] are about *models* being open, and
[[concepts/open-weights-licensing-tightening]] tracks vendors tightening model licenses; this page is
about *AI-generated code* (the output side). Related legal precedent pages:
[[concepts/anthropic-copyright-settlement]] (training-data side), [[concepts/ai-music-copyright]],
[[concepts/open-source-licensing]].

## Related

- [[concepts/open-source-ai]] — the open-model position
- [[concepts/open-source-ai-must-win]] — manifesto-level open-source argument
- [[concepts/coding-agents/coding-agents]] — the practice whose output is at issue
- [[concepts/open-source-licensing]] — licensing mechanics
- [[concepts/anthropic-copyright-settlement]] — training-side copyright precedent

## Sources

- Jakub T. Jankiewicz, "All AI-generated code should be Open Source" — https://jakub.jankiewicz.org/blog/ai-code-open-source/
  (raw: `raw/articles/2026-11-16_jankiewicz_ai-code-open-source.md`)
- HN discussion: https://news.ycombinator.com/item?id=50507303 (1174 pts / 621 comments)
