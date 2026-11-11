---
title: "Monads in Lean - Eli Bendersky's website"
url: "https://eli.thegreenplace.net/2026/monads-in-lean/"
fetched_at: 2026-11-11T10:01:31.117412+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Monads in Lean - Eli Bendersky's website

Source: https://eli.thegreenplace.net/2026/monads-in-lean/

This post demonstrates how to use monads in the Lean programming language
(Lean 4, to be specific). If you're not familiar with Lean, this part of the
language is very similar to other functional programming languages, like
Haskell or OCaml.
Motivating example - evaluating expressions
Suppose we want to write a simple numerical expression evaluator that supports
numbers with addition and division:
inductive
Expr
where
|
num
:
Int
→
Expr
|
add
:
Expr
→
Expr
→
Expr
|
div
:
Expr
→
Expr
→
Expr
What happens when we encounter a division by zero? We'll want our evaluator
to report this as a failure, which will be represented explicitly using the
the
Option
type:
def
safeDiv
(
x
y
:
Int
)
:
Option
Int
:=
if
y
==
0
then
none
else
some
(
x
/
y
)
With this in hand, the
eval
function can be written as follows:
def
eval
:
Expr
→
Option
Int
|
.
num
n
=>
some
n
|
.
add
a
b
=>
match
eval
a
with
|
none
=>
none
|
some
x
=>
match
eval
b
with
|
none
=>
none
|
some
y
=>
some
(
x
+
y
)
|
.
div
a
b
=>
match
eval
a
with
|
none
=>
none
|
some
x
=>
match
eval
b
with
|
none
=>
none
|
some
y
=>
safeDiv
x
y
safeDiv
returns an
Option
; to propagate that possible failure to
its caller,
eval
also returns an
Option
, and - moreover - has to perform
lots of tedious checking for the possibility of a
none
value. Is there a
better way?
Note a common code pattern repeated here:
Examine the value of an
Option
If it's
none
, return
none
without proceeding
Otherwise if it's
some result
, continue the computation with
result
We can extract it into a helper function:
def
withSome
(
result
:
Option
α
)
(
onSuccess
:
α
→
Option
β
)
:
Option
β
:=
match
result
with
|
none
=>
none
|
some
x
=>
onSuccess
x
And rewrite our
eval
using this helper:
def
evalWithSome
:
Expr
→
Option
Int
|
.
num
n
=>
some
n
|
.
add
a
b
=>
withSome
(
evalWithSome
a
)
(
fun
x
=>
withSome
(
evalWithSome
b
)
(
fun
y
=>
some
(
x
+
y
)))
|
.
div
a
b
=>
withSome
(
evalWithSome
a
)
(
fun
x
=>
withSome
(
evalWithSome
b
)
(
fun
y
=>
safeDiv
x
y
))
This is already much better; we can make it even cleaner using operator
overloading:
infixl
:
55
" >>? "
=>
withSome
def
evalOp
:
Expr
→
Option
Int
|
.
num
n
=>
some
n
|
.
add
a
b
=>
evalOp
a
>>?
fun
x
=>
evalOp
b
>>?
fun
y
=>
some
(
x
+
y
)
|
.
div
a
b
=>
evalOp
a
>>?
fun
x
=>
evalOp
b
>>?
fun
y
=>
safeDiv
x
y
Congratulations - we've pretty much invented monads!
Option
as a
Monad
in expression evaluation
In simplified form, the
Monad
type class in Lean is defined as:
class
Monad
(
m
:
Type
→
Type
)
where
pure
:
α
→
m
α
bind
:
m
α
→
(
α
→
m
β
)
→
m
β
In our code,
pure
is equivalent to
some
, and
bind
is equivalent
to
withSome
; in fact, the
Monad
instance for
Option
is something
like:
instance
:
Monad
Option
where
pure
x
:=
some
x
bind
opt
next
:=
match
opt
with
|
none
=>
none
|
some
x
=>
next
x
An operator akin to
>>?
for monads is already defined in Lean; it's called
>>=
, and picks up the
bind
method of the
Monad
type class. So we can
rewrite our evaluator using the standard
Monad
instance, without defining
withSome
or the
>>?
operator :
def
evalBind
:
Expr
→
Option
Int
|
.
num
n
=>
pure
n
|
.
add
a
b
=>
evalBind
a
>>=
fun
x
=>
evalBind
b
>>=
fun
y
=>
some
(
x
+
y
)
|
.
div
a
b
=>
evalBind
a
>>=
fun
x
=>
evalBind
b
>>=
fun
y
=>
safeDiv
x
y
We can go even further with the
do
notation, which is syntactic sugar around
>>=
that lets us rewrite the evaluator as:
def
evalDo
:
Expr
→
Option
Int
|
.
num
n
=>
pure
n
|
.
add
a
b
=>
do
let
x
←
evalDo
a
let
y
←
evalDo
b
some
(
x
+
y
)
|
.
div
a
b
=>
do
let
x
←
evalDo
a
let
y
←
evalDo
b
safeDiv
x
y
This notation should be familiar if you've seen Lean code dealing with I/O;
we'll revisit I/O later in the post.
Monads for modeling side effects
Functional programming languages place a lot of emphasis on
pure
functions
that are free of side effects. There's no question that such functions are
easier to reason about, debug, and even optimize (by memoization). That said,
the real world is messy and sometimes side effects are inescapable; monads
help encapsulate side effects in functional programs.
The core idea is: side effects are encapsulated inside a
Monad
, which
wraps the value returned from a computation. The
bind
method (or the
equivalent
>>=
operator) lets us take a wrapped value and push it into the
next computation in the sequence. This may look familiar from
continuation-passing style (CPS). Continuations themselves can also be modeled
with a monad .
The definition of
bind
is:
bind
:
m
α
→
(
α
→
m
β
)
→
m
β
Here's a mental model to think about it:
Take a value wrapped with potential side effects
Take a computation that takes this value and may produce additional side
effects
Combine the results into a final wrapped value
Chaining multiple
bind
s together is essentially a sequence of computations
while keeping track of the side effects. A monad decouples what computations
do
from
how they are sequenced
. The programmer describes the sequence of
computations and their dependencies, while the monad's
bind
implementation
handles the bookkeeping necessary to combine their side effects.
Our evaluator case study shows one example of side effects: early return from
a computation with a
none
value.
Let's see another idiomatic way of doing that, with the
Except
type that
contains either a successful result or an error value (very similar to the
Result
type in Rust).
We'll begin by writing an exception-returning version of
safeDiv
:
def
safeDivExc
(
x
y
:
Int
)
:
Except
String
Int
:=
if
y
==
0
then
.
error
"division by zero"
else
.
ok
(
x
/
y
)
Instead of writing a whole new
eval
variant for
Except
, we'll
create a generic one that works with any
Monad
:
def
evalM
{
m
:
Type
→
Type
}
[
Monad
m
]
(
div
:
Int
→
Int
→
m
Int
)
:
Expr
→
m
Int
|
.
num
n
=>
pure
n
|
.
add
a
b
=>
do
let
x
←
evalM
div
a
let
y
←
evalM
div
b
pure
(
x
+
y
)
|
.
div
a
b
=>
do
let
x
←
evalM
div
a
let
y
←
evalM
div
b
div
x
y
Now
evalM
can be used with
safeDivExc
to implement an evaluator where
division returns
Except
; used with
safeDiv
, it would be equivalent to
the
Option
-specific
evalDo
we've written before.
#
eval
evalM
safeDiv
(
.
add
(
.
num
4
)
(
.
div
(
.
num
6
)
(
.
num
0
)))
#
eval
evalM
safeDivExc
(
.
add
(
.
num
4
)
(
.
div
(
.
num
6
)
(
.
num
0
)))
Logging computations - an example of the writer monad
Let's look at a more advanced example: an evaluator that also
logs
the
computation it executes in a linear log of strings. The challenge here is that
we still have to combine that with
Option
to support the divide-by-zero
case, so we'll start by creating a new structure to carry the state of the
computation:
structure
LoggedOption
(
α
:
Type
)
where
value
:
Option
α
log
:
List
String
This will be the result of one
eval
call; it produces an optional value,
along with a list of strings (the log). Here's the
Monad
implementation for
this type:
instance
:
Monad
LoggedOption
where
pure
x
:=
⟨
some
x
,
[]
⟩
bind
v
next
:=
match
v
.
value
with
|
none
=>
⟨
none
,
v
.
log
⟩
|
some
x
=>
let
nextResult
:=
next
x
⟨
nextResult
.
value
,
v
.
log
++
nextResult
.
log
⟩
The main idea is combining the stored log with the log of the next computation
by appending them (thus accumulating a linear log). Here's our evaluator:
def
evalLogged
:
Expr
→
LoggedOption
Int
|
.
num
n
=>
pure
n
|
.
add
a
b
=>
do
let
x
←
evalLogged
a
let
y
←
evalLogged
b
⟨
some
(
x
+
y
),
[
s!
"adding {x} and {y}"
]
⟩
|
.
div
a
b
=>
do
let
x
←
evalLogged
a
let
y
←
evalLogged
b
match
y
with
|
0
=>
⟨
none
,
[
s!
"dividing {x} by zero"
]
⟩
|
_
=>
⟨
some
(
x
/
y
),
[
s!
"dividing {x} by {y}"
]
⟩
Note how the code of
evalLogged
doesn't have to deal with the mechanics
of logging too much (other than adding new log entries). All of that is hidden
within the monad instance.
LoggedOption
is an example of the
writer monad
,
which is a write-only version of the
state monad
.
State monad
One of the most important use cases of monads in functional programming
languages is modeling mutable state through a computation.
A stateful computation is modeled as a function that takes an initial state
and returns a tuple containing the result value and a new, updated state. In
Lean notation:
def
State
(
σ
:
Type
)
(
α
:
Type
)
:
Type
:=
σ
→
(
α
×
σ
)
To demonstrate this in action, let's enhance our evaluator to support variable
assignments and lookups. Our state is going to be an association list of
name, value
pairs:
abbrev
Vars
:=
List
(
String
×
Int
)
And we'll augment our expression enum with additional operations:
inductive
ExprV
where
|
num
:
Int
→
ExprV
|
add
:
ExprV
→
ExprV
→
ExprV
|
div
:
ExprV
→
ExprV
→
ExprV
|
store
:
String
→
ExprV
→
ExprV
|
load
:
String
→
ExprV
This is going to be our state monad:
structure
EvalM
(
α
:
Type
)
where
run
:
Vars
→
Option
(
α
×
Vars
)
Note the correspondence of the
run
function to the
State
signature
above:
It takes the current state, which for our use cases is an association list
carrying values for all defined variables.
It returns an optional result which is a pair of some value (in our case,
the result of the computation) and an updated state.
This is its
Monad
class implementation:
instance
:
Monad
EvalM
where
pure
x
:=
⟨
fun
vars
=>
some
(
x
,
vars
)
⟩
bind
action
next
:=
⟨
fun
vars
=>
match
action
.
run
vars
with
|
none
=>
none
|
some
(
x
,
vars'
)
=>
(
next
x
)
.
run
vars'
⟩
And finally, the evaluator:
def
evalState
:
ExprV
→
EvalM
Int
|
.
num
n
=>
pure
n
|
.
add
a
b
=>
do
let
x
←
evalState
a
let
y
←
evalState
b
pure
(
x
+
y
)
|
.
div
a
b
=>
do
let
x
←
evalState
a
let
y
←
evalState
b
⟨
fun
vars
=>
(
safeDiv
x
y
)
.
map
(
fun
value
=>
(
value
,
vars
))
⟩
|
.
load
name
=>
⟨
fun
vars
=>
do
let
value
←
vars
.
lookup
name
pure
(
value
,
vars
)
⟩
|
.
store
name
rhs
=>
do
let
value
←
evalState
rhs
⟨
fun
vars
=>
let
vars'
:=
(
name
,
value
)
::
vars
.
filter
(
fun
p
=>
p
.
1
!=
name
)
some
(
value
,
vars'
)
⟩
Operations that don't deal with variables directly (like
.num
and
.add
) just do their work as before.
.div
only has to deal with the
actual monad type to ensure that
none
is propagated in case of division
by zero. Note also that this evaluator supports stores as expressions, since
they separately return a value and the updated state; therefore, computations
like this one will work:
-- (x := 12) + (x / 3): the right operand sees the left operand's assignment.
#
eval
(
evalState
(
.
add
(
.
store
"x"
(
.
num
12
))
(
.
div
(
.
load
"x"
)
(
.
num
3
))))
.
run
[]
Producing the result
some (16,
[("x",
12)])
.
In a language with mutable state, modeling side effects is easy - just assign
some state (like a struct field or class member). In a functional language like
Lean, however, we have to carry this state across the computations explicitly;
monads help us do this with elegance - by hiding most of the mechanics of
actually carrying the state around, the majority of the code remains free
of bookkeeping.
IO monad
Perhaps the most well known example of a monad in functional programming
languages like Lean and Haskell is
IO
. To anyone who's written a "real"
program that interacts with the outer world,
IO
is very familiar. Here's
a customized "Hello" program that's typically taught in the first 15
minutes of learning a new programming language:
def
greet
:
IO
Unit
:=
do
let
stdin
←
IO
.
getStdin
IO
.
println
"What is your name?"
let
name
←
stdin
.
getLine
IO
.
println
s!
"Hello, {name}"
Note the
do
notation here, suggesting monads. As mentioned before,
do
is syntactic sugar for the monad's
bind
method, or the
>>=
operator; we
can rewrite this code more explicitly as:
def
greetBind
:
IO
Unit
:=
IO
.
getStdin
>>=
fun
stdin
=>
IO
.
println
"What is your name?"
>>=
fun
_
=>
stdin
.
getLine
>>=
fun
name
=>
IO
.
println
s!
"Hello, {name}"
In essence,
IO
is a state monad, where the state carried around represents
the "outside world".
IO
operations like
println
act on that world,
and its state is carried over using
bind
, like other state monads.
Here's a version of our expression evaluator that logs directly to standard out,
instead of collecting the log as a list of strings:
def
evalIO
:
Expr
→
OptionT
IO
Int
|
.
num
n
=>
pure
n
|
.
add
a
b
=>
do
let
x
←
evalIO
a
let
y
←
evalIO
b
IO
.
println
s!
"adding {x} and {y}"
pure
(
x
+
y
)
|
.
div
a
b
=>
do
let
x
←
evalIO
a
let
y
←
evalIO
b
IO
.
println
s!
"dividing {x} by {y}"
OptionT
.
mk
(
pure
(
safeDiv
x
y
))
The only unusual construct here is
OptionT
, which is a
monad transformer
that helps us compose
Option
(for propagating failure from safe division)
with the
IO
Monad .
The
IO
monad also supports
throw
for Python-like exception behavior,
but in this example we use
Option
explicitly; exceptions are a matter of
programming preference, and using them inside library functions like
eval
doesn't feel right to me.
Monad laws in Lean
Just like in Haskell, monads in Lean should obey
certain laws
.
Those are:
Left identity
: wrapping a value in
pure
and immediately passing it to
f
with
bind
should be equivalent to just calling
f
on the value:
Right identity
: extracting a value from a computation and immediately
wrapping it with
pure
again should not change the computation:
Associativity
: the grouping of operations doesn't matter, as long as their
order remains the same:
(
m
>>=
f
)
>>=
g
=
m
>>=
(
fun
v
=>
f
v
>>=
g
)
Let's see how
Option
obeys these laws.
For left identity,
pure v
is
some v
and the
bind
implementation
matches
some x
to
next x
, which is equivalent to
f v
.
For right identity,
m >>= pure
just rewraps a
some
value in
pure
,
leaving
none
alone - this is equivalent to keeping things as they are.
For associativity, if
m
is
none
then both sides are
none
. If
m
is
some v
, the left side is
f v >>= g
, and the right side reduces to
the same, so again they are equivalent.
While Lean doesn't enforce that a
Monad
instance obeys these laws, it has
a separate type class called
LawfulMonad
which
does
require Lean proofs;
this is useful for Lean's main use case - proving theorems about programs,
expressed through its powerful type system. But this is a topic for another
day.
