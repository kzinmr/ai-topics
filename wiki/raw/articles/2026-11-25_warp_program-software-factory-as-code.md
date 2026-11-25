---
title: "How to program a software factory as code"
source: "Warp Blog"
url: "https://www.warp.dev/blog/program-software-factory-as-code"
scraped: "2026-11-25T06:00:56.698026+00:00"
lastmod: "2026-11-24T23:12:30.000Z"
type: "sitemap"
---

# How to program a software factory as code

**Source**: [https://www.warp.dev/blog/program-software-factory-as-code](https://www.warp.dev/blog/program-software-factory-as-code)

Engineering
How to build a software factory you'll actually use
Ben Holmes
|
November 24, 2026
There are countless ways to define a software factory. This is the one we’ve used on our own team:
An automation loop in the cloud that orchestrates agents to build better and better software over time.
A lot of teams focus on the
automation loop
part, trying to push a backlog of issues through an agent to ramp up velocity. It’s easy to start there… but many teams end up with a black box they don’t trust, or a “slop cannon” producing PRs no one reads.
So, I’d argue that we should focus on the rest of the definition:
in the cloud
and
better software over time:
In the cloud:
Centralize everyone’s knowledge on how to have agents write better code.
Better software over time:
Systematize that knowledge into a step-by-step workflow that the whole team (and agents) can contribute to, measure, and improve.
I’m going to walk through this progression, starting from a plain backlog automation, and showing how to shape it into a software factory you’d
want
to review the PRs from.
We’ll cover:
How to write a basic implementation pipeline as a blueprint, then attach a backlog to see how it performs
Where to bring developers in to judge product requirements with triage and spec writing
How to give agents a computer to verify their own work
How to assess merge risk so you know, at a glance, which PRs need the closest review
We’ll cover a process that you can bring to any agent setup. If you want to follow along, check out
Unit 2 of our software factories course
to create your own factory.
Defining a factory
To build our backlog agent, let’s start by listing out the step-by-step sequence an agent should take. Perhaps we’ll write this down as a markdown skill:
Markdown
1. Take in the user’s request, including any links and attachments.
2. Implement the change in the repository and run static checks.
3. Open a draft pull request and send the user a link with a summary.
This is simple enough. And if we attach an MCP service for our taskboard app (GitHub, Linear, Jira, etc), we could review the output from where we’re working as well.
Still, this isn’t the
most
deterministic way to write this. What if we want to enforce the structure of inputs and outputs at each step? Or offload different steps to different agent sandboxes to manage the context window? Or compile these steps into a nice visual or state diagram?
To gain this flexibility, let’s translate these steps into a YAML template.
Here’s one representation we could use, following the “blueprint” format in
Warp Factories
:
YAML
blueprint:
  worker: foreman
  start:
    to: implement
  stages:
    implement:
      worker: builder
      inputs: |-
        request: the requester's ask in its exact words, with links and attachments.
      outputs: |-
        pr: the pull request that was opened or updated.
      prompt:
        file: stages/implement.md
      to: handoff
    handoff:
      worker: foreman
      inputs: |-
        report: the builder's result, summary, and links.
      prompt: Deliver the PR to the requester.
      to: end
Let’s break down the properties:
The
prompt
tells the agent what to do at that stage. We keep the implementation prompt in a separate Markdown file so it’s easy to amend as we go. At this point, it just asks the agent to implement the change and run static checks. The
to
field indicates where work goes next.
The
inputs
describe what a stage expects to receive. Here, implementation gets a
request
containing the user’s ask, along with its links and attachments. The
outputs
describe what it should hand back: in this case, a
pr
.
Lastly,
workers
are separate sandboxes where you can assign a stage of work. This example uses two, each with its own context window: a foreman that engages with the user, and a builder that writes the code. That gives us a front-door agent we can ask for updates while the backend agent works uninterrupted.
There are two useful benefits to writing the workflow this way. First, we have named inputs and structured outputs, so each run is asked to return the same shape of result.
Second, we have a format we can visualize as work flows through the system. We’ve built a visualizer around this format in Warp, so you can follow the stages and see which worker is handling the task:
A preview of a more complex software factory, with additional steps for triage, spec-writing, and review.
This also lets us, say, generate debugging tools to understand which agents are working on which steps in the pipeline.
Here’s a preview of our own debugging tools to track work performed by the “foreman” and “builder” agents in our 2-agent pipeline here:
A run in Warp showing the foreman and builder timeline as implementation finishes and the PR moves to handoff.
Course example
.
Test the code quality
Now that we defined our factory, let’s put some real work through it using an issue backlog.
First, we’ll need a trigger to bring that work into the factory. Here’s a sample definition from Warp Factories, which starts a factory task whenever a GitHub issue gets the
factory
label:
Markdown
---
triggers:
  - provider: github
    event: issue_labeled
    filter:
      repos: [YOUR_GITHUB_ORG/my-markdown-app]
      labels: [factory]
      skip_bots: self
---
Use the issue that triggered this run as the request:

- author: the requester
- URL: the issue this work tracks; link the pull request on it
- title / body: the description to follow
Here’s what that looks like after sending a backlog of ten issues through the factory:
One run per labeled issue, with links to the issue and resulting PR.
Course example
.
This works pretty well for small, well-defined fixes. For
this native desktop application
, a small implementation using an open weight model cost under a dollar per issue.
But for deeper feature work, these PRs demand a second look. If you just tell an agent to “go build,” what product decisions is it going to just vibe out?
Introduce human judgment with triage and specs
Take this issue for our application here:
In the file sidebar, add a way to expand or collapse all folders at once.
The problem statement is clear, but if I got this issue on my desk, I would probably ask some questions first:
Do we even want to add this new affordance in the product?
If so, where should it live? A new button in the sidebar, a right-click option on a folder, the View menu in the macOS menu bar, somewhere else?
The problem is, our backlog agent is eager to write code no matter the ambiguity. This is the PR we received on the other side after sending this issue along:
Well, it’s a working solution. But personally, I’d prefer a single toggle button instead of separate controls, or I’d move the option somewhere quieter, like the application’s menu bar.
And the more questions a request leaves open, the more likely agents are going to get something wrong. This is how you end up with a slop cannon: agents pumping out changes without human judgment. We need a way to “gate” our implementation agent before it runs wild.
Let’s add two stages ahead of implementation for this:
triage
and
spec writing
.
Triage
serves as the router. It researches the request and decides between three paths:
It’s a well-defined change that can proceed straight to implementation
It’s a feature with open product decisions that deserves a collaboration session
It’s a question that just needs an answer, without implementation at all
If (2) is selected, we’ll proceed to the
spec
stage. This gives the agent room to ask questions upfront and collaborate with the developer on what to implement. Then, the agent will write a spec describing the product behavior and the technical approach for implementation to use. We can encode the whole flow into our blueprint from earlier:
YAML
blueprint:
  worker: foreman
  start:
    to: triage
  stages:
    triage:
      worker: builder
      inputs: |-
        request: the requester's ask in its exact words, with links and attachments.
      outputs: |-
        goal: answer, change, or unclear.
        issue: the issue URL, or the decision that the work needs no issue.
        complexity: the assessed size, and any behavior choices left open.
        spec: whether a spec is needed, and why.
      prompt:
        file: stages/triage.md
      to:
        - stage: spec
          when: A spec is needed, or the requester asked for one.
        - stage: implement
          when: The goal is a change, and no spec is needed.
        - stage: handoff
          when: Otherwise. The request was answer-only, or is unclear and waiting on the requester.
    spec:
      worker: builder
      inputs: |-
        request: the requester's ask in its exact words, with links and attachments.
      outputs: |-
        spec_pr: the draft pull request holding the committed spec.
        decisions: the choices the requester made, and the assumptions recorded.
      prompt:
        file: stages/spec.md
      to:
        - stage: implement
          when: The requester approved the spec.
        - stage: spec
          when: The requester gave feedback on the spec. Revise it on the same branch and pull request.
    implement:
      worker: builder
      inputs: |-
        request: the requester's ask in its exact words, with links and attachments.
        triage: the triage outputs, with the request they came from.
        spec: the approved spec pull request, when there is one.
      outputs: |-
        pr: the pull request that was opened or updated.
      prompt:
        file: stages/implement.md
      to: handoff
    handoff:
      worker: foreman
      inputs: |-
        report: the worker's result, summary, and links.
      prompt: Deliver the result to the requester, including the PR link when there is one.
      to: end
Here,
triage
lists paths for the agent to decide between using the
to
field, and
implement
now expects a triage result and optional spec document as
inputs
.
This spec is used as context for building, and its validation section becomes a checklist for verifying the work later. Our opinionated take is to commit this spec as code, but it can live in-memory too. You can find the sample triage and spec prompts in
“Adding stages for triage and speccing” on our Warp learn course.
When we run the folder request through this flow, the agent comes back with questions, instead of immediately pumping out code:
Surface:
Where should “expand all” and “collapse all” live?
Scope:
Should the action apply to every folder in the sidebar, or just the chosen folder and its descendants?
Open file:
After “collapse all,” what happens to the branch containing the currently open file?
That last question was actually an edge case I hadn’t considered. If you’ve used
Matt Pocock’s /grill-me skill
enough times, you’ve probably had these moments too! And now, the agent is smartly grilling us only when it matters.
For this example, I answered: put it in the View menu, apply it to every folder, and keep the open file’s folder expanded. Here’s the result:
The implementation now follows the approved spec, with Expand All Folders and Collapse All Folders in the macOS View menu.
Course example
.
Give the agent a computer to verify its work
We’ve brought human judgment into the process
before
implementation. Now let’s talk about the other side: verification ahead of PR.
To get the solution screenshot above, I had to pull the branch down onto my machine, run the app end to end, and think through the user flows I needed to click through, all to trust that the PR worked according to the PR description.
Sure, checking out a change locally is fine, even expected when reviewing a coworker’s changes in the pre-AI era. But ask yourself: would you want to pull down a PR that the author hadn’t tested on their own machine? Probably not. So why are we okay with agents doing this?
Let’s teach agents how to test on a computer. This involves computer use, allowing an agent to mock an environment and click around what it's built end-to-end. A number of agent harnesses support computer use today, and
Warp Factories comes with it built into the workers’ sandboxes.
We’ll encode the application-specific instructions as a skill. For this Electron app, our
UI verification skill
describes how to start the app, connect to DevTools, walk the requested flow, and record proof:
Markdown
---
name: ui-verification
description: Prove a user-facing change works by driving the running app with computer use, and add a Visual proof section to the pull request description.
---
# UI verification

Use this whenever a change affects something a user can see or click.

## Start the app

Run `MARKY_DESKTOP_ENABLE_CDP=1 pnpm dev:desktop`.
Read the terminal output for the playground path and DevTools endpoint.
Use the auto-opened editable playground for verification.

## Walk the path

Walk the exact path the request describes. For a bug, show the symptom
is gone. For a feature, show the new behavior and its key interactions.
Use computer use to see and record the app. Prefer the Chrome DevTools
Protocol endpoint for interaction-heavy steps.

## Record the proof

Record a video of the flow. Add a screenshot for a final state worth
inspecting closely. Add a Visual proof section to the PR describing
the path you walked and what each recording or screenshot shows.
If the app cannot launch or the path cannot be reached, say so.

## Gotchas

- Screenshots are DPR 2: CSS pixels times 2.
- Right clicks need real Input.dispatchMouseEvent events; synthetic
  contextmenu events do not open base-ui context menus.
Note: The “gotchas” are useful knowledge the agent has discovered testing this skill over time. I go deeper on how to train agents to track this in
my AI Engineer talk on self-improvement
.
Now, the agent has a skill at its disposal to verify its work before opening the pull request. Here is a sample “visual proof” section our agent added when given this skill, verifying a slide-out sidebar it implemented for narrow screens:
Visual proof attached to a PR: the path the agent walked, a recording, and before-and-after screenshots.
Course example
.
A generated video recording that shows the slide-out menu’s behavior. Warp Factories
automatically edits out dead space and highlights cursor clicks
in the recording.
Assess merge risk
With verification in place, let’s look at that wall of completed factory runs again:
That’s quite a few PRs in our inbox to review; It’s hard to tell which PRs are high risk, which are incomplete, or which are ready to merge after a quick review of the description. I need some way to assess this without clicking into every diff.
That’s where merge risk assessment comes in. We’ve put our approach into a skill you can
download at warp.dev/merge-risk
to try for yourself. It has the agent evaluate its work across five categories:
Alignment:
Does the code match the PR description and issue, or did the worker include undocumented drive-by changes?
Impact:
What is the blast radius, for example an isolated view versus a shared component library, and does it touch sensitive areas like auth, permissions, or database schemas?
Verification:
Was the behavior verified with computer use, end-to-end tests, and unit tests?
Rollback cost:
Is this a two-way door, such as an easy commit revert or feature flag, or a one-way door, such as a destructive schema change or broken persisted state?
Error detection:
If something goes wrong in production, will it report to monitoring or logs, or are errors silently swallowed?
The skill combines those verdicts into a low, medium, or high risk score and calls out the gaps that increase risk. You can pull out these assessments into GitHub labels, PR description items, or a full report as a GitHub comment.
It’s also worth asking the implementer to run this skill
before
opening the PR. That gives it a chance to mitigate risk early, such as adding missing error logging or collecting verification evidence, and then include the assessment in the handoff. We add this to our own implementation prompt:
Markdown
Before opening a PR, use skills/merge-risk/SKILL.md to mitigate risk
ahead of PR, if possible. Report the "Impact" and "Rollback cost" as
sectioned headings in the PR, with a **Verdict** matching the risk
for that category, and a brief summary for each.
Now the PR description carries the visual proof, impact, and rollback cost alongside the implementation summary.
Here’s an example of a well-formatted PR
that covers verification, impact, and rollback cost.
Keep building the factory
Hopefully this gave you some ideas on how to build a software factory that you’d trust to start pushing out PRs. As long as you cover a) structured workflows, b) human judgement, and c) verification, you’ll have all the tools you need.
From here, there’s so much more you can do. Our team has already started
benchmarking different versions of code review ahead of opening a PR
, introducing a research agent with a separate context window to improve token efficiency, and adding bespoke runners for macOS to test native iOS apps.
If any of that interests you, take a look at
Warp Factories
and work through
our Learn course
to build these workflows yourself. It goes deeper than this guide, with full code snippets and examples you can use to build a factory of your own.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Nov 19, 2026
|
Engineering
7
min
Becoming a factory engineer
7
min
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
View all articles
