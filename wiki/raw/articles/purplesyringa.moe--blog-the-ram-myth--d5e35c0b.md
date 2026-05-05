---
title: "The RAM myth | purplesyringa's blog"
url: "https://purplesyringa.moe/blog/./the-ram-myth/"
fetched_at: 2026-05-05T07:02:09.616970+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# The RAM myth | purplesyringa's blog

Source: https://purplesyringa.moe/blog/./the-ram-myth/

The RAM myth
December 19, 2024
Reddit
Hacker News
Russian
The RAM myth is a belief that modern computer memory resembles perfect random-access memory. Cache is seen as an optimization for small data: if it fits in L2, it’s going to be processed faster; if it doesn’t, there’s nothing we can do.
Most likely, you believe that code like this is the fastest way to shard data (I’m using Python as pseudocode; pretend I used your favorite low-level language):
groups = [[]
for
_
in
range
(n_groups)]
for
element
in
elements:
    groups[element.group].append(element)
Indeed, it’s linear (i.e. asymptotically optimal), and we have to access random indices anyway, so cache isn’t going to help us in any case.
In reality, when the number of groups is high, this is leaving a lot of performance on the table, and certain
asymptotically slower
algorithms can perform sharding significantly faster. They are mostly used by on-disk databases, but, surprisingly, they are useful even for in-RAM data.
Solution
The algorithm from above has an almost-guaranteed cache miss on every iteration. The only way to prevent cache misses is to make the memory accesses more ordered. If you can ensure the elements are ordered by
group
, that’s great. If you can’t, you can still sort the accesses before the
for
loop:
elements.sort(key =
lambda
element: element.group)
Sorting costs some time, but in return, removes cache misses from the
for
loop entirely. If the data is large enough that it doesn’t fit in cache, this is a net win. As a bonus, creating individual lists can be replaced with a group-by operation:
elements.sort(key =
lambda
element: element.group)
groups = [
    group_elements
for
_, group_elements
in
itertools.groupby(elements, key =
lambda
element: element.group)
]
There’s many cache-aware sorting algorithms, but as indices are just integers, radix sort works best here. Among off-the-shelf implementations,
radsort
worked the best for me in Rust.
Speedups
This is already better than the straightforward algorithm on large data, but there’s many tricks to make it faster.
Generators
Sorting APIs try to make it seem like the data is sorted in-place, even when that’s not the case. This requires sorted data to be explicitly written to memory in a particular format. But if we only need to iterate over groups, generators or callbacks help avoid this:
def
radix_sort
(
elements, bits =
32
):
if
len
(elements) <=
1
or
bits <=
0
:
yield
from
elements
return
buckets = [[]
for
_
in
range
(
256
)]
for
element
in
elements:
        buckets[(element.index >>
max
(
0
, bits -
8
)) &
0xff
].append(element)
for
bucket
in
buckets:
yield
from
radix_sort(bucket, bits -
8
)
We can even remove the
groupby
step by yielding individual groups:
if
bits <=
0
:
if
elements:
yield
elements
return
Reallocs
The next problem with this code is constantly reallocating the
bucket
arrays on
append
. This invokes
memcpy
more often than necessary and is bad for cache. A common fix is to compute sizes beforehand:
def
get_bucket
(
element
):
return
(element.index >>
max
(
0
, bits -
8
)) &
0xff
sizes = Counter(
map
(get_bucket, elements))



buckets = [reserve(sizes[i])
for
i
in
range
(
256
)]
for
element
in
elements:
    buckets[get_bucket(element)].append(element)
This, however, requires two iterations, and ideally we’d keep the code single-pass. If the index is random, we can have our cake and eat it too:
estimate
the size of each bucket as
len(elements) / 256
and reserve that much space. There’s going to be some leftovers if we underestimate, which we’ll store in a small separate storage:
class
Bucket
:
    reserved:
list
leftovers:
list
def
__init__
(
self, capacity
):
        self.reserved = reserve(capacity) 
        self.leftovers = []
def
append
(
self, element
):
if
len
(self.reserved) < self.reserved.capacity(): 
            self.reserved.append(element)
else
:
            self.leftovers.append(element)
def
__len__
(
self
):
return
len
(self.reserved) +
len
(self.leftovers)
def
__iter__
(
self
):
yield
from
self.reserved
yield
from
self.leftovers
The probability distribution plays ball here: on large input, only a tiny percentage of the elements overflow into
leftovers
, so the memory overhead is pretty small, reallocations on pushing into
leftovers
are fast, and bucketing (and iterating over a bucket) is cache-friendly.
Partitioning
One simple micro-optimization is to allocate once and split the returned memory into chunks instead of invoking
malloc
(or creating vectors) multiple times. Allocations are pretty slow, and this is a cheap way to reduce the effect.
Base case
Switching to the straightforward algorithm on small inputs increases performance, as the effects of
𝒪
(
n
log
⁡
n
)
code are more pronounced there. However, as
radix_sort
is recursive, we can perform this check on every level of recursion, scoring a win even on large data:
if
len
(elements) <= CUTOFF
or
bits <=
8
:
    counts = [
0
] *
256
for
element
in
elements:
        counts[element.index &
0xff
] +=
1
groups = [[]
for
_
in
range
(
256
)]
for
element
in
elements:
        groups[get_bucket(element)].append(element)
for
group
in
groups:
if
group:
yield
group
return
The optimal
CUTOFF
is heavily machine-dependent. It depends on the relative speed of cache levels and RAM, as well as cache size and data types. For 64-bit integers, I’ve seen machines where the optimal value was
50k
,
200k
, and
1M
. The best way to determine it is to benchmark in runtime – an acceptable solution for long-running software, like databases.
Benchmark
Setup
Here’s a small benchmark.
The input data is an array of random 64-bit integers. We want to group them by a simple multiplicative hash and perform a simple analysis on the buckets – say, compute the sum of minimums among buckets. (In reality, you’d consume the buckets with some other cache-friendly algorithm down the pipeline.)
We’ll compare two implementations:
The straightforward algorithm with optimized allocations.
Radix sort-based grouping, with all optimizations from above and the optimal cutoff.
The average group size is
10
.
The code is available on
GitHub
.
Results
The relative efficiency of the optimized algorithm grows as the data gets larger. Both the straightforward algorithm and the optimized one eventually settle at a fixed throughput. Depending on the machine, the improvement can be anywhere between
2.5
×
and
9
×
in the limit.
The results are (
A
,
Y
,
M
indicate different devices):
Conclusion
Is it worth it? If you absolutely need performance and sharding is a large part of your pipeline, by all means, use this. For example, I use this to find a collision-free hash on a given dataset. But just like with any optimization, you need to consider if increasing the code complexity is worth the hassle.
At the very least, if you work with big data, this trick is good to keep in mind.
Here’s another takeaway lesson. Everyone knows that, when working with on-disk data, you shouldn’t just map it to memory and run typical in-memory algorithms. It’s
possible
, but the performance are going to be bad. The take-away lesson here is that this applies to RAM and cache too: if you’ve got more than, say,
32
MiB of data, you need to seriously consider partitioning your data or switching to external memory algorithms.
