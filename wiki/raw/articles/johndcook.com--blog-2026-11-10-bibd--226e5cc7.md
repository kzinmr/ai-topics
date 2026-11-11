---
title: "Balanced Incomplete Block Designs"
url: "https://www.johndcook.com/blog/2026/11/10/bibd/"
fetched_at: 2026-11-11T10:01:30.460140+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Balanced Incomplete Block Designs

Source: https://www.johndcook.com/blog/2026/11/10/bibd/

Suppose you have
n
different fertilizers you want to test. The simplest experiment would be to take a big plot of land, divide it into
n
sections, and apply each fertilizer to a section. That’s fine if you have one big enough plot of land, and the land itself doesn’t matter.
If the fertilizer supplies a nutrient that is already abundant in a particular soil, you won’t see as much benefit from that fertilizer on that soil. Plots of land will vary in other ways besides soil composition—some may receive more sun than others, some may have better drainage, etc.—that may interact with the effect of the fertilizer. So you’d like to test your fertilizers on several different plots of land. Call the number of plots
b
.
Suppose each of your plots is large enough to test
q
<
n
fertilizers, i.e. the plots are not large enough to test every fertilizer on every plot. You would like to design your experiment so that each fertilizer is tested the same number of times, and so that every pair of fertilizers is tested somewhere on the same plot of land for a direct comparison.
The resulting experimental design is called a
balanced incomplete block design
or
BIBD
. The blocks are the plots of land. The design is incomplete because you cannot test everything on every plot. The design is balanced because every pair of fertilizers is tested together the same number of times. BIBDs are important in the
design of experiments
.
A BIBD is a special case of the
combinatorial designs
discussed in the previous post with parameters (
n
,
q
, 2, λ), i.e. the parameter
r
is set to 2 because you want every pair to appear in some number of blocks.
A design with parameters (
n
,
q
,
r
, λ) is sometimes called an
r
-(
n
,
q
, λ) design [1].
Steiner systems
correspond to λ = 1 and BIBDs correspond to
r
= 2.
While the number of blocks
b
is of interest, it is not an independent parameter. For combinatorial designs in general the number of blocks is determined by the other parameters:
Similarly, you may see the number of blocks each treatment appears in given as a parameter, but this count is also determined by the other parameters, namely
Examples
Here is a design to test
n
= 6 treatments on
b
= 10 plots, testing
q
= 3 treatments on each plot, with each pair of treatments (i.e.
r
= 2) appearing in λ = 2 plots, i.e. a (6, 3, 2) design.
0000011122
    1123423433
    2345554545
The way to read this is that each treatment is a number 0 through 5, and each column indicates the treatments tested in a particular block (plot).
Here is another example, an (8, 4, 3) design:
n
= 8 treatments, blocks of size
q
= 4, with each pair of treatments being tested in λ = 3 blocks.
00000001111222
    11123342334334
    22554666455455
    34675777677766
[1] Combinatorial designs are sometimes called
t
-designs, which makes sense if you denote the size of the set you’re looking for in each block by
t
but not if you denote it by
r
. You’ll see both conventions. And while we’re mentioning notational variations, the number of treatments is sometimes denoted
v
for variety, going back to agricultural applications, testing crop varieties.
