---
title: "Proxies for Expertise — How AI Counterfeits the Signals We Use to Judge Skill"
aliases: ["proxies for expertise", "legible skill signals", "counterfeit expertise"]
created: 2026-09-17
updated: 2026-09-17
type: concept
confidence: medium
tags: [ai-slop, ai-adoption, labor, epistemology, ai-commentary, controversy, methodology, ai-agents, agent-evaluation]
sources:
  - raw/articles/seangoedecke.com--ai-is-breaking-our-proxies-for-expertise--0af86730.md
  - raw/articles/arxiv-2606-05405-agents-last-exam.txt
related: [agent-slop, agents-last-exam, benchmark-ceiling, agi-declaration-controversy-2026, ai-engineer-worlds-fair-2026, ai-delegation-patterns, agent-human-oversight-failure]
---

# Proxies for Expertise

Every field judges skill by **legible artifacts** — a Fields Medal, a Fermat proof, a substantial GitHub repo, a benchmark score. Sean Goedecke's thesis (Sep 2026): frontier AI does not attack the skill; it attacks the *artifact*, producing convincing counterfeits at near-zero marginal cost. Once the artifact can be faked, the whole reputation circuit that allocated prestige, hiring, and funding breaks — and no field has yet built a replacement.

The page was referenced across the wiki for days without existing (see [[concepts/agent-slop]], [[entities/geoffrey-huntley]]); it is created here to close that broken link and to consolidate a claim set that was previously scattered across three pages.

## Goedecke's Mathematician Argument (the template case)

~5,000 mathematicians including 25 Fields medalists signed *"A Severe Misalignment of AI in Mathematics"*. Goedecke reads their complaint as structural, not Luddite ([raw](raw/articles/seangoedecke.com--ai-is-breaking-our-proxies-for-expertise--0af86730.md)):

- Math has two activities: **puzzle-solving** (legible, prestigious, hard to do) and **idea-generating** (the actual intellectual work, illegible to outsiders — is a "Goedecke set" a natural kind? nobody can tell for decades).
- Puzzles were an **un-gameable proxy**: solving them required generating new ideas, so the solution certified the idea's worth, and the prize made skill visible to outsiders.
- AI solves the puzzles "the hard way" — no intuitive new idea — so the proxy certifies nothing. **Goodhart's Law applied to prestige itself**: AI companies claim the medal's prestige without advancing the underlying goal.

## The Software Engineering Case (Goedecke's own field)

Same mechanism, different artifact:

| Old proxy | What it certified | Status (2026) |
|---|---|---|
| Substantial GitHub project (emulator, toy OS) | Engineering depth | Worthless — "everyone just assumes they're vibe-coded" |
| Weekend rewrite, thousands of LOC/day | Exceptional ability | Anyone with an OpenAI subscription |
| Benchmark / demo score | Agent capability | Scaffold moves same model 3%→60% ([[concepts/agents-last-exam]]) |
| Conference talk cited as evidence | Empirical grounding | Huntley: "we cite each other's talks at AI Engineer conferences as evidence enough" |

Goedecke's proposed exits: **silo** human vs AI work as chess and speedrunning did (human-only leagues keep prestige), or **find uncounterfeitable legible skills**. He rejects "LLMs are intrinsically incapable of idea-generation" — three straight years of such claims being falsified.

## Where This Wiki Already Measured the Same Break

The proxy failure is not one blogger's hunch; independent 2026 evidence converges:

- **Measurement**: ALE blind expert grading exists because agent self-reporting is uninformative; scaffold variance makes headline scores meaningless ([[concepts/benchmark-ceiling]] — depreciating benchmarks are where slop hides).
- **Market**: the [[concepts/agi-declaration-controversy-2026|AGI declaration]] is a CEO settling a scientific question via benchmark prestige whose currency is already devalued.
- **Human side**: [[concepts/ai-delegation-patterns]] documents users who stop reviewing outputs as confidence grows (abdication); [[concepts/agent-human-oversight-failure]] quantifies it — ~33% of dangerous agent actions approved by human gates (ScaleX, 409k decisions). Both are what happens when the *consumer* of the counterfeit artifact is also on an attention budget.

## Open Questions

- What uncounterfeitable signal replaces "I built X" for junior engineers whose skill formation depended on legible artifacts?
- Does ALE's blind-grading recipe generalize beyond benchmarks into hiring and funding, or does it only work where tasks can run on remote VMs?
- The "human league" exit assumes buyers care about provenance. Nothing in current market behavior supports that yet.

## Related

- [[concepts/agent-slop]] — the counterfeit *actions* this proxy failure rewards
- [[concepts/agents-last-exam]] / [[concepts/benchmark-ceiling]] — measurement-layer evidence
- [[entities/geoffrey-huntley]] — the insider-polemicist version of the same critique
- [[concepts/ai-engineer-worlds-fair-2026]] — the conference-citation loop under attack

## Sources

- Goedecke, Sean. ["AI is breaking our proxies for expertise"](https://seangoedecke.com/ai-is-breaking-our-proxies-for-expertise/) (Jul–Sep 2026). Raw: `raw/articles/seangoedecke.com--ai-is-breaking-our-proxies-for-expertise--0af86730.md`
- Sun et al., "Agents' Last Exam," arXiv:2606.05405 — via [[concepts/agents-last-exam]]
