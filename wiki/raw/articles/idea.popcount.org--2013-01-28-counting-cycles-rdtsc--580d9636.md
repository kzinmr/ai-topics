---
title: "Counting cycles - RDTSC"
url: "https://idea.popcount.org/2013-01-28-counting-cycles---rdtsc"
fetched_at: 2026-05-05T07:01:13.683194+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Counting cycles - RDTSC

Source: https://idea.popcount.org/2013-01-28-counting-cycles---rdtsc

Counting cycles - RDTSC
28 January 2013
In 2010 Intel engineer, Gabriele Paoloni, released a very informative
paper on
How To Benchmark Code Execution
.
It boils down to the following observations regarding counting CPU
cycles:
Disable hyper-threading, frequency scaling and turbo mode. Ie: all
   hardware sources of indeterminism.
Consider loading your code to a kernel module for a benchmark.
Disable interrupts.
Use
cpuid
and
rdtsc
to get cycle count when starting the hot
   code.
Use
rdtscp
and
cpuid
to get the counter when code finishes.
Make sure to "warm up" the code before benchmarking. As the author
   puts it: "[This code fragment] is to ‘warm up’ the instruction cache
   to avoid spurious measurements due to cache effects in the first
   iterations of the [benchmarked] loop."
The final code follows. Beware - I put one of the shift operations
within the hot code - to get even more accurate cycle count of your
code consider moving the
cycles
calculation out of the hot code
section.
Additionally, to get accurate measurements you need to subtrack the
fixed cost of the timing code. On my i7 CPU it's 36 cycles (including
the
cycles
calculation).
#ifdef __i386__
#  define RDTSC_DIRTY "%eax", "%ebx", "%ecx", "%edx"
#elif __x86_64__
#  define RDTSC_DIRTY "%rax", "%rbx", "%rcx", "%rdx"
#else
# error unknown platform
#endif
#define RDTSC_START(cycles)                                \
do {                                                   \
register unsigned cyc_high, cyc_low;               \
asm volatile("CPUID\n\t"                           \
"RDTSC\n\t"                           \
"mov %%edx, %0\n\t"                   \
"mov %%eax, %1\n\t"                   \
: "=r" (cyc_high), "=r" (cyc_low)     \
:: RDTSC_DIRTY);                      \
(cycles) = ((uint64_t)cyc_high << 32) | cyc_low;   \
} while (0)
#define RDTSC_STOP(cycles)                                 \
do {                                                   \
register unsigned cyc_high, cyc_low;               \
asm volatile("RDTSCP\n\t"                          \
"mov %%edx, %0\n\t"                   \
"mov %%eax, %1\n\t"                   \
"CPUID\n\t"                           \
: "=r" (cyc_high), "=r" (cyc_low)     \
:: RDTSC_DIRTY);                      \
(cycles) = ((uint64_t)cyc_high << 32) | cyc_low;   \
} while(0)
As a side note,
Prof. John Regehr wrote about counting cycles on Raspberry Pi
.
