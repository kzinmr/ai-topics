---
title: "Linux first announced August 25, 1991"
url: "https://dfarq.homeip.net/linux-kernel-announced-august-25-1991/?utm_source=rss&utm_medium=rss&utm_campaign=linux-kernel-announced-august-25-1991"
fetched_at: 2026-08-26T10:01:00.809422+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Linux first announced August 25, 1991

Source: https://dfarq.homeip.net/linux-kernel-announced-august-25-1991/?utm_source=rss&utm_medium=rss&utm_campaign=linux-kernel-announced-august-25-1991

On August 25, 1991, Linus Torvalds wrote a message that changed the world. He didn’t expect that when he wrote it, that’s clear from the message and some of the replies. He had something he wanted to share with his fellow hobbyists, and he wanted some feedback. He was working on a project, an operating system he called Linux. And on that Sunday afternoon, he announced Linux for the first time by posting a message to a Usenet group called comp.os.minix.
The message was very informal, even including two
emojis
. Usenet, if you’re wondering, was one of the major uses of the Internet in the days before the Web. It is essentially a decentralized discussion forum or message board and still exists today, though it’s not as prominent as it was in 1991. Old Usenet posts can be a goldmine of information, and fortunately, an early dotcom,
Deja News
, archived it. Thanks to that, you can still read the
message thread
today.
Humble beginnings when Linux was first announced
Linus Torvalds first announced his creation, Linux, very informally on August 25, 1991, on comp.os.minix on Usenet.
In the announcement, Torvalds said he had been working on a free hobby operating system for 386/
486
PCs since April, and he had two key tools, the bash shell and gcc compiler, running under it. He said it wouldn’t be “big and professional like gnu” and warned it wasn’t portable and would probably never support anything other than AT hard disks.
He saw it as an alternative to Minix, a Unix-like operating system designed primarily as a teaching aid for computer science students. Minix ran on inexpensive PC clones, but it wasn’t truly open source and it didn’t take full advantage of 386 processors.
This left an opening for a suitably ambitious computer science student to walk in.
Linux’s opening
The world of Unix was dominated by expensive workstation computers made by companies like
Sun Microsystems
and Silicon Graphics that cost upwards of $10,000. Students who wanted to learn Unix could go to computer labs on campus and get computer time, but there weren’t always enough computers to go around.
Many Unix experts considered PCs toys. The hardware wasn’t as powerful as the hardware in Unix workstations. That started to change by the time the 386 came around, but if you wanted to run Unix on it, your choices were to buy
SCO Unix
, or run something like Minix that didn’t take full advantage of the hardware and still treated the PC as a toy.
What about GNU?
The GNU project was seeking to create a fully open source
Unix-like
operating system. GNU started in 1983 and by 1989 had all of the userland tools cloned, but lacked a kernel. The original GNU kernel started development in 1986 and ended up abandoned. In 1987, GNU decided on a new way forward, but delays over license uncertainty prevented work from starting until 1990.
This was the void Linus Torvalds walked into with Linux. Here was a kernel, written from scratch, that would run on a cheap 386SX-based PC, and could run at least some of the GNU tools. And on March 7, 1992, it adopted the GNU GPL, making it fully compatible, license-wise, with the GNU toolset. For perspective, in August 1991,
Gateway 2000
offered a 16 MHz 386SX with 2 MB RAM, dual floppies, a 40 MB hard drive, and a 14-inch monitor for $1495.
Longtime Linux kernel developer Alan Cox had said in multiple interviews he decided to get a 386 after he saw the Linux kernel and 386BSD announcement. Since 386BSD required a math coprocessor and Linux didn’t, and he didn’t have one, he installed Linux.
Linux vs proprietary Unix
Linux didn’t have proprietary Unix in its sights in 1991. Torvalds was happy to leave that battle to GNU. But as GNU’s kernel continued to be delayed and the Linux kernel continued to grow and mature, increasingly Linux looked like a viable alternative to proprietary Unix over time. The proprietary vendors weren’t necessarily hostile to Linux, at least not all of them. Silicon Graphics contributed code to the Linux kernel and Sun hosted numerous open source projects. IBM famously spent $1 billion contributing code to the Linux kernel early in the 21st century.
And as the early 2000s wore on, large, once-popular proprietary Unix variants started fading away. SGI’s Irix is gone, Sun’s Solaris is nearly gone, and even HP-UX went end of life in early 2026. IBM’s AIX survives, but IBM is also a major Linux vendor, having
acquired Red Hat in 2018
.
Linux vs Microsoft Windows
It was more natural to pit Linux against proprietary Unix than against Windows. But Microsoft had all of Unix in its sights with Windows NT, so of course comparisons did happen, and Microsoft was antagonistic about Linux, especially during the Gates and Ballmer eras. In more recent years, Microsoft has grown less hostile, even releasing some software for Linux under open source licenses.
How the Linux announcement changed the world
I don’t think it’s hyperbole to say Linux changed the world. Its humble beginnings in a dorm room read like the classic technology startup. It was a hobby OS that solved a problem for a young computer science student and gave him something to experiment on, and it kept growing over time, becoming capable of ever bigger things. Today it’s one of the top three most common operating system families in the world.
It’s largely a story of being in the right place at the right time and being up to the task. Torvalds was all three. There were other Unix-like projects going on at the time, even outside of GNU. BSD was also a contender. But BSD also lost momentum due to AT&T suing the University of California, Berkeley in 1992. AT&T lost in 1994, which meant BSD derivatives like FreeBSD were free to continue. But prior to 1994, Linux had no such doubt. That meant developers scared off by the lawsuit could (and did) seek refuge in the Linux camp. By the time
SCO sued
to try to stop or slow it down, Linux had too much momentum.
The
dotcom boom
needed an inexpensive operating system to fuel it. Linux proved itself during the boom, and even proved part of the business model in cases like
Red Hat
and
VA Linux
. And it’s remained an indispensable part of the computing landscape ever since.
Why Linux is more important than ever 35 years after its was first announced
Make no mistake, big tech is spying on you. This is going to piss off some people, but it needs to be said. Microsoft isn’t your friend. Google isn’t your friend. And Apple isn’t your friend. All of them force obsolescence onto you, rendering hardware unable to run current software even though it’s still perfectly capable of doing so. And all of them spy on you. The major difference is whether they lie about it or how much they do. And all of them do everything they can to sell you as many subscriptions as they can, forcing you pay monthly fees to use that expensive computer.
Now, I’m not so idealistic as to say examining source code is a fundamental human right. Not everyone wants or needs to be a computer scientist. But being able to write a letter to a loved one without a computer reading it, training an AI model on it, selling inferences about you to advertisers, and giving inferences about you to any government that wants it
is
a fundamental human right.
For several decades, I ran Linux on my servers while running Windows on the rest of my computers. This spring I installed Debian 13 on a PC that can no longer run Windows. Windows 11 won’t install on it unless I hack it, and even after I hack it to do so, I have to spend half a day changing it to make it run acceptably. Debian installed on it in less than 30 minutes and only asked me a few simple questions. It happily found and used all my hardware. And the overall user experience was very comfortable.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
