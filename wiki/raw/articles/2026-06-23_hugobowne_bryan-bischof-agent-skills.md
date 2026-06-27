---
type: article
date: 2026-06-23
source: https://hugobowne.github.io/show-us-your-agent-skills/agent-skills/guests/bryan-bischof/
author: Hugo Bowne-Anderson
tags: [agent, agent-workflows, agent-skills, bbplot, eval-driven-charts]
---

# Bryan Bischof — Show Us Your Agent Skills (EP 02 Guest Dossier)

**Bryan Bischof** · Theory Ventures · BBPlot · Eval-Driven Charts · Grammar of Graphics

Bryan is designing the grammar of graphics for the agent age. BBPlot packages the human's intent inside the chart spec, generates variants where the ask is ambiguous, and lets a separate eval repo decide what features to build next. He only steps in at the end to say a chart looks bad; the evals do the rest.

## Key Principle

> "What would be the grammar of graphics for the agent age?"

This is the question BBPlot is Bryan's answer to.

## Scoreboard — BBPlot Principles

- **RATCHET**: never advance until it does. never get worse
- **K > 1**: ambiguity yields variants, not one premature answer
- **PINNED**: the eval repo is not allowed to read BBPlot's code
- **GAPS**: the goal isn't a high score. it's information about gaps
- **LINT**: a feature with no demonstrated example fails the build
- **EYES**: the human's only job: the final "this chart looks bad"

## Package Context with Content

> "You'll ask for one change, and it will somehow manage to completely break the chart."

Everyone who has iterated on a chart with an agent knows this. Bryan's diagnosis: the human's intent lives in the chat, so it gets lost. His fix is to write that intent into the chart itself — the spec records both how to draw the chart and why, so the next turn can't forget.

Then he does something clever: **BBPlot** is the chart tool. **BBPlot Eval** is a second, walled-off project that hands fresh agents a target chart and asks them to recreate it using only BBPlot's public examples. Wherever they fail, that's a missing feature. He builds it, and a rule keeps the tool honest: each version can stall, but it can never score worse than before.

## The Seven Principles (from eval-driven-charts write-up)

1. Turn every failed chart eval into a library feature
2. Package context with the chart — intent lives in the spec, not the chat
3. K > 1 — ambiguity yields variants, not one premature answer
4. The eval repo is pinned; it cannot read BBPlot source code
5. The goal is information about gaps, not a high score
6. A feature with no demonstrated example fails linting
7. The human is only the late backstop: "this chart looks bad"

Write-up: https://github.com/hugobowne/show-us-your-agent-skills/tree/main/workflows/eval-driven-charts

## Evals Find the Gaps — The Failure-to-Feature Loop

1. **Distrust your guesses about agents** — "As a human, I don't actually know what agents want." Don't design the DSL from intuition; measure what fresh agents can actually build.
2. **Pin the package, hide the code** — "In BBPlot Eval, you are not allowed to look at BBPlot's code." The eval agent works from the gallery, the same path an outsider would.
3. **Write eval cards, predict the failures** — Each card has a target, prompt, requirements, failure funnels, and predicted ways the agent could screw up.
4. **Generalize the failure into a request** — "Feature requests to BBPlot are developed by generalizing failures on specific evals." Fix the class, never the one chart.
5. **Ratchet the version forward** — "We're not allowed to move forward until we have continually ratcheted. We're not always getting better, but we're never getting worse."
6. **Be the late backstop** — "I don't really know what's good. What I do know is what charts would be great, and I can be a very late backstop on this chart looks bad."

> "This is intense." — sethtam, on Discord, during the live demo

## Keeping Agents Honest

- **eval-driven-charts**: The full write-up of the BBPlot / BBPlot Eval loop: seven principles, the session shape, anti-patterns, and what you need to run it yourself.
- **Scene graph**: BBPlot emits a scene graph so a rendered chart can report what overlaps what. "You care about what's on the chart, but also where they are and how they relate."
- **Gallery (executable docs + feature matrix)**: Every feature is demonstrated with a spec and an image, linted for. "And yes, it's YAML. Deal with it."
- **Traces (notes after failure)**: "No, you screwed up again. Make yourself a note," then he reviews the note. Local DuckDB stores every trace and iteration.

> "Like all great movements in technology or politics, I started with a manifesto."

Its first rules: "a chart spec should enumerate how to render the chart and what context has been provided by the human," and "every choice that's been made explicit by a human should be codified in the spec."

## The Stack

- **Cursor** — the two-repo loop
- **DuckDB** — local trace store
- **Matplotlib** — the fragile baseline
- **ggplot2** — the name riff
- **Midjourney** — the K>1 pattern
- **D3** — where his chart taste began

## Key Insight

> "BBPlot is not for humans. BBPlot is for humans plus agents."

Which changes what docs are: a gallery of specs and rendered images, the only thing the eval agents may read. A feature with no demonstrated example fails linting.

## Links

- YouTube segment: https://www.youtube.com/watch?v=l37PR-OkYKA&t=5095s (01:24:55)
- Full episode 02: https://www.youtube.com/watch?v=l37PR-OkYKA
- Eval-driven-charts write-up: https://github.com/hugobowne/show-us-your-agent-skills/tree/main/workflows/eval-driven-charts
- Bryan's GitHub: https://github.com/BBischof
- Theory Ventures: https://theoryvc.com/team-members/bryan-bischof
- Full field notes: https://github.com/hugobowne/show-us-your-agent-skills/blob/main/episode-field-notes/ep-2/bryan.md

## Footer

© 2026 Hugo Bowne-Anderson · Show Us Your Agent Skills · Bryan debuting BBPlot: "this is the first time I've shown this to anyone, so we're gonna give it hell"
