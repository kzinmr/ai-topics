---
title: "How to build a cloud software factory - add spec-driven development skills"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-add-spec-driven-development-skills"
scraped: "2026-06-30T06:01:00.286657+00:00"
lastmod: "2026-06-29T19:03:44.000Z"
type: "sitemap"
---

# How to build a cloud software factory - add spec-driven development skills

**Source**: [https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-add-spec-driven-development-skills](https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-add-spec-driven-development-skills)

Engineering
How to build a cloud software factory - add spec-driven development skills
Zach Lloyd
June 29, 2026
This is my second post in a series on how to build out a fully automated cloud software factory. In this post, I’ll show how you can add spec-driven development for issues that are too complex or ambiguous to one-shot. The goal of these posts is to build a fully working factory that addresses the whole SDLC.
In my prior post
, we started with a simple flow of Triage → Implementation, where an agent reviews the quality of an issue, asks clarifying questions, and implements as draft PR if the issue is scoped well enough to one-shot.. This works well for straightforward bugs and small features, but doesn’t work for issues that have more ambiguity or technical complexity.
In order to have factory agents work with those kinds of issues, we will add a new agent: the
Spec agent
:
If the issue is simple, apply “ready-to-implement” label →
Implementation Agent
runs
If the issue is complex but fits the roadmap, apply “ready-to-spec” label →
Spec Agent
runs
If the issue has ambiguity, apply “needs-info”
Otherwise, apply “wait-to-implement”
We implemented the basics of this earlier, but now we will refine the “ready-to-spec” step.
The first change to get this to work is to update the
Triage skill
to have a better logic for when to create specs. We should apply “ready-to-spec” when an issue:
Matches our roadmap and vision
I added “
roadmap.md
” and “
vision.md
” to our sample image editor project describing what we want it to turn into and what we are planning on building towards to help the agent here
Has enough complexity or ambiguity that it would benefit from a spec. To keep it simple:
“Ambiguity” means there are many potential product or technical implementations that have significant differences, and a human should weigh in on which is best
“Complexity” means that the implementation would be more than a few hundred lines of code.
The roadmap for our example app
Here’s the update to our triage skill to handle spec’ing:
The updated triage skill
If the issue is either ambiguous or complex but matches the roadmap and vision, the Triager applies the “ready-to-spec” label, which triggers a new
Github action
that invokes a new
Spec agent
.
The spec action
I’m re-using all the infrastructure I set up in the first post, which means you’ll need a Docker image with your code and toolchain, a place to run it (our example uses
Oz
, Warp’s cloud automation platform), and the ability to set up Github actions.
The spec action produces two specs:
A
PRODUCT.md
: this is responsible for defining the product behavior for the agent to implement
A
TECH.md
: this is responsible for defining the tech architecture and code shape.
These both live under a “specs” directory that is tied to the issue number being fixed.
A sample PRODUCT.md for a feature in our example image editing app
A sample TECH.md
I would recommend checking in these specs as part of your implementation PR, although you can also check them in separately first, and do the implementation only after they are merged. Checking them in gives you a record of the “what” and the “how” that the agent was aiming for that you can later verify against. I’ll show you how to do this when we add a Verification agent using
/validate-changes-match-specs
in a later post.
The agent will produce an initial version of the specs, but it’s often a good idea to pull them into your local workspace and go through an interactive refinement process to align your expectations with the agent. I recommend something like
Matt Pocock’s /grill-me Skill
for this.
Once the specs look good, ask your agent to mark the underlying issue as ready-to-implement (or just mark it as such directly in Github). This kicks off our implementation agent on building the spec’d version. To make this work, I updated our
implementation skill
to look for specs and follow them while implementing.
Instructing the implementation agent to follow the specs
Once you have this all in place, you now have a flow that can accept issues, implement the simple ones, spec the harder ones, and loop you in when necessary to review and iterate.
The next step after this is to start making sure the implementation is high quality by adding review and verification agents – this will be the subject of my next post.
If you want to try it yourself, follow the instructions here:
https://github.com/warpdotdev-demos/cloud-factory-demo/
and run the /oz-cloud-factory-demo skill using
Warp’s cloud platform
or a coding agent of your choice.
Try it out and let me know how it goes.
Related articles
Jun 25, 2026  ·  7 min
How to build a cloud software factory - the automatic triage skill
This post is the first in a series I’m doing on how to set up your own cloud software factory using skills and loops. It’s easier than it sounds to get something simple and effective running so you can start to automate significant parts of your team’s development flow.
Jun 18, 2026  ·  4 min
Building a skill optimization loop
This post shows how to create a loop with automated feedback that an agent can run to optimize its own Skills. It uses an automated grader with computer use to assess how well a Skill is performing, and then iteratively improves the Skill.
Jun 18, 2026  ·  1 min
Generate interactive PR Walkthroughs with a single Skill
While we’re waiting for someone to re-invent Github I put together a useful skill that can help folks better understand agent (or human) generated PRs.
