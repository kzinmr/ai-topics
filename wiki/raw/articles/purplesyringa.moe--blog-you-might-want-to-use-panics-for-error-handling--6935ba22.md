---
title: "You might want to use panics for error handling"
url: "https://purplesyringa.moe/blog/./you-might-want-to-use-panics-for-error-handling/"
fetched_at: 2026-05-05T07:02:09.998701+00:00
source: "Alisa Sireneva (PurpleSyringa)"
tags: [blog, raw]
---

# You might want to use panics for error handling

Source: https://purplesyringa.moe/blog/./you-might-want-to-use-panics-for-error-handling/

You might want to use panics for error handling
August 13, 2024
Rust’s approach to error handling is neat, but it comes at a cost. Fallible functions return this type:
enum
Result
<T, E> {
Ok
(T),
Err
(E),
}
So the
Result
type is almost always larger than the actual returned value:
Discriminant
                                          vv
                                     +-----------+--------------------------+
                       Ok variant:   | 0x00...00 |       actual data        |
                                     +-----------+--------------------------+

                                     +-----------+--------------------------+
                       Err variant:  | 0x00...01 |       actual error       |
                                     +-----------+--------------------------+
Oftentimes it doesn’t fit in CPU registers, so it has to be spilled to stack.
Callers of fallible functions have to check whether the returned value is
Ok
or
Err
:
f
()?
match
f
() {
Ok
(value) => value,
Err
(err) =>
return
Err
(err), 
}
That’s a comparison, a branch, and a lot of error handling code intertwined with the hot path that
just shouldn’t be here
. And I don’t mean that lightly: large code size inhibits inlining, the most important optimization of all.
Alternatives
Checked exceptions – the closest thing there is to
Result
s – have different priorities. They simplify the success path at the expense of the failure path, so it’s easy to forget about the occasional error. This is an explicit anti-goal of Rust.
Rust has panics that use the same mechanism, but guides against using them for fallible functions, because they are almost unusable for that purpose:
fn
produces
(n:
i32
)
->
i32
{
if
n >
0
{
        n
    }
else
{
panic!
(
"oopsie"
)
    }
}
fn
produces_result
(n:
i32
)
->
Result
<
i32
, &
'static
str
> {
if
n >
0
{
Ok
(n)
    }
else
{
Err
(
"oopsie"
)
    }
}
fn
forwards
(n:
i32
)
->
i32
{
let
a
=
produces
(n);
let
b
=
produces
(n +
1
);
    a + b
}
fn
forwards_result
(n:
i32
)
->
Result
<
i32
, &
'static
str
> {
let
a
=
produces_result
(n)?;
let
b
=
produces_result
(n +
1
)?;
Ok
(a + b)
}
fn
catches
(n:
i32
)
->
i32
{
    
    std::panic::
catch_unwind
(|| forwards(n)).
unwrap_or
(
0
)
}
fn
catches_result
(n:
i32
)
->
i32
{
    forwards_result(n).
unwrap_or
(
0
)
}
Forbidden fruit
However, panics don’t suffer from inefficiency! Throwing an exception unwinds the stack automatically, without any cooperation from the functions except the one that throws the exception and the one that catches it.
Wouldn’t it be
neat
if a mechanism with the performance of
panic!
and the ergonomics of
Result
existed?
#[iex]
I’m quite familiar with the Rust macro ecosystem, so I devised a way to
fix that with a crate
. Here’s how it works, roughly:
use
iex::{iex, Outcome};
#[iex]
fn
produces
(n:
i32
)
->
Result
<
i32
, &
'static
str
> {
if
n >
0
{
Ok
(n)
    }
else
{
Err
(
"oopsie"
)
    }
}
#[iex]
fn
forwards
(n:
i32
)
->
Result
<
i32
, &
'static
str
> {
let
a
=
produces
(n)?;
let
b
=
produces
(n +
1
)?;
Ok
(a + b)
}
fn
catches
(n:
i32
)
->
i32
{
    
    forwards(n).
into_result
().
unwrap_or
(
0
)
}
This was just a joke experiment at first. It
should
work quite efficiently. Microbenchmarks are bound to show that.
But the design allows
Result
-based code to work with
#[iex]
with minimal changes. So I can slap
#[iex]
on a
real
project and benchmark it on
realistic data
.
Benchmarks
One simple commonly used project is
serde
. After fixing some glaring bugs, I got these benchmark results on JSON deserialization tests:
Speed (MB/s, higher is better)
canada
citm_catalog
twitter
DOM
struct
DOM
struct
DOM
struct
Result
282.4
404.2
363.8
907.8
301.2
612.4
#[iex] Result
282.4
565.0
439.4
1025.4
317.6
657.8
Performance increase
0%
+40%
+21%
+13%
+5%
+7%
This might not sound like a lot, but that’s a
great
performance increase
just
from error handling. And this is a universal fix to a global problem.
That includes you
To be clear, this benchmark only measures the success path. In realistic programs, the error path may be reached more often than the success path in some cases, so this is not a generic optimization.
However, it is applicable in almost every project to some degree: for example, querying a database is almost always successful. Optimizing such paths is trivial with
#[iex]
:
Slap
#[iex]
onto all functions that return
Result
,
Whenever you need to match on a
Result
or apply a combinator, try to rewrite code without that, and if you can’t, add
.into_result()
,
Occasionally replace
return e
with
return Ok(e?)
for… reasons.
Afterword
#[iex]
is a very young project. It might not be the best solution for production code, and it would certainly be great if rustc supported something like a
#[cold_err]
attribute to propagate errors by unwinding without external crates.
But I think it’s a move in the right direction.
The crate documentation
includes instructions on how to use
#[iex]
in your project. If you find this library useful, please tell me
on the issue tracker
.
