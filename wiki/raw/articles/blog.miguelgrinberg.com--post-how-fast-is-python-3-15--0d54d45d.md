---
title: "How fast is Python 3.15?"
url: "https://blog.miguelgrinberg.com/post/how-fast-is-python-3-15"
fetched_at: 2026-10-06T10:01:35.412161+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# How fast is Python 3.15?

Source: https://blog.miguelgrinberg.com/post/how-fast-is-python-3-15

It's October once again, and that means it is time to take the new release of Python for a spin (technically, it is the 3.15.0rc3 release that I'm using, the official 3.15 release is still a few days out). As I did with my
Python 3.14 performance
article of a year ago, today I'm sharing a new run of my informal Python benchmark, comparing Python 3.15 against previous interpreters all the way back to 3.10.
If you are not interested in the charts and the tables and just want to read my analysis, feel free to jump to the
conclusions
section at the end.
The benchmark
I just called my benchmark "informal". What does that mean?
Getting an objective and universal measure of the performance of a programming language is impossible. All you can do is write some programs and run them to get a measure of their performance. Other programs may show similar performance characteristics or they may not, there is really no way to know. My intention with this benchmark is just to get a feel for the performance changes across versions of Python, but I want to make it clear that I'm not trying to obtain a comprehensive performance profile of the Python interpreter.
For my benchmark I will be running two programs called
fibo.py
and
bubble.py
, which
you can inspect
if you like. These are the same programs I used in past editions of this benchmark. The first calculates numbers from the
Fibonacci sequence
, and the second sorts numbers using the
bubble sort
algorithm.
I've chosen these two programs as representative of two classes of algorithms. The Fibonacci calculation is done using
recursion
, which I have found to be somewhat inefficient in Python interpreters. On the other side, the bubble sort only uses for-loops, without any recursion. There are other types of programs that my benchmark does not attempt to cover. In particular, note that I'm not including
I/O bound
code in this benchmark.
Because some of the performance improvements in recent Python versions revolve around multi-threading, I also created a multi-threaded variation for each program, so in total I have four different tests.
The testing matrix
The complete testing matrix is actually fairly complex, because I have to run the four program variations under all the Python versions, plus the JIT and free-threading alternatives for those that have them. I like to run the tests under PyPy as well, because this interpreter has shown impressive performance in past runs of this benchmark. And to place Python performance within the wider ecosystem, I've also ported the two programs to JavaScript (Node.js) and Rust.
Here is the full test matrix that I've worked with:
2 test scripts
fibo.py
: calculates Fibonacci numbers, with recursion
bubble.py
: sorts a list of randomly generated numbers, without recursion
2 threading modes
Single-threaded
4 parallel threads
6 Python versions, plus recent versions of PyPy, Node.js and Rust:
3 Python interpreters
Standard
Just-In-Time (JIT): only for CPython 3.13+
Free-threading (FT): only for CPython 3.13+
Readers of my previous benchmarks may recall that I had an additional dimension in my matrix for Linux vs. macOS. Given that there were no significant differences between them in the two previous runs of the benchmark, I've decided to drop the macOS tests this time around, so all tests were executed on my Linux laptop, which has an Intel Core i5 CPU and runs Gentoo Linux.
The method I'm using to measure the performance of each participant in this benchmark is to run the test program three times and take the average duration of the three. In the tables of results that I share below I also show the speed difference versus the 3.15 version, and when it makes sense also the speed difference versus the previous version of a given interpreter. For speed comparisons I'm using a simple ratio, where 1x means same speed, 0.5x means half speed (or that it took twice the time to run), 2x means twice as fast (or that it ran in half the time if you prefer), etc. Hopefully this makes sense.
Test 1: fibo.py, single-threaded
Let's get started. The first test calculates the first 40 Fibonacci numbers.
fibo(40) - 1 thread
Time (secs)
vs. 3.15
vs. previous
3.10
15.9442
0.44x
3.11
9.4058
0.74x
1.70x
3.12
8.8545
0.78x
1.06x
3.13
8.8174
0.79x
1.00x
3.14
7.1659
0.97x
1.23x
3.15
6.9361
1.03x
pypy3.12
1.2517
5.54x
node-26.3
1.3899
4.99x
rust-1.97
0.0898
77.24x
Below you can see the above speeds in chart form:
From these results we can infer that for this test Python 3.15 is just a tiny bit faster than 3.14, probably not enough to matter. As I have also observed in previous years, the performance of PyPy 3.12 is out of this world, clocking in at 5.5x the speed of 3.15, and even getting a small lead over Node.js. As for Rust there are no surprises, but it is always good to know where the limits are!
Comparing each Python release against the previous one shows an interesting detail. The only two releases that made significant performance improvements over their predecessors are Python 3.11 and 3.14. You can see this clearly in the chart, when there is a larger drop in the height of a bar compared to the previous one. The other releases either maintained the same speed or made small improvements, so overall there's always been progress.
In the next set of results you can see the progress of the JIT and free-threading (FT) releases of Python on the same test. Keep in mind that these alternative versions of the Python interpreter were first introduced in 3.13, so the range of versions to evaluate is much smaller.
fibo(40) - 1 thread
Time (secs)
vs. 3.15
vs. previous
3.13 JIT
8.8339
3.14 JIT
7.1587
1.23x
3.15 JIT
5.7625
1.20x
1.24x
3.13 FT
12.0368
3.14 FT
7.1185
1.69x
3.15 FT
7.0298
0.99x
1.01x
Below is a chart with these results:
Really the most interesting thing from this is that the JIT in the 3.15 interpreter was faster than the standard interpreter of the same test, which was not the case in previous years. And a 1.20x speed increase is not negligible, this is very exciting to see!
On the free-threading front there isn't really a lot to expect because this test is single-threaded. But we can say that the performance of the free-threading interpreter is about the same as the 3.14 one.
Test 2: bubble.py, single-threaded
Let's look at the second test now. Here are the table and the chart for the single-threaded bubble sort test, which was configured to sort 10,000 random numbers:
bubble(10000) - 1 thread
Time (secs)
vs. 3.15
vs. previous
3.10
3.9918
0.49x
3.11
2.6237
0.75x
1.52x
3.12
2.7341
0.72x
0.96x
3.13
2.833
0.70x
0.97x
3.14
2.0575
0.96x
1.38x
3.15
1.9716
1.04x
pypy3.12
0.1073
18.37x
node-26.3
0.0643
30.66x
rust-1.97
0.0391
50.42x
As in the previous test, here we can also see that 3.15 had a very small improvement in performance with respect to 3.14. And we again can see that 3.11 and 3.14 are the two recent releases of Python that have really moved the needle in terms of performance. Some releases are even showing small regressions on this test. PyPy continued to be very fast, but for this test Node.js was faster.
The next table and chart show the results for the JIT and free-threading editions of the Python interpreter:
bubble(10000) - 1 thread
Time (secs)
vs. 3.15
vs. previous
3.13 JIT
2.5887
3.14 JIT
2.3624
1.10x
3.15 JIT
1.5435
1.28x
1.53x
3.13 FT
4.1888
3.14 FT
2.7248
1.54x
3.15 FT
2.6808
0.74x
1.02x
This shows the same overall picture from the first test. The 3.15 JIT once again shows an impressive 1.28x speed gain over the regular interpreter. The free-threading version shows a performance drop with respect to the standard interpreter, but a similar drop occurred with the 3.14 interpreter, so this is not a regression. As I said before, this does not matter much because this test is single-threaded, so it isn't the kind of application that will ever help the free-threading interpreter shine. I think it is reasonable to expect the free-threading interpreter to perform comparably to the regular one, so from that point of view we can say that there is work to be done yet.
Test 3: fibo.py, multi-threaded
Let's now repeat all the tests, but running 4 threads in parallel. Given that this is a very specific test that is designed to evaluate the free-threading version of the Python interpreter, I'm dropping the non-Python runs.
To get a baseline, first I ran the multi-threaded test on the standard Pythons. To be absolutely clear, these results are going to be bad for CPython, because the global interpreter lock (GIL) prevents true concurrency between threads. Here are the results and chart for the multi-threaded Fibonacci test:
fibo(40) - 4 threads
Time (secs)
vs. 3.15
vs. previous
3.10
67.2867
0.48x
3.11
49.726
0.65x
1.35x
3.12
38.7307
0.84x
1.28x
3.13
38.9421
0.84x
0.99x
3.14
31.8367
1.02x
1.22x
3.15
32.5421
0.98x
pypy3.12
5.6385
5.77x
This test shows 3.15 being a tiny bit slower than 3.14. We've seen in the single-threaded tests that the 3.15 interpreter was only slightly faster than 3.14, so overall I think we can say that the standard interpreter is about the same speed as 3.14. Here we can also see that PyPy continues to run circles around standard Python, but with the threads its speed slowed it down by a similar ratio, because PyPy's concurrency is also affected by a GIL.
Now let's see how the JIT and free-threading versions of the Python interpreters do on this test.
fibo(40) - 4 threads
Time (secs)
vs. 3.15
vs. previous
3.13 JIT
38.5661
3.14 JIT
30.9696
1.25x
3.15 JIT
27.1641
1.20x
1.14x
3.13 FT
12.4376
3.14 FT
7.3052
1.70x
3.15 FT
7.235
4.50x
1.01x
The free-threading edition of the Python 3.15 interpreter runs about 4.5 times faster than the standard interpreter, and the ratio was about the same with 3.14. This significant speed gain can be attributed to the interpreter running without the GIL, which allows for more efficient thread concurrency.
A secondary observation that we can make from these results is that the JIT edition of the interpreter, which runs with the GIL, keeps a similar edge over the standard interpreter even when running multiple threads, and this is new with 3.15.
Test 4: bubble.py, multi-threaded
We have one more set of results to go over. Here are the standard interpreter results for the bubble sort test:
bubble(10000) - 4 threads
Time (secs)
vs. 3.15
vs. previous
3.10
16.5959
0.51x
3.11
10.7541
0.79x
1.54x
3.12
10.979
0.77x
0.98x
3.13
11.1337
0.76x
0.99x
3.14
8.7198
0.97x
1.28x
3.15
8.4514
1.03x
pypy3.12
0.5165
16.36x
This is, again, more or less in alignment with the previous results, with the 3.15 interpreter just a hair faster than 3.14.
Now that we have the baseline for this test, let's have a look at the JIT and free-threading interpreters:
bubble(10000) - 4 threads
Time (secs)
vs. 3.15
vs. previous
3.13 JIT
10.3004
3.14 JIT
9.9454
1.04x
3.15 JIT
6.6417
1.27x
1.50x
3.13 FT
8.0547
3.14 FT
4.9934
1.61x
3.15 FT
4.8549
1.74x
1.03x
And here the free-threading 3.15 interpreter is once again faster than the standard one. The gains are not as impressive as in the Fibonacci test, but this type of program is still a good use case for a GIL-free interpreter.
As for the JIT results, they seem consistent with all other runs of this interpreter, which show a great improvement in 3.15.
Conclusions
I hope you enjoyed looking at my benchmark. Maybe in addition to seeing a bunch of numbers and colorful charts, you are wondering what does this all mean in practical terms.
What I want to do before ending this article is to give you my personal interpretation of what these numbers suggest, because you may want to know if it makes sense to upgrade to 3.15, and what improvements you can expect to see when you do. In this section we are leaving determinism and enter opinion territory, so please keep in mind that someone else looking at these numbers may have a completely different interpretation than mine!
With the disclaimer out of the way, I'll say that my gut feeling after running the tests is that Python 3.15 is at best a fairly minor improvement over 3.14 in terms of performance. I may eventually upgrade production projects I currently have on 3.14 such as this website, but the results that I obtained do not make me want to rush an upgrade like I did after seeing such great results with 3.14 last year.
The only area where there is a clear improvement in the 3.15 release is in the JIT. But the JIT continues to be an experimental feature, so it is not a good idea to use it in production. I will consider using the JIT in production only when it is out of the experimental phase.
Aside from the JIT, there aren't really any significant performance gains in this release. Some tests do show a small performance increment, but others show regressions, so I don't expect these small variations to translate into noticeable performance changes for a real world project. I honestly don't feel I'm losing anything by staying on 3.14 for a few more months, or even until 3.16 drops in a year and I have one more release to evaluate.
I do, however, plan to use 3.15 as my main day-to-day interpreter, and maybe I will end up upgrading some of my production projects just so that I can use some of the new features, such as the JavaScript-like unpacking of comprehensions or the lazy imports.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
