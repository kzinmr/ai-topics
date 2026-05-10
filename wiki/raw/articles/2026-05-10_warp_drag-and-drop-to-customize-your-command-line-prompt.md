---
title: "Drag and drop to customize your command line prompt. Why not?"
source: "Warp Blog"
url: "https://www.warp.dev/blog/drag-and-drop-to-customize-your-command-line-prompt"
scraped: "2026-05-10T01:27:20.393419+00:00"
lastmod: "2026-04-24T14:39:25.000Z"
type: "sitemap"
---

# Drag and drop to customize your command line prompt. Why not?

**Source**: [https://www.warp.dev/blog/drag-and-drop-to-customize-your-command-line-prompt](https://www.warp.dev/blog/drag-and-drop-to-customize-your-command-line-prompt)

Product
Drag and drop to customize your command line prompt. Why not?
Melanie Crissey
August 23, 2023
Warp’s new customizable prompt lets you add useful metadata without touching your config files.
In this post we’ll introduce you to Warp’s customizable prompt builder and walk you through how it works.
Context in your prompt keeps you from getting lost
Custom prompts like Starship and
Powerlevel10k
are popular for a reason. They’re beautiful, useful, and grounding. Custom segments that display your working directory or your Git branch tell you exactly where you’re working. Useful metadata like the date and time make it easy to scan recent commands like you would your logs.
It only takes a little extra effort to step through a setup wizard or edit your .zshrc file.
But, what if you didn’t have to mess with that at all?
Enter Warp’s new customizable prompt!
Now you can add context, like timestamps, to your Warp prompt.
How to customize your Warp prompt
Right-click on your prompt in Warp and select ‘Edit prompt’ to open the prompt editor.
(Alternatively, you can navigate to the same place through Settings > Appearance > Prompt and then click on the preview of your prompt.)
From here, you’ll find a collection of metadata bits you can drag to include in your customized Warp prompt. We call these bits "context chips."
Pull them down into the editor canvas and rearrange them as you please.
Change your mind? Hit the ‘x’ on the chip to send it back up into no man’s land.
When you’re done, save your changes to initiate your new prompt and check it out on the command line.
‍
Edit prompt and drag and drop to customize.
‍
Your context stays in sync across sessions
One neat feature of context chips in Warp’s customized prompt is they dynamically update across multiple sessions without you even needing to run a command.
If you change a git branch in one session, your prompt will automatically update to reflect that new git branch in all other sessions where you’re working in the same git repo.
This makes context-switching a lot less painful as you’re working.
Give it a try!
‍
Context chips stay in sync across sessions.
‍
Show off your custom prompts
We’re spotlighting the new customizable Warp prompt with context chips as part of Warp’s “Why Not? Week.”
What’s your favorite way to customize your prompt? Any new context chips you’d like to see added? Share your prompts and send feedback in the
Warp community Discord
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
