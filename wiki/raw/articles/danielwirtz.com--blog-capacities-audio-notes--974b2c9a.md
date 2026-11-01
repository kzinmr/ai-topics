---
title: "Audio notes to Capacities (iOS Shortcuts)"
url: "https://danielwirtz.com/blog/capacities-audio-notes"
fetched_at: 2026-11-01T10:01:33.461276+00:00
source: "danielwirtz.com"
tags: [blog, raw]
---

# Audio notes to Capacities (iOS Shortcuts)

Source: https://danielwirtz.com/blog/capacities-audio-notes

I’m currently using
Capacities
as my daily note-taking tool. There are a lot of things I like about capacities. One being, that it has a daily note feature that makes it easy to journal and to write down random thoughts.
The other day, I was thinking it would be nice to be able to do that with audio. I know that
Reflect
has a feature like that, but Capacities unfortunately not. After a bit of looking around, I remembered that Capacities has a API that allows you to append things to the daily notes.
On iOS there is the Shortcut app, that’s actually quite powerful. There are many actions in shortcuts, but the two that where interesting for my use case are:
Dictate text (Listens to audio, transcribes it and saves the text as a variable)
Get contents of URL (Let’s you send a HTTP request to a website or API)
Using both actions – and a bit of tinkering and testing – I was able to put together exactly what I was looking for. A button that I can press, that allows me to speak into my phone to make that appear in my daily notes.
Currently, there's a minor issue when using the outliner mode: bullets from iOS shortcuts aren't collapsible. I've raised made a small post the Requests & Idea board and hope the team considers it.
If you'd like to set up this shortcut yourself, you can copy my implementation here:
There are only two things you to change in the "Get contents of URL" action to get it running yourself:
Add your authentication token under
Header
→
Authorization
. Check out the
Capacities API docs
to learn how to generate your own token.
Add your space id in the under
Request body
→
spaceId
. You can find your space ID in Capacities under
Settings
→
Space settings
.
For a visual guide, I've included a screenshot of my implementation below:
If you don't need the timestamp, you can simplify the process even further. Just remove the "Current date", "Format", and "Text" actions. Then, simply pass the dictated text directly into the mdText field in the "Get contents of URL" action.
Also, you can easily add the shortcut to your lock screen, as a widget or in the control center.
