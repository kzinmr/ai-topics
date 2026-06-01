---
title: "Restartable Sequences"
url: "https://justine.lol/rseq/"
fetched_at: 2026-06-01T07:14:09.885947+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# Restartable Sequences

Source: https://justine.lol/rseq/

May 31
st
, 2026 @
justine's web page
Restartable Sequences
The best kept secret at the frontier of system programming right now is
the Linux 4.18+ (c. 2018) concept of restartable sequences or rseq for
short. They allow you to create thread-safe data structures without
locks or atomics which scale to microprocessors with many cores.
It's currently only possible to use rseq on Linux using handwritten
assembly code. However I believe in the future, all operating systems
will be updated to support
rseq()
, all system programming
languages will be redesigned to be able to express restartable
sequences, and all data structure libraries will be rewritten to use
them.
So far the only software I've seen using rseq is tcmalloc, jemalloc,
glibc, and cosmopolitan. That's destined to change now that
microprocessors with 128 or even 192 cores are becoming inexpensive. For
example,
On my $160
Raspberry Pi 5
(which
has 4 cores), rseq makes my
malloc()
implementation
3x faster
versus having a dlmalloc
mspace assigned to each thread. For most developers, that's a take it or
leave it kind of improvement. However,
On my $4,834
System76 Thelio Astra
with Ampere's 128 core 3GHz Altra CPU
, rseq makes cosmopolitan
malloc()
go
34x faster
(compared to
sharding ops over an array of mspaces
using
sched_getcpu()%32
)
On my $17,628.55
AMD Threadripper Pro
7995WX
with 96 cores, rseq makes
my
malloc()
43x faster
(versus using that
same
sched_getcpu()
mutex sharding technique)
System programmers who don't have a workstation like the ones above are
going to be left behind like a dinosaur, with no opportunity to pluck
the low hanging fruit of 10x performance optimizations. For example, I
wouldn't have been able to pull off the
speedups I made to matrix multiplication
last
year if I hadn't splurged on a 96 core CPU. It put me in the poor house
for a few months (since the cheaper Ampere workstations weren't
available it the time) but was so worth it, since my work received
press
coverage
,
it
made
me famous in the AI community
, it helped my project
get
adopted
by 32% of organizations
, and even earned me a job offer from Google
to work in their Gradient Canopy improving TPU performance for Gemini.
If you do have one of these microprocessors, then restartable sequences
are going to be one of the most important tricks you'll use to exploit
its capabilities. This tutorial will show you how they work, and provide
you with a concrete example for pushing and popping which can be
immediately useful.
What Problems Do Restartable Sequences Solve?
Whenever the Cosmopolitan C runtime creates a thread on a Linux system,
it issues an
rseq()
system call which gives the kernel 32
bytes of TLS memory. Then, for the remainder of that thread's life, the
kernel will update the TLS memory with the CPU number whenever the
thread is rescheduled. I found that to be immediately helpful for
improving my
sched_getcpu()
implementation. Since now it
just needs a 1 nanosecond relaxed
mov
instruction to get
the CPU number, whereas before I needed to wait an entire microsecond
for the
getcpu()
system call.
However it gets better. There's a second field in the rseq TLS memory
that allows the thread to send information back to the kernel. Normally
the
rseq_cs
field is
NULL
, but it can be
updated with a pointer specifying a sequence of assembly instructions in
your program. Now, whenever the kernel preempts your thread and tries to
move it to a different CPU, it'll notice your
rseq_cs
is
non-null, and will check the program counter (a.k.a. %rip on x86) to see
if it's currently within the specified interval. If that's the case,
then the kernel will force the thread to jump to an abort handler you
also specify, which can do things like jump back to the beginning of the
function to retry the operation.
Here's why we need that. Let's say you have a GIL like this:
static
pthread_mutex_t
lock
;
static struct
List
*
list
;
If you're using that to protect your data structures, then it's going to
go slow on systems with dozens of cores, since only a single thread can
hold the lock at any given moment. So you might think, let's create a
lockless list using atomics. That's pretty simple if we're only pushing,
but if we want to also be able to pop, then we'd need to account for the
ABA
problem
with something like the following:
#define
MASQUE
0x00fffffffffffff0
// supports pml5t w/ malloc'd memory
#define
PTR
(x) ((
uintptr_t
)(x) & MASQUE)
#define
TAG
(x) ROL((
uintptr_t
)(x) & ~MASQUE, 8)
#define
ABA
(p, t) ((
uintptr_t
)(p) | (ROR((
uintptr_t
)(t), 8) & ~MASQUE))
#define
ROL
(x, n) (((x) << (n)) | ((x) >> (64 - (n))))
#define
ROR
(x, n) (((x) >> (n)) | ((x) << (64 - (n))))
struct
List
{
struct
List
*next;
// ...
};
_Atomic
(
struct
List
*)
list
;
void
push
(
struct
List
*elem) {
struct List
*tip;
for
(tip = atomic_load_explicit(&list, memory_order_relaxed);;) {
    elem->next = (
struct
List
*)PTR(tip);
if
(atomic_compare_exchange_weak_explicit(
            &list, &tip, (
struct
List
*)ABA(elem, TAG(tip) + 1),
            memory_order_release, memory_order_relaxed))
break
;
    pthread_yield_np();
  }
}
struct
List
*
pop
(void) {
struct
List
*tip, *elem;
  tip = atomic_load_explicit(&list, memory_order_relaxed);
while
((elem = (
struct
List
*)PTR(tip))) {
if
(atomic_compare_exchange_weak_explicit(
            &list, &tip, (
struct
List
*)ABA(elem->next, TAG(tip) + 1),
            memory_order_acquire, memory_order_relaxed))
break
;
    pthread_yield_np();
  }
return
elem;
}
The issue is this will likely go just as slow if not slower. The mere
act of sharing the same 64-byte region of memory (a.k.a. cacheline)
between multiple cores, causes the CPU internally to basically use a
mutex, and chances are the CPU's internal mutexes aren't as good as the
ones you've implemented in userspace.
So one potentially smarter approach is to shard the data structure, so
each CPU gets its own area.
static struct
{
alignas
(64)
struct
List
*list;
}
lists
[CPU_SETSIZE];
Then all you have to do is index the
lists
array
using
sched_getcpu()
. The issue is that doesn't work. We
still need a mutex, due to how the operating system might preempt and
relocate your thread twixt the cpu number load and any mutations you've
made.
static struct
{
alignas
(64)
pthread_mutex_t
lock;
struct
List
*list;
}
gil
[CPU_SETSIZE];
So now that we've fixed things, it looks like we ended up back where we
started, except now we have to manage 1024 copies. However, despite
appearances, this code actually is much more optimal. By having a
separate mutex for each cpu, we've ensured they'll only be contended
when we hit corner cases. It matters because the difference between a
contended versus uncontended lock is like the night and the day. With
a
great mutex library like nsync
a contended
lock operation will cost you
at least
200 nanoseconds. However
an uncontended lock/unlock operation only costs about 15 nanoseconds. We
further use
alignas(64)
to ensure that the pointer is
placed on a separate cacheline for each CPU, thereby reducing any
hardware internal contention to a very low order of probability.
However if all we're doing is pushing and popping, then that 15
nanoseconds is still an enormous cost compared to a thread local linked
list push or pop which only costs about a nanosecond. So we really want
to get rid of the mutex. The only thing standing in our way is a fringe
rarely-occurring corner case where the operating system interrupts our
tiny sequence of a few assembly instructions during which we mutate the
list.
So how do we get rid of the mutex? At this point, you might be thinking
you need an RTOS which guarantees your thread won't be preempted, or
perhaps your existing OS might have a
sched_setscheduler()
policy that gives you back some semblance of control. For specialized
deployments, that might work. There's also
sched_setaffinity()
which is supported on Linux, FreeBSD,
and Windows. That will work for a given application, if you feel
comfortable pinning your threads to particular CPUs. But all these
approaches folks have invented in the past for controlling the OS
scheduler can be potentially disastrous if your program's execution
doesn't go the way you planned.
This is why Linux now provides
rseq()
which is a much more enlightened solution. With
restartable sequences, you actually can get rid of both the mutex and
atomics, while the OS continues to fully abstract scheduling. The way it
works is you advise the kernel whenever your program enters a critical
section of code that you don't want interrupted. It's probably going to
be maybe 10 assembly instructions tops. The first assembly opcode should
be a move instruction that sets the
rseq_cs
field. The last
instruction needs to be the thing that makes the modification to your
global data structure. Think of it sort of like a really tiny database
transaction. What makes it go fast, is that the bidirectional
communication with the kernel happens via shared memory.
Here's your gentle introduction to restartable sequences. We're going to
build a program that just increments a number. Since that's probably the
simplest thing imaginable. Imagine you have a blog that gets billions of
visitors per second, which is hosted on a multi-threaded webserver you
wrote from scratch and you need to track visits. In that case, I can
think of five ways you could build your hit counter
(using
cosmocc
to build the example code).
96 core AMD Ryzen Threadripper Pro 7995WX (x86-64)
wall
time (ms)
wall
ops/sec
user
time (ms)
system
time (ms)
cpu
ops/sec
implementation
62,461
30,739k
118,631
11,744,462
161k
hitcounter-mutex.c
(glibc)
29,389
65,331k
34,094
13,259
40,547k
hitcounter-mutex.c
(cosmo)
23,412
82,009k
4,366,203
0
440k
hitcounter-atomic.c
543
3,535,912k
93,274
0
20,585k
hitcounter-shard.c
20
96,000,000k
1,150
12
1,652,324k
hitcounter-rseq.c
7
274,285,714k
0
11
174,545,455k
hitcounter-affinity.c
Earlier when I said rseq made my code go 34x or 43x faster, it's
important to note that I was comparing it to the
portable
version of my
malloc()
implementation, which is already
heavily optimized for multicore systems. If we compare rseq to a truly
naïve solution, such as using a glibc mutex to guard an increment
operation, then we see that rseq can actually make things go
a
million times faster
judging by CPU time consumption.
It sounds like I'm joking, except I'm not, since half the friends I
asked told me that using the mutex was their first instinct here.
Now in terms of exploring the five approaches listed above, we can see
that only three are worth considering.
Sharding is the best when you need portability to all operating systems.
We use the
cosmo_shard()
function pointer to accomplish
this. This will use
__get_rseq()->cpu_id
on modern Linux,
falling back to alternatives like
lsl
'ing the global
descriptor table,
rdpid
,
rdtscp
, or
sched_getcpu()
when available, and if all else fails
it'll use
murmur3(gettid())%32
as a last resort.
Affinity was the absolute fastest, but it requires micromanaging all
threads. That rules it out for library authors. It's probably a bad idea
for app authors too. I'd be terrified of shooting myself in the foot if
I tried that. However, I could potentially imagine some situations where
it might be appropriate. However it's important to note that GCC
cheated. By annihilating all volatile operations, we were able to
leverage the compiler's knowledge of mathematics to find a closed form
solution to increment, which is addition. So that's not cheating at all.
If I use
alignas(64) volatile long x
in
the
hitcounter-affinity.c
example, then it ends up going exactly the same speed as the rseq
example.
Restartable sequences make superior tradeoffs. They only currently work
on modern Linux, so if you're building a library or something that's
open source, you're going to need to support other strategies too. It
requires writing code at a higher difficulty setting. I'm afraid LLMs
are not yet smart enough to help you build restartable sequences.
However in the future I believe programming languages will change so we
can elegantly express restartable sequences, similar to how C11
introduced compiler APIs for atomics.
Now let's move on to my ARM workstation.
System76 Thelio Astra w/ Ampere's 128 core 3GHz Altra CPU (ARM64)
wall
time (ms)
wall
ops/sec
user
time (ms)
system
time (ms)
cpu
ops/sec
implementation
219,484
5,832k
322,259
15,790,712
79k
hitcounter-mutex.c
(glibc)
212,005
6,038k
144,163
67,841
6,038k
hitcounter-mutex.c
(cosmo)
17,924
71,413k
2,162,867
0
592k
hitcounter-atomic.c
417
3,069,544k
42,972
0
29,787k
hitcounter-shard.c
39
32,820,513k
2,966
61
422,861k
hitcounter-rseq.c
12
106,666,667k
15
1
80,000,000k
hitcounter-affinity.c
In the table above, the ops/sec columns are most directly comparable
with the Threadripper results, since they're scaled with respect to the
workload. More ops/sec is better. Looking at these numbers, a few things
stand out:
Ampere's ARM Altra CPU has really fast atomics. One benefit of ARM is
that it has a fancier memory model,
which
hitcounter-atomic.c
exploits using
atomic_fetch_add_explicit(&counter, 1,
memory_order_relaxed)
. Thanks to relaxed ordering, we get
an
ldadd
instruction, which doesn't need to manage memory
barriers. You can't do that on x86, since
xadd
is always
strongly ordered. What's more interesting is that, even if I specify
memory_order_seq_cst
(for
ldaddal
) my Altra
CPU
still
goes noticeably faster than my Threadripper. I
suspect it might be hyperthreading that got it into trouble, because my
Threadripper
claims
to have 192 CPUs.
Cosmopolitan's implementation of POSIX mutexes is very complicated. It
does a better job than glibc, but I think we could improve our
implementation to have better latency on ARM microprocessors.
The rest of the differences in numbers are mostly commensurate with the
difference in price.
Using restartable sequences turned my 3GHz CPU into a 33GHz CPU.
Using mutexes turned my 3GHz CPU into a 219MHz CPU.
Here's what I think is cool about Ampere's ARM CPUs. I'm actually huge
fan of x86-64. I always have been. For years, I've been reading people
on forums like Hacker News talk about how x86 is bad because it has
things like a complicated instruction decoder. RISC fans have always
claimed that ARM, due to its intelligent design (like how all
instructions are 4 bytes long) you can have more cores at a lower price.
To that, my response has always been, "then show me where I can buy one"
and no one has really given me an answer until now. Ampere made the
dream of RISC finally come true. Now the CPU I own with the most cores
is an ARM chip, and I was pleasantly surprised to discover that
benchmarks exist where it's able to outperform a significantly more
expensive x86 chip.
Let's say you want to track object instances globally. Using rseq, it's
relatively easy to implement the
push()
and
pop()
operations for a sharded linked list. Here's a
working example that you can compile with
cosmocc
:
#include
<assert.h>
#include
<cosmo.h>
#include
<linux/rseq.h>
#include
<pthread.h>
#include
<stdio.h>
#include
<stdlib.h>
#define
ITERATIONS
10000000l
struct
List
{
struct
List
*next;
};
struct
{
alignas
(64)
struct
List
*freelist;
}
heaps
[CPU_SETSIZE];
Here we see that we finally got rid of the locks and atomics. We're
using
alignas(64)
to ensure each CPU's memory is on a
separate cacheline, which means there'll be no synchronization
bloodbaths happening inside the hardware. Since Linux
defines
CPU_SETSIZE
as 1024, we have to burn quite a bit of
BSS memory, however most of it isn't going to be used. For single
threaded programs, the Linux Kernel does a remarkably good job picking 1
or 2 cores and sticking with it. We put a lot of faith in the kernel to
not fragment our objects needlessly, since this design doesn't easily
allow for a rebalancing of elements. It should not be needed.
static inline void
push
(
struct
List
*chunk) {
#ifdef
__x86_64__
asm volatile
(
".pushsection .rodata.rseq,\"a\",@progbits\n"
"	.balign	32\n"
"300:	.long	0\n"
// rseq_cs::version
"	.long	0\n"
// rseq_cs::flags
"	.quad	301f\n"
// rseq_cs::start_ip
"	.quad	302f-301f\n"
// rseq_cs::post_commit_offset
"	.quad	303f\n"
// rseq_cs::abort_ip
"	.popsection\n"
//
"301:	lea	300b(%%rip),%%rcx\n"
//
"	mov	%%rcx,8(%1)\n"
// rseq->rseq_cs
"	mov	(%1),%%ecx\n"
// rseq->cpu_id_start
"	shl	$6,%%ecx\n"
//
"	mov	(%2,%%rcx),%%rdx\n"
// rdx = freelist
"	mov	%%rdx,(%0)\n"
// chunk->next = rdx
"	mov	%0,(%2,%%rcx)\n"
// freelist = chunk
"302:	.pushsection .text.unlikely,\"ax\",@progbits\n"
"	.byte	0x0f,0xb9,0x4d\n"
"	.long	0x53053053\n"
"303:	jmp	301b\n"
// restart on abort
"	.popsection"
:
/* no outputs */
:
"r"
(chunk),
"r"
(__get_rseq()),
"r"
(heaps)
               :
"rcx"
,
"rdx"
,
"memory"
);
#elifdef
__aarch64__
asm volatile
(
".pushsection .rodata.rseq,\"a\",@progbits\n"
"	.balign	32\n"
"300:	.long	0\n"
// rseq_cs::version
"	.long	0\n"
// rseq_cs::flags
"	.quad	301f\n"
// rseq_cs::start_ip
"	.quad	302f-301f\n"
// rseq_cs::post_commit_offset
"	.quad	303f\n"
// rseq_cs::abort_ip
"	.popsection\n"
//
"301:	adrp	x4, 300b\n"
// load address of rseq_cs
"	add	x4, x4, :lo12:300b\n"
//
"	str	x4, [%1, #8]\n"
// rseq->rseq_cs
"	ldr	w4, [%1]\n"
// rseq->cpu_id_start
"	lsl	w4, w4, #6\n"
//
"	ldr	x5, [%2, x4]\n"
// x5 = freelist
"	str	x5, [%0]\n"
// chunk->next = x5
"	str	%0, [%2, x4]\n"
// freelist = chunk
"302:	.pushsection .text.unlikely,\"ax\",@progbits\n"
"	.long	0xd428bc00\n"
"303:	adrp	x5, 301b\n"
// load page address of 301b
"	add	x5, x5, :lo12:301b\n"
// add low 12 bits
"	br	x5\n"
// branch to 301b via register
"	.popsection"
:
/* no outputs */
:
"r"
(chunk),
"r"
(__get_rseq()),
"r"
(heaps)
               :
"x4"
,
"x5"
,
"memory"
);
#endif
}
static inline struct
List
*
pop
(
void
) {
struct
List
*chunk;
#ifdef
__x86_64__
asm volatile
(
".pushsection .rodata.rseq,\"a\",@progbits\n"
"	.balign	32\n"
"300:	.long	0\n"
// rseq_cs::version
"	.long	0\n"
// rseq_cs::flags
"	.quad	301f\n"
// rseq_cs::start_ip
"	.quad	302f-301f\n"
// rseq_cs::post_commit_offset
"	.quad	303f\n"
// rseq_cs::abort_ip
"	.popsection\n"
//
"301:	lea	300b(%%rip),%%rcx\n"
//
"	mov	%%rcx,8(%1)\n"
// rseq->rseq_cs
"	mov	(%1),%%ecx\n"
// rseq->cpu_id_start
"	shl	$6,%%ecx\n"
//
"	mov	(%2,%%rcx),%0\n"
// chunk = chunks[cpu].freelist
"	test	%0,%0\n"
//
"	jz	302f\n"
//
"	mov	(%0),%%rdx\n"
// rdx = chunk->next
"	mov	%%rdx,(%2,%%rcx)\n"
// freelist = rdx
"302:	.pushsection .text.unlikely,\"ax\",@progbits\n"
"	.byte	0x0f,0xb9,0x4d\n"
"	.long	0x53053053\n"
"303:	jmp	301b\n"
// restart on abort
"	.popsection"
:
"=&r"
(chunk)
               :
"r"
(__get_rseq()),
"r"
(heaps)
               :
"rcx"
,
"rdx"
,
"memory"
);
#elifdef
__aarch64__
asm volatile
(
".pushsection .rodata.rseq,\"a\",@progbits\n"
"	.balign	32\n"
"300:	.long	0\n"
// rseq_cs::version
"	.long	0\n"
// rseq_cs::flags
"	.quad	301f\n"
// rseq_cs::start_ip
"	.quad	302f-301f\n"
// rseq_cs::post_commit_offset
"	.quad	303f\n"
// rseq_cs::abort_ip
"	.popsection\n"
//
"301:	adrp	x4, 300b\n"
// load address of rseq_cs
"	add	x4, x4, :lo12:300b\n"
//
"	str	x4, [%1, #8]\n"
// rseq->rseq_cs
"	ldr	w4, [%1]\n"
// rseq->cpu_id_start
"	lsl	w4, w4, #6\n"
//
"	ldr	%0, [%2, x4]\n"
// chunk = chunks[cpu].freelist
"	cbz	%0, 302f\n"
//
"	ldr	x5, [%0]\n"
// x5 = chunk->next
"	str	x5, [%2, x4]\n"
// freelist = x5
"302:	.pushsection .text.unlikely,\"ax\",@progbits\n"
"	.long	0xd428bc00\n"
"303:	adrp	x5, 301b\n"
// load page address of 301b
"	add	x5, x5, :lo12:301b\n"
// add low 12 bits
"	br	x5\n"
// branch to 301b via register
"	.popsection"
:
"=&r"
(chunk)
               :
"r"
(__get_rseq()),
"r"
(heaps)
               :
"x4"
,
"x5"
,
"memory"
);
#endif
return
chunk;
}
Now let's go over the assembly code, in the hopes of demystifying it.
For starters, we're using
Richard
Stallman's Math 55 assembly notation
, which I documented for
personal reference on x86 many years ago in that text file. The GNU
assembler mixed with the C/C++ constraints system is the most powerful
thing there is. For starters,
.pushsection
.rodata.rseq,
"a"
,
@progbits
// ...
.popsection
lets us teleport content to a totally different area of the executable
file. In this case, we're using the section
name
.rodata.rseq
because the standard GNU linker scripts
(e.g.
/usr/lib/x86_64-linux-gnu/ldscripts/elf_x86_64.x
) are
hard-coded to recognize sections named
.rodata
or
.rodata.*
and then puts them into an ELF program header
segment that'll be marked
PROT_READ
on process startup. The
code within the pushpop:
300
:
.long
0
// rseq_cs::version
.long
0
// rseq_cs::flags
.quad
301
f
// rseq_cs::start_ip
.quad
302
f
-301
f
// rseq_cs::post_commit_offset
.quad
303
f
// rseq_cs::abort_ip
lays out the
static const struct rseq_cs
content (see
definition below) which describes the restartable sequence. It's
important to use System V style numeric labels here with the forwards
(f) and backwards (b) references. That's because they can be repeated in
the assembly multiple times, which means the assembler won't break if
our function is inlined multiple times by the compiler. Alternatively,
it's also possible to create labels like
.Ldescription.%=
since that'll generate a unique ID for each
asm()
block.
301
:
lea
300b(
%%rip
),
%%rcx
mov
%%rcx
,8(
%1
)
We use the
301
label for the actual restartable sequence.
These first two opcodes in our sequence is basically saying
__get_rseq()->rseq_cs = &300b
(note: the
%1
is
used to reference the asm block arguments by index, which in this case
is
"r"(__get_rseq())
, further noting that
the
r
causes the rseq address to be stored in an arbitrary
register). That's basically modifying a piece of
TLS
memory we shared with the kernel. The
lea
instruction is needed to
support
PIC
, but
the above could be shortened to
movq $300b,8(%1)
if you're
using Cosmopolitan.
When the kernel decides to preempt our thread, it'll check
the
rseq_cs
field and read the rodata structure we created
earlier, to determine whether or not the program counter (%rip) is
currently located inside
300
label. If it is, then kernel
changes the program counter to the
abort_ip
which we
specified as pointing to label
303
.
mov
(
%1
),
%%ecx
// rseq->cpu_id_start
shl
$6
,
%%ecx
//
Next up, we load the
__get_rseq()->cpu_id_start
field
documented below. This tells us the index of the CPU on which our thread
is currently running. Then we shift it left by 6 places, which is a fast
way to multiply by 64. It's important that this happen inside the
sequence. Since you'll notice our abort handler simply jumps back to the
start of the sequence. At that point, after being preempted and
relocated, the CPU index is obviously going to change, so the memory
index needs to be recomputed.
mov
(
%2
,
%%rcx
),
%%rdx
// rdx = heaps[rcx].freelist
mov
%%rdx
,(
%0
)
// chunk->next = rdx
mov
%0
,(
%2
,
%%rcx
)
// heaps[rcx].freelist = chunk
302
:
Finally, we perform the actual push operation. Note that we don't
actually mutate global memory until the last instruction. The whole
sequence works like a transaction. The last instruction is special,
since it's what commits the change.
.pushsection
.text.unlikely,
"ax"
,
@progbits
.byte
0x0f,0xb9,0x4d
.long
0x53053053
303
:
jmp
301
b
// restart on abort
.popsection
Our abort handler is simple enough. All it does is jump back to the
start of our restartable sequence. The only thing surprising about this
code is that the kernel requires it to be prefixed by an arbitrary
32-bit word that was passed to the
rseq()
system call
earlier. Since that Cosmopolitan C runtime is responsible for issuing
that system call, cosmo defines that magic number as
RSEQ_SIG
in the
<linux/rseq.h>
header
file documented below. Another thing we do is we teleport the abort
handler code to the
.text.unlikely
section of our binary,
since that's another GNU standard section name explicitly defined by
stock linker scripts.
All you see here is basically the technique I used in
my
malloc()
implementation for Cosmopolitan Libc. When a
small allocation (fewer than 512 bytes) is requested, it tries to pop a
piece of memory from a global sharded list like the above. If one isn't
there, then it asks
mmap()
for a new page of memory,
divides it into chunks, pushes them all, and then the allocation
operation tries again. It's a fast, simple, and elegant design. But the
tradeoff is that it's difficult to release memory back to the system,
since here we're basically assuming
List
memory is
permanent.
Now let's write some code for testing our push and pop functions.
void
*
worker
(
void
*arg) {
struct
List
*elem;
for
(
long
i = 0; i < ITERATIONS; ++i) {
switch
(i % (ITERATIONS / 10000)) {
case
0:
        push(malloc(
sizeof
(
struct
List
)));
break
;
default
:
if
((elem = pop()))
          push(elem);
break
;
    }
  }
return
0;
}
void
cleanup
(
void
) {
for
(
int
i = 0; i < CPU_SETSIZE; ++i) {
struct
List
*chunk;
while
((chunk = heaps[i].freelist)) {
      heaps[i].freelist = chunk->next;
      free(chunk);
    }
  }
}
int
main
(
void
) {
if
(__get_rseq()->cpu_id < 0) {
    fprintf(stderr,
"rseq is not supported on this system\n"
);
return
1;
  }
int
threads = cosmo_cpu_count();
pthread_t
th[threads];
for
(
long
i = 0; i < threads; ++i)
    pthread_create(&th[i], 0, worker, 0);
for
(
long
i = 0; i < threads; ++i)
    pthread_join(th[i], 0);
  cleanup();
}
So there you have it. A gentle introduction to restartable sequences, by
way of a concrete example offering decent code you can use today, to
make your global linked lists more scalable on CPUs with many cores.
#define
RSEQ_CPU_ID_UNINITIALIZED
-1
#define
RSEQ_CPU_ID_REGISTRATION_FAILED
-2
#define
RSEQ_FLAG_UNREGISTER
1
#define
RSEQ_CS_FLAG_NO_RESTART_ON_PREEMPT
1
/* deprecated */
#define
RSEQ_CS_FLAG_NO_RESTART_ON_SIGNAL
2
/* deprecated */
#define
RSEQ_CS_FLAG_NO_RESTART_ON_MIGRATE
4
/* deprecated */
#ifdef
__x86_64__
#define
RSEQ_SIG
0x53053053
/* ud1 0x53053053(%rip),%edi */
#elif
defined
(__aarch64__)
#define
RSEQ_SIG
0xd428bc00
/* brk #0x45e0 */
#endif
/* consider putting this in the .rodata.rseq section of your binary */
struct
rseq_cs
{
uint32_t
version;
uint32_t
flags;
uint64_t
start_ip;
uint64_t
post_commit_offset;
uint64_t
abort_ip;
}
forcealign
(32);
/* this memory should go in thread local storage */
struct
rseq
{
/* The difference between the two is that `cpu_id_start` is always in
     range, whereas `cpu_id` may contain error values. The kernel
     provides both in order to support computation of values derived
     from the CPU ID that happens before entering the critical section.
     We could do this with one CPU ID, but it would require an extra
     branch to distinguish "not initialized" from "CPU ID changed after
     fetching it". On the other hand if (like tcmalloc) you only fetch
     the CPU Id within a critical section, then you need only one field
     because you have only one branch: am I initialized. There is no
     such thing as a CPU mismatch because instead you are just restarted
     when the CPU ID changes. —Quoth tcmalloc (rseq.md) */
uint32_t
cpu_id_start;
/* this should be initialized to RSEQ_CPU_ID_UNINITIALIZED when this
     data structure is registered with the kernel. you'll then be able
     to test if the host OS is Linux 4.18+ by simply checking cpu_id≥0 */
volatile int
cpu_id;
/* when this points to `struct rseq_cs` the kernel will be advised on
     how to handle the interrupting of this thread */
uint64_t
rseq_cs;
uint32_t
flags;
uint32_t
node_id;
uint32_t
mm_cid;
char
end[];
}
forcealign
(32);
#define
__get_rseq
() ((
struct
rseq
*)__get_tls()->tib_rseq)
Cosmopolitan creates portable binaries, which means the code I
compiled
by default
targets K8 on x86-64 and ARMv8.0-a on
Ampere. Now, obviously, cosmocc still uses tricks to exploit modern
capabilities at runtime. For example, atomic instructions on ARM are
compiled to emit a function call that dispatches to the modern LSE
opcodes when
HWCAP_ATOMICS
is advertised by the kernel. But
it's worth mentioning that, if you don't care about portable binaries,
you can squeeze another 10% performance from these programs if you build
your ARM code just for Altra using
aarch64-unknown-cosmo-cc
-mcpu=neoverse-n1 -fpermitted-flt-eval-methods=c11
.
In the first section of this blog post, I threw out a bunch of numbers
like "malloc() goes 34x faster". I measured that using the following
code, which simply spawns a thread for each CPU and repeatedly allocates
and frees small pieces of memory.
#include
<cosmo.h>
#include
<pthread.h>
#include
<stdio.h>
#include
<stdlib.h>
#define
NUM_THREADS
cosmo_cpu_count()
#define
NUM_ITERATIONS
10000000
void
*
identity
(
void
*arg) {
return
arg;
}
void
*(*
pIdentity
)(
void
*) = identity;
void
*
thread_func
(
void
*arg) {
for
(
unsigned long
i = 0; i < NUM_ITERATIONS; i++)
    free(pIdentity(malloc(i % 256)));
return
NULL
;
}
int
main
() {
pthread_t
threads[NUM_THREADS];
for
(
int
i = 0; i < NUM_THREADS; i++)
if
(pthread_create(&threads[i],
NULL
, thread_func,
NULL
))
return
1;
for
(
int
i = 0; i < NUM_THREADS; i++)
if
(pthread_join(threads[i],
NULL
))
return
1;
}
When I build this program with cosmocc, it's possible for me to disable
malloc's use of rseq by setting an environment variable, which specifies
the maximum number of rseq memory pages allowed.
cosmocc -O -o bench bench.c
time
./bench
export
COSMOPOLITAN_M_RSEQ_MAX=0
time
./bench
That environment variable is super useful, since it gives you a clear
picture on your Linux workstation of what your malloc performance is
going to look like when you run your actually portable executables on
every other OS. I'm also using it as a bulwark against pathological
cases I could envision with memory consumption.
The
tcmalloc
documentation
explains how they used rseq in their malloc
implementation. For example, the trick they use to have multiple global
memory writes is they use an array (instead of linked lists) and they
have an integer indicating how much of that array has been committed so
far. That way they can write whatever they want to the uncommitted area,
and then roll forward the integer when they're done.
The
MEMBARRIER_CMD_PRIVATE_EXPEDITED_RSEQ
command was
introduced to the
membarrier()
system call in Linux v5.10.
This is what tcmalloc uses to facilitate cross-CPU modifications to rseq
data structures.
The graphic of the Genthree Linux penguin above was drawn in
collaboration with ChatGPT.
The code font on this page is
PragmataPro
Variable
(€299) which was designed by Fabrizio Schiavi in Italy.
The
rseq()
system call was developed
by
Paul
Turner and Andrew Hunter at Google
and
Mathieu Desnoyers
at
EfficiOS
who
introduced
it into the Linux Kernel in 2018.
You're invited to join my
redbean
discord
server, where you can hang out with me and cosmo developers.
System76 and Ampere were kind enough to let me purchase their
workstation at a discounted rate, to help my open source work on
projects like llamafile. My
GitHub sponsors
,
and
Patreon subscribers
have done
much to help make my blogging and open source work possible these last
five years. This article has Amazon Associate hyperlinks, so purchasing
the recommended products is another way you can support me. Lastly
Google and Mozilla are the two companies you can thank most for helping
enable me to do what I do.
