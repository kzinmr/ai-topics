---
title: "The LLVM Project Blog"
url: "https://blog.llvm.org/2015/05/openmp-support_22.html"
fetched_at: 2026-05-05T07:01:40.568481+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project Blog

Source: https://blog.llvm.org/2015/05/openmp-support_22.html

OpenMP support in Clang compiler is completed! Every pragma and clause from
3.1 version of the standard
is supported in full, including combined directives (like ‘#pragma omp parallel for’ and ‘#pragma omp parallel sections’).  In addition
, some elements of OpenMP 4.0 are supported as well. This includes “almost complete” support for ‘#pragma omp simd” and full support for ‘#pragma omp atomic’  (combined pragmas and a couple of clauses are still missing).
OpenMP enables Clang users to harness full power of modern multi-core processors with vector units. Pragmas from OpenMP 3.1 provide an industry standard way to employ task parallelism, while ‘#pragma omp simd’ is a simple yet flexible way to enable data parallelism (aka vectorization).
Clang implementation of OpenMP standard relies on LLVM OpenMP runtime library, available at
http://openmp.llvm.org/
. This runtime supports ARM® architecture processors, PowerPC™ processors, 32 and 64 bit X86 processors and provides ABI compatibility with GCC and Intel's existing OpenMP compilers.
To enable OpenMP, just add ‘
-fopenmp
’ to the command line and provide paths to OpenMP headers and library with ‘
-I <
path to omp.h
> -L <
LLVM OpenMP library path
>
’.
To run a compiled program you may need to provide a path to shared OpenMP library as well:
$ export LD_LIBRARY_PATH=<OpenMP library path>:$LD_LIBRARY_PATH
or:
$ export DYLD_LIBRARY_PATH=<OpenMP library path>:$DYLD_LIBRARY_PATH
on Mac OS X.
You can confirm that the compiler works correctly by trying this simple parallel C program:
#include <omp.h>
#include <stdio.h>
int main() {
#pragma omp parallel
printf("Hello from thread %d, nthreads %d\n", omp_get_thread_num(), omp_get_num_threads());
}
Compile it (you should see no errors or warnings):
$ clang -fopenmp -I <path to omp.h> -L <LLVM OpenMP library path> hello_openmp.c -o hello_openmp
and execute:
$
export [DY]LD_LIBRARY_PATH=<OpenMP library path>:$[DY]LD_LIBRARY_PATH
$ ./hello_openmp
You will see more than one “Hello” line with different thread numbers (note that the lines may be mixed together). If you see only one line, try setting the environment variable OMP_NUM_THREADS to some number (say 4) and try again.
Hopefully, you will enjoy using OpenMP and witness dramatic boosts of your applications’ performance!
