---
title: "Why we tore down our no-code site and went back to code"
source: "Warp Blog"
url: "https://www.warp.dev/blog/why-we-tore-down-our-no-code-site-and-went-back-to-code"
scraped: "2026-06-10T06:00:24.958527+00:00"
lastmod: "2026-06-09T21:18:25.000Z"
type: "sitemap"
---

# Why we tore down our no-code site and went back to code

**Source**: [https://www.warp.dev/blog/why-we-tore-down-our-no-code-site-and-went-back-to-code](https://www.warp.dev/blog/why-we-tore-down-our-no-code-site-and-went-back-to-code)

Engineering
Why we tore down our no-code site and went back to code
Chris Muccioli
June 2, 2026
Our marketing site sees over 10 million visitors a year. This past week, we launched a brand-new version — rebuilt from scratch so agents can work on it as fluidly as humans do.
There was a brief window where going from Figma to a live website felt like a genuine shortcut. Drag, drop, publish. That window has quietly closed. Today, it’s often faster to build a page in code than it is to assemble one in a visual editor. The tools have changed. Most workflows haven’t.
This past week, we launched a brand new marketing site, built from scratch, so agents can work on it as fluidly as humans do.
The Problem: The limits of No-Code
About a year ago, our growth team had a problem: we needed to move fast, updating landing pages, refreshing copy, and spinning up campaign pages for every release-- but we were completely dependent on engineering to do it. So we did what most teams do: we moved to a WYSIWYG editor and handed the keys to the creative team. We got speed, but at a cost. Pages got built faster but not correctly. SEO slipped. Technical and visual design debt quietly accumulated.
SEO issues identified by various reports
A few months ago, we started experimenting with agents. Emily Simonin, one of our founding Agent team members, built experiment agents that could analyze traffic, suggest copy changes, and spin up A/B variants automatically. It was exactly the kind of speed the team had been chasing. The catch was we could only run those experiments on 3% of our site. A small repo of legacy SEO focused pages that we hadn’t migrated because they remained mostly static. The rest wasn't accessible to agents.
That’s when we realized this wasn’t really a website problem. It was a workflow problem. The pace of change had outgrown the systems we were using to manage it.
The Solution: Build for how agents think.
Working with agents day in and day out with a product like Warp, we know first-hand how to best set them up for success. When considering a transition like this, it’s helpful to understand how Agents think and what they need to perform best.
Agents need documentation.
Agents navigate through what’s referenceable and queryable. Documentation gives them context, helps them orient themselves, and makes it easier to understand how a system is supposed to work.
Agents need clear structure.
We rebuilt the site around a clean, modular component architecture with consistent naming and patterns. Using Next.js gave us a predictable framework for organizing pages, layouts, and components, making it easier for both humans and agents to understand how the site fits together.
Agents need direct access to the source.
Visual editors are designed for humans. Source code is designed to be read, searched, and modified. By moving back to a fully code-driven frontend, agents can reason about and update the entire site rather than a small portion of it.
Agents like well-known frameworks.
Agents aren’t learning your stack from scratch. They’re drawing on patterns they’ve already seen countless times. We chose Tailwind because it’s one of the most documented frameworks on the internet. The more familiar the tooling, the more reliable the results.
Agents like separation of concerns.
Agents perform best when systems have clear responsibilities and predictable places to make changes. We moved content, assets, and page management into Sanity while keeping presentation and behavior in code. That separation makes it easier for agents to know where a change belongs and reduces the risk of unintended side effects.
The goal is to create systems where changes are predictable, visible, reviewable, and reversible. By building this foundation and being aware of these considerations from the start, agents can move quickly while humans stay in control.
The Process: Human to Agent Handoff
One thing we didn’t want to lose in moving back to code was speed. The biggest advantage of a WYSIWYG editor is that anyone can jump in, make a change, and publish it immediately. Returning to a code-based workflow shouldn’t mean returning to engineering bottlenecks.
Instead, we wanted a new kind of handoff. Humans should still be able to define intent, review outcomes, and make judgment calls. Agents should handle the mechanical work of implementing, updating, and maintaining the system.
To make that possible, we separated content from implementation. We moved content into Sanity and treated it as the operational layer of the site. Editors can update content directly, agents can generate and modify pages, and every change remains visible, reviewable, and reversible. Rather than hiding complexity behind a visual editor, we exposed it through systems that both humans and agents can understand.
The result is a workflow where humans spend less time executing changes and more time directing them. When you’re rebuilding a site in three weeks, you quickly learn that perfect parity is the wrong goal. If you optimize for pixel-perfect recreation of the past, you’ll miss the opportunity to build for the future.
What It Means: Build systems, not pages
The result is a site where we control 100% of the source code, which means 100% of it is available for agents to work with. But more than that, it changed how we think about design work altogether.
It's less about crafting individual assets and more about building systems with enough flexibility to serve a range of needs and enough structure to stay coherent at scale. Brand guidelines become agent-legible rules. A component library becomes the guardrails within which agents make decisions. An internal asset system that automatically tags images for color, text, and usage context means an agent can query for the right image rather than grabbing whatever's most recent.
PRs serve as the source of truth created by Agents and Warp team members
Speed is table stakes now. The real differentiator is orchestration: designing systems where agents can execute meaningful work autonomously while humans retain oversight, taste, and control. The teams who figure that out early aren't just going to move faster, they're going to work in a way that most teams aren't even thinking about yet.
For a long time, the designer's job was: make it look good. Then: make it look good and ship it fast. Now it's closer to: build the system that enables everything else to keep up with the pace of change, whether a human does it, an agent does it, or both.
Related articles
May 14, 2026  ·  10 min
Agents Need Feedback Loops, Not Perfect Prompts
For agents doing judgement-heavy work, the starting prompt is only the beginning. The best agents learn what good looks like from the team and improve themselves over time.
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
