---
title: "Setting up a bottom-end Chromebook for development"
url: "https://tomrenner.com/posts/setting-up-chromebook/"
fetched_at: 2026-05-01T07:01:08.393185+00:00
source: "tomrenner.com"
tags: [blog, raw]
---

# Setting up a bottom-end Chromebook for development

Source: https://tomrenner.com/posts/setting-up-chromebook/

I like being able to code wherever I am.
“Unfortunately”
, my 15" laptop bought to run simulations for my degree still runs like a dream, so I can’t really justify buying myself a replacement for it. So instead, just over a year ago, I decided to get something that is:
Lightweight
Cheap
Allows me to code on the go
Looking around a bit, a budget Chromebook seemed like a good choice. I settled on an
Asus Chromebook C201
, which cost me £190. It has 4GB of RAM, a 16GB SSD, and weighs under a kilo.
I thought I could get away with keeping ChromeOS running and still end up with a passable development environment. Unfortunately, my first discovery was that the model I’d bought didn’t yet have the Android App Store Beta. I should probably have checked that earlier in the process.
However, reading around a bit I still thought development on ChromeOS on a bottom-end machine would be possible. Enter Chromebrew. A tool that promised me functional Vim, Python, and Git with little hassle.
Setting that up was reasonably easy. Although I mildly resent having to enable a special “developer mode” that gives you annoyingly beepy warnings when you boot, all in all it only took a couple of hours of googling to get my dotfiles cloned, vim and python installed, and a helloworld run to prove to myself it was workable.
I’ve now had the machine for just over a year I’ve concluded it’s worked pretty much exactly as intended. I now take it everywhere (I’m typing this on it!) because it weighs less than a kilo. And because the machine cost less than my phone (and all data on it is saved to the cloud somewhere) I’m not overly concerned about it being lost or stolen.
The major advantage is that having something that’s always on me lets me use spare half hours productively, where previously I would have just stared at my phone. It’s actually especially noticeable because I really dislike using my phone for a lot of things, like shopping or drafting emails longer than two sentences.
There are a few remaining annoyances, which come from the fact that you’re not really meant to use the terminal on ChromeOS. I haven’t got around to installing some of the basic command-line tools my fingers type automatically, like
less
or
man
. They’re not installed by default, which surprised me.
I also don’t think I can update ChromeOS without wiping my “developer-mode” set up, which is a pain. This doesn’t make the security nerd in me happy, as I don’t get any patches, nor the tech nerd, since I don’t get any new features. I want to do some more research into this, to see if I can work around it somehow.
All in all though this has been a really great change to my life. Having a computer small and light enough to code on everywhere, at a bargain-basement price, really has changed the way I work for the better.
