---
title: "How to Open Warp from VS Code"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-open-warp-vscode"
scraped: "2026-05-10T01:27:31.507000+00:00"
lastmod: "2026-04-24T14:39:35.000Z"
type: "sitemap"
---

# How to Open Warp from VS Code

**Source**: [https://www.warp.dev/blog/how-to-open-warp-vscode](https://www.warp.dev/blog/how-to-open-warp-vscode)

Engineering
How to Open Warp from VS Code
Jess Wang
July 6, 2022
VS Code offers a default integration terminal that fits right in with the editor GUI, but many developers still prefer to use their own terminal of preference. I'm going to offer two ways for you to integration Warp with VSCode so you can open up your Warp terminal with just a keyboard shortcut.
Option 1: VS Code Configuration
This option will allow you to open up a new session of Warp from within VS Code.
VS Code > Settings > Preferences
Type "terminal" into the search bar
Where it says "Terminal > External: Osx Exec", replace whatever is there with "warp.app"
Now when you press Command + Shift + C, a new session of Warp should pop up.
Option 2: Warp Configuration
This option will allow you to focus your existing session of Warp while in VS Code, using Warp's Hotkey Window feature.
Open up a Warp window > Click menu in top right corner > Settings > Features
Enable the Hotkey Window feature
Set your keybinding to whatever you prefer
Go to VS Code and press that keybinding to focus & unfocus your Warp terminal window.
Want to try out Warp?
Download Warp using the Download button in the top right corner of this site. It's free to use. If you want to hear from the people who are already using Warp, go
here
.
Once you have Warp downloaded, you can check out our
official documentation
to see what features we have, or check out our socials to learn more. We appreciate any feedback.
Thanks for reading!
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
