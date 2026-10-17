---
source_url: https://sunshowers.io/posts/anthropic-mononoke/
ingested: 2026-10-17
sha256: 39a6c4ced5edf4ee12e384ab659c0f16b5586ebfc96bed59a917cf50fdfda6ea
---

# Anthropic's Scion is heavily inspired by Mononoke

Author: Rain (sunshowers.io) | Date: 2026-10-14 (followup 2026-10-15)

Anthropic announced its new version control system, **Scion**, describing how it uses a
concept called "derived data" to make operations like `blame` more efficient. Rain (a former
Meta Mononoke engineer) compared Anthropic's Scion write-up to his own 2022 Oxide candidate
materials describing how the **Mononoke** source control server (built at Meta, 2017-18)
uses the same "derived data" concept for the same blame-efficiency goal.

Key claims:
- The level of imitation "goes well beyond having similar insights."
- Scion credited Sapling only for "hard-won lessons" and did NOT mention Mononoke at all —
  which Rain says "borders on plagiarism."
- The post reads as if Anthropic/Claude designed all this, when the reality is the Meta team
  came up with many of the insights that "Claude dutifully applied almost a decade later."
- Rain does NOT have a problem with Anthropic copying Mononoke's design (it is open source,
  deliberately, "to benefit humanity through the spread of good ideas").

The general thesis (the durable point for the wiki):
- As LLMs assist in designing new systems, they index heavily on existing designs. Mononoke is
  open source and in every LLM's training set. Ask Opus 5.5 or GPT-6 Astra about prior art and
  both immediately point out the similarities to Mononoke.
- "Giving credit to those that came before us is now easier — and more important — than ever.
  There is no longer an excuse."
- Points to Vicent Marti's Cursor blog post as an example of a system with similar insights but
  many key design differences.

HN discussion: 425 pts (part 1, item 50094694), 253 pts (part 2 followup, item 50106738).
