---
title: "The Silicon Underground"
url: "https://dfarq.homeip.net/the-6502-cpus-odd-debut/?utm_source=rss&utm_medium=rss&utm_campaign=the-6502-cpus-odd-debut"
fetched_at: 2026-09-17T10:01:21.013411+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# The Silicon Underground

Source: https://dfarq.homeip.net/the-6502-cpus-odd-debut/?utm_source=rss&utm_medium=rss&utm_campaign=the-6502-cpus-odd-debut

On September 16, 1975, the 6502 CPU made its debut. It was a simple, inexpensive processor designed and priced for everyone. The 6502 cost $25 when Intel’s closest equivalent cost $370. Unsurprisingly, its low price made it an immediate success and it ended up powering numerous computers and game consoles from the 1970s and 1980s.
The debut at Wescon
If you used a computer in the 1980s, there’s a reasonable chance it had a MOS 6502 CPU inside like this one.
MOS Technology intended to offer the 6501 and 6502 for sale at the Wescon trade show in San Francisco on September 16th, 1975. When they arrived, they found out no selling was permitted on the floor of the show.
To work around this prohibition, they quickly rented a suite at the St. Francis Hotel nearby. One MOS employee stayed at the booth, handing out directions to the hotel room for anyone who wanted to see the $25 CPU in action or buy one. Other members of the MOS staff sold the CPUs out of jars in the suite.
One of their customers that day was Steve Wozniak. In some interviews, he said he bought several chips. In other interviews he said he could only afford one at the time. Different interviews also differ on whether he bought from Chuck Peddle or Peddle’s wife. But they all agree it was the only chip he could afford. While competitors would demand correspondence on company letterhead, MOS would sell a CPU to anyone who had the money. And they’d let you borrow and photocopy the documentation at the show if you didn’t want to spend $10 to buy an official copy. In an interview in the December 12, 1983 issue of
Infoworld
, Woz said Intel charged $370 for an 8080 and would only sell through distributors, where he could buy a 6502 over the counter like electronics surplus.
But the initial purchase even skipped the formality of a counter. He handed over a $20 bill and they pulled a CPU out of a jar and handed it to him.
Early customers of the 6502 CPU
That’s how Apple ended up using 6502 CPUs. But they were hardly the only ones. 8-bit home computers from Acorn, Apple, Atari, and Commodore utilized the 6502 or a variant of it. If, like me, the first computer you owned or used was one of those brands, there is a very good chance a 6502 powered it. My first encounter with a computer of any kind was playing
Choplifter
on a Commodore VIC-20 in 1982 at my dad’s friend’s house. It had a 6502 under the hood.
And what if you couldn’t afford even a 6502? That was Atari’s predicament. MOS had you covered. They quickly designed several reduced-capability versions of the 6502 for meeting even lower price points. The Atari 2600 used one of these CPUs, the
MOS 6507
. Atari and Commodore both used these cheaper 6502 CPU variants to control disk drives as well.
The 6502’s origins
The 6502’s eight designers, Chuck Peddle, Bill Mensch, Rod Orgill, Harry Bawcom, Ray Hirt, Terry Holdt, Wil Mathys, and Mike Janes worked at
Motorola
on the 6800 CPU. But when Chuck Peddle accompanied salespeople on trips to sell the 6800 CPU, potential customers frequently voiced objections at the CPU’s cost and complexity. Instead, they would tell Peddle what they needed in an inexpensive processor, with a minimal list of instructions.
Motorola wasn’t interested in building a cheap CPU. They wanted to extend the 6800 even further, which they did with the 6809 and 68000 processors. Motorola ordered Peddle to stop work on the project, so Peddle declared the idea was his to do with what he pleased.
Eight of the 17 members of the Motorola 6800 design team ended up leaving Motorola, taking the idea with them. They landed at MOS technology, where they designed the CPU Motorola didn’t want. It was 43% smaller than the 6800 and implemented 55 of the 6800’s 72 instructions. This was enough to allow the 6502 to give the power of an 8-bit CPU at close to the cost of Intel’s 4-bit 4040 CPU. The very first 6502s lacked a Rotate Right (ROR) instruction. Later versions added this, bringing the official total to 56 instructions.
Initially the chip came in two versions. They were compatible with each other in software, but not electrically. The first one, the 6501, plugged into the Motorola 6800 socket. It wasn’t software compatible with the 6800, but it meant someone who had an existing design for a 6800 could use a 6501, rewrite the software, and save money on the hardware costs.
The 6502 used its own socket, and proved very successful. A version of the 6502 is still available today from Western Design Center, the company Bill Mensch founded after he left MOS Technology. It’s still used in embedded applications even today.
Pros and cons of the 6502
The 6502 was very efficient. It ran at relatively low clock rates even for its time, but its instructions finished in about half as many clock cycles as competing CPUs, so a 6502 running at 2 MHz could keep pace with a competing CPU running at 4 MHz.
But the tradeoff was the small number of instructions and registers. Bill Gates famously hated the 6502 because of that tradeoff. There were ways to make up for the small number of registers. I made up for it by stashing the contents of the X and Y registers in zero page, or pushing them onto the stack.
Making up for the lack of instructions to do multiplication and division was harder. The ROL instruction meant it could divide by 2 very efficiently. But the lack of ROR meant you had to ROL seven times to multiply by 2. MOS quickly added an ROR instruction. But adding instructions for decimal multiply and divide wasn’t going to happen. Accomplished 6502 programmers kept a library of math routines for that.
But if you could train yourself to code within the 6502’s limits, it was very fast and efficient. For me, the 6502 was the first CPU I ever coded on in assembly language, so I didn’t know any different.
Legal action from Motorola
Motorola didn’t take kindly to the 6501 and 6502. On November 3, 1975, Motorola sued, seeking to stop MOS from selling CPUs altogether. Allen-Bradley, one of MOS Technology’s backers, decided not to fight this case and sold their interest back to the founders. In March 1976, MOS Technology was running out of money and had to settle the case. They agreed to drop the 6501 processor, pay Motorola $200,000 and return any documents that Motorola contended were confidential. Both companies agreed to cross-license microprocessor patents. But the legal problems left MOS Technology in a precarious financial condition, and in November 1976, Commodore acquired MOS Technology.
Commodore soon needed all of MOS Technology’s production capacity and then some, but the 6502 was available from secondary sources like Synertek, Rockwell, VLSI, and NCR. Western Design Center still sells a modern version today, using fabrication from TSMC.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
