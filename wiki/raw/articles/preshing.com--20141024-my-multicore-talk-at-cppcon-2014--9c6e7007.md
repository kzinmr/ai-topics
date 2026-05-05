---
title: "My Multicore Talk at CppCon 2014"
url: "https://preshing.com/20141024/my-multicore-talk-at-cppcon-2014"
fetched_at: 2026-05-05T07:01:04.828577+00:00
source: "Preshing"
tags: [blog, raw]
---

# My Multicore Talk at CppCon 2014

Source: https://preshing.com/20141024/my-multicore-talk-at-cppcon-2014

Last month, I attended
CppCon
2014 in Bellevue, Washington. It was an awesome conference, filled with the who’s who of C++ development, and loaded with interesting, relevant talks. It was a first-year conference, so I’m sure CppCon 2015 will be even better. I highly recommend it for any serious C++ developer.
While I was there, I gave a talk entitled, “How Ubisoft Montreal Develops Games For Multicore – Before and After C++11.” You can watch the whole thing here:
VIDEO
To summarize the talk:
At Ubisoft Montreal, we exploit multicore by building our game engines on top of three common threading patterns.
To implement those patterns, we need to write a lot of custom concurrent objects.
When a concurrent object is under heavy contention, we optimize it using atomic operations.
Game engines have their own portable atomic libraries. These libraries are similar to the C++11 atomic library’s “low level” functionality.
Most of the talk is spent exploring that last point: Comparing game atomics to low-level C++11 atomics.
There was a wide range of experience levels in the room, which was cool. Among the attendees were Michael Wong, CEO of OpenMP and C++ standard committee member, and Lawrence Crowl, who authored most of section 29, “Atomic operations library,” in the C++11 standard. Both of them chime in at various points. (I certainly wasn’t expecting to explain the standard to the guy who wrote it!)
You can download the slides
here
and grab the source code for the sample application
here
. A couple of corrections about certain points:
Compiler Ordering Around C++ Volatiles
At 24:05, I said that the compiler could have reordered some instructions on x86, leading to the same kind of memory reordering bug we saw at runtime on PowerPC, and that we were just lucky it didn’t.
However, I should acknowledge that in the previous console generation, the only x86 compiler we used at Ubisoft was Microsoft’s. Microsoft’s compiler is exceptional in that it does
not
perform those particular instruction reorderings on x86, because it treats volatile variables differently from other compilers, and
m_writePos
is volatile. That’s Microsoft’s
default x86 behavior
today, and it was its only x86 behavior back then. So in fact, the absence of compiler reordering was more than just luck: It was a vendor-specific guarantee. If we had used GCC or Clang,
then
we would have run the risk of compiler reordering in these two places.
Enforcing Correct Usage of Concurrent Objects
Throughout the talk, I keep returning to the example of a single-producer, single-consumer concurrent queue. For this queue to work correctly, you must follow the rules. In particular, it’s important not to call
tryPush
from multiple threads at the same time.
At 54:00, somebody asks if there’s a way to prevent coworkers from breaking such rules. My answer was to talk to them. At Ubisoft Montreal, the community of programmers playing with lock-free data structures is small, and we tend to know each other, so this answer is actually quite true for us. In many cases, the only person using a lock-free data structure is the one who implemented it.
But there was a better answer to his question, which I didn’t think of at the time: We can implement a macro that fires an assert when two threads enter the same function simultaneously. I won’t show the macro’s implementation here, but as it turns out, the
tryPush
and
tryPop
functions are two perfect candidates for it. This assert won’t prevent people from breaking the rules, but it will help catch errors earlier.
bool
tryPush(
const
T& item)
{
ASSERT_SINGLE_THREADED(m_pushDetector);
int
w = m_writePos.load(memory_order_relaxed);
if
(w >= size)
return
false
;  
    m_items[w] = item;   
    m_writePos.store(w +
1
, memory_order_release);
return
true
;
}
