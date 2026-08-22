---
title: "Microsoft QuickBasic remembered"
url: "https://dfarq.homeip.net/microsoft-quickbasic-remembered/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-quickbasic-remembered"
fetched_at: 2026-08-22T10:01:33.761660+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Microsoft QuickBasic remembered

Source: https://dfarq.homeip.net/microsoft-quickbasic-remembered/?utm_source=rss&utm_medium=rss&utm_campaign=microsoft-quickbasic-remembered

Microsoft QuickBasic was a commercially available programming language for MS-DOS, initially released August 18, 1985. Qbasic, the Basic interpreter included with
MS-DOS
versions 5 and 6, was a cut-down version of QuickBasic. Most notably, the bundled version lacked the ability to compile programs into standalone executable files. But otherwise, the two were compatible.
In this screenshot, I am compiling my
IBM 5170 setup program
using QuickBasic’s
Make EXE file
option.
QuickBasic was a commercially available Basic compiler suitable for creating standalone executable files written in Basic, a programming language that most 1980s home computers included, or at least had available as an inexpensive add-on.
QuickBasic was derived from and highly compatible with the Basic programming language that was
built into the IBM PC
and that came as part of MS-DOS prior to version 5 in the form of GW-Basic. It didn’t need line numbers and you could use labels to name your subroutines, but otherwise felt very familiar to anyone who’d used Microsoft Basic, whether on an IBM PC or another platform, even going all the way back to
Altair Basic
.
QBasic was easier to use than the earlier Basic interpreters. But it also served as a gateway to Microsoft’s separate-sale QuickBasic.
Advantages of Microsoft QuickBasic
QuickBasic admittedly was less powerful than languages like C or Pascal. But the ease of learning it provided a low barrier to entry. Someone who was interested in programming could mess around in Qbasic for free, since it came with DOS. If they ended up writing something useful and interesting and they wanted to distribute it, they could purchase QuickBasic for around $99 at a store like
Egghead Software
or maybe
Babbage’s
to gain the ability. Compiled programs had the advantage of being able to run straight from the command line as an EXE file like commercial software. It also made the program unlistable and allowed the program to run faster.
QuickBasic was and remains a good choice for easy software development. Sometimes I need a simple program that runs in DOS that I can write in a few minutes in Basic. It would be smaller and faster if I wrote in C or Pascal but would take longer to write. So I write it in QuickBasic, and save myself the time.
Converting GW-Basic or BASICA programs to QuickBasic
If you have an interesting GW-Basic, BASICA, or Qbasic program, maybe a
magazine type-in
, that you would like to be able to run as a standalone EXE, it frequently is possible to load the program into QuickBasic and compile it with little or no modification.
To do this, load the file into QuickBasic, then compile it. If the program comes across garbled when you load it into QuickBasic, you will need to convert the program into plain text format. To do this, exit QuickBasic and start GW-Basic, load the file using Basic’s
LOAD
command, then save the file with a slightly different name
and
append a comma and the letter a to the end of the command. Something like this:
SAVE “HELLO.BAS”,A
This will save the program as a plain text file. Then exit GW-Basic by typing the command
SYSTEM
, and then proceed to load your converted program into QuickBasic. Then, from QuickBasic’s
RUN
menu, select the option called
Make EXE file
.
I used this trick to create a standalone program to let me run my
IBM 5170 without a battery
.
QuickBasic’s legacy
Microsoft introduced QuickBasic in August 1985 and sold it through 1994. In the mid 1990s, Microsoft shifted focus to Visual Basic, a Basic derivative that was object-oriented like C++. This made it more suitable for developing programs for Windows. But for a generation of tinkerers who acquired an MS-DOS computer in the late 80s and early 90s, QuickBasic often served as a first introduction to software development.
Microsoft never created a QuickBasic-like product for Windows. The commercial product Liberty Basic is about the closest thing you’ll find to that, and it is still in active development and support.
The DOS editor
QuickBasic showed its influence in one other place. EDIT.COM in MS-DOS 5.0 and 6.x was a stub that ran qbasic.exe in a different mode, so Quickbasic’s full screen editor also became ubiquitous in DOS. A standalone version of the editor later appeared in Windows 95 and later. A couple of clones for Linux exist,
setedit
and
FTE
, and Microsoft themselves
revived the idea in 2025
, porting it to Windows, Mac OS and Linux and releasing it as open source. If you don’t like the monstrosity that AI-enabled Notepad has become, you can go all the way back to text-mode edit if you like.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
