---
title: "Nontrailing separators do not spark joy"
url: "https://buttondown.com/hillelwayne/archive/nontrailing-separators-do-not-spark-joy/"
fetched_at: 2026-06-11T07:00:58.797776+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# Nontrailing separators do not spark joy

Source: https://buttondown.com/hillelwayne/archive/nontrailing-separators-do-not-spark-joy/

This is valid JSON:
{
"a"
:
1
,
"b"
:
2
,
"c"
:
3
}
This is invalid JSON:
{
"a"
:
1
,
"b"
:
2
,
"c"
:
3
,
}
The difference is the last comma. The
JSON grammar
specifies that a comma can separate two members of an object but not postcede ("trail") a member. I think this was a design mistake. Say we want to add two new keys to the struct, one before the
"a"
member and one after the
"c"
member. Here's what it would look like if trailing commas were permitted:
{
+   "x": 0,
"a": 1,
"b": 2,
"c": 3,
+   "y": 4,
}
It's the exact same text transformation regardless of where we add the key. In the current model, we instead have this:
{
+   "x": 0,
"a": 1,
"b": 2,
-   "c": 3
+   "c": 3,
+   "y": 4
}
Those are different transformations! Similarly if you want to remove an element, you can't just delete the corresponding line
, you have to delete the line
and then
check that the last line doesn't have a trailing comma. Don't even get me started on all the special cases involved in swapping two lines.
JSON isn't the only language with this problem. Haskell writes record types like this:
-- from https://play.haskell.org/
data
Drone
=
Drone
{
xPos
::
Int
,
yPos
::
Int
,
zPos
::
Int
}
This "partial bullet point" style of putting separators at the beginning of rows makes it easier to change the last row but harder to change the first one.
TLA+ has this problem too:
\* both valid
VARIABLES a, b, c
vars == <<a, b, c>>

\* both invalid
VARIABLES a, b, c,
vars == <<a, b, c,>>
This one's annoying because 1) you're constantly adding new top-level variables while working on a spec and 2) the PlusCal DSL does
not
have this problem:
\* Totally fine!
(*--algorithm foo {
variables a; b; c;
The worst offenders, IMO, are logic languages like Prolog. Not only don't you have trailing separators, you have a
special terminating symbol
:
foo
(
A
,
B
,
C
)
:-
A
=
1
,
% comma
B
=
2
,
% comma
C
=
3.
% period!
I guess you can sort of think of it as funny-lookin' braces:
foo
(
A
,
B
,
C
)
:-
A
=
1
,
B
=
2
,
C
=
3
.
But this is not standard syntax and people will look at you weird if you try it. And you still don't get trailing separators.
Something better
Some languages allow trailing separators:
// go
valid
:=
map
[
string
]
int
{
"a"
:
1
,
"b"
:
2
,
"c"
:
3
,
}
# python
valid
=
{
"a"
:
1
,
"b"
:
2
,
"c"
:
3
,
}
But I think we can do one better than that. Python and Go commas can trail but not lead, meaning we can't go 100% bullet points:
# python again
invalid
=
{
,
"a"
:
1
,
"b"
:
2
,
"c"
:
3
}
Now I personally think that bullet points are the bee's knees and wish more languages allowed leading separators. TLA+ actually has leading conjunction and disjunction operations:
// Not TLA+ but the same semantics
|| && a == 1
   && b == 2

|| && a == 3
   && b == 4
You can't trail these, though, no writing
(a &&)
.
The most flexible I've seen is
Alloy
, which allows both leading and trailing commas:
// Alloy
sig
Valid
{
,
a
:
1
,
b
:
2
}
sig
AlsoValid
{
a
:
1
,
b
:
2
,
}
Alloy does go a little power-mad here, because it also allows empty separators.
sig
StillValid
{
,,
a
:
1
,,
,,,,,,,,,
,,
b
:
2
,,
}
I've heard some people call this
"stuttering"
. I can't figure out how to
commit crimes with this
but you never know.
Devil's advocate
One argument against trailing separators is that they make parsing ambiguous. Consider this Prolog:
foo
(
A
,
B
)
:-
A
=
1
,
B
=
2.
bar
(
c
).
Here it's pretty clear that
foo
and
bar
are separate definitions. But if we replace the rule terminator with commas:
foo
(
A
,
B
)
:-
A
=
1
,
B
=
2
,
bar
(
c
),
Now it
could
be alternatively parsed that
bar(c)
is part of the definition of
foo
—
foo
is only true when
bar(c)
is also true.
As another example,
this is valid Ruby
:
# prints 5
puts
3
.
succ
()
.
succ
()
If we could "trail method calls", this is ambiguous:
foo
.
bar
()
.
baz
()
.
quux
()
Now it's not clear if
quux()
is a top-level function or a method of
foo
.
Both of those relate to control separators, not data separators. Python has an edge data case with trailing data separators. The language uses parenthesis both for expression grouping like
(2+3)
and for tuple definition like
(2,3)
. So how do you distinguish an expression evaluation from a single-element tuple? With a trailing comma!
>>> x = (2+3)
>>> type(x)
<class 'int'>
>>> x = (2+3,)
>>> type(x)
<class 'tuple'>
Okay that's all I got. New (and final) preview release of
Logic for Programmers
next week.
