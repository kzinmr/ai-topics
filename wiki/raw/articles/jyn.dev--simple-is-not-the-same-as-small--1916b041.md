---
title: "simple is not small"
url: "https://jyn.dev/simple-is-not-the-same-as-small/"
fetched_at: 2026-09-04T10:00:43.703315+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# simple is not small

Source: https://jyn.dev/simple-is-not-the-same-as-small/

@notjack.space
: UIs with too many buttons confuse and alarm me
@
sixfold-origami.com
: ah, this is the unix thing!
@notjack.space
: no, because I want cross device sync to actually work
Do we need simplicity?
Recently, I gave a talk titled
"Precise, consistent, and reliable code coverage"
.
It's about a truly gnarly bug that took my company 9 months to debug.
At the end, my friend
Predrag
asks:
How would you recommend that we think about building tools such that these epic debugging stories aren't as necessary?
and I answer him:
We need to prioritize simplicity.
If you go back to my coverage pipeline, there are a
lot
of nodes in this diagram. [...]
The tooling's complicated.
We need to rethink how our computing works.
I'm not satisfied with that answer.
Unix pipelines are not simple
Consider two programs to calculate the frequency of words of a file. First, a small unix pipeline:
cat
README.md
\
|
tr
--
complement
--
squeeze-repeats
'
[:alpha:]
'
'
\n
'
\
|
tr
A-Z a-z
\
|
sort
\
|
uniq
--
count
\
|
sort
--
reverse
--
numeric-sort
This says "read README.md, translate each word boundary into a newline, collapsing multiple newlines, convert uppercase to lowercase, count the number of occurrences of each word, then show them in frequency order".
I think this is what most people think of when they think of "simple":
each program is small, they're designed to be joined together ad-hoc in this way, it's concise and somewhat easy to read.
Next, consider a Clojure program:
(
->>
(
slurp
"
README.md
"
)
(
re-seq
#
"
[
a
-z
A
-Z
]
+
"
)
(
map
str/lower-case
)
frequencies
(
sort-by
val >
)
(
run!
(
fn
[
[
word count
]
]
(
println
count word
)
)
)
)
This does the same thing, with a few more names and higher-order functions thrown in.
Now, let's say we want to make a small change: show the output in the original file order.
In Clojure, this is fairly straightforward:
store an ordered sequence of the words in
word_seq
, store a map from each word to its frequency in
freq_map
, iterate over the sequence, and look up each word in the map:
(
let
[
word_seq
(
->>
(
slurp
"
README.md
"
)
(
re-seq
#
"
[
a
-z
A
-Z
]
+
"
)
(
map
str/lower-case
)
)
freq_map
(
frequencies
word_seq
)
]
(
->>
(
distinct
word_seq
)
(
run!
(
fn
[
w
]
(
println
(
freq_map
w
)
w
)
)
)
)
)
In Bash you need a bunch of temp files and ugly opaque regexes, sorts, and joins:
tr
<
README.md
--
complement
--
squeeze-repeats
'
[:alpha:]
'
'
\n
'
\
|
grep
.
>
words
sort
words
\
|
uniq
--
count
\
|
sed
--
regexp-extended
'
s/^ *([0-9]+) (.*)/\2 \1/
'
\
|
sort
>
counts
nl
--
body-numbering
=
a words
\
|
sort
--
key
=
2,2
--
key
=
1,1n
\
|
uniq
--
skip-fields
=
1
\
|
sort
--
key
=
2,2
>
firstseen
join
-
1
2
-
2
1
-
o
1.1,2.2,1.2 firstseen counts
\
|
sort
--
numeric-sort
\
|
cut
--
delimiter
=
'
'
--
field
=
2,3
That's because our original program was
small
but not
simple
.
What is simplicity?
In
Simple Made Easy
(
transcript
),
Rich Hickey defines "simple" from its root, "sim-plex": having only one braid.
He contrasts this to "com-plex": braiding multiple things together.
In this post I'll use "coupled" as a synonym for "complex" to avoid ambiguity.
And that gives us a language to talk about what's going on with our first Unix pipeline: it's
small
but it's
coupled
.
Let's look at exactly what makes it that way.
tr
<
README.md
--
complement
--
squeeze-repeats
'
[:alpha:]
'
'
\n
'
\
|
tr
A-Z a-z
\
|
sort
\
|
uniq
--
count
\
|
sort
--
reverse
--
numeric-sort
There are a bunch of little things here I could nitpick, but the main thing that's coupled (
braided together
) is the
sort | uniq --count
.
If we look at
uniq
's man page, it says this:
Repeated lines in the input will not be detected if they are not adjacent, so it may be necessary to sort the files first.
There's no native Unix equivalent to
frequencies
, this
sort | uniq -c
is the closest we can get.
Not only is it less performant (it has to collect the full input into memory before continuing),
but it ties aggregation to ordering.
This is exactly the thing that makes "separate ordering from aggregation" so hard;
we end up having to do this weird dance with table-joins-through-text-files.
You might have heard the phrase "Write programs that do one thing and do it well" in reference to Unix systems.
Maybe you heard it called the
Unix Philosophy
.
I think "do one thing" is commonly understood to be about simplicity, but in practice it's actually about
size
.
Unix tools are
small
but they are not
simple
.
Large is not the same as coupled
Now, let's consider the opposite end.
Say you have Google Drive for Desktop running on your computer.
This is a
massively
large program:
it depends on platform-specific file watchers, "all of Google3", a streaming and syncing network client, and conflict resolution logic.
But to the
user
it feels quite simple:
Install the program, tell it which folder you want it to watch, tell it whether to keep the files locally or primarily on Google's infra.
It does all the rest.
Decoupling
When I think about complex programs, I think about
coupling
.
Programs are complex when different features are
coupled
to each other, even when they don't have to be.
Let's take one small example.
In Rust, you can associate names to values with a map, or with a struct:
struct
HttpResponse
{
status
:
u16
,
}
let
strukt
=
HttpResponse
{
status
:
200
}
;
let
mut
map
=
HashMap
::
new
(
)
;
map
.
insert
(
"
status
"
,
200
)
;
println!
(
"
map:
{}
"
,
map
.
get
(
"
status
"
)
.
unwrap
(
)
)
;
println!
(
"
struct:
{}
"
,
strukt
.
status
)
;
It's very clear from this that a struct gets you
known present fields
.
For the map, we have to call
unwrap()
, because the type checker doesn't know what keys are in a map.
For the struct it does, so we can just directly access the value.
What might not be clear about this is that a struct
loses runtime information
.
If you want to iterate a map, that's easy: call
for (key, val) in map { ...
.
If you want to iterate a struct ... get fucked? write a proc-macro?
The reason for this is that in Rust, a struct
couples
type-checking to a fixed data representation.
You can't get one without the other.
Contrast this to Clojure, where you
can
.
In Clojure, structs
are
maps: rather than defining a type, you annotate which fields a map is allowed to have.
If we wanted to translate our
struct HttpResponse
, we could write this:
(
def
http-response
[
:
map
[
:
status
:
int
]
]
)
(
defn
^
{
:
malli/schema
[
:
=>
[
:
cat
http-response
]
:
nil
]
}
print-resp
[
map
]
(
println
"
status:
"
(
:
status
map
)
)
)
Here, we've created a type annotation that's checked at runtime with the function
(malli/instrument!)
.
Notably, this is checked
with a library
(Malli), not by a compiler;
and the annotation is
inspectable
.
You can, for example, write a
schema->md
function that acts as your own little mini Rustdoc, without needing to integrate with compiler APIs.
And all of this works without giving up type safety, reflection, or iteration over the values of the map.
This works because Clojure
decouples
data representations from type checking.
Typed Racket does a similar trick, but using macros so that the type checking happens at compile time instead of runtime.
When is it useful to be small?
Being small makes sense when you as the maintainer don't have a lot of resources to dedicate to your program.
Maybe you're Brian Kernighan and your program is running on a literal PDP-11.
Maybe you're an open source maintainer with only a couple hours a month to dedicate to your project.
Maybe you work in an environment where doing
anything
is a victory and you can only get support for a small subset of the features you actually want to build.
All of these are good reasons to keep your program small.
But small is not the same as simple.
The answer to "when should your program be simple?" is:
always
.
There is very little advantage to introducing coupling to parts of your program;
it makes it harder for you as a developer to maintain the program, and is less flexible for your users.
How do we make simple programs?
Ah, now this is the hard part.
To write simple programs, you need to have a good
mental model
of your program.
You also need to have
good taste
, which is something I don't yet know how to teach.
Sometimes, you also need to Suck It Up And Write The Hard Thing.
CSS and SQL are highly decoupled (
mostly
):
you write a declarative specification of what you want the program to do, and the browser engine or database runtime figure out how to do it.
This is really really hard!
SQLite alone has had centuries of person-years put into making it work reliably.
Blink (Chrome's renderer) has probably had tens of thousands of person-years put into it.
In some domains, that's what it takes to let you write programs that are decoupled.
It doesn't always make sense to spend that much time on a program.
Crunchy
technical work can be a
mothlamp problem
:
it attracts a certain kind of person who loves dreaming about how code
might
,
should
,
could
work.
Sometimes it's better to put down your tools and take a nap in the sun instead.
But when it does work—
If we go back to the start of the post, the coverage pipeline I describe actually got
larger
after I fixed it, not smaller.
But at the same time it got
simpler
, because there were fewer hidden dependencies between parts of the dataflow graph.
What next?
I hope this post encourages you to write programs that are simple, not small,
and to look for tools that you use that are unnecessarily coupled.
In a future post, I hope to extend these ideas:
how to develop your sense of taste;
how programs can be vertically integrated while still being decoupled;
and how to build large systems without making them complex.
