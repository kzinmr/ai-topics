---
title: "December 2024 Release"
source: "Warp Blog"
url: "https://www.warp.dev/blog/december-drop"
scraped: "2026-05-10T01:27:17.495591+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# December 2024 Release

**Source**: [https://www.warp.dev/blog/december-drop](https://www.warp.dev/blog/december-drop)

Product
December Release: Enhanced session sharing, Warp on Web, expanded AI capabilities, and a new icon
Olivia Johnston
December 11, 2024
Session Sharing brings multiplayer to your command line
With Session Sharing you can instantly share web links to your terminal session and pass controls to a teammate. Teammates will be able to follow along with your session and, with your permission, take control through the Warp app or via a web link. No Warp account needed.
Session Sharing allows you to start working together instantly, with nothing more than a link in a Slack channel. It’s perfect for all of those moments where you need a second (or third, or fourth) pair of eyes on a problem: you’ve hit an error and need to phone a friend; you’re onboarding remotely and having trouble setting up your environment; you’re on-call and need help in your terminal “war room”.
Session Sharing isn’t just for when things are going wrong. Our team has been using it for pair programming, and even for monitoring a long-running command from home devices by sending links to ourselves.
When you start sharing a session, you’ll choose whether to share with individuals via email or through a link with either your team or anyone on the web. You’ll also select whether to grant ‘view’ or ‘edit’ access. Individuals with view access can highlight and copy blocks, but edit access is required to write and run commands.
You can host up to five sessions from any Warp Free and Pro plans and unlimited sessions are available when you upgrade to a Team plan.
Read more
Publicly share workflows with Warp on web
You can now share your saved workflows with anyone, Warp user or not. With the new sharing experience, you can create objects and share with specific email addresses, or create public links which are viewable on the web (even without a Warp account).
The use cases are endless: you’re a professor sharing assignment instructions, a creator sharing your configuration, or maybe:
You’re a Team Lead onboarding a new team member
: imagine sharing the env vars, notebooks, and workflows required to set up their environment with a single link. All the tools the new engineer needs become embedded in the terminal flow, reducing time switching between apps, hopping into your Slack DMs, and jumping on quick Zoom calls.
You’re building a CLI tool
: imagine your users having installation, configuration, and advanced workflows seamlessly embedded into their terminal– and being used as context for AI requests (more on that below)-- with a single link. Moving from finding an exciting tool to being a power-user becomes frictionless.
To see the experience in action, check out the
quick start guide to the nix package manager
created by
@JustSteveKing
.
Choose your own model: Claude 3.5 Sonnet and Haiku support
You can now choose which model Agent Mode uses: GPT-4o, Claude 3.5 Sonnet, or Claude 3.5 Haiku.
Each of these models excel at different CLI and programming tasks, and strike a different balance between answer complexity and latency. Warp now defaults to Claude 3.5 Sonnet, which we’ve observed to be most helpful for multi-step development workflows.
The choice is yours—try each and let us know what you observe and what models you’d like to see next.
Read more about Agent Mode in our docs
Add context to Agent Mode with Warp Drive
Agent Mode has been a powerful tool to help developers use natural language in their CLI to execute tasks or troubleshoot. However, it was limited by the context it could use: information generically available on the web and context you explicitly included in the request.
Today, Agent Mode will automatically use your Warp Drive as context. Perhaps you're new to a team and trying to understand the team’s infrastructure and processes. Now Agent Mode will use your team’s saved Workflows and Notebooks to provide tailored answers. Each output will include references so you can see which Workflow or Notebook Agent Mode is consulting.
We’ve also indexed docs.warp.dev so you can easily use Agent Mode to retrieve Warp documentation. Agent Mode will help make you a Warp power user; it knows what ‘warpifying a subshell’ is and will teach you how to do it.
We at Warp have been loving this improvement– Agent Mode can now accurately suggest commands for bespoke processes like adding IP addresses to our internal staging allowlist.
Prompt Suggestions for Agent Mode
Prompt Suggestions are contextual, AI-powered suggestions that activate Agent Mode. These banners will provide suggestions for what to ask Agent Mode in specific scenarios— similar to how Warp already suggests commands to run.
Note that Prompt Suggestions uses an LLM to generate prompts based on your terminal session. Visit Settings > AI > Agent Mode to turn it off.
Learn more in our docs
.
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
