---
title: "Grep Match a Tab"
url: "https://boyter.org/2011/06/grep-match-a-tab/"
fetched_at: 2026-05-05T07:02:06.440769+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Grep Match a Tab

Source: https://boyter.org/2011/06/grep-match-a-tab/

Grep Match a Tab
2011/06/07
(116 words)
Ever wanted to match a tab while using grep for some reason? The trick (under bash anyway) is to Ctrl+V and then press the tab key so you get whatever you are looking for.
$ cat file_to_grep.txt | grep "^log    "
I was trying to match a file for the exact match of log and then a tab. Without the tab I ended up getting back a bunch of junk results like “logger” “logging” “login” etc…
The above gives me what I want although I suspect there is a better way to do this. I did look into using [[:space:]] but it matches spaces as well which ended up in my case not being accurate enough.
