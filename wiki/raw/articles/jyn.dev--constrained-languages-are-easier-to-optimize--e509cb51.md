---
title: "constrained languages are easier to optimize"
url: "https://jyn.dev/constrained-languages-are-easier-to-optimize/"
fetched_at: 2026-04-28T07:02:50.736154+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# constrained languages are easier to optimize

Source: https://jyn.dev/constrained-languages-are-easier-to-optimize/

jyn, what the fuck are you talking about
a recurring problem in modern “low-level” languages is that they are hard to optimize. they
do not reflect the hardware
, they require doing
complex alias analysis
, and they
constantly allocate and deallocate memory
.  they looked at
the structure/expressiveness tradeoff
and consistently chose expressiveness.
what does a faster language look like
consider this paper on
stream fusion in Haskell
. this takes a series of nested loops, each of which logically allocate an array equal in size to the input, and optimizes them down to constant space using unboxed integers. doing the same with C is inherently less general because the optimizing compiler must first prove that none of the pointers involved alias each other. in fact, optimizations are so much easier to get right in Haskell that
GHC exposes a mechanism for users to define them
! these optimizations are possible because of
referential transparency
—the compiler statically knows whether an expression can have a side effect.
“haskell is known for performance problems, why are you using it as an example. also all GC languages constantly box and unbox values, you need raw pointers to avoid that.”
GC languages do constantly box and unbox , but you don’t need raw pointers to avoid that. consider
futhark
, a functional parallel language that compiles to the GPU. its benchmarks show it being
up to orders of magnitude faster than sequential C
on problems that fit well into its domain. it does so by having unboxed fixed-size integers, disallowing ragged arrays, and constraining many common operations on arrays to only work if the arrays are statically known to have the same size.
futhark is highly restrictive. consider instead SQL. SQL is a declarative language, which means the actual execution is determined by a query planner, it’s not constrained by the source code. SQL has also been around for decades, which means we can compare the performance of the same code over decades. it turns out
common operations in postgres are twice as fast as they were a decade ago
. you can imagine writing SQL inline—wait no it turns out C#
already has that covered
.
SQL is not a general purpose language. but you don’t need it to be! your performance issues are not evenly distributed across your code; you can identify the hotspots and choose against a language with raw pointers in favor of one more structured and therefore more amenable to optimization.
sometimes you need raw pointers
there are various kinds of memory optimizations that are only possible if you have access to raw pointers; for example
NaN boxing
,
XOR linked lists
, and
tagged pointers
. sometimes you need them, which means you need a language that allows them. but these kinds of data structures are very rare! we should steer towards a general purpose language that does not expose raw pointers, and only drop down when we actually need to use them.
what does a faster general purpose language look like
well, Rust is a good step in the right direction: raw pointers are opt-in with
unsafe
; Iterators support functional paradigms that allow removing bounds checks and
fusing stream-like operations
; and libraries like
rayon
make it much easier to do multi-threaded compilation.
but i think this is in some sense the wrong question. we should not be asking “what language can i use everywhere for every purpose”; we should build meta-languages that allow you to easily use the right tool for the job. this is already true for regular expressions and query languages; let’s go further. i want inline futhark; inline CSS selectors; inline datalog; ffi between python and C that’s trivially easy. the easier we make it to interop, the easier it becomes to pick the right tool for the job.
next time you hit a missed optimization, ask yourself: why was this hard for the compiler? can i imagine a language where optimizing this is easier?
what have we learned?
languages that expose raw pointers are surprisingly hard to optimize
by constraining the language to require additional structure, the compiler has much more freedom to optimize
by making it easier to switch between languages, we make it easier to choose the right tool for the job, increasing the performance of our code
