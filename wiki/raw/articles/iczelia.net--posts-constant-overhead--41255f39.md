---
title: "Measuring Constant Overhead"
url: "https://iczelia.net/posts/constant-overhead/"
fetched_at: 2026-05-05T07:01:19.397349+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Measuring Constant Overhead

Source: https://iczelia.net/posts/constant-overhead/

Do we have a problem?
⌗
It makes sense to think that a particular language runtime is fast or slow. There have been various attempts at quantifying what
fast
or
slow
means. Such attempts include for example
this
or
this
. However,
voices of skepticism
have been raised against the validity and representativeness of such comparisons. My personal pet peeves include:
Task implementations varying wildly wildly from language to language because programmers of lower level languages find hacks to make their code faster.
Tasks necessitate the use of data structures and their implementations that vary from platform to platform (e.g. Java’s
HashMap
, C++’s
unordered_map
and Rust’s
HashMap
have diverging design goals in a couple of places). Non-trivial dependencies on standard libraries and external packages, in my opinion, invalidate the comparison.
They compare languages and not particular implementations.
We don’t know much about their testing rig. Compiler/interpreter versions, hardware (CPU, RAM, system load, etc.)
All the ‘X beating C’ proofs are egregious.
…
Is there a solution?
⌗
Not a useful one, no, I reckon. But chances are that you are looking for something as specific as I do, so hang on.
There is a fundamental reason for why you’d want to compare runtimes and let this influence your language choice: boxing is not free, many runtimes can’t reliably elide it; some runtimes, particularly for dynamic languages, can not perform type inference well enough to lower FP operations to integer operations. These issues are practical and serious for computation-heavy code.
I am interested in measuring the
constant overhead
of a programming language runtime. The core idea is rather simple: the time taken by some algorithm generally grows proportionally to the input size, but from a programming standpoint, solutions that have too high constant factor (e.g. compare a program that takes
20
n
20n
20
n
steps vs a program that takes
2
n
2n
2
n
steps for an input of size
n
n
n
) are sometimes not feasible. The methodology is rather simple: take an uncomplicated algorithm which can not be improved too much using standard tricks (autovectorisation, loop unrolling) and translate it to each of the languages, applying performance tweaks (like defining types, turning off the GC, localising data) if they are feasible.
What we want to get out of this is to single out runtimes that:
Behave badly in tight (yet very uncomplicated) loops
. Because (for example) they use an inefficient interpreter loop or don’t compile to native code during execution.
Can’t use the typing information well or infer it in the runtime
. It is crucial for the performance of any (crafted or real-world) application that the typing information is used or inferred correctly. This saves type checks, lets runtimes elide bounds checks, eliminates the need for boxing and thus leads to more efficient code generation.
Don’t offer rudimentary performance improvement techniques
. For example, making it impossible to issue the
idiv
instruction for integer division, forcing the programmer to perform a floating point operation and then cast the result to an integer. Another example is the lack of bitwise operations, which are crucial for many algorithms (e.g., Myers’ edit distance algorithm).
Can’t inline code efficiently
. This benchmark in particular tests extremely basic functions - called only once, a few lines long. If the runtime can’t inline them, it will incur a penalty in function call overhead and render the runtime incapable of performing inter-procedural optimisations that result from inlining.
Don’t optimise arithmetic or use an inefficient numerical tower
. Notoriously, some runtimes may not offer fixed width integer types or may unnecessarily promote integers to floating point numbers when performing arithmetic operations.
Incur unavoidable penalties in array accesses
. Largely self-explanatory.
Some of the things that we don’t want to test for:
GC
- we are not interested in the GC performance, hence our application will not allocate much. Testing GC and allocation performance is very difficult, allocator-dependent (e.g. glibc
malloc
is generally slower than
jemalloc
) and ignores the fact that more sophisticared runtimes like the Java HotSpot VM can perform escape analysis or stack allocation to avoid heap allocation. Further, the use of a bump allocator and a copying collector for the young generation drastically improves allocation and deallocation performance, especially for workloads that produce a lot of short-lived objects (as the computational complexity of a copying collector is dominated by the number of live objects, not the total number of objects). Such comparisons are difficult and generally not very fruitful.
Standard library performance
- while crucial for real-world applications, we concern outself only with the capabilities of the interpreter/compiler itself. Many facts about the performance of standard library containers and algorithms are well-known and documented (especially pertaining computational complexities), making it unnecessary/overly ambitious to test them.
Concurrency
.
I/O
- we are not interested in the performance of I/O operations. Hence the programs will be locked to buffered, byte-wise I/O.
Memory usage
- it is difficult and unfruitful to measure. Often also unrepresentative.
Startup time
- to make the comparison fair, we will perform both small and large scale comparisons.
The benchmark.
⌗
FPAQ0 - the test program - is a very simple order-0 statistical model coupled together with a bitwise arithmetic coder due to Matt Mahoney. We slightly simplify it and use it as a benchmark. Among data compression experts, FPAQ0 and variants are used for benchmarking particular bitwise arithmetic coding strategies. The code is rather simple and we will recall it. First, we define the predictor:
This function is called for each bit in the input file. It performs some arithmetic, notably an integer division and multiplication. It also extensively uses array loads/stores.
The arithmetic coder will maintain a few bits of state and read/write data from/to buffered I/O streams bytewise. The
ac_flush
and
ac_rescale
functions are prime candidates for inlining. Outside of that, we perform bit operations, shifts and multiplications.
The results
⌗
First, some notes:
PUC-RIO Lua/CPython were not tested, because they are not worth testing.
LuaJIT lacks a way to issue
idiv
and likely pays for it, but according to
luajit -lp
most of the time is spent in the arithmetic coder anyway.
WASI-SDK clang’s standard library might use (too) small I/O buffers, worsening its performance.
In line with the C implementation, try to not use object-oriented programming: in metatable/prototype-oriented languages, looking up a method in an object is somewhat costly. The code does, however, use any feature of the language feasible to represent the arithmetic encoder state structure that can be passed around. This often amounts to having a class with just a constructor and a few public fields.
Numba: Seems to be missing a lot of opcode implementations, dunno how to make it work. Cython also does not seem to help much.
Temurin JDK was not tested as it does not significantly affect the performance.
Interesting findings:
Turn-the-GC-off snake oil doesn’t work (e.g. through enabling EpsilonGC for Java). For major runtimes this makes no difference because the program does not allocate enough to warrant a GC cycle. This is at least a bit surprising, because in programmer folklore, GC is always responsible for all the plagues of the world.
The test machine is Notebook 20Y7003XPB (LENOVO_MT_20Y7_BU_Think_FM_ThinkPad E14 Gen 3). Specifications:
Memory: 40GB.
Bank 0: SODIMM DDR4 Synchronous Unbuffered (Unregistered). Product CT32G4SFD832A.16FB2. Slot DIMM 0. Size: 32GiB. Width: 64 bits. Clock: 3200MHz (0.3ns).
Bank 1: SODIMM DDR4 Synchronous Unbuffered (Unregistered). Product 4ATF1G64HZ-3G2E1. Slot DIMM 0. Size: 8GiB. Width: 64 bits. Clock: 3200MHz (0.3ns).
Cache:
L1: 512KiB. Clock: 1GHz (1.0ns). Capabilities: pipeline-burst internal write-back unified.
L2: 4MiB. Clock: 1GHz (1.0ns). Capabilities: pipeline-burst internal write-back unified.
L3: 8MiB. Clock: 1GHz (1.0ns). Capabilities: pipeline-burst internal write-back unified.
CPU: AMD Ryzen 7 5700U with Radeon Graphics. Use Google to find the specification.
OS: Linux laplace 6.8.12-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.8.12-1 (2024-05-31) x86_64 GNU/Linux
We denote
[U: x ms, S: y ms]
as the user and system time, respectively.
Results (
book1
):
Benchmark
Time
Debian clang version 16.0.6 (27)
-O2
35.1 ms ± 0.7 ms [U: 33.2 ms, S: 1.5 ms]
gcc version 13.2.0 (Debian 13.2.0-25)
-O3 -march=native -mtune=native
35.6 ms ± 0.7 ms [U: 33.7 ms, S: 1.6 ms]
gcc version 13.2.0 (Debian 13.2.0-25)
-O2
35.7 ms ± 1.3 ms [U: 33.1 ms, S: 2.2 ms]
Debian clang version 16.0.6 (27)
-O3 -march=native -mtune=native
35.7 ms ± 1.6 ms [U: 33.7 ms, S: 1.8 ms]
wasmtime-cli 21.0.1 (cedf9aa0f 2024-05-22), wasi-sdk clang version 18.1.2
49.4 ms ± 1.3 ms [U: 38.1 ms, S: 12.3 ms]
native-image
OpenJDK 64-Bit Server VM GraalVM CE 22.2.0 (build 17.0.4+8-jvmci-22.2-b06, mixed mode, sharing)
87.6 ms ± 2.7 ms [U: 82.8 ms, S: 4.5 ms]
OpenJDK 64-Bit Server VM (build 17.0.11+9-Debian-1, mixed mode, sharing)
97.5 ms ± 3.3 ms [U: 98.2 ms, S: 31.7 ms]
OpenJDK 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)
107.3 ms ± 2.3 ms [U: 140.0 ms, S: 36.6 ms]
OpenJDK 64-Bit Server VM GraalVM CE 22.2.0 (build 17.0.4+8-jvmci-22.2-b06, mixed mode, sharing)
123.8 ms ± 2.0 ms [U: 151.4 ms, S: 55.9 ms]
OpenJDK 64-Bit Server VM Corretto-8.412.08.1
128.7 ms ± 3.6 ms [U: 148.0 ms, S: 45.0 ms]
luajit/unstable,now 2.1.0+openresty20240314-1
-O3
150.7 ms ± 4.4 ms [U: 148.0 ms, S: 2.5 ms]
Node.js v20.14.0
177.5 ms ± 2.3 ms [U: 172.4 ms, S: 32.7 ms]
PyPy 7.3.16 with GCC 13.2.0
251.2 ms ± 6.7 ms [U: 222.7 ms, S: 28.3 ms]
Results (
enwik8
):
Benchmark
Time
Debian clang version 16.0.6 (27)
-O2
4.468 s ± 0.014 s [U: 4.343 s, S: 0.124 s]
Debian clang version 16.0.6 (27)
-O3 -march=native -mtune=native
4.516 s ± 0.012 s [U: 4.386 s, S: 0.130 s]
gcc version 13.2.0 (Debian 13.2.0-25)
-O2
4.605 s ± 0.017 s [U: 4.479 s, S: 0.125 s]
gcc version 13.2.0 (Debian 13.2.0-25)
-O3 -march=native -mtune=native
4.621 s ± 0.010 s [U: 4.488 s, S: 0.132 s]
wasmtime-cli 21.0.1 (cedf9aa0f 2024-05-22), wasi-sdk clang version 18.1.2
5.333 s ± 0.058 s [U: 4.732 s, S: 0.601 s]
OpenJDK 64-Bit Server VM GraalVM CE 22.2.0 (build 17.0.4+8-jvmci-22.2-b06, mixed mode, sharing)
5.608 s ± 0.046 s [U: 5.550 s, S: 0.176 s]
OpenJDK 64-Bit Server VM (build 17.0.11+9-Debian-1, mixed mode, sharing)
5.996 s ± 0.085 s [U: 5.889 s, S: 0.150 s]
OpenJDK 64-Bit Server VM Corretto-8.412.08.1
6.122 s ± 0.086 s [U: 6.030 s, S: 0.167 s]
OpenJDK 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)
7.091 s ± 0.149 s [U: 7.000 s, S: 0.176 s]
Node.js v20.14.0
9.412 s ± 0.096 s [U: 9.312 s, S: 0.128 s]
native-image
OpenJDK 64-Bit Server VM GraalVM CE 22.2.0 (build 17.0.4+8-jvmci-22.2-b06, mixed mode, sharing)
11.254 s ± 0.114 s [U: 11.146 s, S: 0.108 s]
luajit/unstable,now 2.1.0+openresty20240314-1
-O3
19.610 s ± 0.152 s [U: 19.437 s, S: 0.170 s]
PyPy 7.3.16 with GCC 13.2.0
24.717 s ± 0.504 s [U: 24.101 s, S: 0.613 s]
Wrapping up
⌗
An overview of the results, source code and test files can be
viewed at GitHub
.
