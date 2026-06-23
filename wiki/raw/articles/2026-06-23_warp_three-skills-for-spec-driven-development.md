---
title: "Three skills you need for spec-driven development"
source: "Warp Blog"
url: "https://www.warp.dev/blog/three-skills-for-spec-driven-development"
scraped: "2026-06-23T06:00:28.942822+00:00"
lastmod: "2026-06-23T01:40:03.000Z"
type: "sitemap"
---

# Three skills you need for spec-driven development

**Source**: [https://www.warp.dev/blog/three-skills-for-spec-driven-development](https://www.warp.dev/blog/three-skills-for-spec-driven-development)

Engineering
Three skills you need for spec-driven development
Zach Lloyd
June 11, 2026
If you want to increase the chances of your agent building the right thing, you should be writing specs to guide the agent.
It’s pretty simple: write product specs that describe user behavior, and tech specs that describe implementation strategy. They should be written as MD files and checked into the implementation PR so your teammates can review them.
You should use Skills for encoding this whole process.
Here’s the flow. It works inside or outside of Warp and is all
open-sourced to adapt as specs for your projects
.
1. Start with a product spec using
/write-product-spec
This Skill creates a PRODUCT.md file in a specs/<issue> directory in the current repo.
The goal of the PRODUCT.md is to specify a feature from the user’s perspective. It’s the “what” of the feature.
It should include references to Figma mocks, screenshots, etc.
The format is user stories plus a very detailed list of product invariants that an agent can verify in code and potentially using computer use.
2. Next create a tech spec using
/write-tech-spec
This Skill creates a TECH.md file in the same specs directory.
The goal of the TECH.md is to specify the implementation strategy for the feature. It’s the “how” of the feature.
It should include overall architecture guidance, specific code locations, and anything else that the agent should know when writing the code.
3. Ask the agent to implement the specs
This should work with any agent, even on a lower reasoning level.
4. Validate the implementation matches the specs
It’s not enough to ask an agent to implement specs, you also need to make sure it did it correctly.
When reviewing the implementation PR, I use a skill in Warp for this called
/validate-changes-match-specs
that asks the agent to double check its work and respond back with any inconsistencies.
The agent then walks me through those inconsistencies and how I want to address them.
5. Validate using computer use
Finally, we have a specific skill we use internally for using Oz to do computer use to validate UX changes.
You can find these skills
on GitHub
and install them using:
npx skills add warpdotdev/common-skills
Related articles
Jun 18, 2026  ·  1 min
Generate interactive PR Walkthroughs with a single Skill
While we’re waiting for someone to re-invent Github I put together a useful skill that can help folks better understand agent (or human) generated PRs.
Jun 16, 2026  ·  4 min
How to build a self-improvement loop for your Skills
There’s been a lot of chatter about using “loops” lately to drive agents, and I think this has been accompanied by a bit of “what actually is a loop”?
Jun 2, 2026  ·  6 min
Why we tore down our no-code site and went back to code
Our marketing site sees over 10 million visitors a year. This past week, we launched a brand-new version — rebuilt from scratch so agents can work on it as fluidly as humans do.
