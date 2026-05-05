---
title: "Faster Inverse BWT"
url: "http://cbloomrants.blogspot.com/2021/03/faster-inverse-bwt.html"
fetched_at: 2026-05-05T07:01:48.377392+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Faster Inverse BWT

Source: http://cbloomrants.blogspot.com/2021/03/faster-inverse-bwt.html

The BWT (Burrows Wheeler Transform) has long fascinated people for its ability to capture complex correlations with
a very simple inverse transform.  Unfortunately despite that inverse transform being very simple, it is also slow.
I will briefly review the inverse BWT (i-BWT) and then look at ways to speed it up.
Jump to the end
for the punch line : speed results and source code.
Let's briefly review the basic BWT to establish the baseline algorithm and notation.
Given an input string like "inputstring" add an EOF symbol so S = "inputstring|" then form all rotations :
inputstring|
nputstring|i
putstring|in
utstring|inp
tstring|inpu
string|input
tring|inputs
ring|inputst
ing|inputstr
ng|inputstri
g|inputstrin
|inputstring
Then sort all the rows, this gives the matrix M :
g|inputstrin
ing|inputstr
inputstring|
ng|inputstri
nputstring|i
putstring|in
ring|inputst
string|input
tring|inputs
tstring|inpu
utstring|inp
|inputstring
^          ^
F          L
this is all the suffixes of the file, and we've sorted them all.  We've labeled the first column F
and the last column L.
The last column L is the BWT, which is what we transmit.  (typically we don't transmit the EOF character,
instead we transmit its location and leave it out of the BWT string that is sent).
In the matrix M each column is a permutation of the original string S (remember the rows are cyclic rotations).
The first column F is just the
alphabetic sort of S.  F can obviously be reconstructed from a histogram of S, which can be counted from L.
The column L is the original characters of S in order of their following suffixes.
The inverse transform is simple conceptually.  We transmit L, the BWT string (the last column), we need to
regenerate S the top row.
Because the rows are all just rotations of S, the character at F[i] on each row is the character that
follows L[i].  This gives you an answer to "what's the next character after this one?" which is all you
need :
Output decoded string D
Start with D=| the EOF character.

What's the next character?

L = nr|iinttsupg
F = giinnprsttu|

Find | in L , it's L[2]
so the next char is F[2] = i

D=|i

What's the next character?

Find i in L , it's L[4]  (NOT L[3])
so the next char is F[4] = n
D=|in

Then find n at L[5] (not L[0])
the next char is p, so D=|inp

after p is u, etc.
So you can just read out the characters one by one like that.
When a character occured multiple times in L we had to find the right one (which corresponds to the 
same location of that character in the original string S).  eg. when finding 'i' we needed L[4] not L[3]
because L[4] is the i that follows | in "input", while L[3] is the i in "string".
The way to do that is to find the same occurance number of that character.  If it's the 2nd "i" in F, we want
that to map to the 2nd "i" in L.
The reason is because L has the characters sorted by their suffixes, while F is sorted by the whole strings.
So when they are the same symbol in L, then the order they occur in L is the same as the order the occur in F.
For example the n's in F :
ng|inputstri
nputstring|i
are in this order because "ng" is less than "np"; in the last column L, the n's occur as :
g|inputstrin
putstring|in
they are sorted by their suffixes "g|" and "pu", so they are in the same order.
So the nth occurance of each character in L/F corresponds to the nth occurance of each character in L/F.
The main thing we need for inversion is this mapping between L and F for each character.
It turns out to be more convenient to go backwards and make the mapping from L to F (rather than F to L).
This is because the F array can just be implicit, we never need to make it in memory.  F is just the "cum prob"
table.  That is :
Each symbol has a histogram count[s]
start[s] = prefix sum of counts < s
cumulative probability range[s] = [ start[s] , start[s] + count[s] )
(closed interval on low end, open interval on high end)
F[] = fill s in range[s]

To find the nth occurance of s in F[] is just i = start[s] + n
This is the same array you would use in arithmetic coding or RANS.
We'll calling the mapping from L to F , LF[] and it is just constructed thusly :
scan L[]
s = L[i]
count C[s] as you go (start at zero)
find the C[s]th occurance of s in F[]
LF[i] = start[s] + C[s]
then C[s] ++
Now LF[i] takes us from the symbol at L[i] to the same symbol in F[] which will be at F[ LF[i] ], then from
there you can step to the prior symbol, which is at L[ LF[i] ].
Note that this is backwards from what we were doing before, so we are now reading at the stream in
reverse.  To read out the i-BWT (backwards) is now : :
start at i = location of EOF in L[]

for N times :
{
find symbol L[i] in F[] ; this is i = LF[i]
then step to the prior symbol F -> L
output L[i]
}
that's it!  A full BWT inverse transform is then :
L[] = the BWT string, we get this from the decoder

count[i] = histogram of L[]
start[i] = prefix sum of count[]

make LF :

C[] = 0
for i to N
{
    s = L[i];
    LF[i] = start[s] + C[s];
    C[s]++;
}

read out :
i = index of EOF (transmitted)
// L[i] is EOF sym which we don't need to output
for N times
{
    i = LF[i];
    *ptr++ = L[i];
}
This produces the string backwards, which we usually handle by reversing in the encoder before doing the
BWT so that the decoder can just output forwards.
That's it!
I'm not going to talk about how the compressor transmits the BWT string L[] compactly.  See the original BW94 paper
or the bzip code for the classic MTF + RLE + switching Huffmans encoding.  See Fenwick for analysis of BWT
as a symbol ranker.  In the modern world most people do BWT encoding without MTF; see Maniscalco M99,
context induction, BCM and BBB.
I'm also not talking about the forward transform at all.  The forward transform also has interesting
efficiency issues, mainly also relating to cache misses for large buffers or to GPU implementations,
and there has been lots of good research on that; see the papers.  In this blog I will assume you don't care much about forward
transform speed, so I'll push all the slow operations to the encoder side to make the decoder as fast as
possible.
I will also just briefly mention that BWT of long string recurrances can be sped up with an LZP pre-pass.  We will
assume this has been done where appropriate so that there are no very long identical strings in our
source input (eg. perhaps suffixes are always unique after 16 symbols).
End of review and we'll dive into speeding up the i-BWT.
So the transform is delightfully simple, but it's slow.  Why?
(and by "slow" I mean *really* slow; specifically 200-400 cycles per iteration on my Intel machine "beasty")
The problem is that each instruction of the i-BWT intrinsically depends on the previous instruction (instrinsically meaning
can't be removed with code reorganization), so no instruction-level-parallelism (ILP) can be used.  On modern CPUs that
might be able to do 4 instructions per clock this is bad.  What's worse is that there is an intrinsic cache miss in the
lookup step of the i-BWT.
The problem is the index of the next symbol in the sequence is semi-random and goes all over the BWT buffer.  It cache misses
often (almost every single iteration).  Now you can obviously fix this by making the BWT chunk smaller, which is what the old bzip does.
If the chunk is small enough to fit in cache, no problem.  But that also kills compression and sort of ruins the whole point
of the BWT (if small chunk BWT compression is good enough for you, then you should just use an LZ like Kraken which better
fits that space-speed niche; high speed small cache is outside the operating range of where BWT makes sense vs alternatives).
In-cache BWT is not a Pareto optimal way to do a fast compressor; we are only interested in BWT in the high-compression domain.
So we want to use BWT chunk sizes that are bigger than the fast cache (16M chunks perhaps, which often fits in L3) and speed
things up.
The core of the i-BWT is just this :
for N times
{
    i = LF[i];
    *ptr++ = L[i];
}
The problem is the LF[i] are a near-random walk around the buffer.
They are in order of the sorted suffixes, which tend to be completely randomly
distributed in N, assuming the input array is not in some degenerate pre-sorted order.
You load at LF[i] and it cache misses, you can't do any more work, the loop completely stalls.  As soon
as the cache miss returns, you immediately do i = LF[i] and look up at LF[i] again and stall again.
Now one obvious thing we can do is to first combine the L[] and LF[] arrays into a single merged array, so that we get
exactly 1 cache missing load per iteration instead of 2.  But we still need fundamental improvements.
There are two big deficiencies we need to address :
1. Instruction sequence with sequential dependencies
2. Cache miss on looking up the next symbol
The most obvious approach to deal with these deficiencies is to use a technique we are now familiar with, which is
to do multiple streams at the same time.
Independent multiple streams allow you to keep more execution units busy, especially in a case like this where there
is a fundamental cache miss stall that you want to fill with useful CPU work during those cycles.
Say you have a single execution stream where every instruction is dependent on the last (c follows b follows a), 
only 1 can execute per cycle, and if one cache misses you get unused cycles with no work to do :
clock tick on the left
"1" is the independent stream number
a,b,c indicate a sequence of dependent instructions

0: 1a
1: 1b
2: 1c (cache miss)
3: .
4: .
5: .
6: .
7: 1d
If you run 4 streams of independent work, each stream dependent on the last instruction within its stream but no
cross-stream dependencies, now the CPU can execute 2 instructions per cycle (say), and fill in during the cache miss :
0: 1a + 2a
1: 1b + 2b
2: 1c + 2c (both cache miss)
3: 3a + 4a
4: 3b + 4b
5: 3c + 4c (both cache miss)
6: .
7: 1d + 2d
It's a bit like what hyper-threading does for you, but we get it just by running more independent execution sequences
on our single thread to give the out-of-order execution a bigger selection of work to find instructions to fill the gaps.
In our case with heavy cache missing dependent work, in the 1-stream case you are waiting on the latency of
each cache miss with the processor doing nothing, so you get a full stall all that time.  Going to more streams
at least lets us get multiple memory operations pending at once, rather than stall, wake up, stall again on one
load at a time.
In the case of i-BWT we can do this by taking the input data (before BWT) and think of it as T segments.  We don't cut
the string into pieces (remember chunking hurts compression and we don't want to do that), we still do the forward BWT
on the whole string.
Like :
"inputstring|"

in 2 segments :
input+string|

do the BWT on the whole string "inputstring|"

then find the locations of the EOF symbol | in L[]
and the + segment boundary, by finding where "string|" starts


g|inputstrin
ing|inputstr
inputstring| <- EOF key
ng|inputstri
nputstring|i
putstring|in
ring|inputst
string|input <- segment key
tring|inputs
tstring|inpu
utstring|inp
|inputstring
^          ^
F          L

EOF key = 2
segment key = 7
Then you would transmit the BWT string L[] and the EOF key (2) as usual, and also transmit the segment key (7).
The segment key lets you start the i-BWT core loop at that location and read out characters from there, in addition
to the stream from the EOF key.
In the i-BWT you can start output cursors for all T segments and you can read them out of the i-BWT simultaneously.
The i-BWT core loop just does "from this symbol, what's the next symbol?" so you can do T of those independently.
1->..+2->...|

cursor 1 starts at i=2 in L[]
cursor 2 starts at i=7 in L[]

decodes:
i....+s.....|
in...+st....|
etc..
input+string|
The N-stream decode is very simple, literally just doing the 1-stream process to N output pointers :
T segments
key[T] are the start indexes
i1,i2,etc. = key[]
ptr1 = start of output buffer
ptr2 = ptr1 + (N/T) , start of next segment, etc.

for N/T times
{
    i1 = LF[i1];
    *ptr1++ = L[i1];

    i2 = LF[i2];
    *ptr2++ = L[i2];
}
it just does the basic i-BWT loop on T segments in each iteration.  Crucially these are independent, so when one of them
stalls on a cache miss, the others can still do work.  If all of them were stalling on cache misses and the memory
system could service T cache line fetches simultaneously, we would be able to stall with all T requests in flight which
would give us factor of T speedup.  In practice it appears to be somewhat less than that.
You can also cut into segments like this for parallel decoding on multiple threads for very large blocks (without doing any
chunking, which sacrifices compression).  eg. you might find 16 segments to decode and give 4 segments each to 4 threads.
The threads have no cache contention because they are writing linearly to different output segments, and the shared memory
of the LF[] array is read-only in this loop.
Going to 4 streams provides around a 2.7X speedup, 8 streams gets us about 4X :
enwik7 :
ibwt_1x1 : seconds:0.7500 | cycles per: 299.330 | MB/s : 13.33
ibwt_1x4 : seconds:0.2801 | cycles per: 111.769 | MB/s : 35.71
ibwt_1x8 : seconds:0.1835 | cycles per: 73.218 | MB/s : 54.51
(see more speeds at end)
The next thing we can do is an idea from the paper "Cache Friendly Burrows-Wheeler Inversion".
We can make our basic i-BWT step output words or dwords instead of bytes.
This is a simple idea, but I think it's quite interesting *why* and *when* it works.
What we want to do is just do our core i-BWT to output words at a time instead of bytes, by outputting
a precomputed pair of one byte steps :
core i-BWT loop for words :

i = key (EOF location in L[])
for N/2 times
{
    *word_ptr++ = LL[i];
    i = LF2[i];
}
where LL = a word, two steps of L[] , and LF2[] = two steps of LF[],
that is LF2[i] = LF[LF[i]].
(reminder that in practice we put the LL[] and LF2[] into a single struct so that we get one cache miss
array lookup rather than two).
So to use that we just need to build the LL and LF2 arrays first.  To do that we just need to precompute
each pair of steps in the byte-at-a-time BWT :
prep for word i-BWT :

first build LF[] as usual

for i = 0 to N
{
    int i2 = LF[i];
    LL[i] = L[i] | (L[i2]<<8);
    LF2[i] = LF[i2];
}
At every index in L[] we precompute a two-character step by following LF[] once.
(side note : you could precompute a two-character step forward more simply; from L[i] the next character is just F[i],
which you could get from the cumulative probability table at i, but that would give you a step forward and what
we want is a step backward; L[i2] here is the character that precedes L[i]; it wouldn't help because we
need a lookup at i2 to make LF2[] anyway)
Now at first glance this might not seem helpful, what we have done is transform :
byte at-a-time BWT :

core i-BWT loop :

N times :
    i <- LF[i]
    output byte from i


word at-a-time BWT :

prep :

N times : 
    LF2[i] = LF[LF[i]]
    word = L[i] + L[LF[i]]

N/2 times :
    i <- LF2[i]
    output word from i
We are actually doing more work; we now do 3/2 N iterations instead of N iterations.
But it is in fact much faster.
Why?
The reason is that the N-step "prep" loop to build LF2 does not have the two big problems of the
core loop.  Remember the two big issues :
1. Instruction sequence with sequential dependencies
2. Cache miss on looking up the next symbol
these are what make the "core" i-BWT loop so slow.
First issue #1 : the "prep" loop naively allows for execution ahead, unlike the core loop.  The reason
is that it is just doing i++ to iterate the loop, rather than chasing i = LF[i] around a data-dependent
serpentine walk through the arrays.  This means that the processor can effectively unroll the loop to execute
ahead :
prep loop :

iter 1 :
    LF2[i] = LF[LF[i]]
    word = L[i] + L[LF[i]]
    i++;

iter 2 :
    LF2[i] = LF[LF[i]]
    word = L[i] + L[LF[i]]
    i++;
    
iter 1 and iter 2 can run at the same time because i++ can be precomputed.
If LF[LF[i]] stalls on a cache miss in iter 1, iter 2 can still proceed.

core loop :

iter 1 :
    i = LF[i]
    output byte/word from i

iter 2 :
    i = LF[i]
    output byte/word from i

iter 2 can't start until iter 1 is done because we don't know "i" until the
results of the lookup at LF[i] are done.
A modern processor will be able to execute ahead in the "prep" loop to fully saturate
execution, and we don't need to manually do the N-streams to get ILP because it just
naturally exists.
issue #2: cache misses.  The "prep" loop cache misses far less than the "core" loop.
Again this is not naively obvious.  The byte "core" loop does N lookups at LF[i].  The "prep" loop
also does N lookups at LF[i].  So they should cache miss the same, right?
Nope.  The difference is because the "core" loop is doing i = LF[i] which takes you to a semi-random
place each time, whereas the "prep" loop is doing i++ for subsequent lookups, and that means the
lookups are often to nearby locations that stay in cache.
core loop does :

    starting from i
    i1 = LF[i]
    lookup at i1
    i2 = LF[i1]
    lookup at i2
    i3 = LF[i2]
    lookup at i3

prep loop does :

    starting from i
    i1 = LF[i]
    lookup at i1
    i2 = LF[i+1]
    lookup at i2
    i3 = LF[i+2]
    lookup at i3
The indexes i1,i2,i3 in the core loop are semi-random, in the prep loop they are not.
To understand, let's remember what LF[] is.  It takes us from the symbol at L[i] to the location of
the preceding symbol in the BWT (we're outputting backwards).
So say you were currently at "ing|" (in "inputstring|"), it takes you to the location of "ring|" then
"tring|" ; those are i1,i2,i3 in the core loop.
In the "prep" loop you are taking the starting strings at i, i+1, i+2.  These are subsequent in sorted
order.  These might be something like :
"hella ..."
"hellish a.."
"hellish b.."
"hello a..."
"hello b..."
So the steps LF[] gives us to i1,i2,i3 will be to tack on the preceding character and look that up.
They might all be preceded by random characters, but in practice because these strings are similar
their preceding characters tend to be similar.  That might be :
" hella ..."
" hellish a.."
"shellish b.."
" hello a..."
"shello b..."
then you look up those locations in the suffix sort.  As long as you tacked on the same preceding
character, they will stay adjacent :
" hella ..." -> i =4000
" hellish a.." -> i = 4001
"shellish b.." -> i = 6078
" hello a..." -> i = 4002
"shello b..." -> i = 6079
The preceding character for the sorted suffixes is of course just the BWT string L[] itself.  The
portion here would be "  s s".
So as long as the BWT string has repeated characters, the indexes of the "prep" loop lookup will be
adjacent.  If they are adjacent indexes, they will not cache miss because we already loaded their
neighbor which brought in that cache line (load at i=4001 won't cache miss because we just did a load at i=4000).
Well, getting repeated characters in L[] is exactly what the BWT gives us!  If we think of it in terms of post-MTF
BWT strings, a 0 will be a load from the most likely location, 1 will be the second most likely, etc. so
there will tend to be a few cache lines that we already have that provide most of our loads for the "prep"
loop.  Only rarely do you get unexpected characters that cause cache misses.
Note that this only works on *compressible* data where the BWT is giving the coherence we want.  On random
data that doesn't compress this breaks down.  (though even in that case, there are still at most 256 hot cache
lines = 16 KB that we need to read from, so it's still better than the "core" loop, and we still have property
#1 that each iteration is independent).
Actual load locations so you can see how this works in practice :
LF[i] = 8853
LF[i] = 8854
LF[i] = 8855
LF[i] = 8856
LF[i] = 10553
LF[i] = 8857
LF[i] = 10554
LF[i] = 48
LF[i] = 49
LF[i] = 50
LF[i] = 10555
LF[i] = 10556
LF[i] = 51
LF[i] = 52
LF[i] = 5070
LF[i] = 10557
LF[i] = 2477
LF[i] = 53
LF[i] = 54
Where you have 10553,10554,10555 that means the same character was preceding those suffixes, so they lookup
in adjacent places.
You can of course take this idea for word output and repeat it again to get dword (u32) output per iteration.
In practice what I see is that dword output is only faster for compressible data where the cache coherence
property above works well.  On random input dword output gets a lot slower than word-at-a-time.  Because of
this I think word output is best if you only choose one i-BWT, 
but you can do even better by adaptively choosing the output algorithm by the compression ratio.
The dword (4x) variant does an N-loop to build LF2 which is quite coherent, the next N-loop to build LF4 is
slightly less coherent unless the data is compressible (we're relying on two-symbols-away correlation now
instead of neighbor correlation, which is less strong), then it does N/4 of the "core" loop which is still quite
cache missy.  So the net is :
!
1x byte loop : N steps of "core" , cache mising
2x word loop : N steps of LF2 + (N/2) steps of core
4x word loop : N steps of LF2 + N steps of LF4 + (N/4) steps of core
The authors of "Cache Friendly Burrows-Wheeler Inversion" have another method that accelerates long repeated
substrings called "precopy".  I think that a pre-pass with an LZP transform is probably a faster to way to accomplish the same
thing on data where that is helpful.  "precopy" also makes N-stream interleaving much more complex.  I have not
tested it.
Speeds measured on my Intel Core i7 3770 (locked at 3403 MHz) (Ivy Bridge)
ibwt 1x1 = classic byte at a time inverse BWT
ibwt 1x4 = byte x 4 streams
ibwt 2x4 = word x 4 streams
ibwt 4x4 = dword x 4 streams
ibwt 1x8 = byte x 8 streams
ibwt 2x8 = word x 8 streams
ibwt 4x8 = dword x 8 streams
cycles per byte for the ibwt :
name
1x1
1x4
2x4
4x4
dickens
350.6
123.7
70.0
47.9
enwik7
301.2
116.0
66.8
47.0
webster
376.9
139.0
78.5
51.2
lzt99
211.3
114.6
65.1
61.4
rand_16M
401.6
130.6
80.4
297.3
name
1x1
1x8
2x8
4x8
dickens
337.0
79.8
46.8
35.8
enwik7
299.1
73.2
46.0
36.1
webster
376.5
98.0
57.5
40.3
lzt99
208.6
77.9
48.1
53.7
rand_16M
401.3
84.1
55.0
273.4
We've improved the i-BWT speed from around 300 cycles/byte to 50 cycles/byte.  That's still extremely slow.  It's around the speed of Oodle LZNA (30 cycles/bytes) or 7z LZMA (70 cycles/byte).
It's an order of magnitude slower than Oodle Leviathan (5 cycles/byte).  But in some cases, such as text, BWT on large blocks gets a lot more compression than those, so it
could be interesting on the right data types if you care about the very high compression domain.
All speeds single threaded.
The i-BWT on a small buffer that stays in cache is around 10 cycles/byte (and could probably be faster; we haven't looked
at all at micro-optimizing the actual instructions here, since if we're stalling on cache misses they don't matter),
so at 50 cycles/byte we're still spending 40 cycles/byte stalled on 
the memory subsystem in our best algorithm, which is not great.
ADD : with MEM_LARGE_PAGES :
name
1x1
1x8
2x8
4x8
dickens
301.3
52.4
33.9
27.7
enwik7
265.8
50.5
33.1
28.2
webster
319.6
54.5
34.8
29.0
lzt99
177.5
50.6
32.5
35.6
rand_16M
336.6
53.5
41.4
154.1
Without large pages, the bottleneck appears to be in TLB/page mapping.  With large pages it seems to be limited by the rate that cache missing reads can be retired (assuming the latency of that is fixed, this is the number of different cache lines that can have in-flight reads simultaneously).  eg. if latency is 300 cycles, with 10 simultaneous reads we could get to 30 cycles/byte.
Downloads :
fast_ibwt_test.cpp
fast_ibwt_test exe (Win x64)
The source code is public domain.
The ibwt routines are standard C.  The test driver uses
cblib
