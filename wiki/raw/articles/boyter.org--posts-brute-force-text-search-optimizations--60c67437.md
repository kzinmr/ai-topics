---
title: "Brute force text search optimizations"
url: "https://boyter.org/posts/brute-force-text-search-optimizations/"
fetched_at: 2026-05-05T07:01:55.308066+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Brute force text search optimizations

Source: https://boyter.org/posts/brute-force-text-search-optimizations/

One of the things I see commonly on any mockup is a search box, usually with vaguely defined requirements as to how this is meant to actually work. However most people tend to assume its an instant update as you type with a debounce option of 100ms or something.
The fastest way to implement this with a database is a horrible concatenated like query. However where you can store things in memory you can do a much better brute force search. A possible implementation in Go could look like the below.
terms
:=
strings
.
Fields
(
strings
.
ToLower
(
query
))
results
:=
[]
SomeType
{}
for
_
,
s
:=
range
searchable
{
isMatch
:=
true
for_
,
t
:=
range
terms
{
if
!
strings
.
Contains
(
s
.
content
,
t
) {
isMatch
=
false
break
}
}
if
isMatch
{
results
= append(
results
,
s
)
}
}
The trick being that SomeType has a field
content
in it, which is some concatenated lowercased text corpus of all the fields you want to search.
Oddly enough the above is good enough to ship and delight users. Also since computers are stupidly powerful, its not that bad in terms of performance either, and scales to tens of thousands of documents in many cases without issue.
However I was wondering is it possible to optimize the above? Either in terms of CPU or possibly more importantly memory usage.
The above will match on any substring. So you could search for the letter
a
and expect results. However because of this it means multiple
a
characters could be redundant, as only the first is needed to be considered a match. Consider the following,
the fast theologian fastly ran
The word
the
is redundant in the search because the word
theologian
also contains it. In fact if we apply this logic to the whole text we only need the following,
theologian fastly ran
. Spaces are also redundant so the string
theologianfastlyran
will produce the same outputs for the same inputs as
the fast theologian fastly ran
.
We can take this a little further to say that for each token in the corpus if a longer token exists that is a superset of that token we don’t need to include it. So
dant
as a token can be ignored if
redundant
exists. Note that the concept of a token is redundant for the corpus once made since we remove spaces, but useful when finding the subsets.
A somewhat slow (depending on your input size) function to achieve this follows.
func
bruteSearchOptimize
(
input
string
)
string
{
tokens
:=
strings
.
Fields
(
input
)
var
sb
strings
.
Builder
skipTokens
:=
map
[
string
]
struct
{}{}
for
i
:=
0
;
i
< len(
tokens
);
i
++
{
tok
:=
tokens
[
i
]
foundLonger
:=
false
// if we have already looked at this token, skip it, important for performance
_
,
ok
:=
skipTokens
[
tok
]
if
ok
{
continue
}
skipTokens
[
tok
] =
struct
{}{}
for
j
:=
i
;
j
< len(
tokens
);
j
++
{
tok2
:=
tokens
[
j
]
if
tok
==
tok2
{
continue
}
if
len(
tok2
)
<=
len(
tok
) {
continue
}
if
strings
.
Contains
(
tok2
,
tok
) {
foundLonger
=
true
}
}
if
!
foundLonger
{
sb
.
WriteString
(
tok
)
}
}
return
sb
.
String
()
}
I was curious about how well this would work, and so turned to my usual test text which is Jane Austen’s Pride and Prejudice. Running it though the above function takes about 6 seconds to process on my Macbook Air M1. However the memory saving at the end is considerable. My copy of Pride and Prejudice has a length of
785,141
and the “optimized” version has a length of a mere
80,651
. So about 1/10 of the initial size. For smaller documents there is less opportunity for reductions here.
What about searching though? We have removed the possibility of our search to find a potential match at the beginning of the text potentially causing it to iterate through the full 80,000 characters more often. With less to search however it may still be better.
A quick benchmark to determine this,
func
Benchmark_bruteSearch
(
b
*
testing
.
B
) {
terms
:=
[]
string
{
"jane"
,
"bennet"
,
"lizzy"
,
"darcy"
,
"nerves"
,
"sarcastic"
,
"netherfield"
,
"thousand"
,
"kitty"
,
"soldiers"
,
"ball"
,
"a"
,
"willnotexistihope"
}
b
.
ResetTimer
()
for
i
:=
0
;
i
<
b
.
N
;
i
++
{
for
_
,
t
:=
range
terms
{
strings
.
Contains
(
pride
,
t
)
}
}
}
func
Benchmark_bruteSearchOptimize
(
b
*
testing
.
B
) {
op
:=
bruteSearchOptimise
(
pride
)
terms
:=
[]
string
{
"jane"
,
"bennet"
,
"lizzy"
,
"darcy"
,
"nerves"
,
"sarcastic"
,
"netherfield"
,
"thousand"
,
"kitty"
,
"soldiers"
,
"ball"
,
"a"
,
"willnotexistihope"
}}
b
.
ResetTimer
()
for
i
:=
0
;
i
<
b
.
N
;
i
++
{
for
_
,
t
:=
range
terms
{
strings
.
Contains
(
op
,
t
)
}
}
}
I picked the search terms just based on what I know should exist inside the corpus as well as a worst case term that should not appear.
So after running the above a few times we get results as follows.
goos: darwin
goarch: arm64
pkg: github.com/boyter/tenders
Benchmark_bruteSearch
Benchmark_bruteSearch-8                1030    1150442 ns/op
Benchmark_bruteSearchOptimize
Benchmark_bruteSearchOptimize-8       18040      62702 ns/op
PASS
I am not going to lie this is a far more impressive result than I expected. It appears not only does this technique save on memory it is also considerably faster to search across. While there is a one off cost on the initial construction in memory, for documents that aren’t as long as Pride and Prejudice it’s a small one, and possibly worth it.
