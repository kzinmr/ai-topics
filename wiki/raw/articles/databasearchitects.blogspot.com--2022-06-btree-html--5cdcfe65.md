---
title: "Making unwinding through JIT-ed code scalable - The b-tree"
url: "https://databasearchitects.blogspot.com/2022/06/btree.html"
fetched_at: 2026-05-05T07:01:28.310046+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Making unwinding through JIT-ed code scalable - The b-tree

Source: https://databasearchitects.blogspot.com/2022/06/btree.html

This article is part of the series about scalable unwinding that starts
here
.
We use a
b-tree
because it offers fast lookup, good data locality, and a scalable implementation is reasonable easy when using optimistic lock coupling. Nevertheless a b-tree is a non-trivial data structure. To avoid having one huge article that includes all details of the b-tree, we just discuss the data structure themselves and some helper functions here, the insert/remove/lookup operations will be discussed in the next article.
A b-tree partitions its elements by value. An inner node contains a sorted list of separator/child pairs, with the guarantee that the elements in the sub-tree rooted at the child pointer will be <= the separator. The leaf nodes contains sorted lists of (base, size, object) entries, where the object is responsible for unwinding entries between base and base+size.  An b-tree maintains the invariants that 1) all nodes except the root are at least half full, and 2) a leaf nodes have the same distance to the root. This guarantees us logarithmic lookup costs. Note that we use fence-keys, i.e., the inner nodes have a separator for the right-most entries, too, which is not the case in all b-tree implementations:
// The largest possible separator value
static
const
uintptr_t
max_separator
=
~
((
uintptr_t
) (
0
));
// Inner entry. The child tree contains all entries <= separator
struct
inner_entry
{
uintptr_t
separator;
struct
btree_node
*
child;
};
// Leaf entry. Stores an object entry
struct
leaf_entry
{
uintptr_t
base, size;
struct
object
*
ob;
};
// node types
enum
node_type
{
  btree_node_inner,
  btree_node_leaf,
  btree_node_free
};
// Node sizes. Chosen such that the result size is roughly 256 bytes
#define max_fanout_inner 15
#define max_fanout_leaf 10
// A btree node
struct
btree_node
{
// The version lock used for optimistic lock coupling
struct
version_lock version_lock;
// The number of entries
unsigned
entry_count;
// The type
enum
node_type type;
// The payload
union
{
// The inner nodes have fence keys, i.e., the right-most entry includes a
// separator
struct
inner_entry children[max_fanout_inner];
struct
leaf_entry entries[max_fanout_leaf];
  } content;
};
To simplify the subsequent code we define a number of helper functions that are largely straight-forward, and that allow to distinguish leaf and inner node and provide searching within a node. The lock operations directly map to operations on the version lock:
// Is an inner node?
static
inline
bool
btree_node_is_inner
(
const
struct
btree_node
*
n)
{
return
n
->
type
==
btree_node_inner;
}
// Is a leaf node?
static
inline
bool
btree_node_is_leaf
(
const
struct
btree_node
*
n)
{
return
n
->
type
==
btree_node_leaf;
}
// Should the node be merged?
static
inline
bool
btree_node_needs_merge
(
const
struct
btree_node
*
n)
{
return
n
->
entry_count
<
(btree_node_is_inner (n)
?
(max_fanout_inner
/
2
)
:
(max_fanout_leaf
/
2
));
}
// Get the fence key for inner nodes
static
inline
uintptr_t
btree_node_get_fence_key
(
const
struct
btree_node
*
n)
{
// For inner nodes we just return our right-most entry
return
n
->
content.children[n
->
entry_count
-
1
].separator;
}
// Find the position for a slot in an inner node
static
unsigned
btree_node_find_inner_slot
(
const
struct
btree_node
*
n,
uintptr_t
value)
{
for
(
unsigned
index
=
0
, ec
=
n
->
entry_count; index
!=
ec;
++
index)
if
(n
->
content.children[index].separator
>=
value)
return
index;
return
n
->
entry_count;
}
// Find the position for a slot in a leaf node
static
unsigned
btree_node_find_leaf_slot
(
const
struct
btree_node
*
n,
uintptr_t
value)
{
for
(
unsigned
index
=
0
, ec
=
n
->
entry_count; index
!=
ec;
++
index)
if
(n
->
content.entries[index].base
+
n
->
content.entries[index].size
>
value)
return
index;
return
n
->
entry_count;
}
// Try to lock the node exclusive
static
inline
bool
btree_node_try_lock_exclusive
(
struct
btree_node
*
n)
{
return
version_lock_try_lock_exclusive (
&
(n
->
version_lock));
}
// Lock the node exclusive, blocking as needed
static
inline
void
btree_node_lock_exclusive
(
struct
btree_node
*
n)
{
  version_lock_lock_exclusive (
&
(n
->
version_lock));
}
// Release a locked node and increase the version lock
static
inline
void
btree_node_unlock_exclusive
(
struct
btree_node
*
n)
{
  version_lock_unlock_exclusive (
&
(n
->
version_lock));
}
// Acquire an optimistic "lock". Note that this does not lock at all, it
// only allows for validation later
static
inline
bool
btree_node_lock_optimistic
(
const
struct
btree_node
*
n,
uintptr_t
*
lock)
{
return
version_lock_lock_optimistic (
&
(n
->
version_lock), lock);
}
// Validate a previously acquire lock
static
inline
bool
btree_node_validate
(
const
struct
btree_node
*
n,
uintptr_t
lock)
{
return
version_lock_validate (
&
(n
->
version_lock), lock);
}
With that we come to the b-tree itself, which consists of a pointer to the root node, a version lock to protect the root, and a free list:
// A btree. Suitable for static initialization, all members are zero at the
// beginning
struct
btree
{
// The root of the btree
struct
btree_node
*
root;
// The free list of released node
struct
btree_node
*
free_list;
// The version lock used to protect the root
struct
version_lock root_lock;
};
// Initialize a btree. Not actually used, just for exposition
static
inline
void
btree_init
(
struct
btree
*
t)
{
  t
->
root
=
NULL
;
  t
->
free_list
=
NULL
;
  t
->
root_lock.version_lock
=
0
;
};
We need that free list because readers operate without visible synchronization. If we would simply free() a node, we would risk that a concurrent reader is still looking at that node, even though no relevant data exist on that node. (But the reader does not know this until it did the read). To prevent that, we put freed nodes in the free list, which ensures that the memory location remains valid, and prefer using nodes from the free list when allocating new nodes:
// Allocate a node. This node will be returned in locked exclusive state
static
struct
btree_node
*
btree_allocate_node
(
struct
btree
*
t,
bool
inner)
{
while
(
true
)
    {
// Try the free list first
struct
btree_node
*
next_free
=
__atomic_load_n (
&
(t
->
free_list), __ATOMIC_SEQ_CST);
if
(next_free)
	{
if
(
!
btree_node_try_lock_exclusive (next_free))
continue
;
// The node might no longer be free, check that again after acquiring
// the exclusive lock
if
(next_free
->
type
==
btree_node_free)
	    {
struct
btree_node
*
ex
=
next_free;
if
(__atomic_compare_exchange_n (
&
(t
->
free_list),
&
ex, next_free
->
content.children[
0
].child,
false
, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST))
		{
		  next_free
->
entry_count
=
0
;
		  next_free
->
type
=
inner
?
btree_node_inner
:
btree_node_leaf;
return
next_free;
		}
	    }
	  btree_node_unlock_exclusive (next_free);
continue
;
	}
// No free node available, allocate a new one
struct
btree_node
*
new_node
=
(
struct
btree_node
*
) (malloc (
sizeof
(
struct
btree_node)));
      version_lock_initialize_locked_exclusive (
&
(new_node
->
version_lock));
// initialize the node in locked state
new_node
->
entry_count
=
0
;
      new_node
->
type
=
inner
?
btree_node_inner
:
btree_node_leaf;
return
new_node;
    }
}
// Release a node. This node must be currently locked exclusively and will
// be placed in the free list
static
void
btree_release_node
(
struct
btree
*
t,
struct
btree_node
*
node)
{
// We cannot release the memory immediately because there might still be
// concurrent readers on that node. Put it in the free list instead
node
->
type
=
btree_node_free;
struct
btree_node
*
next_free
=
__atomic_load_n (
&
(t
->
free_list), __ATOMIC_SEQ_CST);
do
{
      node
->
content.children[
0
].child
=
next_free;
  }
while
(
!
__atomic_compare_exchange_n (
&
(t
->
free_list),
&
next_free, node,
false
, __ATOMIC_SEQ_CST,
					 __ATOMIC_SEQ_CST));
  btree_node_unlock_exclusive (node);
}
The last remaining infrastructure code is destroying the b-tree. Here, we simply walk the tree recursively and release all nodes. The recursion is safe because the depth is bound logarithmic:
// Recursively release a tree. The btree is by design very shallow, thus
// we can risk recursion here
static
void
btree_release_tree_recursively
(
struct
btree
*
t,
struct
btree_node
*
node)
{
  btree_node_lock_exclusive (node);
if
(btree_node_is_inner (node))
    {
for
(
unsigned
index
=
0
; index
<
node
->
entry_count;
++
index)
	btree_release_tree_recursively (t, node
->
content.children[index].child);
    }
  btree_release_node (t, node);
}
// Destroy a tree and release all nodes
static
void
btree_destroy
(
struct
btree
*
t)
{
// Disable the mechanism before cleaning up
struct
btree_node
*
old_root
=
__atomic_exchange_n (
&
(t
->
root),
NULL
, __ATOMIC_SEQ_CST);
if
(old_root)
    btree_release_tree_recursively (t, old_root);
// Release all free nodes
while
(t
->
free_list)
    {
struct
btree_node
*
next
=
t
->
free_list
->
content.children[
0
].child;
      free (t
->
free_list);
      t
->
free_list
=
next;
    }
}
This finished the infrastructure part of the b-tree, the high-level insert/remove/lookup functions are covered
in the next article
.
