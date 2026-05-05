---
title: "10x Faster C++ String Split, 16 Years Later 👴🏻"
url: "https://ashvardanian.com/posts/splitting-strings-cpp/"
fetched_at: 2026-05-05T07:01:50.086683+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# 10x Faster C++ String Split, 16 Years Later 👴🏻

Source: https://ashvardanian.com/posts/splitting-strings-cpp/

It’s 2025.
Sixteen years ago, someone
asked on StackOverflow how to split a string in C++
.
With 3000 upvotes, you might think this question has been definitively answered.
However, the provided solutions can be greatly improved in terms of both flexibility and performance, yielding up to a 10x speedup.
In this post, we’ll explore three better ways to split strings in C++, including a solution I briefly mentioned in 2024 as
part
of a longer review of the
Painful Pitfalls of C++ STL Strings
.
Tokenizing a String
#
The task is straightforward: given a sequence of bytes and some predefined delimiter characters, we want to split the sequence into substrings using these delimiters as separators.
Common use cases include:
Splitting lines using
'\n'
and
'\r'
as delimiters.
Splitting words using space (
' '
), horizontal tab (
'\t'
), and line breaks as delimiters.
The
default C locale classifies
six
characters as whitespace
: space, form-feed, newline, carriage return, horizontal tab, and vertical tab.
Most answers to the original question overlook this fact and simply use
' '
as the only delimiter.
In real-world parsing tasks, multiple delimiter characters are common - think
'<'
and
'>'
in XML, or
'{'
and
'}'
in JSON.
Therefore, our solutions should be applicable to a broad range of parsing applications.
C++17 STL String Views
#
The most straightforward way to implement a splitter is using
std::string_view::find_first_of
, unless we know the exact delimiter characters in advance:
1
2
3
4
5
6
7
8
9
template
<
typename
callback_type_
>
void
split
(
std
::
string_view
str
,
std
::
string_view
delimiters
,
callback_type_
&&
callback
)
{
std
::
size_t
pos
=
0
;
while
(
pos
<
str
.
size
())
{
auto
const
next_pos
=
str
.
find_first_of
(
delimiters
,
pos
);
callback
(
str
.
substr
(
pos
,
next_pos
-
pos
));
pos
=
next_pos
==
std
::
string_view
::
npos
?
str
.
size
()
:
next_pos
+
1
;
}
}
If you do know the delimiters, replacing
.find_first_of
with a lambda will yield a ~5x performance improvement:
1
2
3
4
5
6
7
8
9
template
<
typename
callback_type_
,
typename
predicate_type_
>
void
split
(
std
::
string_view
str
,
predicate_type_
&&
is_delimiter
,
callback_type_
&&
callback
)
{
std
::
size_t
pos
=
0
;
while
(
pos
<
str
.
size
())
{
auto
const
next_pos
=
std
::
find_if
(
str
.
begin
()
+
pos
,
str
.
end
(),
is_delimiter
)
-
str
.
begin
();
callback
(
str
.
substr
(
pos
,
next_pos
-
pos
));
pos
=
next_pos
==
str
.
size
()
?
str
.
size
()
:
next_pos
+
1
;
}
}
C++20 STL Ranges and C++14 Range-V3
#
C++20 introduces
std::ranges
, based on Eric Niebler’s Range-V3 library, which was recently featured in Daniel Lemire’s
post
on parsing.
It’s a perfect example of a library becoming a de-facto standard before official standardization.
Similar to Victor Zverovich’s
fmt
and
std::format
, the original library offers more functionality.
Installing Range-V3 with CMake is straightforward:
1
2
3
4
5
FetchContent_Declare
(
RangeV3
GIT_REPOSITORY
https://github.com/ericniebler/range-v3
GIT_TAG
master
)
FetchContent_MakeAvailable
(
RangeV3
)
While
std::ranges::split
can split around a single character delimiter, passing a lambda as the second argument results in a complex error message.
Fortunately, the
range-v3
library provides a
split_when
function that accepts a lambda as a delimiter:
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
#include
<range/v3/split_when.hpp>
#include
<range/v3/transform.hpp>
template
<
typename
callback_type_
,
typename
predicate_type_
>
void
split
(
std
::
string_view
str
,
predicate_type_
&&
is_delimiter
,
callback_type_
&&
callback
)
noexcept
{
for
(
auto
&&
token
:
ranges
::
split_when
(
str
,
is_delimiter
)
|
ranges
::
transform
([](
auto
&&
slice
)
{
// Transform sequence of characters back into string-views
// https://stackoverflow.com/a/48403210/2766161
auto
const
size
=
ranges
::
distance
(
slice
);
// `&*slice.begin()` is UB if the range is empty:
return
size
?
std
::
string_view
(
&*
slice
.
begin
(),
size
)
:
std
::
string_view
();
}))
callback
(
token
);
}
While ranges are a powerful library, merging slices of single-byte entries inevitably comes with performance overhead.
The Right Way
#
GLibC is arguably the world’s most popular string processing library.
However, looking into
<string.h>
feels like peering into the past, where everything was simpler and strings were
NULL
-terminated.
In that world,
strpbrk
would be the answer for fast, SIMD-accelerated tokenization.
Fast forward to today, strings may contain zero characters in the middle or not contain them at all.
This makes the
const char* strpbrk(const char* dest, const char* breakset)
function inadequate for handling arbitrary byte strings of known length.
Enter StringZilla and its C++ SDK:
1
2
3
4
5
FetchContent_Declare
(
StringZilla
GIT_REPOSITORY
https://github.com/ashvardanian/stringzilla
GIT_TAG
main
)
FetchContent_MakeAvailable
(
StringZilla
)
With StringZilla, we don’t need to implement
split
ourselves, as it’s provided through custom lazily-evaluated ranges.
We also don’t need a custom predicate.
The algorithm constructs a 256-slot bitset on the fly and checks chunks of 16-64 bytes at a time using SIMD instructions on both x86 and Arm:
1
2
3
4
5
6
7
8
#include
<stringzilla/stringzilla.h>
namespace
sz
=
ashvardanian
::
stringzilla
;
template
<
typename
callback_type_
,
typename
predicate_type_
>
void
split
(
std
::
string_view
str
,
std
::
string_view
delimiters
,
callback_type_
&&
callback
)
noexcept
{
for
(
auto
&&
token
:
sz
::
string_view
(
str
).
split
(
sz
::
char_set
(
delimiters
)))
callback
(
std
::
string_view
(
token
));
}
In previous specialized benchmarks on larger strings, StringZilla showed mixed results: it lost to GLibC on Intel Sapphire Rapids (5.42 GB/s vs 4.08 GB/s) but won on AWS Graviton 4 (3.22 GB/s vs 2.19 GB/s).
Both implementations were often 10x faster than C++ STL, which doesn’t use SIMD instructions.
For shorter strings, the performance difference is smaller and mostly depends on higher-level logic.
To replicate StringZilla pattern matching benchmarks:
clone the repo
,
pull the datasets
,
compile the code
, and run the
stringzilla_bench_search
target.
Let’s explore how these approaches perform in real-world scenarios.
Composite Benchmarks
#
While it’s easy to create a synthetic micro-benchmark that splits huge strings and shows a 10x improvement, a more interesting comparison would involve implementing a practical parser that does more than just splitting.
For our test, we’ll use two simple config files.
First, a small one:
1
2
3
4
5
6
# This is a comment line\r\n
host: example.com\n
\n
port: 8080\r
# Another comment\n\r
path: /api/v1
And a larger one with more complex configuration:
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
# Server Configuration
primary_host: api-main-prod-eu-west-1.company.com
secondary_host: api-backup-prod-eu-west-1.company.com
port: 443
base_path: /services/v2/resource/data-access-layer
connection_timeout: 120000
# Database Configuration
database_host: db-prod-eu-west-1.cluster.company.internal
database_port: 3306
database_username: api_service_user
database_password: 8kD3jQ!9Fs&2P
database_name: analytics_reporting
# Logging Configuration
log_file_path: /var/log/api/prod/services/access.log
log_rotation_strategy: size_based
log_retention_period: 30_days
# Feature Toggles
new_auth_flow: enabled
legacy_support: disabled
dark_mode_experiment: enabled
# Monitoring Configuration
metrics_endpoint: metrics.company.com/v2/ingest
alerting_thresholds: critical:90, warning:75, info:50
dashboard_url: https://dashboard.company.com/api/monitoring/prod
STL Parser
#
Parsing the config requires not only splitting but also trimming functions to strip whitespace around the key and value portions of each line:
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
#include
<cctype>
// `std::isspace`
#include
<string_view>
// `std::string_view`
bool
is_newline
(
char
c
)
noexcept
{
return
c
==
'\n'
||
c
==
'\r'
;
}
std
::
string_view
strip_spaces
(
std
::
string_view
text
)
noexcept
{
// Trim leading whitespace
while
(
!
text
.
empty
()
&&
std
::
isspace
(
text
.
front
()))
text
.
remove_prefix
(
1
);
// Trim trailing whitespace
while
(
!
text
.
empty
()
&&
std
::
isspace
(
text
.
back
()))
text
.
remove_suffix
(
1
);
return
text
;
}
std
::
pair
<
std
::
string_view
,
std
::
string_view
>
split_key_value
(
std
::
string_view
line
)
noexcept
{
// Find the first colon (':'), which we treat as the key/value boundary
auto
pos
=
line
.
find
(
':'
);
if
(
pos
==
std
::
string_view
::
npos
)
return
{};
// Trim key and value separately
auto
key
=
strip_spaces
(
line
.
substr
(
0
,
pos
));
auto
value
=
strip_spaces
(
line
.
substr
(
pos
+
1
));
// Store them in a pair
return
std
::
make_pair
(
key
,
value
);
}
void
parse
(
std
::
string_view
config
,
std
::
vector
<
std
::
pair
<
std
::
string
,
std
::
string
>>
&
settings
)
{
split
(
config
,
&
is_newline
,
[
&
](
std
::
string_view
line
)
{
if
(
line
.
empty
()
||
line
.
front
()
==
'#'
)
return
;
// Skip empty lines or comments
auto
[
key
,
value
]
=
split_key_value
(
line
);
if
(
key
.
empty
()
||
value
.
empty
())
return
;
// Skip invalid lines
settings
.
emplace_back
(
key
,
value
);
});
}
Ranges Parser
#
We can reuse the
is_newline
and
split_key_value
functions while leveraging ranges to create a more concise parser:
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
#include
<range/v3/view/filter.hpp>
#include
<range/v3/view/split_when.hpp>
#include
<range/v3/view/transform.hpp>
void
parse
(
std
::
string_view
config
,
std
::
vector
<
std
::
pair
<
std
::
string
,
std
::
string
>>
&
settings
)
{
namespace
rv
=
ranges
::
views
;
auto
lines
=
config
|
rv
::
split_when
(
is_newline
)
|
rv
::
transform
([](
auto
&&
slice
)
{
auto
const
size
=
ranges
::
distance
(
slice
);
return
size
?
std
::
string_view
(
&*
slice
.
begin
(),
size
)
:
std
::
string_view
();
})
|
// Skip comments and empty lines
rv
::
filter
([](
std
::
string_view
line
)
{
return
!
line
.
empty
()
&&
line
.
front
()
!=
'#'
;
})
|
rv
::
transform
(
split_key_value
)
|
// Skip invalid lines
rv
::
filter
([](
auto
&&
kv
)
{
return
!
kv
.
first
.
empty
()
&&
!
kv
.
second
.
empty
();
});
for
(
auto
[
key
,
value
]
:
std
::
move
(
lines
))
settings
.
emplace_back
(
key
,
value
);
}
StringZilla Parser
#
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
#include
<stringzilla/stringzilla.hpp>
namespace
sz
=
ashvardanian
::
stringzilla
;
void
parse
(
std
::
string_view
config
,
std
::
vector
<
std
::
pair
<
std
::
string
,
std
::
string
>>
&
settings
)
{
auto
newlines
=
sz
::
char_set
(
"
\r\n
"
);
auto
whitespaces
=
sz
::
whitespaces_set
();
for
(
sz
::
string_view
line
:
sz
::
string_view
(
config
).
split
(
newlines
))
{
if
(
line
.
empty
()
||
line
.
front
()
==
'#'
)
continue
;
// Skip empty lines or comments
auto
[
key
,
delimiter
,
value
]
=
line
.
partition
(
':'
);
key
=
key
.
strip
(
whitespaces
);
value
=
value
.
strip
(
whitespaces
);
if
(
key
.
empty
()
||
value
.
empty
())
continue
;
// Skip invalid lines
settings
.
emplace_back
(
key
,
value
);
}
}
Benchmarking Results
#
All code was compiled with
-O3
and
-march=native
flags using GCC 13.
Benchmarks were run on two different AWS EC2 instances running Ubuntu 24.04: Intel Sapphire Rapids and AWS Graviton 4.
Parser
Intel Sapphire Rapids
AWS Graviton 4
Small Config
Large Config
Small Config
Large Config
STL
179 ns
1606 ns
104 ns
1042 ns
Ranges v3
559 ns
6862 ns
540 ns
5702 ns
StringZilla
115 ns
666 ns
115 ns
964 ns
These benchmarks are integrated into the
less_slow.cpp
repository and can be easily replicated on Linux-based machines following the README instructions.
You’ll also find many more non-string performance comparisons there, including cases where
std::ranges
is the clear winner.
Byte in Set SIMD Kernels
#
For those curious about the low-level implementation details, let’s examine the actual SIMD kernels from the library - the
sz_find_charset_avx512
and
sz_find_charset_neon
functions.
AVX-512 Implementation
#
Wojciech Muła’s
blog post
provides excellent insights into byte-in-set algorithms.
While StringZilla’s implementation uses 512-bit ZMM registers instead of his 128-bit XMM registers, the core mechanics remain similar, as many AVX-512 instructions operate on 128-bit lanes.
One notable difference is the use of
K
mask registers for blends.
The bitset ordering differs slightly due to personal preference.
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
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
typedef
union
sz_u512_vec_t
{
__m512i
zmm
;
__m256i
ymms
[
2
];
__m128i
xmms
[
4
];
sz_u64_t
u64s
[
8
];
sz_u32_t
u32s
[
16
];
sz_u16_t
u16s
[
32
];
sz_u8_t
u8s
[
64
];
sz_i64_t
i64s
[
8
];
sz_i32_t
i32s
[
16
];
}
sz_u512_vec_t
;
sz_cptr_t
sz_find_charset_avx512
(
sz_cptr_t
text
,
sz_size_t
length
,
sz_charset_t
const
*
filter
)
{
// Before initializing the AVX-512 vectors, we may want to run the sequential code for the first few bytes.
// In practice, that only hurts, even when we have matches every 5-ish bytes.
//
//      if (length < SZ_SWAR_THRESHOLD) return sz_find_charset_serial(text, length, filter);
//      sz_cptr_t early_result = sz_find_charset_serial(text, SZ_SWAR_THRESHOLD, filter);
//      if (early_result) return early_result;
//      text += SZ_SWAR_THRESHOLD;
//      length -= SZ_SWAR_THRESHOLD;
//
// Let's unzip even and odd elements and replicate them into both lanes of the YMM register.
// That way when we invoke `_mm512_shuffle_epi8` we can use the same mask for both lanes.
sz_u512_vec_t
filter_even_vec
,
filter_odd_vec
;
__m256i
filter_ymm
=
_mm256_lddqu_si256
((
__m256i
const
*
)
filter
);
// There are a few way to initialize filters without having native strided loads.
// In the chronological order of experiments:
// - serial code initializing 128 bytes of odd and even mask
// - using several shuffles
// - using `_mm512_permutexvar_epi8`
// - using `_mm512_broadcast_i32x4(_mm256_castsi256_si128(_mm256_maskz_compress_epi8(0x55555555, filter_ymm)))`
//   and `_mm512_broadcast_i32x4(_mm256_castsi256_si128(_mm256_maskz_compress_epi8(0xaaaaaaaa, filter_ymm)))`
filter_even_vec
.
zmm
=
_mm512_broadcast_i32x4
(
_mm256_castsi256_si128
(
// broadcast __m128i to __m512i
_mm256_maskz_compress_epi8
(
0x55555555
,
filter_ymm
)));
filter_odd_vec
.
zmm
=
_mm512_broadcast_i32x4
(
_mm256_castsi256_si128
(
// broadcast __m128i to __m512i
_mm256_maskz_compress_epi8
(
0xaaaaaaaa
,
filter_ymm
)));
// After the unzipping operation, we can validate the contents of the vectors like this:
//
//      for (sz_size_t i = 0; i != 16; ++i) {
//          sz_assert(filter_even_vec.u8s[i] == filter->_u8s[i * 2]);
//          sz_assert(filter_odd_vec.u8s[i] == filter->_u8s[i * 2 + 1]);
//          sz_assert(filter_even_vec.u8s[i + 16] == filter->_u8s[i * 2]);
//          sz_assert(filter_odd_vec.u8s[i + 16] == filter->_u8s[i * 2 + 1]);
//          sz_assert(filter_even_vec.u8s[i + 32] == filter->_u8s[i * 2]);
//          sz_assert(filter_odd_vec.u8s[i + 32] == filter->_u8s[i * 2 + 1]);
//          sz_assert(filter_even_vec.u8s[i + 48] == filter->_u8s[i * 2]);
//          sz_assert(filter_odd_vec.u8s[i + 48] == filter->_u8s[i * 2 + 1]);
//      }
//
sz_u512_vec_t
text_vec
;
sz_u512_vec_t
lower_nibbles_vec
,
higher_nibbles_vec
;
sz_u512_vec_t
bitset_even_vec
,
bitset_odd_vec
;
sz_u512_vec_t
bitmask_vec
,
bitmask_lookup_vec
;
bitmask_lookup_vec
.
zmm
=
_mm512_set_epi8
(
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
//
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
//
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
//
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
,
-
128
,
64
,
32
,
16
,
8
,
4
,
2
,
1
);
while
(
length
)
{
// The following algorithm is a transposed equivalent of the "SIMDized check which bytes are in a set"
// solutions by Wojciech Muła. We populate the bitmask differently and target newer CPUs, so
// StrinZilla uses a somewhat different approach.
// http://0x80.pl/articles/simd-byte-lookup.html#alternative-implementation-new
//
//      sz_u8_t input = *(sz_u8_t const *)text;
//      sz_u8_t lo_nibble = input & 0x0f;
//      sz_u8_t hi_nibble = input >> 4;
//      sz_u8_t bitset_even = filter_even_vec.u8s[hi_nibble];
//      sz_u8_t bitset_odd = filter_odd_vec.u8s[hi_nibble];
//      sz_u8_t bitmask = (1 << (lo_nibble & 0x7));
//      sz_u8_t bitset = lo_nibble < 8 ? bitset_even : bitset_odd;
//      if ((bitset & bitmask) != 0) return text;
//      else { length--, text++; }
//
// The nice part about this, loading the strided data is vey easy with Arm NEON,
// while with x86 CPUs after AVX, shuffles within 256 bits shouldn't be an issue either.
sz_size_t
load_length
=
sz_min_of_two
(
length
,
64
);
__mmask64
load_mask
=
_sz_u64_mask_until
(
load_length
);
text_vec
.
zmm
=
_mm512_maskz_loadu_epi8
(
load_mask
,
text
);
// Extract and process nibbles
lower_nibbles_vec
.
zmm
=
_mm512_and_si512
(
text_vec
.
zmm
,
_mm512_set1_epi8
(
0x0f
));
bitmask_vec
.
zmm
=
_mm512_shuffle_epi8
(
bitmask_lookup_vec
.
zmm
,
lower_nibbles_vec
.
zmm
);
//
// At this point we can validate the `bitmask_vec` contents like this:
//
//      for (sz_size_t i = 0; i != load_length; ++i) {
//          sz_u8_t input = *(sz_u8_t const *)(text + i);
//          sz_u8_t lo_nibble = input & 0x0f;
//          sz_u8_t bitmask = (1 << (lo_nibble & 0x7));
//          sz_assert(bitmask_vec.u8s[i] == bitmask);
//      }
//
// Shift right every byte by 4 bits.
// There is no `_mm512_srli_epi8` intrinsic, so we have to use `_mm512_srli_epi16`
// and combine it with a mask to clear the higher bits.
higher_nibbles_vec
.
zmm
=
_mm512_and_si512
(
_mm512_srli_epi16
(
text_vec
.
zmm
,
4
),
_mm512_set1_epi8
(
0x0f
));
bitset_even_vec
.
zmm
=
_mm512_shuffle_epi8
(
filter_even_vec
.
zmm
,
higher_nibbles_vec
.
zmm
);
bitset_odd_vec
.
zmm
=
_mm512_shuffle_epi8
(
filter_odd_vec
.
zmm
,
higher_nibbles_vec
.
zmm
);
//
// At this point we can validate the `bitset_even_vec` and `bitset_odd_vec` contents like this:
//
//      for (sz_size_t i = 0; i != load_length; ++i) {
//          sz_u8_t input = *(sz_u8_t const *)(text + i);
//          sz_u8_t const *bitset_ptr = &filter->_u8s[0];
//          sz_u8_t hi_nibble = input >> 4;
//          sz_u8_t bitset_even = bitset_ptr[hi_nibble * 2];
//          sz_u8_t bitset_odd = bitset_ptr[hi_nibble * 2 + 1];
//          sz_assert(bitset_even_vec.u8s[i] == bitset_even);
//          sz_assert(bitset_odd_vec.u8s[i] == bitset_odd);
//      }
//
__mmask64
take_first
=
_mm512_cmplt_epi8_mask
(
lower_nibbles_vec
.
zmm
,
_mm512_set1_epi8
(
8
));
bitset_even_vec
.
zmm
=
_mm512_mask_blend_epi8
(
take_first
,
bitset_odd_vec
.
zmm
,
bitset_even_vec
.
zmm
);
__mmask64
matches_mask
=
_mm512_mask_test_epi8_mask
(
load_mask
,
bitset_even_vec
.
zmm
,
bitmask_vec
.
zmm
);
if
(
matches_mask
)
{
int
offset
=
sz_u64_ctz
(
matches_mask
);
return
text
+
offset
;
}
else
{
text
+=
load_length
,
length
-=
load_length
;
}
}
return
SZ_NULL_CHAR
;
}
ARM NEON Implementation
#
The ARM implementation is somewhat simpler, thanks to the
vqtbl1q_u8
instruction for table lookups.
The main challenge lies in replacing the x86
movemask
instruction, which can be accomplished using
vshrn
as described in Danila Kutenin’s
blog post
.
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
51
52
53
typedef
union
sz_u128_vec_t
{
uint8x16_t
u8x16
;
uint16x8_t
u16x8
;
uint32x4_t
u32x4
;
uint64x2_t
u64x2
;
sz_u64_t
u64s
[
2
];
sz_u32_t
u32s
[
4
];
sz_u16_t
u16s
[
8
];
sz_u8_t
u8s
[
16
];
}
sz_u128_vec_t
;
sz_u64_t
_sz_vreinterpretq_u8_u4
(
uint8x16_t
vec
)
{
return
vget_lane_u64
(
vreinterpret_u64_u8
(
vshrn_n_u16
(
vreinterpretq_u16_u8
(
vec
),
4
)),
0
)
&
0x8888888888888888ull
;
}
sz_u64_t
_sz_find_charset_neon_register
(
sz_u128_vec_t
h_vec
,
uint8x16_t
set_top_vec_u8x16
,
uint8x16_t
set_bottom_vec_u8x16
)
{
// Once we've read the characters in the haystack, we want to
// compare them against our bitset. The serial version of that code
// would look like: `(set_->_u8s[c >> 3] & (1u << (c & 7u))) != 0`.
uint8x16_t
byte_index_vec
=
vshrq_n_u8
(
h_vec
.
u8x16
,
3
);
uint8x16_t
byte_mask_vec
=
vshlq_u8
(
vdupq_n_u8
(
1
),
vreinterpretq_s8_u8
(
vandq_u8
(
h_vec
.
u8x16
,
vdupq_n_u8
(
7
))));
uint8x16_t
matches_top_vec
=
vqtbl1q_u8
(
set_top_vec_u8x16
,
byte_index_vec
);
// The table lookup instruction in NEON replies to out-of-bound requests with zeros.
// The values in `byte_index_vec` all fall in [0; 32). So for values under 16, substracting 16 will underflow
// and map into interval [240, 256). Meaning that those will be populated with zeros and we can safely
// merge `matches_top_vec` and `matches_bottom_vec` with a bitwise OR.
uint8x16_t
matches_bottom_vec
=
vqtbl1q_u8
(
set_bottom_vec_u8x16
,
vsubq_u8
(
byte_index_vec
,
vdupq_n_u8
(
16
)));
uint8x16_t
matches_vec
=
vorrq_u8
(
matches_top_vec
,
matches_bottom_vec
);
// Instead of pure `vandq_u8`, we can immediately broadcast a match presence across each 8-bit word.
matches_vec
=
vtstq_u8
(
matches_vec
,
byte_mask_vec
);
return
_sz_vreinterpretq_u8_u4
(
matches_vec
);
}
sz_cptr_t
sz_find_charset_neon
(
sz_cptr_t
h
,
sz_size_t
h_length
,
sz_charset_t
const
*
set
)
{
sz_u64_t
matches
;
sz_u128_vec_t
h_vec
;
uint8x16_t
set_top_vec_u8x16
=
vld1q_u8
(
&
set
->
_u8s
[
0
]);
uint8x16_t
set_bottom_vec_u8x16
=
vld1q_u8
(
&
set
->
_u8s
[
16
]);
// Process text in 16-byte chunks
for
(;
h_length
>=
16
;
h
+=
16
,
h_length
-=
16
)
{
h_vec
.
u8x16
=
vld1q_u8
((
sz_u8_t
const
*
)(
h
));
matches
=
_sz_find_charset_neon_register
(
h_vec
,
set_top_vec_u8x16
,
set_bottom_vec_u8x16
);
if
(
matches
)
return
h
+
sz_u64_ctz
(
matches
)
/
4
;
}
// Handle remaining bytes with serial implementation
return
sz_find_charset_serial
(
h
,
h_length
,
set
);
}
