---
title: "The Painful Pitfalls of C++ STL Strings 🧵"
url: "https://ashvardanian.com/posts/painful-strings/"
fetched_at: 2026-05-05T07:01:50.526137+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# The Painful Pitfalls of C++ STL Strings 🧵

Source: https://ashvardanian.com/posts/painful-strings/

Criticizing software is easy, yet the C++ and C standard libraries have withstood the test of time admirably.
Nevertheless, they are not perfect.
Especially the
<string>
,
<string_view>
, and
<string.h>
headers.
The first two alone bring in
over 20,000 lines of code
, slowing the compilation of every translation unit by over 100 milliseconds.
Most of that code seems
dated, much slower than LibC, and equally error-prone
, with interfaces that are very hard to distinguish.
This is not a new problem, and I don’t have an exhaustive list of all the issues with STL and LibC, but some issues became very noticeable when upgrading
StringZilla
to
v3
.
The upgrade makes it largely compatible with STL, stateful allocators aside.
Now it covers most of C++ 20 strings functionality in a C++ 11 compatible form, also adding dynamic (runtime) dispatch for SIMD-accelerated functions.
It also provides a few extensions, that are not present in STL, but are common in other languages.
For most code bases, replacing
std::string
and
std::string_view
with
sz::string
and
sz::string_view
should now be a
drop-in replacement
.
Error Prone APIs
#
Ambiguous Function Overloads
#
Let’s start with a question.
The
std::string
has
14 variants of
replace
with different argument order and meaning.
Can you guess what they do?
1
2
3
4
5
6
7
8
using
str
=
std
::
string
;
str
(
"hello"
).
replace
(
1
,
2
,
"123"
);
str
(
"hello"
).
replace
(
1
,
2
,
str
(
"123"
),
1
);
str
(
"hello"
).
replace
(
1
,
2
,
"123"
,
1
);
str
(
"hello"
).
replace
(
1
,
2
,
"123"
,
1
,
1
);
str
(
"hello"
).
replace
(
1
,
2
,
str
(
"123"
),
1
,
1
);
str
(
"hello"
).
replace
(
1
,
2
,
3
,
'a'
);
str
(
"hello"
).
replace
(
1
,
2
,
{
'a'
,
'b'
});
I definitely can’t… despite testing this functionality last week.
Those seven
replace
calls produce six different results.
1
2
3
4
5
6
7
8
using
str
=
std
::
string
;
str
(
"hello"
).
replace
(
1
,
2
,
"123"
)
==
"h123lo"
;
str
(
"hello"
).
replace
(
1
,
2
,
str
(
"123"
),
1
)
==
"h23lo"
;
str
(
"hello"
).
replace
(
1
,
2
,
"123"
,
1
)
==
"h1lo"
;
str
(
"hello"
).
replace
(
1
,
2
,
"123"
,
1
,
1
)
==
"h2lo"
;
str
(
"hello"
).
replace
(
1
,
2
,
str
(
"123"
),
1
,
1
)
==
"h2lo"
;
str
(
"hello"
).
replace
(
1
,
2
,
3
,
'a'
)
==
"haaalo"
;
str
(
"hello"
).
replace
(
1
,
2
,
{
'a'
,
'b'
})
==
"hablo"
;
This complexity is likely a byproduct of the standard library’s evolutionary path:
std::string
was welcomed in C++ 98.
std::string_view
made its debut in C++ 17.
std::span
joined the roster in C++ 20.
I’ve noticed a trend of preferring these newer constructs in reverse order.
Absent non-owning views and slices, you’re bound to lug around references to the original strings.
Doing so, you need to pass additional integer arguments to specify the range of the original string you want to operate on.
This raises another inquiry - why opt for integers over iterators?
And more crucially, how thorough are the checks on these integer parameters?
Asymmetric “Out of Bounds” Checks
#
Most containers in the C++ standard library have an
operator[]
and an
at
method.
The
operator[]
is fast, unchecked, and can lead to undefined behavior.
The
at
method is slower, checked, and throws an exception on out-of-bounds access.
Easy to remember when it’s just one argument per function.
What if you have two arguments?
Common sense suggests that argument checking is either done for both or for neither.
Documentation suggests otherwise.
1
2
3
4
5
6
7
using
str
=
std
::
string
;
str
(
"hello world"
).
substr
(
6
)
==
"world"
;
str
(
"hello world"
).
substr
(
6
,
100
)
==
"world"
;
// 106 is beyond the length of the string, but its OK
str
(
"hello world"
).
substr
(
100
);
// leads to `std::out_of_range`, as 100 is beyond the length of the string
str
(
"hello world"
).
substr
(
20
,
5
);
// leads to `std::out_of_range`, as 20 is beyond the length of the string
str
(
"hello world"
).
substr
(
-
1
,
5
);
// leads to `std::out_of_range`, as -1 casts to unsigned without any warnings...
str
(
"hello world"
).
substr
(
0
,
-
1
)
==
"hello world"
;
// -1 casts to unsigned without any warnings...
The
substr
method is the one-dimensional sibling of the zero-dimensional
at
.
Instead of returning one
char
scalar, it returns a string slice.
The kicker is that the
substr
method has a boundary check for the first argument but not for the second.
Moreover, unless you enable “warnings as errors”, the compiler won’t even warn you about the negative arguments
1
2
std
::
string
s
=
"hello world"
;
s
.
substr
(
1
,
s
.
size
()
-
2
)
==
"ello worl"
;
It’s debatable, but Python’s support for negative indices is more intuitive.
Without it, you need to write
s.substr(1, s.size() - 2)
instead of
s.substr(1, -2)
.
With StringZilla, you can use negative indices and get the expected results:
1
2
3
4
5
6
7
using
str
=
sz
::
string
;
str
(
"a:b"
).
front
(
1
)
==
"a"
;
// no checks, unlike `substr`
str
(
"a:b"
).
back
(
-
1
)
==
"b"
;
// accepting negative indices
str
(
"a:b"
).
sub
(
1
,
-
1
)
==
":"
;
// similar to Python's `"a:b"[1:-1]`
str
(
"a:b"
).
sub
(
-
2
,
-
1
)
==
":"
;
// similar to Python's `"a:b"[-2:-1]`
str
(
"a:b"
).
sub
(
-
2
,
1
)
==
""
;
// similar to Python's `"a:b"[-2:1]`
"a:b"
_sz
[{
-
2
,
-
1
}]
==
":"
;
// works on views and overloads `operator[]`
We can’t have all the good things for now.
Due to language constraints, the
"a:v"[-2:-1]
syntax is impossible.
So I’ve used an
std::initializer_list
for the indices, and an underscore-prefixed literal for the view.
Missing Functionality
#
Continuing the topic of extended functionality, there are some very basic utilities missing in STL.
This includes lazy ranges for
find
,
split
, and bulk
replace
.
Split and Search Lazy Ranges
#
Many production code bases have utility functions like:
1
2
3
std
::
vector
<
std
::
string
>
split
(
std
::
string
const
&
text
,
char
delimiter
);
std
::
vector
<
std
::
string
>
split
(
std
::
string
const
&
text
,
std
::
string
const
&
delimiter
);
std
::
vector
<
std
::
string_view
>
split
(
std
::
string_view
text
,
std
::
string_view
delimiter
);
Going from worst to best, they allocate memory at least for the
std::vector
, and reallocate when it needs to grow.
Each allocation can be orders of magnitude more expensive than the search itself.
StringZilla provides lazily-evaluated ranges to avoid those, similar to Rust and some other systems languages.
Implementing them in C++ is not trivial and took about 400 lines of expression templates.
Now, StringZilla supports overlapping and non-overlapping substring search ranges.
Splits.
By string.
By character.
By character-set delimiters.
In normal and reverse order.
All SIMD-accelerated.
1
2
3
for
(
auto
line
:
haystack
.
split
(
"
\r\n
"
))
for
(
auto
word
:
line
.
split
(
char_set
(
" \w
\t
.,;:!?"
)))
std
::
cout
<<
word
<<
std
::
endl
;
Here is a list:
haystack.[r]find_all(needle[, interleaving])
haystack.[r]find_all(char_set(""))
haystack.[r]split(needle)
haystack.[r]split(char_set(""))
For $N$ matches, the split functions will report $N + 1$ matches, potentially including empty strings.
Ranges provide
begin()
and
end()
forward-iterators and have a few convenience methods as well:
1
2
3
4
range
.
size
();
// -> std::size_t
range
.
empty
();
// -> bool
range
.
template
to
<
std
::
set
<
std
::
sting
>>
();
range
.
template
to
<
std
::
vector
<
std
::
sting_view
>>
();
A special case of
split
is
partition
.
It’s one of the most neglected functions in Python strings.
StringZilla brings them to C++, returning a simple
struct
, that can be unpacked with structured bindings.
1
2
3
4
5
auto
parts
=
haystack
.
partition
(
':'
);
// Matching a character
auto
[
before
,
match
,
after
]
=
haystack
.
partition
(
':'
);
// Structure unpacking
auto
[
before
,
match
,
after
]
=
haystack
.
partition
(
char_set
(
":;"
));
// Character-set argument
auto
[
before
,
match
,
after
]
=
haystack
.
partition
(
" : "
);
// String argument
auto
[
before
,
match
,
after
]
=
haystack
.
rpartition
(
sz
::
whitespaces
);
// Split around the last whitespace
Bulk Replace
#
Another way to know that the functionality is missing in STL is its frequency on StackOverflow and presence in Boost.
Boost has a
replace_all
function, which is not in STL.
The
std::string::replace
is a very different beast.
It replaces one predefined string slice with the given input.
The Boost function returns all occurrences of a substring with another substring, combining bulk-search functionality with several
memmove
or
memcpy
calls.
StringZilla supports that out of the box.
1
2
3
4
sz
::
string
s
=
"hello!"
;
s
.
replace_all
(
"ello"
,
"alo"
);
// -> "halo!"
s
.
replace_all
(
sz
::
char_set
(
"lo"
),
"a"
);
// -> "haaa!"
s
.
erase_all
(
sz
::
char_set
(
"hnm"
));
// -> "aaa!"
Updates and Allocations
#
Memory allocators are broken in C++, the same as in most languages.
That’s not a big deal for most applications, but it is a problem in IoT and Big Data applications.
The
Unum
stack is designed for the latter.
In Big Data, efficient software would always work in a memory-starved environment.
Even if you have 2 TB of RAM on a CPU socket, you will reach a point where 100% is used, you can’t allocate more, but you also can’t
terminate
.
The fact that most containers in STL raise exceptions when memory allocations fail is an issue.
That’s why StringZilla provides “try” versions of all allocation functions and explicitly marks all public interfaces with
noexcept
and
noexcept(false)
.
1
2
3
4
sz
::
string
s
=
"hello!"
;
s
.
try_erase
(
3
,
-
1
);
// update to "he!", return 2 for the number of removed bytes.
s
.
try_insert
(
2
,
"he"
);
// update to "hehe!" and return `true`.
s
.
try_replace
(
-
3
,
-
1
,
"llo"
);
// back to "hello!" on success, return `false` otherwise.
This might be a niche use case.
A more common one is concatenating multiple strings together.
The STL provides
std::string::operator+
and
std::string::append
, but those are inefficient if many invocations are performed.
1
2
std
::
string
name
,
domain
,
tld
;
auto
email
=
name
+
"@"
+
domain
+
"."
+
tld
;
// 4 allocations
The efficient approach would be pre-allocating the memory and copying the strings into it.
1
2
3
std
::
string
email
;
email
.
reserve
(
name
.
size
()
+
domain
.
size
()
+
tld
.
size
()
+
2
);
email
.
append
(
name
),
email
.
append
(
"@"
),
email
.
append
(
domain
),
email
.
append
(
"."
),
email
.
append
(
tld
);
That’s mouthful and error-prone.
StringZilla provides a more convenient
concatenate
function, which takes variadic arguments.
It also overrides the
operator|
to concatenate strings lazily without any allocations.
1
2
3
auto
email
=
sz
::
concatenate
(
name
,
"@"
,
domain
,
"."
,
tld
);
// 0 allocations
auto
email
=
name
|
"@"
|
domain
|
"."
|
tld
;
// 0 allocations
sz
::
string
email
=
name
|
"@"
|
domain
|
"."
|
tld
;
// 1 allocations
Generating Random Strings
#
Software developers often need to generate random strings for testing purposes.
The STL provides
std::generate
and
std::random_device
, that can be used with StringZilla.
1
2
3
4
5
6
7
8
sz
::
string
random_string
(
std
::
size_t
length
,
std
::
string_view
alphabet
)
{
sz
::
string
result
(
length
,
'\0'
);
static
std
::
random_device
seed_source
;
// Too expensive to construct every time
std
::
mt19937
generator
(
seed_source
());
std
::
uniform_int_distribution
<
std
::
size_t
>
distribution
(
1
,
alphabet
.
size
());
std
::
generate
(
result
.
begin
(),
result
.
end
(),
[
&
]()
{
return
alphabet
[
distribution
(
generator
)];
});
return
result
;
}
Mouthful and slow.
StringZilla provides a C native method -
sz_generate
and a convenient C++ wrapper -
sz::generate
.
Similar to Python it also defines the commonly used character sets.
It uses precomputed multiplication and shift tables to avoid module and division operations.
Those are used to sample from the given alphabet fairly and are slow on most CPU architectures.
1
2
3
4
5
6
7
8
auto
protein
=
sz
::
string
::
random
(
300
,
"ARNDCQEGHILKMFPSTWYV"
);
// static method
auto
dna
=
sz
::
basic_string
<
custom_allocator
>::
random
(
3
_000_000_000
,
"ACGT"
);
dna
.
randomize
(
"ACGT"
);
// `noexcept` pre-allocated version
dna
.
randomize
(
&
std
::
rand
,
"ACGT"
);
// pass any generator, like `std::mt19937`
char
uuid
[
36
];
sz
::
randomize
(
sz
::
string_span
(
uuid
,
36
),
"0123456789abcdef-"
);
// Overwrite any buffer
Performance and LibC
#
C++ is synonymous with performance.
The STL is not.
Every major shop in town has homegrown hash tables or prefers open-source alternatives to
std::unordered_map
and
std::unordered_set
.
The
std::string
is not an exception.
For some operations, it calls down to LibC, which is much more optimized in general but still doesn’t reach the hardware potential and doesn’t cover all the needs of the C++ class.
The
strstr
can only be used for substring search on NULL-terminated strings.
The
memmem
is better and can be used with
std::string_view
.
But there is a catch - there is no reverse search in LibC.
So, only one evaluation order is optimized.
Let’s see the numbers for exact search performance.
LibC
C++ Standard
Python
StringZilla
find the first occurrence of a random word from text, ≅ 5 bytes long
strstr
1
x86:
7.4
·
arm:
2.0
GB/s
.find
x86:
2.9
·
arm:
1.6
GB/s
.find
x86:
1.1
·
arm:
0.6
GB/s
sz_find
x86:
10.6
·
arm:
7.1
GB/s
find the last occurrence of a random word from text, ≅ 5 bytes long
❌
.rfind
x86:
0.5
·
arm:
0.4
GB/s
.rfind
x86:
0.9
·
arm:
0.5
GB/s
sz_rfind
x86:
10.8
·
arm:
6.7
GB/s
find the first occurrence of any of 6 whitespaces
2
strcspn
1
x86:
0.74
·
arm:
0.29
GB/s
.find_first_of
x86:
0.25
·
arm:
0.23
GB/s
re.finditer
x86:
0.06
·
arm:
0.02
GB/s
sz_find_charset
x86:
0.43
·
arm:
0.23
GB/s
find the last occurrence of any of 6 whitespaces
2
❌
.find_last_of
x86:
0.25
·
arm:
0.25
GB/s
❌
sz_rfind_charset
x86:
0.43
·
arm:
0.23
GB/s
Most benchmarks were conducted on a 1 GB English text corpus, with an average word length of 5 characters.
The code was compiled with GCC 12, using
glibc
v2.35.
The benchmarks performed on Arm-based Graviton3 AWS
c7g
instances and
r7iz
Intel Sapphire Rapids.
Most modern Arm-based 64-bit CPUs will have similar relative speedups.
Variance withing x86 CPUs will be larger.
¹ Unlike other libraries, LibC requires strings to be NULL-terminated.
² Six whitespace characters in the ASCII set are:
\t\n\v\f\r
.
Python’s and other standard libraries have specialized functions for those.
Summarizing, StringZilla is…:
3.5x faster than LibC for substring search
.
4.4x faster than STL for substring search
.
16.8x faster than STL for reverse order substring search
.
You can read more about the SIMD tricks in the
preceding articles
.
Conclusion
#
The library has a lot of “work in progress” functionality that goes far beyond the “standard needs”.
It packs Levenshtein edit distances, Needleman-Wunsch alignment scores for Bioinformatics, Rabin fingerprints for fuzzy matching, and fast Radix-based sorting.
As it matures, it might be worth suggesting as a new baseline implementation for the standard library of C++ and the strings in other programming languages.
Until then, it’s an easy-to-install tool for performance-sensitive applications.
Give it a chance and let me know if there is some functionality you would like to see in the next release 🤗
