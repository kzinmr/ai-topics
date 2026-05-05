---
title: "LLVM Weekly - #23, Jun 9th 2014"
url: "https://blog.llvm.org/2014/06/llvm-weekly-23-jun-9th-2014.html"
fetched_at: 2026-05-05T07:01:42.153345+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM Weekly - #23, Jun 9th 2014

Source: https://blog.llvm.org/2014/06/llvm-weekly-23-jun-9th-2014.html

LLVM Weekly - #23, Jun 9th 2014
Welcome to the twenty-third issue of LLVM Weekly, a weekly newsletter (published every Monday) covering developments in LLVM, Clang, and related projects. LLVM Weekly is brought to you by
Alex Bradbury
. Subscribe to future issues at
http://llvmweekly.org
and pass it on to anyone else you think may be interested. Please send any tips or feedback to
asb@asbradbury.org
, or
@llvmweekly
or
@asbradbury
on Twitter.
The canonical home for this issue
can be found here at llvmweekly.org
.
News and articles from around the web
Philip Reames has
announced that code for late safepoint placement is now available
.
This is a set of patches to LLVM from Azul Systems that aim to support precise relocating garbage collection in LLVM. Phlip has a long list of questions where he is seeking feedback from the community on how to move forwards with these patches. There's not been much response so far, hopefully it will come soon as I know there are many communities who are very interested in seeing better GC support in LLVM (e.g. Rust, Ocaml).
The biggest LLVM news this week is of course the announcement of
the Swift programming language
from Apple. Its development was led by Chris Lattner, original author of LLVM. He has some more info about Swift
on his website
. There is no source release as of yet, and
no indication
from Apple as to whether it will remain proprietary. Either way, it's an interesting development. Chris Lattner is now on Twitter and has been
passing out tidbits about the Swift implementation
.
LunarG have
announced the Glassy Mesa project
. This project, funded by Valve, will explore increasing game performance in Mesa through improvements in the shader compiler. The current parser and optimisation layer are replaced with glslang and the LLVM-based LunarGlass. More technical details are
available in the slide deck
.
Sébastien Métrot has released
xspray
, a frontend for lldb on OS X. One of its interesting features is the inbuilt support for plotting your data.
With all the LLVM news recently, it seems
search traffic for 'llvm' has skyrocketed
.
On the mailing lists
LLVM commits
The jumptable attribute has been introduced. If you mark a function with this attribute, references to it can be rewritten with a reference to the appropriate jump-instruction-table function pointer.
r210280
.
Support was added for Windows ARM exception handling data structures, including decoding them.
r209998
,
r210192
.
GlobalAlias can now point to an arbitrary ConstantExpression. See the commit message for a discussion of the consequences of this.
r210062
.
The subword level parallelism (SLP) vectorizer has been extended to support vectorization of getelementptr expressions.
r210342
.
The LLVM programmer's manual has been improved with an example of using IRBuilder.
r210354
.
Clang commits
Semantic analysis to make sure a loop is in OpenMP canonical form has been committed.
r210095
.
__builtin_operator_new
and
__builtin_operator_delete
have been added. Some optimisations are allowed on these which would not be on
::operator new
and are intended for the implementation of things like std::allocator.
r210137
.
New pragmas have been introduced to give optimisation hints for vectorization and interleaving. You can now use
#pragma clang loop vectorize(enable)
as well as
vectorize(disable)
,
vectorize_width(n)
,
interleave(enable/disable)
, and
interleave_count(n)
.
r210330
.
Support for the MSVC++ ABI continues with the addition of
dynamic_cast
for MS.
r210377
.
Support for global named registers has been expanded slightly to allow pointer types to be held in these variables.
r210274
.
GCC's
-Wframe-larger-than=bytes
diagnostic is now supported.
r210293
.
Other project commits
A benchmarking-only mode has been added to the testsuite
r210251
.
A
status page
for post-C++14 features in libcxx has been added.
r210056
.
An initial set of Makefiles has been committed to lld.
r210177
.
lldb gained support for inspecting enum members.
r210046
.
Polly can now be built without any GPLed software.
r210176
.
