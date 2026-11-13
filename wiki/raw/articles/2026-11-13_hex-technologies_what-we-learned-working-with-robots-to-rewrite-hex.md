---
title: "What we learned working with robots to rewrite Hex"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/what-we-learned-working-with-robots-to-rewrite-hex/"
scraped: "2026-11-13T06:00:31.709584+00:00"
lastmod: "2026-11-12"
type: "sitemap"
---

# What we learned working with robots to rewrite Hex

**Source**: [https://hex.tech/blog/what-we-learned-working-with-robots-to-rewrite-hex/](https://hex.tech/blog/what-we-learned-working-with-robots-to-rewrite-hex/)

Skip to main content
📈
A new era for Hex, and data
Announcing Hex 4.0, and a $100m fundraise building toward the agent-native future for analytics.
Blog
What we learned working with robots to rewrite Hex
Charlie Imhoff
Engineering
Product
November 12, 2026
Share:
twitter
linkedin
The Hex engineering team recently shipped Hex 4.0. In doing so, we touched (and often rewrote) nearly every one of our foundational systems within a four-month-long push. That means we changed around 250,000 lines of code, which equates to approximately 10% of a 6-year-old codebase. There’s no question that our use of coding agents enabled us to make so many changes so quickly, but we also encountered some key tradeoffs and limitations of agents along the way.
The benefits are pretty obvious:
describing
code enables you to move faster than typing everything by hand. The question then, becomes "at what specificity do I need to describe the code, and at what specificity do I need to review it?" This is, to be blunt, still a moving target that likely varies by organization and by system. Given the current pace of model evolution,I'll probably be looking back on this post like it's a 2024-era prompt engineering guide in about six months.
But in the meantime, we all still need to ship software. So here are some key tips that we picked up over the past few months.
You will not one-shot into production.
Writing good software is
iterative
, and agents
do not change that
.
The robot will almost
never
one-shot anything. It's not a failure of you, your prompt, or the robot's intelligence. The complexities of most software engineering tasks are discovered during implementation, by you or by the robot, and enumerating them upfront is not typically possible. The robot won't complain if you instruct it to do something, change your mind after seeing it, and ask it to do something else. If the result is terrible, the robot may have made an early bad decision you can steer better next time.
Often, it's better to not restart in a new thread each time, even if you revert the changes. Instead, you should maintain the context of the task as you and the robot move through it
together,
unless that context is truly poisoned.
The task is really the same shape as it always has been: write code, read code, refactor code, repeat. The robot’s speed should enable you to iterate
more,
not less.
Be vigilant about coupling
AI agents have no respect for an API boundary.
They will absolutely toss a low-level parameter into a high-level function, just to drill it all the way down to the root of the stack to influence a single log-line. They will tie two implementations together by duplicating logic and hoping it stays in sync. They will ignore a structured API and send a raw untyped request into a hardcoded port. They don't give a SHIT. You gave them a
prompt,
damn it, and they're going to implement it
in the most direct way they see ahead of them.
If you want to create an abstraction, the robots will not do so unless you
tell them to make the specified abstraction
. If you suspect your change will cross or require changing an API boundary, you have to provide guidance on how to handle that upfront. And do not trust the agent to do the right thing at API boundaries.
At Hex we’ve had to remain diligent and principled. We pay very close attention to the signatures of functions. We still care about names. One strategy that's worked has been disallowingthe robot from adding or modifying any exported function signature or data type. That way, the author focuses on writing all the signatures and ensuring they make sense, and then the robot fills in and updates all the function bodies.
No TODO left behind
When tasked to build large changes, a common pattern at Hex is to build toward end-to-end proof of concepts quickly, and then fill in optimizations, quality of life, edge-cases, and unhappy paths later. It's common to see a PR that introduces a new feature act as the
scaffolding
, with lots of TODOs in place. The author and others will independently fill in parts of the implementation later.
This is
really
helpful, because it allows engineers to focus that first review on overall structure, independent of the inner details, while still proving out an end-to-end story. It allows humans to grok the overall shape of a system before it's draped in complexities. It also serves a human communication purpose; a PR with lots of TODOs and gaps in it explicitly clarifies what decisions are being made now, and which are being deferred. It is, in short, an encapsulation of what matters, and what does not.
When asked to build large things, robots are more than happy to build
the whole hog
at once. Every edge case, every optimization, every test. This makes understanding the actual
meat
of the PR difficult, as it can hide key decisions. Robots are not trained to write code that ladders up into production
over time
, they are trained to produce production code
immediately
. They never say "no", even when "I shouldn't worry about this right now" is the correct answer for the PR.
I'll often withhold the complete plan for what a given refactor or change is in service of, so that a robot can't jump the gun. Instead, I'll have the robot generate a plan, and then go prompt other threads with
pieces of
the plan. When prototyping, I instruct the agent to leave TODOs liberally.
DRY? More like DAMP (Damn, A Massive Program).
Two facts: Engineers are lazy, and engineers are not paid by lines of code. This produces a useful economic effect: if you see a snippet of code, you know that snippet of code was deemed important enough to be written. If a PR floats across your desk with 500 lines of bookkeeping you didn't expect to find, you can be pretty confident that the author first tried the code
without
that, and then realized it was worth it.
By contrast, the robots are anything but lazy, and they
are
paid per line—so the robots write
a lot
of code. And because their context windows are small, and searches can be expensive, they don't look for preexisting patterns or solutions unless told to. You'll often end up seeing that robots can find duplicated symbols, but aren’t great at identifying a coherent path to unifying them.
So, it becomes a key part of review to not just look at the
diff
, but recall the system as a whole, and try to identify parts of that diff which missed out on existing tools, functions, patterns, data structures, or refactors which would simplify things. Structural refactors are still very common, as we flatten disparate code into shared abstractions. Few of these are agent-initiated. When it comes to refactoring, it still takes a human Eagle Scout to leave things better than they found them.
Give agents statically verifiable exit criteria
Whenever possible, it's important to ensure the agent has some mechanism in place to validate it has completed a task, and that it hasn't regressed. Provide an exit criteria, and make that criteria deterministic. Tasks that span large chunks of code will exhaust the context window, so it needs some mechanism to keep track of and make progress on as code enters and exits its working memory.
As a concrete example, we recently refactored some code to more consistently handle file paths. APIs dealing with execution files would assume file paths were relative from
project/execution/
but APIs working with app files would assume file paths were relative from
project/apps
. This led to subtle bugs and lots of converting file paths to different stems, so we decided to refactor all the APIs to just accept paths relative from
project/
.
Updating consumers to adhere to the new semantics proved surprisingly **challenging for the robot. All the values were just strings, so there was no way to statically check whether each reader/writer had been updated to align to the new semantics. The agent would frequently get stuck in loops, generally unable to verify it was done and would cycle with broader and broader greps. After some false starts, we decided that the solution was to change the APIs to accept a wrapped string type. This way, all the callers would
statically break,
and the task could then become “fix the build,”with a clear exit criteria and a clear tool call to check progress. Once it was stable, another agent thread removed the wrapping.
You can do one thing at a time
Codex's Cloud agents and Worktree buttons are a siren's song:
🎵 double, triple, 10x your productivity 🎵 turn yourself into a fleet of AI agents 🎵
Tie yourself to the mast Code-ysseus!
Using one agent well is a big productivity boost. Using ten at once will not make you faster, it will just make you very, very stressed. I've limited myself to one, with an absolute max of two.
So what do I do while I wait for my agent? It's pretty straightforward. I read its output while it spins. I steer it,grok its choices, and queue follow ups as if it's getting a code review right when its done. I also write documents, plan architecture, or improve docs. I drink water. And sometimes — and I know this is crazy — I look at pictures of dogs on my phone, and rejoice in the benefits of automation.
Define where you’re okay with YOLOing code
Internally, we've sometimes used the word "procedural" to describe chunks of code that are algorithmically complex but do not contribute to the overall complexity of a system. A good example would be the parsing logic within Hex 4.0. Splitting, iterating over, and parsing token streams is dense code that can span hundreds of lines, but it's ultimately very simple to test, and very simple to consume. It has a single, clear entry point and it produces obvious results with no side effects. Robots are phenomenal at these tasks. Even if they write some messy code, that mess is very likely to stay contained.
As such, we've declared some
fairly narrow
portions of the code base as "black boxes." When you encounter code like this; it's important to ensure everyone is on the same page. You don't want somebody declaring a piece of code as "full send vibes" if you actually think it is important, and you also don’t want to waste your time refactoring a section of the code when your team doesn’t have a stake in it.
Robots are not people, but people are still the authors
The robots are not people. You can call them "robot." And you can be a little mean to them (just not too mean, lest Claude stop interacting with you).
But when you have a PR in front of you, remember that you're still looking at something a human attached their name to. So becareful when calling something "slop" because you may have accidentally highlighted a cluster of code that
they
wrote or feel ownership over. Don't diminish the impact of a colleague by attributing their successes to Anthropic.
When you put code in front of people, try and let them know what parts you're proud of, and what parts you couldn't care less if they teared into. This is a new social phenomenon we're all navigating under a time of relative stress. Clear communication about what are your contributions help people not make mistakes.
We’re all in this together, and we’re all still learning. Good luck. Don’t let the robots get you down.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
✨
🔊
🎧
🌊
🍀
🤠
🎷
on
🌎
.
Platform
AI and agents
Agentic notebooks
Conversational analytics
Context Studio
Data apps
Hex CLI
Business intelligence
Exploratory analysis
Embedded analytics
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Company
About
Careers
Customers
Solutions
Media kit
Newsroom
Connect
Request a demo
Technical support
Contact us
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
You have opted out of data tracking
