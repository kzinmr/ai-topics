---
title: "Thoughts on starting new projects with LLM agents"
url: "https://eli.thegreenplace.net/2026/thoughts-on-starting-new-projects-with-llm-agents/"
fetched_at: 2026-06-07T07:01:35.496166+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Thoughts on starting new projects with LLM agents

Source: https://eli.thegreenplace.net/2026/thoughts-on-starting-new-projects-with-llm-agents/

A few months ago I wrote about
using LLM agents to help restructuring one of my
Python projects
.
It's worth beginning by saying that the
rewrite has been successful by all reasonable measures; I've been able to
continue maintaining that project since then without an issue.
In this post, I want to discuss another project I've recently completed with
significant help from agents:
watgo
. In
this project many things are different; most notably, it's a from-scratch
project rather than a rewrite, and it uses a different programming language
(Go). This post describes my experience working on the project, and some lessons
learned along the way.
The process
This is a new project, so it required extensive design. I began by iterating on
the design with the agent, with a sketch of the API. For this purpose, I
recommend using a Markdown file
committed into the repository
for future reference.
After that, I started asking the agent to write CLs  in a logical order that
made sense to me, keeping them small
and reviewable (more on this in the next section). Sometimes it's not easy to
have a small CL, and multiple rounds of revision may confuse the agent;
in this case, I commit the CL and then go back and ask the agent to modify
or refactor the code, as much as needed, with separate CLs. In the worst case,
the whole sequence can be reverted if I feel we've taken the wrong direction
(branches could also be helpful here for more complicated scenarios).
This point is worth reiterating: sometimes a single CL is a huge step forward,
but requires lots of review, cleanup and refactoring to be viable. I've had
multiple instances where an agent produced several days of work in a single
CL, but I then spent hours instructing it to clean up and refactor. Overall,
it's still a productivity gain, just not as much as some pundits would like us
to believe.
Keeping the human in the loop
Given the current state of agent capabilities, I think it's worth splitting
projects into two categories:
Low importance / prototype / throw away projects where deep code
understanding is unnecessary. These can be "vibe-coded" (submitting agent
code without even reviewing it).
High importance projects that I actually want to maintain; here, vibe-coding
is ill advised and I insist on reviewing and guiding all code the agent
writes before it's submitted (or shortly after, as discussed above).
The
watgo
projects is a clear example of (2): I certainly intend to maintain
this project in the long term, so I insist on code that I understand. With very
few exceptions, no code gets in without full review and often multiple rounds
of revisions.
Even if the cost for writing code went down, maintaining a project is so much
more than that. It's triaging and fixing bugs, it's thinking through what needs
to be done rather than how to do it, it's keeping the code healthy over time,
and so on. As
Brian Kernighan said
:
Everyone knows that debugging is twice as hard as writing a program in the
first place. So if you're as clever as you can be when you write it, how will
you ever debug it?
Maybe at some point agents will become good enough that projects in category
(2) can be implemented and maintained completely autonomously. Maybe. But
we're certainly not there yet. My hunch is that getting there will require
crossing the AGI line , after which little in our world remains certain.
Practical workflow
If you're using an agent to send an actual PR and only review
that
, it's
difficult to be disciplined enough to actually perform a thorough review. I find
the following method to be more reliable:
I use a CLI agent running locally in my repository, and ask it to update the
code there. In parallel, I have a VSCode window open in the same project, where
I can:
Review the agent's changes using VSCode's diff view
Make my own tweaks and code changes if needed
Once I'm pleased with the change, I manually create a commit.
Keeping the CLs small
As mentioned above, it's imperative to keep making progress in small chunks,
with small enough CLs that a human can fully understand in a single review. It's
very tempting to sprint ahead submitting thousands of lines of code every day,
but this temptation has to be avoided. Coding with an agent is like
speed-reading; yes, you're making more progress, but comprehension suffers
the faster you go.
Particularly for refactoring, agents still take the shortest route to
destination. It's important to guide them to think about the "big picture" at
all times, find all instances where X is better done as Y, not just a single
place noticed during a review. This is why it's sometimes OK to have
a CL submitted before you fully agree with everything, and go back to it later
for several refactoring rounds. Source control works amazingly well when
pair-coding with agents.
Testing strategy
It's a key point discussed in every "how to succeed with AI" article, but
still critical enough to reiterate here: a solid testing strategy is absolutely
crucial for success. Agents produce - by far - the best results when they have
a solid test suite to test their code against.
With the
pycparser
rewrite, I had
a large existing test suite. For
watgo
,
the very first thing I did was think through how to adapt the test suites of
the
WASM spec
and of the
wabt project
for my needs.
If your project doesn't have such tests to rely on, this should be your first
order of business - finding one, or building one from scratch. Beware of
self-reinforcing loops though; it's dangerous to trust agents for both the
tests and the implementations tested against them.
Language choice - Go for agent-written projects
Go is a fantastic language for agents to write, because it's designed to be
very readable by humans. The biggest strengths of Go
are exactly what makes the experience of reviewing agent code so positive:
Go changes very infrequently, so you don't have to wonder "are we using the
most modern / idiomatic approach" or "what the hell is this construct"
as often as with other languages (looking at you, Python and TypeScript).
There are relatively few ways to accomplish the same thing in Go, further
lowering the mental burden.
The standard library is rich and there's much less need to keep abreast of
the package-everyone-uses du jour.
In general, Go is designed for readability, with a mild-but-still-strong type
system, uniform formatting, explicit error propagation and opinionated choices
already made for you.
Since most of the time spent by humans when using agents is
reading
rather
than
writing
code, these effects compound and produce a great experience.
Recall the discussion of how some languages are optimized for writability (Perl)
while others are optimized for readability (Go)? Well, when working on a project
with an agent we live in a world of 99% reading vs. 1% writing, so this really
matters.
I find this aspect really crucial in light of the earlier points made in this
post - namely, keeping the human in the loop by understanding and reviewing
all of the agent's design choices and code.
Final thoughts
If you're working on a subject that's completely new to you, I would strongly
recommend
against
the approach described in this post. To really learn
something, you have to work through it from scratch, yourself, reading,
designing, writing the code. Agents don't change this basic fact; even before
agents, if you wanted to learn X, copying it from Stack Overflow or some other
project clearly wasn't the right way to go. Similarly, while agents can be used
as a prop for learning, they cannot learn
for you
.
As a corollary, junior engineers should exercise
extreme caution
when relying
on LLMs. There's no replacement to hard-won experience and the sweat and tears
of learning new, challenging topics. Learning is supposed to be hard; if it's
too easy, you're probably not learning.
For senior engineers, agents are a boon; it's a great tool to increase
productivity, avoid the boring stuff, and get unstuck from procrastination; but
only when used judiciously.
