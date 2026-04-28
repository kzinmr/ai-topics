---
title: "what is a build system, anyway?"
url: "https://jyn.dev/what-is-a-build-system-anyway/"
fetched_at: 2026-04-28T07:02:50.246009+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# what is a build system, anyway?

Source: https://jyn.dev/what-is-a-build-system-anyway/

Andrew Nesbitt recently wrote a post titled
What is a Package Manager
? This post attempts to do the same for build systems.
big picture
At a high level,
build systems
are tools or libraries that provide a way to
define
and
execute
a series of transformations from
input
data to
output
data that are
memoized
by
caching
them in an
object store
.
Transformations are called
steps
or
rules
and define how to execute a
task
that generates zero or more outputs from zero or more inputs.
A rule is usually the
unit of caching
; i.e. the
cache points
are the outputs of a rule, and
cache invalidations
must happen on the inputs of a rule.
Rules can have
dependencies
on previous outputs, forming a directed graph called a
dependency graph
.
Dependencies that form a cyclic graph are called
circular dependencies
and are usually banned.
Outputs that are only used by other rules, but not “interesting” to the end-user, are called
intermediate outputs
.
A output is
outdated
,
dirty
, or
stale
if one of its dependencies is modified, or,
transitively
, if one of its dependencies is outdated.
Stale outputs invalidate the cache and require the outputs to be
rebuilt
.
An output that is cached and not dirty is
up-to-date
.
Rules are outdated if any of their outputs are outdated.
If a rule has no outputs, it is always outdated.
Each invocation of the build tool is called a
build
.
A
full build
or
clean build
occurs when the cache is empty and all transformations are executed as a
batch job
.
A cache is
full
if all its rules are up-to-date.
An
incremental build
occurs when the cache is partially full but some outputs are outdated and need to be rebuilt.
Deleting the cache is called
cleaning
.
A build is
correct
or
sound
if all possible incremental builds have the same result as a full build.
A build is
minimal
(occasionally
optimal
) if rules are rerun at most once per build, and only run if necessary for soundness (
Build Systems à la Carte
,
Pluto
).
In order for a build to be sound, all possible cache invalidations must be
tracked
as dependencies.
A build system without caching is called a
task runner
or
batch compiler
.
Note that task runners still often support dependencies even if they don't support caching.
Build systems with caching can emulate a task runner by only defining tasks with zero outputs, but they are usually not designed for this use case.
Some examples of build systems:
make
,
docker build
, rustc.
Some examples of task runners:
just
, shell scripts,
gcc
.
specifying dependencies
A build can be either
inter-process
, in which case the task is usually a single
process execution
and its input and output files, or
intra-process
, in which case a task is usually a single function call and its arguments and return values.
In order to track dependencies, either all inputs and outputs must be
declared
in source code ahead of time, or it must be possible to
infer
them from the execution of a task.
Build systems that track changes to a rule definition are called
self-tracking
. Past versions of the rule are called its
history
(
Build Systems à la Carte
).
The act of inferring dependencies from runtime behavior is called
tracing
.
If a traced rule depends on a dependency that hasn’t been built yet, the build system may either error,
suspend
the task and
resume
it later once the dependency is built, or
abort
the task and
restart
it later once the dependency is built (
Build Systems à la Carte
).
Inter-process builds often declare their inputs and outputs, and intra-process builds often infer them, but this is not inherent to the definition.
Some example of intra-process builds include spreadsheets, the
wild
linker, and memoization libraries such as python’s
functools.cache
.
applicative and monadic structure
A build graph is
applicative
if all inputs, outputs, and rules are declared ahead of time.
We say in this case the graph is
statically known
.
Very few build systems are purely applicative, almost all have an escape hatch.
The graph is
monadic
if not all outputs are known ahead of time, or if rules can generate other rules dynamically at runtime. Inputs that aren’t known ahead of time are called
dynamic dependencies
. Dynamic dependencies are weaker than a fully monadic build system, in the sense that they can
express
fewer build graphs.
Build systems that do not require declaring build rules are always monadic.
Some examples of monadic build systems include
Shake
, ninja
dyndeps
, and Cargo build scripts.
Some examples of applicative build systems include
make
(with
recursive make
and
self-rebuilding Makefiles
disallowed), Bazel (excluding native rules), and map/reduce libraries with memoization, such as
this unison program
.
early cutoff
If a dirty rule R has an outdated output, reruns, and creates a new output that matches the old one, the build system has an opportunity to avoid running later rules that depend on R.
Taking advantage of that opportunity is called
early cutoff
.
See
the rustc-dev-guide
for much more information about early cutoff.
rebuild detection
In unsound build systems, it’s possible that the build system does not accurately
detect
that it needs to rebuild.
Such systems sometimes offer a way to
force-rerun
a target: keeping the existing cache, but rerunning a single rule.
For inter-process build systems, this often involves
touch
ing a file to set its modification date to the current time.
the executor
A
build executor
runs tasks and is responsible for
scheduling
tasks in an order that respects all dependencies, often using heuristics such as dependency depth or the time taken by the task on the last run.
They also detect whether rule inputs have been modified, making the rule outdated; this is called
rebuild detection
.
The build executor is responsible for restarting or suspending tasks in build systems that support it.
Executors usually schedule many tasks in parallel, but this is not inherent to the definition.
Executors often provide
progress reporting
, and sometimes allow
querying
the dependency graph.
Occasionally they trace the inputs used by the task to enforce they match the declared dependencies, or to automatically add them to an internal dependency graph.
inter-process builds
In the context of inter-process builds, an
artifact
is an output file generated by a rule.
A
source file
is an input file that is specific to the current
project
(sometimes
repository
or
workspace
) as opposed to a
system dependency
that is reused across multiple projects.
A project is loosely defined but generally refers to the set of all input and output files that the build system knows about, usually contained in a single directory.
Source files can be
generated
, which means they are an output of a previous rule.
Build files
contain rule definitions, including (but not limited to) task definitions, input and output declarations, and metadata such as a human-readable description of the rule.
Inputs are usually split into
explicit inputs
passed to the spawned process,
implicit inputs
that are tracked by the build system but not used in the task definition, and
order-only inputs
that must exist before the rule can execute, but do not invalidate the cache when modified.
Process executions have more inputs than just files, such as the rule itself, environment variables, the current time, the current working directory, and occasionally network services or local daemons .
The set of all inputs that are not source files or command line arguments is called the
environment
.
Processes can be
sandboxed
to prevent them from depending on the network, a daemon, or occasionally system dependencies; this is sometimes called a
sandboxed environment
or
isolated environment
.
System dependencies are more expansive than I think they are often understood to be.
They include compilers, linkers, programming language libraries , and
static and dynamically linked object files
, but also the dynamic loader, language runtime, and various system configuration files.
The subset of these dependencies needed for building a minimal program in a given language, along with various tools for inspecting and modifying the outputs at runtime, are called a
toolchain
.
Toolchains are inherently specific to a given language, but sometimes (e.g. in GCC) a single compiler will support multiple languages as inputs.
A build is
hermetic
(rarely,
self-contained
or
isolated
) if it uses no system dependencies and instead defines all its dependencies in the project (
Bazel
).
Sandboxing and hermeticity are orthogonal axes; neither one implies the other.
For example, docker builds are sandboxed but not hermetic, and nix shells are hermetic but not sandboxed.
Compiler or linkers sometimes have their own
incremental caches
.
Reusing the cache requires you to
trust
the compiler to be sound when incrementally rebuilding.
This is usually implicit, but hermetic or sandboxed builds require an opt-in to reuse the cache.
Bazel calls this kind of reuse a
persistent worker
.
determinism
A build is
deterministic
if it creates the same output every time in some specific environment.
A build is
reproducible
if it is deterministic and also has the same output in
any environment
, as long as the system dependencies remain the same.
remote caching
Caching can be remote or local.
Remote caching
is almost always unsound unless the build is both hermetic and reproducible (i.e. its only environment dependencies are controlled by the build system).
Downloading files from the remote cache is called
materializing
them.
Most build systems with remote caching
defer materialization
as long as possible, since in large build graphs the cache is often too large to fit on disk.
Builds where the cache is never fully materialized are called
shallow builds
(
Build Systems à la Carte
).
Remote caching usually, but not necessarily, uses
content addressed hashing
in a
key-value store
to identify which artifact to download.
Some example build systems that use remote caching: Bazel, Buck2, nix,
docker build
.
interface
Build systems usually have a way to run a subset of the build.
The identifier used to specify which part of the build you want to run is called a
target
.
Targets are usually the filenames of an artifact, but can also be abstract names of one or more rules.
Bazel-descended build systems call these names
labels
.
Make-descended build systems call these
phony targets
.
Some build systems, such as cargo, do not use target identifiers but instead only have subcommands with arguments; the combination of arguments together specifies a set of targets.
Some example targets:
make all
cargo build --test http_integration
buck2 build :main
Inter-process build systems are often divided into a
configuration
step and a
build
step.
A build system that only runs the configuration step, and requires another tool for the build step, is called a
meta-build system
.
Usually this meta-build system
discovers
the rules that need to be executed (often through file globbing or some other programmatic way to describe dependencies), then
serializes
these rules into an
action graph
, which can be stored either in-memory or on-disk. On-disk serialized action graphs are usually themselves build files, in the sense that you can write them by hand but you wouldn't want to.
Configuration steps usually allow the developer to choose a set of
configuration flags
(occasionally,
build flags
) that affect the generated rules.
Some build systems also integrate directly with the
package manager
, but this is uncommon, and usually the build system expects all packages to be pre-downloaded into a known location.
Some examples of meta-build systems are CMake, meson, and autotools.
VFS
Advanced build systems can integrate with a
virtual file system
(VFS) to check-out source control files on-demand, rather than eagerly (
EdenFS
).
A VFS can also persistently store
content hashes
and provide efficient
change detection
for files, avoiding the need for file watching or constant re-hashing.
intra-process builds
The equivalent of system dependencies within a process is
non-local state
, including environment variables, globals, thread-locals, and class member fields (for languages where
this
is passed implicitly).
Especially tricky are function calls that do
inter-process communication
(IPC), which are basically never sound to cache.
Tracing intra-process builds is very very hard since it’s easy to call a function that depends on global state without you knowing.
In this intra-process context, most object stores are
in-memory caches
. A build system that supports saving (
persisting
) the cache to disk is said to have
persistence
. The system for persisting the cache is sometimes called a
database
, even if it is not a general-purpose database in the sense the term is normally used (
Salsa
).
tracing
Tracing intra-process build systems are sometimes called a
query system
.  They work similarly to their inter-process equivalents: the interface looks like normal function calls, and the build system tracks which functions call which other functions, so it knows which to rerun later.
Some examples of tools with tracing intra-process build systems:
salsa
, the
rustc query system
.
FRP
Intra-process build systems that allow you to explicitly declare dependencies usually come from the background of
functional reactive programming
(FRP). FRP is most often used in UI and frontend design, but many of the ideas are the same as the build systems used for compiling programs.
Unlike any of the build systems we've talked about so far, FRP libraries let you look at
past versions
of your outputs, which is sometimes called
remembering
state (
React
). To make this easier to reason about, rules can be written as
event handlers
.
Some examples of libraries with dependency declarations:
React
.
so, what counts as a build system?
A build system is pretty much anything that lets you specify dependencies on a previous artifact 😄 Some more weird examples of build systems:
Github Actions (jobs and workflows)
Static site generators
Docker-compose files
Systemd unit files
Excel
Hopefully this post has given you both a vocabulary to talk about build systems and a context to compare them!
bibliography
Andrew Nesbitt, “What is a Package Manager?”
jyn, “build system tradeoffs”
Jade Lovelace, “The postmodern build system”
Casey Rodarmor, “Just Programmer's Manual”
Fabien Sanglard, “Driving Compilers”
The Rust Project Contributors, “Incremental compilation in detail”
The Rust Project Contributors, “Queries: demand-driven compilation”
“functools — Higher-order functions and operations on callable objects — Python 3.14.2 documentation”
Hillel Wayne, “The Capability-Tractability Tradeoff”
Neil Mitchell, “Shake Build System”
“The Ninja build system”
Peter Miller, “Recursive Make Considered Harmful”
Rebecca Mark and Paul Chiusano,  “Incremental evaluation via memoization · Unison programming language”
“Hermeticity  |  Bazel”
“Persistent Workers  |  Bazel”
“Labels  |  Bazel”
“Commandments of reproducible builds”
Mokhov et. al., Build Systems à la Carte
“Phony Targets (GNU make)”
Facebook, “Sapling: A Scalable, User-Friendly Source Control System.”
Erdweg et. al., "A Sound and Optimal Incremental Build System with Dynamic Dependencies"
David Lattimore, “Designing Wild's incremental linking”
Bo Lord, “How to Recalculate a Spreadsheet”
“ninja—
depfile_parser
”
“salsa - A generic framework for on-demand, incrementalized computation”
“Defining the database struct - Salsa”
Felix Klock and Mark Rousskov on behalf of the Rust compiler team, “Announcing Rust 1.52.1”
Yaron Minsky, “Jane Street Blog - Breaking down FRP ”
“Adding Interactivity – React”
“State: A Component's Memory – React”
