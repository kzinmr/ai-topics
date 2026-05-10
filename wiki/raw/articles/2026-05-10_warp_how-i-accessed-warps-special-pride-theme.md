---
title: "How I Accessed Warp's Special Pride Theme"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-i-accessed-warps-special-pride-theme"
scraped: "2026-05-10T01:27:30.101389+00:00"
lastmod: "2026-04-24T14:39:33.000Z"
type: "sitemap"
---

# How I Accessed Warp's Special Pride Theme

**Source**: [https://www.warp.dev/blog/how-i-accessed-warps-special-pride-theme](https://www.warp.dev/blog/how-i-accessed-warps-special-pride-theme)

Product
How I Accessed Warp's Special Pride Theme
Jess Wang
June 16, 2022
Introduction
In my high school days, I was obsessed with switching out the themes of my terminal. It was cool that I was able to customize a tool that, for the most part, isn’t the most advanced in terms of user interface. It was also a nice way to subtly showcase my personality and hobbies, similar to a poster I might tape up in the wall of my room. For many years, my terminal wallpaper was the famous meme of Saitama from One Punch Man (if you know, you know).
‍
‍
In this blog, I am going walk you through how to customize your terminal to Warp’s pride theme in honor of pride month.
How I Customized My Terminal to Use Warp's Special Pride Theme
For context, Warp has an open source repo for its theme extension point, meaning anybody can contribute themes that you can then download into your local version of Warp. There are two options:
Option 1: Downloading the specific theme you want.
This option will take about 1-2 minutes to set up. The video below shows how I download the specific pride.yaml file and pride background image into my local Warp directory.
Run
mkdir -p ~/.warp/themes
Run
cd ~/.warp/themes
Run
mkdir holiday
Run
vi pride.yaml
.A blank .yaml file should show up in your terminal
Copy paste the contents of pride.yaml in the open source repo to the pride.yaml file you just generated locally
Press
:wq
to save the contents of your pride.yaml file and quit
Download the pride\_bg.jpg image from the open source repo, make sure to name it "pride\_bg.jpg"
Run
cp ~/Downloads/pride_bg.jpg ~/.warp/themes/holiday
Quit Warp and then open it back up
Go to Settings > Appearance > Choose the theme you just added
Option 2: Downloading the entire themes repo locally.
This option is faster, but you will end up with all the themes in the open source repo. The video below shows how I cloned the themes repository into my local Warp directory.
Go to the open source themes repo home page
Press on the "Code" dropdown and copy the HTTPS link to the git repository
Run
git clone <Insert HTTPS link that you just copied>
Wait a few seconds for it to finish running
Quit Warp and then open it back up
Go to Settings > Appearance > Choose the theme you just added
References
We hope this tutorial helped.Below, we'll include links to everything you need to get started.
Warp's open-source themes Github repository
Warp's official documentation for custom themes
Youtube video referenced in this blog
Discord channel where you can discuss Warp's open source themes
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
