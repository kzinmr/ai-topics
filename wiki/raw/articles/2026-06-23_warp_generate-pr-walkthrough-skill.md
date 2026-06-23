---
title: "Generate interactive PR Walkthroughs with a single Skill"
source: "Warp Blog"
url: "https://www.warp.dev/blog/generate-pr-walkthrough-skill"
scraped: "2026-06-23T06:00:31.007935+00:00"
lastmod: "2026-06-23T01:40:06.000Z"
type: "sitemap"
---

# Generate interactive PR Walkthroughs with a single Skill

**Source**: [https://www.warp.dev/blog/generate-pr-walkthrough-skill](https://www.warp.dev/blog/generate-pr-walkthrough-skill)

Engineering
Generate interactive PR Walkthroughs with a single Skill
Zach Lloyd
June 18, 2026
While we’re waiting for someone to re-invent Github I put together a useful skill that can help folks better understand agent (or human) generated PRs.
It’s called /pr-walkthrough and
it’s available here
.
Sh
npx skills add warpdotdev/common-skills --skill pr-walkthrough
What it does:
Takes a PR link as input (e.g.
https://github.com/warpdotdev/warp/pull/12518
, which I’m currently noodling on for Warp in my free time)
Creates an interactive website with plain HTML/CSS/JS and D3 for visualization. This UI walks through the key components of the change from four angles:
A system overview
– what are the major components?
The data flow
– what are the inputs and outputs?
Code dependency graph
– useful for seeing how the components relate
The user experience
– a step by step walkthrough of the user changes
It’s built using D3 and is interactive so you can explore the PR using a custom per-PR GUI.
It’s pretty easy and cheap to put this into CI and have a cloud agent like
Oz
run it for you.
If you want to generate visualizers for every PR, here’s a guide on how to set it up in CI using GitHub Actions + GitHub Pages to host the mini-site:
https://github.com/warpdotdev-demos/pr-walkthrough-ci
Would love feedback.
Contributions to the skill
are welcome!
Related articles
Jun 16, 2026  ·  4 min
How to build a self-improvement loop for your Skills
There’s been a lot of chatter about using “loops” lately to drive agents, and I think this has been accompanied by a bit of “what actually is a loop”?
Jun 11, 2026  ·  2 min
Three skills you need for spec-driven development
Use Skills to guide agents through product specs, technical specs, implementation, and validation so spec-driven development is repeatable and reviewable.
Jun 2, 2026  ·  6 min
Why we tore down our no-code site and went back to code
Our marketing site sees over 10 million visitors a year. This past week, we launched a brand-new version — rebuilt from scratch so agents can work on it as fluidly as humans do.
