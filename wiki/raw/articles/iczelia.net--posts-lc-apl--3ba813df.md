---
title: "Journey to the Center of the Lambda Calculus"
url: "https://iczelia.net/posts/lc-apl/"
fetched_at: 2026-05-05T07:01:20.980025+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Journey to the Center of the Lambda Calculus

Source: https://iczelia.net/posts/lc-apl/

Introduction
⌗
λ calculus is a system for expressing computation, terms of which are built using the following rules:
Abstraction:
λx. X
- an anonymous function definition.
Application:
(X Y)
- applying a function
X
to the argument
Y
.
Variables:
x
- a bound or free reference.
The following operations are commonly performed on λ terms:
α conversion:
λx. A[x] → λy. A[y]
(renaming bound variables in an expression).
β reduction:
((λx. A[x]) B) → A[x := B]
(substitution).
η conversion:
f → λx. (f x)
(adding abstraction).
η reduction:
λx. (f x) → f
(removing abstraction).
Elementary examples
⌗
Consider the following sequence of operations aiming at providing the
normal form
of the initial term:
Some terms do not have a normal form. For example, the term
Ω = (λx.x x) (λx.x x)
can be β-reduced infinitely.
Preliminary considerations
⌗
I started implementing the λ-calculus evaluator with the symbol table. The symbol table could contain many useful pre-defined terms, but for the purposes of this article, I will limit it to Church terms for
true
and
false
. Other terms could be easily added.
I begin my implementation with some variable shuffling to ensure that the default symbol table is loaded if an alternative has not been supplied. I also reset the values of system variables
⎕IO
and
⎕ML
:
The next step is defining functions to insert and remove a value from the symbol table. Insertion is trivial:
Removing entries from the symbol table involves finding the index of the entry and then, using
↑
and
↓
, ignoring the removed column when reassigning the table:
I define a few helper functions. Raising an error and hashing an array:
The array hash method uses the I-beam 220 (to serialise the array to a signed byte array), the array is turned into an unsigned array to improve the characteristics of the hash function. The hash holds an accumulator, to which the product of the next input and a small prime number (31) is added. The operation is performed modulo 1e10 to avoid overflows.
Next, I define a vector of standalone single character tokens that will be consumed by the lexer.
To facilitate α conversion, I create a helper function to append a subscript index to a given variable:
Lexical analysis
⌗
Lexical analysis of λ calculus terms is remarkably simple. The only lexemes that need to be recognised are the standalone single character tokens described above, whitespace and line comments (to be ignored) and identifiers. As a recursive function, the lexer begins with a check for the input length and the single character token matcher:
Then, whitespace and line comments are ignored (terminated by the ASCII code 10 or end of the input):
The only remaining token type that needs to be recognised is the identifier. Define the characters that are allowed inside of an identifier:
Then, I compute the bitmask that decides whether individual characters in the input stream are valid identifier characters and count leading ones to determine the length of the identifier. If the identifier has length 0, an unexpected token has been observed.
Syntactic analysis
⌗
Begin the recursive descent parser code by defining useful abbreviations for single-character tokens:
If the input is in the form
ID = ...
, process a binding. Otherwise, read a term:
A binding simply processes the term following the aforementioned token sequence. The binding function alters the symbol table approperiately:
If the term begins with a λ sign, the term is an abstraction. Otherwise, the input is a sequence of one or more applications of atoms to each other.
An abstraction accepts the token stream that starts with a list of identifiers separated with a dot from the abstraction’s body (a term). Multiple arguments in a lambda definition are converted to a cascading single argument lambda function, i.e.
(λx y z. z) → (λx (λy (λz. z)))
.
Finally, an atom is defined either as a parenthesised term, a variable reference or another lambda function.
Abstract syntax trees are trivially turned into a natural notation string as follows:
δ expansion
⌗
δ expansion is applied by the evaluator after the parsing step to expand the underlying definitions of variables bound in the symbol table. Start by defining a function that determines what to replace the variable with when walking the syntax tree. Extra precaution needs to be taken, since variables may be shadowed by abstractions:
Finally, tree traversal is performed. The recursive traversal function keeps an accumulator of shadowed variables in scope that can not be replaced.
Var
nodes are passed to
lk
,
App
nodes are recursed into,
Lam
nodes are recursed into and append the variable they bind to the accumulator.
α conversion
⌗
Start by defining a table that tracks the amount of times a name has appeared in different contexts. Define a function that performs table lookup and increments a desired entry. The table lookup function automatically appends the subscript suffix to the identifier.
Tree traversal is as trivial as previously demonstrated. Variables are delegated to
∆i
, application is being recursed into, abstractons trigger table increments.
β reduction
⌗
Variables are invariant under β reduction. Abstractions are recursed into.
When encountering an application, normal forms of the function and the argument are computed. If the function is not an abstraction, no operation is performed:
α conversion is performed to avoid name clashes:
At this point, the only operation left is replacing all instances of the name
2⊃an
with
bn
in
3⊃an
. A simple recursive approach follows, minding shadowing:
Wrapping up
⌗
To evaluate an expression from a string, it needs to be lexed and parsed first. If the parser encounters a binding, there is nothing left to evaluate, so the function should abort early. Otherwise, δ expansion is performed on the syntax tree and β reduction is repeatedly applied to the input. This is accomplished by the following code:
Shortly after this blog post was published, Nick Nickolov wrote a simple evaluator for simplified Lambda Calculus.
Make sure to check it out
.
The source code
⌗
The full source code to this article can be downloaded
from Github
.
The evaluator correctly handles edge cases:
