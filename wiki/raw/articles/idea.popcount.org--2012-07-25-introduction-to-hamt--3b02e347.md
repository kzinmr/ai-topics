---
title: "Introduction to HAMT"
url: "https://idea.popcount.org/2012-07-25-introduction-to-hamt"
fetched_at: 2026-05-05T07:01:14.441800+00:00
source: "Marek Vavruša (idea.popcount)"
tags: [blog, raw]
---

# Introduction to HAMT

Source: https://idea.popcount.org/2012-07-25-introduction-to-hamt

Introduction to HAMT
25 July 2012
In the previous post I explained
that a binary tree wasn't the best data structure for my needs - it
wastes too much memory.
I looked for a memory-efficient data structures and I found a gem:
Hash Array Mapped Trie (HAMT)
.
The author, Phil Bagwell, wrote two papers related to the subject:
Fast And Space Efficient Trie Searches, 2000 (pdf)
(source)
In this paper the author is comparing various implementations of
   Tries and introduces Array Mapped Trie.
Ideal Hash Trees, 2001 (pdf)
(source)
This paper describes using Array Mapped Trie as a good data
  structure for a generic
hash table
.
Let's start with the basics.
The basics
Okay, let's not start with the basics. Tries (aka. prefix Trees) are
nicely described on Wikipedia
, go
and read that first.
An exectuive summary: Tries are like normal Trees but, instead of
having a value stored on every node, it is only stored on the final leaves.
For comparison, here's the normal binary Tree storing values
00000000
,
11111110
and
11111111
:
And a Trie (prefix tree) whith prefix size of two bits:
Although it may look good, we haven't yet described the data structure
in all details: how to store mapping between prefix and value or pointer
on every node?
Naive representation
One obvious idea may be to just use an array for that. In our tree
that would mean an array of length four for every node.  This is
indeed a good idea - no need to find the relevant mapping, just use
the prefix as an array index:
The problem is that memory footprint is quite big. Even for our simple
case there are a lot slots wasted by NULL values.
Compression
Mr Bagwell in his paper proposes compressing this array by using a
bitmap to store which slots are not-NULL. For example,
the map for the first leaf:
would be:
1001
. Having this bitmap, we are able to compress the
array and store only something like that:
With the mask and a few bitwise operations (including the famous
popcount
instruction) it is
possible to quickly say which position on the array holds which exact
prefix. For example in our case
00
is the 0th element of the array
and stores a value, and
11
is 1st element and stores the pointer to
next layer.
Our Trie after compression will look like:
No bytes are now wasted and retrieving data still has complexity
proportional to the prefix length.
Now you know how a compressed Trie works and that it keeps all the
advantages of the Trie but having optimal memory footprint.
More tweaks
I described a simplified data structure, much more can be done to
make it go really fast.
Memory management
The uncompressed implementation has an advantage - every node was
exactly the same size and memory management is trivial.  The
compressed variant on the other hand doesn't waste any memory, but it
puts a lot of stress onto the "malloc(3)" implememtation.
Implementing a tuned for this data structure memory allocator is
neccesary to gain an ultimate performance.
Bitmask size
I showed examples of 2-bit dispatching, but original Hash Array Mapped
Trie described in the paper is using 5 bits on each layer (bitmaps of
size 32 bits). Of course, nothing is stopping from extending the schema
to 64 bitmaps and 6 bits for each layer.
Closing words
HAMT is a very nice data structure. Reasonably easy to work with, with
very good performance characteristics when the keys are distributed
uniformally. This suits ideally for a generic hash table
implementation and will work well for my full-text search engine if
I'll use md5 checksums instead of plaintext words for keys.
Finally, HAMT introduces very little memory overhead.
