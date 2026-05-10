---
title: "12 Favorite Features Warp Shipped in 2023"
source: "Warp Blog"
url: "https://www.warp.dev/blog/12-favorite-features-warp-shipped-in-2023"
scraped: "2026-05-10T01:27:03.710630+00:00"
lastmod: "2026-04-24T14:39:15.000Z"
type: "sitemap"
---

# 12 Favorite Features Warp Shipped in 2023

**Source**: [https://www.warp.dev/blog/12-favorite-features-warp-shipped-in-2023](https://www.warp.dev/blog/12-favorite-features-warp-shipped-in-2023)

Product
12 Favorite Features Warp Shipped in 2023
Catherine Yeo
January 2, 2024
From announcing our
Series B funding round
to being used at
OpenAI’s DevDay keynote
, 2023 was a monumental year at Warp. To celebrate, we’re looking back at our favorite features we shipped last year!
Stay until the end for some sneak previews for 2024 as well 👀
Warp AI
The days of switching back and forth between your terminal and ChatGPT are over. A fully integrated
AI assistant
now lives in Warp! With Warp AI you can receive step-by-step guidance on what command to run next when debugging and coding (even through tasks as terrifying as database migrations). No need to copy-and-paste either – you can click the command to directly execute it in your terminal.
Bonus: AI command suggestions got a glow up too! Simply by typing # on the command line, Warp AI will suggest commands for you to run based on your inputted prompt/question.
‍
Warp Drive
Tired of saving terminal commands in one giant, messy document, then constantly messaging individual commands to your teammates?
You’re not the only one. With the arrival of
Warp Drive
, you can now collaborate with your teammates inside the terminal for the first time ever. Save your team’s most frequently used commands as Workflows. Similarly, you can streamline your own productivity by saving Workflows in your personal space too.
Block Filtering
grep walked so
block filtering
could run! Using the filter icon in the top right corner of a block, you can now quickly focus on a subset of the output by filtering via plaintext or regex. This is especially useful for parsing through logs, even as a process is still running. We’ve also added the option to control how many lines show up when you filter.
Vim Keybindings
We’ve heard you all
loud and clear
. Yes, you can now edit commands with
Vim keybindings
in Warp 🎉 You can enable this feature in the Command Palette (CMD - P).
Input at the Top
Another
highly requested feature
is our new
input position settings
, which gives you the option to configure the input to start at the top. This is a delightful win for ergonomics, as you can now keep the command line at eye level. (Maybe we should add a page to our
How We Work
titled How We Sit.)
Bonus: if you’re feeling ~risky~, feel free to try Reverse Mode, which always stacks the input on top!
Warpified Subshells
When you’re in a subshell, we don’t want you to lose the magic of Warp – so we’ve added the ability to
Warpify
your bash, zsh, or fish subshell. You can also add your own custom list of bash/zsh/fish commands.
Bonus: with the new
Warp extension for Docker
, you can open your Docker container in a Warpified subshell.
Synced Inputs
Warp’s
Synced Inputs
allow you to sync your commands from one session to multiple panes as you’re typing, so you can easily run the same command in multiple sessions at the same time.
Markdown Viewer
Why should your README experience be separate from the terminal? With Warp’s new
Markdown Viewer
, your markdown files can happily live right next to your command line! All commands in your files will be rendered as interactive code blocks, and with a simple click (or CMD - Enter) the commands will be executed directly in the terminal.
Secret Redaction
Scared of accidentally leaking sensitive information when you’re screen-sharing a demo or working in a public location?
Warp has added
secret redaction
, so private information (e.g. API keys, passwords, IP addresses) will be hidden as you’re working and removed entirely when blocks are shared. You can enable this feature in the Command Palette (CMD - P).
Create Theme From Image
During our
“Why Not?” hack week
, we asked ourselves: why not create themes from images within the Warp app? Now you can personalize your Warp experience further by uploading an image to generate a custom theme.
Now even your terminal can be in the Spiderverse
Warp Prompt Builder
With Warp’s new
drag-and-drop prompt builder
, you can now customize your prompt to add the relevant pieces of metadata of your choice: your directory, Git branch, Kube context, date, time, and so on. And, if you’d rather use PS1, Warp supports
p10K
as well.
Raycast Extension
For any Raycast fans out there, you can now open Warp tabs/windows and launch configurations from Raycast! Install the extension from their marketplace:
https://www.raycast.com/warpdotdev/warp
‍
Looking ahead for 2024…
Warp has a BIG year planned in 2024 – here are a couple sneak previews of what’s coming:
Warp is arriving on Linux at last!
Join the waitlist
More collaborative features are coming to Warp Drive, including Notebooks, a new way to save your workflows as interactive runbooks
Keep sending us feedback through our
GitHub
. We’re excited for what 2024 has in store!
Try it for yourself
If you’re not already using Warp as your daily driver, download the latest version and give these new features a try today.
Download Warp
‍
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
