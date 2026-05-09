---
title: "The Coding Agent Is Dead"
source: https://ampcode.com/news/the-coding-agent-is-dead
date: "2026-02-19"
scraped: "2026-05-09"
author: Amp (Thorsten Ball / Sourcegraph)
tags:
  - coding-agents
  - agent-harness
  - model-capability
  - commoditization
  - amp
---

# The Coding Agent Is Dead

**Source:** https://ampcode.com/news/the-coding-agent-is-dead
**Published:** February 19, 2026

The current generation of coding agents is dead. The heart is still beating,
yes, but the bullet has already left the chamber. This generation isn't the
future.

With the newest models, the agent — the prompts and tools you wrap around a
model — is no longer the limiting factor. These models can be powerful with
nearly any tool you throw at them. A simple tool called `bash` is often enough.
Whether you show LSP diagnostics here or there is dwarfed by what these models
can do through sheer brute force. As long as it mostly gets out of the way,
nearly any agent can get good results out of them. These new models barely
need to be told how to act like coding agents anymore. They're now fully
trained for that.

How you organize your codebase for agents, how your organization uses them —
those are now the bottlenecks.

The frontier has shifted. And we're going to make massive changes to Amp so it
stays on the frontier.

It's tempting not to. Amp is growing faster than ever. We could stay, keep
things as they are, pretend that the coding agents of February 2026 are the
final form and watch the numbers go up. We could say yes to more VC money and
sell $2,000 worth of tokens for $20 a month.

But what would that buy us? A local maximum. And while we're sitting on top of
the local maximum, each new model generation would move the frontier further and
further into the distance. And the longer we keep things the same, the more we
select for users that aren't comfortable at the frontier. But the users we want
and need are those who are willing to pack up and travel light with us.

So, Amp has to evolve.

First step: we're going to kill the Amp editor extensions for VS Code and
Cursor. We're unshackling these models from the editor.

By keeping these new models in an editor sidebar, we restrict them. They're now
much more than mere assistants. They no longer need the hand-holding and really
want to kick off their training wheels. They want to write code and run even
when you're not sitting in front of your editor. It's time to see what they can
do without supervision.

**The Amp editor extensions will self-destruct on March 5 at 8pm Pacific Time.
Time to switch to the Amp CLI.**

Because we're keeping the CLI, for now. Its heart is still beating and it helps
us get to where we need to go. Think of it as a ladder: we use it to climb up to
the next level and then we might not need it. It's flexible, light, easy to
change, can be run anywhere and anytime. It attracts the kind of users we're
building for.

For those of you who read "everything is changing" on our landing page back in
April 2025 and nodded, this is nothing new. Our only promise was that when the
frontier moved, we would move too.

The agent. It's no longer a point on a map. It's an arrow. Not a stop, but a
ride. And it might self-destruct too.
