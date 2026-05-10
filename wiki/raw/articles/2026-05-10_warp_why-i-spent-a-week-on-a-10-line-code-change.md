---
title: "Why I Spent a Week on a 10-Line Code Change"
source: "Warp Blog"
url: "https://www.warp.dev/blog/why-i-spent-a-week-on-a-10-line-code-change"
scraped: "2026-05-10T01:28:25.770959+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Why I Spent a Week on a 10-Line Code Change

**Source**: [https://www.warp.dev/blog/why-i-spent-a-week-on-a-10-line-code-change](https://www.warp.dev/blog/why-i-spent-a-week-on-a-10-line-code-change)

Engineering
Why I Spent a Week on a 10-Line Code Change
Chuck Pierce
March 29, 2023
Recently, while working on the ability to drag tabs in
Warp
, I ran into a major blocker: trying to drag an individual tab would instead drag the entire window around. Tracking down the source of that bug took more than a week of investigation and experimentation, but ultimately was fixed in a pull request that changed fewer than 10 lines of code! That mismatch between effort and output also drove home an important fact about engineering—building software is about so much more than writing code. Here's a blog post about how it went.
For context,
Warp
is a Rust-based terminal for developers. We built it using our own
custom UI framework,
so we had to build tabs and drag-and-drop from scratch.
On the surface, the question I was investigating seemed straightforward: How do we allow users to drag tabs around without dragging the whole window? This is behavior you can see in Chrome as well as Electron apps with certain settings, so I knew it was possible. However, every time I tried to duplicate the behavior in Warp or in small sample apps, the title bar window drag persisted. It didn’t matter that the title bar was hidden and had no contents, nor that I had drawn something in that space myself.
In an old build of Warp, dragging the tab dragged the whole window.
To investigate this issue, I started with the Apple documentation for macOS APIs. Unfortunately, that documentation doesn’t provide many examples and there wasn’t an obvious single value I could set to prevent the dragging. Similarly, neither basic web searches nor stack overflow provided any help. There was plenty of writing about how to make
other
areas of the window cause a drag, but nothing I could find that would let me turn off the drag for the title bar. What little I could find, I tried in my sample app, to no avail.
Next, I turned to the examples that I knew worked: Electron and Chrome. Luckily, both Electron and Chromium are open-source projects, so I could dig around in their code freely. Unluckily, both projects are complex and it was not at all easy to dive in with no prior knowledge and understand how macOS windows are created by each.
I started with Electron, because I knew that it had an option that could be set to create the behavior I wanted. I followed that option through the code until I found where it was used, and then tried to recreate the changes in the window creation that are triggered by that setting. I tried everything I could find that was different from what we were already doing in Warp, but every attempt was a dead end and I wound up with a bunch more understanding of how Electron worked, but no closer to making Warp better.
Next, I turned to Chromium, which was a much more daunting task since I didn’t really have a starting point. I spent many hours tracing through code search to find snippets of code that seemed to be related. Similar to Electron, every time I found something that looked possible, I would get excited and try it locally, only to be met time and again by the same persistent window dragging.
Eventually, after several days without making meaningful progress towards a solution, I stumbled across
a comment in the Chromium code base
talking about a potential optimization in the dragging behavior. That comment included a link to an issue in their issue tracker. The issue itself doesn’t provide much more context, however it in turn links to
a commit message
that provided the breakthrough I needed.
The commit message that saved the day
That commit message describes in great detail a process—which I haven’t found documented anywhere else—for how macOS determines what sections of a window are draggable. Crucially, it also includes this caveat for the whole behavior:
One more complication: views that underlap the title bar in a window with a full size content view, even if the title bar is hidden, only cut a hole in the drag map if they override
mouseDown
and
return YES for
acceptsFirstResponder
Finally, I had a plausible suggestion that included clear reasoning and helped me understand the problem I was facing better. I included the required settings in my sample application and it immediately worked the way I was expecting! Porting those changes to Warp itself resulted in a tiny PR that has one of the highest effort : change ratios I’ve ever worked on.
The code change I made
Having so much work go into so few changes really emphasized for me how much of software engineering is about achieving deep understanding rather than speed of writing code. When debugging, you need to build a strong model of what is going wrong so that you can fix the actual problem and not only the symptoms.
Last, the fact that the critical information was ultimately found in a commit message where an engineer documented their understanding for future developers made the value of sharing knowledge crystal clear. While finally having that “Aha!” moment after days or weeks of debugging can be deeply rewarding, helping your team and future maintainers avoid that work in the first place is even better! Additionally, I am grateful for the open-source community for providing code examples and documentation we all can learn from.
In the current build of Warp, tag dragging drags the tab!
If you're interested in trying out the drag-and-drop behavior or trying out a modern Rust-based terminal, download
Warp
here:
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
