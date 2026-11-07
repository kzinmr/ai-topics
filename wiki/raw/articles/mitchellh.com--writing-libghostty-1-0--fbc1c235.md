---
title: "Mitchell Hashimoto"
url: "https://mitchellh.com/writing/libghostty-1-0"
fetched_at: 2026-11-07T10:01:29.677120+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Mitchell Hashimoto

Source: https://mitchellh.com/writing/libghostty-1-0

libghostty-vt
1.0 is here.
libghostty
is a
portable, high-performance C library for terminal emulation, extracted
directly from the core of Ghostty. The 1.0 release means both the library
itself and the C ABI are now stable.
A little over a year ago, I wrote that
libghostty is coming
. At the time,
the Zig module had just been merged, the C API didn't exist, and nobody
but Ghostty was a consumer. Today, the C API is a complete terminal emulator,
it runs in production for millions of people across hundreds of products,
both free and commercial, and it has a real, enforced ABI stability policy.
This post is about how we got here and what 1.0 actually means.
1
Who Is Already Using It
Since starting the Ghostty project in 2022, the most common question I've
been asked is "why?". I already answered this in the
libghostty is coming
post, so feel free to read that if you wish. Today, I'd rather answer this
by showing the broad industry impact libghostty
has already had
. I believe
this strongly validates its existence.
A year ago, I used a
bug in JediTerm
,
the terminal emulator in JetBrains IDEs, as an example of why terminal
emulation is hard to get right. A year later,
the terminal in JetBrains IDEs now runs on libghostty
.
Every IntelliJ, PyCharm, GoLand, etc. user now has a libghostty-powered
terminal. Based on a report by JetBrains, that's over 12.5 million
active users.
Neovim has an
approved pull request
replacing libvterm with
libghostty-vt
. Among other things, it closes a
10-year-old issue
about reflowing scrollback on resize. The maintainers are waiting on a
tagged release before merging so that distributions can package the
dependency separately, and the release today should enable that.
KDE developers are
experimenting with a Konsole replacement
built on it. Vercel's Turborepo
uses it
to render task output in its TUI.
devenv
uses it to drive shells. Antithesis
used it to fuzz TUI programs
and found real bugs in btop and others.
Ghostel
brings it to Emacs.
ghostty-web
is the WASM build with an Xterm.js-compatible API. Commercial products
like
OrbStack
embed it. And a whole wave of
new terminals and "agentic" coding tools, such as
herdr
and
cmux
, have been built on it
rather than writing yet another emulator.
There are community bindings for Rust, Go, JavaScript, Swift, Python,
.NET, Elixir, Dart, Java, and more, and the
awesome-libghostty
list tracks well over a hundred projects.
More people today use a terminal powered by libghostty than use Ghostty
the application, by a very large multiple. And libghostty is having
a much larger impact than being "just" a terminal emulator.
2
ABI Stability
1.0 means
libghostty-vt
follows semantic versioning and has strict
ABI compatibility
promises so that packagers across distributions and operating systems
can be confident packaging
libghostty-vt
and program developers can be
confident dynamically linking against it.
Beyond providing useful features, I believe the hallmark of a high-quality
and enduring C library is ABI stability. So from the start, I took inspiration
from C libraries I enjoyed working with and designed the API to have
a strong, stable ABI that allows for future additions.
Every object is an opaque handle. The hundreds of values you might read or
write go through a small set of enum-keyed getters and setters, so we
can add new values easily without introducing a new symbol. Programs with
newer headers linked against an older libghostty get
GHOSTTY_UNSUPPORTED
results instead of crashes or undefined behavior. The few non-opaque structs
we have carry their size so that fields can be appended later, or contain
reserved padding. Enums are pinned to
int
on every compiler, as much as
the C standard allows.
Our CI enforces our ABI policy. Every change is checked with
libabigail
against a committed baseline
on Linux, and against golden type manifests on macOS and WebAssembly.
On ELF platforms, every exported symbol is also versioned, so the dynamic
loader refuses to load a mismatched library by name rather than failing in
some mysterious way later.
Packaging
In addition to ABI stability, the 1.0 release brings along the proper
build tooling, tarballs, dependency licensing manifests, documentation,
and more to enable every major operating system and distribution to
package
libghostty-vt
through standard official tooling.
Libghostty has its own release cycle, separate from Ghostty the
application. And it has its own tarballs with only the files and dependencies
libghostty needs, resulting in smaller sizes and simpler licensing
verification and compatibility.
Each release publishes a signed source tarball along with a companion
dependencies tarball containing every Zig package in Zig's own cache
layout, so a distribution can build the library completely offline. The
build installs the shared and static libraries with a proper SONAME,
headers, pkg-config files, and a CMake package config, and it honors
--prefix
,
DESTDIR
, and
lib64
. Debug info is kept by default so
distros can split it out. All of this is documented in
PACKAGING-LIBGHOSTTY.md
,
which ships with the tarball.
Dependencies and Licensing
libghostty-vt
is MIT licensed. At runtime it needs nothing beyond
libc, and it can be built fully freestanding if you don't want that
either.
3
The library compiles in a small number of permissively licensed
dependencies:
simdutf
and
Google Highway
for SIMD, a compact
Unicode table for grapheme data, and
Wuffs
for image decoding in the
Kitty graphics protocol. Both simdutf and Highway are built
without libc++
, so there is no C++
standard library dependency.
There is no copyleft code anywhere in the
dependency tree. Every dependency is listed in a machine-readable
manifest with its version, SPDX license, and hash, specifically so
distros can fill in their bundled-library metadata more easily.
If a distro would rather dynamically link the system simdutf or Highway,
there's a build flag for that.
Portability
libghostty-vt
is highly portable. The table below lists all the platforms
and architectures that we build and test (full unit tests plus running all
examples) in CI:
Platform
Architectures
Linux (glibc, musl)
x86_64
,
aarch64
macOS 13+
x86_64
,
aarch64
iOS 13+
aarch64
FreeBSD
x86_64
,
aarch64
Windows
x86_64
Android
aarch64
,
x86_64
,
arm
WebAssembly
wasm32
(freestanding)
There is a second set of platforms we build in CI but do not run tests for.
These systems all have known users; we just haven't set up the machinery
for automated testing:
Platform
Architectures
Bare metal
riscv32
,
thumb
WebAssembly (WASI)
wasm32
Windows
arm64
illumos
x86_64
32-bit x86
x86
Each of the tested platforms gets the artifacts it expects:
Linux and FreeBSD
get a shared library with a proper SONAME and
versioned symbols, a static library, headers, pkg-config files, and
a CMake package config.
macOS and iOS
get a
dylib
with an
@rpath
install name and
compatibility version, plus an XCFramework covering macOS, iOS, and
the iOS simulator that drops straight into Xcode or Swift Package
Manager.
Windows
gets a DLL with a
.pdb
, an import library, and a static
library. The library is built with the GNU ABI, but MSVC programs
link against it through the import library and CI verifies this.
Android
gets a shared library built against the NDK with 16 KB
page size support, as required by Android 15+.
WebAssembly
ships in two flavors, one optimized for speed and one
for size, and the small one is under a megabyte with every feature
enabled. If you only need a read-only viewer, subsystems like input
encoding, search, selection, and Kitty graphics can be compiled out
with a build flag, which roughly halves the module. Every function
stays exported and simply returns
GHOSTTY_UNSUPPORTED
so your code
doesn't have to change.
4
Portability isn't just about the ability to build and run. It's also
about resource usage and being able to work in a wide variety of
resource environments.
For resource usage, the library creates no threads, allocates only through
an allocator you can customize, and uses minimal compute and memory.
I've run 10,000 active terminals, each with a live shell producing output,
on a Linux server with 4 cores and 8 GB of RAM. In this test, I had to use
dash
because
bash
used far more RAM than
libghostty-vt
and wouldn't fit
into the 8 GB budget.
What's Next
Libghostty 1.0 is a major milestone.
You can now create a terminal in
~1,500 lines of C
that has more features and better performance than just about any terminal
that existed in 2025, and most today in 2026.
5
And thanks to the rich
ecosystem of language bindings, you can do this in every major programming
language. You get this for free. For almost no effort. You can just do it.
libghostty-vt
is a generalized library, so we will focus on stability
while implementing as many terminal protocols as exist
(giving options to enable/disable them, of course) so that embedders
have the luxury of choice.
Every bug any
libghostty-vt
embedder reports makes everyone else in
the ecosystem better. Every feature we ship in
libghostty-vt
becomes
available to everyone quickly and safely. Terminals can move faster with
less fragmentation.
Thank you to everyone who contributed to the library, wrote bindings,
filed bugs, and shipped something on top of it while the API was still
experimental. As with all open source, this was the work of a large
community.
Docs, examples, and downloads are at
lib.ghostty.org
.
Boo. 👻
