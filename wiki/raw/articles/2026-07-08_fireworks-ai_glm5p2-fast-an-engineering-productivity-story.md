---
title: "How I shipped a month of engineering work in four days with GLM 5.2 Fast"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/glm5p2-fast-an-engineering-productivity-story"
scraped: "2026-07-08T06:00:53.793702+00:00"
lastmod: "2026-07-08T04:44:15.000Z"
type: "sitemap"
---

# How I shipped a month of engineering work in four days with GLM 5.2 Fast

**Source**: [https://fireworks.ai/blog/glm5p2-fast-an-engineering-productivity-story](https://fireworks.ai/blog/glm5p2-fast-an-engineering-productivity-story)

GLM 5.2 Fast is available! Opus-level intelligence at open-source rates. No contracts, pay per token. Start building.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Glm5p2 Fast An Engineering Productivity Story
Using GLM 5.2 Fast to deliver one engineer-month in just four days and $218 of tokens
PUBLISHED
7/7/2026
Table of Contents
TL;DR
The problem
The workflow
How to try it
Closing
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
TL;DR
The problem
The workflow
How to try it
Closing
Table of Contents
Last week I shipped a feature I would normally have scoped at a full engineer-month. It took four days and cost $218 in inference. Here is what happened, and why I think fast open models are quietly changing how senior engineers work.
TL;DR
Using
glm-5p2-fast
through FireConnect on Claude Code, I designed, planned, and implemented a "reclaim" capability for our GPU scheduler in about four days of my own time. The result was a stack of four PRs, roughly 3,000 lines of code, 16 unit tests, and 18 integration tests all passing, CI green and ready for review. Total inference cost, per the Fireworks dashboard: $218. The comparable effort in the past would have been about one engineer-month.
The problem
I wanted to add a
reclaim capability
to our GPU scheduling system.
The mental model is Linux page cache. The kernel treats free RAM as wasted RAM: it fills idle memory with cache to speed everything up, but the instant an application actually needs that memory, the kernel hands it back. No negotiation, no delay. I wanted the same property for GPU capacity: put otherwise-idle capacity to work, while preserving the guarantee that protected placements take precedence the moment they need to.
This sounds close to Kubernetes preemption, but the hard part was in the details: deciding which work was actually safe to move, keeping our internal accounting consistent, and making those decisions correctly while the world was changing underneath the scheduler.
This is not a toy feature. It was hard for five reasons:
It touches the most critical path in the system, the scheduling logic itself.
It requires deep domain knowledge on two fronts: Kubernetes internals and the specifics of how Fireworks scheduling works.
There were several viable designs, each with real trade-offs.
It has to be correct under concurrency, which means reasoning carefully about race conditions and locking.
It has a long tail of corner cases.
In other words, exactly the kind of work where you would expect a model to fall over and a human to spend weeks.
The workflow
I ran the project in three phases, with GLM 5.2 as a partner in each.
Design (about 1 day)
I started by using GLM 5.2 as a design partner, iterating on where the reclaim logic belonged in the scheduling path and how it should interact with normal placement decisions, until both my teammates and I were happy with it.
Historically this phase alone takes me about two weeks: reading code, talking to people, researching how the industry solves it, authoring the design doc, and running design reviews.
Reality is that even in 2026, context switching is a major challenge to eng productivity. Everyone interacts with AI now, and most of us have quietly accepted a workflow of 8+ tabs, each with an agent that needs babysitting, swapping our own mental state in and out like an oversubscribed CPU. The fix is to make it so fast that switching isn't worth it. At roughly 400 tokens per second, GLM 5.2 Fast answers before my attention has anywhere else to go. Even with a frontier closed model like Opus, this phase would have taken two to three days, mostly spent waiting and swapping back in. With GLM 5.2 Fast, I got to a reviewed, agreed design in one.
Plan (about 0.5 day)
Next I moved into a planning phase and iterated the implementation plan to a "ready to implement" state. I work spec- and test-driven, so I had GLM 5.2 compose the test surface up front: 16 unit tests and 18 integration tests, covering every corner case I could think of. Locking down 34 tests before writing implementation code is what makes the next phase safe to hand off.
Implementation (about 1.5 days)
GLM 5.2 then implemented against that plan, producing a stack of four PRs totaling around 3,000 lines of code, with all 34 tests passing and CI green, on a modest amount of direction from me.
The mechanism here matters: GLM 5.2 and Claude Code loop against a concrete goal, that all 34 tests must pass, and keep iterating until they get there. GLM 5.2 Fast is quick on its own; most of the wall-clock time in this phase was the integration tests themselves running each iteration, not the model thinking.
The results
For a project I would normally budget at one engineer-month, this took about four days of my time, and the total inference cost was surprisingly low at $218.
A few observations on why it worked:
Speed compounds.
Faster inference is not just a nicer number. When responses land in seconds, the work becomes a real-time debate. I propose ideas A, B, and C and ask the model to challenge them from first principles. A will not work, B holds up with one caveat, C introduces a risk I had not considered, and sometimes it gives me a D I never thought of. When that loop runs fast, it feels like having a capable teammate at the whiteboard with me. Slow inference breaks the loop. Ask a question, wait fifteen minutes, and I can't just sit there. I join a meeting, switch to something else, and lose the thread. With typical AI speeds and latency, collaboration degrades from a live whiteboard session into feeling like async code review: the same information eventually gets exchanged, but every round trip costs a context switch, and the context switches are mine, not the machine's. On a problem with this many moving parts, that's the difference between days and weeks.
No stress about token spend.
Like many engineering teams, we have monthly token limits for closed models. I historically have had to self-regulate when to use Claude & Codex because otherwise I burn through the monthly quota in just a few days. For this project, GLM 5.2 did so well in the design and planning phases that after preparing my test coverage, I simply sent the plan to GPT 5.5 for a first-principle based review, and it only provided a few minor suggestions. That gave me the confidence to continue pushing with GLM 5.2 the rest of the way. Not having to ration requests or worry about hitting a spend limit was a genuine relief, and it let me lean on the model as hard as the problem demanded.
Quality held on hard work.
This was critical scheduling logic with concurrency and corner cases, not boilerplate, and the combination of a strong open model, a test-driven plan, and a capable harness held up.
How to try it
The setup is a one-time change to point Claude Code (or your harness of choice) at Fireworks through
FireConnect
, then select the fast GLM 5.2 path:
1
2
curl -fsSL https://raw.githubusercontent.com/fw-ai/fireconnect/main/install.sh
fireconnect claude on
The model ID for the fast path is:
accounts/fireworks/routers/glm-5p2-fast
GLM 5.2 Fast runs 2 to 3x faster than the standard path on shared serverless, keeps the full context window, and rewards cached input heavily, which is what makes long agentic coding loops practical and cheap. More on the serving details in
GLM 5.2 Fast is live on Fireworks
.
Closing
The headline number is real: an engineer-month of work in four days for $218. But the takeaway I keep coming back to is about more than just speed or cost or quality. It's the full combination. Because GLM 5.2 produces design and code quality that I actually trust, and likewise at a speed and cost that lets me to stop self-regulating, I can actually feel fully productive. The promise of AI was supposed to take the drudgery out of engineering, and instead a lot of us traded typing for tab-juggling, waiting on slow agents and paying switching costs with our own attention. This project convinced me that the promise is now real. When the model answers before you can reach for another tab, you stay focused. Four days instead of a month is what that feels like.
Thanks to the FireConnect team for making this possible, and thank you for reading.
Shoucong Chen
Shoucong previously architected large-scale cloud infrastructure platforms across Google, Databricks, and Uber.
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
How I shipped a month of engineering work in four days with GLM 5.2 Fast
