---
title: "Simple guided fuzzing for libraries using LLVM's new libFuzzer"
url: "https://blog.llvm.org/2015/04/fuzz-all-clangs.html"
fetched_at: 2026-05-05T07:01:40.751928+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Simple guided fuzzing for libraries using LLVM's new libFuzzer

Source: https://blog.llvm.org/2015/04/fuzz-all-clangs.html

Fuzzing (or
fuzz testing
) is becoming increasingly popular. Fuzzing Clang and fuzzing
with
Clang is not new: Clang-based
AddressSanitizer
has been used for fuzz-testing the Chrome browser for
several years
and Clang itself has been extensively fuzzed using
csmith
and, more recently, using
AFL
.
Now we’ve closed the loop and started to fuzz parts of LLVM (including Clang) using LLVM itself.
LibFuzzer
, recently added to the LLVM tree, is a library for in-process fuzzing that uses
Sanitizer Coverage instrumentation
to guide test generation.
With LibFuzzer one can implement a guided fuzzer for some library by writing one simple function:
extern "C" void TestOneInput(const uint8_t *Data, size_t Size);
We have implemented two fuzzers on top of LibFuzzer:
clang-format-fuzzer
and
clang-fuzzer
.
Clang-format is mostly a lexical analyzer, so giving it random bytes to format worked perfectly and discovered
over 20 bugs
. Clang however is more than just a lexer and giving it random bytes barely scratches the surface, so in addition to testing with random bytes we also fuzzed Clang in
token-aware mode
. Both modes found
bugs
; some of them were previously
detected
by AFL
, some others were not: we’ve run this fuzzer with AddressSanitizer and some of the bugs are not easily discoverable without it.
Just to give you the feeling, here are some of the input samples discovered by the token-aware clang-fuzzer starting from an empty test corpus:
static void g(){}
signed*Qwchar_t;
overridedouble++!=~;inline-=}y=^bitand{;*=or;goto*&&k}==n
int XS/=~char16_t&s<=const_cast<Xchar*>(thread_local3+=char32_t
Fuzzing is not a one-off thing -- it shines when used continuously. We have set up a
public build bot
that runs clang-fuzzer and clang-format-fuzzer 24/7. This way, the fuzzers keep improving the test corpus and will periodically find old bugs or fresh regressions (the bot has
caught
at least one such regression already
).
The benefit of in-process fuzzing compared to out-of-process is that you can test more inputs per second. This is also a weakness: you can not effectively limit the execution time for every input. If some of the inputs trigger superlinear behavior, it may slow down or paralyze the fuzzing. Our fuzzing bot was nearly dead after it discovered
exponential parsing time in clang-format
. You can workaround the problem by setting a timeout for the fuzzer, but it’s always better to fix superlinear behavior.
It would be interesting to fuzz other parts of LLVM, but a requirement for in-process fuzzing is that the library does not crash on invalid inputs. This holds for clang and clang-format, but not for, e.g., the LLVM bitcode reader.
Help is more than welcome! You can start by fixing one of the existing bugs in clang or clang-format (see
PR23057
,
PR23052
and the
results from AFL
)
or write your own fuzzer for some other part of LLVM or profile one of the existing fuzzers and try to make it faster by fixing performance bugs.
Of course, LibFuzzer can be used to test things outside of the LLVM project. As an example, and following
Hanno Böck’s blog post
on
Heartbleed
, we’ve applied LibFuzzer to
openssl
and found Heartbleed in
less than a minute
. Also, quite a few new bugs have been discovered in
PCRE2
(
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
,
10
,
11
),
Glibc
and
MUSL libc
(
1
,
2
)
.
Fuzz testing, especially coverage-directed and sanitizer-aided fuzz testing, should directly compliment unit testing, integration testing, and system functional testing. We encourage everyone to start actively fuzz testing their interfaces, especially those with even a small chance of being subject to attacker-controlled inputs. We hope the LLVM fuzzing library helps you start leveraging our tools to better test your code, and let us know about any truly exciting bugs they help you find!
