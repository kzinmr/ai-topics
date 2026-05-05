---
title: "Counting Strings in C++: 30x Throughput Difference 💬"
url: "https://ashvardanian.com/posts/count-unique-strings/"
fetched_at: 2026-05-05T07:01:51.767274+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Counting Strings in C++: 30x Throughput Difference 💬

Source: https://ashvardanian.com/posts/count-unique-strings/

Some of the most common questions in programming interviews are about strings - reversing them, splitting, joining, counting, etc.
These days, having to interview more and more developers across the whole spectrum, we see how vastly the solutions, even to the most straightforward problems, differ depending on experience.
Let’s imagine a test with the following constraints:
You must find the first occurrence of every unique string in a non-empty array.
You are only allowed to use the standard library, no other dependencies.
You have 20 minutes.
In Python, the solution may look like this:
1
2
3
4
5
6
def
first_offsets
(
strings
:
list
[
str
])
->
dict
[
str
,
int
]:
offsets
=
{}
for
idx
,
string
in
strings
:
if
string
not
in
offsets
:
offsets
[
string
]
=
idx
return
offsets
There must be a way to make this faster, even in Python, but as often happens, the hack may backfire once the next CPython version comes out.
The simplest solution is generally the best.
In C++, that’s not the case.
There are many ways to implement the same thing, and the performance difference can be staggering.
Junior
#
C++ allows you to combine very high-level and low-level abstractions, giving you opportunities to improve almost any code snippet or shoot yourself in the foot.
We will do just that.
Let’s start with a solution that any developer can write after the first two C++ tutorials and progress through their career, marking potential differences in answers of Junior, Mid, Senior, and Enthusiast developers and benchmarking everything to get some unexpected results.
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
#include
<map>
#include
<string>
#include
<vector>
std
::
map
<
std
::
string
,
int
>
first_offsets
(
std
::
vector
<
std
::
string
>
strings
)
{
std
::
map
<
std
::
string
,
int
>
offsets
;
for
(
int
idx
=
0
;
idx
<
strings
.
size
();
idx
++
)
if
(
offsets
.
find
(
strings
[
idx
])
==
offsets
.
end
())
offsets
[
strings
[
idx
]]
=
idx
;
return
offsets
;
}
Mid
#
A mid-developer will probably have the following suggestions looking at that code:
Capturing a copy of an input
std::vector<std::string>
argument by value can be more expensive than the logic inside the function.
Using
std::map
is slower than
std::unordered_map
, both asymptotically and practically. One is a Binary Search Tree. Another one is a Hash-Table. You should probably use the latter if you don’t need sorted iterators.
Using
int
results in comparing integers of a different sign as the
strings.size()
output is a
std::size_t
In the end, a mid developer may add that
offsets.find
can be replaced with an
offsets.contains
in C++20 and patch the code like this:
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
#include
<unordered_map>
#include
<string>
#include
<vector>
std
::
unordered_map
<
std
::
string
,
std
::
size_t
>
first_offsets
(
std
::
vector
<
std
::
string
>
const
&
strings
)
{
std
::
unordered_map
<
std
::
string
,
std
::
size_t
>
offsets
;
for
(
std
::
size_t
idx
=
0
;
idx
<
strings
.
size
();
idx
++
)
if
(
!
offsets
.
contains
(
strings
[
idx
]))
offsets
[
strings
[
idx
]]
=
idx
;
return
offsets
;
}
Senior
#
Senior developers would notice that the previous solution performs two lookups for every new unique string.
First, when checking for presence with
contains
, and then on insertion.
The standard has more functionality than just
operator []
overloads:
insert
,
emplace
, and most importantly
try_emplace
, which will only add an entry, if the key isn’t present.
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
#include
<unordered_map>
#include
<span>
#include
<string>
#include
<string_view>
std
::
unordered_map
<
std
::
string_view
,
std
::
size_t
>
first_offsets
(
std
::
span
<
std
::
string
>
strings
)
{
std
::
unordered_map
<
std
::
string_view
,
std
::
size_t
>
offsets
;
for
(
std
::
size_t
idx
=
0
;
idx
!=
strings
.
size
();
++
idx
)
offsets
.
try_emplace
(
strings
[
idx
],
idx
);
return
offsets
;
}
Another anti-pattern is to use
std::vector<...> const &
, where all you need is just a span.
The
std::vector
is a very specific class template, that instantiates with a specific allocator and owns the memory.
But the logic of this function is independent of the memory allocator used for the input, so it is wiser to use
std::span
.
It is a surprisingly new tool, introduced in C++20, but every major C++ framework implements something like this.
A
Span
in Abseil,
Slice
in RocksDB, and so on.
Similarly, dynamically-allocating containers placed inside other dynamically allocating containers should be avoided where possible.
In this case it is easy, as we can use a
std::string_view
mapping into parts of the original input.
Enthusiast
#
Writing general-purpose libraries for most of the last decade, I have a natural tendency to overcomplicate things.
A passion for cutting-edge tech may only sometimes be an advantage, but let’s explore how we can improve the previous already good solution.
The
std::string_view
and
std::size_t
, being 16 and 8 bytes, respectively, will be combined into a
std::pair<std::string_view, std::size_t>
, resulting in a 32-byte structure, not 24. Moreover, one can’t stop thinking that we don’t need the
std::size_t
to solve the puzzle.
As everyone knows,
std::unordered_map
is not the fastest Hash-Table out there, and it is far from being space-efficient. To be more efficient, we need a Hash-Table with continuous addressing.
The
“Apple to Apple comparison”
article covers HTs in more details, benchmarking Arm-based Macs against older Intel-based versions and a $50K server.
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
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
#include
<bit>
// `std::bit_ceil`
#include
<span>
#include
<limits>
// `std::numeric_limits`
#include
<string>
#include
<vector>
#include
<optional>
#include
<functional>
// `std::hash`
#include
<string_view>
using
string_ptr_t
=
std
::
string
const
*
;
class
flat_unordered_set_t
{
string_ptr_t
first
{};
std
::
vector
<
string_ptr_t
>
hashed
{};
public
:
flat_unordered_set_t
(
std
::
span
<
std
::
string
>
strings
)
:
first
(
strings
.
data
()),
hashed
(
std
::
bit_ceil
<
std
::
size_t
>
(
strings
.
size
()
*
1.3
))
{
std
::
fill_n
(
hashed
.
data
(),
hashed
.
size
(),
nullptr
);
}
void
try_emplace
(
std
::
string
const
&
string
)
{
auto
hash
=
std
::
hash
<
std
::
string_view
>
{}(
string
);
auto
slot
=
hash
&
(
hashed
.
size
()
-
1
);
while
(
hashed
[
slot
]
&&
*
hashed
[
slot
]
!=
string
)
slot
=
(
slot
+
1
)
&
(
hashed
.
size
()
-
1
);
if
(
!
hashed
[
slot
])
hashed
[
slot
]
=
&
string
;
}
std
::
size_t
operator
[](
std
::
string_view
string
)
const
noexcept
{
auto
hash
=
std
::
hash
<
std
::
string_view
>
{}(
string
);
auto
slot
=
hash
&
(
hashed
.
size
()
-
1
);
while
(
hashed
[
slot
]
&&
*
hashed
[
slot
]
!=
string
)
slot
=
(
slot
+
1
)
&
(
hashed
.
size
()
-
1
);
return
hashed
[
slot
]
?
hashed
[
slot
]
-
first
:
std
::
numeric_limits
<
std
::
size_t
>::
max
();
}
};
std
::
optional
<
flat_unordered_set_t
>
first_offsets
(
std
::
span
<
std
::
string
>
strings
)
try
{
flat_unordered_set_t
offsets
{
strings
};
for
(
auto
const
&
string
:
strings
)
offsets
.
try_emplace
(
string
);
return
{
std
::
move
(
offsets
)};
}
catch
(...)
{
return
{};
}
This is a bit harder to implement in 20 minutes, but most C++ enthusiasts have probably implemented hash-tables at least a dozen times.
Which C++ and STL features did we use here?
Well, this solution is much longer - 45 lines instead of 10.
Let’s benchmark to see if it was worth it.
Benchmarks
#
Let’s generate large arrays of random strings controlling three variables:
number of strings in the input array,
size of the alphabet,
length of strings.
We would then use Google Benchmark to evaluate the four algorithms.
The last column contains the expected number of repetitions per unique string.
The other columns store the number of strings processed on 1 core.
The measurements were conducted on a 16" i9 2019 MacBook Pro.
The unit of measurement is: millions of strings per second.
Higher is better.
Junior
Middle
Senior
Enthusiast
1 M strings
32 char alphabet, length 3
3.1
13.2
12.6
23.9
32 char alphabet, length 4
0.8
2.0
2.0
14.0
32 char alphabet, length 5
0.6
1.4
1.2
18.6
1 M strings
16 char alphabet, length 3
4.9
21.5
19.2
31.0
16 char alphabet, length 4
2.2
9.8
8.9
20.5
16 char alphabet, length 5
0.8
2.0
2.1
13.2
32 char alphabet
1 M strings of length 3
3.1
13.2
12.6
23.9
100 K strings of length 4
0.9
2.5
2.6
26.3
10 K strings of length 5
1.4
3.3
3.6
41.6
In at least 2 cases we are getting close to 30x performance improvement even in the single-threaded environment.
In multi-threaded case, the memory allocations would be more expensive, and the gap would be wider.
Frankly speaking, reserving a relatively small buffer ahead of time and using copy-less Hash-Table with open addressing would obviously be faster than the associative container in STL.
The sources for the benchmark are on my GitHub, together with some other strings- and SIMD-related benchmarks.
Feel free to repeat and share your numbers.
What is the weird part?
The numbers for the Senior solution are sometimes worse, than the Middle, while the code looks strictly better.
If we just change the
try_emplace
line to this:
1
offsets
.
try_emplace
(
std
::
string_view
(
strings
[
idx
]),
idx
);
And rerun the benchmark:
1
2
3
cmake -DCMAKE_BUILD_TYPE
=
Release -B build_release
&&
\
make -j
12
--silent -C build_release
&&
\
build_release/unique_strings_cpp
The numbers for the senior case get strictly better.
This was a nice warm-up, but if you are curious about advanced string algorithms and ready to go below the C++ layer and into the assembly, check out StringZilla and some of the other libraries I maintain 🤗
