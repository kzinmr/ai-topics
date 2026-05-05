---
title: "C++ Concurrency Model on x86 for Dummies"
url: "https://databasearchitects.blogspot.com/2020/10/c-concurrency-model-on-x86-for-dummies.html"
fetched_at: 2026-05-05T07:01:29.295370+00:00
source: "Database Architects"
tags: [blog, raw]
---

# C++ Concurrency Model on x86 for Dummies

Source: https://databasearchitects.blogspot.com/2020/10/c-concurrency-model-on-x86-for-dummies.html

Since C++11, multi-threaded C++ code has been governed by a rigorous memory model. The model allows implementing concurrent code such as low-level synchronization primitives or lock-free data structures in a portable fashion. To use the memory model, programmers need to do two things: First, they have to use the
std::atomic
type for concurrently-accessed memory locations. Second, each atomic operation requires a memory order argument with six options determining the concurrency semantics in terms of which re-orderings are allowed. (Some operations even allow specifying two memory orders!)
While there are a number of attempts to describe the model, I always found the full semantics very hard to understand and consequently concurrent code hard to write and reason about. And since we are talking about low-level concurrent code here, making a mistake (like picking the wrong memory order) can lead to disastrous consequences.
Luckily, at least on x86, a small subset of the full C++11 memory model is sufficient. In this post, I'll present such a subset that is sufficient to write high-performance concurrent code on x86. This simplification has the advantage that the resulting code is much more likely to be correct, without leaving any performance on the table. (On non-x86 platforms like ARM, code written based on this simplified model will still be correct, but might potentially be slightly slower than necessary.)
There are only six things one needs to know to write high-performance concurrent code on x86.
1. Data races are undefined
If a data race occurs in C++, the behavior of the program is undefined. Let's unpack that statement. A data race can be defined as two or more threads accessing the same memory location with at least one of the accesses being a write. By default (i.e., without using
std::atomic
), the compiler may assume that no other thread is concurrently modifying memory. This allows the compiler to optimize the code, for example by reordering or optimizing away memory accesses. Consider the following example:
void
wait(bool* flag) {
while
(*flag);
}
Because data races are undefined, the compiler may assume that the value behind the pointer
flag
is not concurrently modified by another thread. Using this assumption,
gcc translates
the code to a return statement while
clang translates
it to an infinite loop if
flag
is initially true. Both translations are likely not what the code intends. To avoid undefined code, it is necessary use
std::atomic
for variables where race conditions may happen:
void
wait(std::atomic<bool>* flag) {
while
(*flag); // same as while(flag->load(std::memory_order_seq_cst));
}
*flag
is equivalent to
flag.load(std::memory_order_seq_cst)
, i.e., the default memory order is sequential consistency. Sequential consistency is the strongest memory order guaranteeing that atomic operations are executed in program order. The compiler is not allowed to reorder memory operations or optimize them away.
2. Sequentially-consistent loads are fast
Making the flag atomic may seem expensive, but luckily atomic loads are cheap on x86. Indeed, our wait function is
translated
to a simple loop with a simple MOV instruction, without any barrier/fence instruction. This is great as it means that on x86 an atomic, sequentially-consistent load can be just as fast as a normal load. It also means that on x86 there is no performance benefit of using any weaker memory order for atomic loads. For loads all memory orders are simply translated to MOV.
3. Sequentially-consistent stores are slow
While sequentially-consistent atomic loads are as cheap as normal loads, this is not the case for stores, as can be observed from the following example:
void
unwait(std::atomic<bool>* flag) {
*flag = false; // same as flag->store(false, std::memory_order_seq_cst);
}
As with atomic loads, atomic stores are sequentially consistent if no explicit memory order is specified. In clang and gcc 10, the store
translates
to an XCHG instruction rather than a MOV instruction (older gcc versions
translate
it to a MOV plus MFENCE.). XCHG and MFENCE are fairly expensive instructions but are required for sequentially consistent stores on x86. (The CPU's store buffer must be flushed to L1 cache to make the write visible to other threads through cache coherency.)
4. Stores that can be delayed can benefit from the
release
memory order
Because sequentially-consistent stores are fairly expensive, there are situations where a weaker memory order can improve performance. A common case is when the effect of a store can be delayed. The classical example is unlocking a mutex. The unlocking thread does not have to synchronously wait for the unlocking to become visible, but can continue executing other instructions. Another way of saying this is that it is correct to move instructions into the critical section, but not out of it. In C++, this weaker form of store consistency is available through the release memory order.
In our unwait example, the store can indeed be delayed, which is why we can use the release memory order for the store:
void
unwait(std::atomic<bool>* flag) {
flag->store(false, std::memory_order_release);
}
This code is
translated
to a simple MOV instruction, which means it can be as efficient as a non-atomic store.
5. Some atomic operations are always sequentially consistent
Besides loads and stores,
std::atomic
also offers the high-level atomic operations
compare_exchange
,
exchange
,
add
,
sub
,
and
,
or
,
xor
. On x86, these are always directly translated to sequentially-consistent CPU instructions. This means that there is no performance benefit from specifying weaker memory orders on any of these operations. (An atomic increment with release semantics would be useful in many situations, but alas is not available.)
6. Scalable code should avoid cache invalidations
I mentioned above that sequentially-consistent loads and release stores may be as cheap as non-atomic loads/store. Unfortunately, this is not always the case. Because CPUs have per-core caches, the performance of concurrent programs depends on the dynamic access pattern. Every store has to invalidate any cached copies of that cache line on other cores. This can cause parallel implementations to be slower than single-threaded code. Therefore, to write scalable code, it is important to minimize the number of writes to shared memory locations. A positive way of saying this is that as long as the program does not frequently write to memory locations that are frequently being read or written, the program will scale very well. (
Optimistic lock coupling
, for example, is a general-purpose concurrency scheme for synchronizing data structures that exploits this observation.)
Summary
The full C++ memory model is notoriously hard to understand. x86, on the other hand, has a fairly strong memory model (
x86-TSO
) that is quite intuitive: basically everything is in-order, except for writes, which are delayed by the write buffer. Exploiting x86's memory model, I presented a simplified subset of the C++ memory model that is sufficient to write scalable, high-performance concurrent programs on x86.
