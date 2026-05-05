---
title: "What's worked in Computer Science: 1999 v. 2015"
url: "https://danluu.com/butler-lampson-1999/"
fetched_at: 2026-05-05T07:01:32.761985+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# What's worked in Computer Science: 1999 v. 2015

Source: https://danluu.com/butler-lampson-1999/

In 1999, Butler Lampson gave a talk about the
past and future of “computer systems research”
.  Here are his opinions from 1999 on "what worked".
Yes
Maybe
No
Virtual memory
Parallelism
Capabilities
Address spaces
RISC
Fancy type systems
Packet nets
Garbage collection
Functional programming
Objects / subtypes
Reuse
Formal methods
RDB and SQL
Software engineering
Transactions
RPC
Bitmaps and GUIs
Distributed computing
Web
Security
Algorithms
Basically everything that was a Yes in 1999 is still important today. Looking at the Maybe category, we have:
Parallelism
This is, unfortunately, still a Maybe. Between the
end of Dennard scaling
and the continued demand for compute, chips now expose plenty of the parallelism to the programmer. Concurrency has gotten much easier to deal with, but really extracting anything close to the full performance available isn't much easier than it was in 1999.
In 2009,
Erik Meijer and Butler Lampson talked about this
, and Lampson's comment was that when they came up with threading, locks, and conditional variables at PARC, they thought they were creating something that programmers could use to take advantage of parallelism, but that they now have decades of evidence that they were wrong. Lampson further remarks that to do parallel programming, what you need to do is put all your parallelism into a little box and then have a wizard go write the code in that box. Not much has changed since 2009.
Also, note that I'm using the same criteria to judge all of these. Whenever you say something doesn't work, someone will drop in say that, no wait, here's a PhD that demonstrates that someone has once done this thing, or here are nine programs that demonstrate that Idris is, in fact, widely used in large scale production systems. I take Lampson's view, which is that if the vast majority of programmers are literally incapable of using a certain class of technologies, that class of technologies has probably not succeeded.
On recent advancements in parallelism, Intel
recently added features that make it easier to take advantage of trivial parallelism by co-scheduling multiple applications on the same machine without interference
, but outside of a couple big companies, no one's really taking advantage of this yet. They also added hardware support for STM recently, but it's still not clear how much STM helps with usability when designing large scale systems.
If this was a Maybe in 1999 it's certainly a No now. In the 80s and 90s a lot of folks, probably the majority of folks, believed RISC was going to take over the world and x86 was doomed. In 1991, Apple, IBM, and Motorola got together to create PowerPC (PPC) chips that were going to demolish Intel in the consumer market. They opened the Somerset facility for chip design, and collected a lot of their best folks for what was going to be a world changing effort. At the upper end of the market, DEC's Alpha chips were getting twice the performance of Intel's, and their threat to the workstation market was serious enough that Microsoft ported Windows NT to the Alpha. DEC started a project to do dynamic translation from x86 to Alpha; at the time the project started, the projected performance of x86 basically running in emulation on Alpha was substantially better than native x86 on Intel chips.
In 1995, Intel released the Pentium Pro. At the time, it had better workstation integer performance than anything else out there, including much more expensive chips targeted at workstations, and its floating point performance was within a factor of 2 of high-end chips. That immediately destroyed the viability of the mainstream Apple/IBM/Moto PPC chips, and in 1998 IBM pulled out of the Somerset venture and everyone gave up on really trying to produce desktop class PPC chips. Apple continued to sell PPC chips for a while, but they had to cook up bogus benchmarks to make the chips look even remotely competitive. By the time DEC finished their dynamic translation efforts, x86 in translation was barely faster than native x86 in floating point code, and substantially slower in integer code. While that was a very impressive technical feat, it wasn't enough to convince people to switch from x86 to Alpha, which killed DEC's attempts to move into the low-end workstation and high-end PC market.
In 1999, high-end workstations were still mostly RISC machines, and supercomputers were a mix of custom chips, RISC chips, and x86 chips. Today, Intel dominates the workstation market with x86, and the supercomputer market has also moved towards x86. Other than POWER, RISC ISAs were mostly wiped out (like PA-RISC) or managed to survive by moving to the low-margin embedded market (like MIPS), which wasn't profitable enough for Intel to pursue with any vigor. You can see a kind of instruction set arbitrage that MIPS and ARM have been able to take advantage of because of this. Cavium and ARM will sell you a network card that offloads a lot of processing to the NIC, which have a bunch of cheap MIPS and ARM processors, respectively, on board. The low-end processors aren't inherently better at processing packets than Intel CPUS; they're just priced low enough that Intel won't compete on price because they don't want to cannibalize their higher margin chips with sales of lower margin chips. MIPS and ARM have no such concerns because MIPS flunked out of the high-end processor market and ARM has yet to get there. If the best thing you can say about RISC chips is that they manage to exist in areas where the profit margins are too low for Intel to care, that's not exactly great evidence of a RISC victory. That Intel ceded the low end of the market might seem ironic considering Intel's origins, but they've always been aggressive about moving upmarket (they did the same thing when they transitioned from DRAM to SRAM to flash, ceding the barely profitable DRAM market to their competitors).
If there's any threat to x86, it's ARM, and it's their business model that's a threat, not their ISA. And as for their ISA, ARM's biggest inroads into mobile and personal computing came with ARMv7 and earlier ISAs, which aren't really more RISC-like than x86. In the area in which they dominated, their "modern" RISC-y ISA, ARMv8, is hopeless and will continue to be hopeless for years, and they'll continue to dominate with their non-RISC ISAs.
In retrospect, the reason RISC chips looked so good in the 80s was that you could fit a complete high-performance RISC microprocessor onto a single chip, which wasn't true of x86 chips at the time. But as we got more transistors, this mattered less.
It's possible to nitpick RISC being a no by saying that modern processors translate x86 ops into RISC micro-ops internally, but if you listened to talk at the time, people thought that having an external RISC ISA would be so much lower overhead that RISC would win, which has clearly not happened. Moreover, modern chips also do micro-op fusion in order to fuse operations into decidedly un-RISC-y operations. A clean RISC ISA is a beautiful thing. I sometimes re-read Dick Sites's
explanation of the Alpha design
just to admire it, but it turns out beauty isn't really critical for the commercial success of an ISA.
Garbage collection
This is a huge Yes now. Every language that's become successful since 1999 has GC and is designed for all normal users to use it to manage all memory. In five years, Rust or D might make that last sentence untrue, but even if that happens, GC will still be in the yes category.
Reuse
Yes, I think, although I'm not 100% sure what Lampson was referring to here. Lampson said that reuse was a maybe because it sometimes works (for UNIX filters, OS, DB, browser) but was also flaky (for OLE/COM). There are now widely used substitutes for OLE; service oriented architectures also seem to fit his definition of re-use.
Looking at the No category, we have:
Capabilities
Yes. Widely used on mobile operating systems.
Fancy type systems
It depends on what qualifies as a fancy type system, but if “fancy” means something at least as fancy as Scala or Haskell, this is a No. That's even true if you relax the standard to an ML-like type system. Boy, would I love to be able to do everyday programming in an ML (F# seems particularly nice to me), but we're pretty far from that.
In 1999 C, and C++ were mainstream, along with maybe Visual Basic and Pascal, with Java on the rise. And maybe Perl, but at the time most people thought of it as a scripting language, not something you'd use for "real" development. PHP, Python, Ruby, and JavaScript all existed, but were mostly used in small niches. Back then, Tcl was one of the most widely used scripting languages, and it wasn't exactly widely used. Now, PHP, Python, Ruby, and JavaScript are not only more mainstream than Tcl, but more mainstream than C and C++. C# is probably the only other language in the same league as those languages in terms of popularity, and Go looks like the only language that's growing fast enough to catch up in the foreseeable future. Since 1999, we have a bunch of dynamic languages, and a few languages with type systems that are specifically designed not to be fancy.
Maybe I'll get to use F# for non-hobby projects in another 16 years, but things don't look promising.
Functional programming
I'd lean towards Maybe on this one, although this is arguably a No. Functional languages are still quite niche, but functional programming ideas are now mainstream, at least for the HN/reddit/twitter crowd.
You might say that I'm being too generous to functional programming here because I have a soft spot for immutability. That's fair. In 1982,
James Morris wrote
:
Functional languages are unnatural to use; but so are knives and forks, diplomatic protocols, double-entry bookkeeping, and a host of other things modern civilization has found useful. Any discipline is unnatural, in that it takes a while to master, and can break down in extreme situations. That is no reason to reject a particular discipline. The important question is whether functional programming in unnatural the way Haiku is unnatural or the way Karate is unnatural.
Haiku is a rigid form poetry in which each poem must have precisely three lines and seventeen syllables. As with poetry, writing a purely functional program often gives one a feeling of great aesthetic pleasure. It is often very enlightening to read or write such a program. These are undoubted benefits, but real programmers are more results-oriented and are not interested in laboring over a program that already works.
They will not accept a language discipline unless it can be used to write programs to solve problems the first time -- just as Karate is occasionally used to deal with real problems as they present themselves. A person who has learned the discipline of Karate finds it directly applicable even in bar-room brawls where no one else knows Karate. Can the same be said of the functional programmer in today's computing environments? No.
Many people would make the same case today. I don't agree, but that's a matter of opinion, not a matter of fact.
Formal methods
Maybe? Formal methods have had high impact in a few areas. Model checking is omnipresent in chip design. Microsoft's
driver verification tool
has probably had more impact than all formal chip design tools combined, clang now has a fair amount of static analysis built in, and so on and so forth. But, formal methods are still quite niche, and the vast majority of developers don't apply formal methods.
Software engineering
No. In 1995, David Parnas had a talk at ICSE (the premier software engineering conference) about the fact that even the ICSE papers that won their “most influential paper award” (including two of Parnas's papers) had
very little impact on industry
.
Basically all of Parnas's criticisms are still true today. One of his suggestions, that there should be distinct conferences for researchers and for practitioners has been taken up, but there's not much cross-pollination between academic conferences like ICSE and FSE and practitioner-focused conferences like StrangeLoop and PyCon.
RPC
Yes. In fact RPCs are now so widely used that I've seen multiple RPCs considered harmful talks.
Distributed systems
Yes. These are so ubiquitous that startups with zero distributed systems expertise regularly use distributed systems provided by Amazon or Microsoft, and it's totally fine. The systems aren't perfect and there are some infamous downtime incidents, but if you compare the bit error rate of random storage from 1999 to something like EBS or Azure Blob Storage, distributed systems don't look so bad.
Security
Maybe? As with formal methods, a handful of projects with very high real world impact get a lot of mileage out of security research. But security still isn't a first class concern for most programmers.
Conclusion
What's worked in computer systems research?
Topic
1999
2015
Virtual memory
Yes
Yes
Address spaces
Yes
Yes
Packet nets
Yes
Yes
Objects / subtypes
Yes
Yes
RDB and SQL
Yes
Yes
Transactions
Yes
Yes
Bitmaps and GUIs
Yes
Yes
Web
Yes
Yes
Algorithms
Yes
Yes
Parallelism
Maybe
Maybe
RISC
Maybe
No
Garbage collection
Maybe
Yes
Reuse
Maybe
Yes
Capabilities
No
Yes
Fancy type systems
No
No
Functional programming
No
Maybe
Formal methods
No
Maybe
Software engineering
No
No
RPC
No
Yes
Distributed computing
No
Yes
Security
No
Maybe
Not only is every Yes from 1999 still Yes today, seven of the Maybes and Nos were upgraded, and only one was downgraded. And on top of that, there are a lot of topics like neural networks that weren't even worth adding to the list as a No that are an unambiguous Yes today.
In 1999, I was taking the SATs and applying to colleges. Today, I'm not really all that far into my career, and the landscape has changed substantially; many previously impractical academic topics are now widely used in industry. I probably have twice again as much time until the end of my career and
things are changing faster now than they were in 1999
. After reviewing Lampson's 1999 talk, I'm much more optimistic about research areas that haven't yielded much real-world impact (yet), like capability based computing and fancy type systems. It seems basically impossible to predict what areas will become valuable over the next thirty years.
Correction
This post originally had Capabilities as a No in 2015. In retrospect, I think that was a mistake and it should have been a Yes due to use on mobile.
Thanks to Seth Holloway, Leah Hanson, Ian Whitlock, Lindsey Kuper, Chris Ball, Steven McCarthy, Joe Wilder, David Wragg, Sophia Wisdom, and Alex Clemmer for comments/discussion.
