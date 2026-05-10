---
title: "Fast regex search: indexing text for agent tools · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/fast-regex-search"
scraped: "2026-05-10T01:19:38.544229+00:00"
lastmod: "2026-05-09T16:09:42.638Z"
type: "sitemap"
---

# Fast regex search: indexing text for agent tools · Cursor

**Source**: [https://cursor.com/blog/fast-regex-search](https://cursor.com/blog/fast-regex-search)

Blog
/
research
Mar 23, 2026
·
research
Fast regex search: indexing text for agent tools
Vicent Marti
·
21 min read
Table of Contents
↑
The classic algorithm
Inverted Indexes
Trigram Decomposition
Putting it all together
Suffix Arrays: a detour
Trigram Queries with Probabilistic Masks
Sparse N-grams: Smarter Trigram Selection
All this, in your machine
Conclusions
Time is a flat circle. When the first version of
grep
was released in 1973, it was a basic utility for matching regular expressions over text files in a filesystem. Over the years, as developer tools became more advanced, it was gradually superseded by more specialized tools. First, by roughly syntactic indexes such as
ctags
. Later on, many developers moved to specialized IDEs for specific programming languages that allowed them to navigate codebases very efficiently by parsing and building syntactical indexes, often augmented with type-level information. Eventually this was standardized in the Language Server Protocol (LSP), which brought these indexes to all text editors, new and old. Then, just when LSP was becoming a standard, Agentic coding arrived, and what do you know: the agents just
love
to use
grep
.
There are other state-of-the art techniques to gather context for Agents. We've
talked in the past
about how much you can improve Agent performance by using semantic indexes for many tasks, but there are specific queries which the model can only resolve by searching with regular expressions. This means going back to 1973, even though the field has advanced a little bit since then.
Most Agent harnesses, including ours, default to using
ripgrep
when providing a search tool. It's a standalone executable developed by Andrew Gallant which provides an alternative to the classic
grep
but with more sensible defaults (e.g. when it comes to ignoring files), and with much better performance.
ripgrep
is notoriously fast because Andrew has
spent a lot of time thinking about speed
when matching regular expressions.
No matter how fast
ripgrep
can match on the contents of a file, it has one serious limitation: it needs to match on the contents of
all
files. This is fine when working in a small project, but many of Cursor's users, particularly large Enterprise customers, work out of very large monorepos. Painstakingly large. We routinely see
rg
invocations that take more than 15 seconds, and that really stalls the workflow of anybody who's actively interacting with the Agent to guide it as it writes code.
Matching regular expressions is now a critical part of Agentic development, and we believe it's crucial to target it explicitly: much like a traditional IDE creates syntactic indexes locally for operations like Go To Definition, we're creating indexes for the core operation that modern Agents perform when looking up text.
#
The classic algorithm
The idea of indexing textual data for speeding up regular expression matches is far from new. It was first published in 1993 by Zobel, Moffat and Sacks-Davis in a paper called
"Searching Large Lexicons for Partially Specified Terms using Compressed Inverted Files"
. They present an approach using n-grams (segments of a string with a width of
n
characters) for creating an inverted index, and heuristics for decomposing regular expressions into a tree of n-grams that can be looked up in the index.
If you've heard of this concept before, it's probably not from that paper, but from
a blog post
that Russ Cox published in 2012, shortly after the shutdown of Google Code Search. Let's do a quick refresher of the building blocks for these indexes, because they apply to basically every other approach to indexing that has been developed since.
#
Inverted Indexes
An inverted index is the fundamental data structure behind a search engine. Working off a set of documents to be indexed, you construct an inverted index by splitting each document into tokens. This is called tokenization, and there are many different ways to do it — for this example, we'll use the simplest possible approach, individual words as tokens. The tokens then become the keys on a dictionary-like data structure, while the values are, for each token, the list of all documents where it appears. This list is commonly known as a
posting list
, because each document is uniquely identified by a numeric value or "posting". When you search for one or more tokens, we load their posting lists; if there is more than one posting list, we intersect them to find the documents that appear in
all of them
.
1. Documents
Edit documents to see how the index updates. Click to select and view
terms
.
Hover or tap a term to trace the same index entry.
D
0
→
t
h
e
c
u
r
i
o
u
s
c
a
t
s
a
t
b
y
t
h
e
w
i
n
d
o
w
w
a
t
c
h
i
n
g
t
h
e
l
i
g
h
t
d
r
i
f
t
a
c
r
o
s
s
t
h
e
r
o
o
m
D
1
D
2
D
3
2. Inverted Index
Each
term
maps to documents containing it. Hover or tap to inspect one entry at a time.
a
c
r
o
s
s
→
D
0
D
1
D
2
a
n
d
→
D
2
D
3
b
a
t
→
D
3
b
l
a
c
k
→
D
2
b
y
→
D
0
D
1
D
2
D
3
c
a
t
→
D
0
D
2
c
a
u
t
i
o
u
s
→
D
1
c
u
r
i
o
u
s
→
D
0
d
r
i
f
t
→
D
0
f
a
l
l
→
D
1
i
n
→
D
3
l
i
g
h
t
→
D
0
D
1
D
2
D
3
r
a
t
→
D
1
r
o
o
m
→
D
0
D
1
D
2
D
3
s
a
t
→
D
0
D
1
D
2
D
3
s
m
a
l
l
→
D
3
t
h
e
→
D
0
D
1
D
2
D
3
w
a
t
c
h
e
d
→
D
2
D
3
w
a
t
c
h
i
n
g
→
D
0
D
1
w
i
n
d
o
w
→
D
0
D
1
D
2
D
3
20
unique
terms
from
4
documents
3. Search
Search for terms to find matching documents.
Try
cat
,
the
, or
ran
.
This design (with a lot of complexity bolted-on on top of it) is the basis for most search engines available today. But these are search engines for
natural language
, and we're trying to search for regular expressions, and we're trying to match them over source code. This doesn't quite work.
You can try to build something useful here by thinking very hard about tokenization — being aware of the syntax of each programming language, breaking up the identifiers in source code, and so on. This is very hard to get right. Back in the early days of GitHub, their Code Search feature worked like that: with a very complex tokenizer for programming languages, and a very large ElasticSearch cluster. The results were not good, and people had very poor opinions of the feature. You could search for identifiers (kind of), but not match regular expressions. You need a better way to tokenize in order to do that.
#
Trigram Decomposition
Naive tokenization on source code is not useful for matching regular expressions. We need to split the documents into more fundamental chunks. The classic algorithm chooses trigrams: a token is every overlapping segment of three characters in the input string.
Why three? We're going to store these trigrams as the keys in our inverted index. If we were to choose bigrams (chunks of 2), we would have very few keys in our index, up to 64k, but the posting lists on each key would be massive — too large to work with efficiently. If we went with quadgrams (chunks of 4), the posting lists would be tiny, which is a very good thing, but we would have billions of keys in our inverted index, and that's also hard to work with.
Trigrams are hence a pretty good middle ground. This makes tokenization when indexing documents very simple: extract every overlapping sequence of 3 characters from the document being indexed and use that as your tokens in the inverted index.
The actual complexity comes when tokenizing a regular expression so that it can be matched against the index. Regular expressions have
syntax
, so you need to parse them and use heuristics to figure out what trigrams can be extracted from the segments of the expression that actually represent text.
Decomposing a
literal string
into trigrams is straightforward, as it is the same algorithm as when you index a document. Extract every overlapping trigram contained in the string; a document that contains
all
these trigrams will probably contain the literal (but not necessarily!).
Alternations
are decomposed separately, resulting in two branches where
either
must be contained in a document for it to match. We query this on the inverted index by
joining
the posting lists instead of intersecting them. Character classes can be decomposed into many trigrams. Small classes like
[rbc]at
result in one trigram for each element of the class. When using
broader character classes
, we simply skip extracting those trigrams across those boundaries.
Regex Pattern:
/
/i
Regex Analysis
regex
/MAX_FILE_SIZE/
→
m
a
x
a
x
_
x
_
f
_
f
i
f
i
l
i
l
e
l
e
_
e
_
s
_
s
i
s
i
z
i
z
e
└──
seq
MAX_FILE_SIZE
→
m
a
x
a
x
_
x
_
f
_
f
i
f
i
l
i
l
e
l
e
_
e
_
s
_
s
i
s
i
z
i
z
e
└──
lit
"MAX_FILE_SIZE"
→
m
a
x
a
x
_
x
_
f
_
f
i
f
i
l
i
l
e
l
e
_
e
_
s
_
s
i
s
i
z
i
z
e
Required (AND):
_
f
i
_
s
i
a
x
_
e
_
s
f
i
l
i
l
e
i
z
e
l
e
_
m
a
x
s
i
z
x
_
f
#
Putting it all together
We know that trigrams are the right way to tokenize these documents, we know how to tokenize documents when building the index, and how to tokenize queries when searching. We can put all this together into an actual search index that can match regular expressions
very efficiently
. By decomposing any regular expression into a set of trigrams and loading all the relevant posting lists from the inverted index, we end up with a list of documents that can
potentially
match our regular expression. This is important! The final result set will only be obtained by actually loading all the potential documents and matching the regular expression "the old fashioned way". But having this sub-set of documents is always faster than having to scan and match the whole codebase, file by file.
1. Documents
Edit documents to see how the index updates. Click to select and view
trigrams
.
Hover or tap a trigram to trace the same index entry.
D
0
→
t
h
e
h
e
·
e
·
c
·
c
a
c
a
t
a
t
·
t
·
s
·
s
a
s
a
t
D
1
D
2
D
3
2. Inverted Index
Each
trigram
maps to documents containing it. Hover or tap to inspect one entry at a time.
·
b
a
→
D
3
·
c
a
→
D
0
D
2
·
r
a
→
D
1
D
2
·
s
a
→
D
0
D
3
a
·
c
→
D
2
a
t
·
→
D
0
D
1
D
2
D
3
b
a
t
→
D
3
c
a
t
→
D
0
D
2
e
·
b
→
D
3
e
·
c
→
D
0
e
·
r
→
D
1
h
e
·
→
D
0
D
1
D
3
r
a
n
→
D
1
D
2
r
a
t
→
D
1
s
a
t
→
D
0
D
3
t
·
r
→
D
1
D
2
t
·
s
→
D
0
D
3
t
h
e
→
D
0
D
1
D
3
18
unique
trigrams
from
4
documents
3. Search
Search using literal strings or regular expressions to see trigram decomposition.
Try
cat
,
the rat
, or the regex
c[au]t
.
Literal
Regex
This design is, by all means, fully functional. Projects like
google/codesearch
and
sourcegraph/zoekt
provide good performance for large indexes using an inverted index of trigrams (and like all search engines, they bolt-on a lot more complexity on top). But there are clear shortcomings here: the index sizes are
not
small, and decomposition at query time must make a trade-off. If you use simple heuristics, you'll decompose queries into a few trigrams, and that will result in a lot of potential documents to match. If you use complex heuristics, you may end up with dozens —perhaps hundreds— of trigrams, and loading all those from the inverted index may become as slow as simply searching everything from scratch.
We can do better than that.
#
Suffix Arrays: a detour
Since we're covering the history of indexing textual data for regular expression searches, I'd like to take a detour and discuss
this implementation
that Nelson Elhage developed in 2015 for his
livegrep
web service. Compared to other large industry efforts,
livegrep
is tiny —it only indexes the most recent version of the Linux Kernel— but because of its reduced scope, its implementation is very much unlike anything else out there, and that makes it very interesting and worth talking about.
Nelson attacked the problem from first principles: there's no inverted index powering this search engine. Instead, all the source code is indexed inside a
suffix array
.
The concept of a suffix array is self-descriptive: a sorted array of all the suffixes of a string. If you try constructing an array for a larger string, you'll see that the data structure grows quickly. It may seem a particularly expensive index, and in many ways it is, but its storage can be compressed very well if you have access to the original string: you can just store the offsets of the start of every suffix.
Once we have constructed a suffix array for the corpus to be searched, regular expression searches can be performed efficiently by de-composing the regular expression into literals. Every potential match position for a regular expression can then be found by performing a binary search over the suffix array.
Try searching for a short string like
th
to see how the binary search scopes all the positions in the document where it
does
match.
Search the Suffix Array
More complex structures in the regular expression syntax can be matched by exploiting the same properties of the suffix array. For instance, if you're matching a character range such as
[a-z]
, you can scope down the array by binary searching the start and the end of the range. Content between those two endpoints will necessarily match the range.
1. Input String
Enter a string to build its suffix array. Each position in the string defines a suffix.
Hover or tap a suffix row to see where that suffix starts in the string.
Character positions:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
h
i
t
h
e
r
·
a
n
d
·
t
h
i
t
h
e
r
2. Suffix Array
All suffixes sorted lexicographically. The array stores only indices; suffixes are derived from the original string.
Pos
Index
Suffix
0
6
·
a
n
d
·
t
h
i
t
h
e
r
1
10
·
t
h
i
t
h
e
r
2
7
a
n
d
·
t
h
i
t
h
e
r
3
9
d
·
t
h
i
t
h
e
r
4
16
e
r
5
4
e
r
·
a
n
d
·
t
h
i
t
h
e
r
6
15
h
e
r
7
3
h
e
r
·
a
n
d
·
t
h
i
t
h
e
r
8
12
h
i
t
h
e
r
9
0
h
i
t
h
e
r
·
a
n
d
·
t
h
i
t
h
e
r
10
13
i
t
h
e
r
11
1
i
t
h
e
r
·
a
n
d
·
t
h
i
t
h
e
r
12
8
n
d
·
t
h
i
t
h
e
r
13
17
r
14
5
r
·
a
n
d
·
t
h
i
t
h
e
r
15
14
t
h
e
r
16
2
t
h
e
r
·
a
n
d
·
t
h
i
t
h
e
r
17
11
t
h
i
t
h
e
r
Show
compact form
What are the shortcomings here? A suffix array must be constructed out of an input string. That is a big limitation. If you're trying to index a large codebase (or perhaps many different codebases), you'll first need to concatenate all the content into a single string, and construct the suffix array out of that. When matching inside the suffix array, you'll also need an auxiliary data structure to map the match position to the original file that contains it. It is not insurmountable complexity, but it makes dynamically updating the index very expensive. This is a solution that is very hard to scale.
#
Trigram Queries with Probabilistic Masks
Jumping back to some more traditional designs: here's an approach that was originally developed at GitHub for
Project Blackbird
. This was a research project aiming to replace the old Code Search feature. As we've discussed earlier, the old search was implemented by tokenizing source code and couldn't match regular expressions. The goal for this new implementation was developing something that could.
The first iterations attempted to use the classic inverted index with trigrams as keys, but it quickly ran into capacity issues. There is a lot of code in GitHub, and using trigrams to index it resulted in posting lists that were just too large to search.
As trigrams were not quite working out, the next step was finding a better size for the n-grams that would be indexed. We've seen that bigrams are too broad, because their posting lists become unmanageably large, and that quadgrams are too specific, because we end up with too many keys in our index. Trigrams are
a
sweet spot between the two, but in practice, the ideal size is more like... 3.5-grams. Yet we can't split a character in two, can we?
We can, in fact, do something quite close to that: this design proposes using trigrams as the key for the inverted index, and augmenting the posting lists with extra information about the "fourth character" that would follow the trigram in that specific document. To do that, we could simply store that fourth character as an extra byte, but that turns our index into a quadgram index, and we've seen those are just too large to store. What we store instead is a
bloom filter
that contains all the characters that follow that specific trigram.
1. Documents & Trigrams
Each trigram gets an
8
-bit
locMask
(position mod
8
) and
nextMask
(hash of each follow-up character).
Hover or tap a trigram to trace the same entry in the index.
D
0
→
t
h
e
@
0
h
e
·
@
1
e
·
f
@
2
·
f
o
@
3
f
o
x
@
4
D
1
D
2
D
3
2. Phrase-Aware Trigram Index
Each (trigram, doc) entry stores two
8
-bit masks. Hover or tap to inspect one trigram at a time.
·
c
a
D
1
loc
0
0
1
0
0
0
0
0
next
0
0
0
0
0
1
0
0
D
3
loc
0
0
0
0
1
0
0
0
next
0
0
0
1
0
0
0
0
·
f
o
D
0
loc
0
0
0
0
1
0
0
0
next
0
0
0
0
0
0
0
1
·
r
e
D
1
loc
0
0
0
0
0
0
1
0
next
0
0
0
1
0
0
0
0
·
r
u
D
2
loc
0
0
0
0
1
0
0
0
next
0
1
0
0
0
0
0
0
a
·
r
D
1
loc
0
0
0
0
0
0
0
1
next
0
0
1
0
0
0
0
0
c
a
r
D
1
loc
0
1
0
0
0
0
0
0
next
0
0
0
0
0
0
0
0
c
a
t
D
3
loc
0
0
0
1
0
0
0
0
next
0
0
0
0
0
0
0
0
d
·
c
D
1
loc
0
0
0
1
0
0
0
0
next
0
0
0
0
0
0
1
0
e
·
c
D
3
loc
0
0
0
0
0
1
0
0
next
0
0
0
0
0
0
1
0
e
·
f
D
0
loc
0
0
0
0
0
1
0
0
next
1
0
0
0
0
0
0
0
e
d
·
D
1
loc
0
0
0
0
1
0
0
0
next
0
0
0
0
1
0
0
0
f
o
x
D
0
loc
0
0
0
1
0
0
0
0
next
0
0
0
0
0
0
0
0
D
2
loc
0
0
0
0
0
0
0
1
next
0
0
0
0
0
0
0
1
h
e
·
D
0
loc
0
0
0
0
0
0
1
0
next
0
1
0
0
0
0
0
0
D
3
loc
0
0
0
0
0
0
1
0
next
0
0
0
0
1
0
0
0
o
x
·
D
2
loc
0
0
0
0
0
0
1
0
next
0
0
0
0
0
1
0
0
r
e
d
D
1
loc
0
0
0
0
0
1
0
0
next
0
0
0
0
0
0
0
1
r
u
n
D
2
loc
0
0
0
1
0
0
0
0
next
0
0
0
0
1
0
0
0
t
h
e
D
0
loc
0
0
0
0
0
0
0
1
next
0
0
0
0
0
0
0
1
D
3
loc
0
0
0
0
0
0
0
1
next
0
0
0
0
0
0
0
1
u
n
s
D
2
loc
0
0
1
0
0
0
0
0
next
0
0
0
0
0
0
0
0
x
·
r
D
2
loc
0
0
0
0
0
1
0
0
next
0
0
1
0
0
0
0
0
locMask
Bit
i
is set when the trigram can start at position
pos mod
8
= i
.
nextMask
Bits mark the hashed follow-up characters that can come right after the trigram.
You may think of a bloom filter as a very large and complex data structure, but it needn't be so. You can squeeze a bloom filter into very few bits. A lot of information can fit in 8 bits if you're careful when encoding it. With just two bytes per posting, we can work around the two biggest issues in a classic trigram index.
By having a mask that contains the characters following each trigram, our inverted index can be constructed using trigram keys, but we can query it using quadgrams! This already scopes down the potential documents much more than a simple trigram index could.
A second augmented mask, containing the offsets where the trigram appears in the document, solves the trigram ambiguity issue: just because a document contains two trigrams doesn't mean that they're actually
next to each other
, which is what we need to match our query. By shifting the position mask of our second trigram one bit to the left and comparing it with the mask for the first trigram, we can ensure that they are indeed adjacent. With particularly common trigrams, this is invaluable for scoping down even further the list of candidate documents.
All this information is, of course, probabilistic: like anything stored in a bloom filter, it can yield false positives. But false positives are always acceptable here, because the final matching is performed deterministically on the text itself. The goal is using our index to minimize the amount of potential documents we need to scan.
Search the Phrase Index
Query trigrams:
e
·
f
✓
·
f
o
✓
Checking consecutive pair:
"
e
·
f
" → "
·
f
o
"
A
Inverted Index Lookup
e
·
f
→
D0
·
f
o
→
D0
Candidates (intersection):
D0
Inspect one candidate:
Tap a row to expand the full bit-mask walkthrough.
D
0
"
the fox
"
nextMask
pass
locMask pass
candidate
D
0
"
the fox
"
B
Adjacency Filter (nextMask)
nextMask(
e
·
f
, D
0
):
7
6
5
4
3
2
1
0
1
0
0
0
0
0
0
0
hash(
o
) = bit
7
Bit is set
C
Position Filter (locMask + rotation)
locMask(
e
·
f
):
0
0
0
0
0
1
0
0
rotate left by 1:
↻
rotated:
0
0
0
0
1
0
0
0
locMask(
·
f
o
):
0
0
0
0
1
0
0
0
AND:
0
0
0
0
1
0
0
0
Non-zero intersection
Likely match, verify with a full scan
Algorithm result:
D
0
✓
Actual matches (full scan for "
e fo
"):
D0
The resulting indexes are
extremely efficient
, but
they have a major shortcoming. Bloom filters can become saturated.
That is an unfortunate property of bloom filters; they can be
updated, but if you add too much data to them, eventually all the
bits in the filter are set. And once the bloom filter is saturated,
it matches everything, so we're back to the performance of the very
first index we talked about.
This is an index that minimizes storage, but it becomes painful when
you need to update it in-place.
#
Sparse N-grams: Smarter Trigram Selection
Here's another very smart idea. You may have seen it used in ClickHouse for
their regular expression operator
, and also at GitHub, in the
new Code Search feature
that shipped a couple years ago and which does allow matching regular expressions. It's called Sparse N-grams, and it is the sweetest of the middle grounds.
A traditional trigram index extracts
every
consecutive 3-character sequence, but you can see how this creates
a lot of redundancy
. The characters in every trigram are duplicated in the adjacent ones! In this algorithm, we extract a random amount of n-grams, with each n-gram having a random length.
Of course
random
here cannot be truly random, because then the index couldn't be queried. We are assigning a "weight" to every pair of characters in the document. This weight could be anything, as long as it's deterministic (ClickHouse uses the
crc32
hash of the two characters). Then, our sparse n-grams are all substrings where the weights at both ends are strictly greater than all the weights contained inside.
Crucially, this means that sparse n-grams can have
any length
. They are not consistent. It also means that we can end up generating a lot of them — more than if we were simply extracting trigrams. But because the n-grams are being generated deterministically, we can do some very important optimizations at query time.  Let's see how.
This is not an easy algorithm to understand, so we'll have to play with it. You can use the
back
and
forward
arrows in the visualization to step through it.
Above the character breakdown for the input, you can see the random weight given to each character pair. These weights are what determine the segments that will be extracted as n-grams.
In the bottommost section, you can see a breakdown of how many sparse n-grams are extracted for the input string, and how many would be extracted if we were doing bigrams, trigrams or quadgrams. Note the stark difference: we're actually extracting
a lot
of sparse n-grams!
So what's the deal here? Are we simply doing something silly? Not quite. We're paying a high upfront cost when indexing so that we can have
very fast queries
at query time. The
build_all
algorithm you're watching right now is what we use when indexing documents. It extracts
all
the possible sparse n-grams from the input. Note, however, that we don't have to do that when querying. Because the weights are random but deterministic, at query time we can use a
covering algorithm
that only generates the minimal amount of n-grams required to match in the index.
Sparse N-Gram Algorithm
build_all
build_covering
We know that the n-grams are minimal because at index time, we only generate them when all the weights
contained inside
are smaller than the ones at the edges.  Hence, we only need to extract the sparse n-grams
at the edges
—way fewer than if we were to extract all trigrams— and we'll be able to select our potential documents with very high specificity.
Input String
Weight Function
CRC32
Frequency
(loading...)
Frequency (inv)
(loading...)
Pseudo-random weights based on CRC32 hash
⏮
◀
1
/
52
▶
⏭
#
1
Position 0: Consider bigram "MA" with weight 5D552B1
M
A
X
_
F
I
L
E
_
S
I
Z
E
0
1
2
3
4
5
6
7
8
9
10
11
12
0
/
13
covered
Stack
—
Emitted N-grams
—
Type
Total
Distribution
Sparse
17
2-grams
12
3-grams
11
4-grams
10
Can we do better than this? Yes! Much better, in fact. We've been using
crc32
as our weight function in the algorithm as an example. However, any hash function would work here, as long as it's deterministic. Let's pick something very smart: a hash function that gives a high weight to every pair of characters that is actually
very rare
, and a low weight to every pair that is
very frequent
.
This hash function is easy to compute. Since we're going to be indexing source code, we can pick up a couple terabytes of Open-Source code from the internet and build a frequency table for all the character pairs we find in it. That frequency table is our hash function. See what happens
when we apply it to our algorithm
: the highest weights now appear under the least frequent pairs of characters, and because of this, the
covering mode
results in
even fewer
n-grams to lookup, and fewer documents that can possibly match.
This approach that minimizes the amount of posting lookups will serve as the perfect starting point to construct indexes that can be efficiently queried on the users' machines.
#
All this, in your machine
Indexes for speeding up regular expression search need to live
somewhere
. All the designs we've seen so far have been deployed on the server side, and the semantic indexes we've talked about are also managed and queried on the server. And yet, we're choosing to go in a different direction here: we're building and querying the indexes in the users' machines.
There are several reasons why keeping these indexes locally makes sense. First, the indexes are just
one
part of what it is required to match a regular expression. They provide a scoped down subset of documents where the regular expressions could match, but you still need to individually scan each file. Doing that on the server would mean either synchronizing all the files, or performing expensive roundtrips back and forth to the client. Doing this on the client is trivial, and also sidesteps a lot of security and privacy concerns around data storage.
Latency also matters a lot for this functionality. Our Composer model has one of the fastest tokens per second (TPS) in the industry, and we're working hard to make it both smarter
and
faster. Adding network roundtrips for such a critical operation that the model uses
constantly
(oftentimes in parallel) just adds friction, stalls, and takes us in the opposite direction of what our goal is for interacting with Agents.
Unlike with semantic indexes, an index for regular expression search also needs to be
very fresh
, particularly when it comes to the model reading its own writes. We don't have to continuously update our semantic index because re-computing the embeddings for a file after it is modified does not cause the new embedding to significantly displace itself in the multi-dimensional space. The nearest-neighbor search we perform will still send the Agent in the right direction. However, if the agent is searching for specific text and it does not find it, it'll often go into a wild goose chase, waste tokens, and defeat the purpose of our performance optimization in the first place.
Bringing these indexes to the client does come with its own set of challenges. Synchronizing disk data can be complex and expensive, but we make it very efficient in practice: we control the state of the index by basing it off a commit in the underlying Git repository. User and agent changes are stored as a layer on top of it. This makes it very quick to update, and very fast to load and synchronize on startup.
To ensure that memory usage in the editor remains minimal, we store our indexes in two separate files. The first file contains all the posting lists for the index, one after the other — we flush this directly to disk during construction. The other file contains a sorted table with the hashes for all n-grams and the offset for their corresponding posting list in the postings file. Storing hashes here without storing the full n-grams is always safe: it can cause a posting list to become more broad when two hashes collide (extremely unlikely in practice), but it cannot give incorrect results. It also gives us a very tight layout for the lookup table. We then
mmap
this table, and only this table, in the editor process, and use it to serve queries with a binary search. The search returns an offset, and we read directly at that offset on the postings file.
Hover or tap a lookup-table row to trace where its posting lives on disk.
Lookup Table (mmap)
hash
offset
000129
0
0020ed
14
00239b
24
0026d8
40
002c70
32
002daf
80
002eaf
50
002f8d
64
002ff4
58
003305
72
0036f0
86
03bd65
8
Postings File (disk)
@
n-gram
files
0
MAX
→
0
3
8
AX_FI
→
0
14
FILE
→
0
2
4
24
LE_S
→
0
3
32
_SIZ
→
0
5
40
SIZE
→
0
5
6
50
conf
→
1
2
58
fig.
→
1
64
g.rs
→
1
4
72
main
→
3
7
80
ain.
→
3
86
util
→
2
4
6
Selected mapping:
000129
→ @
0
→
MAX
#
Conclusions
We've found that providing text search indexes to fast models, such as our own
Composer 2
, creates a qualitative difference for Agentic workflows. The impact is much more pronounced in larger Enterprise repositories, because
grep
is one of the few Agent operations whose latency scales with the size and complexity of the code being worked on. Take a look at these example workflows running with Composer 2: removing altogether the time spent searching the codebase provides meaningful time savings —particularly when the Agent investigates bugs— and allows for much more effective iteration.
Toggle the mode, then hover or tap a segment to inspect its duration.
Normal Grep
Instant Grep
Investigation in
chromium
Refactoring in
chromium
Investigation in
cursor
Minor feature in
cursor
0s
30s
60s
90s
120s
150s
180s
210s
240s
Thinking
Grep
Read
Edit
As for what's next, who knows! There are many exciting developments around providing context for Agents, and a lot of researchers working in the space — including ours. We're going to continue optimizing the performance of current approaches, including
semantic indexes
, and we're hoping to bring forward brand new ways of improving the performance of Agents even further, whilst always ensuring that they're operable where they really matter: in the largest repositories of the world, where the future of Agentic development is really gaining traction.
Filed under:
research
Author
:
Vicent Marti
