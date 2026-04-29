---
title: "I want a better build executor"
url: "https://jyn.dev/i-want-a-better-build-executor/"
fetched_at: 2026-04-29T07:02:11.399230+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# I want a better build executor

Source: https://jyn.dev/i-want-a-better-build-executor/

This post is part 4/4 of
a series about build systems
.
The market fit is interesting. Git has clearly won, it has all of the mindshare, but since you can use jj to work on Git repositories, it can be adopted incrementally. This is, in my opinion, the only viable way to introduce a new VCS: it has to be able to be partially adopted.
Steve Klabnik
If you've worked with other determinism-based systems, one thing they have in common is they feel really fragile, and you have to be careful that you don't do something that breaks the determinism. But in our case, since we've created every level of the stack to support this, we can offload the determinism to the development environment and you can basically write whatever code you want without having to worry about whether it's going to break something.
Allan Blomquist
In
my last post
, I describe an improved build graph serialization. In this post, I describe the build executor that reads those files.
what is a build executor?
Generally, there are three stages to a build:
Resolving and downloading dependencies. The tool that does this is called a
package manager
. Common examples are
npm
,
pip
,
Conan
, and the
cargo
resolver
.
Configuring the build based on the host environment and build targets. I am not aware of any common name for this, other than maybe
configure script
(but there exist many tools for this that are not just shell scripts). Common examples are CMake, Meson, autotools, and the Cargo CLI interface (e.g.
--feature
and
--target
).
Executing a bunch of processes and reporting on their progress. The tool that does this is called a
build executor
. Common examples are
make
,
ninja
,
docker build
, and the
Compiling
phase of
cargo build
.
There are a lot more things an executor can do than just spawning processes and showing a progress report!
This post explores what those are and sketches a design for a tool that could improve on current executors.
change detection
Ninja depends on
mtimes, which have many issues
. Ideally, it would take notes from
redo
and look at file attributes, not just the mtime, which eliminates many more false positives.
querying
I wrote earlier about
querying the build graph
.
There are two kinds of things you can query: The configuration graph (what bazel calls the
target graph
), which shows dependencies between "human meaningful" packages; and the
action graph
, which shows dependencies between files.
Queries on the action graph live in the executor; queries on the configuration graph live in the configure script. For example,
cargo metadata
/
cargo tree
,
bazel query
, and
cmake --graphiz
query the configuration graph;
ninja -t inputs
and
bazel aquery
query the action graph. Cargo has no stable way to query the action graph.
Note that “querying the graph” is not a binary yes/no. Ninja's query language is much more restricted than Bazel's. Compare Ninja's syntax for querying “the command line for all C++ files used to build the target
//:hello_world
” :
$
ninja
-
t
inputs hello_world
|
grep
'
\.c++$
'
|
xargs
ninja
-
t
targets
|
cut
-
d
:
-
f
1
|
xargs
ninja
-
t
commands
g++ -c -o my_lib.o my_lib.cpp
g++ -o hello_world hello_world.cpp my_lib.o
to Bazel's:
$
bazel
aquery
'
inputs(".*cpp", deps(//:hello_world))
'
action 'Compiling hello_world.cpp'
Mnemonic: CppCompile
Target: //:hello_world
Configuration: k8-fastbuild
Execution platform: @@platforms//host:host
ActionKey: 155b2cdb875736efc8d218ea790d2ef9ce698f0b1b1700d58de3c135145b1d12
Inputs: [external/rules_cc++cc_configure_extension+local_config_cc/builtin_include_directory_paths, external/rules_cc++cc_configure_extension+local_config_cc/cc_wrapper.sh, external/rules_cc++cc_configure_extension+local_config_cc/deps_scanner_wrapper.sh, external/rules_cc++cc_configure_extension+local_config_cc/validate_static_library.sh, hello_world.cpp, my_lib.h]
Outputs: [bazel-out/k8-fastbuild/bin/_objs/hello_world/hello_world.pic.d, bazel-out/k8-fastbuild/bin/_objs/hello_world/hello_world.pic.o]
Command Line: (exec /nix/store/vr15iyyykg9zai6fpgvhcgyw7gckl78w-gcc-wrapper-14.3.0/bin/gcc \
full command line
-U_FORTIFY_SOURCE \
-fstack-protector \
-Wall \
-Wunused-but-set-parameter \
-Wno-free-nonheap-object \
-fno-omit-frame-pointer \
'-std=c++17' \
-MD \
-MF \
bazel-out/k8-fastbuild/bin/_objs/hello_world/hello_world.pic.d \
'-frandom-seed=bazel-out/k8-fastbuild/bin/_objs/hello_world/hello_world.pic.o' \
-fPIC \
-iquote \
. \
-iquote \
bazel-out/k8-fastbuild/bin \
-iquote \
external/rules_cc+ \
-iquote \
bazel-out/k8-fastbuild/bin/external/rules_cc+ \
-iquote \
external/bazel_tools \
-iquote \
bazel-out/k8-fastbuild/bin/external/bazel_tools \
-c \
hello_world.cpp \
-o \
bazel-out/k8-fastbuild/bin/_objs/hello_world/hello_world.pic.o \
-fno-canonical-system-headers \
-Wno-builtin-macro-redefined \
'-D__DATE__="redacted"' \
'-D__TIMESTAMP__="redacted"' \
'-D__TIME__="redacted"')
Bazel’s language has graph operators, such as union, intersection, and filtering, that let you build up quite complex predicates. Ninja can only express one predicate at a time, with much more limited filtering—but unlike Bazel, allows you to filter to individual parts of the action, like the command line invocation, without needing a full protobuf parser or trying to do text post-processing.
I would like to see a query language that combines both these strengths: the same nested predicate structure of Bazel queries, but add a new
emit()
predicate that takes another predicate as an argument for complex output filtering:
emit(commands, inputs(".*cpp", deps(./src/hello_world)))
We could even go so far as to give this a jq-like syntax:
./src/hello_world | deps | inputs "*.c++" | emit commands
For more complex predicates that have multiple sets as inputs, such as set union and intersection, we could introduce a
subquery
operator:
glob "src/**" | except subquery(glob("src/package/**") | executable)
tracing
In
my previous post
, I talked about two main uses for a tracing build system: first, to automatically add dependency edges for you; and second, to verify at runtime that no dependency edges are missing. This especially shines when the action graph has a way to express negative dependencies, because the tracing system
sees
every attempted file access and can add them to the graph automatically.
For prior art, see the
Shake build system
. Shake is higher-level than an executor and doesn't work on an action graph, but it has
built-in support for file tracing
in all three of these modes: warning about incorrect edges; adding new edges to the graph when they're detected at runtime; and finally,
fully inferring all edges from the nodes alone
.
I would want my executor to only support linting and hard errors for missing edges. Inferring a full action graph is scary and IMO belongs in a higher-level tool, and adding dependency edges automatically can be done by a tool that wraps the executor and parses the lints.
What's really cool about this linting system is that it allows you to gradually transition to a hermetic build over time, without frontloading all the work to when you switch to the tool.
The main downside of tracing is that it's highly non-portable, and in particular is very limited on macOS.
One possible alternative I've thought of is to do a buck2-style unsandboxed hermetic builds, where you copy exactly the specified inputs into a tempdir and run the build from the tempdir. If that fails, rerun the build from the main source directory. This can't tell
which
dependency edges are missing, but it can tell you
a
dependency is missing without fully failing the build.
The downside to
that
is it assumes command spawning is a pure function, which of course it's not; anything that talks to a socket is trouble because it might be stateful.
environment variables
Tracing environment variable access is … hard. Traditionally access goes through the libc
getenv
function, but it’s also possible to take an
envp
in a main function, in which case accesses are just memory reads. That means we need to trace memory reads somehow.
On x86 machines, there’s something called
PIN
that can do this directly in the CPU without needing compile time instrumentation. On ARM there’s
SPE
, which is how
perf mem
works, but I’m not sure whether it can be configured to track 100% of memory accesses. I need to do more research here.
On Linux, this is all abstracted by
perf_event_open
. I’m not sure if there’s equivalent wrappers on Windows and macOS.
There’s also
DynamicRIO
, which supports a bunch of platforms, but I believe it works in a similar way to QEMU, by interposing itself between the program and the CPU, which comes with a bunch of overhead. That could work as an opt-in.
One last way to do this is with a
SIGSEGV signal handler
, but that requires that environment variables are in their own page of memory and therefore a linker script. This doesn’t work for environment variables specifically, because they
aren’t linker symbols in the normal sense, they get injected by the C runtime
. In general, injecting linker scripts means we’re modifying the binaries being run and might cause unexpected build or runtime failures.
ronin
: a ninja successor
Here I describe more concretely the tool I want to build, which I’ve named
ronin
. It would read the
constrained clojure action graph serialization format
(Magma) that I describe in the previous post; perhaps with a way to automatically convert Ninja files to Magma.
interface
Like
Ekam
, Ronin would have a
--watch
continuous rebuild mode (but unlike Bazel and Buck2, no background server). Like Shake, It would have runtime tracing, with all of
--tracing=never|warn|error
options, to allow gradually transitioning to a hermetic build. And it would have bazel-like querying for the action graph, both through CLI arguments with an jq syntax and through a programmatic API.
Finally, it would have pluggable backends for file watching, tracing, stat-ing, progress reporting, and checksums, so that it can take advantage of systems that have more features while still being reasonably fast on systems that don’t. For example, on Windows stats are slow, so it would cache stat info; but on Linux stats are fast so it would just directly make a syscall.
architecture
Like Ninja, Ronin would keep a command log with a history of past versions of the action graph. It would reuse the
bipartite graph structure
, with one half being files and the other being commands. It would parse depfiles and dyndeps files just after they’re built, while the cache is still hot.
Like
n2
, ronin would use a single-pass approach to support early cutoff. It would hash an "input manifest" to decide whether to rebuild. Unlike
n2
, it would store a mapping from that hash back to the original manifest so you can query why a rebuild happened.
Tracing would be built on top of a FUSE file system that tracked file access.
Unlike other build systems I know, state (such as manifest hashes, content hashes, and removed outputs) would be stored in an SQLite database, not in flat files.
did you just reinvent buck2?
Kinda. Ronin takes a lot of ideas from buck2. It differs in two major ways:
It does not expect to be a top-level build system. It is perfectly happy to read (and encourages) generated files from a higher level configure tool. This allows systems like CMake and Meson to mechanically translate Ninja files into this new format, so builds for existing projects can get nice things.
It allows you to gradually transition from non-hermetic to hermetic builds, without forcing you to fix all your rules at once, and with tracing to help you find where you need to make your fixes. Buck2 doesn’t support tracing at all. It technically supports non-hermetic builds, but you don't get many benefits compared to using a different build system, and it's still high cost to switch build systems .
The main advantage of Ronin is that it can slot in underneath existing build systems people are already using—CMake and Meson—without needing changes to your build files at all.
summary
In this post I describe what a build executor does, some features I would like to see from an executor (with a special focus on tracing), and a design for a new executor called
ronin
that allows existing projects generating ninja files to gradually transition to hermetic builds over time, without a “flag day” that requires rewriting the whole build system.
I don’t know yet if I will actually build this tool, that seems like a lot of work  😄 but it’s something I would like to exist in the world.
