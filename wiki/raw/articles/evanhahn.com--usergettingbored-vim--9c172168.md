---
title: "Vim's UserGettingBored autocmd"
url: "https://evanhahn.com/usergettingbored-vim/"
fetched_at: 2026-08-23T10:01:40.907816+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# Vim's UserGettingBored autocmd

Source: https://evanhahn.com/usergettingbored-vim/

Vim's UserGettingBored autocmd
In short: Vim has a joke
autocmd
called
UserGettingBored
that doesn’t do anything.
Vim’s
automatic commands
feature, usually shortened to “
autocmd
”, lets you run code when various events occur. For example, you could implement an auto-save feature by binding the
TextChanged
event to the
:w
command.
Vim has over 100 events, from “buffer was created” to “file was saved”. But one of them sticks out to me:
UserGettingBored
. Here’s the documentation:
UserGettingBored
: When the user presses the same key 42 times. Just kidding! :-)
When I saw this, I was busy doing something else and it completely derailed me. “I must know more,” I thought.
Here’s what I found:
Unfortunately, it doesn’t do anything. It only exists in the documentation (and some tests). If you try to use it with somethig like
autocmd UserGettingBored ...
, you’ll get a “no such group or event” error.
It’s present in
Vim
,
Neovim
, and
Vim Classic
.
It was first added by Bram Moolenaar in
July 2000
, over a year before Vim 6.0 was released. The original description was, “When the user hits CTRL-C. Just kidding!” And it didn’t do anything back then, so I don’t think it’s
ever
been real.
In August 2001, he
added the smiley face to the documentation
. It then read, “When the user hits CTRL-C. Just kidding! :-)”
Twelve years later, in 2013,
the description changed
to its current iteration: “When the user presses the same key 42 times. Just kidding! :-)”
In 2022, developer Mike Smith
created an unofficial plugin
inspired by this joke
autocmd
. If you press the same key 42 times in Insert mode, a picture of Samuel L. Jackson appears. 22 years later, it’s finally real.
