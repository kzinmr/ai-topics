---
title: "Rethinking full text search"
url: "https://idea.popcount.org/2012-07-02-rethinking-full-text-search"
fetched_at: 2026-05-05T07:01:14.565255+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Rethinking full text search

Source: https://idea.popcount.org/2012-07-02-rethinking-full-text-search

Rethinking full text search
02 July 2012
In
January 2009
I was wondering whether it is possible to build a full-text search
engine that could handle
the search for Twitter
. At that time the
search tool they provided was barely working. Later
Twitter acquired Summize
to solve this problem.
A search engine for Twitter presents a unique set of
constraints. Traditional full-text search engines assume that index
once created won't be changed, updating is expensive by
design. Twitter use case requires something opposite - adding items to
the index must happen instantly and cheaply.
I wondered if it's possible to have:
a basic full-text search engine
able to update indexes in real-time
horizontally scalable with regard to both data retrieval and
  indexing speed
ideally, based on simple architecture
At that time available open-source search engines weren't really
horizontally scalable and updating indexes was expensive. Scaling was
usually "solved" by serving the same index from multiple machines. As
updating index was quite complex, it was usually easier to create a
separate index for recent updates. But that resulted in a large number
of small indexes - which is very inefficient. To avoid that an
occasional merge was required.
Scaling required distributing very large indexes to the multiple
machines, while updating indexes means rewriting them. These two
behaviours don't play together nicely.
Being disappointed with available solutions and feeling the wave of
NoSQL I went for a quest:
Is it possible to build a full-text search engine on a distributed
key-value store?
Suffering the
not-invented-here syndrome
,
I jumped straight into coding.
Let the experiment begin
Writing the basic lexer and indexer
wasn't all that hard
.
I run a few experiments, mostly trying to index the huge
Wikipedia dump
,
and I was surprised to see the indexer, written in not-that-fast
Python, was not the biggest bottleneck.
Although initially it was indeed the slowest part of the system, when
the indexes grew to a certain size the storage layer started to ruin
the performance of the whole system.
The weakest link
I repeated the tests with both
Tokyo Cabinet
and
Berkeley DB
. Neither
behaved nicely when the dataset outgrew available memory.
It's not that surprising. Both databases are tuned for common usage
patterns. Storing data for a full-text search engine is definitely not
one of them.
What I needed is a key-value storage layer optimised for:
huge number of small objects
Full-text search index is composed of a huge number of mostly small
  items, at least one for every indexed word. Value size follows a
  logarithmic distribution, with most items having only a few bytes,
  followed by a long tail of much larger items.
large data sets
Stored data will be significantly larger than RAM size.
retrieval speed
Accessing every key should require at most one disk seek.
write speed
Writes should be bulked and done only to a single file at a
  time. That ensures an average write cost is close to zero disk
  seeks.
Again, at the time there wasn't a decent database layer having these
features. Recently alternatives started arriving - for example things
like
LevelDB
and
BitCask
promise
similar set of properties.
Naive database layer
I decided to write my own database, specially tuned for my specific
use case.
My first attempt was a rather simple database with an append-only log
architecture. In order to locate a particular key on a disk I stored
key metadata in-memory. Concretely the relationship stored in memory:
key
->
(
log_file
,
data_offset
,
data_size
)
I decided to use a simplest data structure for this - a binary tree.
The implementation
went smoothly
and soon I was able to squeeze more performance than from previously
tested databases. But then I hit another problem.
It's all about memory, Luke
The custom database performed well until it stopped with an
out-of-memory error. Ruling out implementation issues like memory
leaks, I realised that the memory cost of a single key was
non-negligible - specially when you try to store millions of keys.
For every stored key, my database needed to have an in-memory object
containing:
size
of
key
:
2
bytes
key
:
9
bytes
on
average
(
may
vary
)
log
file
number
:
4
bytes
value
offset
in
file
:
8
bytes
value
size
:
4
bytes
binary
tree
overhead
:
24
bytes
(
3
pointers
)
An average key length in my experiments was around 9 bytes, in total
that gives about 51 bytes per key. In theory in 4GiB RAM one could
store 84 million keys.
I clearly wanted to store more keys.
Beating trees
We can surely do better - by far the biggest contribution to the
memory usage is the binary tree overhead.  Almost all binary tree
implementations use three pointers per node (to
left
,
right
and
parent
nodes). Counting 8 bytes per pointer on a 64 bit architecture
gives a constant overhead of 24 bytes per key.
It's pretty disappointing when you realise that half of the nodes on
the tree have NULL in two out of three pointers - the leafs and have
no childs - they store an empty value in
left
and
right
!
What can be done to reduce memory footprint of a key in such database?
A lot. Later I was able to reduce the memory usage to about 33 bytes
per key.
But let's not jump ahead of the story. First, we need to find a more
memory efficient data structure than a stupid binary tree.
Continue reading →
