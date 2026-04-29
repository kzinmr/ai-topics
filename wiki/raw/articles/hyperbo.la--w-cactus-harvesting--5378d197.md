---
title: "Cactus Harvesting: Cycle-Aware Reference Counting in Rust"
url: "https://hyperbo.la/w/cactus-harvesting/"
fetched_at: 2026-04-29T07:02:15.647080+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Cactus Harvesting: Cycle-Aware Reference Counting in Rust

Source: https://hyperbo.la/w/cactus-harvesting/

🌵 CactusRef is a single-threaded, cycle-aware, reference counting smart pointer
[
docs
] [
code
]. CactusRef is nearly a drop-in replacement for
std::rc
from the Rust standard library. (CactusRef implements all
std::rc::Rc
APIs
except for
std::rc::Rc::downcast
,
CoerceUnsized
, and
DispatchFromDyn
.) Throughout this post,
Rc
refers to
cactusref::Rc
. I
will refer to
std::rc::Rc
with its fully qualified name.
Motivation
Building cyclic data structures in Rust is
hard
. When a
T
needs to have
multiple owners, it can be wrapped in a
std::rc::Rc
.
std::rc::Rc
, however,
is not cycle-aware. Creating a cycle of
std::rc::Rc
s will leak memory. To work
around this, an
std::rc::Rc
can be
downgraded
into a
std::rc::Weak
.
std::rc::Rc
Limitations
Strong references are much more convenient to work with than weak references.
Imagine the following code (written in Ruby) to create a ring:
class
Node
attr_accessor
:next
end
def
ring
n1
=
Node
.
new
n2
=
Node
.
new
n3
=
Node
.
new
n1.
next
=
n2
n2.
next
=
n3
n3.
next
=
n1
n1
end
head
=
ring
This code is quite difficult to write with
std::rc::Rc
and
std::rc::Weak
because the ring wants to own references. If we used
std::rc::Weak
to
implement
next
, after
ring
returns,
n2
and
n3
would be dropped and the
std::rc::Weak
s in the object graph would be dangling.
n1
,
n2
, and
n3
form a cycle. This cycle is
reachable
because
n1
is
also bound to the variable
head
. The strong count of
n1
is two, which is
greater than the number of times it is owned by nodes in the cycle (only
n3
owns
n1
).
n2
and
n3
should not be deallocated because they are in a cycle
with
n1
. Because
n1
is externally reachable, the entire cycle is externally
reachable.
If we instead write this code:
head
=
ring
head
=
nil
# the cycle is unreachable and should be deallocated
The cycle is
orphaned
because the only strong references to nodes in the cycle
come from other nodes in the cycle. The cycle is safe to deallocate and should
be reaped.
Rust Example: Doubly Linked List
CactusRef can be used to
implement a doubly linked list
with ergonomic strong
references. The list is deallocated when the
list
binding is dropped because
the linked list is no longer externally reachable.
use
cactusref
::
{
Adoptable
,
Rc
};
use
std
::
cell
::
RefCell
;
use
std
::
iter;
struct
Node
<
T
> {
pub
prev
:
Option
<
Rc
<
RefCell
<
Self
>>>,
pub
next
:
Option
<
Rc
<
RefCell
<
Self
>>>,
pub
data
:
T
,
}
struct
List
<
T
> {
pub
head
:
Option
<
Rc
<
RefCell
<
Node
<
T
>>>>,
}
impl
<
T
>
List
<
T
> {
fn
pop
(
&mut
self
)
->
Option
<
Rc
<
RefCell
<
Node
<
T
>>>> {
let
head
=
self
.
head
.
take
()
?
;
let
tail
=
head
.
borrow_mut
()
.
prev
.
take
();
let
next
=
head
.
borrow_mut
()
.
next
.
take
();
if
let
Some
(
ref
tail)
=
tail {
Rc
::
unadopt
(
&
head,
&
tail);
Rc
::
unadopt
(
&
tail,
&
head);
tail
.
borrow_mut
()
.
next
=
next
.
as_ref
()
.
map
(
Rc
::
clone);
if
let
Some
(
ref
next)
=
next {
Rc
::
adopt
(tail, next);
}
}
if
let
Some
(
ref
next)
=
next {
Rc
::
unadopt
(
&
head,
&
next);
Rc
::
unadopt
(
&
next,
&
head);
next
.
borrow_mut
()
.
prev
=
tail
.
as_ref
()
.
map
(
Rc
::
clone);
if
let
Some
(
ref
tail)
=
tail {
Rc
::
adopt
(next, tail);
}
}
self
.
head
=
next;
Some
(head)
}
}
impl
<
T
>
From
<
Vec
<
T
>>
for
List
<
T
> {
fn
from
(list
:
Vec
<
T
>)
->
Self
{
let
nodes
=
list
.
into_iter
()
.
map
(
|
data
|
{
Rc
::
new
(
RefCell
::
new
(
Node
{
prev
:
None
,
next
:
None
,
data,
}))
})
.
collect
::
<
Vec
<_>>();
for
i
in
0
..
nodes
.
len
()
-
1
{
let
curr
=
&
nodes[i];
let
next
=
&
nodes[i
+
1
];
curr
.
borrow_mut
()
.
next
=
Some
(
Rc
::
clone
(next));
next
.
borrow_mut
()
.
prev
=
Some
(
Rc
::
clone
(curr));
Rc
::
adopt
(curr, next);
Rc
::
adopt
(next, curr);
}
let
tail
=
&
nodes[nodes
.
len
()
-
1
];
let
head
=
&
nodes[
0
];
tail
.
borrow_mut
()
.
next
=
Some
(
Rc
::
clone
(head));
head
.
borrow_mut
()
.
prev
=
Some
(
Rc
::
clone
(tail));
Rc
::
adopt
(tail, head);
Rc
::
adopt
(head, tail);
let
head
=
Rc
::
clone
(head);
Self
{ head
:
Some
(head) }
}
}
let
list
=
iter
::
repeat
(())
.
map
(
|
_
|
"a"
.
repeat
(
1024
*
1024
))
.
take
(
10
)
.
collect
::
<
Vec
<_>>();
let
mut
list
=
List
::
from
(list);
let
head
=
list
.
pop
()
.
unwrap
();
assert_eq!
(
Rc
::
strong_count
(
&
head),
1
);
assert_eq!
(list
.
head
.
as_ref
()
.
map
(
Rc
::
strong_count),
Some
(
3
));
let
weak
=
Rc
::
downgrade
(
&
head);
drop
(head);
assert!
(weak
.
upgrade
()
.
is_none
());
drop
(list);
// all memory consumed by the list nodes is reclaimed.
CactusRef Implementation
There are two magic pieces to CactusRef:
Rc
adoption and the cycle-busting
Drop
implementation.
Adoption
When an
Rc<T>
takes and holds an owned reference to another
Rc<T>
, calling
Rc::adopt
performs bookkeeping to build a graph of reachable objects. There
is an unlinking API,
Rc::unadopt
, which removes a reference from the graph.
An
Rc<T>
is able to adopt another
Rc<T>
multiple times. An
Rc<T>
is able
to adopt
itself
multiple times. Together, these behaviors allow implementing
the following Ruby structure:
ary
=
[]
# => []
hash
=
{ ary => ary }
# => {[]=>[]}
hash[hash]
=
hash
# => {[]=>[], {...}=>{...}}
ary
<<
hash
<<
hash
<<
ary
<<
ary
# => [{[...]=>[...], {...}=>{...}}, {[...]=>[...], {...}=>{...}}, [...], [...]]
hash
=
nil
ary
=
nil
# all structures are deallocated
This bookkeeping is implemented as a set of forward (owned) and backward (owned
by) links stored on the data structure that backs the
Rc
(called an
RcBox
).
Drop
There are three states that
Rc
needs to deal with on
Drop
in this order:
Rc
is unreachable and does not own any others. In this case,
Rc::strong_count
is zero and the set of forward links is empty.
Rc
is part of an orphaned cycle. In this case,
Rc::strong_count
is
greater than zero and the
Rc
has some forward or back links.
Rc
is unreachable and has adopted links. In this case,
Rc::strong_count
is zero and the set of forward links is non-empty.
Each case is implemented with these steps:
Bust forward and back links on this
Rc
’s back links.
Bust forward and back links on this
Rc
.
Mark all reachable
Rc
s as killed.
Drop strong references.
Decrement the implicit “strong weak” pointer.
Deallocate.
The interesting case is state 2 which requires knowing whether this
Rc
is part
of an
orphaned cycle
.
Drop
detects whether this
Rc
is a member of a cycle
by performing breadth first search over the total set of forward and back links
in the object graph. The cycle detection algorithm tracks the reachability of
each node in the cycle by other cycle members. Forward links contribute toward
reachability. Backward references do not contribute but are added to the set of
nodes to traverse in the reachability analysis. Cycle detection is
O(links)
where links is the number of active adoptions.
To determine whether the cycle is orphaned, the intra-cycle ownership counts are
compared to the strong count of each node. If the strong count for a node is
greater than the number of links the cycle has to that node, the node is
externally reachable and the cycle is not orphaned. Detecting an orphaned cycle
is
O(links + nodes)
where links is the number of active adoptions and nodes is
the number of
Rc
s in the cycle.
Deallocating an orphaned cycle
is
fun
and filled with unsafe peril. It is
guaranteed that at least one other object in the cycle owns a reference to this
Rc
, so as we deallocate members of the cycle, this
Rc
will be dropped again.
Dropping this
Rc
multiple times is good because it manages decrementing the
strong count of this
Rc
automatically. This ensures that any outstanding
Weak
pointers detect that they are dangling and return
None
on
Weak::upgrade
. However, it will also certainly result in a
double-free or
use-after-free
if we are not careful.
To avoid a double-free, the
RcBox
includes a
usize
field called
tombstone
.
When we attempt to drop an
Rc
in the cycle we
mark it as killed
. Subsequent
calls to
drop
on killed
Rc
s early return after decrementing the strong
count.
To avoid a use-after-free, on drop, an
Rc
removes itself from all link
tables
so it is not used for cycle detection.
To do the deallocation,
drop the
values
in the
Rc
s
instead of the
Rc
s.
This breaks the cycle during the deallocation and allows
Drop
to crawl the
object graph.
Cycle Detection Is a Zero-Cost Abstraction
Cycle detection is a zero-cost abstraction. If you never
use cactusref::Adoptable;
,
Drop
uses the same implementation as
std::rc::Rc
(and leaks in the same way as
std::rc::Rc
if you form a cycle of
strong references). The only costs you pay are the memory costs of one
Cell<usize>
for preventing double frees, two empty
RefCell
<
HashMap
<NonNull<T>, usize>>
for tracking adoptions, and an
if statement to check if these structures are empty on
drop
.
Next Steps
I am
implementing a Ruby
💎 in Rust and CactusRef will be used to implement
the heap. CactusRef allows Ruby objects to own strong references to their
subordinate members (like instance variables, keys and values in the case of a
Hash
, items in the case of an
Array
, class, ancestor chain, and bound
methods) and be automatically reaped once they become unreachable in the VM.
CactusRef allows implementing a Ruby without a garbage collector, although if
you squint, CactusRef implements a tracing garbage collector using Rust’s
built-in memory management.
Thank you
Stephen
and
Nelson
for helping me think hard about algorithms. 😄
Thank you to the segfaults along the way for helping me find bugs in the cycle
detection and drop implementations. 😱
