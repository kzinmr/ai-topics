---
title: "Introducing Support for Gemini 3 Pro"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-gemini-3-support"
scraped: "2026-05-10T01:27:40.735729+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Introducing Support for Gemini 3 Pro

**Source**: [https://www.warp.dev/blog/introducing-gemini-3-support](https://www.warp.dev/blog/introducing-gemini-3-support)

Product
Introducing Support for Gemini 3 Pro
Olivia Johnston
November 18, 2025
Google’s latest model, Gemini 3 Pro, is now available for all Warp users. Give it a try, and let us know what you think.
Gemini 3 Pro impressed the Warp team right out of the gate. It performed well on benchmarks and real tasks— more on both below.
Over 15% improvement on Terminal-Bench 2.0
Warp’s
last score
on Terminal-Bench was 50.1%, which is #2 on the board. Switching from our previous default model to using
Gemini 3 Pro raised our score to 59.1%.
Standout performance in tests
The Warp team has been using Gemini 3 Pro internally for around a week. Sharing some comments that have organically come through our Slack channel below.
I had Gemini implement this change for me.
The thing I was most impressed by was the change that Gemini made to our UI framework itself, adding an API that I as a developer would have added — it felt like Gemini wrote really high quality code in addition to creating something that worked.
Just had Gemini 3 take a stack of 6 prs, start on the first one, run presubmit, fix everything, amend, go to next one, and do the same for all 6, then push all the PRs back up. All the fixes (albeit kinda trivial) were correct on the first try.
Kinda mundane, but it felt magical to not have to do that grunt work.
Okay, Gemini 3 cooked. This new model is a game-changer. It is consistently nailing multi-step fixes.
This is the first model that I don't even need to wait on our Rust compiler to run. It works every time. I've gotten 3 features done today and the code quality is very high.
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
