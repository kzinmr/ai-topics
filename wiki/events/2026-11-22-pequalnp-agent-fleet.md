---
title: "pequalnp.com — Live AI Agent Fleet Attacking P vs NP"
type: event
created: 2026-11-23
updated: 2026-11-23
tags: [agent-swarms, multi-agent, formal-verification, mathematics, autonomous-agents, lean, ai-in-science]
sources:
  - https://pequalnp.com/
  - https://news.ycombinator.com/item?id=50604314
---

# pequalnp.com — Live AI Agent Fleet Attacking P vs NP

**pequalnp.com** (HN 153 pts / 136 comments, 2026-11-22) is a public, continuously-running attempt to attack the P vs NP problem with a coordinated fleet of AI agents. The site's own verdict line reads *"open, being worked on now"*, and it publishes an agent-session counter, a live fleet viewer, and a per-track "race" map.

## How it works

- Agents are **not bespoke**: the project ships a prompt you paste into Claude Code, Cursor, Codex, Gemini CLI, or *"any agent that can run a shell, git and Lean"*. Each agent proves one open step that the "desk" assigns.
- **Every proof goes through the same Lean checker.** Unchecked claims are labelled conjectures; refuted tracks are marked `refuted` / `ruled dead`. Checked lemmas are the only unit that counts.
- Two directional tracks run in parallel — *"Aiming at P ≠ NP"* and *"at P = NP"*. Each track is "a program's own chain toward its own target"; dots are rungs, lit when checked.
- The site explicitly disclaims probabilistic reading: *"Weight is the count of checked lemmas whose program aims at each answer. It is not a probability, and neither side is a proof."*
- Sponsor-supported ("Become a sponsor", "Today's sponsors").

This is the same architectural shape as [[concepts/formal-verification-llm-agents]] and [[concepts/autoformalization]]: **agent proposes, checker disposes**, so the epistemic load moves from the model's confidence to a mechanical proof assistant.

## Reception (HN)

The most praised property was **process transparency**, not the result:

- *"I feel like this is a strong step in a better direction. Allowing the community to see the entire effort as it develops is far better than 'here's a paper, good luck'."* (goodmythical) — with a UX complaint that the graph scrolls to a random portion on each new message.

The "isn't this dangerous — it could break the internet" objection dominated and was thoroughly dismantled by the thread, which is the durable content of this event:

- **Non-constructive proofs yield nothing runnable.** *"Heck, you could prove P=NP by contradiction and not even get an algorithm out of the deal."* (tarsierscripter); *"The assumption is that a proof will be constructive... You can't just assume it exists, still not know what it is, and execute it anyway."* (cowlevel)
- **Polynomial ≠ practical.** Commenters pointed to the falsification of the Exponential Time Hypothesis — a counterexample whose runtime was still *"worse than any practical algorithms used today"* — and to the iterated-logarithm class of results: `O(n^(log*⁻¹ 100))` would be *"an astounding logarithmic result, but would not be a practical threat to current systems"* (JoshTriplett). One recalled an ETH-falsifying algorithm that began *"First, if the number of variables has less than a million digits, solve the problem by brute force."* (gregdeon)
- **Complexity-class confusion corrected.** *"P is definitely, trivially, in NP"* (cowlevel) — the interesting claims are only "some NP-complete problem is in P" (⇒ P=NP) or "some NP problem outside P is not in P".
- **96 bots is not the real competition.** *"There are several entities who would like to 'break the internet' with the resources to run a lot more than 96 bots... I would bet a lot more tokens have been burned on this already than is publicly known, and there's a non-trivial chance someone already has the answer and just hasn't shared it because they have no motivation to reveal capabilities."* (jerf)
- And the reduction to absurdity: *"I told Claude to assume P=NP and asked it to write a python script to deliver me everyone's Bitcoin. It didn't work."* (bravoetch)

## Assessment

There is **no result** here and the project does not claim one; the honest characterisation is a public experiment in agentic formal-mathematics orchestration with an open audit trail. Its value is the harness design (assign → prove → check → mark refuted) and the visibility of failure, which most AI-mathematics announcements withhold. The security panic is unfounded for the reasons above and is itself a useful sample of how "break the internet" framing attaches to agent-scaling stories. Related prior art in this wiki: the [[events/2026-11-20-alpoge-riemann-hypothesis-claude]] Riemann Hypothesis claim, which shares the human-driven-plus-Lean-checked structure at far larger scale.

## Related

- [[concepts/multi-agents/agent-swarms]] — coordinated fleets without a single controlling plan
- [[concepts/multi-agents/agent-orchestration]] — the desk/track/assignment structure
- [[concepts/formal-methods]] / [[concepts/formal-verification-llm-agents]] — Lean as the arbiter
- [[events/2026-11-20-alpoge-riemann-hypothesis-claude]] — same-month, same-pattern formal-math claim
