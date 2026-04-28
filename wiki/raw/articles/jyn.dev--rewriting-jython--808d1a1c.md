---
title: "Rewriting Jython"
url: "https://jyn.dev/rewriting-jython/"
fetched_at: 2026-04-28T07:02:51.996477+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Rewriting Jython

Source: https://jyn.dev/rewriting-jython/

Intro
Have you heard of Jython? It's a variant of Python written in Java instead of C;
it lets you use native Java classes in python code.
The most common use case is integration with large existing Java codebases:
You can reuse Java code and still get the readability and conciseness of python.
I was thinking about types in Python, particularly how it allows
primitive operators to be overridden (+-/*%). For those unfamiliar with Python classes,
check out my
previous post
;
essentially it uses methods like
__add__
,
__sub__
, etc. as interfaces.
This lets you do things like
>
>
>
[
4
]
+
[
3
]
[
4
,
3
]
>
>
>
[
4
]
*
3
[
4
,
4
,
4
]
which would throw nasty exceptions in most other languages.
Because python allows any type to be called with these methods, it's the
responsibility of the class implementing the interface to ensure type safety,
for example
42 - '2'
will throw
TypeError: unsupported operand type(s) for -: 'int' and 'str'
.
I thought to myself, this looks doable.
Reflections
Java has a rarely-used but very powerful
reflection API
.
This allows you to do anything from get the class of a variable at runtime
(and do different things depending on which class it is)
to get the methods and constructors of an unknown class.
My (primitive) implementation of Jython make heavy use of reflections to use the
builtin Java classes and avoiding writing an interpreter from scratch.
Since python doesn't enforce types, we won't either. That means we have to call
methods at runtime, without knowing the class of the variable.
Java lets you do this!
[//]: # Secondly, since we want to allow inheritance, we have to find the constructors at runtime.
[//]: # This
can be done
as well,
[//]: # but since we want the types to match, we have to iterate all the constructors until we find one that's compatible.
API
The current API is exactly one class,
NumberWrapper
, which does nothing more than
type promotion
(and demotion).
I'm currently working on a
ListWrapper
which would demonstrate the power of
duck typing more clearly.
Because this is a toy project (and because parsing is hard), I have not implemented
an interpreter; the sample usage would be
add(new NumberWrapper(5), new NumberWrapper(-.14))
.
The full code is available
here
.
Its output is as follows:
$ javac jython.java -Xlint:unchecked
$ java main
3.5
Note that despite the extensive use of duck typing there are no type warnings;
javac
emits warnings only for casts, not calls to the reflection API.
