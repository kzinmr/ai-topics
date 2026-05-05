---
title: "Bloom Filters and SQLite"
url: "https://boyter.org/posts/bloom-filters-sqlite/"
fetched_at: 2026-05-05T07:01:54.766843+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Bloom Filters and SQLite

Source: https://boyter.org/posts/bloom-filters-sqlite/

I was talking to someone recently about how searchcode.com works with regards to its bloom filter. The question came up about why it stores the index in memory and not on disk considering how fast disks are these days.
Now the answer is firstly performance, but the second is that writing all the code to store the index on disk is a lot of work and I didn’t feel like working on it. However I was curious… since I have been using SQLite a lot recently, how about storing the bloom filter on disk using that? It comes with its own indexes for stepping though the filters and is likely out of the box to be better than anything I could come up with quickly.
So I tried it out. Pulling some existing code I had
https://github.com/boyter/indexer
I was able to modify it slightly to create a bloom filter backed by SQLite.
I then populated it with some random values in order to simulate a bloom filter and ran some queries over it using two different select approaches. The first being where each portion of the filter is pulled back by a single select, and another where all of the values needed to be checked were pulled back. In effect
select num from bloom where id = ?
vs
select num from bloom where id in (?,?,?,?,?,?,?);
The reason for both is that the first has the potential to perform less disk seeks since it can calculate the bloom matches and skip later ones if not required, while the latter could be more efficient since SQLite can do everything in a single select operation.
Populating the index with 64,000 documents produced the following runtimes when searching.
> abc
serial 7839 31.975417ms
serial modified 7839 22.238459ms
As you would expect the second SQL selecting everything was faster, since with 2 hashes per trigram this would only need at most 6 rows to be pulled back into memory. However with a longer search term the reverse is true,
> abcdefghijklmnopqrstuvwxyz
serial 0 74.158208ms
serial modified 0 146.137125ms
Now the select multiple takes twice as much time to run.
Regardless however the runtime is unacceptable for searchcode.com… by comparison a similar index using searchcodes caisson index would run this query in under 1ms.
Anyway it was a interesting experiment to trial.
You can find the code for it all here
https://github.com/boyter/bloom-sqlite
Feel free to get more performance out of it. I know I will attempt again at some point when I am not so busy.
