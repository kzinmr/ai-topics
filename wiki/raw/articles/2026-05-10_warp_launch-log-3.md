---
title: "Launch Log 3"
source: "Warp Blog"
url: "https://www.warp.dev/blog/launch-log-3"
scraped: "2026-05-10T01:27:48.994390+00:00"
lastmod: "2026-04-07T02:47:31.000Z"
type: "sitemap"
---

# Launch Log 3

**Source**: [https://www.warp.dev/blog/launch-log-3](https://www.warp.dev/blog/launch-log-3)

Product
Launch Log 3
Olivia Johnston
June 4, 2025
From MCP’s GA launch to attaching images as AI context, we’ve been shipping at Warp speed. Check out the full set of updates.
MCP launched to GA:
Add MCP servers to Warp, and agents will use them to gather external information
(Preview) Images as context:
Attach an image to your next Agent Mode request. We’ve used this to show Figma mocks of the webpage design we want and even architecture diagrams
Refining agent suggestions:
You can now ask agents to refine commands suggested by Agent Mode and more easily edit execution plans
(Preview) Suggested prompts:
You’ll now see suggestions for Prompts in Warp. Follow the suggestion to save your Prompt, which you can then parameterize and reuse.
Learn about the newest features from Jess, our Developer Advocate
MCP support
Interact with MCP servers directly in Warp. By connecting to an MCP server, Warp will be able to access external data and services and use these in Agent Mode conversations.
You can add an MCP server by opening your Warp Drive pane, navigating to the “Personal” section, and clicking the new “MCP Servers” tab there.
Using the Puppeteer MCP server to take a screenshot of a webpage from Warp
In Launch Log 2, we announced that MCP was available on Warp Preview. Ahead of this release, we added support for adding servers with JSON, modified env vars to only be saved locally, and increased stability. Thank you to all the Preview users in our
Warp Community
who provided feedback!
Images as context
(Preview only)
Upload an image alongside your next Agent Mode request. Warp will use the image as context and use it to inform next steps. To upload an image, click the “image” icon in the bottom right of the input area.
Uploading an architecture diagram
One use case for image as text that we've been using internally is uploading diagrams of what system the agent should be building.
Image as Context is only available on Warp Preview today, but we're looking forward to launching it to all Warp users in the coming weeks. Keep an eye out, and download
Warp Preview
to try it today.
Edit agent-suggested commands and Plans
Now, when Agent Mode suggests a command for you to run, you can suggest refinements. This feature is great for adjusting the little details— adding a flag, editing a commit message, or tweaking a parameter.
We've also updated your ability to update execution plans and agent-generated code difs. Click the "edit" button on the top of the code section to begin editing directly.
Suggested Prompts
(Preview only)
You’ll now see chips show up after some Agent Mode interactions, prompting you to save the prompt. Follow the flow to add the Prompt to your personal Warp Drive.
Saved Prompts help you avoid retyping the same prompts again and again. Some of our favorites internally include packaging up a PR, having AI take a pass at code review, and merging main into the current branch.
Prompts will be used as context in AI requests, and are also shareable with peers. Take a look at some of our favorites at
dothings.warp.dev
!
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
