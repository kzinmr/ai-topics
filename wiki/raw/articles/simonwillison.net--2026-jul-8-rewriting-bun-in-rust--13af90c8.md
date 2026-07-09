---
title: "Rewriting Bun in Rust"
url: "https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything"
fetched_at: 2026-07-09T07:01:30.412093+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Rewriting Bun in Rust

Source: https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything

Rewriting Bun in Rust
(
via
) Jarred Sumner has been promising this blog post (
since May 9th
) about his Zig to Rust rewrite of Bun for significantly longer than it took him to finish the rewrite.
Honestly, it was worth the wait. This is a detailed description of an extremely sophisticated piece of agentic engineering, featuring dynamic workflows, trial runs, adversarial review and all sorts of other interesting tricks.
Jarred spends the first half of the post praising Zig for getting Bun this far. Then we get to a core idea in the piece, emphasis mine:
Our bugfix list felt bad and I was tired of going to sleep worrying about crashes in Bun. I don't blame Zig for that - other users of Zig don't have the bugs we had, and mixing GC with manually-managed memory is an uncommon enough thing for software to need that no language really designs for it. We wouldn't have gotten this far if not for Zig, and I'll always be grateful.
Until very recently, programming language choice was a one-way decision for a project like Bun.
Everyone knows you should never stop the world and rewrite a large piece of software from the ground up. Joel Spolsky highlighted that in
Things You Should Never Do, Part I
back in April 2000!
Coding agents powered by today's frontier models change that equation.
Why pick Rust? It all came down to those challenges with memory management:
A large percentage of bugs from that list are use-after-free, double-free, and "forgot to free" in an error path. In safe Rust, these are compiler errors and RAII-like automatic cleanup with
Drop
.
A crucial enabling factor for the rewrite was that the Bun test suite was written in TypeScript, which meant it could act as
a conformance suite
. This allowed an agent harness to automate much of the initial port from Bun to Rust, initially as an experiment to try out an earlier version of the model we now have access to as Mythos/Fable.
At first, I didn't expect it to work. A few days in, a high % of the test suite started passing and I saw how much the new Rust code matched up with the original Zig codebase. My opinion went from "this is worth trying" to "I'm going to merge this". [...]
For most of those 11 days (and after), I monitored workflows - manually reading the outputs to check for issues and bugs, and prompting Claude to edit the loop to fix things.
How do you review a PR with +1 million lines added? How do you start to build the confidence needed to responsibly merge large quantities of LLM-authored code?
A language-independent test suite with a million assertions, adversarial code review and when something does go wrong, fixing the process that generates the code instead of hand-fixing the code.
The new implementation of Bun has been live in Claude Code for nearly a month now:
Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good.
A perk of working at Anthropic is that you don't have to pay for your tokens - handy when the estimated cost is $165,000!
Pre-merge, this took 5.9 billion uncached input tokens, 690 million output tokens, and 72 billion cached input token reads — around $165,000 at API pricing.
This whole thing is a fascinating case study in taking on wildly ambitious projects with the help of coordinated parallel agents.
