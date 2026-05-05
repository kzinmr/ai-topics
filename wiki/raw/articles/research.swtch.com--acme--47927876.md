---
title: "research!rsc: A Tour of Acme"
url: "https://research.swtch.com/acme"
fetched_at: 2026-05-05T07:01:01.622908+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# research!rsc: A Tour of Acme

Source: https://research.swtch.com/acme

A Tour of Acme
Russ Cox
September 17, 2012
research.swtch.com/acme
Posted on Monday, September 17, 2012.
People I work with recognize my computer easily:
it's the one with nothing but yellow windows and blue bars on the screen.
That's the text editor acme, written by Rob Pike for Plan 9 in the early 1990s.
Acme focuses entirely on the idea of text as user interface.
It's difficult to explain acme without seeing it, though, so I've put together
a screencast explaining the basics of acme and showing a brief programming session.
Remember as you watch the video that the 854x480 screen is quite cramped.
Usually you'd run acme on a larger screen: even my MacBook Air has almost four times
as much screen real estate.
VIDEO
The video doesn't show everything acme can do, nor does it show all the ways you can use it.
Even small idioms like where you type text to be loaded or executed vary from user to user.
To learn more about acme, read Rob Pike's paper “
Acme: A User Interface for Programmers
” and then try it.
Acme runs on most operating systems.
If you use
Plan 9 from Bell Labs
, you already have it.
If you use FreeBSD, Linux, OS X, or most other Unix clones, you can get it as part of
Plan 9 from User Space
.
If you use Windows, I suggest trying acme as packaged in
acme stand alone complex
, which is based on the Inferno programming environment.
Mini-FAQ
:
Q. Can I use scalable fonts?
A. On the Mac, yes. If you run
acme -f /mnt/font/Monaco/16a/font
you get 16-point anti-aliased Monaco as your font, served via
fontsrv
. If you'd like to add X11 support to fontsrv, I'd be happy to apply the patch.
Q. Do I need X11 to build on the Mac?
A. No. The build will complain that it cannot build ‘snarfer’ but it should complete otherwise. You probably don't need snarfer.
If you're interested in history, the predecessor to acme was called help. Rob Pike's paper “
A Minimalist Global User Interface
” describes it. See also “
The Text Editor sam
”
Correction
: the smiley program in the video was written by Ken Thompson.
I got it from Dennis Ritchie, the more meticulous archivist of the pair.
