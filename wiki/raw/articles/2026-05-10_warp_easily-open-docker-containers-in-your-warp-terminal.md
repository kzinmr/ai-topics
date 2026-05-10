---
title: "Easily open Docker containers in your Warp terminal"
source: "Warp Blog"
url: "https://www.warp.dev/blog/easily-open-docker-containers-in-your-warp-terminal"
scraped: "2026-05-10T01:27:23.698054+00:00"
lastmod: "2026-04-24T14:39:29.000Z"
type: "sitemap"
---

# Easily open Docker containers in your Warp terminal

**Source**: [https://www.warp.dev/blog/easily-open-docker-containers-in-your-warp-terminal](https://www.warp.dev/blog/easily-open-docker-containers-in-your-warp-terminal)

Product
Easily open Docker containers in your Warp terminal
David Melvin
December 7, 2023
Warp’s new Docker extension makes it easier to open containers in your terminal.
Try the extension, available in the Docker Extensions marketplace today.
Install Warp for Docker
No more typing out long container ids
The
`docker exec`
command lets you run commands inside of a running Docker container, but it requires you to define a shell type and type out a lengthy container ID.
It is possible to use the embedded terminal in Docker Desktop or even open the container in a default external terminal, but neither of those options give you the benefits of using the Warp terminal like:
Modern text editing
Integrated AI assistance
, and
Access to your saved workflows in
Warp Drive
Until now, if you wanted to use Warp as your driver for running commands in a Docker container, you had to copy the container ID and paste it on the command line.
With the new Warp extension for Docker, you can:
Check out a list of available containers
Configure the shell type and user
Easily open the container in Warp without typing out
docker exec
or the container id or the shell type manually
This will open your container in a
Warpified subshell
so you can enjoy all the expected productivity features of Warp.
Click "Open in Warp" to open any container.
Your container opens in a Warpified subshell.
Try the Warp extension for Docker today
Warp’s Docker extension is available to install now. Give it a try and
file an issue on GitHub
if you have requests.
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
