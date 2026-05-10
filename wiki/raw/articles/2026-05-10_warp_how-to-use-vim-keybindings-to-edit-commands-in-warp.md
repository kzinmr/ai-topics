---
title: "How to use Vim keybindings to edit commands in Warp"
source: "Warp Blog"
url: "https://www.warp.dev/blog/how-to-use-vim-keybindings-to-edit-commands-in-warp"
scraped: "2026-05-10T01:27:33.670351+00:00"
lastmod: "2026-04-24T14:39:37.000Z"
type: "sitemap"
---

# How to use Vim keybindings to edit commands in Warp

**Source**: [https://www.warp.dev/blog/how-to-use-vim-keybindings-to-edit-commands-in-warp](https://www.warp.dev/blog/how-to-use-vim-keybindings-to-edit-commands-in-warp)

Product
How to use Vim keybindings to edit commands in Warp
Lucie le Blanc
January 4, 2024
Warp recently released the option to edit commands with Vim keybindings. This setting is now generally available.
Learn how to enable Vim-style editing in Warp and which settings you might want to configure.
What are Vim keybindings and why should you use them?
Vim
and
Neovim
are programs which seek to improve on top of the vi text editor, a modal text editor used in many Unix-based operating systems.
Vim-style editing programs are popular and polarizing. Some developers may find them infuriating to learn. (Insert joke about remembering how to exit Vim here :q!)
However, once you develop the muscle memory, the promise of Vim is that you can edit files and commands much faster without ever needing to reach for your mouse.
Vim editing uses specific keybindings to navigate through text and edit text. For example, in Vim you use ‘j’ to move down instead of ↓ and you can use ‘x’ or ‘d’ to delete characters under a cursor.
If you’re accustomed to these keybindings for editing commands, you may want to enable Vim editing mode in Warp.
How to enable Vim editing in Warp
Because Warp has its own modern editing capabilities that override the shell, you will need to explicitly enable the option to edit commands with Vim keybindings.
You can enable this using the Command Palette (CMD-P) or by navigating to Settings → Features → Enable with Vim keybindings
Use CMD - P to adjust Vim editing settings from the Command Palette.
Find the Vim editing toggles under Settings → Features.
There are two options you can configure with Vim keybindings:
“Set unnamed register as system clipboard” lets you configure which clipboard the Vim editing program references when you initiate an operation like copy or yank.By default, Vim will reference its own “clipboard” scoped to the program instead of the MacOS clipboard; setting any unnamed register as the system clipboard will allow the Vim editing mode to access the MacOS clipboard instead
“Show Vim status bar” gives you the option to show an indicator on the command line to reference whether you’re currently in Insert Mode or Visual Mode for navigation. This can be helpful, but if you don’t like extra visual “noise” on your command line you will want to keep this turned off
How to navigate and edit commands with Vim in Warp
With Vim editing for commands enabled, you can use the standard Vim keybindings to switch between modes, navigate through text, insert, edit, paste, yank, and so on.
You can find the full list of supported keybindings
in the Warp docs
.
Try Vim editing in Warp today
Whether you’re a longtime Vim user or a new convert, we want to hear from you about your experience using Vim in Warp!
If you run into any bugs or unexpected behaviors, don’t hesitate to file an issue or upvote an existing one on
Warp’s GitHub
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
