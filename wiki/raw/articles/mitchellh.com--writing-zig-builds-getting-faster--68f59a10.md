---
title: "Zig Builds Are Getting Faster"
url: "https://mitchellh.com/writing/zig-builds-getting-faster"
fetched_at: 2026-04-30T07:01:53.583863+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Zig Builds Are Getting Faster

Source: https://mitchellh.com/writing/zig-builds-getting-faster

Andrew Kelley famously (or infamously, depending on your views) said
"the compiler is too damn slow, that's why we have bugs."
1
As a result, one of the primary stated goals of
Zig
for
years has been faster compile times. The Zig team has been working on
extremely hard problems to make this a reality
(such as
yeeting LLVM
,
writing their own
code generation backends
,
building their own
linkers
,
and marching towards
incremental compilation
in general).
2
The fruits of this multi-year labor are finally starting to show
with Zig 0.15.1. The
Ghostty
project just completed upgrading to
Zig 0.15.1, and I'd like to share some real-world build times.
3
Build Script Compilation
Zig 0.14: 7sec 167ms
Zig 0.15: 1sec 702ms
This is the time it takes to build the
build.zig
script itself. The
times above were measured by running
zig build --help
.
A well-written build script should only rebuild itself rarely. However,
this is a cost every new uncached source build will pay (e.g. a user
downloading the project to build from source one time). As such, it directly
impacts the time to build a usable binary.
Full Uncached Ghostty Binary
Zig 0.14: 41sec
Zig 0.15: 32sec
This includes the time to build the build script itself. Given the prior
results, Zig 0.15 is building everything else ~2 seconds faster. But, you
can still see in wall time the change in this initial build time.
Important: most of this is still using LLVM.
Ghostty still can't fully build and link using
the self-hosted x86_64 backend, since the backend still has bugs. So, this just shows the general
improvements in the Zig compiler itself, even with LLVM in the picture.
Once Ghostty can use the self-hosted x86_64 backend completely, I expect
this time to plummet to around 25 seconds or less, fully half the time it
would take with Zig 0.14.
Incremental Build (Ghostty Executable)
Zig 0.14: 19sec
Zig 0.15: 16sec
This is the time it takes to rebuild Ghostty after a one-line change to
the most core terminal emulation code (adding a log function call to the
escape sequence parser).
This build has a fully cached build script and dependency graph, so it
is only rebuilding what it needs to. Incremental compilation in Zig isn't
functional yet, so this still recompiles a considerable amount of code.
Additionally, as with the prior section,
this is still using LLVM
.
By simply dropping LLVM out of the picture, I expect this time to drop to
around 12 seconds or so (less the time LLVM is emitting).
Going further, once Zig supports incremental compilation, I expect
we'll be able to measure incremental builds like this within milliseconds
at worst. But, let's wait and see when that is reality.
Incremental Build (libghostty-vt)
Zig 0.14: 2sec 884ms
Zig 0.15: 975ms
This is the time it takes to rebuild only
libghostty-vt
after a one-line change. Unlike the Ghostty executable,
libghostty-vt
is fully functional with the self-hosted x86_64 backend, so this
shows the differences in build times without LLVM in the picture.
Similar to the Ghostty executable, this is still rebuilding the full
Zig module for
libghostty-vt
, since incremental compilation isn't
fully functional yet. I expect this to also drop to single-digit milliseconds
at worst once incremental compilation is a reality.
But still, a sub-second build time for a non-trivial library is
amazing
.
This is the library I'm spending most of my time working on right now,
and even in a few short days since upgrading to Zig 0.15.1, I've felt
a huge difference in my workflow. Previously, I might tab out to read an
email between builds or tests, but now its so fast I can stay in flow
in my terminal.
This improvement is most indicative of what's to come in the short term.
The self-hosted x86_64 backend is already stable enough to build all debug
builds by default and the aarch64 backend is getting there, too. We aren't
able to build the full Ghostty executable yet, but I bet this will get
ironed out within months.
Faster Builds Are Here
As you can see, building Ghostty with Zig 0.15.1 is faster in every single
scenario, despite the fact that a lot of Ghostty still can't even take
advantage of the self-hosted backend! And despite the fact that incremental
compilation isn't functional yet!
I've loved betting on Zig for Ghostty, and I love that they're focusing
on compile times. These improvements are real, and they're here now. And
I suspect in the next couple years, the results posted today will look
downright slow. 😜
