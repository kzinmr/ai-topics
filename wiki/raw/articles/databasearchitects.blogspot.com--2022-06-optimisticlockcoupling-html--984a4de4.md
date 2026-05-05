---
title: "Making unwinding through JIT-ed code scalable - Optimistic Lock Coupling"
url: "https://databasearchitects.blogspot.com/2022/06/optimisticlockcoupling.html"
fetched_at: 2026-05-05T07:01:28.648779+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Making unwinding through JIT-ed code scalable - Optimistic Lock Coupling

Source: https://databasearchitects.blogspot.com/2022/06/optimisticlockcoupling.html

This article is part of the series about scalable unwinding that starts
here
.
When thinking about exception handling it is reasonable to assume that we will have far more unwinding requests than changes to the unwinding tables. In our setup, the tables only change when JITed code is added to or removed from the program.  That is always expensive to begin with due the mprotect calls, TLB shootdowns, etc. Thus we can safely assume that we will have at most a few hundred updates per second even in extreme cases, probably far less. Lookups however can easily reach thousands or even millions per second, as we do one lookup per frame.
This motivates us to use a read-optimized data structure, a b-tree with optimistic lock coupling: Writers use traditional lock coupling (lock parent node exclusive, lock child node exclusive, release parent node, lock child of child, etc.), which works fine as long as there is not too much contention. Readers however have to do something else, as we expect thousands of them. One might be tempted to use a rw-lock for readers, but that does not help. Locking an rw-lock in shared mode causes an atomic write, which makes the threads fight over the cache line of the lock even if there is no (logical) contention.
Instead, we use version locks, where readers do no write at all:
// Common logic for version locks
struct
version_lock
{
// The lock itself. The lowest bit indicates an exclusive lock,
// the second bit indicates waiting threads. All other bits are
// used as counter to recognize changes.
// Overflows are okay here, we must only prevent overflow to the
// same value within one lock_optimistic/validate
// range. Even on 32 bit platforms that would require 1 billion
// frame registrations within the time span of a few assembler
// instructions.
uintptr_t
version_lock;
};
#ifdef __GTHREAD_HAS_COND
// We should never get contention within the tree as it rarely changes.
// But if we ever do get contention we use these for waiting
static
__gthread_mutex_t
version_lock_mutex
=
__GTHREAD_MUTEX_INIT;
static
__gthread_cond_t
version_lock_cond
=
__GTHREAD_COND_INIT;
#endif
The version lock consists of a single number, where the lower two bits indicate the lock status. As we will see below, for exclusive locks we will use them just like a regular mutex, with the addition that the higher bits are incremented on every unlock. If we do get contention we use version_lock_mutex and version_lock_cond for sleeping, but that should be very rare. For readers we do not modify the lock at all but just remember its state. After the read is finished we check the state again. If it changed, we did a racy read, and try again. Note that such a locking mechanism is sometimes call a
sequence lock
in the literature. The great advantage is that readers can run fully parallel, and the performance is excellent as long as writes are uncommon.
Initialiizing the lock and trying to acquire the lock in exclusive more are straight forward:
// Initialize in locked state
static
inline
void
version_lock_initialize_locked_exclusive
(
struct
version_lock
*
vl)
{
  vl
->
version_lock
=
1
;
}
// Try to lock the node exclusive
static
inline
bool
version_lock_try_lock_exclusive
(
struct
version_lock
*
vl)
{
uintptr_t
state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
if
(state
&
1
)
return
false
;
return
__atomic_compare_exchange_n (
&
(vl
->
version_lock),
&
state, state
|
1
,
false
, __ATOMIC_SEQ_CST,
				      __ATOMIC_SEQ_CST);
}
We simply set the lock to 1 to initialize a new lock in locked state. The try_lock tries to change the lowest bit, and fails if that is not possible.
For blocking lock_exclusive calls we first try the same as try_lock. If that fails, we acquire the mutex, try to lock again, and sleep if we did not get the lock:
// Lock the node exclusive, blocking as needed
static
void
version_lock_lock_exclusive
(
struct
version_lock
*
vl)
{
#ifndef __GTHREAD_HAS_COND
restart:
#endif
// We should virtually never get contention here, as frame
// changes are rare
uintptr_t
state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
if
(
!
(state
&
1
))
    {
if
(__atomic_compare_exchange_n (
&
(vl
->
version_lock),
&
state, state
|
1
,
false
, __ATOMIC_SEQ_CST,
				       __ATOMIC_SEQ_CST))
return
;
    }
// We did get contention, wait properly
#ifdef __GTHREAD_HAS_COND
__gthread_mutex_lock (
&
version_lock_mutex);
  state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
while
(
true
)
    {
// Check if the lock is still held
if
(
!
(state
&
1
))
	{
if
(__atomic_compare_exchange_n (
&
(vl
->
version_lock),
&
state,
					   state
|
1
,
false
, __ATOMIC_SEQ_CST,
					   __ATOMIC_SEQ_CST))
	    {
	      __gthread_mutex_unlock (
&
version_lock_mutex);
return
;
	    }
else
{
continue
;
	    }
	}
// Register waiting thread
if
(
!
(state
&
2
))
	{
if
(
!
__atomic_compare_exchange_n (
&
(vl
->
version_lock),
&
state,
					    state
|
2
,
false
, __ATOMIC_SEQ_CST,
					    __ATOMIC_SEQ_CST))
continue
;
	}
// And sleep
__gthread_cond_wait (
&
version_lock_cond,
&
version_lock_mutex);
      state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
    }
#else
// Spin if we do not have condition variables available
// We expect no contention here, spinning should be okay
goto
restart;
#endif
}
When sleeping we set the second-lowest bit, too, to indicate waiting threads. The unlock function checks that bit, and wakes up the threads if needed:
// Release a locked node and increase the version lock
static
void
version_lock_unlock_exclusive
(
struct
version_lock
*
vl)
{
// increase version, reset exclusive lock bits
uintptr_t
state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
uintptr_t
ns
=
(state
+
4
)
&
(
~
((
uintptr_t
)
3
));
  state
=
__atomic_exchange_n (
&
(vl
->
version_lock), ns, __ATOMIC_SEQ_CST);
#ifdef __GTHREAD_HAS_COND
if
(state
&
2
)
    {
// Wake up waiting threads. This should be extremely rare.
__gthread_mutex_lock (
&
version_lock_mutex);
      __gthread_cond_broadcast (
&
version_lock_cond);
      __gthread_mutex_unlock (
&
version_lock_mutex);
    }
#endif
}
Readers do not modify the lock at all. When they "lock" in shared mode they store the current state, and check if the state is still the same in the validate function:
// Acquire an optimistic "lock". Note that this does not lock at all, it
// only allows for validation later
static
inline
bool
version_lock_lock_optimistic
(
const
struct
version_lock
*
vl,
uintptr_t
*
lock)
{
uintptr_t
state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
*
lock
=
state;
// Acquiring the lock fails when there is currently an exclusive lock
return
!
(state
&
1
);
}
// Validate a previously acquire lock
static
inline
bool
version_lock_validate
(
const
struct
version_lock
*
vl,
uintptr_t
lock)
{
// Prevent the reordering of non-atomic loads behind the atomic load.
// Hans Boehm, Can Seqlocks Get Along with Programming Language Memory
// Models?, Section 4.
__atomic_thread_fence (__ATOMIC_ACQUIRE);
// Check that the node is still in the same state
uintptr_t
state
=
__atomic_load_n (
&
(vl
->
version_lock), __ATOMIC_SEQ_CST);
return
(state
==
lock);
}
We fail early if the lock is currently locked exclusive.
Note that optimistic lock coupling conceptually does the same as classical lock coupling. The main difference is that we have to valid a lock before we can act upon a value that we have read. This means: 1) lock parent, 2) fetch child pointer, 3) validate parent, restart if validation fails, 4) lock child, etc.
In the next article we look at the
b-tree data structure
that we use to store the frames.
