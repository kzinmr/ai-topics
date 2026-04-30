---
title: "Don't Trip[wire] Yourself: Testing Error Recovery in Zig"
url: "https://mitchellh.com/writing/tripwire"
fetched_at: 2026-04-30T07:01:53.505814+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Don't Trip[wire] Yourself: Testing Error Recovery in Zig

Source: https://mitchellh.com/writing/tripwire

I've written a library called
Tripwire
1
for injecting failures into Zig programs for the express purpose of
testing error handling paths. Outside of unit tests, it is
completely
optimized away
and has zero runtime cost (space or time).
Zig has a language feature
errdefer
for running code on block exit only when an error is being returned.
The idea is simple: if an error occurs, you need to "undo" your partial
effects so that when the function returns an error, the world state
can be in some well-defined state.
Ironically, error cleanup is one of the most error-prone parts of Zig
programs and is a consistent source of resource leaks and memory corruption.
This is easily understood: error codepaths are typically much less frequently
executed and triggering them in tests can be difficult. As a result,
they usually are only cognitively reviewed once or twice during development,
and never truly exercised until a user hits them in production.
Errors in Zig
This section covers some background on how errors work in general in Zig. If you're familiar with
Zig error handling, feel free to skip this section.
All functions in Zig can return
error values
.
An error value acts a bit like an enum and looks like this:
error.OutOfMemory
.
Error values are collected into name sets known as
error sets
.
And functions can return either an error or a success value using
something called an
error union
.
You can wrap an error union (usually a function call result) with
try
to unwrap the value or return the error.
And, finally, the key point for this post, you can put
errdefer
anywhere and when an error is returned (either directly or via
try
), then
all prior
errdefer
statements in the current scope will be executed
in reverse order.
All-in-all, it looks a bit like this in a toy example:
fn
create
(alloc
:
Allocator)
!*
Widget {
const
self
=
try
alloc
.
create
(Widget)
;
errdefer
alloc
.
destroy
(self)
;
self
.
*
=
try
.
init
(alloc)
;
errdefer
self
.
deinit
()
;
const
file
=
try
std
.
fs
.
cwd
()
.
openFile
(
"config.txt"
,
.
{})
;
// etc...
return
self
;
}
In this example, you can see the basic path:
After allocating room for
Widget
, if we see an error we should deallocate.
After initializing the
Widget
, if we see an error we should deinitialize it.
etc.
This is a quintessential Zig pattern, and you will see it all over the
Zig standard library and in most Zig programs. This is an easy case where
errdefer
is
obviously correct
even without tests.
But the real world gets messy fast.
2
Why So Fragile?
It is also useful background to understand why it is so difficult to
test error handling codepaths in Zig.
Zig provides some great utilities for program correctness. First,
it has a number of
runtime safety checks
covering things from index of bounds to null dereferencing and so on.
Next, Zig's
parameterized allocators
make it easier to test out of memory scenarios, constrained memory
environments, and so on. Finally, Zig has a builtin
test framework
and encourages writing tests culturally.
But, it has no mechanism to trigger errors to test
errdefer
. For
memory allocation errors, you can use specialized allocators like the
std.testing.failing_allocator
, but getting it exactly configured right
in complex code that does many allocations and whose allocations may be
conditional is tricky and fragile.
You always get
defer
testing for free if you unit test your code because
defers run unconditionally on block exit. But
errdefer
only runs
when errors occur, so if you can't trigger the error, you can't test
the corresponding
errdefer
!
And besides tooling, error handling code by its nature is more rarely
executed and the state of the world when an error occurs is often
more complex than the success path (since it is also may be dependent
on
where
the error occurred).
Tripwire
I ultimately grew tired of eyeballing error handling code and hoping
it was correct, or spending hours trying to write tests that create
a perfect-but-fragile scenario to trigger an exact error path. So,
I wrote
Tripwire
.
Tripwire is a small, single-file library
1
that lets you put named
points in your code where you can trigger errors during tests. Outside of
tests, it is written in such a way that it is completely optimized away
(takes no memory and emits no machine code).
Conceptually it works like this:
How tripwire injects failures
Click to trigger:
.alloc_buffer
.open_file
fn init(alloc: Allocator) !*Self {
try tw.check(.alloc_buffer);
const buf = try alloc.alloc(u8, 1024);
errdefer alloc.free(buf);
try tw.check(.open_file);
← error injected!
const file = try openFile("config");
errdefer file.close();
return self;
}
Triggering .open_file:
Buffer was allocated, so
errdefer alloc.free(buf)
must run. If it's missing or wrong, the test fails with a memory leak!
With code, it looks like this:
const
tripwire
=
@import
(
"tripwire.zig"
)
;
// Define a tripwire module with named failure points. The second
// argument is the function itself to get its error set.
const
init_tw
=
tripwire
.
module
(
enum
{
alloc_buffer
,
open_file
,
}
,
init)
;
fn
init
(alloc
:
Allocator)
!*
Self {
// Check the tripwire before the fallible operation.
// In tests, this can be configured to return an error.
// In release builds, this compiles to nothing.
try
init_tw
.
check
(
.
alloc_buffer)
;
const
buf
=
try
alloc
.
alloc
(
u8
,
1024
)
;
errdefer
alloc
.
free
(buf)
;
try
init_tw
.
check
(
.
open_file)
;
const
file
=
try
std
.
fs
.
cwd
()
.
openFile
(
"config.txt"
,
.
{})
;
errdefer
file
.
close
()
;
// ...
}
test
"init error on open_file"
{
// Configure the tripwire to fail at the open_file point.
try
init_tw
.
errorAlways
(
.
open_file
,
error
.
OutOfMemory)
;
// Call the function and expect the error.
try
std
.
testing
.
expectError
(
error
.
OutOfMemory
,
init
(std
.
testing
.
allocator))
;
// End the tripwire session and reset state.
// This also verifies the tripwire was actually hit.
try
init_tw
.
end
(
.
reset)
;
}
The key insight is that
std.testing.allocator
will fail the test if any
memory is leaked. So by triggering an error at
.open_file
, we force the
errdefer alloc.free(buf)
to run. If that
errdefer
was missing or wrong,
the test would fail with a memory leak. In more complex scenarios, you'd
add additional state testing in the unit test after the error is tripped.
Another common pattern I use is to iterate through all possible
failure points to get complete coverage:
test
"init handles all error points"
{
for
(std
.
meta
.
tags
(init_tw
.
FailPoint))
|
point
|
{
try
init_tw
.
errorAlways
(point
,
error
.
OutOfMemory)
;
try
std
.
testing
.
expectError
(
error
.
OutOfMemory
,
init
(std
.
testing
.
allocator))
;
try
init_tw
.
end
(
.
reset)
;
}
}
As I said before, in practice you probably need a bit more expectations
after the tripwire end to verify that your world state is sensible. But
even at a basic level, this makes it easy to ensure no runtime safety
checks or leaks are detected.
In addition to
errorAlways
, you can use
errorAfter
to only
trigger an error after a certain number of times that that failure
point has been reached. And
end
will verify that it was triggered.
This is useful to catch resource leakage or state corruption due to
poor loop cleanup.
Zero-Cost Outside of Tests
Outside of tests, Tripwire emits no machine code and uses no memory;
it is completely optimized away.
To do this, we use Zig's comptime to detect the test framework:
/// Whether our module is enabled or not.
pub
const
enabled
=
builtin
.
is_test
;
And use that to conditionally make our functions no-ops:
pub
fn
check
(point
:
FailPoint)
callconv
(
callingConvention
()) Error
!
void
{
if
(
comptime
!
enabled)
return
;
// actually do stuff
}
We also use comptime to set the calling convention so that the function
is inlined if we're not enabled:
/// Our calling convention is inline if our tripwire module is
/// NOT enabled, so that all calls to `check` are optimized away.
fn
callingConvention
() std
.
builtin
.
CallingConvention {
return
if
(
!
enabled)
.
@"inline"
else
.
auto
;
}
Some have told me this isn't necessary, but we've seen real compilations
produce machine code with full function call overhead to a function
with an empty body and only a
ret
. Inlining fixes this, until we
figure out what is causing that.
And finally, the Zig compiler only analyzes and emits code for declarations
that are actively referenced (or volatile). Since no code references this
state when Tripwire is disabled, none of our global state gets emitted
into the binary, either.
Bugs, Bugs
I integrated Tripwire into Ghostty in only a handful of places and
immediately uncovered
many bugs
.
In the initial PR I fixed ~6
errdefer
bugs. They've all never been
known to trigger in the real world but they are bugs nonetheless.
And most importantly, the bugs are now fixed paired with unit tests that
verified they exist! If I remove the fix, the tests fail!
I plan to continue to integrate Tripwire into more parts of the Ghostty
codebase and to ensure that I'm considering
errdefer
testing for any newly
written code by myself, maintainers, or contributors.
Please, copy the file if you find it useful and use it in your own
projects! Ghostty is MIT licensed and Tripwire is fully self-contained
in a single file. Use it!
