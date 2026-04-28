---
title: "negative build dependencies"
url: "https://jyn.dev/negative-build-dependencies/"
fetched_at: 2026-04-28T07:02:50.493604+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# negative build dependencies

Source: https://jyn.dev/negative-build-dependencies/

This post is part 2/4 of
a series about build systems
.
The next post is
I want a better action graph serialization
.
This post is about a limitation of the dependencies you can express in a build file.
It uses Ninja just because it's simple and I'm very familiar with it, but the problem exists in most build systems.
Say you have a C project with two different include paths:
dependency/include
and
src
:
.
├── build.ninja
├── dependency
│   └── include
│       └── interface.h
└── src
└── main.c
and the following build.ninja:
rule cc
command = cc -I dependency/include -I src $in -o $out
build src/main: cc src/main.c | dependency/include/interface.h
and some small implementations, just so we can see that it actually works:
#include
<
stdio.h
>
#include
"
interface.h
"
int
main
(
void
)
{
printf
(
"
%d
\n
"
,
interface_version
)
;
}
const
static
short
interface_version
=
1
;
This works ok on our first build, and when
dependency/include/interface.h
changes:
$ ninja
[1/1] cc -I dependency/include -I src src/main.c -o src/main
But say now that we add our own
src/interface.h
file:
$
cat
src/interface.h
const static char *version = "1.0";
$
ninja
ninja: no work to do.
Now we have a problem. If we remove our build artifacts, ninja
does
rerun, and shows us what that problem is:
[1/1] cc -I dependency/include -I src src/main.c -o src/main
FAILED: [code=1] src/main
cc -I dependency/include -I src src/main.c -o src/main
src/main.c: In function ‘main’:
src/main.c:5:24: error: ‘interface_version’ undeclared (first use in this function)
5 |         printf("%d\n", interface_version);
|                        ^~~~~~~~~~~~~~~~~
src/main.c:5:24: note: each undeclared identifier is reported only once for each function it appears in
ninja: build stopped: subcommand failed.
We switched out what
interface.h
resolved to, but ninja didn't know about the changed dependency.
What we want is a way to tell it to rebuild if the file
src/interface.h
is created. To my knowledge, ninja has no way of expressing this kind of negative dependency edge.
Another way to avoid needing negative dependencies is to simply have a
hermetic build
, so that our
cc src/main.c | dependency/interface.h
rule never even makes the
src/interface.h
file available to the command. That works, but puts us firmly out of Ninja's design space; hermetic builds come with severe tradeoffs.
Yet another idea is to introduce an early-cutoff point:
For each
.c
file, run
cc -M
to get a list of include files. Save that to disk.
Whenever a directory is changed, rerun
cc -M
. If our list has changed, rerun a full build for that file.
This has the problem that it's
O(n
3
)
: For each file, for each include, for each directory in the search path, the preprocessor will try to
stat
that file to see whether it exists.
One possible workaround is to calculate the list of include files
in the build system
:
Look at the order of the search paths, list each path recursively, ignore filenames that are overridden by an include earlier in the search path.
Save that to disk.
Next time a directory is modified, check if the list of include files has changed. If so, only then rerun
cc -M
for all files.
This requires the build system to have some quite deep knowledge of how the language works, but I do think it would work today without changes to Ninja.
Thanks to
Jade Lovelace
for this suggestion.
Thanks to David Chisnall and Ben Boeckel (
@mathstuf
) for making me aware of this issue.
