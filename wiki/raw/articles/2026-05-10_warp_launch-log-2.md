---
title: "Launch Log 2"
source: "Warp Blog"
url: "https://www.warp.dev/blog/launch-log-2"
scraped: "2026-05-10T01:27:48.630631+00:00"
lastmod: "2026-04-07T02:47:21.000Z"
type: "sitemap"
---

# Launch Log 2

**Source**: [https://www.warp.dev/blog/launch-log-2](https://www.warp.dev/blog/launch-log-2)

Product
Launch Log 2
Olivia Johnston
May 14, 2025
From MCP integrations to smarter AI interactions and faster terminal performance, we’ve rolled out a wave of updates to make Warp even more powerful. Here’s what’s new.
MCP support:
Warp Preview now supports MCP, connecting to external data for richer Agent Mode interactions.
AI context:
Attach URLs as prompt context, pro-actively suggested Rules
AI experience:
Continue past Agent Mode conversations, notifications when long-AI tasks are complete, plus we have better codebase search
Core terminal:
Kitty image support, ligature support, and settings sync across devices
Performance:
Our intern doubled the speed of our command search
Jess, our developer advocate, talks through and demos the features in Launch Log 2
MCP & Warp Preview
In case you missed it, Warp Preview is now available! Warp Preview grants you early access to our latest features. Think features that are out of dogfood, but still require some additional time and data to be production ready. If you’re open to some features that may be a bit rougher around the edges, you’ll get access to the fastest improvements we’re making to the app.
Warp Preview’s biggest advantage today is support for Model Context Protocol (MCP), enabling you to interact with MCP servers within Warp. By connecting an MCP server, Warp will be able to access external data and services and use these in Agent Mode conversations.
To add an MCP server in Warp Preview, open your Warp Drive panel, and click the “MCP Servers” object under your “Personal” workspace.
Download Warp Preview today.
Increased context for Agent Mode interactions
We’ve been making Agent Mode better at giving you tailored responses, as well as making it easier to track autonomous jobs.
Web context
Include a URL along with your Agent Mode request and Warp will include the page contents as context. This feature is particularly useful for tasks like using a specific API or referencing specific documents.
Suggested Rules
Warp will suggest Rules at the end of your Agent Mode conversations. To accept a suggestion, click the chip, edit the suggestion as needed, and press save. Saved Rules will be used in all Agent Mode responses.
AI upgrades
Continue past agent conversations
You’re now able to restart conversations with agents. Once you restart a conversation, the agent will be given all context from the previous interaction to provide a continued conversation. Continue conversations after interrupting an agent’s work, coming back to a task you didn’t finish the day before, or to continue digging into a similar topic.
Desktop notifications for agents
You’ll now receive notifications from agents if notifications are enabled. Agents will notify whenever they need your attention for things like approving an execution plan, running a deny-listed command, reviewing a code change, or letting you know a task is complete. This feature makes it easier to parallel process while an agent is working autonomously.
To enable notifications go to Settings > Features > Notifications and enable desktop notifications.
Better codebase search
Warp is now better at searching your codebase for specific keywords like function names, variables, or symbols. This is especially helpful when making changes within a large codebase to ensure you’ve updated everything appropriately.
Long file support
Ask Warp to make edits to files with over 10,000+ lines of code. The agent now has the ability to read, understand, and make changes to these long-files. Internally, we’ve been using this on our longest file (18K+ lines).
Core terminal
We continue to add features to our terminal base.
Kitty image support
Warp now has full support for Kitty image protocol, meaning you can view images and videos directly within Warp. Use this feature on its own or alongside tools like Yazi, Chafa, or mpv. Use this feature to view the images or video output of your scripts without ever having to leave Warp.
Ligature support
You can now opt in to use ligatures within Warp. To turn them on, go to Settings > Appearance > Text and toggle the “Show ligatures in terminal” switch.
Settings sync across devices
Your Warp settings will now sync across all your logged in devices. This feature allows you to have the same comfortable configuration wherever you're logged into Warp. Toggle this setting on or off on Settings > Account. Read more about what is and isn’t synced with this feature in our
docs
.
Performance
2x faster command search
We made command palette search within Warp two times faster by shifting our internal data structures. This means that when you next hit CTRL+SHIFT+R to open the command search palette, you’ll feel less latency in the process.
What’s next
Keep an eye out for exciting product updates, coming soon!
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
