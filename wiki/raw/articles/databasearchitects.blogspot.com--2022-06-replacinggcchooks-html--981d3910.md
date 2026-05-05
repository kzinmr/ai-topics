---
title: "Making unwinding through JIT-ed code scalable - Replacing the gcc hooks"
url: "https://databasearchitects.blogspot.com/2022/06/replacinggcchooks.html"
fetched_at: 2026-05-05T07:01:28.793066+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Making unwinding through JIT-ed code scalable - Replacing the gcc hooks

Source: https://databasearchitects.blogspot.com/2022/06/replacinggcchooks.html

This article is part of the series about scalable unwinding that starts
here
.
As discussed in the previous article, the gcc mechanism does not scale because it uses a global lock to protect its list of unwinding frames. To solve that problem, we replace that list with a read-optimized b-tree that allows for concurrent reads and writes. In this article we just discuss the patches to gcc necessary to enable that mechanism, the b-tree itself is discussed in subsequent articles.
We start by replacing the old fast path mechanism with a b-tree root:
index 8ee55be5675..d546b9e4c43 100644
--- a/libgcc/unwind-dw2-fde.c
+++ b/libgcc/unwind-dw2-fde.c
@@ -42,15 +42,34 @@ see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see
#endif
 #endif
+#ifdef ATOMIC_FDE_FAST_PATH
+#include "unwind-dw2-btree.h"
+
+static struct btree registered_frames;
+
+static void
+release_registered_frames (void) __attribute__ ((destructor (110)));
+static void
+release_registered_frames (void)
+{
+  /* Release the b-tree and all frames. Frame releases that happen later are
+   * silently ignored */
+  btree_destroy (&registered_frames);
+}
+
+static void
+get_pc_range (const struct object *ob, uintptr_t *range);
+static void
+init_object (struct object *ob);
+
+#else
+
/* The unseen_objects list contains objects that have been registered
    but not yet categorized in any way.  The seen_objects list has had
    its pc_begin and count fields initialized at minimum, and is sorted
    by decreasing value of pc_begin.  */
 static struct object *unseen_objects;
 static struct object *seen_objects;
-#ifdef ATOMIC_FDE_FAST_PATH
-static int any_objects_registered;
-#endif
#ifdef __GTHREAD_MUTEX_INIT
 static __gthread_mutex_t object_mutex = __GTHREAD_MUTEX_INIT;
@@ -78,6 +97,7 @@ init_object_mutex_once (void)
static __gthread_mutex_t object_mutex;
 #endif
 #endif
+#endif
When the platform supports atomics (ATOMIC_FDE_FAST_PATH), we replace the whole mechanism with one b-tree, whose root is registered_frames. Neither the objects lists not the mutex exist on such platforms. To avoid leaking the memory for the b-tree we register release_registered_frames as destructor with a very late priority on shutdown. Note that it is still safe to throw exceptions even when the b-tree is gone as long as unwinding does not have to go through JITed code that was registered here. The destroyed b-tree behaves like an empty b-tree. get_pc_range and init_object are forward declared because we need them already when inserting into the b-tree.
When registering frames we no longer grab a mutex, we immediately store the frames in the b-tree:
@@ -99,23 +119,23 @@ __register_frame_info_bases (const void *begin, struct object *ob,
ob->fde_end = NULL;
 #endif
+#ifdef ATOMIC_FDE_FAST_PATH
+  // Initialize  eagerly to avoid locking later
+  init_object (ob);
+
+  // And register the frame
+  uintptr_t range[2];
+  get_pc_range (ob, range);
+  btree_insert (&registered_frames, range[0], range[1] - range[0], ob);
+#else
init_object_mutex_once ();
   __gthread_mutex_lock (&object_mutex);
 
   ob->next = unseen_objects;
   unseen_objects = ob;
-#ifdef ATOMIC_FDE_FAST_PATH
-  /* Set flag that at least one library has registered FDEs.
-     Use relaxed MO here, it is up to the app to ensure that the library
-     loading/initialization happens-before using that library in other
-     threads (in particular unwinding with that library's functions
-     appearing in the backtraces).  Calling that library's functions
-     without waiting for the library to initialize would be racy.  */
-  if (!any_objects_registered)
-    __atomic_store_n (&any_objects_registered, 1, __ATOMIC_RELAXED);
-#endif
__gthread_mutex_unlock (&object_mutex);
+#endif
}
 
 void
@@ -153,23 +173,23 @@ __register_frame_info_table_bases (void *begin, struct object *ob,
ob->s.b.from_array = 1;
   ob->s.b.encoding = DW_EH_PE_omit;
+#ifdef ATOMIC_FDE_FAST_PATH
+  // Initialize  eagerly to avoid locking later
+  init_object (ob);
+
+  // And register the frame
+  uintptr_t range[2];
+  get_pc_range (ob, range);
+  btree_insert (&registered_frames, range[0], range[1] - range[0], ob);
+#else
init_object_mutex_once ();
   __gthread_mutex_lock (&object_mutex);
 
   ob->next = unseen_objects;
   unseen_objects = ob;
-#ifdef ATOMIC_FDE_FAST_PATH
-  /* Set flag that at least one library has registered FDEs.
-     Use relaxed MO here, it is up to the app to ensure that the library
-     loading/initialization happens-before using that library in other
-     threads (in particular unwinding with that library's functions
-     appearing in the backtraces).  Calling that library's functions
-     without waiting for the library to initialize would be racy.  */
-  if (!any_objects_registered)
-    __atomic_store_n (&any_objects_registered, 1, __ATOMIC_RELAXED);
-#endif
__gthread_mutex_unlock (&object_mutex);
+#endif
}
Note that there is a subtle change of logic here: The old mechanism stores all incoming frames as they are in the unseen_objects chain without even looking at them. Then, during unwinding, it inspects the frames to find out the range of program counter values (pc_range), and sorts them in the seen_objects list. This fundamentally requires a lock, as the objects are modified during unwinding. To avoid that, the new code immediately computes the PC range and lets the b-tree do the sorting. Which keeps the frame immutable during unwinding.
When searching a frame during unwinding we delegate everything to the b-tree, which provides lock-free lookups. No mutex is acquired on platforms that support atomics:
@@ -1033,17 +1161,12 @@ _Unwind_Find_FDE (void *pc, struct dwarf_eh_bases *bases)
const fde *f = NULL;
 
 #ifdef ATOMIC_FDE_FAST_PATH
-  /* For targets where unwind info is usually not registered through these
-     APIs anymore, avoid taking a global lock.
-     Use relaxed MO here, it is up to the app to ensure that the library
-     loading/initialization happens-before using that library in other
-     threads (in particular unwinding with that library's functions
-     appearing in the backtraces).  Calling that library's functions
-     without waiting for the library to initialize would be racy.  */
-  if (__builtin_expect (!__atomic_load_n (&any_objects_registered,
-					  __ATOMIC_RELAXED), 1))
+  ob = btree_lookup (&registered_frames, (uintptr_t) pc);
+  if (!ob)
return NULL;
-#endif
+
+  f = search_object (ob, pc);
+#else
init_object_mutex_once ();
   __gthread_mutex_lock (&object_mutex);
@@ -1081,6 +1204,7 @@ _Unwind_Find_FDE (void *pc, struct dwarf_eh_bases *bases)
fini:
   __gthread_mutex_unlock (&object_mutex);
+#endif
if (f)
     {
De-registering a frame works just the same as registering, we use get_pc_range to get the range and then remove it from the b-tree:
@@ -200,16 +220,33 @@ __register_frame_table (void *begin)
void *
 __deregister_frame_info_bases (const void *begin)
 {
-  struct object **p;
struct object *ob = 0;
 
   /* If .eh_frame is empty, we haven't registered.  */
   if ((const uword *) begin == 0 || *(const uword *) begin == 0)
     return ob;
+#ifdef ATOMIC_FDE_FAST_PATH
+  // Find the corresponding PC range
+  struct object lookupob;
+  lookupob.tbase = 0;
+  lookupob.dbase = 0;
+  lookupob.u.single = begin;
+  lookupob.s.i = 0;
+  lookupob.s.b.encoding = DW_EH_PE_omit;
+#ifdef DWARF2_OBJECT_END_PTR_EXTENSION
+  lookupob.fde_end = NULL;
+#endif
+  uintptr_t range[2];
+  get_pc_range (&lookupob, range);
+
+  // And remove
+  ob = btree_remove (&registered_frames, range[0]);
+#else
init_object_mutex_once ();
   __gthread_mutex_lock (&object_mutex);
+  struct object **p;
for (p = &unseen_objects; *p ; p = &(*p)->next)
     if ((*p)->u.single == begin)
       {
@@ -241,6 +278,8 @@ __deregister_frame_info_bases (const void *begin)
out:
   __gthread_mutex_unlock (&object_mutex);
+#endif
+
gcc_assert (ob);
   return (void *) ob;
 }
We are nearly done with our changes to existing gcc code, we just need a few more helper functions for get_pc_range:
@@ -264,7 +303,7 @@ __deregister_frame (void *begin)
instead of an _Unwind_Context.  */
 
 static _Unwind_Ptr
-base_from_object (unsigned char encoding, struct object *ob)
+base_from_object (unsigned char encoding, const struct object *ob)
{
   if (encoding == DW_EH_PE_omit)
     return 0;
@@ -821,6 +860,91 @@ init_object (struct object* ob)
ob->s.b.sorted = 1;
 }
+#ifdef ATOMIC_FDE_FAST_PATH
+/* Get the PC range from FDEs. The code is very similar to
+   classify_object_over_fdes and should be kept in sync with
+   that. The main difference is that classify_object_over_fdes
+   modifies the object, which we cannot do here */
+static void
+get_pc_range_from_fdes (const struct object *ob, const fde *this_fde,
+			uintptr_t *range)
+{
+  const struct dwarf_cie *last_cie = 0;
+  int encoding = DW_EH_PE_absptr;
+  _Unwind_Ptr base = 0;
+
+  for (; !last_fde (ob, this_fde); this_fde = next_fde (this_fde))
+    {
+      const struct dwarf_cie *this_cie;
+      _Unwind_Ptr mask, pc_begin, pc_range;
+
+      /* Skip CIEs.  */
+      if (this_fde->CIE_delta == 0)
+	continue;
+
+      this_cie = get_cie (this_fde);
+      if (this_cie != last_cie)
+	{
+	  last_cie = this_cie;
+	  encoding = get_cie_encoding (this_cie);
+	  base = base_from_object (encoding, ob);
+	}
+
+      const unsigned char *p;
+      p = read_encoded_value_with_base (encoding, base, this_fde->pc_begin,
+					&pc_begin);
+      read_encoded_value_with_base (encoding & 0x0F, 0, p, &pc_range);
+
+      /* Take care to ignore link-once functions that were removed.
+	 In these cases, the function address will be NULL, but if
+	 the encoding is smaller than a pointer a true NULL may not
+	 be representable.  Assume 0 in the representable bits is NULL.  */
+      mask = size_of_encoded_value (encoding);
+      if (mask < sizeof (void *))
+	mask = (((_Unwind_Ptr) 1) << (mask << 3)) - 1;
+      else
+	mask = -1;
+      if ((pc_begin & mask) == 0)
+	continue;
+
+      _Unwind_Ptr pc_end = pc_begin + pc_range;
+      if ((!range[0]) && (!range[1]))
+	{
+	  range[0] = pc_begin;
+	  range[1] = pc_end;
+	}
+      else
+	{
+	  if (pc_begin < range[0])
+	    range[0] = pc_begin;
+	  if (pc_end > range[1])
+	    range[1] = pc_end;
+	}
+    }
+}
+
+/* Get the PC range for lookup */
+static void
+get_pc_range (const struct object *ob, uintptr_t *range)
+{
+  range[0] = range[1] = 0;
+  if (ob->s.b.sorted)
+    {
+      get_pc_range_from_fdes (ob, ob->u.sort->orig_data, range);
+    }
+  else if (ob->s.b.from_array)
+    {
+      fde **p = ob->u.array;
+      for (; *p; ++p)
+	get_pc_range_from_fdes (ob, *p, range);
+    }
+  else
+    {
+      get_pc_range_from_fdes (ob, ob->u.single, range);
+    }
+}
+#endif
+
/* A linear search through a set of FDEs for the given PC.  This is
    used when there was insufficient memory to allocate and sort an
    array.  */
The code finds out the range of possible pc values for the FDE. Conceptually it does nearly the same as the already existing function classify_object_over_fdes. Unfortunately we cannot reuse that code, as classify_object_over_fdes modifies the object in order to speed up subsequent searches, and we require our data to be immutable.
In the next article we look at
optimistic lock coupling
, which is the mechanism that we use to allow for lock-free readers.
