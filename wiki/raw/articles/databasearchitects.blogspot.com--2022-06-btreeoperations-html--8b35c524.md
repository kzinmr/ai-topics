---
title: "Making unwinding through JIT-ed code scalable - b-tree operations"
url: "https://databasearchitects.blogspot.com/2022/06/btreeoperations.html"
fetched_at: 2026-05-05T07:01:28.261860+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Making unwinding through JIT-ed code scalable - b-tree operations

Source: https://databasearchitects.blogspot.com/2022/06/btreeoperations.html

This article is part of the series about scalable unwinding that starts
here
.
Now that we have all infrastructure in place, we look at the high-level algorithms. For inserts, we walk down the tree until we hit the leaf-node that should contain the new value. If that node is full, we split the leaf node, and insert a new separator into the parent node to distinguish the two nodes. To avoid propagating that split further up (as the inner node might be full, too, requiring an inner split), we eagerly split full inner nodes when walking down. This guarantees that the parent of a node is never full, which allows us to look at nodes purely from top-to-bottom, which greatly simplifies locking.
The splits themselves are relatively simple, we just copy the right half of each node into a new node, reduce the size of the original node, and insert a separator into the parent. However two problems require some care 1) we might have to split the root, which does not have a parent itself, and 2) the node split could mean that the value we try to insert could be either in the left or the right node. The split functions always update the node iterator to the correct node, and release the lock on the node that is not needed after the split.
// Insert a new separator after splitting
static
void
btree_node_update_separator_after_split
(
struct
btree_node
*
n,
uintptr_t
old_separator,
uintptr_t
new_separator,
struct
btree_node
*
new_right)
{
unsigned
slot
=
btree_node_find_inner_slot (n, old_separator);
for
(
unsigned
index
=
n
->
entry_count; index
>
slot;
--
index)
    n
->
content.children[index]
=
n
->
content.children[index
-
1
];
  n
->
content.children[slot].separator
=
new_separator;
  n
->
content.children[slot
+
1
].child
=
new_right;
  n
->
entry_count
++
;
}
// Check if we are splitting the root
static
void
btree_handle_root_split
(
struct
btree
*
t,
struct
btree_node
**
node,
struct
btree_node
**
parent)
{
// We want to keep the root pointer stable to allow for contention
// free reads. Thus, we split the root by first moving the content
// of the root node to a new node, and then split that new node
if
(
!*
parent)
    {
// Allocate a new node, this guarantees us that we will have a parent
// afterwards
struct
btree_node
*
new_node
=
btree_allocate_node (t, btree_node_is_inner (
*
node));
struct
btree_node
*
old_node
=
*
node;
      new_node
->
entry_count
=
old_node
->
entry_count;
      new_node
->
content
=
old_node
->
content;
      old_node
->
content.children[
0
].separator
=
max_separator;
      old_node
->
content.children[
0
].child
=
new_node;
      old_node
->
entry_count
=
1
;
      old_node
->
type
=
btree_node_inner;
*
parent
=
old_node;
*
node
=
new_node;
    }
}
// Split an inner node
static
void
btree_split_inner
(
struct
btree
*
t,
struct
btree_node
**
inner,
struct
btree_node
**
parent,
uintptr_t
target)
{
// Check for the root
btree_handle_root_split (t, inner, parent);
// Create two inner node
uintptr_t
right_fence
=
btree_node_get_fence_key (
*
inner);
struct
btree_node
*
left_inner
=
*
inner;
struct
btree_node
*
right_inner
=
btree_allocate_node (t,
true
);
unsigned
split
=
left_inner
->
entry_count
/
2
;
  right_inner
->
entry_count
=
left_inner
->
entry_count
-
split;
for
(
unsigned
index
=
0
; index
<
right_inner
->
entry_count;
++
index)
    right_inner
->
content.children[index]
=
left_inner
->
content.children[split
+
index];
  left_inner
->
entry_count
=
split;
uintptr_t
left_fence
=
btree_node_get_fence_key (left_inner);
  btree_node_update_separator_after_split (
*
parent, right_fence, left_fence,
					   right_inner);
if
(target
<=
left_fence)
    {
*
inner
=
left_inner;
      btree_node_unlock_exclusive (right_inner);
    }
else
{
*
inner
=
right_inner;
      btree_node_unlock_exclusive (left_inner);
    }
}
// Split a leaf node
static
void
btree_split_leaf
(
struct
btree
*
t,
struct
btree_node
**
leaf,
struct
btree_node
**
parent,
uintptr_t
fence,
uintptr_t
target)
{
// Check for the root
btree_handle_root_split (t, leaf, parent);
// Create two leaf node
uintptr_t
right_fence
=
fence;
struct
btree_node
*
left_leaf
=
*
leaf;
struct
btree_node
*
right_leaf
=
btree_allocate_node (t,
false
);
unsigned
split
=
left_leaf
->
entry_count
/
2
;
  right_leaf
->
entry_count
=
left_leaf
->
entry_count
-
split;
for
(
unsigned
index
=
0
; index
!=
right_leaf
->
entry_count;
++
index)
    right_leaf
->
content.entries[index]
=
left_leaf
->
content.entries[split
+
index];
  left_leaf
->
entry_count
=
split;
uintptr_t
left_fence
=
right_leaf
->
content.entries[
0
].base
-
1
;
  btree_node_update_separator_after_split (
*
parent, right_fence, left_fence,
					   right_leaf);
if
(target
<=
left_fence)
    {
*
leaf
=
left_leaf;
      btree_node_unlock_exclusive (right_leaf);
    }
else
{
*
leaf
=
right_leaf;
      btree_node_unlock_exclusive (left_leaf);
    }
}
// Insert an entry
static
bool
btree_insert
(
struct
btree
*
t,
uintptr_t
base,
uintptr_t
size,
struct
object
*
ob)
{
// Sanity check
if
(
!
size)
return
false
;
// Access the root
struct
btree_node
*
iter,
*
parent
=
NULL
;
  {
    version_lock_lock_exclusive (
&
(t
->
root_lock));
    iter
=
t
->
root;
if
(iter)
      {
	btree_node_lock_exclusive (iter);
      }
else
{
	t
->
root
=
iter
=
btree_allocate_node (t,
false
);
      }
    version_lock_unlock_exclusive (
&
(t
->
root_lock));
  }
// Walk down the btree with classic lock coupling and eager splits.
// Strictly speaking this is not performance optimal, we could use
// optimistic lock coupling until we hit a node that has to be modified.
// But that is more difficult to implement and frame registration is
// rare anyway, we use simple locking for now
uintptr_t
fence
=
max_separator;
while
(btree_node_is_inner (iter))
    {
// Use eager splits to avoid lock coupling up
if
(iter
->
entry_count
==
max_fanout_inner)
	btree_split_inner (t,
&
iter,
&
parent, base);
unsigned
slot
=
btree_node_find_inner_slot (iter, base);
if
(parent)
	btree_node_unlock_exclusive (parent);
      parent
=
iter;
      fence
=
iter
->
content.children[slot].separator;
      iter
=
iter
->
content.children[slot].child;
      btree_node_lock_exclusive (iter);
    }
// Make sure we have space
if
(iter
->
entry_count
==
max_fanout_leaf)
    btree_split_leaf (t,
&
iter,
&
parent, fence, base);
if
(parent)
    btree_node_unlock_exclusive (parent);
// Insert in node
unsigned
slot
=
btree_node_find_leaf_slot (iter, base);
if
((slot
<
iter
->
entry_count)
&&
(iter
->
content.entries[slot].base
==
base))
    {
// duplicate entry, this should never happen
btree_node_unlock_exclusive (iter);
return
false
;
    }
for
(
unsigned
index
=
iter
->
entry_count; index
>
slot;
--
index)
    iter
->
content.entries[index]
=
iter
->
content.entries[index
-
1
];
struct
leaf_entry
*
e
=
&
(iter
->
content.entries[slot]);
  e
->
base
=
base;
  e
->
size
=
size;
  e
->
ob
=
ob;
  iter
->
entry_count
++
;
  btree_node_unlock_exclusive (iter);
return
true
;
}
Deletion is more complex, as there are more cases. We have to maintain the invariant that each node is at least half full. Just like insertion we have the problem that operations can trickle up, e.g., deleting in element in a node might make it less than half-full, merging that node with a half-full neighbor deletes an entry from the parent, which can make that node less than half-full, etc. We solve that problem by merging while going down: When traversing the tree during element-removal, we check if the current node is less than half full. If yes, we merge/balance it with a neighbor node. If the parent becomes less than half-full that will be fixed at the next traversal. Strictly speaking this means nodes can, at least temporarily, be less than half full, but that is fine for asymptotic complexity, as we are never more than one element below the threshold.
The merge logic examines that least-full neighbor of the current code. If both nodes together would fit in one node, they are merged and the separator for the left node is removed from the parent. Otherwise, elements are shifted from the less-full node to the other node, which makes both nodes at least half full. The separator of the left node is updated after the shift:
// Merge (or balance) child nodes
static
struct
btree_node
*
btree_merge_node
(
struct
btree
*
t,
unsigned
child_slot,
struct
btree_node
*
parent,
uintptr_t
target)
{
// Choose the emptiest neighbor and lock both. The target child is already
// locked
unsigned
left_slot;
struct
btree_node
*
left_node,
*
right_node;
if
((child_slot
==
0
)
||
(((child_slot
+
1
)
<
parent
->
entry_count)
&&
(parent
->
content.children[child_slot
+
1
].child
->
entry_count
<
parent
->
content.children[child_slot
-
1
].child
->
entry_count)))
    {
      left_slot
=
child_slot;
      left_node
=
parent
->
content.children[left_slot].child;
      right_node
=
parent
->
content.children[left_slot
+
1
].child;
      btree_node_lock_exclusive (right_node);
    }
else
{
      left_slot
=
child_slot
-
1
;
      left_node
=
parent
->
content.children[left_slot].child;
      right_node
=
parent
->
content.children[left_slot
+
1
].child;
      btree_node_lock_exclusive (left_node);
    }
// Can we merge both nodes into one node?
unsigned
total_count
=
left_node
->
entry_count
+
right_node
->
entry_count;
unsigned
max_count
=
btree_node_is_inner (left_node)
?
max_fanout_inner
:
max_fanout_leaf;
if
(total_count
<=
max_count)
    {
// Merge into the parent?
if
(parent
->
entry_count
==
2
)
	{
// Merge children into parent. This can only happen at the root
if
(btree_node_is_inner (left_node))
	    {
for
(
unsigned
index
=
0
; index
!=
left_node
->
entry_count;
++
index)
		parent
->
content.children[index]
=
left_node
->
content.children[index];
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count;
++
index)
		parent
->
content.children[index
+
left_node
->
entry_count]
=
right_node
->
content.children[index];
	    }
else
{
	      parent
->
type
=
btree_node_leaf;
for
(
unsigned
index
=
0
; index
!=
left_node
->
entry_count;
++
index)
		parent
->
content.entries[index]
=
left_node
->
content.entries[index];
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count;
++
index)
		parent
->
content.entries[index
+
left_node
->
entry_count]
=
right_node
->
content.entries[index];
	    }
	  parent
->
entry_count
=
total_count;
	  btree_release_node (t, left_node);
	  btree_release_node (t, right_node);
return
parent;
	}
else
{
// Regular merge
if
(btree_node_is_inner (left_node))
	    {
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count;
++
index)
		left_node
->
content.children[left_node
->
entry_count
++
]
=
right_node
->
content.children[index];
	    }
else
{
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count;
++
index)
		left_node
->
content.entries[left_node
->
entry_count
++
]
=
right_node
->
content.entries[index];
	    }
	  parent
->
content.children[left_slot].separator
=
parent
->
content.children[left_slot
+
1
].separator;
for
(
unsigned
index
=
left_slot
+
1
; index
+
1
<
parent
->
entry_count;
++
index)
	    parent
->
content.children[index]
=
parent
->
content.children[index
+
1
];
	  parent
->
entry_count
--
;
	  btree_release_node (t, right_node);
	  btree_node_unlock_exclusive (parent);
return
left_node;
	}
    }
// No merge possible, rebalance instead
if
(left_node
->
entry_count
>
right_node
->
entry_count)
    {
// Shift from left to right
unsigned
to_shift
=
(left_node
->
entry_count
-
right_node
->
entry_count)
/
2
;
if
(btree_node_is_inner (left_node))
	{
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count;
++
index)
	    {
unsigned
pos
=
right_node
->
entry_count
-
1
-
index;
	      right_node
->
content.children[pos
+
to_shift]
=
right_node
->
content.children[pos];
	    }
for
(
unsigned
index
=
0
; index
!=
to_shift;
++
index)
	    right_node
->
content.children[index]
=
left_node
->
content
		  .children[left_node
->
entry_count
-
to_shift
+
index];
	}
else
{
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count;
++
index)
	    {
unsigned
pos
=
right_node
->
entry_count
-
1
-
index;
	      right_node
->
content.entries[pos
+
to_shift]
=
right_node
->
content.entries[pos];
	    }
for
(
unsigned
index
=
0
; index
!=
to_shift;
++
index)
	    right_node
->
content.entries[index]
=
left_node
->
content
		  .entries[left_node
->
entry_count
-
to_shift
+
index];
	}
      left_node
->
entry_count
-=
to_shift;
      right_node
->
entry_count
+=
to_shift;
    }
else
{
// Shift from right to left
unsigned
to_shift
=
(right_node
->
entry_count
-
left_node
->
entry_count)
/
2
;
if
(btree_node_is_inner (left_node))
	{
for
(
unsigned
index
=
0
; index
!=
to_shift;
++
index)
	    left_node
->
content.children[left_node
->
entry_count
+
index]
=
right_node
->
content.children[index];
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count
-
to_shift;
++
index)
	    right_node
->
content.children[index]
=
right_node
->
content.children[index
+
to_shift];
	}
else
{
for
(
unsigned
index
=
0
; index
!=
to_shift;
++
index)
	    left_node
->
content.entries[left_node
->
entry_count
+
index]
=
right_node
->
content.entries[index];
for
(
unsigned
index
=
0
; index
!=
right_node
->
entry_count
-
to_shift;
++
index)
	    right_node
->
content.entries[index]
=
right_node
->
content.entries[index
+
to_shift];
	}
      left_node
->
entry_count
+=
to_shift;
      right_node
->
entry_count
-=
to_shift;
    }
uintptr_t
left_fence;
if
(btree_node_is_leaf (left_node))
    {
      left_fence
=
right_node
->
content.entries[
0
].base
-
1
;
    }
else
{
      left_fence
=
btree_node_get_fence_key (left_node);
    }
  parent
->
content.children[left_slot].separator
=
left_fence;
  btree_node_unlock_exclusive (parent);
if
(target
<=
left_fence)
    {
      btree_node_unlock_exclusive (right_node);
return
left_node;
    }
else
{
      btree_node_unlock_exclusive (left_node);
return
right_node;
    }
}
// Remove an entry
static
struct
object
*
btree_remove
(
struct
btree
*
t,
uintptr_t
base)
{
// Access the root
version_lock_lock_exclusive (
&
(t
->
root_lock));
struct
btree_node
*
iter
=
t
->
root;
if
(iter)
    btree_node_lock_exclusive (iter);
  version_lock_unlock_exclusive (
&
(t
->
root_lock));
if
(
!
iter)
return
NULL
;
// Same strategy as with insert, walk down with lock coupling and
// merge eagerly
while
(btree_node_is_inner (iter))
    {
unsigned
slot
=
btree_node_find_inner_slot (iter, base);
struct
btree_node
*
next
=
iter
->
content.children[slot].child;
      btree_node_lock_exclusive (next);
if
(btree_node_needs_merge (next))
	{
// Use eager merges to avoid lock coupling up
iter
=
btree_merge_node (t, slot, iter, base);
	}
else
{
	  btree_node_unlock_exclusive (iter);
	  iter
=
next;
	}
    }
// Remove existing entry
unsigned
slot
=
btree_node_find_leaf_slot (iter, base);
if
((slot
>=
iter
->
entry_count)
||
(iter
->
content.entries[slot].base
!=
base))
    {
// not found, this should never happen
btree_node_unlock_exclusive (iter);
return
NULL
;
    }
struct
object
*
ob
=
iter
->
content.entries[slot].ob;
for
(
unsigned
index
=
slot; index
+
1
<
iter
->
entry_count;
++
index)
    iter
->
content.entries[index]
=
iter
->
content.entries[index
+
1
];
  iter
->
entry_count
--
;
  btree_node_unlock_exclusive (iter);
return
ob;
}
Lookups are conceptually simple, we just walk down the b-tree. However we do the traversal using optimistic lock coupling, which means the data could change behind our back at any time. As a consequence, all reads have to be (relaxed) atomic reads, and we have to validate the current lock before acting upon a value that we have read. In case of failures (e.g., concurrent writes during reading), we simply restart the traversal.
// Find the corresponding entry for the given address
static
struct
object
*
btree_lookup
(
const
struct
btree
*
t,
uintptr_t
target_addr)
{
// Within this function many loads are relaxed atomic loads.
// Use a macro to keep the code reasonable
#define RLOAD(x) __atomic_load_n (&(x), __ATOMIC_RELAXED)
// For targets where unwind info is usually not registered through these
// APIs anymore, avoid any sequential consistent atomics.
// Use relaxed MO here, it is up to the app to ensure that the library
// loading/initialization happens-before using that library in other
// threads (in particular unwinding with that library's functions
// appearing in the backtraces).  Calling that library's functions
// without waiting for the library to initialize would be racy.
if
(__builtin_expect (
!
RLOAD (t
->
root),
1
))
return
NULL
;
// The unwinding tables are mostly static, they only change when
// frames are added or removed. This makes it extremely unlikely that they
// change during a given unwinding sequence. Thus, we optimize for the
// contention free case and use optimistic lock coupling. This does not
// require any writes to shared state, instead we validate every read. It is
// important that we do not trust any value that we have read until we call
// validate again. Data can change at arbitrary points in time, thus we always
// copy something into a local variable and validate again before acting on
// the read. In the unlikely event that we encounter a concurrent change we
// simply restart and try again.
restart:
struct
btree_node
*
iter;
uintptr_t
lock;
  {
// Accessing the root node requires defending against concurrent pointer
// changes Thus we couple rootLock -> lock on root node -> validate rootLock
if
(
!
version_lock_lock_optimistic (
&
(t
->
root_lock),
&
lock))
goto
restart;
    iter
=
RLOAD (t
->
root);
if
(
!
version_lock_validate (
&
(t
->
root_lock), lock))
goto
restart;
if
(
!
iter)
return
NULL
;
uintptr_t
child_lock;
if
((
!
btree_node_lock_optimistic (iter,
&
child_lock))
||
(
!
version_lock_validate (
&
(t
->
root_lock), lock)))
goto
restart;
    lock
=
child_lock;
  }
// Now we can walk down towards the right leaf node
while
(
true
)
    {
enum
node_type type
=
RLOAD (iter
->
type);
unsigned
entry_count
=
RLOAD (iter
->
entry_count);
if
(
!
btree_node_validate (iter, lock))
goto
restart;
if
(
!
entry_count)
return
NULL
;
if
(type
==
btree_node_inner)
	{
// We cannot call find_inner_slot here because we need (relaxed)
// atomic reads here
unsigned
slot
=
0
;
while
(
	    ((slot
+
1
)
<
entry_count)
&&
(RLOAD (iter
->
content.children[slot].separator)
<
target_addr))
++
slot;
struct
btree_node
*
child
=
RLOAD (iter
->
content.children[slot].child);
if
(
!
btree_node_validate (iter, lock))
goto
restart;
// The node content can change at any point in time, thus we must
// interleave parent and child checks
uintptr_t
child_lock;
if
(
!
btree_node_lock_optimistic (child,
&
child_lock))
goto
restart;
if
(
!
btree_node_validate (iter, lock))
goto
restart;
// make sure we still point to the correct node after
// acquiring the optimistic lock
// Go down
iter
=
child;
	  lock
=
child_lock;
	}
else
{
// We cannot call find_leaf_slot here because we need (relaxed)
// atomic reads here
unsigned
slot
=
0
;
while
(((slot
+
1
)
<
entry_count)
&&
(RLOAD (iter
->
content.entries[slot].base)
+
RLOAD (iter
->
content.entries[slot].size)
<=
target_addr))
++
slot;
struct
leaf_entry entry;
	  entry.base
=
RLOAD (iter
->
content.entries[slot].base);
	  entry.size
=
RLOAD (iter
->
content.entries[slot].size);
	  entry.ob
=
RLOAD (iter
->
content.entries[slot].ob);
if
(
!
btree_node_validate (iter, lock))
goto
restart;
// Check if we have a hit
if
((entry.base
<=
target_addr)
&&
(target_addr
<
entry.base
+
entry.size))
	    {
return
entry.ob;
	    }
return
NULL
;
	}
    }
#undef RLOAD
}
This is the end of the article series discussing the gcc patch for lock-free unwinding. With that patch, we get scalable unwinding even on a machine with 256 hardware contexts. I hope the series helps with understanding the patch, and eventually allows it to be integrated into gcc.
