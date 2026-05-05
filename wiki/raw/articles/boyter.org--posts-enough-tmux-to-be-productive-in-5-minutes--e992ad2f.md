---
title: "Learn Enough tmux to be Productive in 5 Minutes"
url: "https://boyter.org/posts/enough-tmux-to-be-productive-in-5-minutes/"
fetched_at: 2026-05-05T07:01:58.838553+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Learn Enough tmux to be Productive in 5 Minutes

Source: https://boyter.org/posts/enough-tmux-to-be-productive-in-5-minutes/

Learn Enough tmux to be Productive in 5 Minutes
2019/02/24
(387 words)
tmux the terminal multiplexer is one of those brilliant tools I use all day. I am not a tmux expert, nor do I have any need to be. What follows is the bare minimum you need to know to feel productive in tmux, written for some work colleagues.
The following assumes you have not configured or tweaked tmux in any way opting for the default settings.
From the command line to start or connect to tmux
tmux
start a new tmux session
tmux ls
view the current active sessions
tmux attach -t 0
attach to one of the tmux sessions listed from
ls
where you replace 0 with some number
Once inside tmux
Ctrl+B d
detach from the current session
To quit the current session type and enter exit till you are kicked out and you can use this to close sessions you have split horizontally or vertically
Ctrl+B s
view the current active sessions, then use up and down keys to highlight and enter to select
Ctrl+B '
split the current session window horizontally
Ctrl+B %
split the current session window vertically
Ctrl+B Alt+↓
expand the current active session window down, if you have split horizontally you can do this, you can push the Alt+↓ key multiple times to keep pushing down
Ctrl+B Alt+↑
expand the current active session window up, if you have split horizontally you can do this, you can push the Alt+↑ key multiple times to keep pushing down
Ctrl+B Alt+→
expand the current active session window right, if you have split vertically you can do this, you can push the Alt+→ key multiple times to keep pushing right
Ctrl+B Alt+←
expand the current active session window left, if you have split vertically you can do this, you can push the Alt+← key multiple times to keep pushing left
Ctrl+B ↓
move the current active session window to the one below
Ctrl+B ↑
move the current active session window to the one above
Ctrl+B →
move the current active session window to the one right
Ctrl+B ←
move the current active session window to the one left
Ctrl+B [
scroll mode
Ctrl+B space
start copy/yank mode when in scroll mode
Ctrl+B w
copy selection in scroll mode
Thats about all you need. Its all I ever use on a day to day basis.
