---
title: "Simdutf Can Now Be Used Without libc++ or libc++abi"
url: "https://mitchellh.com/writing/simdutf-no-libcxx"
fetched_at: 2026-04-30T07:01:53.345531+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Simdutf Can Now Be Used Without libc++ or libc++abi

Source: https://mitchellh.com/writing/simdutf-no-libcxx

As of
this PR
,
simdutf
can be used without libc++ or libc++abi
1
.
Simdutf was the final remaining libc++ dependency in
libghostty-vt
2
.
After
updating Ghostty to use this new simdutf build
,
we were able to remove libc++ and libc++abi completely from our dependencies.
The Benefits of Not Depending on libc++
Not depending on libc++ makes a library more portable (embedded, WebAssembly,
freestanding environments), simplifies cross-compilation (no target-specific
C++ standard library needed), reduces binary size, and can simplify
static linking.
As a general purpose, low-level library, simdutf should be as portable and
flexible as possible. If a downstream consumer can easily use libc++,
great! But if they can't, they shouldn't be blocked from using simdutf
since it fundamentally doesn't need it.
libc++ vs libc++abi
There are two parts to extricating a program from libc++.
First,
libc++
is the C++ standard library, which provides things like
std::vector
,
std::string
, etc. If you import
<vector>
or even the libc
C++ fallbacks like
<cstring>
, you're depending on libc++.
The sneakier part is
libc++abi
, which provides the C++ ABI, including
things like exception handling, virtual function tables, RTTI, etc.
If you use any C++ features that require these, you're depending on libc++abi,
even if you don't import any C++ standard library headers
at all
.
For example, the minimal C++ program below depends on libc++abi
because it uses function-local static variables, which require thread-safe
initialization that is part of the C++ ABI:
struct
Implementation
{
int
version
;
};
const
Implementation
&
get_impl
()
{
static
const
Implementation impl
{
1
};
return
impl
;
}
int
main
()
{
return
get_impl
().
version
;
}
Extricating simdutf from libc++
Let's talk about
libc++
first (not the ABI).
simdutf is a C++ library that makes heavy use of the latest and greatest C++ features and though
I don't know him personally,
Daniel Lemire
seems
to really love utilizing C++ features to their fullest extent. So, simdutf is
very much a C++ project.
For there to be any chance that my changes would be accepted, I had to make
sure that the project could continue to use C++ features without it
being a headache.
STL Usage
The approach I decided to take was to introduce a
stl_compat.h
header
that centralizes all of the C++ standard library types. In
normal libc++ mode, everything in
stl_compat.h
is a simple include or
minimal alias to the corresponding C++ standard library type with no runtime
overhead.
In
NO_LIBCXX
mode,
stl_compat.h
provides its own implementations of the
C++ types that simdutf uses, but only just enough for them to be compatible
with what simdutf needs. For example,
stl_compat.h
provides its own
implementation of
std::pair
.
As a result, the changes required end up mostly looking like this
throughout the diff:
-
std::pair<const char *, char32_t *>
+
internal::pair<const char *, char32_t *>
arm_convert_latin1_to_utf32(const char *buf, size_t len,
char32_t *utf32_output) {
ABI Compatibility
My goal was to retain as much ABI compatibility as possible.
Some of the
public ABI
expose C++ types such as
std::string
, so in those scenarios, ABI
had to be broken. Otherwise, it is fully retained.
Given
SIMDUTF_NO_LIBCXX
is a new feature that applies changes
to the compilation unit, I felt that it was acceptable to break ABI
only when this flag is present
. In the existing case where the
NO_LIBCXX
flag is not present, the ABI is fully retained and simdutf can be
updated without breaking ABI for existing users.
I was pleasantly surprised to find that the ABI breakage was very minimal,
and only applied to a handful of diagnostic functions (e.g. to get
the name of the active implementation) and helpers to work with other
C++ types (e.g. text encoding
std::string
). Since by definition someone
using
SIMDUTF_NO_LIBCXX
is not interested in libc++, these ABI
breakages felt like a feature rather than a bug.
Extricating simdutf from libc++abi
This task was significantly more complex.
The main problem was that
libc++abi
dependencies don't usually show up as
obvious source-level includes. They show up because the compiler quietly emits
calls into the C++ ABI runtime for ordinary-looking language features.
To detect these, I had to write a script that decompiles the object files
and looks for symbols such as
__cxa_guard_acquire
.
The biggest offender in simdutf was the runtime dispatch layer. The original
code relied heavily on function-local static variables. In C++, those locals
are guarded by thread-safe initialization helpers such as
__cxa_guard_acquire
and
__cxa_guard_release
, which are provided by the C++ ABI runtime. So even
though the code didn't mention libc++abi anywhere, the compiled object still depended on it.
The fix for this is to use translation-unit static variables instead of
function-local statics in
NO_LIBCXX
mode.
#
if
SIMDUTF_IMPLEMENTATION_ICELAKE
#
ifdef
SIMDUTF_NO_LIBCXX
static
const
icelake
::
implementation icelake_singleton
{};
#
endif
static
const
icelake
::
implementation
*
get_icelake_singleton
()
{
#
ifdef
SIMDUTF_NO_LIBCXX
return
&
icelake_singleton
;
#
else
static
const
icelake
::
implementation icelake_singleton
{};
return
&
icelake_singleton
;
#
endif
}
#
endif
Next, simdutf models each backend as a subclass of an abstract
implementation
interface. That design can stay, but abstract-class vtables still reference
__cxa_pure_virtual
for impossible-to-call pure virtual entries.
In
SIMDUTF_NO_LIBCXX
mode I chose to provide a tiny local shim
and ensure the runtime never actually reaches it. I marked this as weak
so that the symbol can be overridden by the C++ ABI if it is present.
#
ifdef
SIMDUTF_NO_LIBCXX
// The abstract implementation vtable still carries pure-virtual slots even
// though correct dispatch never reaches them in this build mode. Provide the
// narrowest possible ABI shim so stricter no-libcxx objects do not require
// libc++abi just for this unreachable hook. Keep it weak so a toolchain's real
// libc++abi definition wins if one is linked in anyway.
extern
"
C
"
SIMDUTF_WEAK
[[
noreturn
]]
void
__cxa_pure_virtual
()
noexcept
{
__builtin_trap
();
}
#
endif
Finally, I wrote a script to audit the build with
-fno-exceptions
and
-fno-rtti
and check that no symbols such as
__cxa_guard_*
,
__gxx_personality
,
__cxa_throw
,
typeinfo
, or
__dynamic_cast
ever show
up. This was added to the simdutf CI to ensure that we never accidentally
reintroduce libc++abi dependencies in the future for
NO_LIBCXX
builds.
Validation
Internal
simdutf is a correctness and performance critical library, so I had to be
sure my changes didn't impact either of those. I modified the pre-existing
test and benchmark suites to run in both
NO_LIBCXX
and normal modes
and ensured that all tests passed and benchmarks were unaffected.
The important part about this is that I committed the changes necessary
to ensure that the
NO_LIBCXX
mode is compatible with the existing
test and benchmark suites. This means that future changes to simdutf
can continue to validate both.
External: Ghostty
Next, I updated Ghostty to use the new simdutf from my fork, updated
our builds to use
SIMDUTF_NO_LIBCXX
, and added our own suite of tests
to verify our artifacts have no dependencies on libc++ or libc++abi.
Ghostty has a robust set of tests that verify our UTF-8 decoding behavior
(especially invalid inputs). And Ghostty has a built-in benchmark suite
that tests our UTF-8 throughput in a variety of scenarios. I ran all the
Ghostty tests and benchmarks and verified that they all passed and that our
UTF-8 performance was unaffected, as expected.
Pull Request
Getting something working and getting something merged are two different things.
I know too well as a maintainer myself the disparity between "this works"
and "this can be merged." I know the challenges of verifying someone's work
and being confident in maintaining it going forward. I know the challenge of
opening a large PR and not having clarity of why it is being opened.
And I know the burden of recent AI slop.
So I put in the effort I would
want from an all-star contributor and tried to be that person for the
simdutf maintainers.
First, I reviewed the entire diff (yes, all ~3,000 lines of it). Then I
reviewed it again. I re-read the entire diff by hand three or four times.
I made multiple changes based on things I probably would've commented
on myself, even if functionally it was fine.
Next, I hand-wrote a detailed PR description that explains the motivation,
the approach, the limitations, and the validation. I wanted to make sure that
the maintainers were aware of the details but also how much thought I put
into the details.
Finally, I disclosed that I did use AI to assist me in writing the code. But
I made it clear that I manually reviewed everything, I didn't use AI in writing
any of the PR description or comments, and that I was capable and comfortable
as a human to defend and modify any proposed changes.
Ironically, the full diff took me about 2 hours to put together, but the
extra validation work and PR preparation took me about 3 hours. I spent more
time on the human boundary than the code itself, as we should out of respect
for the effort maintainers put into their projects.
Final Status
The
simdutf PR
is still
under review. Initial feedback is positive, and I'm open to any and all
changes requested of me. There's a possibility that the maintainers will not
want to merge it, and that's okay, too.
If you want to use simdutf without libc++ or libc++abi, you can
use my fork
in the
meantime. The same instructions for producing an amalgamated single-file plus
header build apply. When building the C++ and including the header, just
make sure to define
SIMDUTF_NO_LIBCXX
to get the no-libc++ version of
the library.
The
Ghostty PR
is
now merged. As such,
libghostty-vt
no longer depends on libc++ or libc++abi
for SIMD builds.
