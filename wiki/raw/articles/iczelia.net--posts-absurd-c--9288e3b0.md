---
title: "How absurd is C?"
url: "https://iczelia.net/posts/absurd-c/"
fetched_at: 2026-05-05T07:01:23.771607+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# How absurd is C?

Source: https://iczelia.net/posts/absurd-c/

Introduction
⌗
C is an
old
language. As we all know, old technology is more likely to accumulate large amounts of technical debt and questionable solutions (e.g. APL being the best example, in-browser JavaScript, C++, and the list goes on and on…). The language designers are forced to some degree to keep their language mostly backwards compatible, because it’s
too late
to make large amounts of breaking changes. If there is a language who nobody uses or it’s still reasonably young, the developers and/or the standard committee can “patch” all the issues with their idea without causing too much harm.
We all know that programmers, and especially the commercial sector, dislike rewriting and reorganising their code. C++ that brought some breaking changes over the years and introduced a lot of
new
functionality that
isn’t really
all that widely adapted
(it’s
really
surprising to see that Visual C++ manages to beat
all other compilers
in terms of language support for C++20). C++ committee
gave up on some things
,
added some new useless things
that
nobody uses
and called it a day. Some languages (like Java, and particularily, the JVM)
constantly
change
internally
and
externally
.
Let’s get back to our today’s special guest, though. For many reasons, C isn’t a language able can afford that.
Trigraph sequences are still supported (5.1.1.2 Translation phases 1.1. of ISO/IEC 9899:201x).
Most “new” features aid the compiler, not the programmer (strict aliasing rule,
restrict
).
As old and useless as it is,
auto
still works.
There’s a
ton
of existing C code. Changing it doesn’t look possible in the first place, so all the new extensions have to be optional to some degree.
The language lacks strictness, which is a double edged sword - in some cases, strictness would be nice, though.
Preprocessor. Everyone loves the preprocessor and the pleathora of issues with it.
Knowing some of the reasons
why
C itself can’t really change, let’s dive into some main selling points of C and see how they impact the language.
A fast, low-level language
⌗
Interfacing with the machine is fairly simple and C is decent at representing how
“the computer”
really works - pointers, most of the things are manual, the compiler can be “persuaded” to emit different assembly code. For instance, compilers at
-O1
or equivalents tend to emit assembly code (at least on x86) that maps to C in a really simple and obvious way. For all of these reasons, C can be used to build very fast software using contemporary, dumb compilers.
Portability
⌗
Put in perspective, C is very portable. While in theory other “system’s” languages tend to claim to be low level and portable, neither of them can provide us the same level of awesomeness C does. Assembly is architecture specific. While it can be optimised well for obscure CPUs that lack advanced address generation circuits (6502, Z80), giving it a
huge
upper hand against C, it’s much larger of a pain to write these manually. It’s not like we have a different choice between C and Assembly. As horrible as it is, LLVM will never support less common platforms - in fact, currently it supports only
6 architectures and 5 main operating systems
. Need a C compiler for an obscure platform? RedPower computers, Apple ][?
There
you go
. Z80, microcontrollers?
We’ve got that too
. GCC has been retargetted
to everything
and
works everywhere
. Neither modern C++ (problems with catching up to standards, a heavy standard & tricky to use in freestanding environments), Rust or Zig (in practice; mostly tied up to LLVM), nor Go (presence of a garbage collector and generally unusable for smaller devices) can contest that.
Used everywhere
⌗
There’s a
ton
of C software around. Pretty much
every
programmer knows basics of C. Either because they were forced to by university, or maybe by the fact that everyone considers C the lingua franca for computing. The most common operating systems are made in C, most of the embedded devices are programmed in C because it’s cheaper and simpler than writing assembly (alarm clocks, microwaves, coffee makers, TVs, radios, vending machines, cash registers). Looking at all the use cases of C and how ubiquitous it is, you might think that
“The Illuminati doesn’t run the world. C programmers do”
.
Cruel reality
⌗
You might ask - there
must
be a cost of all this, right? I’m
not
the person to blindly believe in nice things when it comes to programming, because most of these tend to have fairly serious drawbacks that we, the programmers, tend to ignore. As you might have guessed, that’s the case with C too.
A clarification on low-levelness
⌗
The C standard draws a line between
hosted
and
freestanding
implementations. Simply put, a
hosted
implementation provides the C program with a full, standard-compiliant C library. A
freestanding
environment provdies the C program with just a bunch of not very useful headers (
<stddef.h>
,
<stdint.h>
, among others). It’s obvious that a low level program can’t be truly portable in it’s entire “low levelness”.
Truly
low level C programs often depend on unspecified behavior, undefined behavior and implementation-defined behavior and, as the name suggests, it’s not that unreasonable to assume that these behaviors will change depending on the implementation and the target machine.
Because hardware differs,
some
degree of vagueness must be kept when it comes to the standard to allow the implementation vendors to provide a reasonably efficient compiler and a libc. Surprisingly or not, undefined, unspecified and implementation-defined behavior pops up in the C standard
at least
400 times
. If there’s so many behaviors to account for, can we reasonably assume that the programmers will account for these? Can we believe that just because the implementation-defined behavior has been exhibited by mine and my friend’s x86 computer, the code will run on a very different machine? Of course, this problem is well known. Architectures like x86, MIPS, PPC, ARM, etc.. have already been researched fairly well, the compiler vendors provide their own compiler extensions and a set of behaviors that are mostly uniform across all the platforms it supports, so other langauges don’t
really
have an upper hand over C here.
Portability
⌗
Writing code that is
strictly conforming
to the C standard borders with impossible. These are some of my favourite picks, starting with the integer overflow. The C standards committee seems believe in faeries and dragons in form of computers that use a weird signedness model.
If, within a translation unit, the same identifier appears with both internal and external linkage, the behavior is undefined.
– 6.2.2 Linkages of identifiers, §7, ISO/IEC 9899:201x
Any pointer type may be converted to an integer type. Except as previously specified, the result is implementation-defined. If the result cannot be represented in the integer type, the behavior is undefined. The result need not be in the range of values of any integer type.
– 6.3.2.3 Pointers, §6, ISO/IEC 9899:201x
If the characters
'
,
\
,
"
,
//
, or
/*
occur in the sequence between the
<
and
>
delimiters, the behavior is undefined. Similarly, if the characters
'
,
\
,
//
, or
/*
occur in the sequence   between the
"
delimiters, the behavior is undefined.
– 6.4.7 Header names, §3, ISO/IEC 9899:201x
This implies that:
A valid POSIX path can contain
//
, but if an
#include
directive uses it, it’s UB.
A valid Windows path can contain
\
and
will
contain it in a lot of cases, but if an
#include
directive uses it, it’s UB.
According to 6.10.2 of ISO/IEC 9899:201x,
“the character sequence in an
#include
preprocessing directive has to start with a letter”
, absolute paths or paths beginning with
./
or
../
are undefined behavior.
The evaluation order is unspecified, and this has more serious consequences that you’d think. Firstly, most functions in C aren’t pure (because it’s a spartan systems language, what did you expect?), so invoking them in an expression might produce undesirable effects. Secondly, it impacts optimisation. To quote the cc65 manual:
Since cc65 is not building an explicit expression tree when parsing an expression, constant subexpressions may not be detected and optimized properly if you don’t help. Look at this example:
#define OFFS 4
int i;
i = i + OFFS + 3;
The expression is parsed from left to right, that means, the compiler sees ‘i’, and puts it contents into the secondary register. Next is OFFS, which is constant. The compiler emits code to add a constant to the secondary register. Same thing again for the constant 3. So the code produced contains a fetch of ‘i’, two additions of constants, and a store (into ‘i’). Unfortunately, the compiler does not see, that “OFFS + 3” is a constant for itself, since it does its evaluation from left to right. There are some ways to help the compiler to recognize expression like this:
Write
i = OFFS + 3 + i;
. Since the first and second operand are constant, the compiler will evaluate them at compile time reducing the code to a fetch, one addition (secondary + constant) and one store.
Write
i = i + (OFFS + 3)
. When seeing the opening parenthesis, the compiler will start a new expression evaluation for the stuff in the braces, and since all operands in the subexpression are constant, it will detect this and reduce the code to one fetch, one addition and one store.
–
cc65 manual
The order and contiguity of storage allocated by successive calls to the calloc, malloc, and realloc functions
(is not defined)
.
– 7.22.3, ISO/IEC 9899:201x
More of these can be found in section J.3.2 of ISO/IEC 9899:201x.
Pointers
⌗
C has extremely strict memory semantics according to the standard. The entire concept of
pointer
isn’t even well defined within it. Let’s start with pointer comparisons.
Two pointers compare equal if and only if both are null pointers, both are pointers to the same object (including a pointer to an object and a subobject at its beginning) or function, both are pointers to one past the last element of the same array object, or one is a pointer to one past the end of one array object and the other is a pointer to the start of a different array object that happens to immediately follow the first array object in the address space.
– 6.5.9 §6 of the C11 standard
(note: in the C context, object is a region of data storage in the execution environment, the contents of which can represent values)
.
There’s a common misconception about this topic -
pointers have types
, which means that a pointer to a 32-bit variable’s lower word doesn’t necessarily have to compare equal with a pointer to it’s 32-bit higher word (even though
“Two pointers compare equal if and only if […], both are pointers to the same object”
) - because an
int32_t *
can’t point to a higher or lower word of an
int32_t
. Of course, if you were to break it down to two
int16_t
, then these would be two different objects.
Now, let’s look at pointer
inequality
:
When two pointers are compared, the result depends on the relative locations in the address space of the objects pointed to. If two pointers to object types both point to the same object, or both point one past the last element of the same array object, they compare equal. If the objects pointed to are members of the same aggregate object, pointers to structure members declared later compare greater than pointers to members declared earlier in the structure, and pointers to array elements with larger subscript values compare greater than pointers to elements of the same array with lower subscript values. All pointers to members of the same union object compare equal. If the expression P points to an element of an array object and the expression Q points to the last element of the same array object, the pointer expression Q+1 compares greater than P. In all other cases, the behavior is undefined.
– 6.5.8 §5 of the C11 standard
There’s also
this defect report
. It’s not really all that interesting,
except
these two fragments:
There can be more than one bit pattern that represents the same value. […] If two objects have identical bit-pattern representations and their types are the same they may still compare as unequal.
Interpreting it literally,
pointer equality can always return false if the operands are derived from distinct objects
. In fact, pointer comparison can in a lot of cases
just not work
. Now that we looked at (mostly) magic black box types, let’s look
into
the structures. Assuming there is a structure with two members,
&x.a
and
&x.b
, after doing arithmetics on these, they might not compare equal. In fact, the only thing we know about representation of structures in C is the fact that the members of them aren’t reordered under any circumstances.
The best conclusion from this section would be -
“C standard is horrendously vague and unreadable. Writing a fully standards-compiliant, nontrivial C program must be hard.”
Additional read: 6.5.6 §7,8 of the C11 standard (+/- operators). - not covered in this article
Compilers
⌗
Compilers, the devil’s kith and kin will always get in C programmer’s way. This is the approperiate moment to talk about how
poor
C metaprogramming and constant evaluation is.
Assume you want a lookup table that’s filled with some function. In languages that support metaprogramming and constant evaluation to a reasonable degree, you can
guarantee
that computations will
always
end up being done at the compile time. This isn’t the case with C.
There is no way to state your intent
. Need something precomputed? Nope. Want something inlined? No! There is
inline
,
__forceinline
and
__attribute__ (( always_inline ))
, but
no compiler actually respects these in all cases
. A
__forceinline
function might not even get inlined and the compiler won’t complain. Not to mention that the last two are a compiler extension.
Let’s think about the following code snippet:
It comes from GnuPG, file
mpi-pow.c
. When compiling with GCC, this code behaves as intended on an x86, but not on a PowerPC - it won’t generate an exception. Clang assumes that the divisor must be non-zero on any system, since otherwise the division is undefined and the programmer couldn’t have meant that. Combined with this assumption, the check
!msize
becomes always false, since msize cannot be both zero and non-zero at the same time. The compiler determines that the whole block of code is unreachable and removes it, so we don’t guard against
msize == 0
anymore.
A similar example comes from PostgreSQL:
There’s one flaw with this code that isn’t instantly obvious.
ereport
isn’t marked as
_Noreturn
, so the compiler thinks that the division will always execute. As a consequence, the compiler moves the division above the check (because it’s considered deadcode -
arg2
can’t be equal to zero if a line later we’re dividing something by it… because a programmer wouldn’t have made a “mistake”… right?
right?
),
causing division by zero
.
Postgresql people claims it’s a gcc bug, while gcc people says the code is incorrect.
Catch-22 is back alive.
Practical usage
⌗
I observed a correlation between language’s/tech’s & the ecosystem’s quality and how large the userbase of a language is. At first, these two concepts seem unrelated, but let me explain.
A large userbase means that a lot of people use a language or a technology.
If a lot of people use a language or a technology, more solutions depend on it, and more code is written with/using it. Examples: JavaScript, Java
The more existing code in a language exists, especially in the commercial sector, the more restricted the language/tech committee is (because nobody wants to rewrite their solutions). Examples: C++, C - although they apply to the stage below too.
The more restricted the language’s/tech’s committee is, the more technical debt accumulates in the language’s specification itself (because the committe is unable to remove old features that are a sign of bad design, and instead end up adding new features
or
stalling the development of the language - strategies of C++ and C respectively). Examples: APL.
The more technical debt a language accumulates, the less enjoyable it is to program, and the language loses it’s relevancy for new projects - instead, it becomes a language that is used mostly (or exclusively) for maintaining legacy systems. Examples: COBOL.
This cycle, of course, might take decades. But keep in mind that C is an
old
language that has advanced quite far into this progression. A good example of existing code slowing down language’s refinement and improvement is IBM blocking the removal of trigraphs and digraphs from C++. Trigraphs were
proposed for deprecation
in C++0x, which was released as C++11, but it didn’t make it through. It was tried
over
and
over
and
over
, but in the end,
trigraphs were finally removed from C++
with C++17.
Syntatic smells
⌗
The syntax is usually the least important part of a language. Because the syntatic “smells” of C stuck around, the following code compiles as valid C89:
Some of the features that this code uses have been deprecated (like implicit
int
; I don’t use the K&R declaration syntax here although it’s quite bad too). All of these are a matter of style and preferences, but the C syntax stands out quite a bit. Let’s start with declarations.
int a;
- a regular
int
variable
int * a;
- a pointer
int * a, b;
- a pointer
a
and an integer
b
int a, * b;
- an integer
a
and pointer
b
int a[10];
- an array
int * a[10];
- an array of pointers
int (* vec)[10];
- a pointer to array of
int
s
int ** a;
- a pointer to a pointer
void (*fp) (void);
- a pointer to a function returning
void
and taking no arguments
struct { char a; float b; } (*function) (int, int);
- a pointer to a function taking two
int
s and returning a structure consisting of a byte and a float
char (*(*x())[]) ()
- function returning pointer to array of pointers to function returning char
int const * const a; int const ** b; int * const * const c;
- const pointer to const int, a pointer to a pointer to a const int and a const pointer to a const pointer to an int (
yes, this is real
).
Digraphs and trigraphs. Enough said.
What now?
⌗
That’s a really good question. I hope that I managed to convey a few things:
New programming language projects will
always
be relevant.
Existing languages and technologies can improve, but only up until some point.
There’s no easy way to fix all the “flaws” with C, because they’re just a consequence of its strengths.
There (in 99% of the cases) are no solutions. Only tradeoffs. And your duty, as a programmer, is to pick a better tradeoff.
An article like this could be written on any language. Including your favourite one.
