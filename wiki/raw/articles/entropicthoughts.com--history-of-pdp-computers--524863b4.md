---
title: "Extremely brief history of PDP computers"
url: "https://entropicthoughts.com/history-of-pdp-computers"
fetched_at: 2026-10-30T10:00:48.571255+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Extremely brief history of PDP computers

Source: https://entropicthoughts.com/history-of-pdp-computers

I don’t know why I started to put this together. These machines fascinate me,
because so much of early computing/hacker type culture happened on them. I
started writing a table, but realised a timeline would be more intuitive. In
this graph, the price is for a minimal configuration and adjusted for inflation.
The time is the memory cycle time, a decent proxy for speed.
Some notes:
The
pdp
-1 was created mostly as an experiment. At the time, industrial
control systems used either humans or complicated contraptions of logic boards
to make decisions. Some engineers at
dec
wanted to see if there was a
customer base willing to use general-purpose computers instead.
1
But
it wasn’t called a computer then, because the word “computer” back then meant
big mainframe systems that ran batch calculations.
The
pdp
-4 was a variant of
pdp
-1 that was a little slower and much
cheaper. It was not compatible with the
pdp
-1. The
pdp
-4 was upgraded with
new chip technology and became the
pdp
-7, which was then optimised further
for cost and speed and became the
pdp
-9.
The
pdp
-5 was created when they realised the
pdp
-1 and
pdp
-4 machines
were overkill for industrial control systems. By being smaller, it could be
much cheaper, at the cost of compatibility with
pdp
-1 and
pdp
-4. It was
still intended for roughly the same market. The chip upgrade turned it into
the
pdp
-8.
The
pdp
-6 was a completely different beast, aimed at a different market. It
supported having tonnes of directly-addressable memory, as well as memory
protection, so it could be used as a time-sharing system. The amount of memory
made it run Lisp well.
2
The smaller machines could also run Lisp, but not
large Lisp programs.
With the chip upgrade, it became the
pdp
-10.
The
pdp
-11 was a new architecture again, intended to subsume all the
previous models, to avoid running three incompatible lines in parallel. There
were many variants of the
pdp
-11, with various performance characteristics
and corresponding price points. However, even its most powerful configuration
wasn’t powerful enough to attract many
pdp
-10 users.
The
vax
came much later, but it’s included in the table anyway because it is
what eventually subsumed the
pdp
-10. The
vax
was somewhat compatible with
the
pdp
-11, but they served different markets.
There is a noticeable split in the hacker culture between users of the smaller
(18 bit and less) and larger (32 bits and more) computers, exemplified by the
contrast between Unix and Emacs. Unix was first created on
pdp
-7, then ported
to
pdp
-11, then distributed to other
pdp
-11 users. The fact that it needed
to run on these smaller machines, and still handle time sharing, shaped much of
its implementation and interface. The same thing is true of the C language and
standard library. Then we have something like Emacs, which was created on the
massive
pdp
-10, and gained popularity with other
pdp
-10 users. It had plenty
of hardware resources to use, and it did. The same thing is true of many Lisp
variants.
What decided whether you became a small-computer hacker or large-computer hacker
was what your employer could afford. Unix was created at Bell Labs, a private
company that tried to do more with less. Emacs, in contrast, was built at
mit
,
which at the time was flush with
darpa
money. This is why Richard Gabriel
calls it
“
mit
/Stanford style” and “New Jersey approach”
.
Some other examples of things that were developed on the
pdp
-11 includes
Usenet,
vi
,
rsx
-11 (another operating system whose lineage continues into
Windows
nt
),
make
, the idea of a shell with composable commands, plus tiny
programming languages like
awk
. Things that were made with the
pdp
-10
includes Scheme, TeX, Zork, email, and Microsoft
basic
.
What do I want to say with this? I don’t know.
