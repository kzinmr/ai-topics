---
title: "Integer overflow checking cost"
url: "https://danluu.com/integer-overflow/"
fetched_at: 2026-05-05T07:01:33.567428+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Integer overflow checking cost

Source: https://danluu.com/integer-overflow/

How much overhead should we expect from enabling integer overflow checks? Using a compiler flag or built-in intrinsics, we should be able to do the check with a conditional branch that branches based on the overflow flag that
add
and
sub
set. Code that looks like
add     %esi, %edi
should turn into something like
add     %esi, %edi
jo      <handle_overflow>
Assuming that branch is always correctly predicted (which should be the case for most code), the costs of the branch are the cost of executing that correctly predicted not-taken branch, the pollution the branch causes in the branch history table, and the cost of decoding the branch (on x86,
jo
and
jno
don't fuse with
add
or
sub
, which means that on the fast path, the branch will take up one of the 4 opcodes that can come from the decoded instruction cache per cycle). That's probably less than a 2x penalty per
add
or
sub
on front-end limited in the worst case (which might happen in a tightly optimized loop, but should be rare in general), plus some nebulous penalty from branch history pollution which is really difficult to measure in microbenchmarks. Overall, we can use 2x as a pessimistic guess for the total penalty.
2x sounds like a lot, but how much time do applications spend adding and subtracting? If we look at the most commonly used benchmark of “workstation” integer workloads,
SPECint
, the composition is maybe 40% load/store ops, 10% branches, and 50% other operations. Of the 50% “other” operations, maybe 30% of those are integer add/sub ops. If we guesstimate that load/store ops are 10x as expensive as add/sub ops, and other ops are as expensive as add/sub, a 2x penalty on add/sub should result in a
(40*10+10+50 + 12) / (40*10+10+50) = 3%
penalty. That the penalty for a branch is 2x, that add/sub ops are only 10x faster than load/store ops, and that add/sub ops aren't faster than other "other" ops are all pessimistic assumptions, so this estimate should be on the high end for most workloads.
John Regehr, who's done serious analysis on integer overflow checks estimates that the penalty should be
about 5%
, which is in the same ballpark as our napkin sketch estimate.
A spec license costs $800, so let's benchmark bzip2 (which is a component of SPECint) instead of paying $800 for SPECint. Compiling bzip2 with
clang -O3
vs.
clang -O3 -fsanitize=signed-integer-overflow,unsigned-integer-overflow
(which prints out a warning on overflow) vs.
-fsanitize-undefined-trap-on-error
with undefined overflow checks (which causes a crash on an undefined overflow), we get the following results on compressing and decompressing 1GB of code and binaries that happened to be lying around on my machine.
options
zip (s)
unzip (s)
zip (ratio)
unzip (ratio)
normal
93
45
1.0
1.0
fsan
119
49
1.28
1.09
fsan ud
94
45
1.01
1.00
In the table, ratio is the relative ratio of the run times, not the compression ratio. The difference between
fsan ud, unzip
and
normal, unzip
isn't actually 0, but it rounds to 0 if we measure in whole seconds. If we enable good error messages, decompression doesn't slow down all that much (45s v. 49s), but compression is a lot slower (93s v. 119s). The penalty for integer overflow checking is 28% for compression and 9% decompression if we print out nice diagnostics, but almost nothing if we don't. How is that possible? Bzip2 normally has a couple of unsigned integer overflows. If I patch the code to remove those so that the diagnostic printing code path is never executed it still causes a large performance hit.
Let's check out the penalty when we just do some adds with something like
for (int i = 0; i < n; ++i) {
  sum += a[i];
}
On my machine (a 3.4 GHz Sandy Bridge), this turns out to be about 6x slower with
-fsanitize=signed-integer-overflow,unsigned-integer-overflow
. Looking at the disassembly, the normal version uses SSE adds, whereas the fsanitize version uses normal adds. Ok, 6x sounds plausible for unchecked SSE adds v. checked adds.
But if I try different permutations of the same loop that don't allow the the compiler to emit SSE instructions for the unchecked version, I still get a 4x-6x performance penalty for versions compiled with fsanitize. Since there are a lot of different optimizations in play, including loop unrolling, let's take a look at a simple function that does a single add to get a better idea of what's going on.
Here's the disassembly for a function that adds two ints, first compiled with
-O3
and then compiled with
-O3 -fsanitize=signed-integer-overflow,unsigned-integer-overflow
.
0000000000400530 <single_add>:
  400530:       01 f7                   add    %esi,%edi
  400532:       89 f8                   mov    %edi,%eax
  400534:       c3                      retq
The compiler does a reasonable job on the
-O3
version. Per the standard AMD64 calling convention, the arguments are passed in via the
esi
and
edi
registers, and passed out via the
eax
register. There's some overhead over an inlined
add
instruction because we have to move the result to
eax
and then return from the function call, but considering that it's a function call, it's a totally reasonable implementation.
000000000041df90 <single_add>:
  41df90:       53                      push   %rbx
  41df91:       89 fb                   mov    %edi,%ebx
  41df93:       01 f3                   add    %esi,%ebx
  41df95:       70 04                   jo     41df9b <single_add+0xb>
  41df97:       89 d8                   mov    %ebx,%eax
  41df99:       5b                      pop    %rbx
  41df9a:       c3                      retq
  41df9b:       89 f8                   mov    %edi,%eax
  41df9d:       89 f1                   mov    %esi,%ecx
  41df9f:       bf a0 89 62 00          mov    $0x6289a0,%edi
  41dfa4:       48 89 c6                mov    %rax,%rsi
  41dfa7:       48 89 ca                mov    %rcx,%rdx
  41dfaa:       e8 91 13 00 00          callq  41f340
<__ubsan_handle_add_overflow>
  41dfaf:       eb e6                   jmp    41df97 <single_add+0x7>
The compiler does not do a reasonable job on the
-O3 -fsanitize=signed-integer-overflow,unsigned-integer-overflow
version. Optimization wizard Nathan Kurz, had this to say about clang's output:
That's awful (although not atypical) compiler generated code. For some reason the compiler decided that it wanted to use %ebx as the destination of the add. Once it did this, it has to do the rest. The question would by why it didn't use a scratch register, why it felt it needed to do the move at all, and what can be done to prevent it from doing so in the future. As you probably know, %ebx is a 'callee save' register, meaning that it must have the same value when the function returns --- thus the push and pop. Had the compiler just done the add without the additional mov, leaving the input in %edi/%esi as it was passed (and as done in the non-checked version), this wouldn't be necessary. I'd guess that it's a residue of some earlier optimization pass, but somehow the ghost of %ebx remained.
However, adding
-fsanitize-undefined-trap-on-error
changes this to
0000000000400530 <single_add>:
  400530:       01 f7                   add    %esi,%edi
  400532:       70 03                   jo     400537 <single_add+0x7>
  400534:       89 f8                   mov    %edi,%eax
  400536:       c3                      retq
  400537:       0f 0b                   ud2
Although this is a tiny, contrived, example, we can see a variety of mis-optimizations in other code compiled with options that allow fsanitize to print out diagnostics.
While a better C compiler could do better, in theory, gcc 4.82 doesn't do better than clang 3.4 here. For one thing, gcc's
-ftrapv
only checks signed overflow. Worse yet, it doesn't work,
and this bug on ftrapv has been open since 2008
. Despite doing fewer checks and not doing them correctly, gcc's
-ftrapv
slows things down about as much as clang's
-fsanitize=signed-integer-overflow,unsigned-integer-overflow
on bzip2, and substantially more than
-fsanitize=signed-integer-overflow
.
Summing up, integer overflow checks ought to cost a few percent on typical integer-heavy workloads, and they do, as long as you don't want nice error messages. The current mechanism that produces nice error messages somehow causes optimizations to get screwed up in a lot of cases.
Update
On clang 3.8.0 and after, and gcc 5 and after, register allocation seems to work as expected (although you may need to pass
-fno-sanitize-recover
. I haven't gone back and re-run my benchmarks across different versions of clang and gcc, but I'd like to do that when I get some time.
CPU internals series
Thanks to Nathan Kurz for comments on this topic, including, but not limited to, the quote that's attributed to him, and to Stan Schwertly, Nick Bergson-Shilcock, Scott Feeney, Marek Majkowski, Adrian and Juan Carlos Borras for typo corrections and suggestions for clarification. Also, huge thanks to Richard Smith, who pointed out the
-fsanitize-undefined-trap-on-error
option to me. This post was updated with results for that option after Richard's comment. Also, thanks to Filipe Cabecinhas for noticing that clang fixed this behavior in clang 3.8 (released approximately 1.5 years after this post).
John Regehr has some
more comments here
on why clang's implementation of integer overflow checking isn't fast (yet).
