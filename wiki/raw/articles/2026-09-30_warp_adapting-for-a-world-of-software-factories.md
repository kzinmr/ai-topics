---
title: "Adapting for a world of software factories"
source: "Warp Blog"
url: "https://www.warp.dev/blog/adapting-for-a-world-of-software-factories"
scraped: "2026-09-30T06:00:30.184788+00:00"
lastmod: "2026-09-29T15:22:58.000Z"
type: "sitemap"
---

# Adapting for a world of software factories

**Source**: [https://www.warp.dev/blog/adapting-for-a-world-of-software-factories](https://www.warp.dev/blog/adapting-for-a-world-of-software-factories)

Company
Adapting for a world of software factories
Zach Lloyd
|
September 28, 2026
Software engineers have been through a lot of change in the past two years, transitioning from writing code by hand to steering agents via local
interactive prompting
, the current paradigm. Engineers were skeptical of prompt-driven development at first, but it’s standard now, and by and large
folks seem well adjusted
to working with agents this way.
The next paradigm is
software factories
, where agents do more and more autonomous work across the entire software lifecycle. From my conversations with customers and observations of Warp’s own team, making this shift is potentially more challenging than the last one. But the gains in productivity, cost management and control are profound with a factory approach, so I believe the shift is inevitable.
There isn’t a universally agreed upon definition of what “software factory” means, and some folks imagine “dark” factories operating with no human oversight at all. If you don’t need humans, engineers rightly ask what their job is. You end up with a demotivated team that thinks they are no longer needed. Business leaders may want dark factories, but that’s not realistic right now, and pursuing them can cause engineering attrition.
In a factory, all work is public by default, including work that used to be private, in a developer’s “inner loop.” This is very different from what engineers are used to, where they work locally on changes and the first the team sees of them is when those changes are pushed for review as a PR. Working in public exposes how you work, not just what you build, to the entire team, and that can be uncomfortable. This is compounded because work is measured, with it being easy to see how efficient each engineer is from a token use perspective. It can make us all feel like cogs in a machine.
Also, the metaphor of “factory” is kind of a bummer. It feels like your job as an engineer is either working on an assembly line, or building the assembly line that obviates the need for your talents. If you use the “AI teammate” metaphor (which I also dislike), then it feels like engineers are becoming managers of sycophantic and somewhat inept junior engineers. For folks who take pride in the craft of building, this all feels like commoditization of software creation.
A day in the life of a factory engineer
At Warp, our entire focus is on building the technical infrastructure,
Warp Factories
, to enable teams to make the transition to this new way of working, but we are also thinking hard about how it empowers engineers working with factories. I’ve written a guide for interested teams on the
crawl, walk, run
steps for adopting factory infrastructure.
At Warp we make clear to our engineering team that they now have two main jobs: building the product
and
building the factory that builds the product.
Our engineering team
still is responsible for the quality and usefulness of the product –
this cannot be delegated to agents. They will continue prompting and steering agents to make sure the right thing gets built and that it works well for users.
This is “product engineering,” and humans will continue to do it. Humans are uniquely positioned to know what to build, how the pieces should fit together, what the product experience ought to be, what constitutes good design. Humans have taste, and humans for the time being have more context than agents, making it more likely they build useful stuff.
There are two caveats here though. First, there will be some types of product work that don’t need any human input at all and
can be purely automated
. Think of fixing server crashes, simple bugs, small UX papercuts, dependency upgrades, etc. This percent starts low (for Warp, it started around 20-30%), but goes up over time. In fact, driving it up is part of the second job of the engineer, which I’ll get to momentarily.
The second caveat is that product engineering will work differently than in the past. Rather than engineers working locally with their own bespoke setups, they will primarily be doing this work “through the software factory,” which means prompting agents that live in the cloud through knowledge work tools like
Slack
and
Jira
, in public. They will hand off as much of the software lifecycle as possible to the factory. All of this work will be inherently visible and measurable, and that’s a feature, not a bug. The whole team should be trying to work more publicly and with more of a bias towards automation.
At Warp we measure “human touches per PR,” and over time, this number should go down. For example, say an engineer is building a relatively complex feature into an app, like adding searching, sorting and filtering to a database driven view (just pulling a random task we did recently at Warp). A human will do an initial prompt (first touch), provide context like mocks, and
iterate with a factory agent on a spec
(n touches, while you iterate). Then the factory takes over for a bit, doing implementation,
adversarial code review
, and producing
computer use videos
showing the behavior. Then a human looks again, and may or may not need to do a manual code review (another touch). Over time there will be fewer touches as the factory improves.
In addition to automation metrics, developers should expect to also measure and iterate on other aspects of how they use the factory, including
how much their agents ship, and at what cost
. Again, engineers could view this as a drag, but they also can view it as a game, and winning that game means shipping more for less, using an engineering mindset to improve.
This brings me to the second job of the engineer, which is, somewhat ironically, to engineer the factory so they are doing less of the first job. I call this
factory engineering
. It consists of
measuring the performance of your factory
using DORA metrics and
LLM-as-a-judge scorers
, identifying areas for potential improvement to
skills
, context and
model mix
, and implementing changes that increase automation and velocity. This needs to be done with an engineering mindset – you don’t adjust your factory on vibes; you measure, test,
benchmark
and then improve. Some of this improvement itself can be automated via
self-improvement
, but much of it needs human insight.
At Warp we make it explicit that the expectation of engineers is not just to build products, but to improve factories. We bake this into feedback and performance reviews, celebrate changes that make code production more efficient or higher quality, and ask senior engineers to model the behavior. We envision both jobs as being the responsibility of all engineers, to make it clear that factory engineering is now part of software engineering.
We emphasize that this work is
engineering
, albeit of a new kind, and can be really fun. On our team, the folks who like it most are senior engineers who love hard systems problems, who enjoy optimizing and debugging performance issues. It requires a lot of thought, testing and patience. We lean into it as a new skill to learn. And ultimately it lets us ship better products more quickly, which has always been our mission.
Closing thoughts
We’ve been through a lot of change as engineers in the past two years, and that change is going to continue as software factories roll out. Engineers are now responsible for both product engineering and factory engineering. Factory engineering is real engineering and a skill to develop.
Warp’s mission is to provide the world’s best engineering teams with the tools to build, measure and optimize their own workflows using
any underlying model and harness
on
open infrastructure
. These capabilities will help teams ship better software more quickly and efficiently.
Warp Factories is currently in early access
. Qualified companies get $10k of factory usage.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Jun 18, 2026
|
Company
7
min
We are now factory engineers, not product engineers
7
min
Jun 12, 2026
|
Company
5
min
How Rectangle Health Built an AI Teammate That Writes Its Own Code
5
min
Apr 28, 2026
|
Company
4
min
The virtuous loop of open, automated development
4
min
Mar 16, 2026
|
Company
8
min
What happens when you give the company 4 hours to automate everything
8
min
Feb 10, 2026
|
Company
12
min
Introducing Oz: the orchestration platform for cloud agents
12
min
View all articles
