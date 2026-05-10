---
title: "The virtuous loop of open, automated development"
source: "Warp Blog"
url: "https://www.warp.dev/blog/the-virtuous-loop-of-open-agentic-development"
scraped: "2026-05-10T01:27:02.643213+00:00"
lastmod: "2026-05-04T14:33:51.000Z"
type: "sitemap"
---

# The virtuous loop of open, automated development

**Source**: [https://www.warp.dev/blog/the-virtuous-loop-of-open-agentic-development](https://www.warp.dev/blog/the-virtuous-loop-of-open-agentic-development)

Company
The virtuous loop of open, automated development
Zach Lloyd
April 28, 2026
With today’s
open-sourcing of Warp
, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
We are creating a flywheel where a user’s idea becomes a real improvement to Warp—prototyped with an agent, refined and approved with our team, built and shipped by our agentic infrastructure, Oz, and verified together—so that each contribution makes the product better and brings more users into the fold. The more people that participate, the faster we build, and the better the product gets.
This is the virtuous loop of Open Agentic Development, and whomever gets it right first is going to build an agentic workbench with escape velocity.
Open agentic development flow
For info on how each part of the loop is backed by agents,
we outlined our architecture here
.
From a product development perspective, I believe companies are increasingly going to benefit from building in the open. When you build privately, you are limited by the distance between you and your users. Users have bugs or ideas that go into feedback channels that get eventually triaged and hopefully make it into the roadmap for some internal team member to one day build. When you build publicly, users can actually hack on the product, prototype ideas, and contribute directly.
Why now? Agents have made the public loop more feasible. Coding is cheap, so any user’s idea can become a prototype with some simple prompting. Your team and the community can try prototypes and see if they are worth including in the real app. The number of ideas to test is limited only by the size of the community and the quality of agents. Testing features happens faster and in the open and is driven directly by users who care about the product, not just your team.
Open sourcing is a necessary condition for enabling this loop, but not the whole story. It won’t be enough for a company to just publish their code – companies need to provide users with the infrastructure for contributing – agents that know how to plan, code and verify within the context of that code. With this infrastructure in place, a user no longer even needs to learn how to code. All they need is to express how they want the product to work, and agent infrastructure like Oz that deeply knows the code can make their vision tangible.
The product development process also matters. You can’t just open-source and add agents and hope the product ships itself. You need alignment between the core team and the community so that you don’t create a Frankenstein product, bloated with a long-tail of unnecessary features. Just because a user wants a feature doesn’t mean it belongs in the app. To this end, one of the primary responsibilities of the core team becomes
editing
the product, assembling the community’s contributions into a cohesive whole.
You also don’t want the codebase to devolve into a mess of agent-generated spaghetti. If you’d asked me six months ago, this risk would have been at the top of my list, but it no longer is. This
tweet
from the past weekend was timely:
I agree that well-tuned agent infrastructure like Oz will manage code better in the long run than humans. For Warp specifically, we’ve invested a tremendous amount in Oz understanding our code and being able to verify changes and self-improve over time. Following a
Spec and Verify
process, I feel better about building in public now than I ever would have in a human-only open loop.
This is obviously a time of great change, but, zooming out, I also think it’s a time of incredible opportunity for software to have the biggest economic impact it’s ever had. As software becomes cheaper to build, I predict more companies will realize the virtues of adopting Open Agentic Development; I’m excited for Warp and Oz to lead the way here.
PS, if you want to try having Oz manage your open-source repo, reach out to us
via this form
. We are working with other open-source repos to enable them to ship faster. Also, a special thank you to OpenAI for sponsoring Oz usage at Warp.
Related articles
Mar 16, 2026  ·  8 min
What happens when you give the company 4 hours to automate everything
The Warp team held a company-wide hackathon to build with Oz, our cloud agent platform. Here's every project, from docs migrations to churn detection, that shipped in just 4 hours.
Feb 10, 2026  ·  12 min
Introducing Oz: the orchestration platform for cloud agents
Run hundreds of coding agents in parallel with full visibility and full control
Dec 30, 2025  ·  8 min
Warp Wrapped: 2025 in Review
2025 was the year Warp became an Agentic Development Environment. Here’s a look at the numbers, launches, and ideas that defined it.
