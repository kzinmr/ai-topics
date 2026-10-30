---
title: "LLM Voice"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags:
  - ai-slop
  - content-quality
  - ai-transparency
  - writing
  - ai-detection
  - epistemology
  - transparency
sources:
  - raw/articles/martinfowler.com--bliki-llm-voice--b7d2c1a4.md
related:
  - concepts/ai-slop
  - concepts/model-collapse-of-viewpoints
  - concepts/llm-assisted-writing
  - concepts/ai-content-transparency
confidence: high
---

# LLM Voice

**LLM Voice** is Martin Fowler's 2026-10-29 bliki term for the recognizable
stylistic signature of LLM-generated prose — and, more importantly, for the
*human* reaction it provokes. Fowler's central move is to relocate the problem
from detection tooling to reader trust: "The reaction to LLM-Voice is a human
one, that sense that we are in an uncanny valley of prose. By the time I'd
reach for a tool to tell me what I'm reading, it's already too late, even if it
confidently tells me there's no LLM present."

Source: [Martin Fowler, "LLM Voice", martinfowler.com bliki, 2026-10-29](../raw/articles/martinfowler.com--bliki-llm-voice--b7d2c1a4.md)
(HN: 492 points / 259 comments, 2026-10-29).

## Core claims

1. **The tells are not the folklore ones.** Fowler explicitly excludes em-dashes
   and names "load-bearing tapestries" instead — i.e. the failure is rhetorical
   density and metaphor-deployment, not surface punctuation.
2. **Detection tools miss the point.** His skepticism is twofold: accuracy doubts,
   plus the deeper objection that the reader's revulsion *is* the signal, and it
   arrives before any classifier does.
3. **Author self-assessment is unreliable.** He tests his own intuition against
   the classic "old man yells at new slang" failure mode: he bristles at "adopting
   a new sales motion" and "a sharp round-up of news", but has heard those from
   human mouths — so that is generational drift, not carbon-vs-silicon. This
   self-suspension is what separates the concept from generic slop-shaming.
4. **Drafting is the trap.** The operational recommendation is narrow and strong:
   do **not** let an LLM write a draft. "Even if it's edited by a human, it's very
   hard to expel the LLM-Voice." Accepting rephrasing suggestions is called
   *dangerous*. Outline-and-structure assistance "may be ok, but only as far as an
   outline." The prose must be filled in by the author.
5. **Counterexample, honestly recorded.** Footnote 1 admits one known case of a
   fully LLM first draft with no detectable LLM Voice — but only after a
   professional editor at a major periodical cleaned it up. This bounds claim 4 as
   "very hard" rather than "impossible".

## The thinking argument

Fowler's strongest claim is instrumental, not aesthetic: writing is
"an almost-essential tool for thinking", and "it's only by writing something down
that I can really get my thoughts on a topic into coherence." Delegating prose to
LLMs therefore delegates comprehension:

> "As more people delegate writing to LLMs they will also delegate thinking and
> comprehension to LLMs."

He also inverts the usual utopia: "In time it may be that LLMs will be so good
that we can't tell the difference. In many ways, that's more worrying." Undetectability
is treated as the *bad* outcome because it removes the reader's defensive signal.

## Legitimate exceptions

Fowler's rule is a default, not an absolute, and the exception list is the part
most summaries drop:

| Case | His position |
|---|---|
| **Jim Highsmith (collaborator)** | Uses LLMs to beat Parkinson's-law procrastination. "I'll gladly deal with LLM-Voice in order to continue imbibing my old friend's wisdom." |
| **Translation for non-native English authors** | Practically valuable, but he'd "prefer rather a genuine human's clunky prose to the smooth but soulless LLM." |
| **Form letters / reports nobody reads** | Reasonable to delegate. Michael Nygard's framing: you are "communicating with a process rather than a human. A human may open the envelope but that person is acting as a component in a cybernetic organism." |
| **Documentation read only by LLMs** | Speculates LLM readers "won't have my uncanny valley worries." |

## Disclosure policy

Fowler's site-level rule: anyone using AI to help write **must declare how** they
used it, usually in the acknowledgments — partly for transparency, partly so
readers can learn useful patterns. The article itself closes with "I did not use
AI or LLMs in any way while writing this post", alongside nine named human
draft-commenters. Fowler's own sole permitted use is as a **search tool**, with
every fact verified against the source.

## Why it matters for this wiki

- It supplies a **named concept** for the reader-side experience of
  [[concepts/ai-slop]], which is mostly discussed as a volume/productivity problem
  rather than a stylistic register problem.
- It connects to [[concepts/model-collapse-of-viewpoints]] as the *micro* analogue:
  model collapse describes homogenization of the corpus, LLM Voice describes
  homogenization detectable in a single artifact.
- It is a counterweight to pure-detector framing in [[concepts/ai-content-transparency]]:
  the paper-and-pen test is a human reader, not a classifier.
- Fowler's "say your writing is" practice (speak the sentence internally, write it,
  edit it) is a concrete alternative workflow, in the spirit of
  [[concepts/llm-assisted-writing]]'s human-led patterns and [[concepts/technical-writing]].

## Open questions

- Is the "load-bearing tapestries" tell stable across languages, or an
  English-language / blog-register artifact? Fowler's own generational-drift caveat
  applies to him but is not measured for others.
- The claim that LLM-Voice survives human editing is anecdotal (one negative
  control, and that one required a professional editor). No base rate is offered.
- Fowler's disclosure norm is site-level. What it would take to become a venue-level
  or platform-level norm (cf. [[concepts/ai-content-transparency]]) is unaddressed.

## Related pages

- [[concepts/ai-slop]] — volume-side framing of the same phenomenon
- [[concepts/model-collapse-of-viewpoints]] — corpus-level homogenization
- [[concepts/llm-assisted-writing]] — human-led writing patterns
- [[concepts/ai-content-transparency]] — classifier approaches Fowler distrusts
- [[concepts/ai-content-transparency]] — disclosure norms
- [[entities/martin-fowler]] — author
- [[concepts/technical-writing]]
