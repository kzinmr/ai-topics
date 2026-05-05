---
title: "Interesting Go Memory Issue"
url: "https://boyter.org/posts/interesting-go-memory-issue/"
fetched_at: 2026-05-05T07:01:57.341873+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Interesting Go Memory Issue

Source: https://boyter.org/posts/interesting-go-memory-issue/

So had an interesting experience with Go the other day.
This is part of building a bloom filter index which is going to replace the index in searchcode.com
So I was trying to verify how long a search would take when the index was full. When trying it out on a machine to see what the performance would be I built a version to create some very large slices over 64,000,000 items in length to simulate the expected workload. This should take about 53 GB in memory with all the overhead and such added in.
So in order to test it I used a 128 GB virtual machine on Digital Ocean, freshly spun up with a base Ubuntu 20.10 install. When running my application I managed to get a lot of out of memory errors. This was running just on the fresh install, and should never have gotten to the 128 GB limit.
I ended up putting in a
runtime.GC
inside the core loop to resolve the issue and was able to finish my tests.
However I wouldn’t have thought it possible. The application should never have hit that 128 GB threshold. I suspect because the Go GC triggers every time the heap doubles, it runs into OOM (no swap-file setup by default) when it gets to just over 64 GB of heap, and then doubles again without first running GC. Then crashes. Checking the following
https://blog.twitch.tv/en/2019/04/10/go-memory-ballast-how-i-learnt-to-stop-worrying-and-love-the-heap/
suggests that might be it as well, but would love someone else to have a theory of deny/confirm my one.
I suspect given a real workload this will be less of an issue because the creation will be slower than the 2 mins or so due to network and other impacts, but thats a problem for later when I actually fully implement it.
