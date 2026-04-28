---
title: "Conditionally Disabling Code with Comptime in Zig"
url: "https://mitchellh.com/writing/zig-comptime-conditional-disable"
fetched_at: 2026-04-28T07:02:40.516944+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Conditionally Disabling Code with Comptime in Zig

Source: https://mitchellh.com/writing/zig-comptime-conditional-disable

Zig has a very powerful feature called
comptime
.
Comptime lets you run Zig code at compile time. This isn't a special macro
language or AST manipulation; it is just standard Zig code that runs at
compile time. The only real limitation is that comptime code can't have
side effects (no syscalls, no IO, etc.).
I admit that when I first started looking into Zig, I thought this was a
gimmick. "How much could I possibly want to
actually
do at comptime,
anyways?" I thought. Two years into using Zig for a
non-trivial project
,
comptime is used
all over
and is by far my favorite feature about Zig.
Comptime itself is a big subject. So instead of diving into everything about
comptime, I want to show you one particularly useful pattern: conditionally
disabling code with comptime.
Why Conditionally Disable Code?
Conditionally disabling code is a common pattern in software development.
Here are a few very common reasons you might want to conditionally disable
code:
Platform-specific code: you might have a function that has a different
implementation on macOS than it does on Linux.
Debugging code: you might have some code that is only useful for debugging
and you want to disable it in production builds.
Build configuration: you might have a feature that you want to omit or modify
based on build-time configuration.
In dynamic languages such as Python or JavaScript, you can usually use a basic
if
statement at runtime to choose the proper code path. Because dynamic
languages only evaluate code at runtime, this avoids hitting code paths that
may not work.
In compiled languages, however, you can't use an
if
statement to conditionally
disable code since the compiler must compile and link all code paths that
could possibly be taken at runtime.
Besides making it compile, omitting the code at compile time also has
the benefit of making your binary smaller and avoiding runtime conditionals
which may have a performance cost.
Non-Zig Approaches
Let's take a look at how other compiled languages approach this problem.
If you're not interested in this, feel free to skip to the next section
to see how we can use Zig's comptime to solve this problem.
C-based Languages
In C-based languages, you will often see the preprocessor used to conditionally
disable code. Here's an example:
#
define
FLAG
void
my_function
()
{
#
ifdef
FLAG
// This code will only be included if FLAG is defined.
#
else
// This code will only be included otherwise.
#
endif
}
This is effectively templating code at compile time. The preprocessor will
run first, transform the code (at the text level), and then the compiler
will compile the code. The first major con is that the preprocessor is
a separate language with its own syntax and rules.
The second major con is that the preprocessor is extremely limited.
C programmers usually rely on a capable build system to generate the
correct preprocessor definitions. The build system usually uses its own
language to generate these definitions.
Go
In Go, compile-time code omission is done per-file with build tags.
Here's an example:
// +build mytag
func
myFunction
()
{
// This code will only be included if the file is built with the "mytag"
// build tag.
}
For platform-specific code, you can also use filename suffixes. This isn't
a Go tutorial so I won't go into detail, but the point is that conditional
compilation is done at the file level.
There are various subjective opinions on this approach. I think an
objectively bad part of this approach is that you still have to use some
preprocessor language to choose whether a tag is included or not and this
is usually deferred to a build system, Makefile, etc.
Zig Comptime
Zig's comptime lets you conditionally disable code using Zig. Here's the
most simple example of platform-specific code:
const
builtin
=
@import
(
"builtin"
)
;
fn
myFunction
()
void
{
if
(
comptime
builtin
.
os
.
tag
==
.
macos) {
// This code will only be included if the target OS is macOS.
return
;
}
// This code will be included for all other operating systems.
}
The first thing to notice is the code is standard Zig. There is no
preprocessor language or special syntax. Second, notice the Zig compiler
is smart enough to know that since the
if
statement ends in an exit
condition, then it doesn't need to compile anything else if the condition
is trivially true. In this case, if the target OS is macOS, then the
compiler will only compile the first block.
A note on the
comptime
keyword:
The comptime keyword above is
unnecessary. Zig will automatically evaluate the condition at compile
time if all available information is known at compile time. Since
builtin
is all compile-time constant, the
comptime
keyword is redundant. I
included it to make the example more explicit.
Here is a more complex example from
an actual project I'm working on
:
if
((
comptime
adwaita
.
versionAtLeast
(
1
,
4
,
0
))
and
adwaita
.
enabled
(
&
config)
and
adwaita
.
versionAtLeast
(
1
,
4
,
0
)) {
// This code will only be included if we're building with
// libadwaita available and the version is at least 1.4.0
// at both build and runtime.
}
This shows the power of comptime being standard Zig. In this case,
we're mixing comptime and non-comptime conditions. The first condition
is comptime and the remainder are runtime conditions.
The first comptime condition checks that our build configuration
has enabled
libadwaita
and that the version we have
at build time
is at least 1.4.0. If this is false, then the Zig compiler knows that
the rest of the conditions can't possibly result in the block being
included, so it doesn't compile the rest of the block at all.
Importantly, this means I can use the
adwaita
library in the runtime
conditions as well as the code block and I won't get compiler errors
if the library isn't available or isn't the right version or if I reference
types that only exist in newer versions of the library.
Why the two
adwaita.versionAtLeast(1, 4, 0)
calls?
The first
one is a build-time check that we have libadwaita available and that
the version is at least 1.4.0. The second one is a runtime check that
the dynamically linked library is at least version 1.4.0. This makes
it possible to compile this code on a system with a newer version of the
library than the one it may run on, amongst other permutations.
To drive the point home, let's consider how we might have done this
in C. In C, we would have probably used a build system such as CMake that
creates a one-time program and attempts to compile it to determine if it
should define a preprocessor flag or not. Ugh. 🤮
Comptime Gotchas
There are some gotchas to be aware of when using comptime to conditionally
disable code. First, comptime doesn't cross function boundaries unless
the
comptime
keyword is used. For example, if we pulled the above conditional
out to a function, it wouldn't work:
fn
myFunction
()
void
{
if
(
hasFeature
()) {
// Feature-specific code.
}
else
{
// Default code.
}
}
fn
hasFeature
()
bool
{
return
false
;
}
In the above example, the compiler will build the code in both branches
of the conditional even though
hasFeature
is trivially false. To fix this
you can prepend
comptime
to the function call:
fn
myFunction
()
void
{
if
(
comptime
hasFeature
()) {
// Feature-specific code.
}
else
{
// Default code.
}
}
Unfortunately, this won't work if
hasFeature
mixes comptime and
non-comptime conditions. In that case, you'll need to inline the
function:
fn
myFunction
()
void
{
if
(
hasFeature
()) {
// Feature-specific code.
}
else
{
// Default code.
}
}
inline
fn
hasFeature
()
bool
{
return
(
comptime
comptimeCheck
())
and
runtimeCheck
()
;
}
This will now work as expected: the compiler will not include the
feature-specific code if the comptime check is false.
This subtle behavior is very easy to miss. Whenever I have comptime
checks like this I always add both branches to CI to ensure that
my program can build in both environments.
Comptime is Great
I love comptime. It's a feature that I didn't know I needed until I had it,
and one that I miss when I'm working in other languages. This blog post
showed only one specific use case for comptime, but if this was all comptime
was good for, it would still be a killer feature.
Conditional compilation with comptime is what allows me to write code that
is cross-platform while sharing the same files and a lot of the same code.
I don't need a complex build system or external tools to manage my
platform-specific code. I can just write Zig code and the compiler takes
care of the rest.
Again, there are so many other things you can do with comptime and
so many other powerful properties of comptime. For example, types in comptime
match the target system (so things like pointer sizes are correct). There's
so much more! I encourage you to check out the Zig documentation and
other blog posts to learn more, and give Zig a shot!
