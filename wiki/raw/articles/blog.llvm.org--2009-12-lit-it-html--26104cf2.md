---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2009/12/lit-it.html"
fetched_at: 2026-05-05T07:01:44.527929+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2009/12/lit-it.html

One thing both systems had in common was that it was very easy to add a new test, usually a couple lines in a file in the appropriate directory. But there were some annoying cons:
There was no way to run tests via CMake or on Windows.
LLVM tests weren't run in parallel.
The UI to the tests was inconsistent and cumbersome (especially for DejaGNU, which would required invoking the LLVM Makefile via a shell script, which then invoked DejaGNU's runtest command).
I didn't actually set out to write a new testing tool --
lit
started because I had a need to run a very large number of "tests", which was just a fixed script to run with many different inputs. I hacked up a quick multithreaded Python test runner for it, and over time it grew a progress bar and more features. Later, when there was growing interest in having Clang work on Windows I wrote a Python based interpreter for the scripts (remember, they amounted to just shell scripts, so
lit
has what amounts to a little (ba)
sh
lexer and parser hiding in it). It didn't take a lot of imagination to put the two together and feature creep it until it could replace DejaGNU (yeah, it has a tiny Tcl parser too).
So, what
is
lit
? Strictly speaking,
lit
is a test running infrastructure, like DejaGNU. Its primary job is to find tests, execute them, and report the results to the user; it just happens to have built in support for the LLVM and Clang test formats. My number one design goal was that
lit
should "just work" whenever possible -- running a test should be as easy as
$ lit exprs.s
lit: lit.cfg:94: note: using out-of-tree build at '/Volumes/Data/ddunbar/llvm.obj.64'
-- Testing: 1 tests, 2 threads --
PASS: LLVM::MC/AsmParser/exprs.s (1 of 1)
Testing Time: 0.06s
Expected Passes    : 1
no matter if you are using an in-tree or out-of-tree build, testing Clang or LLVM, a regression test or googletest based unit test, on Windows or Unix, and so on. And of course I also wanted it to be fast!
I'm not going to go into more detail on how to use
lit
(since it should be self explanatory or documented) but these are some of the features and benefits we've gotten from switching to
lit
:
LLVM tests run much faster, this improved our buildbot build/test cycle on a fast machine by about 25%, if I recall correctly. I still have a secret desire to make them even faster... one day...
Clang tests work on Windows and have been incorporated into our buildbot. There is still work to be done on LLVM tests.
LLVM/Clang tests work in CMake builds (with Makefiles, Xcode, and Visual Studio generators).
lit
integrates nicely into buildbot, so individual failures get split out into their own log. I hope to continue to improve the UI for diagnosing failures.
The LLVM googletest based unit tests are seamlessly integrated with the other tests. In fact, when using the standard LLVM Makefiles, its possibly to run all LLVM & Clang tests with just
make check-all
.
We're using some of the fancier
lit
features to help with C++ testing. For example, we have custom test suites which run
clang -fsyntax-only
over libstdc++ and the LLVM/Clang headers to test the parser, or which run
clang -c
over the LLVM and Clang C++ code to test Clang's C++ code generation. I secretly suspect Doug of having more
lit
test suites hiding on his hard drive.
And I have more improvements in store...
You can read the
lit
man page
here
, and I hope to add more information to the LLVM
Testing Guide
once all the pieces are fully in place. Try it out, I hope you like it!
- Daniel
p.s.
lit
stands for LLVM Integrated Tester, at least thats what I publicly claim. That, or it's the first three letter pronounceable name I came up with...
