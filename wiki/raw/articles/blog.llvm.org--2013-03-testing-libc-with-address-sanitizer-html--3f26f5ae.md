---
title: "Testing libc++ with Address Sanitizer"
url: "https://blog.llvm.org/2013/03/testing-libc-with-address-sanitizer.html"
fetched_at: 2026-05-05T07:01:43.433446+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Testing libc++ with Address Sanitizer

Source: https://blog.llvm.org/2013/03/testing-libc-with-address-sanitizer.html

Testing libc++ with Address Sanitizer
[This article is re-posted in a slightly expanded form
from Marshall's blog
]
I've been running the libc++ tests off and on for a while. It's a quite extensive test suite, but I wondered if there were any bugs that the test suite was not uncovering. In the upcoming clang 3.3, there is a new feature named
Address Sanitizer
which inserts a bunch of runtime checks into your executable to see if there are any "out of bounds" reads and writes to memory.
In the back of my head, I've always thought that it would be nice to be able to say that libc++ was "ASan clean" (i.e, passed all of the test suite when running with Address Sanitizer).
So I decided to do that.
[ All of this work was done on Mac OS X 10.8.2/3 ]
How to run the tests:
There's a script for running the tests. It's called
testit
.
$ cd $LLVM/libcxx/test ; ./testit
where $LLVM/libcxx is where libc++ is checked out. This takes about 30 minutes to run. Without Address Sanitizer, libc++ fails 12 out of the 4348 tests on my system.
Running the tests with Address Sanitizer
$ cd $LLVM/libcxx/test ; CC=/path/to/tot/clang++ OPTIONS= "-std=c++11 -stdlib=libc++ -fsanitize=address" ./testit
Note: the default options are "-std=c++11 -stdlib=libc++", that's what you get if you don't specify anything
.This takes about 92 minutes; just a bit more than three times as long. With Address Sanitizer, libc++ fails 54 tests (again, out of 4348)
What are the failures?
In 11 tests, Address Sanitizer detected a one-byte write outside a heap block. All of these involve iostreams. I created a small test program that ASan also fires on, and sent it to Howard Hinnant (who wrote most of libc++), and he found a place where he was allocating a zero-byte buffer by mistake. One bug, multiple failures. He fixed this in revision
177452
.
2 tests for std::random were failing. This turned out to be an off-by-one error in the test code, not in libc++. I fixed these in revisions
177355
and
177464
.
Address Sanitizer detected memory allocations failing in 4 cases. This is expected, since some of the tests are testing the memory allocation system of libc++. However, it appears that ASan does not call the user-supplied
new_handler
when memory allocation fails (and may not throw
std::bad_alloc
, ether). I have filed
PR15544
to track this issue.
25 cases are failing where the program is failing to load, due to a missing symbol. This is most commonly
std::__1::__get_sp_mut(void const *)
, but there are a couple others. Howard says that this was added to libc++ after 10.8 shipped, so it's not in the dylib in /usr/lib. If the tests are run with a copy of libc++ built from source, they pass.
There are the 12 cases that were failing before enabling Address Sanitizer.
Once Howard and I fixed the random tests and the bug in the iostreams code, I re-ran the tests using a recently build libc++.dylib.
$ cd $LLVM/libcxx/test ; DYLD_LIBRARY_PATH=$LLVM/libcxx/lib CC=/path/to/tot/clang++ OPTIONS= "-std=c++11 -stdlib=libc++ -fsanitize=address" ./testit
This gave us 16 failures:
The 4 failures that have to do with memory allocation failures.
The 12 failures that we started with.
Conclusion
I'm glad to see that there were so few problems in the libc++ code. It's a fundamental building block for applications on Mac OS X (and, as llvm becomes more popular, other systems). And now it's better than it was when we started this exercise.However, we did find a couple bugs in the test suite, and one heap-smashing bug in libc++. We also found a limitation in Address Sanitizer, too - which the developers are working on addressing.
