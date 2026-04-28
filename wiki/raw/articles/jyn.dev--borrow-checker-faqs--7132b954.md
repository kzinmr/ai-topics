---
title: "borrow-checker FAQs"
url: "https://jyn.dev/borrow-checker-faqs/"
fetched_at: 2026-04-28T07:02:51.867072+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# borrow-checker FAQs

Source: https://jyn.dev/borrow-checker-faqs/

I got lots of positive feedback about
the FAQ
section
in my Rust 2020 blog post, so
I'm trying that format again for another topic that's been requested a lot: How to fix common
borrow-checker issues. This isn't meant to explain how or why the borrow checker works the way it
does (see
The Nomicon
or
Two Beautiful Rust
Programs
for that), just how
to work around some of its current limitations.
In a small break from the format, the 'questions' will instead be Rust code and the accompanying
compiler error. I make no pretense that the code is doing useful work, it's just meant to give
examples of errors.
FAQ
How do I modify elements in a collection while also modifying the collection?
Playground
let
mut
queue
=
vec!
[
1
,
2
,
3
]
;
for
elem
in
queue
.
iter_mut
(
)
{
*
elem
+=
2
;
queue
.
push
(
*
elem
+
1
)
;
}
error[E0499]: cannot borrow `queue` as mutable more than once at a time
--> src/main.rs:5:9
|
3 |     for elem in queue.iter_mut() {
|                 ----------------
|                 |
|                 first mutable borrow occurs here
|                 first borrow later used here
4 |         *elem += 2;
5 |         queue.push(*elem + 1);
|         ^^^^^ second mutable borrow occurs here
This happens because for-loops borrow the iterator for the
whole
loop, not just for a single
iteration. You can work around it by using
while let
instead:
let
mut
queue
=
vec!
[
1
,
2
,
3
]
;
while
let
Some
(
mut
elem
)
=
queue
.
pop
(
)
{
elem
+=
2
;
queue
.
push
(
elem
+
1
)
;
}
Note that this has a behavior change: unlike the previous loop, this removes the element from the
queue before modifying it. You can get the behavior from before back by adding
queue.insert(0, elem)
(although at that point you may want to use a
VecDeque
).
I have disjoint fields in a struct, but because I use one in a closure, I can't use the other.
struct
S
{
elems
:
Vec
<
i32
>
,
metadata
:
i32
,
}
let
mut
s
=
S
{
elems
:
vec!
[
1
,
2
,
3
]
,
metadata
:
0
,
}
;
std
::
thread
::
spawn
(
|
|
{
for
x
in
s
.
elems
{
println!
(
"
{}
"
,
x
)
;
}
}
)
;
println!
(
"
{}
"
,
s
.
metadata
)
;
error[E0382]: borrow of moved value: `s`
--> src/main.rs:18:16
|
8  | let s = S {
|     - move occurs because `s` has type `S`, which does not implement the `Copy` trait
...
12 | std::thread::spawn(|| {
|                    -- value moved into closure here
13 |     for x in s.elems {
|              ------- variable moved due to use in closure
...
18 | println!("{}", s.metadata);
|                ^^^^^^^^^^ value borrowed here after move
This happens because the closure captures the whole
s
struct, not just the fields it needs.
You can explicitly say which fields to capture by adding a
let
statement:
let
elems
=
s
.
elems
;
std
::
thread
::
spawn
(
|
|
{
for
x
in
elems
{
println!
(
"
{}
"
,
x
)
;
}
}
)
;
This is done automatically for you with
#![feature(capture_disjoint_fields)]
, which will
hopefully be
enabled by default
in the 2021 edition.
Similar issues happen for structs that aren't
Send
or
Sync
:
use
std
::
cell
::
RefCell
;
struct
S
{
elems
:
Vec
<
i32
>
,
metadata
:
RefCell
<
i32
>
,
}
let
s
=
S
{
elems
:
vec!
[
1
,
2
,
3
]
,
metadata
:
RefCell
::
new
(
0
)
,
}
;
std
::
thread
::
spawn
(
|
|
{
for
x
in
&
s
.
elems
{
println!
(
"
{}
"
,
x
)
;
}
}
)
;
println!
(
"
{}
"
,
s
.
metadata
.
borrow
(
)
)
;
error[E0277]: `RefCell<i32>` cannot be shared between threads safely
--> src/main.rs:16:1
|
16  | std::thread::spawn(|| {
| ^^^^^^^^^^^^^^^^^^ `RefCell<i32>` cannot be shared between threads safely
|
= help: within `S`, the trait `Sync` is not implemented for `RefCell<i32>`
= note: required because it appears within the type `S`
= note: required because of the requirements on the impl of `Send` for `&S`
= note: required because it appears within the type `[closure@src/main.rs:16:20: 20:2]`
error: aborting due to previous error
If you only need a few of the fields, you can add explicit
let
statements in the same way.
let
elems
=
s
.
elems
;
std
::
thread
::
spawn
(
|
|
{
for
x
in
elems
{
println!
(
"
{}
"
,
x
)
;
}
}
)
;
println!
(
"
{}
"
,
s
.
metadata
.
borrow
(
)
)
;
Moving a line of code into a separate function makes it fail to compile.
There are actually quite a few things that will cause this. The most common are:
The compiler can no longer tell you're using disjoint fields.
You wrote the wrong lifetimes (or the elided lifetimes are wrong).
An example of 1 (
Playground
):
struct
S
{
elems
:
Vec
<
i32
>
,
metadata
:
i32
,
}
impl
S
{
fn
set_metadata
(
&
mut
self
,
val
:
i32
)
{
self
.
metadata
=
val
;
}
}
let
mut
s
=
S
{
elems
:
vec!
[
1
,
2
,
3
]
,
metadata
:
0
,
}
;
let
_elems
=
s
.
elems
;
s
.
metadata
=
1
;
s
.
set_metadata
(
1
)
;
error[E0382]: borrow of partially moved value: `s`
--> src/main.rs:22:1
|
20 | let elems = s.elems; // moves out of `elems`
|             ------- value partially moved here
21 | s.metadata = 1; // works fine
22 | s.set_metadata(1); // breaks because `elems` is moved
| ^ value borrowed here after partial move
|
= note: partial move occurs because `s.elems` has type `Vec<i32>`, which does not implement the `Copy` trait
There is no simple fix for this; this is the main reason getters and setters are discouraged in
Rust. You can either manually inline the code, or change your struct so that the relevant parts
use composition instead of all being in the same struct:
struct
S
{
elems
:
Vec
<
i32
>
,
metadata
:
Inner,
}
struct
Inner
(
i32
)
;
impl
Inner
{
fn
set_metadata
(
&
mut
self
,
val
:
i32
)
{
*
self
=
Inner
(
val
)
;
}
}
let
mut
s
=
S
{
elems
:
vec!
[
1
,
2
,
3
]
,
metadata
:
Inner
(
0
)
,
}
;
let
_elems
=
s
.
elems
;
s
.
metadata
=
Inner
(
1
)
;
s
.
metadata
.
set_metadata
(
1
)
;
An example of 2 (
Playground
):
struct
S
<
'a
>
(
&
'a
i32
)
;
impl
S
<
'
_
>
{
fn
inner
(
&
self
)
->
&
i32
{
self
.
0
}
}
let
x
=
0
;
let
_p
=
{
let
s
=
S
(
&
x
)
;
s
.
0
}
;
let
_q
=
{
let
s
=
S
(
&
x
)
;
s
.
inner
(
)
}
;
This one is tricky to spot: the issue isn't the code you wrote, but rather the code you
didn't
write.
If you desugar
inner()
, it would be something like
fn
inner
<
's
>
(
&
's
self
)
->
&
's
i32
{
self
.
0
}
But this is unnecessarily restrictive -
self.0
lives longer than
self
. The fix is to write the lifetime yourself:
impl
<
'a
>
S
<
'a
>
{
fn
inner
(
&
self
)
->
&
'a
i32
{
self
.
0
}
}
There are a lot more variants of this. I might publish a follow-up post with more.
How can I use an iterator from a struct when I also need mutable access? I know that my changes won't affect the iterator.
Playground
struct
S
{
elems
:
Vec
<
i32
>
,
metadata
:
i32
,
}
let
mut
s
=
S
{
elems
:
vec!
[
1
,
2
,
3
]
,
metadata
:
0
,
}
;
for
x
in
s
.
elems
.
iter
(
)
{
takes_s
(
*
x
,
&
mut
s
)
;
}
fn
takes_s
(
x
:
i32
,
s
:
&
mut
S
)
{
s
.
metadata
=
x
;
}
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable
--> src/main.rs:13:17
|
12 | for x in s.elems.iter() {
|          --------------
|          |
|          immutable borrow occurs here
|          immutable borrow later used here
13 |     takes_s(*x, &mut s);
|                 ^^^^^^ mutable borrow occurs here
You can
.collect
the iterator before using it:
let
iter
:
Vec
<
_
>
=
s
.
elems
.
iter
(
)
.
copied
(
)
.
collect
(
)
;
for
x
in
iter
{
takes_s
(
x
,
&
mut
s
)
;
}
Note that this isn't ideal in several ways:
If you're wrong that
takes_s
doesn't affect the iterator, it changes the behavior.
It makes the iterator eager instead of lazy, which means you have to allocate a new collection
(you don't strictly have to use
Vec
, but there's no reason to use anything else).
It requires either copying or cloning the elements.
However, in some cases, there's no alternative. See
this Rustdoc
PR
for a real-world example.
