---
title: "Athlon 64: How AMD turned the tables on Intel"
url: "https://dfarq.homeip.net/athlon-64-how-amd-turned-the-tables-on-intel/?utm_source=rss&utm_medium=rss&utm_campaign=athlon-64-how-amd-turned-the-tables-on-intel"
fetched_at: 2026-09-23T10:01:03.298184+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# Athlon 64: How AMD turned the tables on Intel

Source: https://dfarq.homeip.net/athlon-64-how-amd-turned-the-tables-on-intel/?utm_source=rss&utm_medium=rss&utm_campaign=athlon-64-how-amd-turned-the-tables-on-intel

23 years ago, on September 23, 2003, AMD changed the game for x86 once and for all. They released the Athlon 64 CPU, a chip that did something Intel didn’t want. Intel didn’t want to extend the x86 CPU architecture to 64 bits. But when AMD did it, it forced Intel to clone AMD, rather than the other way around.
Why Intel didn’t want to go 64-bit
With the Athlon 64, AMD pulled x86 kicking and screaming into the world of 64-bit, dragging Intel along with it.
Even in 2001, x86 had decades of baggage attached to it. It was a 32-bit architecture that had been extended from a 16-bit architecture. But that in turn had been extended from an 8-bit CPU design from 1972 that, believe it or not, originated at
Datapoint
, not Intel.
This was great for backward compatibility. 8-bit applications were very easy to port to x86 in the early 1980s, which was one of the reasons IBM chose the Intel 8088 for its original Model 5150 PC. Those early DOS applications still ran flawlessly on modern systems 30 years later. For that matter, it’s not impossible to get them running even today.
Removal of the ability to run 16-bit applications in 64-bit Windows was a design decision of the operating system, not a technical limitation of the CPU.
Intel wanted to start over to go 64-bit. Without having to worry about backward compatibility, they could design something that would be faster and more efficient. In theory at least, it would be able to scale higher in clock speed. And there was no question a new design would outperform a theoretical 64-bit x86 when running at the same speed because of efficiency. To paraphrase one of the best quotes in Tracy Kidder’s classic book
The Soul of a New Machine
, Intel didn’t want to just put a bag on the side of x86.
And if you are cynical, there was one more motivation. If Intel could start over, they wouldn’t have to worry about competing CPU designs, at least not for a very long time. The new design would be encumbered with so many patents, it might be 20 years before someone could clone it.
Keep in mind that in 2003, not only was AMD in the picture, but
Transmeta
was still in the picture, and
Cyrix
was fading but not completely gone.
Starting over with a new CPU architecture outright was massively attractive to Intel.
This new 64-bit architecture wasn’t theoretical, either. Intel was producing it. It was called Itanium, and it had been a long time coming. Intel first released it in June 2001, and announced it way back on June 8, 1994.
AMD’s risky bet and why they made it
AMD was well aware of the shortcomings of extending x86 to 64 bits. And they did it anyway. For them, the stakes were completely different.
AMD knew that if Itanium caught on, that would be the end for them as a CPU company, unless maybe they wanted to become just another ARM licensee. Being just another ARM licensee is much more attractive in 2026 than it was in 2003.
But they could see Itanium wasn’t catching on. It had its uses, and it was doing well enough in those niches, but Windows on Itanium was a non-starter. So much so,
The Register
called it “Itanic.”
AMD bet that there would be appeal in a 64-bit architecture that was fully backward compatible with x86 and natively ran 32-bit applications at full speed. People would be able to run 32-bit Windows and 32-bit applications on it if they needed to, and then when they were ready for 64-bit software, the hardware was there and ready to go. And they could continue to run 32-bit apps in 64-bit operating systems as long as needed to ease the transition.
The transition to 32 bits took a decade. AMD reasoned more people would be willing to upgrade to 64 bits if they made that transition as similar as the transition from the
286 to the 386
as possible. Because backward compatibility tends to sell well. For AMD, the baggage was a feature. It was desirable, even if it was inelegant.
They believed the market would willingly trade lower 64-bit performance in the long term for better 32-bit performance right away. They also believed that if Microsoft was willing to build Windows on Itanium, they would be willing to take a chance on 64-bit x86 as well. And as long as the 32-bit performance was competitive, the worst case scenario was AMD64 becoming a vestigial extension like 3DNow. The best case scenario was leapfrogging Intel.
So on September 23, 2003, AMD launched its Athlon 64, the first 64-bit x86 CPU.
Why the Athlon 64 was a hit
AMD64 was everything AMD hoped it would be. It was backward compatible with 32-bit x86. The 64-bit builds of Windows weren’t available immediately, and they didn’t catch on immediately, but you cannot say nobody used them. People did, in fact, use them. In late 2005, I was in charge of administering the complimentary antivirus software that Charter Communications provided to its subscribers. I’m not going to say say someone called me every day wanting 64-bit antivirus for 64-bit Windows. But it did happen once a week.
The transition took at least as long as AMD expected.
When I finally bought an Athlon 64 in 2011
, I found native 64-bit software was still scarce. I’m an outspoken Firefox fan; the reason I briefly switched to
Google Chrome
was to get a 64-bit web browser.
The Athlon 64 in the enterprise
A few months later, I got a better job with more pay and better growth potential. I can’t talk a lot about the job, but I was administering a mission critical system that ran on Windows, mostly on Dell hardware. I mention
Dell
because they were exclusively an Intel vendor for years. Cofounder and longtime AMD CEO
Jerry Sanders
once said of Michael Dell, “I can’t sell him a[n AMD]
K6
no matter what I do.”
It was the Athlon 64 that made Dell relent and finally start using AMD CPUs. Not only were they using them on desktop systems, but they were putting AMD CPUs in servers, an idea that would have been extremely controversial 5 years before. At least in the circles I ran in.
The Athlon 64 caught on because, in spite of its name, it was an outstanding 32-bit CPU. It was faster than an Intel CPU running at the same clock rate, and it used less power as well. The power consumption was the key to getting into the data center. The Intel name was a security blanket, even though AMD had been making x86 CPUs exactly as long as Intel. But certain decision makers bought Intel marketing and saw AMD as a second tier brand.
The thing is, when you have a data center with hundreds of systems in it, the money you save on a more efficient CPU really talks.
Replacing Intel Prescott-based servers with AMD64 servers was not a universally popular idea. But you could tell a difference when you were standing behind a rack full of Intel-based servers versus a rack full of AMD based servers. The Intels ran hotter.
From an uptime perspective, we couldn’t see much difference. But the uptime metrics I collected showed the slight difference was in AMD’s favor. The performance metrics were in AMD’s favor too. So the AMD critics quickly ate their words.
I had a cousin who was a sales engineer at HP at the time, and he told me his enterprise customers were buying AMD64 for the power efficiency gains.
Intel giving in and cloning AMD64
In 2004, Intel wrote off the Itanium and cloned AMD64. They called it Intel64, but it was a blatant copy of the AMD implementation. The agreements that allowed AMD to use the x86 instruction set were reciprocal, giving Intel the rights to use the AMD64 instructions. So there was nothing illegal about what Intel did. Itanium continued to see use in specialized applications, but Intel quietly discontinued it in 2020.
AMD and Intel have been chasing and catching each other ever since. One of them will pass the other for a CPU generation or two, and then they will change positions. It’s not terribly different from the situation in 1999 with the
original Athlon
, when AMD outperformed Intel for the first time. The question in everyone’s mind was whether they would do it a second time. The Athlon 64 was the second time.
It was a big step forward. Eight years before, AMD was trying to pass off a high-clocked
486 as a Pentium equivalent
. With the Athlon 64, AMD was innovating.
There were times in the past when AMD seemed to be in trouble and one misstep away from fading into oblivion. You don’t hear that kind of talk much anymore. If anything, in 2026, it’s Intel that seems to be having more trouble than AMD.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
