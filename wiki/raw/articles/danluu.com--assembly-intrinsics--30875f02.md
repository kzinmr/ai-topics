---
title: "Assembly v. intrinsics"
url: "https://danluu.com/assembly-intrinsics/"
fetched_at: 2026-05-05T07:01:34.805630+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Assembly v. intrinsics

Source: https://danluu.com/assembly-intrinsics/

Every once in a while, I hear how intrinsics have improved enough that it's safe to use them for high performance code. That would be nice. The promise of intrinsics is that you can write optimized code by calling out to functions (intrinsics) that correspond to particular assembly instructions. Since intrinsics act like normal functions, they can be cross platform. And since your compiler has access to more computational power than your brain, as well as a detailed model of every CPU, the compiler should be able to do a better job of micro-optimizations. Despite decade old claims that intrinsics can make your life easier, it never seems to work out.
The last time I tried intrinsics was around 2007; for more on why they were hopeless then (
see this exploration by the author of VirtualDub
). I gave them another shot recently, and while they've improved, they're still not worth the effort. The problem is that intrinsics are so unreliable that you have to manually check the result on every platform and every compiler you expect your code to be run on, and then tweak the intrinsics until you get a reasonable result. That's more work than just writing the assembly by hand. If you don't check the results by hand, it's easy to get bad results.
For example, as of this writing, the first two Google hits for
popcnt benchmark
(and 2 out of the top 3 bing hits) claim that Intel's hardware
popcnt
instruction is slower than a software implementation that counts the number of bits set in a buffer, via a table lookup using the
SSSE3
pshufb
instruction. This turns out to be untrue, but it must not be obvious, or this claim wouldn't be so persistent. Let's see why someone might have come to the conclusion that the
popcnt
instruction is slow if they coded up a solution using intrinsics.
One of the top search hits has sample code and benchmarks for both native
popcnt
as well as the software version using
pshufb
.
Their code
requires MSVC, which I don't have access to, but their first
popcnt
implementation just calls the
popcnt
intrinsic in a loop, which is fairly easy to reproduce in a form that gcc and clang will accept. Timing it is also pretty simple, since we're just timing a function (that happens to count the number of bits set in some fixed sized buffer).
uint32_t builtin_popcnt(const uint64_t* buf, int len) {
  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    cnt += __builtin_popcountll(buf[i]);
  }
  return cnt;
}
This is slightly different from the code I linked to above, since they use the dword (32-bit) version of
popcnt
, and we're using the qword (64-bit) version. Since our version gets twice as much done per loop iteration, I'd expect our version to be faster than their version.
Running
clang -O3 -mpopcnt -funroll-loops
produces a binary that we can examine. On macs, we can use
otool -tv
to get the disassembly. On linux, there's
objdump -d
.
_builtin_popcnt:
; address                        instruction
0000000100000b30        pushq   %rbp
0000000100000b31        movq    %rsp, %rbp
0000000100000b34        movq    %rdi, -0x8(%rbp)
0000000100000b38        movl    %esi, -0xc(%rbp)
0000000100000b3b        movl    $0x0, -0x10(%rbp)
0000000100000b42        movl    $0x0, -0x14(%rbp)
0000000100000b49        movl    -0x14(%rbp), %eax
0000000100000b4c        cmpl    -0xc(%rbp), %eax
0000000100000b4f        jge     0x100000bd4
0000000100000b55        movslq  -0x14(%rbp), %rax
0000000100000b59        movq    -0x8(%rbp), %rcx
0000000100000b5d        movq    (%rcx,%rax,8), %rax
0000000100000b61        movq    %rax, %rcx
0000000100000b64        shrq    %rcx
0000000100000b67        movabsq $0x5555555555555555, %rdx
0000000100000b71        andq    %rdx, %rcx
0000000100000b74        subq    %rcx, %rax
0000000100000b77        movabsq $0x3333333333333333, %rcx
0000000100000b81        movq    %rax, %rdx
0000000100000b84        andq    %rcx, %rdx
0000000100000b87        shrq    $0x2, %rax
0000000100000b8b        andq    %rcx, %rax
0000000100000b8e        addq    %rax, %rdx
0000000100000b91        movq    %rdx, %rax
0000000100000b94        shrq    $0x4, %rax
0000000100000b98        addq    %rax, %rdx
0000000100000b9b        movabsq $0xf0f0f0f0f0f0f0f, %rax
0000000100000ba5        andq    %rax, %rdx
0000000100000ba8        movabsq $0x101010101010101, %rax
0000000100000bb2        imulq   %rax, %rdx
0000000100000bb6        shrq    $0x38, %rdx
0000000100000bba        movl    %edx, %esi
0000000100000bbc        movl    -0x10(%rbp), %edi
0000000100000bbf        addl    %esi, %edi
0000000100000bc1        movl    %edi, -0x10(%rbp)
0000000100000bc4        movl    -0x14(%rbp), %eax
0000000100000bc7        addl    $0x1, %eax
0000000100000bcc        movl    %eax, -0x14(%rbp)
0000000100000bcf        jmpq    0x100000b49
0000000100000bd4        movl    -0x10(%rbp), %eax
0000000100000bd7        popq    %rbp
0000000100000bd8        ret
Well, that's interesting. Clang seems to be calculating things manually rather than using
popcnt
. It seems to be using
the approach described here
, which is something like
x = x - ((x >> 0x1) & 0x5555555555555555);
x = (x & 0x3333333333333333) + ((x >> 0x2) & 0x3333333333333333);
x = (x + (x >> 0x4)) & 0xF0F0F0F0F0F0F0F;
ans = (x * 0x101010101010101) >> 0x38;
That's not bad for a simple implementation that doesn't rely on any kind of specialized hardware, but that's going to take a lot longer than a single
popcnt
instruction.
I've got a pretty old version of clang (3.0), so let me try this again after upgrading to 3.4, in case they added hardware
popcnt
support “recently”.
0000000100001340        pushq   %rbp         ; save frame pointer
0000000100001341        movq    %rsp, %rbp   ; new frame pointer
0000000100001344        xorl    %ecx, %ecx   ; cnt = 0
0000000100001346        testl   %esi, %esi
0000000100001348        jle     0x100001363
000000010000134a        nopw    (%rax,%rax)
0000000100001350        popcntq (%rdi), %rax ; “eax” = popcnt[rdi]
0000000100001355        addl    %ecx, %eax   ; eax += cnt
0000000100001357        addq    $0x8, %rdi   ; increment address by 64-bits (8 bytes)
000000010000135b        decl    %esi         ; decrement loop counter; sets flags
000000010000135d        movl    %eax, %ecx   ;  cnt = eax; does not set flags
000000010000135f        jne     0x100001350  ; examine flags. if esi != 0, goto popcnt
0000000100001361        jmp     0x100001365  ; goto “restore frame pointer”
0000000100001363        movl    %ecx, %eax
0000000100001365        popq    %rbp         ; restore frame pointer
0000000100001366        ret
That's better! We get a hardware
popcnt
! Let's compare this to the SSSE3
pshufb
implementation
presented here
as the fastest way to do a popcnt. We'll use a table like the one in the link to show speed, except that we're going to show a rate, instead of the raw cycle count, so that the relative speed between different sizes is clear. The rate is GB/s, i.e., how many gigs of buffer we can process per second. We give the function data in chunks (varying from 1kb to 16Mb); each column is the rate for a different chunk-size. If we look at how fast each algorithm is for various buffer sizes, we get the following.
Algorithm
1k
4k
16k
65k
256k
1M
4M
16M
Intrinsic
6.9
7.3
7.4
7.5
7.5
7.5
7.5
7.5
PSHUFB
11.5
13.0
13.3
13.4
13.1
13.4
13.0
12.6
That's not so great. Relative to the the benchmark linked above, we're doing better because we're using 64-bit
popcnt
instead of 32-bit
popcnt
, but the PSHUFB version is still almost twice as fast.
One odd thing is the way
cnt
gets accumulated.
cnt
is stored in
ecx
. But, instead of adding the result of the
popcnt
to
ecx
, clang has decided to add
ecx
to the result of the
popcnt
. To fix that, clang then has to move that sum into
ecx
at the end of each loop iteration.
The other noticeable problem is that we only get one
popcnt
per iteration of the loop, which means the loop isn't getting unrolled, and we're paying the entire cost of the loop overhead for each
popcnt
. Unrolling the loop can also let the CPU extract more instruction level parallelism from the code, although that's a bit beyond the scope of this blog post.
Using clang, that happens even with
-O3 -funroll-loops
. Using gcc, we get a properly unrolled loop, but gcc has other problems, as we'll see later. For now, let's try unrolling the loop ourselves by calling
__builtin_popcountll
multiple times during each iteration of the loop. For simplicity, let's try doing four
popcnt
operations on each iteration. I don't claim that's optimal, but it should be an improvement.
uint32_t builtin_popcnt_unrolled(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  int cnt = 0;
  for (int i = 0; i < len; i+=4) {
    cnt += __builtin_popcountll(buf[i]);
    cnt += __builtin_popcountll(buf[i+1]);
    cnt += __builtin_popcountll(buf[i+2]);
    cnt += __builtin_popcountll(buf[i+3]);
  }
  return cnt;
}
The core of our loop now has
0000000100001390        popcntq (%rdi,%rcx,8), %rdx
0000000100001396        addl    %eax, %edx
0000000100001398        popcntq 0x8(%rdi,%rcx,8), %rax
000000010000139f        addl    %edx, %eax
00000001000013a1        popcntq 0x10(%rdi,%rcx,8), %rdx
00000001000013a8        addl    %eax, %edx
00000001000013aa        popcntq 0x18(%rdi,%rcx,8), %rax
00000001000013b1        addl    %edx, %eax
with pretty much the same code surrounding the loop body. We're doing four
popcnt
operations every time through the loop, which results in the following performance:
Algorithm
1k
4k
16k
65k
256k
1M
4M
16M
Intrinsic
6.9
7.3
7.4
7.5
7.5
7.5
7.5
7.5
PSHUFB
11.5
13.0
13.3
13.4
13.1
13.4
13.0
12.6
Unrolled
12.5
14.4
15.0
15.1
15.2
15.2
15.2
15.2
Between using 64-bit
popcnt
and unrolling the loop, we've already beaten the allegedly faster
pshufb
code! But it's close enough that we might get different results with another compiler or some other chip. Let's see if we can do better.
So, what's the deal with this
popcnt false dependency bug
that's been getting a lot of publicity lately? Turns out,
popcnt
has a false dependency on its destination register, which means that even though the result of
popcnt
doesn't depend on its destination register, the CPU thinks that it does and will wait until the destination register is ready before starting the
popcnt
instruction.
x86 typically has two operand operations, e.g.,
addl %eax, %edx
adds
eax
and
edx
, and then places the result in
edx
, so it's common for an operation to have a dependency on its output register. In this case, there shouldn't be a dependency, since the result doesn't depend on the contents of the output register, but that's an easy bug to introduce, and a hard one to catch.
In this particular case,
popcnt
has a 3 cycle latency, but it's pipelined such that a
popcnt
operation can execute each cycle. If we ignore other overhead, that means that a single
popcnt
will take 3 cycles, 2 will take 4 cycles, 3 will take 5 cycles, and n will take n+2 cycles, as long as the operations are independent. But, if the CPU incorrectly thinks there's a dependency between them, we effectively lose the ability to pipeline the instructions, and that n+2 turns into 3n.
We can work around this by buying a CPU from AMD or VIA, or by putting the
popcnt
results in different registers. Let's making an array of destinations, which will let us put the result from each
popcnt
into a different place.
uint32_t builtin_popcnt_unrolled_errata(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  int cnt[4];
  for (int i = 0; i < 4; ++i) {
    cnt[i] = 0;
  }

  for (int i = 0; i < len; i+=4) {
    cnt[0] += __builtin_popcountll(buf[i]);
    cnt[1] += __builtin_popcountll(buf[i+1]);
    cnt[2] += __builtin_popcountll(buf[i+2]);
    cnt[3] += __builtin_popcountll(buf[i+3]);
  }
  return cnt[0] + cnt[1] + cnt[2] + cnt[3];
}
And now we get
0000000100001420        popcntq (%rdi,%r9,8), %r8
0000000100001426        addl    %ebx, %r8d
0000000100001429        popcntq 0x8(%rdi,%r9,8), %rax
0000000100001430        addl    %r14d, %eax
0000000100001433        popcntq 0x10(%rdi,%r9,8), %rdx
000000010000143a        addl    %r11d, %edx
000000010000143d        popcntq 0x18(%rdi,%r9,8), %rcx
That's better -- we can see that the first popcnt outputs into
r8
, the second into
rax
, the third into
rdx
, and the fourth into
rcx
. However, this does the same odd accumulation as the original, where instead of adding the result of the
popcnt
to
cnt[i]
, it does the opposite, which necessitates moving the results back to
cnt[i]
afterwards.
000000010000133e        movl    %ecx, %r10d
0000000100001341        movl    %edx, %r11d
0000000100001344        movl    %eax, %r14d
0000000100001347        movl    %r8d, %ebx
Well, at least in clang (3.4). Gcc (4.8.2) is too smart to fall for this separate destination thing and “optimizes” the code back to something like our original version.
Algorithm
1k
4k
16k
65k
256k
1M
4M
16M
Intrinsic
6.9
7.3
7.4
7.5
7.5
7.5
7.5
7.5
PSHUFB
11.5
13.0
13.3
13.4
13.1
13.4
13.0
12.6
Unrolled
12.5
14.4
15.0
15.1
15.2
15.2
15.2
15.2
Unrolled 2
14.3
16.3
17.0
17.2
17.2
17.0
16.8
16.7
To get a version that works with both gcc and clang, and doesn't have these extra
mov
s, we'll have to write the assembly by hand:
uint32_t builtin_popcnt_unrolled_errata_manual(const uint64_t* buf, int len) {
  assert(len % 4 == 0);
  uint64_t cnt[4];
  for (int i = 0; i < 4; ++i) {
    cnt[i] = 0;
  }

  for (int i = 0; i < len; i+=4) {
    __asm__(
        "popcnt %4, %4  \n\
        "add %4, %0     \n\t"
        "popcnt %5, %5  \n\t"
        "add %5, %1     \n\t"
        "popcnt %6, %6  \n\t"
        "add %6, %2     \n\t"
        "popcnt %7, %7  \n\t"
        "add %7, %3     \n\t" // +r means input/output, r means intput
        : "+r" (cnt[0]), "+r" (cnt[1]), "+r" (cnt[2]), "+r" (cnt[3])
        : "r"  (buf[i]), "r"  (buf[i+1]), "r"  (buf[i+2]), "r"  (buf[i+3]));
  }
  return cnt[0] + cnt[1] + cnt[2] + cnt[3];
}
This directly translates the assembly into the loop:
00000001000013c3        popcntq %r10, %r10
00000001000013c8        addq    %r10, %rcx
00000001000013cb        popcntq %r11, %r11
00000001000013d0        addq    %r11, %r9
00000001000013d3        popcntq %r14, %r14
00000001000013d8        addq    %r14, %r8
00000001000013db        popcntq %rbx, %rbx
Great! The
add
s are now going the right direction, because we specified exactly what they should do.
Algorithm
1k
4k
16k
65k
256k
1M
4M
16M
Intrinsic
6.9
7.3
7.4
7.5
7.5
7.5
7.5
7.5
PSHUFB
11.5
13.0
13.3
13.4
13.1
13.4
13.0
12.6
Unrolled
12.5
14.4
15.0
15.1
15.2
15.2
15.2
15.2
Unrolled 2
14.3
16.3
17.0
17.2
17.2
17.0
16.8
16.7
Assembly
17.5
23.7
25.3
25.3
26.3
26.3
25.3
24.3
Finally! A version that blows away the
PSHUFB
implementation. How do we know this should be the final version? We can see from
Agner's instruction tables
that we can execute, at most, one
popcnt
per cycle. I happen to have run this on a 3.4Ghz Sandy Bridge, so we've got an upper bound of
8 bytes / cycle * 3.4 G cycles / sec = 27.2 GB/s
. That's pretty close to the
26.3 GB/s
we're actually getting, which is a sign that we can't make this much faster.
In this case, the hand coded assembly version is about 3x faster than the original intrinsic loop (not counting the version from a version of clang that didn't emit a
popcnt
). It happens that, for the compiler we used, the unrolled loop using the
popcnt
intrinsic is a bit faster than the
pshufb
version, but that wasn't true of one of the two unrolled versions when I tried this with
gcc
.
It's easy to see why someone might have benchmarked the same code and decided that
popcnt
isn't very fast. It's also easy to see why using intrinsics for performance critical code can be a huge time sink.
Thanks to
Scott
for some comments on the organization of this post, and to
Leah
for extensive comments on just about everything
If you liked this, you'll probably enjoy
this post about how CPUs have changed since the 80s
.
