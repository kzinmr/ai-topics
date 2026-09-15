---
title: "How can I remove the Close button from my window caption?"
url: "https://devblogs.microsoft.com/oldnewthing/20260911-00/?p=112691"
fetched_at: 2026-09-15T10:01:19.959813+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# How can I remove the Close button from my window caption?

Source: https://devblogs.microsoft.com/oldnewthing/20260911-00/?p=112691

Occasionally, somebody wants to create a window without a Close button.
The only way to get rid of the Close button is not to have a System menu at all: Remove the
WS_
SYS­MENU
style from the window. But that also gets rid of the Minimize and Maximize buttons, so it’s kind of drastic.
If you want a System menu, or if you want Minimize and Maximize buttons, you can at least disable the Close button by disabling the
SC_CLOSE
menu item.
HMENU menu = GetSystemMenu(hwnd, FALSE);
EnableMenuItem(menu, SC_CLOSE, MF_DISABLED);
Of course, you could use the nuclear option and implement your own custom title bar. Then you can do whatever you want. But most people are probably not willing to take things to such an extreme.
But really, try not to hide or disable the Close the button at all. End users don’t like it. It makes them feel trapped.
