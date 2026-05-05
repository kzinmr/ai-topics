---
title: "Search index implementations"
url: "https://boyter.org/posts/search-index-implementations/"
fetched_at: 2026-05-05T07:01:56.843395+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Search index implementations

Source: https://boyter.org/posts/search-index-implementations/

A living document where I will be putting information about search index implementations as I learn about them.
So there are a few talked about ways to search across content or build an index that I am aware of. Lets discuss each in term with its advantages and disadvantages
Brute Force
Brute Force, note that this isn’t an index strategy per say, but worth discussing anyway. Assuming you can get the entire corpus you are search into RAM it is possible to brute force search. I’m including it here so I have the advantages and disadvantages. While brute force isnt a solution to every problem, a lot of problems are pretty brute forcible given enough CPU and RAM.
Advantages
100% space efficient (for the index anyway) since there isn’t one
Easy to query/write
Can determine TF easily as its a positional “index”
Scales (assuming you are prepared to pay)
Disadvantages
Slow… at scale if you cannot fit your corpus in RAM
Harder to scale because gotta duplicate all the data
Writing high performance string searches is a hard problem
Inverted Index
Inverted index. This is pretty much building a map of terms to documents and then intersecting them and ranking. One issue with this technique is that you end up with enormous term lists, known as posting lists for common terms.
Advantages
Easy to query
Does not miss terms
Can store TF alongside terms creating a positional index
Fast and easy; intersecting posting lists is something you can hand off to your most junior developer (at least initially)
Query execution time is related to the number of returned results
Disadvantages
Harder to do wildcard queries OR use more space for them
Hard to update documents and avoid false positives, usually have to rebuild the index or do delta + merge
Need to implement skip lists or compression on the posting lists at scale
Queries can be slow due to the complexity of the list structures
Trie
Trie for example
https://github.com/typesense/typesense
which uses Adaptive Radix Tree
https://stackoverflow.com/questions/50127290/data-structure-for-fast-full-text-search
Advantages
Constant lookup time
Potential to be space efficient if key terms share the same prefixes
Easy to do wildcard queries
Can store TF alongside terms as a positional index
Disadvantages
Can take up more space if lots of prefixes
Not friendly to GC due to the use of pointers (problem for Go/Java and other GC languages)
Need to implement skip lists or compression on the posting lists at scale
Bit Signatures
This is something I remember reading about years ago, and found this link to prove I had not lost my mind
https://www.stavros.io/posts/bloom-filter-search-engine/
At the time I thought it was neat but not very practical… However then it turns out that Bing has been using this technique over its entire web corpus
http://bitfunnel.org/
https://www.youtube.com/watch?v=1-Xoy5w5ydM
Advantages
Stupidly fast if careful (bitwise operations are almost free from a CPU point of view)
Space/Memory efficient as it’s compressed
Easy to update/delete modify the document in memory
Disadvantages
Cannot store TF information along terms as its a non-positional index
Produces false positive matches
Query execution time is linear in the collection size (bitfunnel is about reducing this to an extent)
Memory bandwidth of the machine limits how large the index can grow on a single machine
