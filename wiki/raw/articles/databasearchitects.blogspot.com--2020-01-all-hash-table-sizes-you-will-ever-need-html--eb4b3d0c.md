---
title: "All hash table sizes you will ever need"
url: "https://databasearchitects.blogspot.com/2020/01/all-hash-table-sizes-you-will-ever-need.html"
fetched_at: 2026-05-05T07:01:29.463370+00:00
source: "Database Architects"
tags: [blog, raw]
---

# All hash table sizes you will ever need

Source: https://databasearchitects.blogspot.com/2020/01/all-hash-table-sizes-you-will-ever-need.html

When picking a hash table size we usually have two choices: Either, we pick a prime number or a power of 2. Powers of 2 are easy to use, as a modulo by a power of 2 is just a bit-wise and, but 1) they waste quite a bit of space, as we have to round up to the next power of 2, and 2) they require "good" hash functions, where looking at just a subset of bits is ok.
Prime numbers are more forgiving concerning the hash function, and we have more choices concerning the size, which leads to less overhead. But using a prime number requires a modulo computation, which is expensive. And we have to find a suitable prime number at runtime, which is not that simple either.
Fortunately we can solve both problems simultaneously, which is what this blog post is about. We can tackle the problem of finding prime numbers by pre-computing suitable numbers with a given maximum distance. For example when when only considering prime numbers that are at least 5% away from each other we can cover the whole space from 0 to 2^64 with just 841 prime numbers. We can solve the performance problem by pre-computing the
magic numbers
from
Hacker's Delight
for each prime number in our list, which allows us to use multiplications instead of expensive modulo computations. And we can skip prime numbers with unpleasant magic numbers (i.e., the ones that require an additional add fixup), preferring the next cheap prime number instead.
The resulting code can be found
here
. It contains every prime number you will ever need for hash tables, covering the whole 64bit address space. Usage is very simple, we just ask for a prime number and then perform modulo operations as needed:
class HashTable {
   primes::Prime prime;
   vector
table;
public:
   HashTable(uint64_t size) {
prime = prime::Prime::pick(size);
table.resize(prime.get());
}
   ...
   Entry* getEntry(uint64_t hash) { return table[prime.mod(hash)]; }
   ...
};
The performance is quite good. On an AMD 1950X, computing the modulo for 10M values (and computing the sum of the results) takes about 4.7ns per value when using a plain (x%p), but only 0.63ns per value when using p.mod(x).
Getting this into
unordered_map
would be useful, it would probably improve the performance quite significantly when we have few cache misses.
