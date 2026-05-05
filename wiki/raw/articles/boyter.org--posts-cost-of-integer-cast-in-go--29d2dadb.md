---
title: "Cost of a integer cast in Go"
url: "https://boyter.org/posts/cost-of-integer-cast-in-go/"
fetched_at: 2026-05-05T07:01:56.619135+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Cost of a integer cast in Go

Source: https://boyter.org/posts/cost-of-integer-cast-in-go/

Recently have been doing interviews at work for Go developers.
The filter for this is a simple review exercise. We present a small chunk of code and ask them to review it over 15 minutes pointing out any issues they see. The idea is to respect their and our time. It works pretty well and we can determine how much experience someone has by their ability to pick up the obvious vs subtle bugs.
One recent result came back with the following,
Using an int32 forces the cast from int which is inefficient
Which was interesting feedback. I don’t believe that to be the case. You lose data due to overflows which is what we expect but, I am fairly sure that the actual conversion is a single CPU operation and stupidly fast…
Of course, belief and hope are not a plan. So I thought I would actually test it.
To save you scrolling down, the answer is for a integer to integer cast it’s as close to “free” as any other CPU operation. Integer to float is about 3x slower, but again for most things you can consider it free.
I started by checking what the overhead of a bitwise & operation is. Since this is almost free from a CPU point of view, taking a single operation.
func
BenchmarkBitwiseAnd
(
b
*
testing
.
B
) {
var
x
int
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
x
+=
i
&
7
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
We keep the result of the
i & i
to ensure the compiler is not optimising anything away.
Running on a 2020 M1 Macbook Air produced the following.
BenchmarkBitwiseAnd-8    1000000000          0.5148 ns/op
So about 0.5 ns for each operation. Which given the clock speed of the CPU means we are observing a single operation. With this as the baseline lets try the int to int32 cast.
func
BenchmarkIntToInt32
(
b
*
testing
.
B
) {
var
x
int32
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
x
+=
int32(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToInt32-8    1000000000          0.5150 ns/op
Interesting. Almost the same as & meaning from a code point of view this is a free operation. What about casts to other integer types?
func
BenchmarkIntToInt64
(
b
*
testing
.
B
) {
var
x
int64
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
x
+=
int64(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToInt64-8    1000000000          0.5147 ns/op
I would expect the above to be just as fast as I am on a 64 bit machine and I suspect it compiles down to not even use the cast.
func
BenchmarkIntToInt16
(
b
*
testing
.
B
) {
var
x
int16
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
x
+=
int16(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToInt16-8    1000000000          0.5143 ns/op
func
BenchmarkIntToInt8
(
b
*
testing
.
B
) {
var
x
int8
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
x
+=
int8(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToInt8-8    1000000000          0.5149 ns/op
So, more or less free across the board! Which is as you would expect if you think about how a cast actually works on the CPU. However, what about unsigned ints?
func
BenchmarkIntToUInt32
(
b
*
testing
.
B
) {
var
x
uint32
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
x
+=
uint32(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToUInt32-8    1000000000          0.5131 ns/op
Same story it seems. I tried the other unsigned types and got the same result. I then thought it worth trying casting to floats, just to get an idea of how much more expensive that is.
func
BenchmarkIntToFloat32
(
b
*
testing
.
B
) {
var
x
float32
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
x
+=
float32(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToFloat32-8    775237407          1.540 ns/op
func
BenchmarkIntToFloat64
(
b
*
testing
.
B
) {
var
x
float64
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
x
+=
float64(
i
)
}
b
.
StopTimer
()
fmt
.
Println
(
x
)
}
BenchmarkIntToFloat64-8    778829048          1.555 ns/op
So about 3x the overhead to convert from int to float.
So in short, my inital throught seemed to hold up. What I also like is that I can stop stressing about casts in some of the more critical pieces of code I work on, as they are unlikely to be a bottleneck.
