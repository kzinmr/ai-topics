---
title: "Open-sourcing our docs and the agents that maintain them"
source: "Warp Blog"
url: "https://www.warp.dev/blog/open-sourcing-our-docs-and-the-agents-that-maintain-them"
scraped: "2026-05-10T01:27:58.486650+00:00"
lastmod: "2026-05-04T15:34:44.000Z"
type: "sitemap"
---

# Open-sourcing our docs and the agents that maintain them

**Source**: [https://www.warp.dev/blog/open-sourcing-our-docs-and-the-agents-that-maintain-them](https://www.warp.dev/blog/open-sourcing-our-docs-and-the-agents-that-maintain-them)

Engineering
Open-sourcing our docs and the agents that maintain them
Hong Yi Chen
May 4, 2026
Today, we’re moving our product documentation at
docs.warp.dev
onto a stack we control end-to-end, and open-sourcing it at
github.com/warpdotdev/docs
.
This is the same drive that led us to
open-source the Warp client
: we want to build closer to our community. We want the surfaces around Warp to be readable, forkable, and editable by anyone who cares enough to send a PR.
Docs felt like the obvious next step. They’re the surface every developer eventually lands on when learning Warp, debugging an issue, or trying to understand what the product can do. But we were using a hosted setup that made it harder than it should have been for our own team, let alone our users, to make changes.
Also, docs are no longer just for humans. They feed the context layer behind Warp Agent through RAG, which means our documentation is part of how the product understands itself. If the docs are stale, incomplete, or hard to maintain, that affects both the reader and the agent.
So, we decided it was time to adopt a new documentation system – one that’s easy to maintain, contribute to, and shape over time. This led us to
Astro
+
Starlight
as a base. All documentation lives as Markdown on GitHub, with options to customize and embed UI elements in code.
Once that was decided, it was time to migrate.
An afternoon prototype, then a week to make it real
The first 80% shipped in a single afternoon.
At our
company-wide hackathon in March
, a small group of us and a swarm of cloud agents had three hours to migrate the entire docs site from our existing system to Starlight. We used Warp to generate a migration script and workflow, kicked off a handful of cloud agents, one per top-level section, and went to lunch.
By the time we got back, every page had been ported. Callouts had been converted. Video embeds had been fixed. Seven PRs were sitting in GitHub, ready for review. That was the easy part.
The remaining 20% was the part that always takes longer than you think: SEO metadata,
llms.txt
for agent consumption, redirect maps for old URL paths, theming polish, broken-link sweeps, dark mode parity, and the API reference. None of it is particularly hard on its own. There is just a lot of it.
That phase ran as a side project over the last week, with one or two of us supervising long-running agents. Across the migration, we spun up roughly
285 cloud-agent tasks
. Some were scoped to a single page. Some bulk-rewrote frontmatter across the site. Some handled tedious work like rebuilding redirect maps. We mostly steered while the agents did the typing.
We’ve also been prototyping an internal orchestration flow where agents can kick off subagents to parallelize larger projects like this.
The receipts:
217
commits across the repo
64 PRs opened, with 55 merged and the rest either closed or still in-flight
About 141K lines added and 59K removed across 5,185 file changes
Roughly 285 cloud-agent runs
We cleaned up the repo before rolling it out publicly, but the migration itself was very real.
Two things stood out by the end:
First, treating documentation as code dramatically changes the scope of what you can do. You can run scripts. You can stage changes in branches. You can review diffs. And more importantly, you can ask an agent to do all of those things too.
Second, supervising 285 small tasks does not feel like 285 times the work. Once the rules, templates, and skills are written down, the marginal cost of the next task gets much closer to zero.
What’s in the box
The new stack is mostly off-the-shelf, with a few pieces of custom glue:
Astro
and
Starlight
for the site framework. Markdown and MDX in, static site out. Everything is versioned in Git like any other code project.
Vercel
for hosting and edge middleware. We get preview deployments per PR, performance metrics, and a real CDN.
Scalar
for the API reference at
docs.warp.dev/api
. It reads our OpenAPI spec directly from the repo, is beautifully styled out of the box, and is also open source.
Kapa
for the on-site Ask AI widget. That’s the little “Ask” button in the top right. We’d love to power this with our own
Oz cloud runners
in the future, but for a one week migration, this did the job.
Our own telemetry pipeline.
Every page event flows into the same analytics stack the rest of Warp uses, so we can understand how the docs are actually being read instead of relying on a vendor dashboard.
A markdown-everywhere pipeline.
Every page has a .md twin you can curl. Those pages feed Warp’s own RAG pipeline, so the in-app agent has the same context as a human reader. They also power llms.txt for every other agent on the internet.
The non-obvious win is control.
We can change anything: the layout of a page, the shape of the sidebar, how search behaves, what telemetry we send, and how agents consume the content. The whole repo is about 314 markdown pages, plus the components and styles that render them. None of it is hidden behind a UI we cannot inspect or modify.
It also let us fully migrate off one of our existing SaaS vendors, saving thousands of dollars a year.
The agents keeping it alive
The fun part, and the reason we’re publishing the repo, is what runs on top of it.
There are 20 versioned skills under
.agents/skills/
that we use as the standard library for working on the docs. Some run on a schedule. Some run on every PR. Some run on demand when we ask. They all live next to the content they operate on, with prompts, rules, and tools checked in.
A few of the useful ones:
PR review on every change
.
A GitHub Action runs an Oz agent against every incoming PR. It reads the diff against our style guide, flags things like missing frontmatter, drifting voice, or cross-references pointing at renamed pages, and posts inline comments. None of it blocks a merge, but all of it catches things that otherwise could have shipped to production.
A changelog agent
.
When a new stable Warp release ships, an agent fetches the release notes and opens a PR adding them to the public changelog. It creates a direct line from the codebase to the docs.
Codebase syncing.
A scheduled agent looks for new platform error codes
in our server and
client repos
, then writes the missing error pages, sidebar entries, and redirects.
Another agent reads through internal code changes
and updates the corresponding feature docs. These are Oz agents running on Warp’s cloud-agent platform, helping the docs follow the code automatically.
Broken-link and redirect sweeps
.
A periodic agent walks the site, finds things that have rotted, and opens a PR with the diff before anyone files an issue.
SEO and AEO audits
.
Two agents work the long tail. One crawls our live sitemap for technical SEO issues like duplicate titles, missing meta descriptions, and malformed H1s. Another researches emerging agent-answer-engine queries we should be writing about.
Authoring skills.
A
draft_*
family handles the boring parts of creating a new page: scaffolding it from the right template, pulling source-code context, and matching our style guide so the first draft is closer to mergeable.
During the migration alone, this fleet ran roughly 285 cloud-agent tasks and reviewed every one of the 64 PRs that landed against the repo.
The point is not that the docs write themselves. They do not. The point is that the docs are now a living surface, and no longer require a person to babysit every small update. The team that owns the surface is small. The surface is large; agents close the gap.
We did not invent this
Hosted docs vendors do many of these things out of the box. They have for years: PR previews, link checking, search, analytics, AI Q&A, and more.
If you are picking a docs platform from scratch and you do not particularly want to operate one, you should probably buy one.
What we wanted was different. We wanted to see how far a small team and a fleet of agents could carry a real production project, end to end, in a few days. The answer is: pretty far.
Far enough that what looked like a multi-week migration turned into a hackathon plus a side project. Far enough that what looked like permanent maintenance overhead turned into a handful of skills checked into the repo.
What’s next, and how to help
The repo is at
github.com/warpdotdev/docs
. The skills are under
.agents/skills/
. The PR review action is in
.github/workflows/
.
Clone it. Read it. Fork it. Copy anything useful.
We’d love your help. The docs cover a lot of ground, and plenty of pages are still stale, missing, or not as good as they could be.
If you spot something:
Open an issue if you want us, or an agent, to take a look.
Open a PR if you have ten minutes and want to fix it yourself. The agents will review it before we do.
Tell us what is missing. There is an entire backlog of pages we have not written yet.
Open-sourcing the client was about inviting the community into the product. Open-sourcing the docs is the smaller, easier sibling of that move, but it matters for the same reason.
The best version of these docs is one we are not writing alone.
—
A huge thank you to Ben Holmes, Petra Donka, Rachael Renk, and Danny Neira for their contributions to this effort, from the migration and implementation work to the content, design, and launch polish that helped get the new docs live.
Related articles
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
Mar 16, 2026  ·  9 min
Building Computer use for Cloud Agents
Imagine you're on your phone and a teammate messages you: the onboarding flow is broken after the latest deploy, the signup form isn't validating inputs, the progress bar is stuck, and the confirmation screen doesn't…
