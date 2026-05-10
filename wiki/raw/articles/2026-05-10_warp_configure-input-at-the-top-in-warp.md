---
title: "Configure input at the top in Warp"
source: "Warp Blog"
url: "https://www.warp.dev/blog/configure-input-at-the-top-in-warp"
scraped: "2026-05-10T01:27:14.734555+00:00"
lastmod: "2026-04-24T14:39:22.000Z"
type: "sitemap"
---

# Configure input at the top in Warp

**Source**: [https://www.warp.dev/blog/configure-input-at-the-top-in-warp](https://www.warp.dev/blog/configure-input-at-the-top-in-warp)

Product
Configure input at the top in Warp
Melanie Crissey
April 6, 2023
Today we’re releasing two new modes for command line input position in the Warp terminal: input
starting
at the top and input
pinned
to the top.
This has been one of the most highly requested features for Warp since the beta launch, and we’re so glad to make this available for Warp developers.
A side-by-side comparison of Reverse Mode vs. Classic Mode.
Let’s go into why we built this and how to try out these new settings.
An ergonomic improvement for the terminal
By default, Warp keeps the input prompt and command line “pinned” to the bottom of the view. This is similar to how inputs work for other work applications like Slack. Your past input and output get grouped together in blocks that flow up and out of view. You can scroll up or navigate up to visit your past commands. However, this is rather unusual behavior for a terminal application.
This screenshot of the Warp terminal shows prompt and command input pinned to the bottom.
Classic terminals typically start with your prompt and command line input initiating at the top of the view. As you enter commands, the output piles up on top, pushing the prompt and command line further down the screen. You can run commands to clear the screen and move your prompt back to the top — which may even become a compulsive habit over time. We love the clear command for a reason.
As one developer who was trying Warp’s beta pointed out
, the sheer ergonomics of having your command line input at the bottom of the view are Not Good. Whether you’re starting with the input on the bottom or pushing that input to the bottom as you work, craning your neck to
look down
is suboptimal compared to keeping the command line at eye level.
This image, submitted by a Warp beta tester, perfectly illustrates how the on-screen position of the command line affects neck strain for developers.
So, why not redesign the Warp experience with the input location in mind?
New input position settings in Warp
Now you have the option to ditch Warp’s default “pinned to the bottom” mode and configure your input position to your liking.
Making the input position for Warp more configurable solves problems for developers in two scenarios:
If you’re coming over to Warp from a classic terminal, you can now enable a “Classic mode” with input starting at the top. This works exactly like you’d expect, so you don’t have to make an uncomfortable habit change in order to experience the other novel features Warp has to offer.
If you’ve been wanting to use Warp but found it to be a literal pain in the neck, you can now enable a uniquely ergonomic “Reverse mode” which keeps input pinned at the top and lets blocks of input/output flow down the page in reversed order. This mode might take some getting used to, but it has the potential to deliver real, quality of life improvements for developers who work in the command line for hours at a time.
“Jump to the bottom of this block”
When using Reverse mode and executing long running tasks, you may find the latest line of your output quickly moves out of view and out of reach. This is a non-issue when your input is pinned to the bottom, but it could get pretty painful when you’re using input pinned to the top.
To combat this, we’re introducing a new “Jump to bottom of this block” button. This will appear in the bottom left corner of your view when a block with multiple lines of output starts to scroll out of reach. You can use this button (or cmd-shift-down) to teleport to the latest line of that block.
The button itself is pretty unobtrusive, but if you’d like to toggle it off, you can do so under
Settings > Appearance > Blocks
.
Find the mode that works best for you
Both of these new input modes — “Classic mode” and “Reverse mode” — are available to try today. You’ll find them under
your Appearance settings
in the latest version of the Warp app.
Take them for a spin and let us know what you think!
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
