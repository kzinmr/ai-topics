---
title: "The Silicon Underground"
url: "https://dfarq.homeip.net/the-pentium-fdiv-bug-and-recall/?utm_source=rss&utm_medium=rss&utm_campaign=the-pentium-fdiv-bug-and-recall"
fetched_at: 2026-06-13T07:00:50.396182+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# The Silicon Underground

Source: https://dfarq.homeip.net/the-pentium-fdiv-bug-and-recall/?utm_source=rss&utm_medium=rss&utm_campaign=the-pentium-fdiv-bug-and-recall

On June 13, 1994, a mathematics professor discovered a bug in Intel’s then-new Pentium CPU. Intel’s new CPU was fast, but it couldn’t divide correctly. The bug became known as the Pentium FDIV bug. It resulted in Intel recalling 60 and 66 MHz Pentium CPUs in stepping levels prior to D1, and 75, 90, and 100 MHz Pentium CPUs in steppings prior to B5. The recall cost Intel $475 million and might have caused reputational damage if more viable competitors had been available at the time. Collectors prize a surviving Pentium CPU with the FDIV bug today.
How Intel’s Pentium FDIV bug was discovered
Early Pentium CPUs contained a flaw, called the FDIV bug. It caused them to perform floating point division incorrectly in some circumstances.
Thomas Nicely, a professor of mathematics at Lynchburg College, was calculating prime numbers when he saw some inconsistencies in his calculations in June 1994. He had a fleet of
486s
doing calculations and had recently added a Pentium. The Pentium was more than twice as fast, but after five months of investigation, he proved the 486s were more accurate. He disclosed his findings to Intel and also asked academic peers to check his work against 486DX4, Pentium, and
Pentium clone
systems. The peers independently verified the problem, and Intel had also become aware of a problem on its own around June 1994. Intel officially acknowledged the bug October 30, 1994.
Intel changed algorithms for floating point division with the Pentium, using a method that was twice as fast per clock cycle as the method used in the
486DX
. There was nothing wrong with the algorithm the Pentium used, just in Intel’s implementation. The Pentium contained a table with 1,066 values in it, and five of those values were set incorrectly.
The incorrect calculations were relatively rare, but they happened every time. In the worst case, the error could occur at the fourth most significant digit. But it usually happened at the 9th or 10th significant digit. One commonly reported example at the fourth most significant digit that works in Windows Calculator is dividing 4,195,835 by 3,145,727. It should result in 1.333820449136241002. But the Pentium with the bug reports 1.333739068902037589.
The story in the media
The story first appeared in the media on November 7, 1994, in an article in
Electronic Engineering Times
titled, “Intel fixes a Pentium FPU glitch” by Alexander Wolfe. CNN reported it in a segment aired on November 22, 1994. The
New York Times
also reported it and so did the
Boston Globe,
on the front page.
The Pentium recall
Intel initially claimed the error wasn’t serious and wouldn’t affect most users. They would replace the processors for users who could prove they were affected. This didn’t go over well, because the errors didn’t happen at random. The numbers it miscalculated would always miscalculate. The error even manifested itself in Quake, causing certain angles to display incorrectly. Corporate buyers started demanding replacements, and the PC manufacturers stepped in offering to replace the CPUs before Intel did.
On December 20, 1994, Intel finally offered to replace all of the flawed CPUs. But even at that point, Intel dropped the ball. Intel required end users to request the replacements and replace the chips themselves. They did not allow retailers and computer manufacturers to participate. Changing a Pentium CPU isn’t a difficult procedure for someone used to working on computers. But it would be nerve-wracking for someone who’s never done it before.
On January 17, 1995, Intel announced a pre-tax charge of $475 million against earnings. Ostensibly this was the total cost of replacing the flawed processors.
The fallout from the Pentium FDIV bug
Intel’s response to the FDIV bug is a well-known and cited public relations problem. The PR impact of a problem was worse than the practical impact of the problem on customers. Most computer users really were unlikely to encounter the flaw in their day-to-day computing. But Intel’s initial reaction to not replace chips unless customers could guarantee they were affected caused pushback from a vocal minority of industry experts.
The subsequent publicity generated shook consumer confidence in the CPUs, creating an opening for
NexGen
, who was then the maker of the only Pentium clone on the market at the time. It also led to a demand for action even from people unlikely to be affected by the issue. The Wall Street Journal quoted Andy Grove, Intel’s then-CEO, as saying “I think the kernel of the issue we missed … was that we presumed to tell somebody what they should or shouldn’t worry about, or should or shouldn’t do.”
Future CPUs from Intel as well as the rest of the industry underwent a more stringent formal verification process. This process helped Intel find several bugs in the Pentium 4 that could have led to a similar incident if they hadn’t been fixed before release.
What saved Intel from the FDIV bug doing more damage
The saving grace for Intel was the lack of alternatives at the time. The September 4, 1995 issue of Computerworld noted that
Nexgen
wasn’t selling CPUs in large enough volumes to present much of a threat, even after getting Compaq to agree to use its CPUs.
Cyrix
‘s Pentium competitor didn’t come out until October 1995, and
AMD’s Pentium competitor
didn’t come out until March 1996.
With only one struggling competitor on the market, Pentium sales actually increased during the FDIV crisis, according to Intel’s 1994 annual report. By the time viable Pentium competitors reached the market, Intel was ready to move on to the
Pentium Pro
and
Pentium II
. While AMD did eventually catch up with Intel, the Pentium FDIV bug was a fairly distant memory by the time it happened.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
