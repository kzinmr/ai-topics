---
title: "Linear Time Liveness Analysis"
url: "https://databasearchitects.blogspot.com/2020/04/linear-time-liveness-analysis.html"
fetched_at: 2026-05-05T07:01:29.460085+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Linear Time Liveness Analysis

Source: https://databasearchitects.blogspot.com/2020/04/linear-time-liveness-analysis.html

Standard compiler are usually used with hand-written programs. These programs tend to have reasonably small functions, and can be processed in (nearly) linear time. Generated programs however can be quite large, and compilers sometimes struggle to compile them at all. This can be seen with the following (silly) demonstration script:
import subprocess  
 from timeit import default_timer as timer  
 def doTest(size):  
   with open("foo.cpp", "w") as out:  
     print("int foo(int x) {", file=out)  
     for s in range(size):  
       p="x" if s==0 else f'l{s-1}'  
       print (f'int l{s}; if (__builtin_sadd_overflow({p},1,&l{s})) goto error;', file=out)  
     print(f'return l{size-1};error: throw;}}', file=out);  
   start = timer()  
   subprocess.run(["gcc", "-c", "foo.cpp"])   
   stop = timer()  
   print(size, ": ", (stop-start))  
 for size in [10,100,1000,10000,100000]:  
   doTest(size)
It generates one function with n statements of the form "
int lX; if (__builtin_sadd_overflow(lY,1,&lX)) goto error;
" which are basically just n additions with overflow checks, and then measures the compile time. The generated code is conceptually a very simple, but it contains a lot of basic blocks due to the large number of ifs. When compiling with gcc we get the following compile times:
n
10
100
1,000
10,000
100,000
compilation [s]
0.02
0.04
0.19
34.99
> 1h
The compile time is dramatically super linear, gcc is basically unable to compile the function if it contains 10,000 ifs or more. In this simple example clang fares better when using -O0, but with -O1 it shows super-linear compile times, too. This is disastrous when processing generated code, where we cannot easily limit the size of individual functions. In
our own system
we use neither gcc nor clang for query compilation, but we have same problem, namely compiling large generated code. And super-linear runtime quickly becomes an issue when the input is large.
One particular important problem in this context is
liveness analysis
, i.e, figuring out which value is alive at which part of the program. The
textbook solution
for that problem involves propagating liveness information for each variable across the blocks, but that is clearly super linear and does not scale to large program sizes. We therefore developed
a different approach
that we recently refined even more and the I want to present here:
Instead of propagating liveness sets or bitmasks, we study the control flow graph of the program. For a simple queries with a for loop and an if within the loop it might look like this:
Now if we define a variable x in block 0, and use it in block 2, the variable has to be alive on every path between definition and usage. Obviously that includes the blocks 0-2, but that is not enough. We see that there is a loop involving all loops between 1 and 4, and we can take that before coming to 2. Thus, the lifetime has to be extended to include the full loop, and is there range 0-4. If, however, we define a variable in 1 and use it in 2, the range is indeed 1-2, as we do not have to wrap around.
Algorithmically, we identify all loops in the program, which we can do in
almost linear time
, and remember how the loops are nested within each other. Then, we examine each occurrence of a variable (in SSA form). In principle the lifetime is the span from the first to the last occurrences. If, however, two occurrences are in different loops, we walk "up" from the lower loop level until we occur in the same loop (or top level), extending the lifetime to cover the full loop while doing so. In this example x in block 0 is top level, while x in block 2 is in loop level 1. Thus, we leave the loop, expand 2 into 1-4, and find the lifetime to be 0-4.
This assumes, of course, that the block numbers are meaningful. We can guarantee that by first labeling all blocks in
reverse postorder
. This guarantees that all dominating blocks will have a lower number than their successors. We can further improve the labeling by re-arranging the blocks such that all blocks within a certain loop are next to each other, keeping the original reverse post order within the loop. This leads to nice, tight liveness intervals. Using just an interval instead of a bitmap is of course less precise, but the block reordering makes sure that the intervals primarily contain the blocks that are indeed involved in the execution.
Asymptotically such an interval based approach is far superior to a classical liveness propagation. All algorithms involved are linear or almost linear, and we only to have to store two numbers per variable. When handling large, generated code such an approach is mandatory. And even for classical, smaller programs it is quite attractive. I looked around a bit at lectures about compiler construction, and I am somewhat surprised that nobody seems to teach similar techniques to handle large programs. When you cannot control the input size, super linear runtime is not an option.
