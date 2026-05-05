---
title: "Making unwinding through JIT-ed code scalable"
url: "https://databasearchitects.blogspot.com/2022/06/making-unwinding-through-jit-ed-code.html"
fetched_at: 2026-05-05T07:01:28.346852+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Making unwinding through JIT-ed code scalable

Source: https://databasearchitects.blogspot.com/2022/06/making-unwinding-through-jit-ed-code.html

Exceptions are a very handy mechanism to propagate errors in C++ programs, but unfortunately
they do not scale very well
. In all common C++ implementations the unwinding mechanism takes global lock during unwinding, which has disastrous consequences when the number of threads is high. On a machine with 256 hardware context we see worse-than-single-threaded behavior even for relatively modest failure rates.
Fortunately the Florian Weimer fixed one contention point in gcc 12 on systems with glibc 2.35 or newer, which gives us scalable exceptions as long as no JIT-ed code has been registered. Unfortunately our system does register JIT-ed code... Which means exception unwinding in our code base is still single-threaded in practice.
But we can fix that by teaching gcc to store the unwinding information in a read-optimized b-tree, which allows for fully parallel unwinding without any atomic writes. There is a
gcc patch
that does just that, but unfortunately it is quite involved and difficult to review. This article series thus explains all parts of the patch and shows how a read-optimized b-tree can be implemented lock-free.
In order to keep the article length somewhat reasonable, the discusses is broken into parts:
The problem (this article)
Replacing the gcc hooks
Optimistic Lock Coupling
The b-tree
b-tree operations
When unwinding exceptions, the compiler has to find the corresponding unwinding information for every call frame on the stack between the throw and the catch. gcc uses two different mechanisms for that: For ahead-of-time compiled code it asks glibc to find the unwinding information using either dl_iterate_phdr (on older systems) or _dl_find_object (on systems with glibc 2.35 or newer). Note that this mapping is not static, as shared libraries could be added or removed at any time, potentially during a concurrent unwind. For that reason dl_iterate_phdr was protected by a global mutex, which clearly does not scale. _dl_find_object avoids that mutex by using a lock-free data structure. But that only affects ahead-of-time compiled code, for JITed code libgcc uses
a different mechanism
, which we now discuss:
For JITed code the emitter has to explicitly register the unwinding information using
__register_frame_info_bases (and the very similar
__register_frame_info_table_bases):
void
__register_frame_info_bases
(
const
void
*
begin,
struct
object
*
ob,
void
*
tbase,
void
*
dbase)
{
/* If .eh_frame is empty, don't register at all.  */
if
((
const
uword
*
) begin
==
0
||
*
(
const
uword
*
) begin
==
0
)
return
;

  ob
->
pc_begin
=
(
void
*
)
-
1
;
  ob
->
tbase
=
tbase;
  ob
->
dbase
=
dbase;
  ob
->
u.single
=
begin;
  ob
->
s.i
=
0
;
  ob
->
s.b.encoding
=
DW_EH_PE_omit;
#ifdef DWARF2_OBJECT_END_PTR_EXTENSION
ob
->
fde_end
=
NULL
;
#endif
init_object_mutex_once ();
  __gthread_mutex_lock (
&
object_mutex);

  ob
->
next
=
unseen_objects;
  unseen_objects
=
ob;
#ifdef ATOMIC_FDE_FAST_PATH
/* Set flag that at least one library has registered FDEs.
Use relaxed MO here, it is up to the app to ensure that the library
loading/initialization happens-before using that library in other
threads (in particular unwinding with that library's functions
appearing in the backtraces).  Calling that library's functions
without waiting for the library to initialize would be racy.  */
if
(
!
any_objects_registered)
    __atomic_store_n (
&
any_objects_registered,
1
, __ATOMIC_RELAXED);
#endif
__gthread_mutex_unlock (
&
object_mutex);
}
Which conceptually is a simple thing: It grabs a mutex, puts the object information into a list, and released the mutex. Note the code within the
ATOMIC_FDE_FAST_PATH
block: As we will see below, that unwinding mechanism is very slow. Thus, libgcc tries to avoid taking that path by remembering if any JITed code was registered at all. If not, it stops unwinding immediately. But that mechanism does not help if we do have JITed code.
During unwinding, the unwinder calls
_Unwind_Find_FDE,
which traverses the list in order to find the corresponding unwind table for the given address:
const
fde
*
_Unwind_Find_FDE
(
void
*
pc,
struct
dwarf_eh_bases
*
bases)
{
struct
object
*
ob;
const
fde
*
f
=
NULL
;
#ifdef ATOMIC_FDE_FAST_PATH
/* For targets where unwind info is usually not registered through these
APIs anymore, avoid taking a global lock.
Use relaxed MO here, it is up to the app to ensure that the library
loading/initialization happens-before using that library in other
threads (in particular unwinding with that library's functions
appearing in the backtraces).  Calling that library's functions
without waiting for the library to initialize would be racy.  */
if
(__builtin_expect (
!
__atomic_load_n (
&
any_objects_registered,
					  __ATOMIC_RELAXED),
1
))
return
NULL
;
#endif
init_object_mutex_once ();
  __gthread_mutex_lock (
&
object_mutex);
/* Linear search through the classified objects, to find the one
containing the pc.  Note that pc_begin is sorted descending, and
we expect objects to be non-overlapping.  */
for
(ob
=
seen_objects; ob; ob
=
ob
->
next)
if
(pc
>=
ob
->
pc_begin)
      {
	f
=
search_object (ob, pc);
if
(f)
goto
fini;
break
;
      }
/* Classify and search the objects we've not yet processed.  */
while
((ob
=
unseen_objects))
    {
struct
object
**
p;

      unseen_objects
=
ob
->
next;
      f
=
search_object (ob, pc);
/* Insert the object into the classified list.  */
for
(p
=
&
seen_objects;
*
p ; p
=
&
(
*
p)
->
next)
if
((
*
p)
->
pc_begin
<
ob
->
pc_begin)
break
;
      ob
->
next
=
*
p;
*
p
=
ob;
if
(f)
goto
fini;
    }
fini:
__gthread_mutex_unlock (
&
object_mutex);
if
(f)
    {
int
encoding;
      _Unwind_Ptr func;

      bases
->
tbase
=
ob
->
tbase;
      bases
->
dbase
=
ob
->
dbase;

      encoding
=
ob
->
s.b.encoding;
if
(ob
->
s.b.mixed_encoding)
	encoding
=
get_fde_encoding (f);
      read_encoded_value_with_base (encoding, base_from_object (encoding, ob),
				    f
->
pc_begin,
&
func);
      bases
->
func
=
(
void
*
) func;
    }
return
f;
}
In the fast path it tries to stop early if no unwinding information had been registered. But if any unwinding frame has been registered by JITed code, it grabs the global object_mutex and does everything effectively single-threaded. This does not scale. Thus, we discuss how to switch gcc to a lock-free lookup structure in the
next article
.
