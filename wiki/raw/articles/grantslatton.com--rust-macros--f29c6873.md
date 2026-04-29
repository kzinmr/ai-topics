---
title: "Rust Macros: Zero to Hero"
url: "https://grantslatton.com/rust-macros"
fetched_at: 2026-04-29T07:02:16.885869+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Rust Macros: Zero to Hero

Source: https://grantslatton.com/rust-macros

Rust Macros
Introduction
In programming, a
macro
is code that writes code (typically, but not always, at compile-time).
Macros were invented in the 1950s. Writing raw binary computer code is a pain, so programmers quickly invented "assemblers" to convert more human-readable code into binary. But writing raw assembly is
also
tedious. So programmers invented macros.
The first macros were just text-substitutions. Suppose your code had a ton of instances of "add register 1 to register 2 and store the result in register 3, then multiply by register 4 and store back in register 1". You could label this sequence
do_the_thing
and then start using that meta-instruction in your code. The assembler would expand it to its constituent instructions.
Then, you get function-like macros that are still just text-substitutions, but with variable inputs. With these, you can write macros like "add the constant N to register 1 and store in register 2, then multiply that by the constant Y and store in register 3". You'd invoke this macro like
my_macro(5, 8)
where 5 and 8 are X and Y, respectively.
This style of macro is still used in languages like C. Here are some example C macros:
#define
PI
3.14159
#define
SQUARE
(
x
)
(
(
x
)
*
(
x
)
)
The first is just a constant definition. All instances of the string
PI
will be replaced by the numeric literal at compile-time. The second is more function-like.
SQUARE(5)
will be replaced by
((5) * (5))
.
Why does the
SQUARE
example have those extra parentheses? They aren't necessary in the
SQUARE(5)
case. But consider
SQUARE(3+2)
. Without the extra parentheses around the
x
argument, this would expand to
(3 + 2 * 2 + 3)
. This evaluates to 10 instead of the expected 25.
This example should highlight how bug-prone simple string-replacement macros are. Here's an even trickier example:
int
x
=
5
;
int
y
=
SQUARE
(
x
+
+
)
;
After this code is executed, what are the values of
x
and
y
? Naively, you might think
x
is 6 (because the
++
increments it) and
y
is 25 (because the increment happens
after
reading the value of
x
).
But in reality,
x
will be 7 and
y
will be 30. Because the macro invocation expands to
((x++) * (x++))
. Even though
SQUARE
looks
like a function, it is
not
a function! It just expands to code! So we increment
x
twice
, and we multiply after
x
has already been incremented once.
Macros in C have a bad reputation for being a perpetual source of bugs, and are a common exploit in the
Underhanded C Contest
.
Here are a few examples from that content:
#define
BYTESPERPIXEL
(
fits8bits
)
(
3
<<
(
!
fits8bits
)
)
Note that lack of parentheses around
fits8bits
— the underhanded code invokes the macro like
BYTESPERPIXEL(256 > max)
which will expand to
3 << (!256 > max)
.
!256
will evaluate to a very large integer that will always be
> max
.
#define
__isleap
(
year
)
(
(
year
)
%
4
==
0
&&
(
(
year
)
%
100
!=
0
||
(
year
)
%
400
==
0
)
)
This one has all the parentheses in the right place, but takes advantage of the fact that
year
will be evaluated up to 3 times. So if you were to do something like:
__isleap
(
current_year
+
+
)
You might increment the year up to 3 times instead of 1.
The actual code
is even more devious and invokes it like:
__isleap
(
curr_year
=
AUDIT
(
…
)
)
Where
AUDIT
is
another
macro that also has side-effects.
Towards saner macros
A lot of modern languages try to bring some order to this situation. Lisp started this trend. Rather than being simple string-replacement like assembler and C, Lisp macros operate on the
abstract syntax tree
itself.
But there are still pitfalls. Consider this pseudocode:
x
=
123
some_macro
(
)
print
(
x
)
What gets printed? 123? What if
some_macro()
generates the code
x = 456
?
In the 1980s, a variant of Lisp called Scheme fixed this problem by introducing
hygienic macros
. The basic idea is to bring the ideas of
scope
to macros.
In the code above,
some_macro
is defined in some other scope, and
x
is not passed into it as an argument, so in a hygienic macro system, we have a guarantee that
x
will not be modified by
some_macro
.
Even if
some_macro
contains the code
x = 456
, the
x
it's assigning to is in a different namespace than the original
x
with value 123. You can imagine the macro's
x
having the name
x2
, so conceptually the resultant code, after the macro is expanded, is:
x
=
123
x2
=
456
print
(
x
)
Hygienic macros are a lot easier to reason about from the callsite, and a lot harder to write surprising, underhanded code.
You can do even better by adding on a type system to the macro language. Just like
fn foo(x: int, y: String)
specifies that it takes an integer and a string arguments, some languages have macros that specify what type of abstract syntax tree node they accept. Maybe the macro only accepts variable names as arguments. Maybe it only accepts numeric constants.
Rust Macros
Rust macros are hygienic and have a type system. Let's just jump into an example.
Basics
macro_rules!
bail_if
{
(
$condition
:
expr
)
=>
{
if
$condition
{
return
None
;
}
}
}
This macro can be invoked like
bail_if!(x < 123)
and will return
None
if the condition is true. If you have a function that has 10 places where you want to return
None
if a condition is true, this kind of macro can make such a function a lot more readable.
Let's break down the syntax.
macro_rules!
says "we are declaring a macro — like the
fn
keyword declares a function, or the
let
keyword declares a variable
bail_if
is the name of the macro
($condition:expr)
is the
pattern
the macro matches — this macro only has 1 pattern, but macros can have multiple, we'll cover that later
$condition
is the name of the argument — all rust macro arguments start with
$
to disambiguate them from normal Rust identifiers
expr
is the
type
of abstract syntax tree node the argument is — just like normal functions might use
int
or
String
, macros can accept expressions (
expr
) or identifiers (
ident
) and many more.
Then the body of the pattern is just Rust code, but with the macro variables
$condition
used rather than a normal Rust variable
This example also shows one of the primary motivators for macros as opposed to just normal functions.
Macros can contain control flow
. A normal function can't do a
return
or
break
or
continue
from the scope of the callsite.
Let's add a feature to our knowledge of macros. Repetition. Sometimes you want a macro to take an arbitrary number of arguments. Consider this code:
trait
CastToF64
{
fn
cast_to_f64
(
self
)
->
f64
;
}
impl
CastToF64
for
i32
{
fn
cast_to_f64
(
self
)
->
f64
{
self
as
f64
}
}
impl
CastToF64
for
u64
{
fn
cast_to_f64
(
self
)
->
f64
{
self
as
f64
}
}
/*
all the other numerics
*/
Here I have a trait that represents the ability to convert the implementor to a floating point number. Implementing it for every numeric type is tedious and boilerplate.
Generating boilerplate is another primary use-case for macros. Boilerplate code gets a bad connotation, but I think this isn't deserved so long as you have macros to do the actual code generation. My friend Sebastian Bensusan wrote
an excellent post
about this.
Here's how we can use a macro to generate this boilerplate. First, let's do it with the tools we already know:
trait
CastToF64
{
fn
cast_to_f64
(
self
)
->
f64
;
}
macro_rules!
impl_cast_to_f64
{
(
$t
:
ty
)
=>
{
impl
CastToF64
for
$t
{
fn
cast_to_f64
(
self
)
->
f64
{
*
self
as
f64
}
}
}
}
impl_cast_to_f64!
(
i16
)
;
impl_cast_to_f64!
(
u16
)
;
impl_cast_to_f64!
(
i32
)
;
impl_cast_to_f64!
(
u32
)
;
impl_cast_to_f64!
(
i64
)
;
impl_cast_to_f64!
(
u64
)
;
impl_cast_to_f64!
(
f32
)
;
We introduced a new AST node type — the
ty
keyword which pattern-matches any type name. Then we just call our macro for each type we want to implement the trait for. But we can do better! Why do we need to invoke the macro once per type? Why not just give the macro a list of types? We can do just that.
Repetition
The syntax for this is
$(pattern)*
, where
pattern
is any other macro pattern, but inside the
$(..)*
repetition markers. We repeat the
$(..)*
repetition in the code as well:
macro_rules!
impl_cast_to_f64
{
(
$
(
$t
:ty
)
*
)
=>
{
$
(
impl
CastToF64
for
$t
{
fn
cast_to_f64
(
&
self
)
->
f64
{
*
self
as
f64
}
}
)
*
}
;
}
impl_cast_to_f64!
(
i16
u16
i32
u32
i64
u64
f32
)
;
A few things to note here:
The
CastToF64
impls inside the
$(..)*
block will get stamped out once for each type. While there is some conceptual relation between
$(..)*
and a for-loop in normal programming, you must always keep in mind that
$(..)*
is a loop
at compile-time
.
You can't use
$t
except inside of a surrounding
$(..)*
— otherwise, which
$t
would you be referring to?
The pattern inside the
$(..)*
can truly be anything, for example if we had made it
$($t:ty,)*
we would be defining a comma-separated list instead of whitespace-separated, because the pattern now demands a trailing comma after each term.
Multiple patterns
I mentioned above that Rust macros can have multiple patterns. Let's make a trivial example.
Rust iterators have a method called
zip
that takes two iterators, and fuses them into a single iterator that returns 2-tuples of their elements.
For example:
let
xs
=
[
1
,
2
,
3
]
;
let
ys
=
[
4
,
5
,
6
]
;
for
(
x
,
y
)
in
xs.
zip
(
ys
)
{
println!
(
"
{x}
{y}
"
)
;
}
This will print
1 4
then
2 5
then
3 6
. But sometimes you want to zip
three
iterators and get 3-tuples. Or
four
iterators and get 4-tuples. You can do this a bit hackily like:
for ((x, y), z) in xs.zip(ys).zip(zs) {
It's zipping the 2-tuple result of the first zip with another iterator to get a 2-tuple whose first element is a 2-tuple. It's isomorphic to a 3-tuple, just uglier.
Because Rust doesn't allow you to easily abstract over different N-tuples (and does not have variadic functions in general), this is a great use-case for macros.
We want a macro we can invoke like:
for
(
x
,
y
,
z
)
in
zip!
(
xs
,
ys
,
zs
)
{
For any (reasonable) number of arguments.
We can define it like this:
macro_rules!
zip
{
(
$x0
:
expr
,
$x1
:
expr
)
=>
{
$x0
.
iter
(
)
.
zip
(
$x1
.
iter
(
)
)
}
;
(
$x0
:
expr
,
$x1
:
expr
,
$x2
:
expr
)
=>
{
$x0
.
iter
(
)
.
zip
(
$x1
.
iter
(
)
)
.
zip
(
$x2
.
iter
(
)
)
.
map
(
|
(
(
a
,
b
)
,
c
)
|
(
a
,
b
,
c
)
)
}
;
(
$x0
:
expr
,
$x1
:
expr
,
$x2
:
expr
,
$x3
:
expr
)
=>
{
$x0
.
iter
(
)
.
zip
(
$x1
.
iter
(
)
)
.
zip
(
$x2
.
iter
(
)
)
.
zip
(
$x3
.
iter
(
)
)
.
map
(
|
(
((
a
,
b
)
,
c
)
,
d)
|
(
a
,
b
,
c
,
d
)
)
}
;
...
}
Here we've defined up to 4-tuples, but you can go as far as you want. We'll look at how to improve and generalize this implementation later with recursive macros, but first, a few notes:
Note the semicolons at the end of each pattern, this is just some required syntax that isn't required in the single-pattern case
The compile checks for a pattern match in sequential order. Order doesn't matter for this case, since all the patterns are mutually exclusive, but order will matter for patterns where you have a catch-all case at the bottom.
Recursion
Macros can call themselves or other macros recursively. This is an
extremely
powerful ability. It actually allows the macro language to be
Turing complete
. Let's dip our toes into the power by implementing a macro that computes the
Collatz number
for a value at compile time.
If you aren't familiar, the Collatz process is: take any number
N
, if it's even, return
N/2
, if odd,
3N+1
— repeat until you get to 1. The number of steps this takes is
N
's Collatz number.
In normal code, it looks like:
fn
collatz
(
n
:
u64
)
->
u64
{
if
n
=
=
1
{
1
}
else
if
n
%
2
=
=
0
{
1
+
collatz
(
n
/
2
)
}
else
{
1
+
collatz
(
3
*
n
+
1
)
}
}
This is all kind of academic since Rust has compile time
const
functions, so we could actually just declare the above function
const
and call it at compile time, but let's not let pragmatism get in the way of fun.
Pattern-oriented macros like Rust are interesting because you can't do dynamic
evaluation
at compile time. So you can't do
math
on normal programming integer literals. For that reason, we'll represent the number N as just N arbitrary tokens — we'll use an
x
token, but it could be any token — a semicolon, a comma, a period, the word
foo
, whatever.
macro_rules!
collatz
{
//
Base case
(
$a
:
tt
)
=>
{
1
}
;
//
Even number case
(
$
(
$a
:tt
$b
:tt
)
*
)
=>
{
1
+
collatz!
(
$
(
$a
)
*
)
}
;
//
Catch-all, i.e. odd number case
(
$
(
$a
:tt
)
*
)
=>
{
1
+
collatz!
(
$
(
$a
)
*
$
(
$a
)
*
$
(
$a
)
*
x
)
}
;
}
Let's break it down.
The base case matches a single token, i.e. our representation of the number 1. That has a Collatz number of 1.
The next case matches an even number of tokens with a repetition pattern that contains 2 tokens as the inner pattern. So it can only match inputs that have a multiple of 2 tokens, i.e. even numbers of tokens. We divide the number of tokens by 2 in the recursive step by just emitting 1 of the 2 inner tokens.
We could have defined the final case like
$a:tt $($b:tt $c:tt)*
for a more proper, discrete mathematics definition of odd numbers, i.e. any number that can be represented by
2N+1
, but since we have already covered the base case and even case, we can be sloppier with a simple catch-all rule that matches any number of tokens.
We multiply it by 3 by just expanding all the inputs 3 times, then adding a final
x
onto the end.
If you do
let x = collatz!(x x x x x x x x x)
, i.e. the 9th Collatz number,
x
will be equal to 20. If you're in VSCode, you can right-click the macro invocation, click
Command Palette
then
Expand Macro Recursively
to see what final code the macro actually expands to. This feature is
incredibly useful
for debugging.
In this case, the code expands to
let x = 1 + 1 + 1 + … + 1
with 20 ones — not very interesting, but neat that we can do it!
Note: the
tt
type we use here means "token tree" and it is the most general token type that is a superset of all other token types. In practice, you mainly use it when you don't care to enforce a more specific type, such as throwaway tokens here, or when you maintain a queue of unprocessed tokens as we'll see below.
Advanced recursion: Token Munching
We can apply our recursion skills to an even more general form of computation. We process the input tokens just 1 (or a few) at a time, and then recurse to process the rest.
To illustrate, let's make a macro that converts any number of binary digits to a mathematical expression that evaluates to the binary number. i.e.
1 0 1 1
evaluates to some expression that equals 11.
This is
very
easy if the tokens are fed to us backwards. The fact that our numeral system is big-endian is a constant source of headaches.
Here's what it would look like if we got the tokens backwards:
macro_rules!
binary
{
(
)
=>
{
0
}
;
(
1
$
(
$rest
:tt
)
*
)
=>
{
1
+
2
*
binary!
(
$
(
$rest
)
*
)
}
;
(
0
$
(
$rest
:tt
)
*
)
=>
{
2
*
binary!
(
$
(
$rest
)
*
)
}
;
}
You can see why this method is called
token munching
. We munch off 1 token from the stream at a time, and process the rest of the stream recursively.
If we expand the macro for the input
1 1 0 1
(i.e.
1 0 1 1
backwards), we see it expands to
(2 * (2 * (2 * (2 * 0 + 1)) + 1) + 1)
which equals 11 as expected.
This method is just the macro implementation of this code:
let
mut
result
=
0
;
for
c
in
s.
chars
(
)
.
rev
(
)
{
result
*
=
2
;
if
c
=
=
'
1
'
{
result
+
=
1
;
}
}
But how to parse in the normal direction? Without having the user put the digits in backwards for us? This is trickier! Because you don't know the total value of the leftmost digit without knowing at least how many digits come to the right of it. If you're parsing 123 and you see the first 1, you don't know if it's 1, 10, 100, 1000, etc without knowing how many digits are to the right of it.
Whereas parsing from right to left, you can just keep recursively multiplying by 10. We did the same thing in binary, but multiplying by 2.
So how to resolve this? There are a lot of ways. Let's just cover a bunch, all of which will add tools to our macro toolkit and demonstrate the flexibility of macros.
Algebraic output
The base 10 number 284 can be represented as 2*10^2 + 8*10^1 + 4*10^0. That is, 2*100 + 8*10 + 4*1.
Similarly, the base 2 number 1011 can be represented as 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0, i.e. 8 + 0 + 2 + 1 = 11.
But how to implement this? We need to know the index of each digit, i.e. how many digits are to the right of it. Here's the trick:
macro_rules!
count_digits
{
(
)
=>
{
0
}
;
(
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
1
+
count_digits!
(
$
(
$rest
)
*
)
}
;
}
This macro will return an expression that equals the number of tokens put into it. So now we can implement:
macro_rules!
binary
{
(
)
=>
{
0
}
;
(
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
$x
*
2
u64
.
pow
(
count_digits!
(
$
(
$rest
)
*
)
)
+
binary!
(
$
(
$rest
)
*
)
}
;
}
For the input
1 0 1 1
, the
Expand Macro Recursively
feature outputs:
1
*
2
usize
.
pow
(
1
+
1
+
1
+
0
)
+
1
*
2
usize
.
pow
(
1
+
1
+
0
)
+
0
*
2
usize
.
pow
(
1
+
0
)
+
1
*
2
usize
.
pow
(
0
)
+
0
And this evaluates to the expected value of 11. If you do implement a macro in production that uses some of these tricks, don't worry about math like this — the compiler will optimize it all away.
Reverse, then process
If we need the tokens in reverse order for the original solution to work, why not just reverse them and then do the initial solution?
It's simple enough to make a macro that reverses its input:
macro_rules!
reverse
{
(
)
=>
{
}
;
(
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
reverse!
(
$
(
$rest
)
*
)
$x
}
;
}
The base case does nothing, the general case peels off the first token and moves it to the end of the reversed tokens. Invoking
reverse!(1 a 2 foo)
expands to
foo 2 a 1
.
But how to pass these tokens into our original
binary
macro? You might think we just do
binary!(reverse!(1 0 1 1))
. Unfortunately, macros are not like expressions that evaluate from innermost out. Macros operate on the tokens they are given.
In this case, all that happens is the tokens
['reverse', '!', '(', '1', '0', '1', '1', ')']
are sent into
binary
. And we just get a compile error saying that
binary
doesn't have any patterns that match (since it only expects 1s and 0s, not words like 'reverse').
There are a lot of reasons why you
want
macros to behave this way, but it's getting in our way right now! How to overcome this limitation? What we really need is a form of memory to build up a list of reversed tokens in. What memory do we have in macros? It's tokens all the way down.
It's hard to incrementally reveal the trick on how to implement memory in a sane way, so I'll just jump right to the solution and explain afterwards:
macro_rules!
binary
{
(
[]
)
=>
{
0
}
;
(
[1
$
(
$reversed
:tt
)
*
]
)
=>
{
1
+
binary!
(
[
$
(
$reversed
)
*
]
)
*
2
}
;
(
[0
$
(
$reversed
:tt
)
*
]
)
=>
{
binary!
(
[
$
(
$reversed
)
*
]
)
*
2
}
;
(
[
$
(
$reversed
:tt
)
*
]
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
binary!
(
[
$x
$
(
$reversed
)
*
]
$
(
$rest
)
*
)
}
;
(
$
(
$rest
:tt
)
*
)
=>
{
binary!
(
[
]
$
(
$rest
)
*
)
}
;
}
What's going on here? What are the
[ ]
brackets for? We store a new, reversed list of tokens inside the
[ ]
. We surround it by
[ ]
to give some structure to pattern-match on. If we didn't have the
[ ]
, it would just be a soup of tokens with no organization.
So on the initial call, none of the
[ ]
patterns match, because the input is all 1s and 0s. So we fall through to the last case that matches everything. All we do in that case is recursively call ourselves with some empty
[ ]
brackets followed by all the tokens.
The top 3 cases only match if there are no tokens after the
[ ]
containing our reversed tokens — i.e. they only match if we have consumed the input which we're storing at the right end of the invocation. These top 3 cases are just our original
binary!
macro we wrote above — munching 1s and 0s, doing 2N and 2N+1, until empty.
It's the 4th case that's new — the one where we are actually reversing the list. In this case we store the first token of the input into
$x
and the rest into
$rest
. We place
$x
at the front of
$reversed
inside the square brackets, and recurse on
$rest
— eventually we'll process all of
$rest
and start converting the binary in the first 3 cases.
It may be helpful to do an example manually. Let's do
1 1 0
. The expansion, step by step, will be:
binary!
(
1
1
0
)
binary!
(
[
]
1
1
0
)
binary!
(
[
1
]
1
0
)
binary!
(
[
1
1
]
0
)
binary!
(
[
0
1
1
]
)
(
binary!
(
[
1
1
]
)
*
2
)
(
(
binary!
(
[
1
]
)
*
2
+
1
)
*
2
)
(
(
(
binary!
(
[
]
)
*
2
+
1
)
*
2
+
1
)
*
2
)
(
(
(
0
*
2
+
1
)
*
2
+
1
)
*
2
)
I've added the parentheses in the latter lines even though they aren't present in the macro — the macro technically doesn't need them because the results of macros are implicitly scoped to prevent some of the pitfall bugs we mentioned with C macros.
That is, if you have a macro that expands to
2+2
, and you do
3 * the_macro!()
, the result will be 12 instead of 8, i.e. 3*(2+2), not 3*2+2.
By the way, the
[ ]
is just a convention for holding these kinds of "memory" groups — you can use whatever delimiters you want.
With this one technique, we have basically unlocked a huge world of what's possible with macros. You can implement a Turing machine now if you wanted.
You can munch tokens from the input, store them in relevant
[ ]
groups as you go, and then once you've got all your pre-processing done, churn through the memory recursively until your problem is solved.
You just have to break down the problem to express it in terms of queues or sets that you build during the input consumption phase, and consume in the computation phase.
It's possible you need to break the problem down into multiple phases where you build up, consume, build up, consume. One common pattern if you need even more organization is to use meaningless pattern tags, e.g:
macro_rules!
example
{
(
@phase1 [...] [...]
)
=>
{
…
}
;
(
@phase2 [...]
)
=>
{
…
}
;
(
$
(
$all
:tt
)
*
)
=>
{
example!
(
@
phase1
[
]
[
]
$
(
$all
)
*
)
}
}
In this trivial little example, the initial invocation will hit the bottom-catch-all case, which just immediately sets up some empty memory containers and recurses, but sticks in the tokens
@phase1
.
There is nothing magic about these! They are just arbitrary symbols that make reasoning about what pattern you're matching obvious. You can only match patterns that also start with
@phase1
. So you can use arbitrary labels like this as another organization tool.
Reflection
Now we have the basics of "advanced macros" down. If you can understand everything above this paragraph, you can implement anything you imagine in a macro. The solutions may be
O(N^3)
, but it all happens at compile time! And your N is hopefully small.
All you have to do is break down the problem into sets and queues and use recursive macro invocations with tokens as memory.
In our whirlwind tour to the big idea, we skipped over some important intermediate techniques. Let's backtrack and cover those now in a haphazard fashion.
Random additional techniques
Full syntax guidance
Like
$(pattern)*
means to repeat the pattern 0-N times, you can use
$(pattern)+
to mean 1-N times. You can also use
$(pattern)?
to mean 0 or 1 times.
$(pattern),*
means comma separated values, e.g.
a,b,c
— note that there are only commas
between
values. This means the following invocation:
example!
(
1
,
2
,
3
,
)
Will not match, because of the trailing comma after the 3. The common way to work around this is something like
$(pattern),* *(,)?
which uses the
?
to allow for up to 1 trailing comma.
Personally, I just always use
$(pattern,)*
and
force
there to be a trailing comma, but all my macros are for personal consumption, not pretty public libraries.
All the pattern types I use on a regular basis are:
tt
- the most general pattern, a token tree — any single token
or
group of tokens surrounded by matching delimiters (
[]
()
{}
)
expr
— any expression, i.e. anything that could be in the blank in a
let x = ____
statement
ident
— any identifier, e.g.
foo
,
my_function
,
SomeStruct
ty
— any type, e.g.
u32
,
Vec<(u32, String)>
literal
— any literal, e.g.
123
,
"string literal"
,
true
Here's
the full list
if you need the rest, though.
Treating collections as single token trees
The definition of
tt
above enables a useful pattern. The
tt
pattern type can match any single token, but also many
tt
inside
delimiters such as
[ ]
.
This means if we are building up some collection that could be represented like
[$($x:tt)*]
, if we happen to have a phase of macro computation where we don't need to operate on this collection and just need to pass it along to the next recursive call, we can instead just refer to the whole unit as
$x:tt
which will match the
[ ]
and everything inside them.
E.g. consider this macro
macro_rules!
example
{
(
[
$
(
$x
:tt
)
*
] [
$
(
$y
:tt
)
*
]
$next
:
tt
$
(
$rest
:tt
)
*
)
=>
{
example!
(
[
$
(
$x
)
*
]
[
$next
$
(
$y
)
*
]
$
(
$rest
:
tt
)
*
)
}
…
}
We're peeling tokens off the input and putting them into the
$y
collection, but we're otherwise just passing
$x
through as-is. We can rewrite this to:
macro_rules!
example
{
(
$x
:
tt
[
$
(
$y
:tt
)
*
]
$next
:
tt
$
(
$rest
:tt
)
*
)
=>
{
example!
(
$x
[
$next
$
(
$y
)
*
]
$
(
$rest
:
tt
)
*
)
}
…
}
Because
tt
can match the whole
[ ]
and its contents.
Beware early-binding patterns
Some pattern types like
ty
can consume multiple tokens. For example:
macro_rules!
first
{
(
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
$x
}
;
}
If you call
first!(Vec<u32>)
, then
$x
will be the token
Vec
and
$rest
will be 3 separate tokens:
<
,
u32
, and
>
.
However
if we bind those tokens to a
ty
pattern at any point, they become "glued together" and can't be broken apart again. For example:
macro_rules!
first
{
(
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
stringify!
(
$x
)
}
;
}
macro_rules!
force_ty
{
(
$x
:
ty
)
=>
{
first!
(
$x
)
}
;
}
So
force_ty
just passes its argument on to
first
, but it binds the input with
ty
. And
force_ty!(Vec<u32>)
will expand to the full
Vec<u32>
, because all those tokens got parsed as a single type token.
So, sometimes you want this behavior, but other times it can be really confusing if you expect to be able to munch each individual token. In the latter case, you want to stick with the more general
tt
instead of
ty
. You can always turn sequences of
tt
into a
ty
later.
Implementing traits for tuples, hygienic variable creation
Most of the examples in this article are of contrived stuff you should never do. Don't abuse macros to do stupid stuff just because you can.
The main reason I would ever use a recursive macro is to implement a trait for every N-tuple up to some maximum N, e.g. 16. This is really useful, because Rust doesn't have variadic generics (i.e. allow you to be generic over N-tuples at the language level).
Suppose we had this trait:
trait
ConsistencyCheck
{
fn
check
(
&
self
)
;
}
All this trait does is some kind of self-check for some invariant properties. E.g.
BalancedBinaryTree
might implement this trait and the
check
method would verify that it's actually balanced. This kind of trait is useful for things like
property-based testing
.
So suppose we want to implement it for all tuples whose constituent members all implement
ConsistencyCheck
. The implementation will just call
check
on every member.
e.g. for 2-tuples:
impl
<
T0
:
ConsistencyCheck, T1
:
ConsistencyCheck
>
ConsistencyCheck
for
(
T0
,
T1
)
{
fn
check
(
&
self
)
{
let
(
x0
,
x1
)
=
self
;
x0.
check
(
)
;
x1.
check
(
)
;
}
}
You can see how we could pretty mechanically create these impls. Let's take a first stab at it:
macro_rules!
impl_check
{
(
$
(
$t
:tt
$x
:tt
)
*
)
=>
{
impl
<
$
(
$t
: ConsistencyCheck,
)
*
>
ConsistencyCheck
for
($(
$t
,)*)
{
fn
check
(
&
self
)
{
let
(
$
(
$x
,
)
*
)
=
self
;
$
(
$x
.
check
(
)
;
)
*
}
}
}
}
Now, invoking like
impl_check!(T0 x0 T1 x1)
will exactly reproduce our manual implementation above.
This is great, but it's still annoying to type:
impl_check!
(
T0
x0
T1
x1
)
;
impl_check!
(
T0
x0
T1
x1
T2
x2
)
;
impl_check!
(
T0
x0
T1
x1
T2
x2
T3
x3
)
;
impl_check!
(
T0
x0
T1
x1
T2
x2
T3
x3
T4
x4
)
;
…
For all 16 impls we want. But we notice that each line is a subset of the line before. Can we do some kind of peeling recursion thing? We sure can:
macro_rules!
impl_check
{
(
@peel
)
=>
{
}
;
(
@peel
$t
:
tt
$x
:
tt
$
(
$rest
:tt
)
*
)
=>
{
impl_check!
(
@
make
$
(
$rest
)
*
)
;
}
;
(
@make
$
(
$t
:tt
$x
:tt
)
*
)
=>
{
impl
<
$
(
$t
: ConsistencyCheck,
)
*
>
ConsistencyCheck
for
($(
$t
,)*)
{
fn
check
(
&
self
)
{
let
(
$
(
$x
,
)
*
)
=
self
;
$
(
$x
.
check
(
)
;
)
*
}
}
impl_check!
(
@
peel
$
(
$t
$x
)
*
)
;
}
;
(
$
(
$t
:ident
$x
:ident
)
*
)
=>
{
impl_check!
(
@
make
$
(
$t
$x
)
*
)
;
}
;
}
So this macro has two @-labeled patterns:
@peel
and
@make
. What happens is
make
spits out the impl for
all
the tokens it receives. Then it recurses into
peel
, which either terminates if we're out of tokens, or strips off the first pair of
T x
and recurses into
make
with the rest.
So if you call
impl_check!(T0 x0 T1 x1 … T15 x15)
, this macro will spit out every tuple impl from 0 to 16.
It would be nice if we didn't need to pass
T0 x0 T1 x1…
though — it's redundant to specify 2 things for each 1 impl. It'd be nicer if we could just do
impl_check!(T0 T1 T2 T3…)
.
But what would be our
$x
in the line
let ($($x,)*) = self
, where we unpack the tuple into its constituent fields?
Thanks to Rust's hygienic macros, we can just conjure an identifier out of nowhere and even if we reuse it, it won't collide so long as it's in a different macro scope. Let me demonstrate:
macro_rules!
impl_check
{
(
@peel []
)
=>
{
}
;
(
@peel [$_:tt
$
(
$rest
:tt
)
*
]
)
=>
{
impl_check!
(
@
make
[
$
(
$rest
)
*
]
)
;
}
;
(
@make [
$
(
[
$T
:ident
$x
:ident]
)
*
]
)
=>
{
impl
<
$
(
$T
: ConsistencyCheck,
)
*
>
ConsistencyCheck
for
($(
$T
,)*)
{
fn
check
(
&
self
)
{
let
(
$
(
$x
,
)
*
)
=
self
;
$
(
$x
.
check
(
)
;
)
*
}
}
impl_check!
(
@
peel
[
$
(
[
$T
$x
]
)
*
]
)
;
}
;
(
@make [
$
(
$pair
:tt
)
*
]
$T
:
ident
$
(
$rest
:tt
)
*
)
=>
{
impl_check!
(
@
make
[
$
(
$pair
)
*
[
$T
x
]
]
$
(
$rest
)
*
)
;
}
;
(
$
(
$T
:ident
)
*
)
=>
{
impl_check!
(
@
make
[
]
$
(
$T
)
*
)
;
}
;
}
In this implementation, we have a few more things going on. We have a consume-input phase, and then a construction phase. During the input consumption phase, we read a single token
$T
off the input. Then we append that token
and
the variable
x
to our queue.
We notably enclose this pair in a
[ ]
which enables us to treat all the other pairs in the queue as a single token for convenience. This means when we match on the pair in the upper
make
, we need to include
[ ]
in the inner pattern.
To walk through the expansion of this macro for the first 3 tuples:
impl_check!
(
T0
T1
T2
)
;
impl_check!
(
@
make
[
]
T0
T1
T2
)
impl_check!
(
@
make
[
[
T0
x
]
]
T1
T2
)
impl_check!
(
@
make
[
[
T0
x
]
[
T1
x
]
]
T2
)
impl_check!
(
@
make
[
[
T0
x
]
[
T1
x
]
[
T2
x
]
]
)
Now we've consumed all the input and we start producing impls and peeling. But wait, what's going on with the variable names? They are all
x
! But because they were created in different invocation scopes, they are actually all "different". You can imagine them actually being named
x0
,
x1
, etc. This is really convenient when we need to conjure a variable name for each item in a list!
Capturing local variables
Rust macros are hygienic, which means they cannot mutate variables that are not in their scope.
For example, this code:
macro_rules!
foo
{
(
)
=>
{
let
x
=
123
;
}
}
fn
main
(
)
{
let
x
=
555
;
foo!
(
)
;
println!
(
"
{x}
"
)
;
}
Will still print
555
. The macro did not overwrite the value of
x
. The macro can't see the
x
in
main
scope. The
x
it creates is in a different namespace — you can think of it as if it's named
x2
or something.
However
if we were to rewrite the code like this:
fn
main
(
)
{
let
mut
x
=
555
;
macro_rules!
foo
{
(
)
=>
{
x
=
123
;
}
}
foo!
(
)
;
println!
(
"
{x}
"
)
;
}
Now
, we can touch
x
. This will print
123
. Because
foo
is defined in a scope that has access to
x
. It "captures"
x
.
This ability can be really useful when you have a function that does the same mutations repeatedly. For example, consider this code:
let
mut
strikes
=
0
;
macro_rules!
strike_if
{
(
$condition
:
expr
)
=>
{
if
$condition
{
strikes
+
=
1
;
if
strikes
=
=
3
{
return
Err
(
"
Too many strikes
"
)
;
}
}
}
}
strike_if!
(
age
<
18
)
;
strike_if!
(
name.
starts_with
(
"
W
"
)
)
;
strike_if!
(
name.
ends_with
(
"
y
"
)
)
;
strike_if!
(
accent
=
=
"
Pittsburgh
"
)
;
strike_if!
(
age
>
120
)
;
Rather than repeating the
strike
incrementing logic, condition checking, and early-return many times, we let the macro repeat it for us. The code is the same as if we had written 5 if-statements, 5 increments, 5 early returns, etc. But much more tidy.
Note how the macro captures the scope of
strikes
, so it is allowed to increment it! If the macro were defined
above
the
let mut strikes = 0
line, it would not have access, or if it was defined outside of this function, etc.
Conclusion
This post contains most of the tricks needed to become a macro master.
However
, with great power comes great responsibility. If you work on a team, your team will hate you if you make macro monstrosities.
The most complicated macro in this post I would recommend actually doing is the one where we implement a trait for all the N-tuples. You put a nice comment explaining how it works above it, and it's not too bad.
Something I learned after getting really good at macros is that a lot of the time, you can take the code you want to use a macro to deduplicate, and instead hide that logic behind a trait interface, and then use a simpler macro to help implement that trait for the relevant types.
To give a concrete example, I once worked on a codebase that defined a custom
RPC
format. Think like an extension of HTTP that has weird verbs and custom headers.
A request might look something like
COMPUTECHECKSUM filename:"foo.txt" timeout_ms:123
There were a few dozen of these requests, they all accepted different headers, etc. I thought I'd be cute and define a macro that was invoked like:
make_request_handler!
(
COMPUTECHECKSUM
filename
:
str
timeout_ms
:
u64
;
ANOTHERREQUEST
header
:
bool
names
:
Vec
<
String
>
;
…
)
;
And that macro created the entire request parser, created a struct for each request (e.g.
ComputeChecksumRequest
with the
filename
and
timeout_ms
fields), a dispatcher, etc.
That macro was a horrific dumpster fire implementation! It built up so many datastructures and craziness while munching those tokens. I feel awful for making anyone ever read that thing. But that's the kind of mistake you make when you lack experience! Upwards and onwards.
What I realized years later — and did go back and update the code — is I could break up the different bits into different, smaller, more manageable macros and traits.
For instance, you could define a common trait like:
trait
Request
{
const
VERB
:
&
str
;
fn
parse
(
s
:
&
str
)
->
Result
<
Self
, Error
>
;
fn
serve
(
self
)
;
}
Then just make
normal Rust structs
for all your requests, e.g.
struct ComputeChecksumRequest
with their fields, but then use a macro to automatically implement the
Request
trait.
Then make a different macro that takes a bunch of type names that all implement the
Request
trait, and that macro spits out just the dispatcher.
Etc. Just break it up into a bunch of manageable pieces. Keep at much of the logic in normal Rust code. Only go into macro-land to deduplicate truly shared logic. This is a ton more manageable than mega-macros!
This post does not cover procedural macros, which are even more powerful. The macros in this post are called
declarative
macros. Declarative macros are basically like a simple token-shunting Lisp executed at compile time.
Procedural macros are full-on Rust code that outputs more Rust code. They are much more powerful — you can do arbitrary Rust computations at compile time — but also a ton more complicated.
Libraries like
serde
use procedural macros to automatically implement serialization for rust structs, and web frameworks like
rocket
use procedural macros for setting up webserver path dispatch. We'll save that article for another day!
If there is anything in this article that's confusing and could be clarified, email me and I'll update it. Happy macroing!
