---
title: "Warp supports subshells with modern IDE, blocks, and autocompletions"
source: "Warp Blog"
url: "https://www.warp.dev/blog/warp-supports-subshells"
scraped: "2026-05-10T01:28:22.973594+00:00"
lastmod: "2026-04-24T14:40:02.000Z"
type: "sitemap"
---

# Warp supports subshells with modern IDE, blocks, and autocompletions

**Source**: [https://www.warp.dev/blog/warp-supports-subshells](https://www.warp.dev/blog/warp-supports-subshells)

Product
Warp supports subshells with modern IDE, blocks, and autocompletions
Melanie Crissey
May 23, 2023
Subshell support is here! Now you can “Warpify” your bash, zsh, or fish subshells to enable all the core features you’d expect from Warp, even when you’re working in a nested session.
Warp displays a banner inviting you to "Warpify subshell."
What counts as a subshell?
The classic definition of a subshell is any child process launched by a shell or shell script.
Within the context of Warp, a “subshell” is defined as any nested interactive shell session that’s spawned and running in the context of an existing, running shell. Common examples would be a shell session running a Docker container or a remote server accessed through SSH.
How to Warpify an initiated subshell
Until now, if you initiated a subshell while using Warp, the terminal would fall back into a sparse mode. You could continue to work, but you’d lose access to the features that make Warp more powerful and easier to use than your basic emulator.
Now, when you initiate a subshell that Warp recognizes as compatible, you will have the option to “Warpify” that subshell. This will enable the complete Warp experience with: modern IDE-style output, blocks, autocompletions, workflows, AI Command Search, and so on.
Out of the box, Warp has a short list of commands it will recognize as “subshell-compatible” including:
bash, zsh, fish
docker exec
gcloud compute ssh
eb ssh
poetry shell
Warpified subshells get wrapped with helpful labels and visual cues. And, you can nest endless subshells within subshells if the need arises.
Each subshell is wrapped with an indicator that describes the type of subshell session that's running.
Customize your subshell preferences
You can also add your own custom list of bash/zsh/fish commands under
Settings > Subshells
.
Once added, commands that initiate subshells will generate a prompt that lets you “Warpify” on the fly. If you’d like to remember your preferences and bypass the banner, you can edit your RC files for automatic Warpification.
On the flip side, if you’d prefer to never Warpify one of the commands Warp recognized as “subshell-compatible,” you can use the blocklist under
Settings > Subshells
to ensure you’re never interrupted with a banner.
Go forth and Warpify
Support for subshells has been one of the
most highly requested features
. We’re so glad to make this available and excited about what this unlocks for developers — especially teams that work with CLIs that generate subshells as part of key workflows.
Check out the docs
or run a command like
docker exec
to experience the power of Warpification today!
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
