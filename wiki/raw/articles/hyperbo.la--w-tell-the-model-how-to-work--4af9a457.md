---
title: "Tell the Model How to Work, Not What to Do"
url: "https://hyperbo.la/w/tell-the-model-how-to-work/"
fetched_at: 2026-09-01T10:00:44.025175+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Tell the Model How to Work, Not What to Do

Source: https://hyperbo.la/w/tell-the-model-how-to-work/

I’m not sure who needs to hear this, but I just don’t use
skills
at all. Zero
skills in my repos.
The reasoning models inside coding agents are fundamentally trained to follow
instructions. Skills are a way to supply instructions, but they’re privileged in
the post-training sense: files on disk wired in as skills get very high
instruction-following fidelity via rewards during RL. That can straightjacket
the agent, especially when skills are bound to specific tasks and workflows.
The magic is their reasoning capability. The instructions I want to give agents
are mostly theory-of-mind stuff: how to think about the world they’re spawned
into, how to ground themselves, and how to
find their own instructions
to
follow.
Broad knowledge of software architecture does not make a model locally correct.
Pretraining gives it many possible ways to solve a problem, and post-training
shapes which of those possibilities it reaches for by default. The model still
has no way to know which choices this repo accepts as good until that context
enters its attention. The
harness
supplies that context so I can get out of
the way.
Daniel asks
how I give agents long-term preferences around what good,
done, and high quality look like. I put those preferences in files in the
agent’s environment. The agent pulls them into context when they are relevant.
Those files explain how to think about the work, what good looks like, and what
done means. This is why I keep pointing to
AGENTS.md
as a
map of the
environment
. The model decides how to execute. I tell the model
how to work,
not what to do
.
As
Miguel Branco put it
, “Teach them
what ‘good’ looks like
and let
them work.” Typical skills prescribe specific workflows, which can make agents
mechanically follow every step even when a step is unnecessary or the situation
calls for an exception. Those instructions consume scarce context and bias
downstream reasoning before the agent has considered the situation in front of
it. No amount of making the model better will obsolete the need for
in-context
learning
.
I use zero skills because the agents are already
generally capable software
engineers
that can learn the job. I give them the local context in ordinary
files and let them work.
