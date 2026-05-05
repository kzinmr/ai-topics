---
title: "scc vs stto a code counter head to head"
url: "https://boyter.org/posts/scc-stto-head-to-head/"
fetched_at: 2026-05-05T07:01:54.921939+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# scc vs stto a code counter head to head

Source: https://boyter.org/posts/scc-stto-head-to-head/

A work colleague (Dazza!) messaged me this morning about a new code counter with some pretty serious performance claims. Not only was it claiming to be accurate it was claiming to have a 38x speed improvement over tools such as tokei!
Code counters are something I am interested in so I did some digging to find the repository
https://github.com/mainak55512/stto
Interesting it is written in Go.
My first though about the times was that all it was measuring is the startup time of a binary in whatever it’s written in to Go. No surprise Go is slower as it has GC and a runtime. However this is not the case here. That said, improving the startup time of scc for times below 20 ms is something I never worried about. There are two main reasons for that, use and human perception.
You have to consider how you run these tools. They are something you run every now and then on a new codebase, or an existing one to get an idea of its size over time. Its not something you call from a command line over and over. As such with the limits of human reaction time being around 100ms anything less than that is perceived to be instant from a human point of view. As such ~14 ms of startup time is not something I have ever worried about. Its a code counter, not a HFT tool.
That said if you don’t want to pay that penalty, say you are running scc over and over on different code bases, consider including it as a library.
The other thing is that benchmarks that run and end this quickly are subject to a lot of system noise. Lets look at something a bit harder to really see whats up.
$ hyperfine 'scc valkey' 'stto valkey'
Benchmark 1: scc valkey
  Time (mean ± σ):      51.0 ms ±   9.9 ms    [User: 180.5 ms, System: 93.8 ms]
  Range (min … max):    39.1 ms …  97.0 ms    29 runs

Benchmark 2: stto valkey
  Time (mean ± σ):     19.676 s ±  1.167 s    [User: 20.607 s, System: 33.182 s]
  Range (min … max):   18.715 s … 22.304 s    10 runs

Summary
  scc valkey ran
  385.53 ± 78.11 times faster than stto valkey
Here I ran scc and stto over a checkout of the Valkey redis fork. Ouch. However I know that walking directories multi-threaded is especially painful when one argument is given like this, so lets try it again in the directory itself. Incidentally if the author of stto wants to solve this
https://github.com/boyter/gocodewalker
which will also give proper .gitignore support (more on this later). Note there is a to be gained performance uplift needed in that code, I just haven’t gotten around to adding it yet. Want to help?
So running inside the directory gives the following,
$ hyperfine 'scc' 'stto'
Benchmark 1: scc
  Time (mean ± σ):      56.9 ms ±   4.8 ms    [User: 194.8 ms, System: 100.9 ms]
  Range (min … max):    41.3 ms …  69.1 ms    67 runs

Benchmark 2: stto
  Time (mean ± σ):      23.0 ms ±   2.2 ms    [User: 39.4 ms, System: 33.8 ms]
  Range (min … max):    20.5 ms …  29.5 ms    92 runs

Summary
  stto ran
    2.47 ± 0.32 times faster than scc
Cool. Not the claimed 38x speedup. But are they doing the same work?
Scc processed 1,545 files and 421,341 lines, while stto processed 536 files of 249,650 lines. So ~1/3 the number of files. Also note that scc is calculating complexity, here but I will leave that calculation in. In short though stto is 2x as fast for 3x less work. Thats due to less language support though. Lets make it more fair.
I had previously created a Python script that creates folders with files that all counters count correctly and equally to ensure I can gauge performance correctly, with identical work between all counters. You can find it here
https://github.com/boyter/scc/blob/master/examples/performance_tests/create_performance_test.py
With that run lets try it out. Note that for each case I changed into the directory I was testing to overcome the afore mentioned issue.
# Case 0
# Create a directory thats quite deep and put 10000 files at the end

Summary
  scc -c ran
    1.07 ± 0.07 times faster than stto

# Case 1
# Create a directory thats quite deep and put 100 files in each folder

Summary
  stto ran
    1.02 ± 0.26 times faster than scc -c

# Case 2
# Create a directory that has a single level and put 10000 files in it

Summary
  scc -c ran
    1.05 ± 0.09 times faster than stto

# Case 3
# Create a directory that has a two levels with 10000 directories in the second with a single file in each

Summary
  scc -c ran
    1.11 ± 0.11 times faster than stto

# Case 4
# Create a directory that with 10 subdirectories and 1000 files in each

Summary
  scc -c ran
    1.12 ± 0.14 times faster than stto

# Case 5
# Create a directory that with 20 subdirectories and 500 files in each

Summary
  scc -c ran
    1.15 ± 0.22 times faster than stto

# Case 6
# Create a directory that with 5 subdirectories and 2000 files in each

Summary
  scc -c ran
    1.07 ± 0.15 times faster than stto

# Case 7
# Create a directory that with 100 subdirectories and 100 files in each

Summary
  scc -c ran
    1.32 ± 0.16 times faster than stto
Cool, so close to a dead heat in one with stto being slightly faster and scc winning everything else. Note I didn’t warm the this, so scc has to eat the performance penalty of waiting for the OS to warm the disk cache for this. I was in a hurry.
How about accuracy? I did a quick check on the performance test python file, and the results from scc and stto were off… This was due to my guess of multiline strings, and a quick check of the stto repo shows this to be the case.
Lastly how about .gitignore support?
$ tree -a
.
├── 0
│   ├── .gitignore
│   └── 1.java
└── 1.java
The .gitignore in this case just ignores the file in the directory. As such we expect 1 file to be counted. The result?
$ scc --no-cocomo --no-size
───────────────────────────────────────────────────────────────────────────────
Language                 Files     Lines   Blanks  Comments     Code Complexity
───────────────────────────────────────────────────────────────────────────────
Java                         1       150       33         0      117         26
───────────────────────────────────────────────────────────────────────────────
Total                        1       150       33         0      117         26
───────────────────────────────────────────────────────────────────────────────

$ stto
+-----------+------------+-----------------+-----+----------+------+
| FILE TYPE | FILE COUNT | NUMBER OF LINES | GAP | COMMENTS | CODE |
+-----------+------------+-----------------+-----+----------+------+
| java      |          2 |             300 |  66 |        0 |  234 |
+-----------+------------+-----------------+-----+----------+------+

Stats
=======

Present working directory:  /Users/boyter/Documents/projects/performance_test/tmp
Total sub-directories:     1
Git initialized: false

Total files:          2 Total lines:        300
Total gaps:         66 Total comments:          0
Total code:        234
So stto does not support nested .gitignores. As mentioned though, if the author wants to use
https://github.com/boyter/gocodewalker
they could get support for this and the other issue for free!
So why post this? This is NOT a beat-down of the author of stto! In fact I starred the repo and I will be keeping and eye on it. It’s more to illustrate that making a fair benchmark is hard. It’s very easy to cherry pick results and make other tools look bad. Not that I mind that other tools exist. In fact I want more code counters out there. There is no “winning” in the open source space, I don’t lose money from “competition”.
No all I want is some more rigor around benchmarks and how they are presented. This is not because I am hurt if my tool is slower. In fact that would me happy, as I can learn from my mistakes. No, I want rigor because you owe it to your audience to do a proper job and reflect reality. Stto author if you read this please get in touch! Id love to discuss.
