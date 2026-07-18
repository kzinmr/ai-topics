---
title: "Code Reds Need Maintenance Loops"
url: "https://hyperbo.la/w/code-reds-need-maintenance-loops/"
fetched_at: 2026-07-18T07:00:47.165590+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Code Reds Need Maintenance Loops

Source: https://hyperbo.la/w/code-reds-need-maintenance-loops/

At Stripe, I was part of the company’s first-ever Code Yellow: a lighthouse
customer was considering churning to a competitor due to better card acceptance
rates. We pulled together a cross-functional team of 20 people — engineering,
data science, marketing, bizops, card policy, partnerships — and worked for two
months to build the first version of
Adaptive Acceptance
, increasing
acceptance via a multi-armed bandit system for retrying likely-to-succeed card
transactions.
Code red as an operating model
Stripe’s “code yellow” was an instance of a common pattern in technology
companies to “call a code red” to fix a high-priority, near-term issue due to an
upstream planning, staffing, and prioritization failure. The Stripe code yellow
was unusual because it left behind a product. Most code reds leave behind a
postmortem, a tired group of ICs, and a metric that is once again nobody’s job.
Some other code reds I’ve worked on are: bringing per-PR CI times down from 15
minutes to 5 minutes, addressing quadratic degradation of merge queue success
rates, healing enterprise customer reliability SLO breaches, reducing local dev
setup times to keep engineers in flow, and accelerating AI adoption in legacy
codebases. These are all long-running optimization problems. None of these are
one-off failures; they’re systems that naturally drift unless someone
continuously maintains them.
All of the hypergrowth technology companies I’ve worked at run teams very “hot,”
which means there is more to do than headcount to allocate. This leads to
metrics that “fall below the line” and do not get attention, continuous or
otherwise.
1
The work below the line is often important. It represents tail risks and
continuous operational maintenance.
In these situations, I have usually seen organizations respond like this:
A concerned IC or leader flags the situation to an executive.
The executive decides to act to restore the relevant metric to the green zone.
The company declares a “code red” and scrambles to assemble a team of ICs to
address the problem, disrupting in-flight work.
The code red has clear exit criteria; the team executes until metrics match
the exit criteria.
The code red ends and the team disbands; the metric returns to being unmanaged
and unmaintained.
Green is not done
When a tiger team is pulled together to execute on a code red, the organization
is executing an adaptive response.
In addition to fixing the proximate cause of calling the code red, the process
also serves to extract and codify information about how the organization
successfully adapted. During the code red, the assembled humans discover what
the invariant actually is, what signals predict it drifting, what interventions
work, and which judgment calls matter. That understanding should become a
maintenance loop the team leaves behind so the organization can keep the
invariant healthy without requiring another tiger team.
Each code red reveals that some first- or second-order metric is more important
than the organization previously believed. This should result in durable changes
to headcount allocation, but because teams run hot, this generally does not
happen. The business was and remains labor constrained.
Goals and durable ownership, not tasks
Agents make maintenance loops cheap enough that we no longer need to permanently
staff every newly discovered invariant.
Because code reds are very reliably tied to SLO breaches and have exit criteria
defined by restoring those metrics back to baseline, they are very amenable to
being solved with a recent coding agent advancement:
/goal
.
2
/goal
is different from asking an agent to do a task (e.g. “fix this flaky
test”). A goal is a process for doing and discovering work which itself spawns
tasks (e.g. “keep p95 CI latency under N minutes;” “reduce customer-visible
incidents in this subsystem;” or “find and remove the top sources of onboarding
churn”). The loop does not terminate when one patch lands; instead, it keeps
observing the metric, generating interventions, testing them, and asking for
human review when it needs authority.
The loop that builds the loop
The role of code reds, and the ICs working on them, should be to leave behind a
loop (either human, programmatic, or agentic) whose responsibilities include
durable ownership for the newly discovered important invariant. In the world of
agents and
harness engineering
, we can manufacture execution capacity for this
by making a persistent agent fleet maintain these SLOs with a single prompt to
/goal
.
Mechanically, this can look like a text box that accepts a prompt, spawns 50
persistent cloud agents, and passes that
/goal
to agent sessions continuously
for every commit to main, or every day with customer retention deltas, etc.
The IC role moves up a level
During the code red, the job is not only to get the metric back inside bounds,
but rather to understand why the metric was able to drift, what human adaptation
was keeping it healthy before, what signals those humans were watching, what
actions were available to them, and which parts of that loop can be made
durable.
The discovery loops
There are other parts of the code red operating model that can be exploded in
this way. One such further application is to use this same
/goal
infrastructure to hunt for things to
/goal
on!
An agentic system reduces dependence on executive-attention topology from the
discovery process. Today, latent code reds surface through who notices, who has
taste, who has enough standing to escalate, who has the right relationship with
an exec, who can narrate the problem, and who happens to be in the room. The
agentic system might not remove all bias, but it replaces one specific discovery
mechanism — ad hoc social escalation — with a named, inspectable, improvable
process.
A named discovery loop also gives the company something to improve. Today, when
a code red is missed, the diagnosis is usually social and vague. Either the
right person did not notice, the wrong person noticed but could not narrate it,
the exec who would have cared was not in the room, or the concern looked like
local whining until the graph was obviously bad.
A named agentic discovery process gives principals (human and agentic!)
something concrete to tune, such as adding metrics and data sources, changing
the prompt, or highlighting which weak signals matter. The process can then be
taught which false positives are wasting attention.
With fewer constraints on execution, this role of code red discovery would
likely be taken by someone in bizops if it could possibly be above the line. The
existence of higher-order
/goal
execution infrastructure probably means hiring
such a person is even more compelling for the business since they can have much
higher utilization and impact.
Code red success
The code red operating model made sense when the only durable way to own one of
these invariants was to allocate a team to it. In that world, most discovered
invariants returned below the line because durable ownership was too expensive.
Agents change that cost. The work that used to require an indefinitely staffed
team can sometimes become a goal, a harness, and a review loop that keeps
running after the borrowed humans go back to their roadmaps. This should change
how code reds are allowed to end.
