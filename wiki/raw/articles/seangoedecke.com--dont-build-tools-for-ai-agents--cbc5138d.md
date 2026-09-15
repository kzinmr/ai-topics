---
title: "Don't build tools for AI agents"
url: "https://seangoedecke.com/dont-build-tools-for-ai-agents/"
fetched_at: 2026-09-12T10:00:56.293512+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Don't build tools for AI agents

Source: https://seangoedecke.com/dont-build-tools-for-ai-agents/

Lots
of
people
are making the case that we should stop building software for human users and start building it for AI agents. This kind of makes sense. For instance, my AI agents now use Datadog way more than I use it myself, purely by virtue of them moving much more quickly and running in parallel. But I think most attempts to build “X for AI agents” are going to fail. Here are three reasons why:
First,
tools that are good for AI agents are also good for humans
. If you took a popular software product — say, Jira — and tried to redesign it for AI agents, you would end up with something very similar to Jira. Agents use a computer in the same way human engineers do, by entering text and making API calls. They ingest new information in the same way humans do, by reading and viewing images. They prioritize and delegate and categorize in the same way humans do. This isn’t intrinsic to how AI works — we could potentially design agents that are more inhuman — but human-like agents are pound-for-pound more useful in our current world.
As an example, let’s imagine that
humanoid robots
have become ubiquitous. What kind of tools would you build for them? Well, they’re shaped like humans, with human hands and limbs, so tools that are great for humans will also be great for robots. It’s a self-reinforcing cycle: if you’re building a robot, you should make them humanoid so they can do a wide range of human tasks
, and that means they’ll be best suited to use human tools. The same principle applies to AI agents.
Second,
being in the training data is a huge advantage for existing tools
. Suppose your new tool for AI agents is 20% better for them than the equivalent piece of software for humans. If the benefit of the agent
already knowing the human software
is greater than 20%, they shouldn’t use your new tool. This is why I’m always suspicious of plans to develop a new programming language for AI agents. The agents have billions and billions of tokens of knowledge about existing programming languages, including their libraries, patterns, and idioms. It is going to be very hard for them to be as effective in a brand-new language.
Third,
we don’t yet know the ideal ergonomics for AI agents
. There are lots of
just-so stories
floating around (like that AI agents prefer statically-typed languages because the feedback loop is tighter), but when you
actually measure
it seems really unclear which tools agents use better. You can construct a plausible story in either direction: Golang is a great agent language because it compiles quickly and is statically typed; Golang is an awful agent language because it requires extensive boilerplate which clogs the context window. It’s also changing so quickly: last year, one primary worry with AI agents was keeping the context window small, but in recent months compaction has become so good
that you can re-compact a
272k
context window almost unlimited times.
There are still some ways you can and should position your tool to be usable by AI agents. Having a way to expose information in plain text or Markdown, building a functional API, implementing MCP servers or CLIs, and so on: these all make it easier for current AIs to use your tool. But these are all improvements on the margin, not fundamental redesigns of the product. Right now, “building for AI agents” just means “we’re prioritizing the API over the UI”. And it’s not even clear that that’s a durable strategy. Now that GPT-6-Astra is getting really good at computer use, the gap between tools-for-AIs and tools-for-humans is closing.
Here's a preview of a related post that shares tags with this one.
They really do think AI might kill everyone
A recent
resignation tweet
from an Anthropic researcher has everyone talking about the AI apocalypse again. Among other things, he said:
The people building AI earnestly believe that it could kill us all by the end of the decade.
Many people found it hard to believe that AI researchers think this way. Some explained it as a
PR campaign
to promote AI regulation, or as
self-promotion
, or as a way to
boost
AI company stock prices.
Others
felt
it had to be impossible, because if you really believed this you’d be bombing datacenters instead of posting on Twitter.
Continue reading...
