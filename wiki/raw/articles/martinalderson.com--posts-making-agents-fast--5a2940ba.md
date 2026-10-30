---
title: "Making agents fast - what I've learnt over the last 12 months"
url: "https://martinalderson.com/posts/making-agents-fast/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-10-30T10:00:47.651000+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Making agents fast - what I've learnt over the last 12 months

Source: https://martinalderson.com/posts/making-agents-fast/?utm_source=rss&utm_medium=rss&utm_campaign=feed

I've spent a lot of my career optimising websites and apps to run faster, and it's been interesting to apply some of those principles to agentic workflows. I'll run over some of my key learnings - there's many more I want to get written down at some point, but for brevity I think this is my rough mental model of tackling this.
Inference speed
The obvious thing to start with is inference speed. This has two key components, which will be familiar if you have done any backend API optimisation.
The first is TTFT (time to first token). This is analogous to TTFB (time to first byte) in web servers, namely how quickly does the first token come after you've done a request. This includes prefill (input token processing), so this scales with how many tokens the agent is sending to the inference provider too - so you
should
expect to see (potentially significant) variance on this number, much like you'd expect TTFB to be higher on an endpoint that e.g. has to do more database calls to prepare the response. A lower TTFT is better.
Prompt caching is, of course, absolutely vital to this. Cached tokens are much faster (and cheaper!) to serve. Most agent harnesses handle this well these days - it's been a while since I've ever seen issues with this. Obviously worth keeping an eye on, but it matters less than I predicted in real world experience.
The second is tok/s (tokens per second), which measures how quickly tokens
come back
once the response starts. This is closer to bandwidth on application servers, where a higher value is better.
How relatively important each are depends on what kind of responses you're expecting back from the LLM provider. For example, if you are sending back and forth lots of short responses between turns in your agentic workflow, TTFT is likely to comparatively be of greater importance than tok/s. Equally, if you are having the LLM output longer responses (say, code or documents), then TTFT is likely to be less important than tok/s.
Illustrative numbers. TTFT is network, queueing and prefill - the wait before anything comes back. Tok/s is how fast it streams once it starts.
Knowing which number you need faster is important when comparing models and inference providers. Smaller models are generally faster than big ones. But between providers of the same model, there is an
enormous
delta in speed. OpenRouter does provide public data on inference providers, but keep in mind this is an aggregate that may only roughly match your real world use.
The main issue that tends to crop up is that providers also tend to vary in speed a lot depending on the time of day and how much load they are under. Big leaps in TTFT (for similar length prompts) can indicate queuing on the provider side, but can also mean your requests are being allocated to slower hardware or more users competing for prefill compute.  Equally, slowdowns in tok/s can mean slower underlying hardware or higher batch sizes at the provider. Either way, there is a
serious
"noisy neighbour" factor on many inference providers.
Of course, many providers offer different tiers of service. For example, OpenAI offers a 'flex' tier alongside their standard and 'fast' tiers. These allow you to trade speed for cost.
But don't overlook the impact of thinking budgets. A "fast" tier model with thinking set to maximum or xhigh will be
vastly
slower than a "slow" tier model with low or medium thinking. I'm guilty of constantly overlooking thinking budgets when looking at this stuff, but it makes an enormous difference. It's easy to be drawn to the quantitative tok/s and TTFT values when in reality reducing thinking can completely dwarf it - if suitable for your task.
But it's not all about inference speed
While having fast(er) inference never hurts, it's worth noting that it's often
not
the biggest part of the speeding up agents, and can be expensive to speed up (paying for faster tiers), or painful to move inference providers (if you have committed spend or contractual requirements).
Rough numbers again, but halving inference time only takes 20% off the task when provisioning, tools and suspend/resume stay the same.
It's good to start looking at your tool calls in more detail. This is much more classic performance optimisation work. But I've noticed things being slow that are not usually slow. A classic example is an agent running
xargs -I{}
over large amounts of files, which causes hundreds of thousands of new process invocations. This can be painfully slow, especially on sandboxed environments.
So while classic software performance engineering applies as per normal to agent tool calls, you need to investigate tool call traces to see what the agent does. It will often chain a bunch of bash commands together to achieve a result and it can be not obvious to see which part is causing slowness.
strace
is helpful here, but not ideal to run all the time as it
itself
has a performance overhead.
Tool output size matters too. While most agent harnesses are pretty strict at stopping
cat
-style commands from blowing up your context window, as mentioned before uncached input tokens directly impact TTFT. SQL-style data sources have a big advantage if you can give your agent access to these - as it can request exactly what it needs without risk of a broad
awk
returning thousands of tokens of unrequired data.
Equally, given many agents start a new shell on
every
command things in your
.bashrc
that are not usually an issue can become a real issue. Be careful about what a shell needs to launch - especially if you have nvm or similar in that. Before you know it you can be spending dramatically more time
starting
the shell than
running
the command.
Build the tooling your agent wants
Building on from the obvious "make this command faster", I think the next step is to think hard about what tooling your agent needs, but is having to "work around". For example, if you have it doing a lot of
xargs
over markdown files over and over, it is potentially better for that data to be in a database it can call with full text search.
This is where things differ a little in my mental model of software optimisation. Usually you look at a request, look at what it's doing, and try and make each part faster, and rinse and repeat. With agentic workflows, you can often just
observe
what the agent does, and deduce what would work better. So purely looking at tool call traces can be misleading.
I've found that open weights models have a massive advantage here as you can read their thinking traces. While CoT traces are well used by the labs trying to work on safety and alignment, it turns out they are great for coming up with ideas to optimise the tools you give the agent.
The way I've worked with this is getting a list of slow calls, and looking at the thinking blocks just before this. You'll usually get some blindingly obvious "hmm, could do x, but no y" style thoughts. And you can just
give
the agent what it wants, and see how things work out.
The other thing that can make a big difference is treating
for
loops with
sleep
as a red flag. This is an indication that the agent wants to be
notified
of something but is instead having to poll for it. Often agents will poll for something that is quick but they tend to set a 10 or 20s minimum wait on the for loop. This can be solved with prompting sometimes, but often it can be an indication that (usually external) services need a async way to fire back task completion.
Finally, parallelisation is a big help in cutting down speed of tool execution. Adding a simple "try and parallelise tool calls in $TASK" can work wonders, but especially with weaker models risks the agent making mistakes and undoing any efficiency gain. As such, providing tools (CLI or MCP) that do the parallel steps for the agent can be worthwhile.
A quick hardware reminder
In my career, primarily driven by cloud computing platforms, I've often found the easiest quick fix is to just use faster hardware. And by faster hardware I do
not
mean a bigger AWS instance - dig into the underlying hardware your agents are running on. That means looking at the exact CPU core type you are using (the Zen 4c/5c cores can be much slower than the full sized ones), clock frequency and file IO speeds.
This depends heavily on the tasks you're doing with your agents, but if they need to write a lot of custom code or doing a lot of data analysis, making sure the underlying hardware is fast can help a lot.
For example, if your agent needs to do quite IO-heavy tasks, you may find a lot of your slowness is coming from networked disks. Having faster (local) NVMe disks may offer many, many orders of magnitude faster IO performance.
This is often worse in many sandboxes. With things like copy on write and other snapshotting techniques, there can be a lot of overhead on file IO. Slow underlying IO just makes everything worse.
Suspend and resume
I often see real speed issues with suspend and resume. Not every agentic workflow uses it, but if you (for example) allow agents to pause for a human in the loop approval, you need to be careful with optimising suspend and resume.
MicroVMs can often resume
on paper
extremely quickly, but actually have pages streamed in on first access. So you need to measure not just what the MicroVM says but how quickly new inference requests are starting after resume.
Being careful with memory management is the crucial thing here. While you don't want to starve your VMs of RAM and thus cause swap or OOMs, it's worth investigating what is using RAM during a suspend. If you have for example headless browser sessions active, it's almost certainly worth killing them before suspending, as is any running server processes the agent may have built.
As always, the key thing is to measure and track RAM usage and break it down over time if you are using a lot of suspend/resume cycles.
Finally, check the network. It's very common in my experience to have broken IPv6 in sandbox environments, and you end up with network timeouts while it does a AAAA lookup on DNS, which adds a small overhead to every request. Basic hygiene stuff like this adds up over the course of an agentic session.
Key takeaways
I think the key things I'd check on any agentic optimisation project are:
Inference speed is nuanced, and knowing what part of inference you rely on most for speed is important.
Check thinking budgets! This is overwhelmingly the lowest hanging fruit
Read traces, and if you are using open weight models read the CoT thinking traces. They often have so much valuable insight into what the agent is wanting to do
Give the agent the tools
it wants
rather than what you think it
needs
Don't overlook the basic stuff. Faster hardware still matters, sandboxing and microVMs open a whole world of potential performance footguns, parallelisation helps and classic software performance optimisation is as relevant as ever.
As always, this space is also evolving fast. Keeping up to date with the field has always been my guiding north star in making sure you can keep stuff fast.
I'd love to
hear from you
if you're working on making agents faster. I'm especially interested if you think I'm missing obvious factors here!
