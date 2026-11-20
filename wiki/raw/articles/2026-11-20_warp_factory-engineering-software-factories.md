---
title: "Becoming a factory engineer"
source: "Warp Blog"
url: "https://www.warp.dev/blog/factory-engineering-software-factories"
scraped: "2026-11-20T06:00:38.193806+00:00"
lastmod: "2026-11-19T19:25:37.000Z"
type: "sitemap"
---

# Becoming a factory engineer

**Source**: [https://www.warp.dev/blog/factory-engineering-software-factories](https://www.warp.dev/blog/factory-engineering-software-factories)

Engineering
Becoming a factory engineer
Ben Holmes
|
November 19, 2026
Software engineering has quickly become factory engineering. We've progressed from writing code, to writing prompts, to engineering the system of agents that executes on those prompts. It's a systems design challenge that
seems to have breathed new life
into software development as a whole.
With this shift, I wanted to talk through the progression, and what it looks like to move from hand-holding agents to building a system (or factory) around them:
What patterns a "factory engineer" looks to solve
What a software factory loop includes to help agents write better code
What metrics are worth tracking to measure the quality of that factory, and how those metrics factor into benchmarking and self-improvement
And when you're ready to build a software factory of your own, we've put together a free, public course to get started:
warp.dev/learn
.
The fall of prompt engineering
Let’s break down software engineering into three steps: planning, implementation, and code review.
Before agents, implementation was a bulk of deep work, and engineers used the time left over for architecture discussions and code review.
But now that we have agents doing a bulk of the implementation, the balance has flipped.
In fact, if you’ve been increasing your velocity to fill that gap, it can feel more like this:
If you stop there… It feels like engineering was replaced with 20% meetings and 80% drudgery.
But if we pause for a moment, there are some interesting engineering challenges worth solving:
Plan:
When should the agent involve humans to draft a plan vs. proceeding with implementation? What questions should it ask? What goes into a good product or technical spec?
Implement:
Now that agents are writing code, how do we optimize the cost and quality of that code? What access permissions do agents have across secrets, MCPs, and skills?
Review:
How do we give agents the tools to
verify their own work end-to-end
before tagging us for review? How can agents
assess the risk of a PR
, and include that assessment in the pull request to save humans time?
These are all the types of systems engineering questions that engineers used to implement in syntax and abstractions, just at a higher level.
What is factory engineering?
These stages of development can be defined as new engineering roles:
Product engineering:
building the product itself. This is the “planning” piece – deciding what needs to exist and how it should be architected.
Factory engineering:
building the system of agents that builds the product. This is what you might call a “
software factory
,” hence
factory
engineering. This optimizes the “implementation” and “review” pieces through automation. That doesn’t mean
full
automation though; it means automating low-risk work, and only requiring human attention when absolutely necessary.
Some sample questions a factory engineer might help answer:
Our agent keeps adding test cases and code comments that it really shouldn’t. Could someone make the agent write better code?
I keep copy/pasting these error monitor reports into an agent when I’m on-call. Could we automate this?
Our API bill skyrocketed after the latest model release. Could we be moving some workflows to cheaper models without sacrificing code quality?
The larger your product becomes and the more agents you deploy to build it, the more valuable factory engineering becomes.
What is a software factory?
So what does this “system of agents” we’re optimizing actually look like?
You’ve probably heard of a software factory:
an automation loop around agents
designed to build better and better software over time.
In its idealized form, you set the product requirements and the factory builds and optimizes your product without  human interaction. But of course, agents aren't at the level (yet) to take “build product and make money” as an input and run forever. That's what factory engineers are for: to build a factory around today's agents that automates as much of the software development process as possible.
To create a software factory, you’ll need a shared setup that both agents and the engineering team have access to. Usually, this means moving away from local setups and towards some centralized system, either in the cloud or on your own compute.
The system should also be configurable by humans and agents:
the environment where the agent runs
,
the agent’s access levels
, and
the pipeline of steps
an agent follows to produce work. That last part has a number of sub-components, including
points that require human interaction
.
Here’s one example of a software factory you might build, with human gates called out at "spec" and "pull request" stages:
Alongside this development loop, you’ll need tools to monitor and improve the factory itself. I invite you to click deeper to learn about each one:
Spending metrics
:
Track what agents are costing you, both in terms of token usage and on-device compute. For these numbers to be useful, you’ll want to translate raw metrics to real value, like cost-per-PR and cycle time (aka initial prompt to release).
LLM-as-a-judge scoring
:
It’s also worth tracking agent quality metrics that you
can’t
check statically. This may be architecture quality, number of redundant /
tautological tests
, efficiency of the agent's tool calls, or any other agent behavior you want to tune.
These scores require another agent to monitor past agent conversations
.
Self-improvement
:
Once you’re tracking these metrics, make them agent accessible. This allows agents to improve their own performance. For example, you may have a “redundant tests” scorer that performs poorly on 60% of conversations. A self-improvement agent would notice that trend and suggest improvements to your skills and code architecture to try and reduce those failures.
Benchmarking
:
Test theories on how different factory configurations can improve cost and quality. The biggest lever is model selection, but you might experiment with reducing the number of stages in your factory, adding or removing subagents, etc. Treat these as hypotheses to test in an experiment, changing one variable in your factory to see how the metrics are affected.
Where do I start?
If you're ready to explore these ideas, we've put together a course on how to build software factories of your own:
warp.dev/learn
It's publicly accessible and free to get started. We'll show you how to build factory workflows using
Warp Factories
throughout the course, and the core ideas should serve as a useful starting point for any setup.
Click through to the first lesson and let us know what you think!
Get started on warp.dev/learn
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Nov 16, 2026
|
Engineering
6
min
Overcoming challenges in software factory adoption
6
min
Nov 5, 2026
|
Engineering
9
min
Addressing the code review bottleneck
9
min
Nov 4, 2026
|
Engineering
11
min
Don’t vibe code your software factory
11
min
Oct 29, 2026
|
Engineering
9
min
7 core components for building a software factory
9
min
Oct 15, 2026
|
Engineering
10
min
Tactics for rolling out software factories: human and organizational changes
10
min
View all articles
