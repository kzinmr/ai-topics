---
title: "The Fastest Mutexes"
url: "https://justine.lol/mutex/"
fetched_at: 2026-05-05T07:01:27.312031+00:00
source: "Justine Tunney"
tags: [blog, raw]
---

# The Fastest Mutexes

Source: https://justine.lol/mutex/

Oct 2
nd
, 2024 @
justine's web page
The Fastest Mutexes
Cosmopolitan Honeybadger
Cosmopolitan Libc
is well-known for
its
polyglot fat binary
hack
that lets your executables run on six OSes for AMD64 / ARM64. What may
surprise you is that it could also be the best C library for your
production workloads too. To demonstrate this point, let's compare
Cosmo's mutex library with other platforms.
We'll do this by writing a simple test that spawns
30
threads
which increment the same integer
100,000
times
. This tests how well a mutex implementation performs in
the heavily contended use case. In essence, that means the following
(see the segment at the bottom of the page for the full source code).
int
g_chores;
pthread_mutex_t
g_locker = PTHREAD_MUTEX_INITIALIZER;
void
*
worker
(
void
*arg) {
for
(
int
i = 0; i < ITERATIONS; ++i) {
    pthread_mutex_lock(&g_locker);
    ++g_chores;
    pthread_mutex_unlock(&g_locker);
  }
return
0;
}
Now let's start with the exciting part, which are my benchmark results.
Benchmarks
Times will be measured in microseconds. Wall time is how long the test
program takes to run. That includes the overhead of spawning and joining
threads. User time is how much CPU time was spent in userspace, and
system time is how much CPU time was spent in the kernel. System and
user time can exceed the actual wall time because multiple threads are
running in parallel.
The first results I'll show are for Windows because Mark Waterman did an
excellent
mutex
shootout
three months ago, where he said, "in the highly contended
scenario, Windows wins the day with its SRWLOCK". Contention is where
mutex implementations show their inequality. Mark was so impressed by
Microsoft's SRWLOCK that he went on to recommend Linux and FreeBSD users
consider targeting Windows if mutex contention is an issue.
Windows Mutex Implementations
24-core Threadripper 29070WX
wall
time (µs)
user
time (µs)
system
time (µs)
implementation
148,940
328,125
62,500
Cosmopolitan pthread_mutex_t
410,416
5,515,625
1,640,625
Microsoft SRWLOCK
949,187
7,937,500
5,078,125
Microsoft CRITICAL_SECTION
991,750
12,156,250
4,031,250
MSVC 2022 std::mutex
1,165,435
24,515,000
15,000
spin lock
9,780,803
1,937,000
6,156,000
Cygwin pthread_mutex_t
As we can see, Cosmopolitan Libc mutexes go 2.75x faster than
Microsoft's SRWLOCK (which was previously believed to be the best of the
best) while consuming 18x fewer CPU resources. Cosmopolitan mutexes were
also 65x faster than Cygwin, which like Cosmopolitan provides a POSIX
implementation on Windows. Cygwin's mutexes are so bad that they would
have been better off for this use case just using a spin lock.
Now onto Linux, the lord of all operating systems.
Linux Mutex Implementations
96-core Threadripper Pro 7995WX
wall
time (µs)
user
time (µs)
system
time (µs)
implementation
36,905
44,511
23,492
Cosmopolitan pthread_mutex_t
101,353
150,706
2,724,851
glibc pthread_mutex_t
202,423
4,694,749
2,000
spin lock
411,013
2,167,898
9,926,850
Musl libc pthread_mutex_t
Here we see Cosmopolitan mutexes are:
3x faster than glibc
11x faster than musl libc
42x less CPU time than glibc
178x less CPU time than musl libc
Here's how things actually work in practice. Imagine you have a workload
where all your threads need to do a serialized operation. With Cosmo, if
you're looking at htop, then it's going to appear like only one core is
active, whereas glibc and musl libc will fill up your entire CPU meter.
That's bad news if you're running a lot of jobs on the same server. If
just one of your servers has a mutex bloodbath, then all your resources
are gone, unless you're using cosmo. It's still a new C library and it's
a little rough around the edges. But it's getting so good, so fast, that
I'm starting to view
not
using it in production as an
abandonment of professional responsibility. The C library is so deeply
embedded in the software supply chain, and so depended upon, that you
really don't want it to be a planet killer. If essential unquestioned
tools are this wasteful then it's no wonder Amazon Cloud makes such a
fortune.
Last but not least, we have MacOS.
MacOS Mutex Implementations
M2 Ultra
wall
time (µs)
user
time (µs)
system
time (µs)
implementation
52,263
43,202
911,009
Apple Libc
54,700
63,055
1,003,674
Cosmopolitan pthread_mutex_t
On MacOS with an M2 ARM64 microprocessor, Apple's Libc slightly
outperforms Cosmopolitan's mutexes. For reasons I do not yet fully
understand, Cosmopolitan's normal mutex implementation doesn't work well
on this platform. It's possibly because the M2 and XNU are in league. So
on MacOS ARM, Cosmopolitan uses a simpler algorithm based on Ulrich
Drepper's
"
Futexes
Are Tricky
" paper that basically just farms out all the heavy
lifting to XNU's ulock system calls. That's why performance is nearly
identical to what Apple does.
So in summary, these benchmark results indicate that Cosmopolitan
mutexes, in the best case, will be overwhelmingly better than
alternatives at the contended + tiny critical section use case, and in
the worst case, Cosmopolitan will be roughly as good.
How I Did It
The reason why Cosmopolitan Mutexes are so good is because I used a
library called
nsync
. It
only has 371 stars on GitHub, but it was written by a distinguished
engineer at Google named Mike Burrows. If you don't know who he is, he's
the guy who coded Google's fiercest competitor, which was Altavista. If
you're not old enough to remember Altavista, it was the first search
engine that was good, and it ran on a single computer.
I've had a lot of fun integrating nsync into Cosmopolitan. I've even
had the opportunity to make upstream contributions. For example, I found
and fixed a bug in his mutex unlock function that had gone undiscovered
for years. I also managed to make contended nsync mutexes go 30% faster
than nsync upstream on AARCH64, by porting it to use C11 atomics. I
wrote new system integration for things like futexes that enable it do
portability at runtime. Lastly I made it work seamlessly with POSIX
thread cancelations.
So how does nsync do it? What are the tricks that it uses? Here's some
of my takes and analysis:
nsync uses an optimistic CAS (compare and swap) immediately, so that
locking happens quickly when there's no contention.
When a lock can't be acquired, nsync adds the calling thread to a
doubly linked list of waiters. Each waiter gets its own semaphore on a
separate independent cacheline. This serves an important purpose. Once a
thread enters the wait state, it's no longer touching the main lock. To
understand why that's important, read Ulrich Drepper's paper
"
What
Every Programmer Should Know About Memory
". He goes into great depth
on the coherency protocols used by modern microprocessors, where cores
basically talk to each other under the hood about which cachelines
they're using. When multiple cores touch the same ones, that creates a
lot of communication overhead within the processor.
nsync enlists the help of the operating system by using futexes. This is
a great abstraction invented by Linux some years ago, that quickly found
its way into other OSes. On MacOS, futexes are called ulock. On Windows,
futexes are called
WaitOnAddress()
. The only OS Cosmo
supports that doesn't have futexes is NetBSD, which implements POSIX
semaphores in kernelspace, and each semaphore sadly requires creating a
new file descriptor. But the important thing about futexes and
semaphores is they allow the OS to put a thread to sleep. That's what
lets nsync avoid consuming CPU time when there's nothing to do.
nsync avoids starvation with this concept of a "long wait". If a waiter
gets woken 30 times and fails to acquire the lock internally every time,
then nsync adds a bit to the lock that prevents threads that haven't
waited yet from acquiring. This means that initial CAS at the beginning
will fail for everyone else until the queue has had some time to clear.
nsync makes the use case we benchmarked go fast (contended lock with a
small critical section) using this concept of a "designated waker". This
bit on the main lock is set when a thread is awake and trying to acquire
the lock. In nsync, the unlock function is what's responsible for waking
the next thread in line waiting for the lock. Having this bit allows the
unlocking thread to know it needn't bother waking a second locker since
one is already awake.
To learn more of nsync's secrets, you can read the source code here:
cosmopolitan/third_party/nsync/mu.c
.
See also
cosmopolitan/libc/intrin/pthread_mutex_lock.c
.
Online Proof
If you want to see a live demo of a piece of software built with Cosmo
mutexes, then do your worst DDOS to the
http://ipv4.games/
web server. Now this
is truly a game for hackers, competing to dominate the Internet. You're
already playing this game because your IP was just claimed for jart. The
service runs on a GCE VM with 2 cores and so far it's managed to survive
being DDOS'd by botnets as large as 49,131,669 IPs. A lot of that is
thanks to nsync which allowed me to move SQL queries to background
threads which send messages to each other. There are still improvements
to be made, but overall it's held up well. You can even monitor
its
/statusz
health metrics.
Source Code
#define ITERATIONS 100000
#define THREADS    30
int
g_chores;
pthread_mutex_t
g_locker = PTHREAD_MUTEX_INITIALIZER;
void
*
worker
(
void
*arg) {
for
(
int
i = 0; i < ITERATIONS; ++i) {
    pthread_mutex_lock(&g_locker);
    ++g_chores;
    pthread_mutex_unlock(&g_locker);
  }
return
0;
}
struct
timeval
tub
(
struct
timeval
a,
struct
timeval
b) {
  a.tv_sec -= b.tv_sec;
if
(a.tv_usec < b.tv_usec) {
    a.tv_usec += 1000000;
    a.tv_sec--;
  }
  a.tv_usec -= b.tv_usec;
return
a;
}
long
tomicros
(
struct
timeval
x) {
return
x.tv_sec * 1000000ul + x.tv_usec;
}
int
main
() {
struct
timeval
start;
  gettimeofday(&start, 0);
pthread_t
th[THREADS];
for
(
int
i = 0; i < THREADS; ++i)
    pthread_create(&th[i], 0, worker, 0);
for
(
int
i = 0; i < THREADS; ++i)
    pthread_join(th[i], 0);
  assert(g_chores == THREADS * ITERATIONS);
struct
rusage
ru;
struct
timeval
end;
  gettimeofday(&end, 0);
  getrusage(RUSAGE_SELF, &ru);
  printf(
"%16ld us real\n"
"%16ld us user\n"
"%16ld us sys\n"
,
         tomicros(tub(end, start)),
         tomicros(ru.ru_utime),
         tomicros(ru.ru_stime));
}
The reason we care about the contended case, because that's where mutex
implementations show their inequality. Uncontended mutexes usually
perform the same across implementations, and even then you might be
better off with a spin lock, which only takes a few lines:
void
spin_lock
(
atomic_int
*lock) {
if
(atomic_exchange_explicit(lock, 1, memory_order_acquire)) {
for
(;;) {
for
(;;)
if
(!atomic_load_explicit(lock, memory_order_relaxed))
break
;
if
(!atomic_exchange_explicit(lock, 1, memory_order_acquire))
break
;
    }
  }
}
void
spin_unlock
(
atomic_int
*lock) {
  atomic_store_explicit(lock, 0, memory_order_release);
}
Please note that spin locks should really only be used when you have no
other choice. They're useful in kernels, where extreme low level
constraints disallow anything fancy. Spin locks are also a useful
implementation detail in nsync locks. But overall they're bad. I imagine
many developers believe they're good. If so, it's probably because
they've only benchmarked wall time. With locks, it's important to take
CPU time into consideration too. That's why we use
getrusage()
.
Funding for The Fastest Mutex was crowdsourced from Justine
Tunney's
GitHub sponsors
and
Patreon subscribers
, the
backing of
Mozilla's MIECO program
,
and the generous contributions of our
developer community
on
Discord. Your support is what makes projects like Cosmopolitan possible.
Thank you!
