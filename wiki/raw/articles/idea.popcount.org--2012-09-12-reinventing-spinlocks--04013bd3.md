---
title: "Reinventing spinlocks"
url: "https://idea.popcount.org/2012-09-12-reinventing-spinlocks"
fetched_at: 2026-05-05T07:01:14.183345+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Reinventing spinlocks

Source: https://idea.popcount.org/2012-09-12-reinventing-spinlocks

Reinventing spinlocks
12 September 2012
In the previous article I was playing with
the implementation of the concurrent Queue in C
.
During the experiments I tried to outsmart
pthread
library and beat
the speed of their spinlock implementation.
CAS/CAS
My first attempt was to use compare-and-swap
CAS
instruction for the
spinlock. Here's the code, basically we spin till the lock is acquired:
static
inline
void
_lock
(
unsigned
int
*
lock
)
{
while
(
1
)
{
int
i
;
for
(
i
=
0
;
i
<
10000
;
i
++
)
{
if
(
__sync_bool_compare_and_swap
(
lock
,
0
,
1
))
{
return
;
}
}
sched_yield
();
}
}
static
inline
void
_unlock
(
unsigned
int
*
lock
)
{
__sync_bool_compare_and_swap
(
lock
,
1
,
0
);
}
This approach works well, but we can still do better.
(
full code
)
CAS/store
It's easy to notice that the
unlock
doesn't actually need the heavy
CAS
write. We know that the value in the lock must be 1 and we can
just unconditionally write 0.
static
inline
void
_unlock
(
unsigned
int
*
lock
)
{
__asm__
__volatile__
(
""
:::
"memory"
);
*
lock
=
0
;
}
The asm line is required to prevent GCC from reordering the
write. Additionally, in x86 the stores aren't reordered, but in other
architectures a write barrier might be required above the assignment.
(
full code
)
Benchmark
I used the
benchmark
from
previous blog post
to get
the numbers. Beware, the locks are only a fraction of the measured
complexity in these benchmarks.
The numbers for four threads spinning on four cores (ie: contended case):
And a single thread (uncontended case):
The
CAS/store
method is as fast as pthread implementation of
spinlocks. That's nothing really surprising considering that pthread
also uses the same approach
(
source
).
So now you know how to implement reasonable spinlocks. This may come
handy for example when you're writing for a platform with glibc that
doesn't have
pthread_spin_lock
, like Mac OS X. Here's the shim for
that case:
int
pthread_spin_init
(
pthread_spinlock_t
*
lock
,
int
pshared
)
{
__asm__
__volatile__
(
""
:::
"memory"
);
*
lock
=
0
;
return
0
;
}
int
pthread_spin_destroy
(
pthread_spinlock_t
*
lock
)
{
return
0
;
}
int
pthread_spin_lock
(
pthread_spinlock_t
*
lock
)
{
while
(
1
)
{
int
i
;
for
(
i
=
0
;
i
<
10000
;
i
++
)
{
if
(
__sync_bool_compare_and_swap
(
lock
,
0
,
1
))
{
return
0
;
}
}
sched_yield
();
}
}
int
pthread_spin_trylock
(
pthread_spinlock_t
*
lock
)
{
if
(
__sync_bool_compare_and_swap
(
lock
,
0
,
1
))
{
return
0
;
}
return
EBUSY
;
}
int
pthread_spin_unlock
(
pthread_spinlock_t
*
lock
)
{
__asm__
__volatile__
(
""
:::
"memory"
);
*
lock
=
0
;
return
0
;
}
(
full source
)
Alternatively,
ConcurrencyKit
is a high-quality library that provides loads of concurrency primitives, including spinlocks:
