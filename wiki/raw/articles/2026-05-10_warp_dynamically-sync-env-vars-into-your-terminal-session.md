---
title: "Dynamically sync env vars into your terminal session"
source: "Warp Blog"
url: "https://www.warp.dev/blog/dynamically-sync-env-vars-into-your-terminal-session"
scraped: "2026-05-10T01:27:21.540321+00:00"
lastmod: "2026-04-24T14:39:27.000Z"
type: "sitemap"
---

# Dynamically sync env vars into your terminal session

**Source**: [https://www.warp.dev/blog/dynamically-sync-env-vars-into-your-terminal-session](https://www.warp.dev/blog/dynamically-sync-env-vars-into-your-terminal-session)

Product
Dynamically sync env vars into your terminal session
Sega Okhira
Noah Zweben
September 26, 2024
With new dynamic environment variables in Warp, you can load keys or secrets from external managers, like 1Password or LastPass, into your terminal session at runtime.
This means you can always access the tokens you need to authenticate into development environments without keeping those variables in local .env files.
Dynamic environment variables reduce interruptions in your development workflow without introducing yet another place to store and update your secrets.
Read more in the docs and try it today
How dynamic environment variables work in Warp
When you use dynamic environment variables in Warp, you are creating a named, templated command that can pull environment variables through the CLI or API for an external management service at the time you need them in your terminal session. You are not storing your secrets in Warp directly.
This conveniently streamlines the workflow for accessing secrets so you can authenticate into different development environments without switching contexts.
How to create a new environment variable
Before you begin, make sure you are authenticated into the CLI for the external manager you’d like to use, such as 1Password or LastPass.
Consider whether this environment variable configuration should be shared with your team, or if it’s for your personal usage only.
Next,
open your Warp Drive
and create a new set of environment variables, just like you’d add a new workflow or notebook.
‍
Be sure to give your environment variables a meaningful name and description.
Then, click the key icon (🗝) and select from the options to bring in a key dynamically. Find your external manager from the list.
‍
‍
If you’re successfully authenticated with the CLI for the external manager, you will be able to search through a list of named keys that you have access to.
When you select a key, Warp will create a templated terminal command to pull that key into your terminal session at runtime, whenever you invoke the variables and load them into your session.
Save your environment variable in your Warp Drive.
When you’re ready to use the environment variable in your session, you can search for it by name, either in Warp Drive or using the Command Palette. Both of these methods work in terminal sessions or in
Warpified subshells
.
‍
Loading env vars along with workflows
Workflows in Warp
allow you to create parameterized commands you can run on-demand. Now, if you have environment variables saved, you will find the option to load those environment variables into your session along with any workflow.
This allows you to re-use a single templated workflow across many environments without needing to manage individual versions tailored to each.
‍
Dynamic vs. static env vars
While we don't recommend using Warp's environment variables as a replacement for a secret manager, you may have some non-sensitive variables like a HOST endpoint that are okay to enter as simple strings.
In those cases, you can use static environment variables, which work more like the .env files you’d keep locally for your project.
When you create a static environment variable, it’s securely stored in Warp Drive where it benefits from all the protections Warp has in place for cloud-based objects.
Visit Warp's trust center to learn more
Start syncing env vars today
We want to extend a special thank you to Tej Singh who worked on this project during their Warp internship.
We’re glad to make dynamic and static environment variables available to all Warp customers in Free Preview today.
Give them a try and let us know what you think!
‍
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
