---
title: "Q&A: Why UI Zoom took three years"
source: "Warp Blog"
url: "https://www.warp.dev/blog/ui-zoom"
scraped: "2026-05-10T01:28:16.983174+00:00"
lastmod: "2026-04-07T02:52:39.000Z"
type: "sitemap"
---

# Q&A: Why UI Zoom took three years

**Source**: [https://www.warp.dev/blog/ui-zoom](https://www.warp.dev/blog/ui-zoom)

Engineering
Q&A: Why UI Zoom took three years
Olivia Johnston
Aloke Desai
October 17, 2025
Warp’s latest release includes full UI zoom, one of our most requested features ever. We sat down with founding engineer and Team Lead Aloke to talk about why it took so long, what finally clicked, and how a couple of flights (and Warp’s agentic coding features) led to one of Warp’s most satisfying fixes yet.
Let’s start with a quick intro. Who are you, what’s your role, and how long have you been at Warp?
I’m Aloke — a founding engineer at Warp. I currently lead the coding team as tech lead and engineering manager, which means I help shape both the product experience and the systems underneath it. I’ve been at Warp for about five years now, which makes me old enough here to have seen us go from a scrappy prototype to a product that hundreds of thousands of developers use every day.
Give me a quick overview of what feature just launched to production.
We just rolled out full UI zoom for Warp — finally! This has been one of the top five most-requested features since our early beta days. Until now, hitting
CMD +
on Mac (or
CTRL +
on Windows/Linux) only changed the terminal font size, leaving the rest of the interface the same. If you were on a high-DPI monitor or needed better accessibility, that meant the UI stayed stubbornly small.
The first official GitHub issue for this feature was opened back in 2022, but users were asking about it long before that. It’s one of those issues that’s been pinged constantly for years — we were still getting comments on it last week. So this one’s been a long time coming.
Why did this take so long to fix?
It’s a deceptively hard problem because of how Warp is built. Unlike most apps, we don’t use Electron or a webview-based framework that gives you zoom “for free.” Warp is written in Rust on a completely custom UI framework — that’s what lets it feel so fast and native. But it also means we have to hand-build every feature like this ourselves.
On top of that, we made some design decisions early on that haven’t aged well. We hard-coded a lot of UI element sizes instead of letting them scale dynamically. So when we tried to increase font size, things would break — tabs would get cut off, icons would misalign, menus would overflow. Fixing that manually would have meant hunting down and adjusting every single component across the product. We estimated it would take about three to four weeks of dedicated engineering work, and as a small team, that was hard to prioritize against new features and critical bugs.
Can you explain more about the hard-coded UI parts?
Yeah, this goes back to the “we were moving fast” energy of Warp’s early days. A lot of components used fixed heights or widths that didn’t scale. Take tab titles, for example: their height was essentially hard-coded. Ideally, when you increase the UI font size, those titles and the icons next to them should all scale proportionally. Without that, just increasing the font size alone looks broken — the text gets bigger, but the box it sits in doesn’t.
So the real challenge wasn’t “make the text bigger.” It was “make the entire product surface scale smoothly.” That’s a much deeper change to the UI system.
Why now? What made the team finally tackle it?
This wasn’t something we ignored — it just kept losing the prioritization battle. Everyone cared about it, but there was always a new feature or bug that needed attention first. It’s the classic startup trade-off.
What finally changed was when our CEO, Zach, tagged me in a Slack thread a month ago and said, “Can someone please think about this?” That was the nudge I needed. I didn’t jump on it right away (sorry, Zach), but a few weeks later, I was on a plane with some time and decided to finally put some real energy behind thinking through the right engineering solution. By the time I landed back home — well, technically after two plane rides — I had the solution.
What was the breakthrough?
The breakthrough was realizing that we already had the mechanism we needed — we just hadn’t looked at it through the right lens. Warp’s rendering system already supports the monitor’s DPI through something we call the “scale factor”, which we use to make sure the UI looks crisp on high-resolution monitors. On a Retina display, for example, the OS tells us to use a scale factor of 2; on a regular monitor, it’s 1.
Then it hit me: we could reuse that exact system for zooming. The trick was to “fake” the window size. If you zoom in 2×, instead of telling the UI framework that the window is 100×100, we tell it it’s 50×50 — then upscale everything by 2× when rendering. The result is a perfectly scaled interface that just works.
Once that clicked, I literally laughed on the plane because it was so simple in hindsight. The code took about 20 minutes to implement using Warp AI. The thinking part was the hard part — the coding part was basically instant.
That’s incredibly fast. How did the team react?
Everyone was thrilled — and a few people assumed I’d pulled off some kind of magic trick. But it wasn’t magic; it was just looking at the problem differently. We’d been thinking about it as “change the font size,” not “zoom the interface.” Once we reframed it, the path was obvious.
It also reinforced one of our biggest beliefs at Warp: the hard part of building software is thinking, not typing. The creativity and design iteration are where human engineers shine. Once you know the right direction, you can delegate the rote coding to AI tools — including Warp itself.
So you literally used Warp to build Warp.
Exactly. Once I had the idea, I used Warp AI to write the code. It took about 20 minutes of “warping” to get the core implementation done. Then I did a bit of refinement to integrate it into the settings menu and command palette, and it was ready to test.
It’s kind of poetic — using Warp to improve Warp. And it’s a perfect showcase of how our team actually works: we rely on the product we’re building to make the product better.
How can users try the new zoom feature?
There are a few ways to use it. The easiest is through keyboard shortcuts:
CMD +
and
CMD -
on Mac (and
CTRL +
and
CTRL -
on Windows) to zoom in or out across the entire interface. You can also go to
Settings
→
Appearance
→
Zoom
to set a custom zoom value.
For anyone who prefers the old behavior of increasing the font size without zooming the whole interface, we’ve kept it! You can still adjust just the terminal font size using separate key bindings. The difference is that terminal font size only affects the terminal, while the new zoom setting scales everything in the product — Warp Drive, command palette, menus, all of it.
Any final thoughts?
Honestly, I’m just really happy to have closed this one. It’s one of our oldest and most-commented GitHub issues, and it’s been on our collective conscience for years. Finally shipping it — and doing it in such an elegant way — feels amazing.
Please try it out, give us feedback, and keep the requests coming. Sometimes all it takes is a Slack tag and a long plane ride.
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
