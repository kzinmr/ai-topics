---
title: "How to build a cloud software factory - computer use verification"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-computer-use-verification"
scraped: "2026-08-04T06:00:09.848361+00:00"
lastmod: "2026-08-03T22:54:32.000Z"
type: "sitemap"
---

# How to build a cloud software factory - computer use verification

**Source**: [https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-computer-use-verification](https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-computer-use-verification)

Product
How to build a cloud software factory - computer use verification
Zach Lloyd
August 3, 2026
This is the fourth post in my series on how to build a
cloud software factory
.
In this post I’ll describe how to add computer and browser use to your agents to reproduce issues and verify fixes and new features.
Prior posts:
Build an issue triage agent and implementor agent
Add spec driven development via a spec agent
Add a self-improving code review agent
For folks unfamiliar with
computer and browser use
, it’s a tool that allows agents to control a running application directly with mouse clicks and keyboard presses. Most of the major model providers have models that support this, and they are increasingly available in different harnesses, including Warp.
We’ve brought computer use to all parts of our agentic stack,
including feature requests on Twitter
The value of computer use in your cloud software factory is less as a standalone agent, and more as a capability to provide to other agents in the factory flow. Specifically, computer use is valuable:
During the
triage phase
to reproduce bugs before trying to fix them
During
implementation
to verify fixes and verify that new features match specs
During
review
to prove to a human reviewer that code actually matches expected behavior
The verification is particularly valuable as a way of lessening code review burden. If you can see a video of a feature working, you are more likely to trust the underlying code (although you’ll still want to review the code to make sure the architecture is good, code is clean and secure, etc). Especially for pure UI changes that are low risk, having “proof” that a feature works from the user perspective is valuable and saves time.
Another less obvious benefit of computer use is that it lets an agent create a loop where it can debug changes on its own. This works especially well with
spec-driven development
when you have a detailed
PRODUCT.md
that the agent is trying to implement. At every implementation pass, it can run computer use to see how close the implementation is to spec, and continue until it’s good. You’ll want to monitor costs here as it can be expensive, but it increases the likelihood of success.
As with prior posts, you can use the implementation on your own repos by following the
open-source demo
. There’s a
skill you can install
and then invoke from your favorite coding agent to directly set up everything on your own repo:
npx skills add warpdotdev-demos/cloud-factory-demo --skill oz-cloud-factory-demo
Add computer use verification to your agents
Diving into computer-use, we create a new skill called
verify-behavior
that defines how to use computer and browser use.
The
verify behavior skill
The key aspects of the skill are:
When to use computer use (desktop and mobile-native) vs. browser use (webapps)
What to capture: video preferably, but screenshots are fine
The two modes to use it in:
reproduce:
try to confirm that a reported bug occurs
verify:
verify a new behavior
In order for this skill to work, it needs to be run through a harness that supports computer and browser use. Since we are building a cloud software factory, this should be a harness that supports cloud agents. As with prior posts, we use
Warp’s cloud agent platform
, but there are others that support it as well.
At this point, you can run the
verify-behavior
skill directly, but it’s actually more useful to hook it into the other agents in your factory as a capability they can take advantage of. To do this, we will update the existing
Triage
,
Review
and
Implementation
skills to encourage them to use the verify-behavior skill when it will help them do their jobs.
For instance, we can update the
Triage skill
to try to reproduce bugs:
And update the
Implementation skill
to verify new features:
The update to the implementation skill to verify behaviors
Note that the verify-behavior skill uses cloud subagents. You can also do computer use locally, but it tends to be a worse experience unless the platform you’re using can test in the background (otherwise it steals focus and prevents you from doing anything while it runs). Warp and Codex do support this, but it still tends to be best in my experience to do computer use on a cloud machine where there’s no chance of the agent doing anything weird with the apps running on your machine.
For complex or new behaviors, we ask our orchestrator to fan-out to verify all of the user stories independently and in-parallel (your harness needs to support multi-agent orchestration for this to work). Computer use is typically single-threaded, so if you want better throughput, it’s best to fanout cloud agents across machines. This can get expensive, but it’s very cool, and reduces latency a ton.\
Computer use in action
I have a
demo repo
that I’ve used in a few of these posts that implements a simple agentic image editor using Nano Banana.
As a first user story, I’m going to show how you can use computer use to verify an issue. In this case, there’s a bug in the demo app: when an image is uploaded, its preview renders at thumbnail size rather than gallery size. The GitHub issue where this was reported is
here
.
The agent here was able to run and produce screenshots of the broken behavior:
The zero state for reproducing the issue
A screenshot showing the incorrect thumbnail
This is a trivial example, but for folks dealing with bug reports, having images automatically generated to verify the reproduction is a big unlock. You can see the raw cloud agent run that generated these images
here if you’re curious what the agent trace
looks like.
Moving on to a second use case, I asked an agent to implement a new feature in this repo end-to-end and verify it using computer use. The feature is described in this
issue
and is a relatively straightforward UI change, adding “clear” and “replace” controls to the image editor. There are clear acceptance criteria in the issue for the verifier to check against:
Acceptance criteria for
verify-behavior
to check
The
PR
itself has screenshots showing the controls, and a link to a video proving they work.
Here’s a
video
the agent produced showing the feature in action end-to-end:
It really is that simple – once you have the scaffolding set up you can use computer use to help lift the burden on PR review. In fact, for low-risk UI changes, you might decide that watching these videos is enough and you don’t need to look at the code at all.
To recap, we have created agents that:
Triage new issues
, optionally sending them to be implemented or spec’d
Spec issues
from a product and technical perspective
Implement the actual code
Review the code
and improve review over time
with an observer loop
And now we’ve added a verification capability that all of the other agents can use to make sure the implementation is correct and allow a human reviewer to see a record of how the feature works.
These posts show how, with a simple set of primitives, you can start to build your own factory and truly automate more of your mundane work. The primitives are just:
A cloud agent platform like
Warp
that supports computer-use
A workflow tool like GitHub Actions
A set of agent skills that you and an agent can tune
My next post in this series will show how you can expand this factory with agents that monitor features and fixes after they are released and feed that monitoring back into the Triage phase, completing a basic factory loop.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Jul 18, 2026  ·  4 min
Get agents off your machine
Even though we are living in 2026, it feels like folks have forgotten the lessons of 2006: software belongs in the cloud, not on individuals’ desktops.
May 20, 2026  ·  6 min
Bring your own inference to Warp
Today we’re releasing one of the most requested updates from the Warp community: more control over inference.
May 19, 2026  ·  6 min
A single pane of glass for managing all of your cloud agents
With Oz, engineering teams can now integrate, orchestrate, control, and improve any cloud agent at scale including Claude Code, Codex, Warp Agent, and whatever comes next.
