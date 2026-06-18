---
title: "How a Microsoft product from June 1979 led to the IBM PC"
url: "https://dfarq.homeip.net/how-a-microsoft-product-from-june-1979-led-to-the-ibm-pc/?utm_source=rss&utm_medium=rss&utm_campaign=how-a-microsoft-product-from-june-1979-led-to-the-ibm-pc"
fetched_at: 2026-06-18T07:01:31.025469+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# How a Microsoft product from June 1979 led to the IBM PC

Source: https://dfarq.homeip.net/how-a-microsoft-product-from-june-1979-led-to-the-ibm-pc/?utm_source=rss&utm_medium=rss&utm_campaign=how-a-microsoft-product-from-june-1979-led-to-the-ibm-pc

June 1979 is a significant month in history for Microsoft for two reasons. That month, they crossed the threshold of an installed base of 200,000 on its flagship 8080 Basic. And on June 18, 1979, Microsoft released a version of Basic for a new CPU called the Intel 8086. They had no way of knowing how significant the 8086 product would become.
Microsoft reworked its 1979 Basic for the 8086 to become IBM Cassette Basic, which shipped in ROM on every IBM PC. A more advanced version, IBM Advanced Basic, shipped on every boot disk.
The MS-DOS origin story is a frequently repeated and often misunderstood legend. I’ve probably mentioned it in more than a dozen blog posts, but Microsoft Basic for the 8086 relates to it directly. In 1980, IBM decided it wanted to release a desktop computer. They knew they wanted to use the Intel 8088 CPU,
which was a cost-reduced version of the 8086
. It was similar enough to the popular Intel 8080 and Zilog Z-80 8-bit processors to make converting software relatively straightforward. But being 16-bit, it was more powerful than those two CPUs and still relatively inexpensive. Conceptually the 8086/8088 extended the 8080 similarly to how
x86-64
extended the x86 architecture in more modern times, just without full binary backward compatibility.
Three things IBM wanted from Microsoft
IBM called on Microsoft because they wanted three things they thought Microsoft could provide: Basic, an operating system, and advice.
Microsoft 8086 Basic
They wanted Microsoft’s 8086 Basic. Microsoft Basic was already the de facto standard for the type of computer they wanted to build. Contrary to some stories, it was Microsoft Basic, not
MS-DOS
,
that made Bill Gates rich
. Basic made Gates a millionaire, and set the stage for DOS to make Gates a billionaire. Gates was already rich when IBM came calling.
The CP/M operating system
IBM wanted an
operating system called CP/M
. CP/M was also a de facto standard, and Microsoft was a large distributor of CP/M, bundling it with its
Softcard
, a hardware product they built for Apple computers. Yes, it was a hardware product that allowed a non Microsoft operating system to run on an
Apple computer
that caught IBM’s attention. Everything in that previous sentence sounds wrong, so if you need to read it again, that’s okay. Read it as many times as you need to until the irony sinks in.
IBM hoped they could sublicense CP/M from Microsoft. Microsoft didn’t have the rights to do that, and CP/M didn’t run on the 8086 at the time anyway.
Advice
The third thing they wanted was some advice. IBM was the biggest computer company in the world, but this was a new and unfamiliar market for them. They had tried to make a small computer before, but it didn’t catch on. They wanted a product that could sell 5,000 to 10,000 units per month, and an outside opinion from someone who knew the industry would help them make sure they were on the right track.
In IBM’s mind, Microsoft had all three things they wanted. And Bill Gates was not a complete stranger to IBM. John Opel, the chairman of IBM, knew his mother from her philanthropic work with the United Way.
8086 Basic ensured Microsoft would be in the deal
Fortunately for Bill Gates, he had two of the three things IBM wanted. Basic for 8086 already existed, the only question was if it would need any fine-tuning to run on IBM’s machine. The adjustments would be minor in any case. The product existed, it was shipping, and there is a very real possibility that Microsoft had an 8086-based machine in the office that they could use to show it running.
How Microsoft ended up providing the operating system
is its own story
.
And Gates wasn’t shy about giving advice to companies who licensed Microsoft Basic. Gates has said that the idea to put graphics characters on the Commodore PET was his suggestion. That goes against Commodore’s version of the story. Leonard Tramiel has said he wanted graphics characters so the PET could do two things: play card games, and draw a picture of the starship Enterprise from Star Trek.
The graphics characters seem like an odd thing for Gates to take credit for, especially given his famous disinterest in Commodore. But precisely because of that disinterest, I don’t know how he would have remembered the PET had that capability if it hadn’t been his idea. One possibility is that Commodore was already planning to do it, didn’t have any reason to mention it to Gates, and Gates made the suggestion, trying to be helpful, and remembers making the suggestion.
Suffice it to say, if Gates was willing to offer advice to Commodore, he was willing to do the same for IBM.
How Microsoft wanted to change the IBM PC
Having 8086 Basic more or less ready for delivery the day IBM came calling ensured that Microsoft would be in the deal. The advice from Gates also didn’t hurt, although initially he wanted IBM to change everything about the design. He really wanted IBM to use the upcoming
Motorola
68000 processor and Xenix, Microsoft’s Unix, as the operating system. The result would have been more powerful than the
5170 PC/AT
that IBM shipped in 1984. It also wouldn’t have run 8086 Basic, but 68000 Basic wouldn’t have been a problem for Microsoft.
Gates relented when IBM told him the 8088 decision was firm. So the 8086 Basic ended up being a key selling point for the IBM PC. And as part of the agreement, IBM included Microsoft cassette Basic in ROM on all of its PC and
PS/2 products
, even though none of those products after the original 5150 IBM PC had a facility for a cassette recorder. If you power up a PC, XT, AT, or PS/2 without a hard drive or a boot floppy, it drops into cassette Basic.
The cassette recorder was a point of contention. Microsoft said a disk drive made a lot more sense, especially at the price IBM was charging. IBM was going forward with it, saying it only needed 50 cents worth of hardware to support it, and reportedly they told Bill Gates to write 50 cents worth of software to go with it. IBM never made or sold a cassette recorder for the IBM PC, but they made the cassette port electrically identical to the TRS-80 cassette port so anyone who wanted to use cassette storage could purchase an appropriate cable and a suitable cassette recorder at the nearest Radio Shack.
The IBM PC became an ecosystem that
accounted for about 2/3 of the computers sold in the 1980s
— if you count the clones.
Gates’ personal software contribution to the IBM PC
I have no idea if Gates wrote any of that 50 cents worth of software for the cassette recorder himself. But one of his contributions was visible on the standard boot disk for the IBM PC. That contribution was donkey.bas, a simple game written in Basic that used software sprites, and the object of the game was to drive down the road and dodge donkeys standing in your way.
It was a very simple game, but it demonstrated how to create an Atari 2600-style video game in Microsoft Basic on the IBM PC. And, arguably, donkey.bas was a better game than some commercial Atari 2600 titles. The hardest part was creating and handling the sprites, which the program showed clearly how to do.
So if you played donkey.bas on an IBM PC as a kid like I did, you used software written personally by Bill Gates, maybe without realizing it.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
