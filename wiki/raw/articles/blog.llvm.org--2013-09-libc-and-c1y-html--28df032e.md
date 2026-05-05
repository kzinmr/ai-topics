---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2013/09/libc-and-c1y.html"
fetched_at: 2026-05-05T07:01:42.990186+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2013/09/libc-and-c1y.html

libc++ and C++1Y
I am proud to announce that as of September 21, libc++ has a full implementation of the C++1Y standard library.
In April of 2013, the C++ standards committee approved a draft version of the next revision of the C++ language, called "C++1Y". (C++11 was called "C++0x" while in development). We hope that this draft standard will be approved next year, and become C++14.
The draft standard includes changes to both the language and the standard library. These changes are designed to correct some mistakes that have been discovered in the C++11 standard and to add new features.
Both clang and libc++ are being enhanced to support this new standard, and they each have a web page to show their current progress:
clang C++1Y Status
and
libc++ C++1Y status
.
The C++ standards committee is meeting this week (September 23-28) to consider comments and defect reports in the C++1Y draft standard, and there will certainly be changes made.
We could have waited until the final version of the C++1Y standard was approved; that would certainly have been less work. The draft standard will to be revised in September (and probably in February), so the libc++ implementation will have to change to track the standard.
However, by implementing the draft standard has several advantages.
We gain experience in working with the new standard.
We found several places where the changes to the draft standard "exposed" other places were improvements can be made. For example, while implementing the new
optional
feature made it clear that interface of the the comparison functions
plus
,
less
(and others) could be enhanced. The result of that was the new paper
n3749
.
By implementating the standard, we can identify problems/inconsistencies in the draft standard. For example, when we implemented the new library feature
dynarray
, we discovered that the interfaces for the allocator-based constructors for the container were
wrong
; in particular there were cases where it was not possible for the compiler to determine the correct constructor to call. This was raised as
LWG Issue 2255
, and will have to be resolved before the standard becomes final.
