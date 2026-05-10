---
title: "How to enable Powerlevel10k in Warp to make your zsh prompt more beautiful and useful"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-set-up-powerlevel10k-on-warp"
scraped: "2026-05-10T01:27:32.319282+00:00"
lastmod: "2026-04-24T14:59:33.000Z"
type: "sitemap"
---

# How to enable Powerlevel10k in Warp to make your zsh prompt more beautiful and useful

**Source**: [https://www.warp.dev/blog/how-to-set-up-powerlevel10k-on-warp](https://www.warp.dev/blog/how-to-set-up-powerlevel10k-on-warp)

Product
How to enable Powerlevel10k in Warp to make your zsh prompt more beautiful and useful
Melanie Crissey
July 25, 2023
“Have nothing in your
terminal] that you do not know to be beautiful or believe to be useful.”
In this post, we’ll walk you through how to customize your zsh prompt so it’s both beautiful and useful when you’re working with the Warp terminal on your Mac computer.
Already familiar with p10k? Skip to the
setup
.
What is Powerlevel10k?
Powerlevel10k (sometimes called “p10k”) is a plugin you can use to customize the appearance of your zsh prompt. Billed by its creator Roman Perepelitsa as “A Zsh theme,” p10k is widely adored by developers, with
more than 37K GitHub stars
as of time of writing.
Compared to no-rcs (the default zsh prompt with zero .rc files), p10k gives you:
Prominent visual breaks in your terminal output so you can easily locate recent commands within a wall of text,
Richer context about where you are working in relation to directories or git branches, and
Useful metadata specific to your recent interactions, tools you’re using, or even aspects of your computer setup.
Out of the box, Warp’s default prompt is more feature rich and contextual than the default you’ll get with zsh on your Mac terminal but p10k takes this to the next level.
For example, in a customized p10k prompt you can use custom “segments” to display information such as:
The calendar day and timestamp of your command (helpful for debugging),
The duration of a process,
Background jobs that are running, and even
The temperature and battery charge level for your current machine.
P10k’s “batteries included” segments are smart enough to show information related to the tools you’re using, like your Ruby version or kubernetes context.
With p10k installed for Warp, the prompt displays icons and informational segments.
The resulting setup is some cool “eye candy” that also serves a purpose, making your terminal more grounding and informative as you work.
How popular is p10k and why do developers love it?
In a recent survey by Warp to developers, 22% of respondents cited Powerlevel10K as a CLI enhancement they currently use, putting p10k right up against other popular tools like Starship and Neovim.
Warp’s State of the CLI Survey recently wrapped for 2023. Results will be coming out soon!
What’s driving all this adoption? Compared to other similar plugins for prompt customization, p10k touts speed as a benefit and promises no prompt lag. You can check out the
benchmarks in the zsh-bench repo
.
Plus, p10k is highly extensible. You can use the open API to create your own custom segments that can sit in the right prompt elements and show values of interest.
Beyond the tangibles, we think there’s something awesome about having a sharp setup and showing it off to your friends that makes p10k a plugin worth hyping.
Let’s set it up in Warp!
How do I set up Powerlevel10k with Warp?
Getting p10k running in Warp is easy but the order of operations matters a bit to yield the best results. We’ll walk you through it step by step.
Prefer to learn by watching instead of reading?
Here’s a video version
that covers all the same stuff.
First, if you don’t already have Warp downloaded, you can download and sign up now.
Download Warp
Once you have Warp installed, you’ll want to get the right fonts and adjust your settings as a prerequisite for the p10K setup wizard.
Install the recommended p10k font
Double-click to download these ttf files and install MesloLGS Nerd Font in Regular, Bold, Italic, and Bold Italic. Follow the prompts to confirm installation in the Font Book on your machine.
Note: p10k works with other Nerd Fonts as well but we’re keeping it simple for the purposes of this tutorial.
Configure your Warp settings to get ready for custom prompt goodness
If you have Warp open, close Warp and re-open the app to bust the font cache.
In Warp, navigate to
Settings > Appearance > Text.
Check the box to
‘View all available system fonts.’
Select ‘
MesloLGS NF’
from the dropdown menu.
On the command line, right-click on your prompt and click 'Edit prompt' to open Warp's prompt editor. Select
Shell prompt (PS1) > Save changes
.
Note: Prior to August 2023, you would have needed to enable a setting called "Honor user’s custom prompt (PS1)" in order to apply your PS1 configuration. This setting is no longer needed. Now when you select your PS1 shell prompt in the Warp prompt editor, this will ensure your customer prompt is honored.
Install and configure p10k
In Warp, run this command to download p10K:
Bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
Run
exec zsh
to restart zsh.
The p10k configuration wizard should open immediately. If it doesn’t, you can run
p10k configure
to get it going.
Follow the p10k setup wizard steps
The install wizard for p10k will walk you through several steps to assess your font compatibility and display supported options for you. Some of the setup options are a matter of personal preference. Here are my personal recommendations if you want to match my setup exactly:
Prompt Style: Rainbow
Character Set: Unicode
Show current time? Yes, 12-hour time format
Prompt Separators: Round
Prompt Heads: Round
Prompt Tails: Blurred
Prompt Height: One Line
Prompt Spacing: Sparse
Icons: Many icons
Prompt Flow: Concise
Enable Transient Prompts? Yes
There you go!
Want to take it further?
Play with Warp themes
to quickly adjust the colors of your prompt.
Or, edit the p10k theme files for more granular customization. You can:
‍
Adjust which segments
are shown by commenting them on / off
Edit the colors for segments using the key from 0-255, or
Run
p10k configure
and overwrite settings for these to take effect
Known quirks and how to file bugs
There are some known quirks and caveats when you’re using p10k on Warp. Here are the current things to know about:
“Prompt Height: Two lines” is not supported yet.
If you select this option and resize your Warp terminal window, you will encounter some messy results.
P10k’s single line setting is not supported yet.
Because Warp’s prompt is always on a new line instead of the same line by design, when you use p10k with Warp, the settings to put input and prompt on a single line will not take effect.
Warp block actions may be harder to reach.
Unlike other terminals, Warp groups input and output into “blocks” that let you take actions such as bookmarking, saving as a workflow, or analyzing content with Warp AI. Depending on how you set up p10K, you may have segments aiming to take that same piece of real estate. For now, we’re prioritizing the p10k UI over the Warp block actions buttons, so you’ll find the Warp settings are hidden until you hover.
If you think you’ve stumbled on a fresh bug, please report it on
this issue #2851
and we’ll review it post haste.
Show off your Powerlevel10k setup
Got a cool set of custom colors or segments ready to go? Share your .p10k.zsh file or a screenshot of your setup on Twitter or in the Warp community Discord in #show-and-tell.
We can’t wait to see what you put together!
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
