---
title: "Deduplicate a slice in Go, use sort or a map?"
url: "https://boyter.org/posts/deduplicate-slice-go-sort-or-map/"
fetched_at: 2026-05-05T07:01:56.105950+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Deduplicate a slice in Go, use sort or a map?

Source: https://boyter.org/posts/deduplicate-slice-go-sort-or-map/

TL;DR:
If you don’t need to preserve order of the elements, sort the slice first and dedupe.
I have been working on
https://searchcode.com
a fair bit recently, having been dealing with memory issues which were causing it to crash with out of memory exceptions. The cause of that was due to backtracking regular expressions in the syntax highlighter, which will be the subject of another post sometime.
As a result of the above I have spent a fair amount of time looking at memory profiles. One thing that stood out to me when doing so was a call I made to remove duplicate values from an array/slice of uint64. A fairly simple fuction that appeared often enough in the output.
I had previously written it to use a map, iterate through the array and remove the duplicates. I was curious if this was optimal. It wastes memory creating a map, but it does a single iteration of the array so it should be fine? Code included below. It was something I didn’t expect to ever appear in any profile but since it has lets explore some options.
func
DedupeUint64Old
(
elements
[]
uint64
) []
uint64
{
encountered
:=
map
[
uint64
]
bool
{}
var
result
[]
uint64
for
v
:=
range
elements
{
if
!
encountered
[
elements
[
v
]]
==
true
{
encountered
[
elements
[
v
]] =
true
result
= append(
result
,
elements
[
v
])
}
}
return
result
}
NB You could probably improve the above by using an
interface
struct rather than a bool to reduce the memory impact. If you need a function that preserves the order that might be a better implementation.
Since I was trying to remove memory pressure I reimplemented it. By sorting the array first, then checking the previous element to see if its the same and if so don’t add the current one. This is considered an optimal solution but requires a sorted slice. My guess was that it would ease the memory pressure, but be slower due to needing to sort. Note that this disturbs the order of the elements, but this was not a problem in my case. It looks like the below, and is much harder to understand.
func
DedupeUint64
(
s
[]
uint64
) []
uint64
{
if
len(
s
) <
2
{
return
s
}
sort
.
Slice
(
s
,
func
(
x
,
y
int
)
bool
{
return
s
[
x
] >
s
[
y
] })
var
e
=
1
for
i
:=
1
;
i
< len(
s
);
i
++
{
if
s
[
i
]
==
s
[
i
-
1
] {
continue
}
s
[
e
] =
s
[
i
]
e
++
}
return
s
[:
e
]
}
Wondering if I was about to lose some performance but save on the memory pressure I wrote a few benchmarks. I could then determine if it was worth it.
The results for an array of length 10 with random integers.
BenchmarkDedupeUint64
BenchmarkDedupeUint64-8               9487034        126.9 ns/op
BenchmarkDedupeUint64Old
BenchmarkDedupeUint64Old-8             1939953        618.0 ns/op
Another benchmark for much longer arrays with random integers.
BenchmarkDedupeUint64
BenchmarkDedupeUint64-8                 26967     120721 ns/op
BenchmarkDedupeUint64Old
BenchmarkDedupeUint64Old-8               10000     814634 ns/op
Benchmark where all of the elements in the array are the same IE input of more than one element but only one should be returned.
BenchmarkDedupeUint64Old
BenchmarkDedupeUint64Old-8               10000     109336 ns/op
BenchmarkDedupeUint64
BenchmarkDedupeUint64-8                 10000     112851 ns/op
Then a test with random ints picked from the first 100 (so there will be some duplicates).
BenchmarkDedupeUint64Old
BenchmarkDedupeUint64Old-8               10000     726771 ns/op
BenchmarkDedupeUint64
BenchmarkDedupeUint64-8                 10000     348226 ns/op
Finally a test where there are random numbers from the first 2048 ints.
BenchmarkDedupeUint64Old
BenchmarkDedupeUint64Old-8               10000     437698 ns/op
BenchmarkDedupeUint64
BenchmarkDedupeUint64-8                 10000     126301 ns/op
Someone requested the benchmark code, and I have added what I think was as close as possible to what I had implemented below.
func
BenchmarkDedupeUint64_10
(
b
*
testing
.
B
) {
r
:=
rand
.
New
(
rand
.
NewSource
(int64(
b
.
N
)))
rands
:=
make([]
uint64
,
10
)
for
i
:=
0
;
i
<
10
;
i
++
{
rands
[
i
] =
r
.
Uint64
()
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
DedupeUint64
(
rands
)
}
}
func
BenchmarkDedupeUint64_AllRandom
(
b
*
testing
.
B
) {
r
:=
rand
.
New
(
rand
.
NewSource
(int64(
b
.
N
)))
rands
:=
make([]
uint64
,
b
.
N
)
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
rands
[
i
] =
r
.
Uint64
()
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
DedupeUint64
(
rands
)
}
}
func
BenchmarkDedupeUint64_AllDuplicates
(
b
*
testing
.
B
) {
rands
:=
make([]
uint64
,
b
.
N
)
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
rands
[
i
] =
123
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
DedupeUint64
(
rands
)
}
}
func
BenchmarkDedupeUint64_Random100
(
b
*
testing
.
B
) {
r
:=
rand
.
New
(
rand
.
NewSource
(int64(
b
.
N
)))
rands
:=
make([]
uint64
,
b
.
N
)
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
rands
[
i
] = uint64(
r
.
Int63n
(
100
))
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
DedupeUint64
(
rands
)
}
}
func
BenchmarkDedupeUint64_Random2048
(
b
*
testing
.
B
) {
r
:=
rand
.
New
(
rand
.
NewSource
(int64(
b
.
N
)))
rands
:=
make([]
uint64
,
b
.
N
)
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
rands
[
i
] = uint64(
r
.
Int63n
(
2048
))
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
DedupeUint64
(
rands
)
}
}
I only have theories as to why this works, but I suspect the main one comes down to the sort impact being overshadowed by the increased cache hit rate, since there is no need to call out to a map to check the duplicate, and it probably fits nicely into the CPU cache. Map access being one of those things that can be slow in Go, hence some other implementations.
I thought this slightly interesting, and it was unexpected. Which is the case for almost anything I profile. The results are almost never what I expect.
EDIT
Someone wisely pointed out you should use a struct not interface which actually uses 16 bytes of space. Someone else wisely wanted to check my benchmark code which I have now included.
Hacker News Comments:
https://news.ycombinator.com/item?id=35536250#35537552
