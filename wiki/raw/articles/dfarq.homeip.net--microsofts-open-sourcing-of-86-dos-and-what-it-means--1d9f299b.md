---
title: "The Silicon Underground"
url: "https://dfarq.homeip.net/microsofts-open-sourcing-of-86-dos-and-what-it-means/?utm_source=rss&utm_medium=rss&utm_campaign=microsofts-open-sourcing-of-86-dos-and-what-it-means"
fetched_at: 2026-05-04T07:01:10.581766+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# The Silicon Underground

Source: https://dfarq.homeip.net/microsofts-open-sourcing-of-86-dos-and-what-it-means/?utm_source=rss&utm_medium=rss&utm_campaign=microsofts-open-sourcing-of-86-dos-and-what-it-means

On April 28, 2026, Microsoft unexpectedly
open sourced 86-DOS
. This is the direct ancestor to PC DOS 1.0. I’ve written a number of things about the controversies around PC DOS 1.0 and early versions of MS-DOS, so of course I need to say something about this, even if I’m a few days late.
CP/M, 86-DOS, Bill Gates, Gary Kildall, and the airplane
Because IBM and Digital Research couldn’t come to an agreement, the IBM PC shipped with an operating system from Microsoft instead.
I think the story around MS-DOS 1.0 is pretty well known at this point, seeing as people tell me their version of it every time I blog about it. There is some controversy about it, and I have definitely contributed to spreading that controversy. I’ll head off some of the but-actually guys by saying this is the operating system that IBM licensed from Bill Gates because Gary Kildall was too busy flying in his airplane to talk with IBM. And to another bunch of you but-actually guys, yes, I am completely aware that it was not Gary’s job to talk to IBM, it was his wife Dorothy’s job to talk to them, which she did. The TLDR is she was not comfortable with the NDA that IBM wanted them to sign, and she was also not comfortable with allowing IBM to name the operating system
PC DOS
.
Bill Gates to the rescue
Meanwhile, IBM was already talking with Microsoft and had attempted to sublicense
CP/M
from Microsoft. Problem was, Microsoft didn’t have the rights to sub license it to them, nor did the version IBM needed exist yet. But friend of Microsoft Tim Paterson, creator of the
Microsoft Softcard
, was working on an 8086-compatible clone of CP/M. Microsoft licensed this operating system from Seattle Computer Products for $50,000, then turned around and licensed this operating system to IBM while reserving the rate to also license it to anyone else they wanted to. This is why IBM computers shipped with something called PC DOS and clone computers shipped with something called MS-DOS, and yet they were mostly compatible.
Early versions of PC DOS have been disassembled and commented, but today, you can view very early source code from the author himself. Apparently Tim Paterson found 45-year-old printouts in his garage.
The controversy around 86-DOS
There have been a number of rumors about early PC DOS.
Gary Kildall
spoke of cryptic similarities between the two that he said he was the only person in the world who understood. But he didn’t elaborate.
A few years after Kildall died, and around the time
Caldera sued Microsoft
, John C. Dvorak wrote that he knew someone who claimed to have an early version of PC dos that contained an Easter egg that would print Kildall’s name and a copyright message. I wondered at the time if he was speaking of Jerry Pournelle. I actually asked Pournelle about that a couple of years later. He did not elaborate. But a number of years after that, he went on a podcast and he did elaborate. He said he had seen it, and computer pioneer Bill Godbout showed it to him. The problem with his story is he never shared the keystroke or command that produced the Easter egg. Godbout never shared it publicly before his death either.
A number of years ago, someone did an analysis to attempt to
prove that MS-DOS wasn’t derived from CP/M
source code. The problem with that is it proved what we already knew. We already knew MS-DOS was written in 8086 assembly language, while CP/M was written mostly in a higher-level language called PL/1 or PL/M. If 86-DOS contained stolen code, it was written from a memory dump, not from source code.
The CP/M source code has been available for a number of years. Caldera released it, along with some other Digital Research code.
Today, the 86-DOS code is available too.
The 86-DOS conspiracy
There is one man alive who would also know a lot about this. That’s Tim Paterson, the man who wrote 86-DOS. Patterson has always maintained he didn’t break any laws. And the action of releasing the code does call something into question. If it contained stolen code, why would he release the original code?
The last time I wrote about this, I speculated Pournelle may have conflated multiple 1980s stories. Microsoft Basic contained Easter eggs to keep companies from stealing it. Maybe Pournelle confused those two stories. At the time Dvorak published hints of Pournelle’s story, Pournelle was in his 50s. At that age, the brain becomes prone to such things. I notice my own tendencies to conflate when researching blog posts. I can’t write entirely from memory the way I did when I was 30.
Now, I do not disagree that Bill Gates double-crossed Gary Kildall. Nor do I disagree that Kildall was a visionary while Gates just saw a money making opportunity, and that the world would be a better place if we’d followed Kildall rather than just falling all over ourselves to give Gates as much money as possible.
But now we have
one more historical artifact to study
, and that’s a good thing.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Like this:
Like
Loading...
Related stories by Dave Farquhar
