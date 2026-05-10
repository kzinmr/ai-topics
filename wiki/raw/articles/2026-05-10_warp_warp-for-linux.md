---
title: "Warp, the modern terminal, is now available for Linux"
source: "Warp Blog"
url: "https://www.warp.dev/blog/warp-for-linux"
scraped: "2026-05-10T01:28:21.137602+00:00"
lastmod: "2026-04-24T14:40:02.000Z"
type: "sitemap"
---

# Warp, the modern terminal, is now available for Linux

**Source**: [https://www.warp.dev/blog/warp-for-linux](https://www.warp.dev/blog/warp-for-linux)

Product
Warp, the modern terminal, is now available for Linux
Aloke Desai
David Stern
February 22, 2024
Warp is now available for Linux! You can install Warp on most Linux distributions, including Ubuntu, Fedora, Arch Linux or Red Hat. The initial set of available packages include:
.deb (apt)
.rpm (yum/dnf/zypper)
.pkg.tar.zst (pacman)
.AppImage
Download Warp
The Windows version of Warp is in development now and slated to release later this year. You can
join the Windows waitlist today
and be the first to know when it’s available to download.
Warp ♥️ Linux
Since launching on Mac, Linux support has been Warp’s number one upvoted
GitHub issue
.
This isn’t surprising: Linux is a uniquely important platform for developers, and the terminal is a uniquely important tool on Linux. The terminal is often the primary, and sometimes the only, way that developers use Linux machines. And Linux machines are everywhere: from the servers powering the internet, to Androids, Chromebooks and even Raspberry Pis.
Despite this, Linux has relatively few terminal options compared to Mac and Windows, and none with the modern features of Warp. We hope the addition of Warp as an option today unlocks a bunch of new productivity and happiness for individuals and teams spending their days in the Linux console.
A tour of Warp for Linux
If you are already familiar with Warp on Mac, you’ll find the experience nearly identical on Linux both from a performance and feature standpoint.
Like on Mac, Warp for Linux is built fully in Rust and all graphics rendering is done directly on the GPU. It’s fast. We've even implemented some additional performance optimizations that we're excited to bring to the Mac application soon.
And like on Mac, Warp for Linux supports zsh, bash and fish out of the box. It’s compatible with your existing shell setup.
Warp for Linux also includes all the features that make the terminal a much happier and more productive place: Modern Editing, Warp AI, and Warp Drive.
If you’re new to Warp, you’ll notice that it’s a more powerful environment for editing and executing commands than the stock terminal. The input works more like a normal text editor (including mouse support) and has in-built completions, syntax highlighting, and support for multiple-cursors.
After a command is executed, Warp groups together terminal input and output into atomic Blocks. These make it much faster to navigate, filter, and even share content from your terminal to other developers on your team.
Warp’s integrated AI lets you look up forgotten commands, debug errors, or chat through complex setups without leaving the terminal. This is not a bolt-on AI integration – AI is uniquely suited to the terminal since it’s an unusually text-heavy and obscure interface. Warp AI integrates directly into terminal workflows, from translating natural language into CLI commands to suggesting reusable workflows to share with your team through Warp Drive.
Warp Drive makes your terminal collaborative, and is one of the most powerful aspects of Warp. It’s a space where you can save your most important parameterized commands as reusable workflows you can search, share, and run on-demand. You can build out a library of workflows in your personal drive, or create a collaborative Team Drive so your whole team stays in sync.
This is especially useful for streamlining new employee onboarding or incident response. The last thing you want to be doing in a firefight is Googling how to run a command or searching through Slack for something your teammate told you about months ago.
The technology behind Warp for Linux
There were some interesting technical challenges in building Warp for Linux, which deserve a post of their own sometime soon.
At a high level, the most interesting challenges were around cross-platform rendering – specifically moving from the Metal APIs to a set of GPU APIs that work across Linux, supporting text rendering well across platforms, and making sure our code had the right abstractions for features that are platform-specific (e.g. the Mac menu bar or native modals).
Aside from the platform-specific abstractions, the Linux version of Warp is built on largely the same Rust codebase as the Mac app. Around 98% of the code is shared, and most of the content in
How Warp Works
applies.
For the Linux build, we decided to build on open-source Rust libraries with cross-platform support, like
wgpu
,
winit
, and
cosmic-text
. These libraries will also make it easier for us to expand Warp to web and Windows quickly, and we’ve upstreamed some bug fixes and performance improvements that we made during the development process.
One cool outcome from the technical work here was that we expanded our internal Rust-based UI framework to better support these platform abstractions. Once it’s been tested more thoroughly across platforms, we are planning to open source our UI framework.
We’re looking forward to sharing the code behind these changes!
What’s next
Since we launched the
first beta of Warp back in 2022
, we’ve heard from the developer community that Warp is a joy to use and also makes them feel more productive. Engineers who use the terminal heavily save hours every week with completions, AI, and reusable workflows. More importantly, engineers who use Warp just like using the terminal more. It becomes a place where they feel more powerful and able to do their best work.
We believe Warp can be even more powerful when entire teams are using Warp together. But we know you can’t champion a rollout of Warp where you work until Warp works for every operating system used by engineers across your team.
That’s why we’ll be shifting gears to make Warp for Windows available as quickly as we can.
Try Warp for Linux today
Download Warp for Linux
, share it with your friends, and tell us what you think! We’d love to hear from you.
If you have any questions about features or settings, you can report them to the team in the
Discord community
or file an issue on
Warp’s GitHub
.
Download Warp
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
