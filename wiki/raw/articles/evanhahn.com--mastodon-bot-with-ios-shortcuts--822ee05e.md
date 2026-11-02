---
title: "A Mastodon bot powered by iOS Shortcuts"
url: "https://evanhahn.com/mastodon-bot-with-ios-shortcuts/"
fetched_at: 2026-11-02T10:18:53.064694+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# A Mastodon bot powered by iOS Shortcuts

Source: https://evanhahn.com/mastodon-bot-with-ios-shortcuts/

A Mastodon bot powered by iOS Shortcuts
In short: I use iOS Shortcuts to run a Mastodon bot.
I run
a Mastodon bot that posts random quotes from
The Legend of Zelda: Link’s Awakening
. (The writing in that game is so charming!) I used to run it off a server, but for the past few days, it’s used an iOS Shortcut on my phone.
How it works
The bot is called Ulrira, named after
a beloved
Link’s Awakening
character
. Ulrira (the bot, not the character) samples a line from the text dump, then makes an HTTP request to post it. Here’s a screenshot of the full thing:
As you can see, everything here is hard-coded, from the server credentials to the file name. (It probably wouldn’t be hard to make this more generic, but I didn’t bother.)
This used to be a short, hand-written Bash script. I used the new AI-powered Shortcut creator and prompted this into existence. I said something like, “Here’s a Bash script. Turn this into a Shortcut.” Like a lot of LLM output, it wasn’t quite right, but it was useful for getting started.
Shortcuts doesn’t seem to have an elegant way to express something like “run this every 6 hours”, so I created four additional scheduler Shortcuts that call the main one. They run at 12am, 6am, 12pm, and 6pm.
That means there are five shortcuts in total: one to actually make the post, and four to schedule the main Shortcut at different times.
Why do it this way?
I didn’t want to pay for my server anymore, nor did I want to maintain it. When I went looking for alternatives, they either (1) cost money (2) had some significant limitation (for example, GitHub Actions requires me to update the repo every 60 days). This solution runs on a device with high uptime and is effectively free.
If you’re a pro software genius, you might complain that this is not reliable! It doesn’t work if my phone is offline, for example. Or what if I change timezones? But in the words of
Link’s Awakening
:
You’re good! You’re a pro, aren’t you? ………… Well, beat it! Pros aren’t allowed in here!
Follow the bot
here
.
