---
title: "C++ futures part 5: std::future and std::shared_future"
url: "https://devblogs.microsoft.com/oldnewthing/20261016-00/?p=112778/"
fetched_at: 2026-10-17T10:05:41.268118+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# C++ futures part 5: std::future and std::shared_future

Source: https://devblogs.microsoft.com/oldnewthing/20261016-00/?p=112778/

Wrapping up our quick introduction to the C++ futures library
, we come to the last two parts:
std::
future
and
std::
shared_future
.
The
std::
future
is the starting point. It is a move-only class that this takes the
source
and forwards its
wait
and
wait_for
methods to the
source
, and forwards its
get
method to
consume
.
Forwarding the
get
to
consume
means that you can call
get
only once.
The idea is that
std::
future
is for the case where there is exactly one consumer of the value. Since it is move-only, you can’t copy it; you can only give it away and transfer the power to retrieve the value to the recipient.
The
std::
future
has a method called
shared()
. This transfers the
source
from the
future
to a
shared_
future
object. The
shared_
future
also forwards its
wait
and
wait_for
methods to the
source
, but instead of forwarding its
get
to the
source::
consume
,
shared_
future::
get()
just calls
source::
get
to get a reference to the value storage.
This is what makes the “shared future” shared: The
shared_
future
is copyable, so you can have multiple people all with their own
shared_
future
that share the same
source
, and each one can separately wait for the value and retrieve the value as many times as they want.
The downside of
shared_
future
is that you always get a const reference, so if you want to perform non-const operations on the result, you’ll have to make a copy and operate on the copy. And that’s not possible at all if the result is itself a move-only type, since you can’t move out of a const reference.
You can see that at the end of the day, all of the pieces of the futures library are just different ways of manipulating the invisible
source
. Some components push values into the
source
, and others pull values out of the
source
.
It took me a while to realize that the most important part of the whole futures library is something you can’t even see.
Bonus chatter
: All the names in the futures library are horrible. I mean, really, “packaged task”?
Here’s my attempt to give the pieces better names:
Old name
New name
promise
promise_source
packaged_task
function_promise_source
async(deferred)
make_lazy_promise
async(async)
make_thread_promise
future
promise
shared_future
shared_promise
I admit, these names aren’t all that good either. But I prefer to use the word “promise” to refer to the thing that “promises” to produce a value. And the pattern
promise_source
/
promise
makes the relationship between the two much clearer: A promise source is a thing that makes promises. And it avoids the hilarity of a non-async
async()
.
