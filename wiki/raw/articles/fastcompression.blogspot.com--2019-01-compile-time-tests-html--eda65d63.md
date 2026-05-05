---
title: "RealTime Data Compression"
url: "http://fastcompression.blogspot.com/2019/01/compile-time-tests.html"
fetched_at: 2026-05-05T07:00:58.183061+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# RealTime Data Compression

Source: http://fastcompression.blogspot.com/2019/01/compile-time-tests.html

Compile-time tests
A function generally operates on states and parameters. The function’s result is deemed valid if its inputs respect a number of (hopefully documented) conditions. It can be as simple as saying that a size should be positive, and a state should be already allocated.
The usual way to check if conditions are met is to
assert()
them, right at the beginning of the function. The
assert()
adds a runtime check, which is typically active during tests. The hope if that, if tests are thorough enough, any scenario which can violate the conditions will be found during tests, and fixed.
As one can already guess, this method is imperfect. Don’t get me wrong: adding
assert()
is
way way better
than not adding them, but the whole precinct is to hope that tests will be good enough to find the bad paths leading to a condition violation, and one can never be sure that all bad paths were uncovered.
In some cases, it’s possible to transfer a check at compile time instead.
It only works for a subset of what can be checked. But whatever is validated at compilation stage carries much stronger guarantees : it’s like a mini-proof that always holds, for whatever state the program is in.
As a consequence, it eliminates the need for a runtime check, which saves cpu and binary size.
More importantly, it removes the need of a “failure code path”, requiring the caller to test and consider carefully what must be done when an incorrect condition happens. This leads to a corresponding simplification of the code, with massive maintenance benefits.
On top of that, since the condition can be checked immediately during compilation or parsing, it’s right in the short feedback loop of the programmer, allowing failures to be identified and fixed quickly.
This set of benefits is too strong to miss. As a general rule, whatever can be checked at compile time should be.
static assert
Invariant guarantees can be checked at compile time with a
static_assert()
. Compilation will stop, with an error, if the invariant condition is not satisfied. A successful compilation necessarily means that the condition is always respected (for the compilation target).
A typical usage is to ensure that the
int
type of target system is wide enough. Or that some constants respect a pre-defined order. Or, as suggested in an earlier article, that a shell type is necessarily large enough to host its target type.
It has all the big advantages mentioned previously : no trace in the generated binary, no runtime nor space cost, no reliance on runtime tests to ensure that the condition is respected.
C90 compatibility
static_assert()
is a special macro added in the
C11
standard. While most modern compilers are compatible with this version of the standard, if you plan on making your code portable on a wider set of compilers, it’s a good thing to consider an alternative which is compatible with older variants, such as
C90
.
Fortunately, it’s not that hard.
static_assert()
started its life as a “compiler trick”, and many of them can be found over Internet. The basic idea is to transform a condition into an invalid construction, so that the compiler
must
issue an error at the position of the
static_assert()
. Typical tricks include :
defining an
enum
value as a constant divided by
0
defining a table which size is negative
For example :
#
define
STATIC_ASSERT(COND,MSG) typedef char static_assert_##MSG[(COND)?1:-1]
One can find multiple versions, with different limitations. The macro above has the following ones :
cannot be expressed in a block after the first statement for
C90
compatibility (declarations before statements)
require different error messages to distinguish multiple assertions
require the error message to be a single uninterrupted word, without double quotes, differing from
C11
version
The 1st restriction can be circumvented by putting brackets around
{ static_assert(); }
whenever needed.
The 2nd one can be improved by adding a
__LINE__
macro as part of the name, thus making it less probable for two definitions to use exactly the same name. The macro definition becomes more complex though.
The last restriction is more concerning: it’s a strong limitation, directly incompatible with
C11
.
That’s why I rather recommend
this more complete version by Joseph Quinsey
, which makes it possible to invoke the macro the same way as the
C11
version, allowing to switch easily from one to another. The declaration / statement limitation for
C90
is still present, but as mentioned, easily mitigated.
Limitations
A huge limitation is that static asserts can only reason about constants, which values are known at compile time.
Constants, in the
C
dialect, regroup a very restricted set :
Literals value, e.g.
222
.
Macros which result in literals value, e.g.
#define value 18
enum
values
sizeof()
results
Mathematical operations over constants which can be solved at compile time, e.g.
4+1
or even
((4+3) << 2) / 18
.
As a counter-example, one might believe that
const int i = 1;
is a constant, as implied by the qualifier
const
. But it’s a misnomer : it does not define a constant, merely a “read-only” (immutable) value.
Therefore it’s
not possible to
static_assert()
conditions on variables
, not even
const
ones. It’s also not possible to
express conditions using functions
, not even pure ones (only macro replacements are valid).
This obviously strongly restrains the set of conditions that can be expressed with a
static_assert()
.
Nonetheless, every time
static_assert()
is a valid option, it’s recommended to use it. It’s a very cheap, efficient zero-cost abstraction which guarantees an invariant, contributing to a safer code generation.
Arbitrary conditions validated at compile time
Checking an arbitrary condition at compile time? like a runtime
assert()
? That sounds preposterous.
Yet, that’s exactly what we are going to see in this paragraph.
The question asked changes in a subtle way : it’s no longer “prove that the condition holds given current value(s) in memory”, but rather “prove that the condition can never be false”, which is a much stronger statement.
The benefits are similar to
static_assert()
: as the condition is guaranteed to be met, no need to check it at run time, hence no runtime cost, no need for a failure path, no reliance on tests to detect bad cases, etc.
Enforcing such a strong property may seem a bit overwhelming. However, that’s exactly what is
already required
by the standard, for any operation featuring
undefined behavior
as a consequence of violation of their
narrow contract
.
The real problem is that the full responsibility of knowing and respecting the contract is transferred onto the programmer, which receives, by default, no compile-time signal to warn when these conditions are broken.
Compile-time condition validation reverse this logic, and ensure that a condition is
always met
if it passes compilation. This is a big change, with corresponding safety benefits.
This method is not suitable for situations determined by some unpredictable runtime event. For example, it’s not possible to guarantee that a certain file
will
exist at runtime, so trying to open a file always requires a runtime check.
But there are a ton of conditions that the programmer expect to be always true, and which violation necessarily constitutes a programming error. These are our targets.
Example
Let’s give a simple example :
dereferencing a pointer requires that, as a bare minimum, the pointer is not
NULL
. It’s not a loose statement, like “this pointer is probably not
NULL
in general”, it must be 100% true, otherwise,
undefined behavior
is invoked.
How to ensure this property then ?
Simple : test if the pointer is
NULL
, and if it is, do not dereference it, and branch elsewhere.
Passing the branch test guarantees the pointer is now non-
NULL
.
This example is trivial, yet very applicable.
It’s extremely common to forget such a test, since there’s no warning for the programmer. A
NULL
pointer can happen due to exceptional conditions which can be difficult to trigger during tests, such as a rare
malloc()
failure for example.
And that’s just a beginning : most functions and operations feature a set of conditions to be respected for their behavior and result to be correct. Want to divide ? better be by non-zero. Want to add signed values ? Well, be sure they don’t overflow. Let’s call
memcpy()
?  First, ensure memory segments are allocated and don’t overlap.
And on, and on, and on.
While it’s sometimes possible to
assert()
some of these conditions, it’s not great, because in absence of compilation warnings, contract violation can still happen at runtime. And while the
assert()
, if enabled, will avoid the situation to degenerate into
undefined behavior
, it still translates into an abrupt
abort()
, which is another form of vulnerability.
A better solution is to ensure that the condition always hold. This is where a compile-time guarantee comes in.
Solution
We want the compiler to emit a warning whenever a condition cannot be guaranteed to be true. Technically, this is almost like an
assert()
, though without a trace in the generated binary.
This outcome is already common : whenever an
assert()
can be proven to be always true, the compiler will remove it, through a fairly common optimization stage called Dead Code Elimination (DCE).
Therefore, the idea is to design an
assert()
that must be removed from final binary through DCE, and emits a warning if it does not.
Since no such instruction exists in the base language, we’ll have to rely on some compiler-specific extensions.
gcc
for example offers a
function attribute
which does exactly that :
warning ("message")
If the
warning
attribute is used on a function declaration and a call to such a function is not eliminated through dead code elimination or other optimizations, a warning that includes
"message"
is diagnosed. This is useful for compile-time checking.
This makes it possible to create this macro :
__attribute__
(
(
noinline
)
)
__attribute__
(
(
warning
(
"condition not guaranteed"
)
)
)
static
void
never_reach
(
void
)
{
abort
(
)
;
}
#
define
EXPECT(c) (void)((c) ? (void)0 : never_reach())
The resulting macro is called
EXPECT()
, for consistency with a recent C++20 proposal, called
attribute contract
, which suggests the notation
[[expects: expression]]
to achieve something similar (though not strictly identical, but that’s a later topic).
EXPECT()
is designed to be used the same way as
assert()
, the difference being it will trigger a warning at compile time whenever it cannot be optimized away, underlying that the condition can not be proven to be always true.
Limitations
It would be too easy if one could just start writing
EXPECT()
everywhere as an
assert()
replacement. Beyond the fact that it can only be used to test programming invariants, there are additional limitations.
First, this version of
EXPECT()
macro only works well on
gcc
. I have not found a good enough equivalent for other compilers, though it can be emulated using other tricks, such as an
incorrect assembler statement
, or linking to some non existing function, both of which feature significant limitations : do not display the line at which condition is broken, or do not work when it’s not a program with a
main()
function.
Second, checking the condition is tied to compiler’s capability to combine
Value Range Analysis
with
Dead Code Elimination
. That means the compiler must use at least a bit of optimization. These optimizations are not too intense, so
-O1
is generally enough. Higher levels can make a difference if they increase the amount of inlining (see below).
However,
-O0
definitely does not cut it, and all
EXPECT()
will fail. Therefore,
EXPECT()
must be disabled when compiling with
-O0
.
-O0
can be used for fast debug builds for example, so it cannot be ruled out. This issue makes it impossible to keep
EXPECT()
always active by default, so its activation must be tied to some explicit build macro.
Third, Value Range Analysis is limited, and can only track function-local changes. It cannot cross function boundaries.
There is a substantial exception to this last rule for
inline
functions : for these cases, since function body will be included into the caller’s body,
EXPECT()
conditions will be applied to both sides of the interface, doing a great job at checking conditions and inheriting VRA outcome for optimization.
inline
functions are likely the best place to start introducing
EXPECT()
into an existing code base.
Function pre-conditions
When a function is not
inline
, the situation becomes more complex, and
EXPECT()
must be used differently compared to
assert()
.
For example, a typical way to check that input conditions are respected is to
assert()
them at the beginning of the function. This wouldn’t work with
EXPECT()
.
Since VRA does not cross function boundaries,
EXPECT()
will not know that the function is called with bad parameters. Actually, it will also not know that the function is called with good parameters. With no ability to make any assumption on function parameters,
EXPECT()
will just always fail.
int
division
(
int
v
)
{
EXPECT
(
v
!=
0
)
;
return
1
/
v
;
}
int
lets_call_division_zero
(
void
)
{
return
division
(
0
)
;
}
To be useful,
EXPECT()
must be declared
on the caller side
, where it can properly check input conditions.
Yet, having to spell input conditions on the caller side at every invocation is cumbersome. Worse, it’s too difficult to maintain: if conditions change, all invocations must be updated !
A better solution is to spell all conditions in a single place, and encapsulate them as  part of the invocation.
int
division
(
int
v
)
{
return
1
/
v
;
}
#
define
division(v) ( EXPECT(v!=0), division(v) )
int
lets_call_division_zero
(
void
)
{
return
division
(
0
)
;
}
int
lets_call_division_by_something
(
int
divisor
)
{
return
division
(
divisor
)
;
}
int
lets_divide_and_pay_attention_now
(
int
divisor
)
{
if
(
divisor
==
0
)
return
0
;
return
division
(
divisor
)
;
}
Here are some more
example usages
. Note how
EXPECT()
are combined with a function signature into a macro, so that compile time checks get triggered every time the function is called.
Limitations
This construction solves the issue on the caller side, which is the most important one.
You may note that the macro features a typical flaw : its argument
v
is present twice. It means that, if
v
is actually a function, it’s going to be invoked twice. In some cases, like
rand()
, both invocations may even produce different results.
However, at this stage, it’s impossible to successfully invoke the macro using a function as argument to begin with.
That’s because then function’s return value has no any guarantee attached beyond its type.
So, if the function is
int f()
, its return value could be any value, from
INT_MIN
to
INT_MAX
.
As a consequence, no function’s return value can ever comply with any condition. It will necessarily generate a warning.
The encapsulating macro can only check conditions on variables, and it will only accept variables which are
guaranteed
to respect the conditions. If a single one
may
break any condition, a warning is issued.
However, pre-conditions remain unknown to the function body itself. This is an issue, because without it, it is necessary to re-express the conditions within the function body, which is an unwelcome burden.
A quick work-around is to express these guarantees inside the function body using
assert()
. This is, by the way, what should have been done anyway.
An associated downside is that ensuring that
EXPECT()
conditions are respected using
assert()
presumes that
assert()
are present and active in source code, to guide the Value Range Analysis. If
assert()
are disabled, their corresponding
EXPECT()
will fail.
This suggests that
EXPECT()
can only be checked in debug builds, and with optimization enabled (
-O1
).
With all these
assert()
back, it seems like these compile-time checks are purely redundant, hence almost useless.
Not quite. It’s true that so far, it has not reduced the amount of
assert()
present in the code, but the compiler now actively checks expressed pre-conditions, and mandates the presence of
assert()
for every condition that the local code does not explicitly rule out. This is still a step up : risks of contract violation are now underlined early, and it’s no longer possible to “forget” an
assert()
. As a side effect, tests will also catch condition violations sooner, leading to more focused and shorter debug sessions. This is still a notable improvement.
It nonetheless feels kind of incomplete. One missing aspect is an ability to transfer pre-conditions from the calling site to the function body, so that they can be re-used to satisfy a chain of pre-conditions.
This capability requires another complementary tool. We’ll see that in the next blog post.
