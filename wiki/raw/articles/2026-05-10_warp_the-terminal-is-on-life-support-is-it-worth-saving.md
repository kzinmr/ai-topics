---
title: "The terminal is on life support. Is it worth saving?"
source: "Warp Blog"
url: "https://www.warp.dev/blog/the-terminal-is-on-life-support-is-it-worth-saving"
scraped: "2026-05-10T01:28:16.611030+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# The terminal is on life support. Is it worth saving?

**Source**: [https://www.warp.dev/blog/the-terminal-is-on-life-support-is-it-worth-saving](https://www.warp.dev/blog/the-terminal-is-on-life-support-is-it-worth-saving)

Product
The terminal is on life support. Is it worth saving?
Zach Lloyd
July 12, 2021
This post introduces Warp, a new Rust-based terminal we have been working on over the past year. Warp keeps what's best about the terminal while making it more modern, accessible, and powerful for all developers.
Why doesn’t the terminal work like the rest of your apps? Developer tools have
evolved towards reusability, composability, and collaboration
. Meanwhile, terminals are
inherently single-user, linear, and ephemeral
.
For instance:
Developers work in teams, but terminals don’t support collaboration
Developers rely on sharing knowledge, but all my terminal work disappears every time I close a session
Developers work across machines, but my terminal environment is tethered to my computer
Developers are becoming accustomed to nice interfaces, but the terminal inflicts pain and makes me feel like an idiot when I try to do moderately complicated things
In spite of these obvious shortcomings, terminals persist!
A lot of developers swear by them.  And I understand why: if you know what you’re doing, the terminal’s text-based interface is fast, efficient, composable, and programmable.  Terminals are awesome power tools.
So we have an interesting situation: terminals are both obviously useful and highly antiquated.  How did we get here? What’s the best way forward?
In the rest of this post, I’ll argue that
Terminals persist because CLIs are the best interface for a lot of developer tasks
Their antiquated architecture has stifled innovation
This has in turn caused terminals to lose share to GUIs
The right way forward is to keep what’s best about the terminal, but modernize it...which is what we are working on at
Warp
And for those who don’t want to read a whole blog post, you can get a sneak peek at Warp up front:
A preview of
Warp
showing blocks, text-editing, native completions and visual hisory.
Terminals persist because CLIs are good interfaces for developers
As a simple example, say you have written a program and suspect it’s leaking file handles but aren’t sure.  If you are comfortable in the terminal you can run a few commands to see what’s going on:
First you can find your program’s process id using ps and grep:
ps aux | grep {program-name}
Then you can see how many files it has open:
lsof -p {process-id} | wc -l
And you can use
watch
to track this over time to see if your debugging theory is right.
A GUI is almost all downside for this use case.  Slower, less-flexible, won’t work over ssh, etc, plus it would be a pain to build.  There are lots of developer tasks like this.
Even though capital-letter CLIs have a lot of use-cases, the current implementation of the terminal is really bad for reasons mentioned earlier - no collaboration, transient sessions, bad UX, etc.
Consequently, terminals are losing developer market share to user-friendly and modern GUI apps like VSCode, Postman, and more.
Why hasn’t anyone already fixed the CLI?
People have tried, but the terminal architecture makes it really difficult to innovate.
Terminals and shells only support the character-in-character-out protocol of a teletype, a piece of hardware that hasn’t been used in most new developers’ lifetimes. Specifically, the terminal sits on one side of a
PTY
and the shell sits on the other. Between them flows a sequence of characters.   The only structure in place is a set of character codes that control how the terminal lays out and paints its buffer.
Because shells are responsible for parsing input and running programs, terminals don’t know even basic things about what's happening; e.g. what separates a command from its output from the next command?  Was the command successful? What text was written to stdout vs. stderr?
Terminals have a knowledge deficit.
Conversely, shells have a much richer understanding of all this, but they have extremely limited capabilities on the UX side.  They can't handle mouse interactions or render graphics, like for instance a completion UI.
Shells have a capability deficit
.
A vt100, 1978, what your terminal app is emulating
As someone wanting to modernize "the CLI", you are faced with the fact that there actually is no single CLI app – there are terminals and shells.  Trying to fix the experience at the shell level can be somewhat effective – e.g.
ohmyzsh
,
fzf
,
thefuck
– but it can never fix fundamental accessibility issues and it will never make the terminal feel like a modern app.
In order to really modernize the CLI, you need to start with the terminal, and keep pushing further and further into the world of shells, ultimately ending up with a better integrated experience.  This is hard, but we think it's worthwhile because of the productivity gains it will unlock.
Warp: a more accessible, powerful terminal
At
Warp
we are building a new Rust-based terminal that keeps what’s best about the CLI while modernizing and upgrading the experience.  One awesome thing about how we are building it is that it works with your existing shell so it's easy to try.
If you’re interested in how we are pushing the technical limits, please give
How Warp Works
a read.
A quick preview
Rather than a single buffer, we divide terminal output into a sequence of commands - making it easy for them to navigate, copy, save, and share units of work.
Warp is a block-based terminal
We make input more familiar and usable, replacing the character buffer with a full-fledged text editor built in Rust, and equipping it with intellisense-like autocomplete:
Built-in completions and documentation
And finally, we want to transform the terminal from an inherently single user utility into a modern collaborative app where sessions, blocks, and environments are all persistent, searchable and shared by link (being very mindful of security and
privacy
).
Real time collaboration and session sharing (coming soon)
These types of features are just the start, and part of a larger set of principles we have for improving the terminal’s CLI.
If you’re interested in learning more, please check out our
site
and request early access here.  We are still in the early days of implementing our vision but would love feedback and input as we move forward.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
