---
title: "Introducing Warp: The Terminal for the 21st Century"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-warp"
scraped: "2026-05-10T01:27:42.798305+00:00"
lastmod: "2026-04-24T14:39:40.000Z"
type: "sitemap"
---

# Introducing Warp: The Terminal for the 21st Century

**Source**: [https://www.warp.dev/blog/introducing-warp](https://www.warp.dev/blog/introducing-warp)

Product
Introducing Warp: The Terminal for the 21st Century
Zach Lloyd
April 5, 2022
Introducing Warp
Today, I’m proud to officially introduce Warp, a from-first-principles reinvention of the terminal to make it work better for developers and teams. As of today, Warp is in public beta and any Mac user can download and use it for free.
 Download Warp
We are also excited to announce that we’ve raised some funds to grow Warp ($23M), both from wonderful firms (
GV
,
Neo
,
BoxGroup
) and world-class operators like Dylan Field (who led our Series A), Elad Gil, Jeff Weiner, and Marc Benioff.
Why Reinvent the Terminal?
Walk by any developer’s desk and you are likely to see two apps open: their code editor and their terminal (sometimes the code editor is the terminal!).
Both are crucial to developer productivity.  The code editor is where developers write code; the terminal is where they do pretty much everything else, from building code to running and deploying it, interacting with source control, configuring their cloud systems, and more.
And yet only one of these two apps – the code editor – has experienced meaningful product improvement over the past 40 years. Compared to using VS Code, using the terminal is like stepping back in time to the 1970s. Only
70% of developers use VSCode
, while 100% use the terminal. So why is the terminal experience still so lackluster?
Our Product Vision
At Warp, our product vision is to bring the terminal into the present in order to help developers build the future.
We are doing this by fixing the two biggest pain points that exist in today’s terminals:
Terminals are hard to use
They don’t work for teams
These are pain points that I’ve personally experienced again and again in my twenty years as an engineer, and I’m sure readers feel the same.
To get good at using a terminal before Warp, users had to do all sorts of complex configuration, master arcane key shortcuts, and memorize abstruse commands. Even then, seemingly simple things like copying a command’s output or positioning the mouse cursor were still difficult.
Warp makes input and output easy, and removes the need for most configuration. Input works like a modern text-editor, and output works like a data notebook. Moreover, Warp makes command-entry fast and fun by suggesting commands for commonly used tools and providing built-in workflows that save developers time.
In short, Warp makes the terminal work for the developer, rather than the other way around.
Secondly, up until Warp, terminals have been inherently single-user, local applications.  But as I learned when I was leading engineering on Google Docs – and as Dylan showed with Figma – every productivity application is more powerful when it’s collaborative.  This is true 100% of the time – from Figma to GDocs to Notion to Front – and I’m confident that the terminal is no exception.
Terminal “collaboration” means not just GDocs-style real-time collaboration, but asynchronous collaboration through sharing commands, settings, and history. It means increased knowledge-sharing through wikis and READMEs that run directly in the terminal. It means making the terminal safer and more secure via integrated password-management and audit logging. It means making the terminal a more extensible and customizable platform, with a nice modern ecosystem.
Finally, all of this needs to be built with speed and compatibility in mind – Warp is made in Rust with GPU-accelerated graphics, and works with existing shells like zsh, fish and bash.
Go Try Warp!
Nine months ago we launched Warp in private beta behind a waitlist.  Since then, thousands of developers have made Warp their daily driver, given us feedback, and allowed us to greatly improve the product.
Today, we are removing our waitlist and launching our public beta.  We are calling it a “beta” because we know there are still some issues to smooth out, but we are confident that even today the experience is meaningfully better than in other terminals.
If you use a Mac, please give it a shot and let us know how it goes. Otherwise, sign up here to be notified when Warp is ready for your platform.
Welcome to the future of the terminal.
 Download Warp
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
