---
title: "Recent LLVM hash table improvements"
url: "https://maskray.me/blog/2026-06-07-recent-llvm-hash-table-improvements"
fetched_at: 2026-06-07T07:01:35.692176+00:00
source: "Fangrui Song (MaskRay)"
tags: [blog, raw]
---

# Recent LLVM hash table improvements

Source: https://maskray.me/blog/2026-06-07-recent-llvm-hash-table-improvements

LLVM has several hash tables. They used quadratic probing with
in-band sentinel keys (empty, tombstone); recent work has been replacing
that with linear probing with tombstone key removed.
DenseMap
(replacement for
std::unordered_map
):
DenseMapInfo::getEmptyKey()
/
getTombstoneKey()
.
SmallPtrSet
(replacement for
std::unordered_set<T *>
): hard-coded
-1
(empty) and
-2
(tombstone).
StringMap
(replacement for
std::unordered_map<std::string, V>
)
For the open-addressed
DenseMap
and
SmallPtrSet
, pointers, references, and iterators are
invalidated by insert.
StringMap
is different: each entry
lives in a heap-allocated
StringMapEntry<V>
node, so
entry pointers survive grow.
std::unordered_map
, being
node-based, keeps surviving-element pointers valid across both insert
and erase and only invalidates the erased element's own iterator. LLVM
code rarely needs that stronger contract — callers do not hold
long-lived references into the container across mutation — and that gap
is what gives pass to relocating erase and bit-array occupancy.
Recently,
Tombstones have been removed from DenseMap and SmallPtrSet.
erase()
also invalidates pointers.
DenseMap has also retired its empty-key sentinel, leading to
significant performance improvements. DenseMap with integer keys
(
int
/
unsigned
/
size_t
) had
-1
/
-2
reserved — a footgun, now fixed.
TODO: pending patch on StringMap
SmallPtrSet
SmallPtrSet has a small mode, used when the number of elements is
below a threshold, and a large mode. The tombstone state was removed by
#96762
in
2024. The patch changed
erase()
operation to invalidate
iterators, requiring treewide fixes.
The large mode used a quadratic probing with two sentinel keys
(empty, tombstone).
Knuth TAOCP Vol. 3 §6.4 Algorithm R describes an algorithm that
avoids lazy deletion.
#197637
has
implemented it.
I've investigated Robin Hood Hashing and Abseil Swiss Table family
implementations - both would lead to inferior performance. Robin Hood
Hashing primarily improves find-miss on high-load factors but imposes a
small cost on find-hit and inserts.
DenseMap
Two major changes have been merged:
Replace the tombstone state with Algorithm R deletion. (
#200595
)
Replace the empty state with a bitarray. (
#201281
)
What the workload looks like
An instrumented clang counts every
(KeyT, ValueT)
operation while compiling
llvm/lib/Analysis/ScalarEvolution.cpp
.
597
distinct
DenseMap
/
DenseSet
types,
~186M
user ops:
op
count
probes mean
find-hit
65.2M
1.55
find-miss
65.7M
1.28
insert
47.8M
1.71
erase
7.0M
—
grow
1.5M
—
Lookups are ~70% of the load; insert ~26%, erase ~4%. Probe means sit
between 1.3 and 1.7 — well inside what linear probing handles.
operator[]
is classified at the bucket it lands on: a
present key is counted as find-hit, an empty slot as insert.
A few instantiations carry most of the traffic:
type
find-hit
find-miss (mean)
insert
erase
grow
peak
DenseMap<const void *, Pass *>
680K
24.8M (1.03)
202K
202K
9.3K
1 KiB
DenseMap<Value *, ValueHandleBase *>
2.8M (2.02)
0
2.2M
2.2M
11
1 MiB
DenseMap<const Value *, StringMapEntry<Value *> *>
3.0M
1.4M (2.26)
540K
439K
13
4 MiB
DenseMap<DeclarationName, StoredDeclsList>
772K
1.2M (1.94)
143K
0
9.0K
64 KiB
DenseMap<LazyCallGraph::Node *, LazyCallGraph::SCC *>
1.3M
98K (2.95)
175K
173K
15
258 KiB
DenseMap<AnalysisKey *, bool>
2.8M
2.0M (1.52)
2.0M
0
124K
1 KiB
<const void *, Pass *>
runs 25.5M lookups at 1.03
mean — volume is not clustering.
<Value *, ValueHandleBase *>
is the single largest
erase consumer at 2.2M; this is the workload where the Algorithm R
relocating-erase callback earns its keep. Its find-miss column is zero
because every access in
llvm/lib/IR/Value.cpp
goes through
operator[]
or
erase
— there is no
find
/
lookup
call site, so an empty-slot probe
is bucketed as insert rather than find-miss. The bucket's value-slot
address is captured by
ValueHandleBase *&Entry = Handles[V]
and stored as a
linked-list back-pointer (
PrevPtr
), which is exactly what
the new
OnMoved
callback refreshes when Algorithm R shifts
neighbors.
StringMapEntry
peaks at 4 MiB, the regime where
the used-bit array's byte overhead matters most. Structural and
graph-pointer keys (
DeclarationName
,
LazyCallGraph::Node *
) still cost a couple of extra probes
per miss.
Code size matters. SIMD tables may be a poor fit.
Linear probing +
Algorithm R deletion (
#200595
)
Linear probing needs a strong pointer hash. The old
DenseMapInfo<T*>::getHashValue
left bump-allocated
pointers — clang's dominant key shape — sharing high bits and collapsing
onto a short bucket range. Quadratic probing had masked this.
#197390
switched to a stronger mixer, unblocking both SmallPtrSet and
DenseMap.
#200595 replaces quadratic probing plus tombstones with linear
probing plus Algorithm R. Two bucket states, no lazy markers. Erase now
relocates following entries to close the hole, so entry pointers may be
invalidated. The new
erase(Key, OnMoved)
and
erase(iterator, OnMoved)
overloads fire a callback once per
shifted bucket;
ValueHandleBase::RemoveFromUseList
uses
this to refresh
PrevPtr
.
The first attempt had a war story. The original landed as
#199615
,
then got reverted by
#200421
after a SCEV crash:
PoisoningVH
cached a bare bucket
pointer across an op that, post-Algorithm R, relocates. The bug was
latent under tombstones, which don't relocate, and only surfaced once
the algorithm flipped. Fixed in
#200540
,
relanded as #200595.
On stage1-O3 the change is
-1.34%
instructions and
all ten CTMark benchmarks improve between -0.85% and -1.61% (
compare
).
Clang wall is
-1.54%
, stage1 binary
-1.40%
— fewer bucket states means less generated code.
The commit message remarks that
"the in-band sentinel value approach
… is the best, or at least very difficult to beat."
The used-bit
array below earns the right to violate this.
Packed used-bit array (
#201281
)
The empty-slot test has switched from
getEmptyKey()
to a
bit test. There is a 1-bit-per-bucket
uint32
array sharing
one allocation with the buckets.
This is a trade-off
Find-miss, iteration, and large-bucket inserts win: the bit array
terminates the probe walk and skips the empty buckets without ever
loading the bucket key.
Find-hit and small-bucket inserts lose: a hit loads the matched
bucket anyway, and a small-bucket insert pays one extra word write.
The aggregate numbers are interesting (
compare
).
Stage1-O3 instructions are
-0.99%
, but stage2-O3 is
+0.13%
and stage2-O0-g is
+0.34%
—
instructions actually go
up
. Clang wall time is
-1.37%
while instructions are only
-0.49%
, and
size-file
is
+0.87%
because the bit array costs bytes.
instructions:u
is the wrong cost model when the savings are
cache loads: the counter sees the new bit-test sequence; it does not see
the bucket load you didn't issue.
After this patch,
DenseMap<int/unsigned/size_t, X>
accepts every value of the key domain.
Cleanup cascade
Tree-wide trait simplification, one PR per subdirectory for
reviewability.
getTombstoneKey()
went out as
ADT #200959
,
IR+Analysis
#200958
,
CodeGen+Transforms
#200956
,
llvm-rest
#200957
,
Target
#200955
, and
clang
#200634
.
getEmptyKey()
removal (post-#201281) followed in
BOLT
#201986
,
clang
#201987
,
flang
#201988
,
lld #201989
,
lldb
#201990
,
mlir
#201991
,
Polly
#201992
,
Target
#201993
,
CodeGen+Transforms
#201994
,
llvm
#201996
,
IR+Analysis
#201997
, and
ADT
#201998
.
Several of these commits showed small but consistent wins on the
tracker. The IR+Analysis cleanups in particular —
#200958
for
getTombstoneKey()
and
#201997
for
getEmptyKey()
— each measured around -0.05% to -0.10%
stage1-O3 instructions and -0.23% clang wall time. But the headline win
is in the trait itself, not the timings: integer keys are now safe, the
MLIR #54908 crash class is gone, and the AssertingVH downcast UB becomes
moot. The design discussion lives in
#200183
.
StringMap
TODO
What didn't make it
Prototyped, measured, rejected — first on
SmallPtrSet
,
then again on
DenseMap
.
Verstable
(metadata + home-rooted chains). Wins
negative-probe and iteration; loses
clang
self-build —
metadata + chain logic inlines into every call site for
+4–10%
binary
. Combined allocation, inline
SmallDenseMap
,
NOINLINE cold paths, fragment removal,
NumTombstones
cleanup all tried; ~+3% instructions / ~+5% size at best.
Robin Hood
. The find-miss early-out depends on
knowing each resident's displacement; without stored metadata it
requires re-hashing every resident on the probe walk, which costs more
than the saved probes. Storing the displacement recovers the early-out
but adds a metadata cache line, and the swap-carry on insert is
intrinsic —
+10–20% insert vs Alg R
regardless of
layout.
boost::unordered_flat_map
. Faster on
synthetic harnesses (
Böther et al.,
PVLDB '23
); each instantiation drags in more code, and
clang
has 597.
Schemes that store metadata pay in code size; the
clang
build is where code size matters. Algorithm R + 1-bit occupancy is the
cheap-metadata corner.
DenseMap variant
optimized for pointer key?
I considered whether DenseMap for pointer keys should keep an in-band
sentinel variant (
#200183
) —
it would avoid the used-bit array's max-rss overhead. Measurements on
AMD Zen 4 and Apple M4 ruled it out: the used-bit version is faster
despite the extra memory.
Takeaways
Linear probing + a good mixer beats quadratic + tombstones on a
pointer-heavy workload.
#197390
was
the unlock; the algorithm change then ran across two containers.
Swiss Table family implementations are poor at small keys. If
deletion performance does not matter, you don't need its heavy
implementation.
SmallPtrSet
was the dry run that de-risked
DenseMap
: same algorithm, smaller blast radius, same
conclusion on rejected alternatives.
Tombstones aren't free at 4% erase — they slow down insertion.
