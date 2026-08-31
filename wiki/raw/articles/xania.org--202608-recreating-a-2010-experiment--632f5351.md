---
title: "Recreating a 2010 Experiment"
url: "http://xania.org/202608/recreating-a-2010-experiment?utm_source=feed&utm_medium=rss"
fetched_at: 2026-08-31T10:07:33.158516+00:00
source: "xania.org"
tags: [blog, raw]
---

# Recreating a 2010 Experiment

Source: http://xania.org/202608/recreating-a-2010-experiment?utm_source=feed&utm_medium=rss

Recreating a 2010 Experiment
Sometime around 2010, while I was working at Google, I came up with a fun mini project to
marry my love of retro computing with my excitement for working at big G.
I smuggled my BBC Master into the office and hooked it up over a serial cable to my
work desktop, and then after some jiggery-pokery, was able to get a terminal
emulator running. The BBC was a dumb terminal to the work machine, and I ran
lynx
and visited
google.com
, searched for
google
. I think I can safely say I’m the
only person who googled Google on a BBC Micro from within Google itself.
My Beeb still has the
moog@
sticker (my LDAP login) to show whose it was.
I was trying to replicate this at home but sadly Google no longer supports non-JS
browsers like
lynx
(I guess I could find another one that does?). But I did see
that DuckDuckGo has a “lite” mode. After an enormous amount of fiddling I was able
to recreate something similar:
The glory of DuckDuckGo on a Beeb.
The image above was captured with my own in-progress software PAL decoder
PALindrome
,
so the blurriness etc is likely from my inept implementation.
I used a cheap no-name USB serial converter
and an RS232-RS423 DIN cable. I first put the cable in 180
degrees the wrong way (bad keying on the cable, oops), but once correctly plugged in things started working. I initially tried with the
Master’s built-in
*TERMINAL
program, but it’s frankly pretty rubbish for this. I used the Acornsoft
“Termulator” ROM instead. 4800 baud was the fastest I could reliably get working, and it needed a bit of
work to get XON/XOFF configured. With some LLM help I got a
getty
running so I could log in with the Beeb.
It’s hard to type your muscle-memory password on a not-quite-normal keyboard! A hack to tell
lynx
not
to process XON/XOFF and not show colour:
INCLUDE
:
/etc/lynx/lynx.cfg
KEYMAP
:
^S:DO_NOTHING
KEYMAP
:
^Q:DO_NOTHING
SHOW_COLOR
:
never
The whole Heath Robinson setup.
A bit of double-nostalgia for me: 2010 is when my youngest was born, and we just celebrated his 16th…
where does the time go?
Despite all my
Compiler Explorer
commitments, and my
fun new(ish) job
, I’ve somehow managed to find time to
hack on things like this, and also use feedback from both PALindrome and some careful
audio recordings and test programs to “improve” the audio and video emulation of
jsbeeb
.
They make it arguably more authentic… but do sound and look objectively
worse – the nostalgia hit is worth it though! All configurable of course (play with the settings
on the settings page or the top right for quick settings).
