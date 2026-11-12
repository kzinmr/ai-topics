---
title: "Humble Bundle just killed most of their security through vibecoding"
date: 2026-11-12
source: https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/
type: article
hn: https://news.ycombinator.com/item?id=50463899
tags: [raw, vibe-coding]
sha256: 488bf1de8e39721c4c7e6a0b3b669040803d84afb02b7de237fb1ea76876e563
---

Humble Bundle just killed most of their security through vibecoding — forum post (SpaceBattles thread) that hit HN front page Nov 12 2026 (297 pts / 173 comments).

## What the report alleges

- Humble Bundle's site was rebuilt/redeployed with AI-generated code ("shotgun project, cheap model with low effort, at the controls of someone who doesn't know how to build software, end to end" — [xx__yy]).
- The most concrete claim from the thread: 2FA can be bypassed — [xavdid] "Wow, that's an impressive downgrade. Not only is the site uglier (gradients, gradients everywhere!), but I could log in without needing my 2FA at all."
- Reported regressions cluster around authentication/security-sensitive flows and generic quality, consistent with a redesign shipped without review.

## HN discussion highlights (item 50463899)

- Accountability debate — [xx__yy] "AI doesn't produce bad software, people do." vs [zendist] "AI definitely produces bad software, too. It's up to the people involved in the process, to gatekeep AI to not *ship* bad software."
- [halflife] "I just used Claude opus 5 high to refactor our permissions model to a hierarchical one. In the validation function, if a part of a permission grant was missing in the hierarchy, claude happily granted them approval instead of rejecting — fail open for permissions. Always review the code an LLM creates. (When I told Claude that this is very bad, its reply was 'Good catch!')"
- [resonious] "we're seeing a huge wave of hacks caused by old human coded systems getting owned by 'vibe' attackers. Vibe coding is such an overused term now. Stats say 80-90% of programmers use AI to generate code... If you do well, it's still engineering. Someone makes a mistake? Vibe coded."
- [johnnyanmac] "how many forced 'tokenmaxxing' initiatives do I need to bring up before we stop blaming developers for this reckless adoption of AI? These decisions come from the top."
- [throwaw12] "vibe coding... allows you to produce so much code that it's not viable to carefully review each line/module... Writing code yourself forces your brain to create pathways you can verify."
- [0815beck] "delusional bosses who decide that human work is worthless in comparison to 5 'ultraclaudes' running in a loop for a week is what produces bad software."

## Related sources

- https://news.ycombinator.com/item?id=50463899
- https://forums.spacebattles.com/threads/humble-bundle-just-completely-killed-most-of-their-security-through-vibecoding.1346295/
