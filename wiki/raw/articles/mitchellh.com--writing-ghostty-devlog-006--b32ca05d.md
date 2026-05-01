---
title: "Ghostty Devlog 006"
url: "https://mitchellh.com/writing/ghostty-devlog-006"
fetched_at: 2026-05-01T07:02:03.345926+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Ghostty Devlog 006

Source: https://mitchellh.com/writing/ghostty-devlog-006

Hello! Welcome to the official devlog for
Ghostty
👻!
This devlog is going to be focused on
speed
🚀. I'm going to show various
ways we've made Ghostty
really, really, fast
in recent weeks.
There are many ways to measure the speed of a terminal emulator.
Perhaps in another blog post I'll define each of the ways, but today
I will simply state that the performance work showcased in this devlog will
all revolve around
IO throughput
.
IO throughput is the speed that the program running within the terminal
emulator (the shell, neovim, tmux, cat, etc.) can pump bytes to the terminal
emulator and have them processed. This particular metric has a very real
world impact, from tailing very loud log output to accidentally dumping a
large file to the terminal (we've all been there).
Improving Plain Text Throughput with SIMD (#1472)
A program uses a single stream (a "pty") to communicate to the terminal
emulator. This stream can contain either
plain text
or
control characters
.
Plain text prints directly to the terminal and is sent as-is. For example,
to write "Hello, World!" to the terminal, the program writes
Hello World!
UTF-8 encoded
1
to the pty.
Control characters are used to do things such as set style attributes
(foreground color, underline, bold, etc.), move the cursor, delete lines,
change the keyboard protocol, etc. Control characters have various formats
but one thing almost all of them
2
have in common is they start with
the escape character (hex
0x1B
).
A naive, but typical approach is to read the bytes in a for loop:
const
bytes
=
read
()
;
for
(byte in bytes) {
if
(byte
==
0x1B
) {
// Process control sequence
}
else
{
// Process plain text
}
}
This looks at one byte at a time. But computers since the late 90s have
been able to perform operations on multiple bytes at a time using
SIMD instructions
("Single Instruction Multiple Data"). According to
Valve's latest
Steam Hardware Survey
,
over 99% of active computers support the ability to look at 16 to 32
bytes
in one CPU instruction
.
We often rely on compilers to optimize our code for us so we don't have
to think about the minutia of individual CPU instructions. Unfortunately,
compilers are notoriously bad at
autovectorization
and with the exception of relatively trivial loops, compilers rarely autovectorize
effectively. SIMD is a rare scenario where hand-writing assembly (or near
it) often results in significantly better performance over a state of the art
optimizing compiler.
The SIMD approach to finding control sequences above looks like this:
const
bytes
=
read
()
;
for
(chunk of
16
bytes in bytes) {
if
(chunk contains
0x1B
) {
// Control sequence in here
}
else
{
// Chunk is entirely plain text
}
}
Assume in the above two examples that the comparison operation takes
exactly the same amount of time. The SIMD example would process the bytes
16x faster. Reality is not quite so simple, but you can get staggering
speedups through SIMD.
To further complicate things, SIMD instruction sets vary by CPU generation.
If you're distributing a binary form of your program and want to take advantage
of the best features available, you must write a variation for each SIMD
instruction set, compile each form, and choose the correct version at runtime
using CPU feature detection (i.e. using the
cpuid
instruction on x86
).
For example, the code above says "chunk of 16 bytes." Well, depending on
the hardware, that might be 16 bytes (aarch64 neon instruction set such
as on Apple Silicon), 32 bytes for AVX2, 64 bytes for AVX512, etc. And its not
just the size that varies, the literal CPU instructions (binary code) varies.
Therefore, you must write or compile the code multiple times.
Ghostty now uses SIMD to execute roughly the second code sample above.
Additionally, we use SIMD to also decode UTF-8
3
multiple bytes at a time.
On Apple Silicon (M3 Max), Ghostty now processes ASCII input 7.3x faster:
Benchmark 1: memcpy
  Time (mean ± σ):      52.7 ms ±   0.7 ms    [User: 41.6 ms, System: 47.6 ms]
  Range (min … max):    50.7 ms …  54.6 ms    53 runs

Benchmark 2: scalar
  Time (mean ± σ):     382.3 ms ±   4.0 ms    [User: 408.6 ms, System: 39.1 ms]
  Range (min … max):   376.1 ms … 388.7 ms    10 runs

Benchmark 3: simd (aarch64 neon)
  Time (mean ± σ):      52.3 ms ±   0.6 ms    [User: 53.8 ms, System: 47.2 ms]
  Range (min … max):    51.3 ms …  54.2 ms    54 runs

Summary
  simd ran
    1.01 ± 0.02 times faster than memcpy
    7.32 ± 0.11 times faster than scalar
And Ghostty now reads
and decodes UTF-8 to UTF-32
16.6x faster:
Benchmark 1: memcpy
  Time (mean ± σ):      22.3 ms ±   0.8 ms    [User: 11.5 ms, System: 31.4 ms]
  Range (min … max):    20.2 ms …  25.5 ms    115 runs

Benchmark 2: scalar
  Time (mean ± σ):     344.1 ms ±   1.2 ms    [User: 344.4 ms, System: 38.3 ms]
  Range (min … max):   341.9 ms … 347.0 ms    10 runs

Benchmark 3: simd (aarch64 neon)
  Time (mean ± σ):      20.7 ms ±   0.8 ms    [User: 18.9 ms, System: 28.0 ms]
  Range (min … max):    19.1 ms …  24.4 ms    127 runs

Summary
  simd ran
    1.07 ± 0.06 times faster than memcpy
   16.60 ± 0.61 times faster than scalar
On
x86_64
machines with AVX2 available, the results are even more
dramatic, but I don't have ready access to an
x86_64
machine to
reproduce the exact output I have above, only anecdotes shared by the
testing community.
The
memcpy
benchmark is
just reading the bytes into a pre-allocated
buffer
. i.e. its basically
for { bytes = read() }
(with some annotations
to ensure the compiler doesn't optimize this away). This means that in both
cases above, our SIMD pipeline is reading
and parsing
(in the case of UTF-8)
text at roughly the same speed as simply reading the data into memory.
In real world
wall time
,
these optimizations made
cat
-ing a large ASCII file 2x faster, and
cat
-ing
a large Japanese file 20% faster. The speedups are dramatically slower
than the benchmarks above due to
other bottlenecks
.
Good news: we found and optimized those too, keep reading!
Precomputed Lookup Tables for Codepoint Width (#1486)
A terminal is made up of a grid of monospace cells. When you write a character
such as
A
or
橋
to the terminal, it must determine
how many cells
the character takes up. This process is surprisingly complex! See
this excellent blog post by Jeff Quast
for details.
Through profiling efforts, we determined that
30% of the time taken for
every printed character
was spent calculating codepoint width. So we set out
to optimize this, and optimize this we did.
Thanks to the direction of a very helpful community member, I precalculated
the codepoint width for
every single Unicode codepoint value
and
used a trie-like
3-stage lookup table
to quickly look up codepoint width without taking up too much memory and
remaining relatively cache friendly.
By building our own custom lookup table, we could account for special
situations unique to a terminal and make it
even faster
. For example,
we know control characters are impossible because we filter them before
this point, and we know terminals can handle at most double-width characters
so we can clamp triple-width characters (the
3-em dash
)
to double-width without an additional conditional at runtime. Every CPU cycle
counts.
The results speak for themselves. Once again, on an Apple Silicon M3 Max,
ASCII throughput was 2.8x faster:
Benchmark 1: noop
  Time (mean ± σ):     113.2 ms ±   1.3 ms    [User: 88.2 ms, System: 23.5 ms]
  Range (min … max):   111.8 ms … 116.5 ms    25 runs

Benchmark 2: wcwidth
  Time (mean ± σ):     358.2 ms ±   2.5 ms    [User: 331.1 ms, System: 24.7 ms]
  Range (min … max):   355.2 ms … 362.3 ms    10 runs

Benchmark 3: ziglyph
  Time (mean ± σ):     549.1 ms ±   2.2 ms    [User: 505.1 ms, System: 31.8 ms]
  Range (min … max):   543.9 ms … 564.2 ms    10 runs

Benchmark 4: table
  Time (mean ± σ):     194.0 ms ±   1.4 ms    [User: 168.9 ms, System: 23.8 ms]
  Range (min … max):   192.6 ms … 197.5 ms    15 runs
And uniformly distributed random UTF-8 throughput was about 5x faster:
Benchmark 1: noop
  Time (mean ± σ):     127.9 ms ±   1.5 ms    [User: 115.8 ms, System: 10.3 ms]
  Range (min … max):   126.5 ms … 131.4 ms    23 runs

Benchmark 2: wcwidth
  Time (mean ± σ):     136.5 ms ±   1.9 ms    [User: 124.3 ms, System: 10.4 ms]
  Range (min … max):   134.9 ms … 143.0 ms    21 runs

Benchmark 3: ziglyph
  Time (mean ± σ):     620.5 ms ±   1.3 ms    [User: 610.5 ms, System: 9.8 ms]
  Range (min … max):   619.0 ms … 602.6 ms    10 runs

Benchmark 4: table
  Time (mean ± σ):     122.4 ms ±   2.4 ms    [User: 110.5 ms, System: 10.4 ms]
  Range (min … max):   120.6 ms … 132.4 ms    23 runs
In the benchmarks above
ziglyph
is the old API we used for codepoint
width calculation. The
wcwidth
benchmark is the libc API for codepoint
width
but it gives incorrect
results (see
my entire post on the topic
).
In both ASCII and random UTF-8 scenarios, we now get
correct results
faster than the simple broken libc API
.
4
In real world wall time, this optimization improved the time it takes to
cat
ASCII by a further 2.5x and Japanese by a further 1.5x. In total with the previously
discussed optimization, real world plain text throughput was anywhere from
2x to 5x faster depending on the complexity of the UTF-8.
Optimized Grapheme Break Detection (#1494)
Ghostty is a
grapheme-aware terminal emulator
.
For every printed codepoint, Ghostty must determine if the codepoint is
part of a new grapheme or the previous grapheme. This process is known
as detecting
grapheme breaks
(the point at which a grapheme
breaks
into
another grapheme).
For example "AB", codepoint U+42
B
breaks
when next to codepoint
U+41
A
, forming two graphemes. However, "🧑‍🌾" has three codepoints
U+1F9D1 🧑, U+200D, and U+1F33E 🌾. The grapheme
does not break
until
after U+1F33E 🌾.
Grapheme break detection is typically a
non-trivial algorithm
.
However, I realized if you add some additional preconditions a terminal
can guarantee (such as zero control characters or ASCII), you can eliminate
enough conditionals such that computing a lookup table of
every possible
codepoint pair plus state
takes up less than 1KB of memory.
So we did that and made our grapheme break detection almost 8x faster
while being only 27% slower than
doing nothing at all
(reading the bytes):
Benchmark 1: noop
  Time (mean ± σ):      51.2 ms ±   1.2 ms    [User: 43.6 ms, System: 6.7 ms]
  Range (min … max):    49.7 ms …  57.7 ms    55 runs

Benchmark 2: ziglyph
  Time (mean ± σ):     519.7 ms ±   0.8 ms    [User: 508.2 ms, System: 8.9 ms]
  Range (min … max):   518.4 ms … 520.7 ms    10 runs

Benchmark 3: table
  Time (mean ± σ):      65.3 ms ±   1.2 ms    [User: 57.2 ms, System: 6.9 ms]
  Range (min … max):    63.4 ms …  71.1 ms    44 runs

Summary
  'noop' ran
    1.27 ± 0.04 times faster than 'table'
   10.14 ± 0.25 times faster than 'ziglyph'
This, combined with the previously mentioned optimizations, resulted
in some really impressive real world results.
Note below that only the
bolded
terminals do grapheme clustering.
The non-bolded terminals
don't perform grapheme break detection at all
,
so in almost every case Ghostty is faster at reading plain text while doing
grapheme break detection over terminals that read plain text while doing
nothing. The
Ghostty (legacy wcswidth)
entry is Ghostty's speed without
grapheme clustering enabled.
Terminal
time cat japanese-bible.txt
(5.4MB)
Ghostty (old)
189ms
Ghostty (new)
73ms
Ghostty (legacy wcswidth)
61ms
Alacritty 0.13.1
66ms (see note)
iTerm2 3.4.23
470ms
Kitty (new unreleased SIMD branch
5
)
103ms
Kitty 0.32.1
392ms
Terminal.app macOS 14.3
124ms
WezTerm 20240203-110809-5046fc22
140ms
Note for the above, I
cat
the file 10 times and took the average. There were
never any outliers; the range of every measurement was always within 2% of the
average.
The test above is real world, but also very contrived. I
am not
trying
to make any blanket statements that Ghostty is faster in every scenario
over every other terminal or anything of the sort. My intentions sharing
the above data are to point out the real world effect of the optimizations
discussed in this devlog.
The video below shows the difference in speed reading a large Japanese
text file between one of the most popular macOS terminals and Ghostty.
This situation isn't purely hypothetical: it'd apply if you ever were
tailing a loud set of logs, accidentally open a large file, etc.
Note the video appears to show a brief hiccup around the 8 second mark.
This appears to be an artifact of my screen recording software. In real
life, I didn't see any pause at all.
CSI Sequence Fast-path Optimizations (#1485)
All of the optimizations previously mentioned were focused on
plain text
output. They don't help much with
control sequence
heavy programs such
as Neovim or tmux. To address this,
a contributor
implemented a
CSI sequence
fast-path
parser.
CSI sequences are some of the most common control sequences used by
programs such as Neovim. They are used to change text style, apply
colors, jump the cursor around, scroll the screen, etc.
The fast-path was implemented in scalar (non-SIMD) instructions and
works by primarily avoiding the VT parsing state machine and optimistically
expecting valid CSI syntax (i.e. decimal-encoded numbers, semicolons,
and single ASCII terminators).
We captured the pty stream from doing some work in Neovim and replayed it as
fast as we could, and verified in the real world that the CSI fast-path
improved throughput anywhere from 1.4 to 2x (depending on the workload
under test). The popular
DOOM fire
stress test -- a CSI-heavy test -- increased in FPS by 1.44x.
I'll repeat that this particular contribution was completely from a
separate contributor (
@Qwerasd
) within the
closed beta. They were also very helpful in providing feedback and direction
for the other optimizations covered in this post. Thank you so much!
Fin
As stated in the introduction, this devlog focused on the work myself and
the community have been doing to make Ghostty
fast
. In this case, all
of that work revolved specifically around making IO fast. There many
other performance metrics that I also plan to improve and write about
(input latency, startup time, framerate, memory usage, etc.).
We're not done improving Ghostty's IO speed. We have identified more bottlenecks
and solutions being researched. I hope to come back in a future devlog and
update you all on that progress.
In addition to
speed
, Ghostty has had many more improvements since the
last devlog. I plan to focus more on some of those in the next devlog.
Someone
recently discovered the failure recovery work
I've also been doing, and I hope to write more about that later.
Finally, our beta as grown from around 350 people at the time of the
last devlog to over 650 people at the time of this devlog. I want to thank
the entire community for helping report issues, contribute code, and being
kind and helpful to everyone.
If you want to keep up to date, follow me on Twitter or Mastodon
(links in footer). This blog also has an
RSS feed
.
Boo. 👻
