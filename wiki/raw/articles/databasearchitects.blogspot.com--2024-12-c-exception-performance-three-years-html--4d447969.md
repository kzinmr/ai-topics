---
title: "C++ exception performance three years later"
url: "https://databasearchitects.blogspot.com/2024/12/c-exception-performance-three-years.html"
fetched_at: 2026-05-05T07:01:27.592542+00:00
source: "Database Architects"
tags: [blog, raw]
---

# C++ exception performance three years later

Source: https://databasearchitects.blogspot.com/2024/12/c-exception-performance-three-years.html

About three years ago we noticed serious
performance problems in C++ exception unwinding
. Due to contention on the unwinding path these became more and more severe the more cores a system had, and unwinding could slow down by orders of magnitude. Due to the constraints of backwards compatibility this contention was not easy to eliminate, and
P2544
discussed ways to fix this problem via language changes in C++.
But fortunately people found less invasive solutions. First, Florian Weimer
changed the glibc
to provide a lock-free mechanism to find the (static) unwind tables for a given shared object. Which eliminates the most serious contention for "simple" C++ programs. For example in a
micro-benchmark
that calls a function with some computations (100 calls to sqrt per function invocation), and which throws with a certain probability, we previously had very poor scalability with increasing core count. With his patch we now see with gcc 14.2 on a dual-socket EPYC 7713 the following performance development (runtime in ms):
1
2
4
8
16
32
64
128
threads
0% failure
29
29
29
29
29
29
29
42
0.1% failure
29
29
29
29
29
29
29
32
1% failure
29
30
30
30
30
30
32
34
10% failure
36
36
37
37
37
37
47
65
Which is more or less perfect. 128 threads are a bit slower, but that is to be expected as one EPYC only has 64 cores. With higher failure rates unwinding itself becomes slower but that is still acceptable here. Thus most C++ programs are just fine.
For
our use case
that is not enough, though. We dynamically generate machine code at runtime, and we want to be able to pass exceptions through generated code. The _dl_find_object mechanism of glibc is not used for JITed code, instead libgcc maintains its own lookup structure. Historically this was a simple list with a global lock, which of course had terrible performance. But through
a series of patches
we managed to change libgcc into using a
lock-free b-tree
for maintaining the dynamic unwinding frames. Using a similar experiment to the one above, but now with JIT-generated code (using LLVM 19), we get the following:
1
2
4
8
16
32
64
128
threads
0% failure
32
38
48
64
48
36
59
62
0.1% failure
32
32
32
32
32
48
62
68
1% failure
41
40
40
40
53
69
80
83
10% failure
123
113
103
116
128
127
131
214
The numbers have more noise than for statically generated code, but overall observation is the same: Unwinding now scales with the number of cores, and we can safely use C++ exceptions even on machines with large core counts.
So is everything perfect now? No. First, only gcc has a fully scalable frame lookup mechanism. clang has its own implementation, and as far as I know it still does not scale properly due to a global lock in DwarfFDECache. Note that at least on many Linux distributions clang uses libgcc by default, thus the problem is not immediately obvious there, but a pure llvm/clang build will have scalability problems. And  second unwinding through JIT-ed code is a quite a bit slower, which is unfortunate. But admittedly the problem is less severe than shown here, the benchmark with JITed code simply has a stack frame more to unwind due to the way static code and JITed code interact. And it makes sense to prioritize static unwinding over dynamic unwinding frames, as most people never JIT-generate code.
Overall we are now quite happy with the unwinding mechanism. The bottlenecks are gone, and performance is fine even with high core counts. It is still not appropriate for high failure rates, something like
P709
would be better for that, but we can live with the status quo.
