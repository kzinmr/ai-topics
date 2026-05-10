---
title: "Warp’s product principles for reinventing the terminal"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-we-design-warp-our-product-philosophy"
scraped: "2026-05-10T01:27:38.168913+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Warp’s product principles for reinventing the terminal

**Source**: [https://www.warp.dev/blog/how-we-design-warp-our-product-philosophy](https://www.warp.dev/blog/how-we-design-warp-our-product-philosophy)

Product
Warp’s product principles for reinventing the terminal
Zach Lloyd
August 18, 2021
At Warp, we are trying to build the best possible terminal for all developers. In this post we share 8 Product Principles we follow as we build towards that goal.
At Warp, we believe we can keep what’s best about the command-line while fixing its pain points and adding super-powers.
Our goal is that using Warp every developer should be as productive as a CLI veteran.
Here are the eight principles that guide our approach:
#1: Meet developers where they are.
This means that our terminal should be backwards compatible.  A developer using it for the first time should be at least as productive as they were in their old terminal.  Practically speaking, this means we are creating a terminal that works with developers’ existing shells, scripts, and key bindings.
#2: Keep the power, but fix the UI.
We don’t see any reason why the terminal can’t have a more modern, intuitive interface, while maintaining the power of a primarily textual, keyboard driven experience.  If a user wants to use the mouse to position the cursor, why not support that?  Why not have a native autocomplete and search experience?  Our goal is to
create the UX that best supports what developers use
the tool to accomplish, and we are pragmatic about whether that UX is character based or pixel based and whether the input mechanism is the keyboard or the mouse.
We introduced blocks to help you navigate your work in the terminal.
#3: A great out-of-the-box experience.
There are many different plugins, themes, and open-source projects that improve aspects of the CLI; e.g.
tmux
,
mosh
,
OhMyZsh
, and
powerlevel10k
.  Each has its own install process, configuration scheme, update mechanism and more.  Many developers end up using a very basic and underpowered version of the CLI because they never discover, configure or learn these tools.  We believe there is value in an
integrated, out-of-the-box
experience that helps all developers be more productive immediately.
Command descriptions & smarter suggestions to help speed up your workflow without extra configuration needed.
#4: Build for speed.
One of the great attractions of working in the CLI is that if you master it, you can work very quickly.  That’s only true though if the underlying terminal is fast.  We are building Warp on the fastest possible modern architecture.  On desktop: a pure Rust app that goes directly to the GPU for rendering. On the web, a WASM app that uses WebGL.
#5: Build a platform.
Most developers will experience Warp as a terminal app, a product they launch and run.  However, the CLI is more than an app, it’s a platform, much like iOS or Windows.  It has (primitive) mechanisms for discovering apps, installing them, running them, but it lacks many of the affordances of modern platforms, like an app-store, a unified way of securely installing and removing apps, a well defined API for developers to configure the runtime environment, and more.  While we are starting by focusing on the terminal app and experience, we eventually want to build the best possible CLI platform.
#6: Build for teams.
Developers today work in teams on shared projects.  Because of this, most applications developers use are collaborative in one sense or another.  Github is a good example, as is VSCode live session sharing.  And yet the CLI is still primarily a single-user tool, with collaboration facilitated by copy/paste, screenshots, and screen-sharing, rather than a true multi-player experience.  We believe that CLI-based teamwork is a very powerful concept, extending beyond google-docs real-time collaboration, to facilitating asynchronous workflows like command-reviews, shared devops terminals and more.
Real time collaboration & session sharing is one of the features we're working on.
#7: Build for everyone.
The CLI traditionally has a bit of a mystique around it; developers feel like hackers when they use it, and there’s almost a rite of passage in conquering its idiosyncrasies.  We believe that the CLI should be more accessible, more humane, and more useful to all developers.  Too many are turned off by the intimidating UI.  Many aspiring developers have their first experience using the CLI (it’s how they set up development environments), and that first experience is often very negative because the interface is so hard and creates so much incidental complexity.  We want to fix this and make a modern CLI for all developers.
We truly believe that following all eight above principles will help us deliver the terminal that will finally bring the developers’ experience to the next level! And while we’re focused on building Warp, you can still meet us in
our Discord community
where we discuss Warp with developers from around the world. Request early access if you haven’t already. We look forward to your feedback.
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
