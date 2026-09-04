---
title: "Microsoft 6502 Basic released as open source Sept 3, 2025"
url: "https://dfarq.homeip.net/microsoft-6502-basic-released-as-open-source-sept-3-2025/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-6502-basic-released-as-open-source-sept-3-2025"
fetched_at: 2026-09-04T10:00:44.732779+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Microsoft 6502 Basic released as open source Sept 3, 2025

Source: https://dfarq.homeip.net/microsoft-6502-basic-released-as-open-source-sept-3-2025/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-6502-basic-released-as-open-source-sept-3-2025

On September 3, 2025, Microsoft released version 1.1 of its 6502 Basic as open source. This code formed the basis for Applesoft Basic on the Apple II series as well as Commodore Basic on all of Commodore’s 8-bit computers, including the C-64. It was the same code that Jack Tramiel licensed for a flat $25,000 and then included in more than 15 million computers.
The code could be built into ROM or it could load from tape or disk and execute from RAM. One of the reasons this code proved so influential was because millions of Commodore computers booted straight into it from ROM.
Origins of the Microsoft 6502 Basic code
Microsoft licensed 6502 Basic to Commodore for use on the Commodore PET and future 6502-based computers for a one-time $25,000 fee. Jack Tramiel was probably the last to get the better of Bill Gates in a business deal.
Microsoft released the code on
Github
under an MIT license, making it free to modify and reuse. Microsoft originally developed it on a DEC PDP-10 minicomputer, and it included directives to select which platform to cross-assemble it for. This allowed the same code to build for the
Apple II
,
Commodore PET
, Ohio Scientific Challenger, or
MOS Technology
KIM-1. It contained 6,955 lines of code, written between 1976 and 1978.
Part of the deal with Commodore was that Commodore could make changes but had to contribute any changes it made back to Microsoft. This code includes some bug fixes to the garbage collection that came from Commodore.
One codebase serving multiple 6502-based computers won’t necessarily surprise those who used these computers in the 1980s. It was common for multi-platform magazines like
Family Computing
and
Compute!
to publish
type-in programs
for several popular computers, and either provide one listing with changes for specific computers, or publish a listing for each machine. While only the simplest programs could run on both Commodore and Apple computers unmodified, their listings were more alike than they were different.
Vintage disassemblies of the code
The code wasn’t entirely unfamiliar when Microsoft released it. Numerous disassemblies of it have existed since the 1980s, but seeing Microsoft’s own comments is enlightening. A disassembly of C-64 Basic cross-referenced with the Microsoft code exists
here
.  Additionally, Compute! Books published a book by Dan Heeb called
Tool Kit: Basic
that stepped through every subroutine in Microsoft Basic, as implemented on the C-64 and VIC-20, showing how to use those routines in your own assembly language programs.
I’ve heard it said that in the 1980s, all software was open source as long as you had enough patience. Existence of these kinds of books is a good example. But seeing Microsoft’s own code gives previously unseen insight into how they developed in the 1970s, including how they used directives to use a single codebase across four different 6502-based platforms from three different manufacturers.
Influence of Microsoft 6502 Basic
I don’t think the influence of Microsoft’s 6502 Basic can be overstated. My story of it is hardly unique. Like millions of other Gen Xers, my first computer was a Commodore 8-bit that booted straight into Basic when you powered the machine on. Many of my earliest experiences with a computer involved sitting at a keyboard, writing simple programs or typing in a program from the latest magazine, debugging it, and then figuring out how to modify it after I got bored with it.
When I jump on a Zoom call from my office in my home and someone in their 50s sees the Commodore computers hanging on my wall behind me, they often tell me a similar story. Or they tell me they were into Apple, and then we laugh about the old rivalry. Maybe someday, someone will tell me they grew up with an Ohio Scientific Challenger. I hope so.
Regardless of the platform, a generation of IT workers learned how computers worked by writing and modifying programs written in Microsoft’s 6502 Basic. Transitioning to
8086 Basic
or to
QuickBasic
on a PC from 6502 Basic was very easy.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
