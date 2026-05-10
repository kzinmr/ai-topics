---
title: "Build error-proof command workflows with defined options for arguments"
source: "Warp Blog"
url: "https://www.warp.dev/blog/build-error-proof-command-workflows-with-defined-options-for-arguments"
scraped: "2026-05-10T01:27:10.164367+00:00"
lastmod: "2026-04-24T14:39:20.000Z"
type: "sitemap"
---

# Build error-proof command workflows with defined options for arguments

**Source**: [https://www.warp.dev/blog/build-error-proof-command-workflows-with-defined-options-for-arguments](https://www.warp.dev/blog/build-error-proof-command-workflows-with-defined-options-for-arguments)

Product
Build error-proof command workflows with defined options for arguments
Lili Wilson
August 20, 2024
We just launched some improvements to the way Workflows work in Warp! Here’s what’s new:
Now the workflow builder opens in a pane instead of a pop-up modal so you have more space for adding and configuring arguments
You can create a defined list of options for an argument instead of relying on plain text
As a refresher:
Workflows in Warp are templatized commands
that you can store in Warp Drive, search from the command palette (CMD + P), and call on the command line (CTRL + R).
Workflows are similar to aliases but they’re more powerful because you can add descriptions and define arguments (parameters).
Now you can preset a defined list of suggested options for an argument. When you’re ready to run the workflow and build out your command, you can use the arrow keys to navigate through the options list and select the appropriate preset to fill in.
Example use cases for enums in workflows
Manage profiles
Need to manage multiple different profile or database names for services you log into from the command line? Make an enum to store a list of profile names, prefixes for database URLs, or environments.
Get GraphQL schema
Enum arguments are also great for writing workflows that can be used across different development environments. We (the Warp team) use the following workflow a lot internally!
Specify HTTP request data
While using the terminal as a Pokedex might not be your primary use case, you can imagine using enums to specify inputs to a request for any custom endpoint with certain headers, query values, or body data.
Enums vs. text for arguments: which should you use?
Enums are best for any argument where there’s a manageable list of acceptable options to sort through. For example, you could create preset options for profile names, environments, databases, or test scripts.
Some arguments will always make the most sense to define with plain text—either because they’re easy to type out manually or because they’d be unreasonable to maintain. For example, you wouldn’t want to create an enum to store a list of personal user IDs. And it would be unwieldy to build an enum to store every path to a directory on your machine.
Pro-tip: If you are using text for an argument, be sure to write a clear description so you’ll remember exactly what syntax to use! In the workflow builder, you can ask Warp AI to autofill descriptions for you if you’re having a hard time coming up with a useful way to describe an argument.
One good thing about enums for arguments in workflows is that they’re still pretty flexible on the command line. The enum options are convenient suggestions but they’re not strictly enforced. If the preset enums list is missing the right option, you can still escape out and go back to plain text on the command line without disrupting your workflow to correct the options list.
You can also reuse an enum across multiple workflows, so you won’t have to rebuild out the same options for multiple workflows that use the same argument.
Try the new workflow builder in Warp today
Thank you to Warp user @vgarvardt for filing
this issue
and putting in this feature request!
It’s been awesome to bring enum arguments to life over the course of my internship, and I’m super excited to be shipping it. As someone who had to go through the onboarding process onto the Warp team this summer, this is a feature I found myself wanting a lot when encountering new team workflows.
A huge, huge thank you to everyone at Warp who supported me throughout this project. It led me through unexpected parts of the codebase, interesting technical problems, and deep product discussions, and I am undoubtedly a better developer than I was three months ago. I can confirm that this team is incredibly special and uniquely user-focused, and I am looking forward to seeing what’s new in future Warp updates on my personal laptop.
Speaking of future Warp updates — if you have ideas for things we can improve in Warp, please file a GH issue. We’d love to hear from you!
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
