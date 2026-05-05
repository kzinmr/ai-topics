---
title: "Switching From C++ to Rust"
url: "https://laplab.me/posts/switching-from-cpp-to-rust/"
fetched_at: 2026-05-05T07:01:24.523080+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# Switching From C++ to Rust

Source: https://laplab.me/posts/switching-from-cpp-to-rust/

Discussion on
HackerNews
and
Lobsters
.
I have been writing C++ professionally for the last 4 years and 3 months ago I started a new job in Rust. I would like to share my experience and thoughts on the transition between 2 languages.
Disclaimer:
This article is
not
a C++ vs Rust comparison. I will talk about my personal experience and things which are important to me, not the engineering community in general.
What kind of C++ and Rust?
I think that the kind of work one does greatly influences the experience with the language, so let’s talk about background.
With C++, I have spent the majority of my time writing databases. Databases are anything but a typical application – they often assume a complete ownership of the host they are running on, use a huge subset of available system calls and in some cases bypass the kernel completely. On the other hand, this makes database an interesting specimen to study a particular language, because you need to care about performance, provide a nice user experience for the customer and be correct all at the same time.
My current company is under innumerable NDA blankets, so I cannot share a lot of details on my job. The environment I use Rust in is number crunching asynchronous server with high load and high bar for performance requirements. It sort of similar to a database, but the user experience is probably not the main focus here.
I will say that these two are similar enough for the purposes of this article.
The thing everybody talks about
We get it, Rust has memory safety guarantees. I think this topic has a pretty good coverage online, so I will be brief. After 4 years of C++, I was still getting occasional memory-related server crashes from the code that was already reviewed and merged. It is very hard to say what percentage of those made it to production environments because people just restart the server when segfault happens, so I won’t say anything. Fuzzing does wonders to ensure weird cases are covered, but it is not a silver bullet. All in all, I feel more at peace shipping Rust code that C++ code.
Build system
There are very few things in my life I hate more than building C++ code. As a developer, I want to come to a project and be able to write single short command to build the whole thing. Nothing is more terrifying than the phrase “You just need to run these two commands before building the server…” because it indicates that the build process is
multi-step
. Do I run these two commands every time? What do you mean I need to run them only when
these two
files change? How these commands change if I want to build the project with sanitizers? What do you mean the sanitizers are not supported by the build process? Why the build script suddenly started printing linker errors?
It might seem like I am pulling these questions out of thin air to make a point. I really wish I did. I have just roughly described onboarding in one of the projects I was working on. So yeah, the absense of a unified build system really hurts. Bazel is a step in the right direction. I still have nightmares about CMake.
After all of this, coming to Rust feels like I was suddenly forgiven and moved from Hell to Heaven. You
can
just write single short command to build the whole thing. What is even more important, every other project in the wild uses the same build system, so you do not need to convert build scripts from their system to yours (a very relevant problem in writing closed-source C++). A line in
Cargo.toml
is all that is required to include a dependency in the build process. It even passes the right compilation flags to it automatically, come on!
Compiler
Error messages from both compilers can be overwhelming and require effort to understand and fix properly. However, the reasons for this are different.
In C++, you can comfortably measure the size of error messages in kilobytes. Infinite scroll in the terminal emulator is an absolute must because oh boy does the compiler like printing text. After a few years, you develop a certain intuition to decide if it makes sense to read the error or try to stare at your code for a while, depending on the error size. Usually the bigger the error, the more effective random staring at the code is. I do not see how this problem can be solved without changing the way C++ templates are defined.
In Rust, the compiler error (after fixing all obvious typos) is usually very bad news. It is quite often an indicator that you need to restructure your code in some way or spend some time massaging the lifetimes so that it is obvious that you cannot misuse the memory. This takes time and can be quite annoying, but the right approach here is to carefully listen to the compiler’s wisdom. This is a humbling experience, but it often produces better code. The error messages also fit on my screen, which is nice.
Type system
It is a pleasure to express ideas in Rust’s type system.
First of all, generics
without
duck typing are greatly appreciated. Traits clearly indicate the contract struct or function expects from the type, which is great. This also helps compiler to generate helpful error messages. Instead of “invalid reference to method clone() on line Y” you get “type X does not implement Clone” - clean and informative.
Second of all, enums are insanely powerful.
Result
and
Option
are useful concepts, but what makes them fantastic is the fact that everybody uses them. These two enums are common language for all libraries (including the standard one) to express fallible computation and optional value. In C++ we have (1) returning error code; (2) returning invalid value; (3) raising an exception
; (4) crashing the process
. All questionable options and each library uses a different one. Apart from
Result
and
Option
, I found the ability to easily define tagged enums very handy on its own.
Conclusion
Altogether, Rust feels like a major improvement for my day-to-day developer experience. The tooling is friendly and helpful, the language is expressive and powerful. I really enjoy it and hope it will avoid some of the C++ pitfalls in the future.
