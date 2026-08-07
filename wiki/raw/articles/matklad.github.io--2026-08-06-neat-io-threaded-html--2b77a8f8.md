---
title: "Zig's Io.Threaded is Neat"
url: "https://matklad.github.io/2026/08/06/neat-io-threaded.html"
fetched_at: 2026-08-07T10:19:27.409978+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# Zig's Io.Threaded is Neat

Source: https://matklad.github.io/2026/08/06/neat-io-threaded.html

Zig’s Io.Threaded is Neat
Aug 6, 2026
std.Io.Threaded
is one of the implementations of Zig’s new
Io
interface that enables concurrency. This is a boring
“just use threads” impl. I personally find it neat though — it does this weird thing that
I wanted to do for ages
, that to my knowledge no
one else is doing properly, and implements it better than I thought to be possible.
Io.Threaded
uses blocking syscalls and fully supports cancelation.
Quoting
@tedinski
,
Concurrency is about handling (asynchronous, nondeterministic) events.
Parallelism is about using hardware resources to do more at the same time.
I think this definition is correct, but doesn’t provide useful intuition directly. Concurrency is
the same thing as state transducers? Yes, obviously, but not really illuminating as to how you’d
program the thing.
For intuition, I like these two litmus tests.
First
, parallelism is deterministic or
“declarative”:
use
rayon::prelude::*;
fn
sum_of_squares
(input: &[
i32
])
->
i32
{
input.
par_iter
()
.
map
(|i| i * i)
.
sum
()
}
You describe how to split the problem into independent partitions, and implement a function to
process one partition at a time . It’s platform’s job to verify the partitioning to be correct
(non-racy), process all partitions, and yield control back once that is done.
Second
, concurrency invariably involves cancelation. Whenever you have two asynchronous
computations happening at the same time, there comes a moment when one computation becomes aware
that the second computation is no longer necessary, and must be canceled, actively. In general, it
is not possible to just wait until the other computation completes: often, the reason why you want
to cancel it in the first place is precisely because you’ve learned that it
can’t
complete (e.g.,
it is waiting for a message it will never receive).
And that is the problem with
Well, there are more, the chief being that, while you totally
can
spawn many threads, this often
requires system-wide configuration change, which is a non-starter for most application. But absence
of cancelation really makes you hit a wall sooner or later. The problem are syscalls. It’s easy
enough, in any loopy code, to do something like
while
(
true
) {
if
(is_canceled())
return
error
.Canceld;
...
}
But, the thread is instead blocked inside the syscall in the kernel, programming language APIs
generally doesn’t give any way to unblock it:
const
read_size =
try
read(fd, buffer);
Wouldn’t it be cool if we could just use standard OS threads, blocking APIs, avoid new shinies like
io_uring, but still get to cancel any work reliably? That’s exactly what Zig’s
std.Io.Threaded
provides.
The way this works on POSIX is a bit cursed. Turns out, the kernel actually provides a roundabout
way to cancel a blocking syscall — signals. When a thread is blocked in the kernel, and a signal
is delivered to the thread, the thread is woken up and the syscall returns
EINTR
. It is customary
to just
loop re-try the syscall
in such cases, but one doesn’t have to.
By itself, signals are not a cancelation mechanism — signaling a thread is inherently racy, the
signal might get delivered before the relevant syscall starts, or after it finishes. Conversely, a
syscall might get interrupted by signal unrelated to cancelation.
The actual protocol is that the canceling thread sets a flag in shared memory to request
cancelation, and then signals the cancelee, in a loop, until the cancelation is acknowledged (a
different value for a flag in the shared memory). Upon receiving
EINTR
from a syscall, the thread
potentially being canceled checks the value of the flag and either retries the syscall, or
acknowledges the cancelation and begins unwinding. See
signalCanceledSyscall
and, eg
fileReadPositionalPosix
for the two halves of the protocol.
On the user-side, cancelation request is materialized as
error.Canceled
. Error management as a
feature is a combination of cancelation,
branching, and reporting
,
and Zig implements the first two. Cancelation isn’t an error
not
because it is
serendipitous success
, but
because, vice versa, an error is a cancelation plus a payload.
On Windows, there’s a much more direct
NtCancelSynchronousIoFile
Love the name!. In general, between fibers, IO Completion Ports, Job objects, and this, it seems
that NT has a better thought through concurrency story than Unix.
In Java, there’s a similarly looking thread interruption mechanism. Critically, it doesn’t support
interrupting syscalls:
IOException
and
InterruptedException
are both checked and unrelated,
meaning that IOing functions are not interruptible. In Zig, reader and writer interfaces completely
type erase errors and therefore support cancelation, though this requires some extra care to handle
correctly, on top of the usual
don’t forget to flush
.
pthread_cancel
implements a similar signal+flag machinery. However, it doesn’t integrate with
language-level cancelation (
try
,
defer
) which makes post-cancelation cleanup cumbersome and
slow. More generally, a lot of angst around concurrency steams from a fact that it falls exactly
into the twilight zone between the kernel, the runtime, and the language. There’s almost (interrupts
excepted) no concurrency on the CPU, it’s an illusion with a mixed authorship. The language is
usually the better equipped one to tackle the problem, but, traditionally, it is handled by the
kernel and libc, with adverse effects on language design.
Another problem with
pthread_cancel
is that it tears down the entire thread, which would be an OK
thing to do if threads were cheap. However, creating threads is still slow, and the configured
system limit for a number of threads is typically low, so its usually a good idea to pool OS
threads. Zig’s
Io
solves this problem ingeniously, separating, at the interface level,
“may run concurrently” from “must run concurrently”:
https://kristoff.it/blog/asynchrony-is-not-concurrency/
This achieves an effect similar to that of
std::launch
policy
(item 36 in effective modern
C++, if you have that around). By naming what is happening (
io.async
vs
io.concurrent
), Zig
makes it easier to understand what is actually going on, and also gets more precise signatures
(
concurrent
is always fallible,
async
never is). Of course
concurrent
is backed by a thread
pool, falling back on spawning a fresh thread only when the pool is exhausted.
