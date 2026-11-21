---
title: "Cartesia Is Hiring a SWE to Raise an Army of Claudes"
source: "Cartesia Blog"
url: "https://www.cartesia.ai/blog/claude-army"
scraped: "2026-11-21T06:00:34.773017+00:00"
lastmod: "None"
type: "sitemap"
---

# Cartesia Is Hiring a SWE to Raise an Army of Claudes

**Source**: [https://www.cartesia.ai/blog/claude-army](https://www.cartesia.ai/blog/claude-army)

I recently came across Ramp’s blog on
building their own background coding agent
, which they call Inspect. It’s a great post, and for the engineering team at Cartesia, it felt timely as we think about how to scale AI coding agents’ productivity benefits across our team.
At Cartesia, we’ve fervently adopted coding agents. Across our team, we use Claude Code, Cursor, Codex, Copilot, Zed, Conductor, and more. In our monorepos, you can expect a review from Claude Code, Cursor BugBot, Vercel Agent, and Codex. The reviews surface varied, sometimes complementary, sometimes contradictory feedback that tangibly improves the quality of shipped code. BugBot is currently the favorite:
This is not the result of top-down mandates to adopt coding agents, just an outcome of organic excitement about ways to do better work faster and automate the boring parts as much as possible, combined with a willingness to spend whatever’s necessary to experiment.
Experimenting widely has made it easier to compare coding agents and experience advances at the frontiers. The playbook is being rewritten every few months.
But it’s felt like there’s something missing.
Writing code feels solved. But engineering is not.
Frontier models can do complex refactors and plumb code into high-traffic endpoints, and it often feels like they can see around corners. We’ve found that simple changes like putting your code in a monorepo create immense leverage, enabling agents to reason across system components and avoid subtle bugs. Review agents help close coding gaps. Writing the code is just not the bottleneck anymore.
But coding and engineering aren’t the same thing. A great engineer is not just plumbing code into a monorepo. They’re thinking about impact. They judge whether a feature is working, iterate based on real-world feedback, and keep going until the company’s goals are met.
This is where agents fall short. We used Opus 4.5 to safely remove a 10K+ line feature:
…but we still can’t ask it to understand whether a feature is getting traction in production and iterate, or get it to tie a spike in API latency to a line in our code.
The real bottleneck is broken feedback loops
Agents don’t fail because they can’t write code, they fail because they get stuck at practical boundaries: Opus 4.5 might successfully write A/B test code, but can’t check PostHog to see if the experiment worked, so it stops there. It might deploy a UI fix but can’t access Vercel preview to verify if it looks right. It could optimize a SQL query but can’t see production metrics to confirm the improvement.
This is where we see leverage: (safely) giving agents the right infra to iterate end-to-end. Access to repos, CI, previews, internal dashboards, PostHog data—whatever they need to judge success and failure the way a human engineer would.
The nice thing? This produces tangible benefits for humans too. If you make the CI run faster or make the end-to-end stack easier to spin up, human engineers onboard faster and stay more productive.
Creating leverage via coding agents is a strategic function
Engineers are often too focused on the problem at hand to think holistically about their developer experience. Tracking the frontier, experimenting with the latest tools, and productizing learnings internally is a full time job.
And the opportunity extends beyond engineering. We think that the same AI-native infra principles that unlock agent productivity for engineers can transform internal workflows across the company. GTM, business, and sales teams have a ton of repetitive work that can produce immense leverage if it’s properly automated.
This gap between agent capabilities and infrastructure won’t close on its own. It requires someone to actively design developer experience for both humans and AI.
We’re actively trying to solve this problem, and we’re hiring for an AI & Developer Acceleration engineer (as in, an engineer to accelerate the work that both AIs and developers do).
If you join us, you’ll write the playbook that lets both engineers and non-engineers go from problem to solution with minimal human intervention, and you’ll get to yell in public about it too. Reach out!
