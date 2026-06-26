---
title: "How to build a cloud software factory - the automatic triage skill"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-the-automatic-triage-skill"
scraped: "2026-06-26T06:00:29.981201+00:00"
lastmod: "2026-06-25T20:45:30.000Z"
type: "sitemap"
---

# How to build a cloud software factory - the automatic triage skill

**Source**: [https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-the-automatic-triage-skill](https://www.warp.dev/blog/how-to-build-a-cloud-software-factory-the-automatic-triage-skill)

Engineering
How to build a cloud software factory - the automatic triage skill
Zach Lloyd
June 25, 2026
This post is the first in a series I’m doing on how to set up your own cloud software factory using skills and loops. It’s easier than it sounds to get something simple and effective running so you can start to automate significant parts of your team’s development flow.
By “cloud software factory” I mean a setup where agents semi-automatically do key parts of the SDLC from triaging issues to spec’ing to coding and verifying changes using cloud agents. You can see a live example of a cloud factory on Warp’s 60k star Github repo:
build.warp.dev
.
The factory workflow is straightforward:
Triage agent runs and tries to understand and repro issue
If it determines the task is automatable → hand it to the implementation agent
If it needs specs because of ambiguity or scope → have the spec agent spec it
If requirements are unclear → get human input and re-run, or just decide to park the issue for now
[If necessary] Spec agent runs
Human reviews specs and then passes to implementation agent
Implementation agent writes code
Code review agent reviews code
Verification agent does computer-use or other verification
Human reviews code and verification output
If necessary, go back to step 2, 3, 4 or 5
CI / CD
Ship it
Monitor agent runs and creates issues if need be completing the loop
A full factory has the whole SDLC loop implemented, but you can start with just some particular slice and add on more agentic flows as you go.
In this post, I’ll start with just Triage → Implement. This will give you the ability to hook up some task management system (e.g. Linear, Jira or Github Issues), have an agent triage issues that come in and implement fixes that the Triager thinks are simple enough to one-shot. In future posts I’ll show how to expand this flow to other parts of the SDLC, including adding agents for spec’ing and verifying, and set it up to improve automatically over time using Skill loops. For now, success is having some percentage of issues automatically implemented up to the point of code review.
My approach here is to set up the factory using an approach that isn’t tightly coupled to any one coding agent or platform and uses Skills and loops as its basis. The goal is to get folks comfortable with a factory approach from first principles (
see my post on factory engineering here
); later you can
explore platforms
that make it easier to manage and scale your factory (and I do suggest this for most teams, as
building all of the infra to scale a factory is a lot of work
).
Here’s what you need to get started:
A repo you want to perform automations on, preferably hosted on Github.
A Docker image with the toolchain for that repo, and a place to run it in the cloud.
An issue tracker that has an MCP or CLI.
Two base Skills:
A Skill for issue triage
A Skill for implementation
A coding agent SDK (e.g. Claude Code or Codex or
Warp
)
I’m going to do this walkthrough using
Oz
, Warp’s cloud factory platform, but you could host it any number of places.
For this walkthrough, I’ll use a demo repo I vibe-coded that’s a simple image editor based on Nano Banana:
https://github.com/warpdotdev-demos/nano-banana-editor
A simple image editing app
I’ve also seeded a bunch of fake issues for improving this tool in Github
issues
.
Let’s say that as issues come in, they get triaged into one of four possible states:
ready-to-implement
,
ready-to-spec
,
needs-info
, and
wait-to-implement
. You can come up with your own label hierarchy here or use whatever your team currently uses.
Depending on the label applied by the Triager, the issue will flow to the next agent or stay parked:
ready-to-implement
→ issue goes directly to an implementation agent
ready-to-spec
→ issue goes to a “spec’ing” agent that writes product and tech specs (will show in a later post)
needs-info
,
wait-to-implement
→ no action until a human reviews and sets another label
Here’s what you need to implement this:
A Docker image for your code. We use
node:20-bookworm
for the sample JavaScript project.
A place to run this image on a trigger with a coding agent (we will use
Oz
here, which has cloud hosting and built-in multi-agent support)
A Github action for invoking the triage agent when a new issue is filed.
A Triage skill encoding the labeling workflow above
The Triage skill
The Github action
The result on a test issue
Once you have this in place, the next step is to automatically implement issues that the triage agent marks
ready-to-implement
. The implementation agent is, you guessed it, just another Skill.
The implementation skill
As long as you have a strong coding agent available, a Skill is good enough to start. You can get fancier and build specific subagents or even a custom harness for this step (and we are bundling this into
Oz
), but it’s not necessary out of the gate.
With this skill in place, just add one more Github action that fires off another cloud agent whenever the
ready-to-implement
label is applied:
The second github action for implementation
This produced a reasonable
diff
on
https://github.com/warpdotdev-demos/nano-banana-editor/issues/15
, implementing a small feature in the app.
To recap, here’s what we’ve done so far:
Made two skills, one for triage, one for implementation
Invoked these Skills using Github actions when new issues are opened, attaching labels at the time of triage
Used Warp as the coding agent and Oz as the cloud agent runner to implement issues that are labeled one-shot ready.
That’s it. At this point, you have a very minimal but functional cloud software factory that triages issues and implements simple fixes and features.
If you want to try this yourself, the best approach is to follow the instructions at
https://github.com/warpdotdev-demos/cloud-factory-demo
to install the relevant agents on your own repo.
I also made a Skill that helps set up this triager on your own repository:
npx skills@latest add warpdotdev-demos/cloud-factory-demo --skill oz-cloud-factory-demo --agent warp --yes
This installs an
/oz-cloud-factory-demo
skill that you can invoke in any coding agent (e.g. Claude Code, Codex or Warp) which will walk you through how to run this demo locally. This uses
Oz
as the runner since it’s flexible to any model provider (
including open-weight models
) and whatever environment configuration you need via Docker. If you prefer to use another cloud agent platform, just ask your agent how to set it up on that platform and it will guide you.
In my next post, I’ll show how to extend this system to be more sophisticated by supporting spec-driven development and richer human-in-the-loop workflows.
Related articles
Jun 18, 2026  ·  4 min
Building a skill optimization loop
This post shows how to create a loop with automated feedback that an agent can run to optimize its own Skills. It uses an automated grader with computer use to assess how well a Skill is performing, and then iteratively improves the Skill.
Jun 18, 2026  ·  1 min
Generate interactive PR Walkthroughs with a single Skill
While we’re waiting for someone to re-invent Github I put together a useful skill that can help folks better understand agent (or human) generated PRs.
Jun 16, 2026  ·  4 min
How to build a self-improvement loop for your Skills
There’s been a lot of chatter about using “loops” lately to drive agents, and I think this has been accompanied by a bit of “what actually is a loop”?
