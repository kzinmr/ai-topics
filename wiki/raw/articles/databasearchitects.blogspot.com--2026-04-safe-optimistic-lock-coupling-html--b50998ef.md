---
title: "Safe Optimistic Lock Coupling"
url: "https://databasearchitects.blogspot.com/2026/04/safe-optimistic-lock-coupling.html"
fetched_at: 2026-05-05T07:01:27.791048+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Safe Optimistic Lock Coupling

Source: https://databasearchitects.blogspot.com/2026/04/safe-optimistic-lock-coupling.html

As the number of CPU cores keeps growing, the scalability of
concurrent data structures becomes increasingly important. A data
structure that works fine on 4 cores can become a bottleneck on 32, not
because of algorithmic limitations, but because of how it synchronizes
access.
We illustrate that with a simple binary tree. Usually these data
structures are protected by some kind of lock:
struct
Node
{
mutex lock
;
key_type
key
;
value_type
value
;
Node
*
left
,
*
right
;
};
struct
Tree
{
mutex lock
;
Node
*
root
;
};
When searching a value, we can traverse the data structure, lock the
parts of the data we are currently touching, and release locks when we
are done (“lock coupling”):
option
<
value_type
>
Tree
::
lookup
(
key_type
key
)
{
lock
.
lock_shared
();
mutex
*
currentLock
=
&
lock
;
Node
*
iter
=
root
;
option
<
value_type
>
result
;
while
(
iter
)
{
if
(
key
==
iter
->
key
)
{
result
=
iter
->
value
;
break
;
}
Node
*
next
=
(
key
<
iter
->
key
)
?
iter
->
left
:
iter
->
right
;
if
(
next
)
next
->
lock
.
lock_shared
();
currentLock
->
unlock
();
currentLock
=
next
?
&
next
->
lock
:
nullptr
;
iter
=
next
;
}
currentLock
->
unlock
();
return
result
;
}
While conceptually simple, lock coupling has quite poor performance
in practice. The problem is that it creates contention on the locks, in
particular for the root node. Every lookup goes through the root node,
thus the root node is constantly locked and unlocked. While there is no
semantic
contention between lookups, as all readers can read
the root concurrently, there is
physical
contention on the lock
itself, which limits scalability. This can be seen below, with
concurrent lookups in a tree of 100,000 elements, executed on a 16-core
/ 32-thread 9950X3D.
Lookup scalability: no locking vs lock
coupling
This contention problem can be solved by using
Optimistic Lock
Coupling
, a synchronization technique where readers do not perform
any writes. The key idea here is that writers lock as usual, and
increase a version number when they are done updating. Readers read the
version number before access, read the elements they are interested in,
and then re-check the version number. If the version number changed (or
the element is currently locked), the read fails and the reader tries
again. In (slightly simplified) code it looks like this:
struct
Node
{
version_lock lock
;
key_type
key
;
value_type
value
;
Node
*
left
,
*
right
;
};
struct
Tree
{
version_lock lock
;
Node
*
root
;
};
option
<
value_type
>
Tree
::
lookup
(
key_type
key
)
{
restart
:
lock_guard guard
=
lock
.
lock_optimistic
();
Node
*
iter
=
root
;
if
(!
guard
.
validate
())
goto
restart
;
option
<
value_type
>
result
;
while
(
iter
)
{
auto
currentKey
=
iter
->
key
;
if
(!
guard
.
validate
())
goto
restart
;
if
(
key
==
currentKey
)
{
auto
currentValue
=
iter
->
value
;
if
(!
guard
.
validate
())
goto
restart
;
result
=
currentValue
;
break
;
}
iter
=
(
key
<
currentKey
)
?
iter
->
left
:
iter
->
right
;
if
(!
guard
.
validate
())
goto
restart
;
auto
nextGuard
=
iter
->
lock
.
lock_optimistic
();
if
(!
guard
.
validate
())
goto
restart
;
guard
=
nextGuard
;
}
return
result
;
}
It is not that different from the classic lock coupling code above,
except that we always have to check for concurrent writes before acting
on the read values. The great benefit of this strategy is that the
lookup code is purely read-only, which allows it to scale nicely with
the number of cores:
Lookup scalability: all
strategies
While Optimistic Lock Coupling offers excellent performance, it is a
bit dangerous to use. If you act upon a value before validating, you
effectively have a race condition in your code. In this small example it
is clear when we have to validate, but in complex code fragments it is
easy to forget to validate.
The best way to mitigate that is to get compiler support, by encoding
the fact that we need to validate in the type system. We can achieve
that by representing unvalidated values as a dedicated type, and having
only the lock guard expose that value. Conceptually it looks like this
(variants that validate multiple values omitted for simplicity):
template
<
class
T
>
class
unvalidated
{
T value
;
friend
class
lock_guard
;
};
class
lock_guard
{
...
template
<
class
T
>
optional
<
T
>
validate
(
unvalidated
<
T
>
value
);
};
Basically we only allow access to the original value by validating,
which makes that construct safe. But how do we ensure that code properly
wraps everything in
unvalidated<T>
? By exposing only
an
optimistic view
over the data. Conceptually we do the
following:
struct
Node
{
class
OptimisticView
;
...
// as above
};
template
<
class
T
>
class
OptimisticPtr
{
T
*
rawPtr
;
public
:
// We cannot use operator-> here unfortunately due to C++ constraints
typename
T
::
OptimisticView data
()
const
{
return
T
::
OptimisticView
(
rawPtr
);
}
};
// Exposes each member as unvalidated<T> value
class
Node
::
OptimisticView
{
class
Node
*
rawData
;
public
:
unvalidated
<
key_type
>
key
()
{
return
unvalidated
(
atomic_ref
(
rawData
->
key
).
load
(
memory_order_relaxed
));
}
unvalidated
<
value_type
>
value
()
{
return
unvalidated
(
atomic_ref
(
rawData
->
value
).
load
(
memory_order_relaxed
));
}
unvalidated
<
OptimisticPtr
<
Node
>>
left
()
{
return
unvalidated
(
OptimisticPtr
(
atomic_ref
(
rawData
->
left
).
load
(
memory_order_relaxed
)));
}
unvalidated
<
OptimisticPtr
<
Node
>>
right
()
{
return
unvalidated
(
OptimisticPtr
(
atomic_ref
(
rawData
->
right
).
load
(
memory_order_relaxed
)));
}
unvalidated
<
lock_guard
>
lock
()
{
return
unvalidated
(
lock_guard
(
atomic_ref
(
rawData
->
lock
).
load
(
memory_order_seq_cst
)));
}
};
Note that the
lock()
accessor returns an
unvalidated<lock_guard>
: before we can hand off to
the next node’s lock, we must first validate the current guard to ensure
we actually read a valid lock. This ensures that lock acquisition itself
is part of the validated chain.
With this design, the optimistic code only accesses data via an
OptimisticPtr, which makes it impossible to access the data without
prior validation. This greatly improves the robustness of the approach.
It is a bit annoying that we have to manually implement accessor
functions in the OptimisticView, but hopefully the
compiler will do that in the future
automatically
.
Using these abstractions, our lookup code now becomes:
option
<
value_type
>
Tree
::
lookup
(
key_type
key
)
{
restart
:
lock_guard guard
=
lock
.
lock_optimistic
();
auto
iterOpt
=
guard
.
validate
(
getRootOptimistic
());
if
(!
iterOpt
)
goto
restart
;
OptimisticPtr
<
Node
>
iter
=
*
iterOpt
;
option
<
value_type
>
result
;
while
(
iter
)
{
auto
currentKey
=
guard
.
validate
(
iter
.
data
().
key
());
if
(!
currentKey
)
goto
restart
;
if
(
key
==
*
currentKey
)
{
auto
currentValue
=
guard
.
validate
(
iter
.
data
().
value
());
if
(!
currentValue
)
goto
restart
;
result
=
*
currentValue
;
break
;
}
auto
next
=
guard
.
validate
((
key
<
*
currentKey
)
?
iter
.
data
().
left
()
:
iter
.
data
().
right
());
if
(!
next
)
goto
restart
;
iter
=
*
next
;
auto
nextGuard
=
guard
.
validate
(
iter
.
data
().
lock
());
if
(!
nextGuard
)
goto
restart
;
guard
=
*
nextGuard
;
}
return
result
;
}
The code is nearly identical to the unsafe version above, but now it
becomes impossible to forget to validate, as the compiler complains
otherwise. This makes this highly attractive concurrency paradigm robust
and easy to use for all kinds of data structures.
In summary, Optimistic Lock Coupling gives us near-lockfree read
scalability while still supporting safe concurrent writes. And by
encoding validation requirements in the type system, we get the
performance benefits without sacrificing correctness. The compiler
catches the mistakes that would otherwise become subtle race conditions
at runtime.
