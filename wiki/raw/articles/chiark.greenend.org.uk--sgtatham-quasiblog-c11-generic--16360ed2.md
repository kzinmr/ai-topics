---
title: "Workarounds for C11 _Generic"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/c11-generic/"
fetched_at: 2026-04-29T07:00:56.884994+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Workarounds for C11 _Generic

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/c11-generic/

Workarounds for C11
_Generic
[Simon Tatham, 2023-07-29]
Introduction
The C programming language has a limited form of type-generic
      programming, based on ‘selection expressions’ using the
      keyword
_Generic
. These expressions look a bit like
      a
switch
, but on types rather than values: based on
      the type of their first argument, they select one of the
      remaining arguments, each of which is of the form ‘type: output
      expression’.
Usually you put these in macro definitions, so that
      they can make the macro test the type of one of its parameters
      and do the right thing for more than one possible answer:
#define my_macro(x, y) _Generic(x,                \
    int            :
some expression
,             \
    double         :
some other expression
,       \
    struct Whatnot :
something else again
,        \
    default        :
fallback expression
)
You can include a
default
clause that matches all
      remaining types, as shown above. Or you can leave it out, so
      that your macro will generate a compile error rather than try to
      operate on a type it isn’t designed to handle.
_Generic
was introduced in the C11 revision of the
      standard. The previous revision, C99, had introduced one
      specific set of type-generic macros
      in
<tgmath.h>
(for selecting the right
      version of a maths function for the particular floating point
      type –
float
vs
double
, real vs
      complex). But it had provided no specification for the
      underlying system for making choices, so that programmers
      couldn’t reuse the same facility for similar cases of their own.
      C11 filled in this gap, by standardising
_Generic
,
      which can be used to implement
<tgmath.h>
and
      things like it.
Once you have a reusable type-generic facility in C, there
      are
lots
of things you can imagine using it for.
As a simple example, suppose you have a structure type of your
      own that stores a string in some kind of allocated buffer. You
      might want to write a ‘string length’ macro that automatically
      chooses between returning
strlen(x)
(if it’s an
      ordinary C string) or
x->length
(if it’s an
      instance of your buffer structure).
More complicated examples might involve having a macro that
      switches its output based on the types of
two
of its
      parameters, or one that accepts an open-ended set of types by
      providing a
default
clause. (In a following section
      I’ll show an example that’s the reverse of this ‘string length’
      one, in which we want to pull out a named field
      from
lots
of structure types, and make only one
      exception.)
Unfortunately, this kind of thing isn’t as easy as it looks!
      The specification of
_Generic
has a huge bug (from
      the point of view of someone wanting to use it for lots of
      different things). It doesn’t affect the original use case
      of
<tgmath.h>
, but it starts to cause
      problems with
most
of the more complicated use cases
      you might think of.
In this article, I describe the bug, and multiple possible
      workarounds. But none of them is perfect, and even after you’ve
      used the workarounds, the results still won’t be very good.
The big bug
Here’s the big problem with
_Generic
.
Depending on the type of the selection argument, one of the
      output expressions will be selected at compile time, and the
      rest will be thrown away completely, and generate no
      code.
But the discarded expressions still have to be
      semantically valid
– they have to get through all of
      the same checking the compiler would apply to any other C
      expression, including type-checking successfully.
For example, here’s how we might implement the ‘string length’
      macro mentioned in the previous section, which provides a
      uniform way to find the length of two different string types, by
      deciding whether to call the standard C
strlen
or
      look up a structure field:
#define string_length_broken(x) _Generic(x,        \
    const char *            : strlen(x),           \
    struct MyStringBuffer * : (x)->length)
This looks clear and simple. It might even have been one of the
      first kinds of idea you had, if you’d sat down and wondered
      “What useful things could I do with a spot of type-based
      selection in C?”
But it won’t work. As soon as you actually try calling this
      macro with a
const char *
parameter pointing to an
      ordinary C string, you’ll get a compile error, because the
      expression
x->length
is illegal, because the
      type
char
isn’t a structure type with
      a
length
field.
Of course, you
know
that! That’s
why
you
      wrote an alternative branch of the
_Generic
expression: in this case, where you
      knew
x->length
wouldn’t work, you wanted to
      use
strlen(x)
instead. But unfortunately, even
      though
_Generic
would end up
selecting
the
strlen
expression, it will still fail to
      compile because the
other
branch isn’t semantically
      valid.
This is likely to affect
almost any
use
      of
_Generic
that reuses the macro parameter inside
      any of the expressions being selected, because it’s so likely
      that the use of the parameter in one branch of the selection
      will become illegal if the parameter has the type from another
      branch. So it
severely
restricts what you can do
      with
_Generic
, at least if you do it in the obvious
      way.
It doesn’t just affect reusing the
same
macro
      parameter, either. Here’s a different example: suppose you have
      a macro with two parameters, and you want to switch on the types
      of both of them at once, with not all combinations of types
      legal. You’d expect that this would be possible by
      nesting
_Generic
s, and for each type of one
      argument, having a sub-switch on whatever types for the other
      argument go with it. For example:
#define switch_on_both_types(x,y) _Generic(x,                      \
    const char * : _Generic(y, int :
this
, const char * :
that
),   \
    struct Foo * : _Generic(y, int :
this
, struct Bar * :
that
))
This code is intended to accept two types for
      argument
x
, namely
const char *
and
struct Foo *
. For either type
      of
x
, it will accept an
int
for
      argument
y
, but it also wants to let you combine
      a
const char *x
with another
const char
      *y
, or a
struct Foo *x
with a
struct Bar
      *y
, but not
vice versa
.
But again, it doesn’t work – not even if the output expressions
      are as simple as possible and don’t mention
x
or
y
at all.
Why not? For the same reason again: a compile error
      in
either
branch is fatal, even if it’s the branch not
      selected. So, suppose I call this macro with types
struct
      Foo *
and
struct Bar *
, expecting the second
      branch of the outer
_Generic
to be selected. But
      the subsidiary
_Generic
in the
first
branch will cause a compile error, because that’s switching on
      the type of argument
y
, and
struct Bar
      *
isn’t in its list of acceptable types.
Thoughts on the failure
When this first happened to me, it was a complete surprise. I
      thought the wrong branch of the
_Generic
must have
      been selected by mistake. It took me a long time to
      even
think
of the possibility that the compile error
      from the unwanted branch was happening
even though
it
      wasn’t selected!
Even after I decided that that must be the answer, I couldn’t
      quite believe it. To my way of thinking, one of the
      main
reasons
you’d want to select at compile time
      between several alternative pieces of code was
because
not all of them would be legal, and you wanted to pick the one
      that was!
Whose bug is this?
Perhaps this was just a bug in the particular compiler I
      happened to try this with?
I don’t think so, because
every
compiler I’ve tried
      agrees that this is how it works. Unless you want to believe
      that multiple completely independent C compilers all managed to
      have an identical
enormous
bug, the only other option
      is that they did it on purpose, because they agree that this was
      the genuine intent of the standard.
But that seemed unlikely
too
, so I went and checked
      the standard myself.
It’s not quite as unambiguous as you’d like
      it to be. C11 §6.5.1 clause 3 says that the unselected
      expressions are not
evaluated
, meaning they do not
      cause any code to be executed at run time, but it doesn’t say
      whether they should still be checked at compile time for
      semantic validity.
But here’s the thing: nothing
else
in C has the
      syntactic form of an expression, without the requirement to be
      semantically valid. (Unlike C++, where it happens all the time
      in template-related contexts.) So if the unselected branches
      of
_Generic
didn’t
have to be valid, then
      they’d be the only kind of expression with that property in the
      whole of C, and so I’d expect the standard to call them out
      explicitly as an exception to the usual rule. It does not.
So, if all those compilers think the intent of the standard is
      that even the untaken branches of
_Generic
have to
      be semantically valid, then I can’t disagree with them. If I’m
      going to complain about anything, it has to be the standard
      itself!
How did this happen?
The C standards working group (WG14) doesn’t just publish the
      final standard. It also publishes records of the process leading
      to the standard: proposals, arguments for and against, minutes
      of meetings, etc. So you can at least try to find
      out
why
a decision was made a particular way, by
      looking in those documents.
According to
      the
original
      proposal
, the idea for
_Generic
originated in a
      GCC language extension feature – or rather, multiple
      features:
__typeof
takes an expression and gives you its
        type
__builtin_types_compatible_p
takes two type
        names and tells you if they’re compatible (returning a
        boolean).
__builtin_choose_expr
is like a compile-time
        version of the
?:
ternary operator: depending on
        its first argument, it returns either its second or third. But
        unlike
?:
, it requires the first argument to be a
        compile-time constant, so that the unselected branch is not
        emitted as code at all, and so that the two output arguments
        can have incompatible types.
The GCC
      manual
gives
      an example
of using these features together to implement
      type-based selection, by
      making
__builtin_choose_expr
’s controlling
      expression the result of
      a
__builtin_types_compatible_p
test which
      checks
__typeof(parameter)
against a known type
      (and then maybe chaining multiple such tests via their ‘else’
      operand).
WG14 apparently found that cumbersome (fair enough!), and
      instead provided a single syntax to do the whole job, adding the
      ability to give a whole list of type associations instead of
      just one.
So the next question is, did the WG introduce the actual bug?
      Or does GCC’s original
__builtin_choose_expr
also
      insist on semantic validity of both its potential output
      expressions?
The latter, it turns out – if you try to do type-based
      selection using GCC’s builtins, you find exactly the same problem:
#define demo(x) __builtin_choose_expr(                        \
    __builtin_types_compatible_p(__typeof(x), struct Foo *),  \
    (x)->field_of_struct_foo,                                 \
    -1)
Just as before, we’re trying to pull out a field from a
      particular structure type if we’re given one, and fall back to a
      default return value of −1 otherwise. But you see exactly the
      same problem if you evaluate, say,
demo(42)
:
test.c:5:8: error: invalid type argument of ‘->’ (have ‘int’)
    5 |     (x)->field_of_struct_foo,                                 \
      |        ^~
test.c:8:27: note: in expansion of macro ‘demo’
    8 | int thing(int f) { return demo(42); }
      |                           ^~~~
So GCC’s original design has the same limitation – WG14 didn’t
      introduce it.
The really curious thing is that I didn’t find
any
discussion in the WG14 proposal of the question I’m addressing
      here. I was expecting to find that they had carefully considered
      the question “Should
_Generic
require even its
      unselected output expressions to be semantically valid?”,
      weighed up the pros and cons, and decided the answer was yes
      (for some reason that I currently can’t imagine, but would have
      been very interested to find out). But instead,
      it
looks
as if nobody even considered it at all.
How was this not noticed?
There are a lot of things you might want to do
      with
_Generic
which are prevented by this design
      feature. But it
does
work for the one case it was
      originally meant for: selecting between a family of related
<math.h>
and
<complex.h>
functions, such
      as
sin()
,
sinf()
,
sinl()
,
csin()
,
csinf()
and
csinl()
, so that the user can just
      write
sin()
every time, and the compiler will
      figure it out for you.
This works because you only need to select between
      the
functions
, not the whole
function call
        expressions
. In other words, instead of writing this ...
#define dangerous(x) _Generic(x, \
    this_type : this_fn
(x)
, \
    that_type : that_fn
(x)
)
... you instead write this, which puts the call
      operation
outside
the
_Generic
, and the only
      thing inside it is function names:
#define safer(x) _Generic(x, \
    this_type : this_fn, \
    that_type : that_fn)
(x)
With the first form, the
x
you provide will be
      type-checked against
both
functions, and there will be a
      compile error if it isn’t compatible with either one. So
      if
this_fn
can’t take a value
      of
that_type
, or
vice versa
, then the macro
      won’t do its job.
But with the second form, the function name isn’t type-checked
      against its argument until
after
the
_Generic
has decided which function it is. And
      each branch of the
_Generic
is a semantically valid
      C expression by itself, regardless of the type
      of
x
, because it doesn’t mention
x
at
      all – it’s just a bare function name, fixed at compile time. So
      this version works.
(I suppose it’s
possible
that, in this mode of use,
      it’s mildly
useful
to have the compiler check all the
      possible output expressions, rather than only the selected one?
      If the output expressions are independent of the type-variable
      input that might make them illegal, then they
should
all be legal, and in that case, it’s better to detect a mistake
      in one as soon as possible, without having to wait until you
      actually exercise the faulty branch. For example, in this case,
      if you misspelled one of the possible function names, you’d get
      an error whether you’d tried to use that branch or not. But this
      still seems like a small consideration next to the huge number
      of useful things you could do if the feature worked the more
      permissive way. And, as I say in the previous section, I found
      no evidence that
_Generic
works this way on purpose
      for the sake of any specific advantage, including this one.)
Inline-functions workaround
In the previous section, I describe the one mode of use
      of
_Generic
that
isn’t
inconvenienced by
      the requirement for all the output expressions to be valid.
So an obvious workaround is:
write your own generic
        expressions in that form if you possibly can.
Then they
      should work, for the same reason
      that
<tgmath.h>
works.
For example, instead of this example from a previous section ...
#define string_length_broken(x) _Generic(x,        \
    const char *            : strlen(x),           \
    struct MyStringBuffer * : (x)->length)
... we could write this:
static inline size_t mystrbuf_len(struct MyStringBuffer *msb)
{
    return msb->length;
}

#define string_length_fixed(x) _Generic(x,         \
    const char *            : strlen,              \
    struct MyStringBuffer * : mystrbuf_len) (x)
This version of the string-length macro is just selecting a
      function name, in exactly the same way as
      the
<tgmath.h>
selector macros do. And the
      function isn’t applied to
x
until after
      the
_Generic
has finished selecting one of its
      branches and thrown the rest away. So it never matters
      that
strlen
can’t accept a
struct
      MyStringBuffer *
, or that the
mystrbuf_len
function I’ve defined here can’t accept a
const char
      *
. This version of the macro will never need them to.
It’s wordier than the first version, and (I think) less
      readable, because it’s less self-contained. But at least it
      works.
Cases where this doesn’t help
This inline-functions workaround only works in cases where
      every branch of the generic
can
be written as a
      function call. But there are lots of reasons why that might not
      be true.
One reason is if you want to do something non-trivial in
      the
default
clause of the generic expression. Then that
      clause has to match more than one input type, so you probably
      can’t write a C function that has a general enough type signature.
As I mentioned in the introduction, an example case of this is
      if you want to pull out a named structure field from an open-ended set of
different
structure types. You might do this in order
      to treat them all as different implementations of the same
      ‘interface’ or ‘trait’. Say, you might have lots of structure
      types contain a
struct Foo foo
field, and then have
      a macro that would take an object of any of those types and
      operate on
obj->foo
.
You don’t even need a
_Generic
to do that much.
      But suppose you also want the same macro to handle
struct
      Foo
itself
, for the case where a function is
      already operating on a
generic
instance of the trait
      rather than a specific type of implementing object?
So we’d like to write code along these lines, analogous to the
    ‘broken’ version of the previous
string_length
example:
#define foo_upcast_broken(x) _Generic(x,  \
    struct Foo * : (x),                   \
    default      : &(x)->foo)
which responds to the one special case of a
struct
        Foo
pointer by just returning the pointer itself, and in
      all
other
cases, assumes you’ve passed it the address of
      a structure containing a
struct Foo foo
, and extracts
      a pointer to that.
Of course, this won’t work, for the same reason
      that
string_length_broken
didn’t work: in the case
      where
x
has type
struct Foo *
,
      the
default
clause will turn out not to be semantically
      valid, because
struct Foo
doesn’t itself have a field
      of type
foo
.
(In this example, you could work around that in turn by
      just
adding
one: give
struct Foo
a dummy
      member called
foo
of any type you like, simply to
      make the default branch of this
_Generic
happy. But
      in a more complicated case, where the expression in the default
      branch also needed
x->foo
to have the
right
type, even that wouldn’t help.)
This workaround also doesn’t help with the other case shown
      above, of selecting based on two argument types by nesting a
      different
_Generic(y, ...)
within each branch of
      the outer
_Generic(x, ...)
. There’s no way to turn
      each of
those
generics into a function call.
Here are some other cases I’ve seen which would prevent you
      from converting one (or all) of your output expressions into a
      function call:
depending on the input type, the output expression might
          need to
not evaluate
a macro parameter (e.g. to
          avoid its side effects). Then the parameter must be included
          in the branches that
do
need it.
in low-level work, the output expression might need to select
        between things that
look
like function calls but are
        really magic compiler builtins, in which case the compiler
        won’t let you use their names by themselves in
        the
_Generic
, because a compiler builtin name is
        often not a valid expression by itself. So you have to write
        the parameters right next to the builtin name, i.e. right
        inside the
_Generic
.
in even lower-level work, the output expression might need
        to stringify one of the macro parameters and paste it into a
        GCC-style
asm
expression as an immediate operand
        to a machine instruction. Then the
asm
expression
        can’t be wrapped in a function.
I’m sure there are more cases I haven’t thought of. The point
      is: this inline-functions workaround is the best
      thing
if
you can do it, but there are lots of reasons
      you can’t always do it.
Type coercion using a secondary
_Generic
Here’s an alternative workaround which can work in cases where
      the inline functions approach doesn’t.
Within each output expression of the
      main
_Generic
, if you need to refer to a macro
      parameter whose type you’re switching on, you can force it to
      have a type appropriate to that particular output expression by
      means of wrapping it in a secondary instance
      of
_Generic
.
How do you force it to have an appropriate type? By checking if
      it already does have that type, and if not, replacing it
      completely with some completely made-up expression
      that
does
have the type you want.
The made-up alternative expression is selected to have the
      right
type
, so that the semantic checks on this branch
      of the
_Generic
won’t fail. It won’t have the
      right
value
at all – but that would only matter if this
      branch were
selected
. The idea is that the dummy
      wrong-value-of-the-right-type is only used in cases where the
      whole containing branch was going to be thrown away.
For example, here’s a macro you might use to generate an
      expression of type
struct MyStringBuffer *
, which
      matches the input expression if
that
is of that type, and
      otherwise makes something up:
void *dummy(void);

#define coerce_to_MyStringBuffer(x) _Generic(x,                    \
    struct MyStringBuffer * : (x),                                 \
    default                 : (struct MyStringBuffer *)dummy())
Using this coercion macro, we can fix the
original
attempt to implement our
string_length
macro, by
      modifying the dangerous
(x)->length
output
      expression to wrap the parameter
x
in our new
      coercion macro:
#define string_length_refixed(x) _Generic(x,                       \
    const char *            : strlen(x),                           \
    struct MyStringBuffer * : coerce_to_MyStringBuffer(x)->length)
This
version of the macro will still compile if
      you give it a
const char *
, because in the
      unselected output expression,
      the
coerce_to_MyStringBuffer()
macro call will
      deliver its dummy expression (calling the
dummy()
function and casting its output type), which is of a type
      that
can
validly take ‘
->length
’ after
      it. But once it’s passed its semantic checks, that expression is
      thrown away completely, so that it doesn’t matter that
      its
value
couldn’t possibly have been anything useful.
On the other hand, if you give this macro a
struct
        MyStringBuffer *
, then the coercion macro will act as a
      no-op, returning the same pointer it was passed. So when the
      second clause of the main
_Generic
is
selected, it will have a useful value in it.
If you’re reading this and you have even an ounce of instinct
      for defensive programming, this probably looks pretty dangerous
      to you! We’re relying here on two
      separate
_Generic
s making their choices the same
      way. Get it wrong, and we might accidentally emit code into the
      object file that
really
calls the
dummy()
function and casts its return type to something it was never
      meant to be.
My answer to that is: I haven’t yet mentioned
      what
dummy()
actually is. In fact, it’s nothing at
      all: it’s a non-existent function. It exists
only
as a
      declaration in whatever header file defines the code
      base’s
_Generic
macros. No
definition
of
      it exists in any translation unit.
Therefore, if the compiler emits an actual call to that
      function into any object file, the effect will be a link
      failure, when the function turns out not to be defined anywhere
      at link time. The only way the program can be compiled
      successfully is if
no
use of this generic macro ends up
      capable of actually calling
dummy()
at run time.
So it’s not as unsafe as all that! It is possible that a coding
      error in one of these
_Generic
s might mismatch the
      inner and outer expressions – but if so, a link failure will
      prevent the mistake from getting as far as executable code, let
      alone actually
being
executed.
Type tuples using a multidimensional array
One case where even
that
workaround doesn’t help is if
      you want to switch based on the types of two expressions at
      once.
Of course, if the sets of permitted types for the two
      expressions are independent – that is, expression
x
can have any of
these
types,
y
can have
      any of
those
types, and any of the former goes with any
      of the latter – then there’s no problem with this, and you can
      just nest a
_Generic
switch on the type
      of
y
inside each branch of the
      outer
_Generic
for
x
. But if there’s
      any type of
y
that goes with one type
      of
x
and not with another, then that won’t work, as
      we’ve already discussed above.
Neither of the previous workarounds will help. You can’t wrap
      the inner
_Generic
into an inline function, because
      inline functions can’t themselves be type-generic. And if you
      try to mimic the type-coercion approach, by giving each
      inner
_Generic
some kind of a default clause that
      prevents it from failing spuriously, then the same default
      clause will apply when it
is
the selected branch of the
      outer
_Generic
, and the effect is that you won’t
      get the compile failures you
did
want, when you
      actually gave your macro a pair of types that don’t go together.
What you
really
want, in this case, is not to have to
      nest two switches in the first place. You want to make a
      combined type that encapsulates the types of
both
your
      controlling arguments
x
and
y
, and
      write a single one-layer
_Generic
expression that
      switches on the set of acceptable
tuples
of types.
In some languages, you could just
do
that, because
      type tuples (or something like them) exist in the language
      already. If this were C++, for example, you can combine any two
      types into a single type by using them as parameters of a
      template – either one you make up yourself, or something
      pre-existing like
std::pair
or
std::tuple
. But then, if this were C++, you
      wouldn’t be trying to get
_Generic
to do something
      useful in the first place, because it wouldn’t exist, and even
      if it did, there are other ways!
In C, the problem is not that type tuples
don’t exist
.
      You could imagine, for example, representing a tuple of two
      types using the type of a function pointer taking two arguments
      with those types, e.g.
void (*)(int, const char *)
might be used to represent the type pair
(int, const char
      *)
. The problem is that you have no way
      to
construct
one of those out of the
      expressions
x,y
passed to your macro.
If you have any language extension available to help, then the
      problem becomes easier. With the GNU
      extension
__typeof
, for example, you could do this
      just fine:
#define type_tuple_switch(x, y) _Generic((void (*)(__typeof(x), __typeof(y)))NULL, \
    void (*)(int, int)        : "got two ints",                                    \
    void (*)(int, char *)     : "got an int and a string",                         \
    void (*)(char *, int)     : "got a string and an int")
Here, we’ve recovered the types of
x,y
via
__typeof
; made a function pointer type with those
      types as arguments; and cast
NULL
to that function
      pointer type for the sake of having an expression of that type to
      use as the first argument to
_Generic
. Then we can
      test pairs of acceptable types by making further
      function-pointer-shaped tuples.
But what if your code needs to compile in
standard
C,
      without benefit of any dialect-specific extension?
As in the previous section, you can work around the
      difficulties of
_Generic
by using yet
      another
_Generic
, because that’s the closest thing
      we
do
have in standard C to
__typeof
. We
      can’t make it output the actual
type
, but we can use it
      to test the type of an input argument and
      output
something
we can use when constructing another
      type.
Specifically: we can convert each input type into
      an
integer
, so that the problem of switching on a pair
      of types is reduced to switching on a pair of integers. Then we
      can wrap our integers back up into a thing
_Generic
can switch on by making a multidimensional array with those
      integers as dimensions.
This is the longest example yet, because we need three stages:
      an enumeration of type ids, a macro that returns the type id of
      an input, and finally, a switch on arrays with type ids as
      dimensions.
enum MyTypeId {
    MTI_NONE,    // avoid using 0 as a type id, because it’s illegal as an array dimension
    MTI_INT,
    MTI_CHAR_PTR,
    MTI_SOME_STRUCT,
};

#define MYTYPEID(x) _Generic(x,           \
    int               : MTI_INT,          \
    char *            : MTI_CHAR_PTR,     \
    struct SomeStruct : MTI_SOME_STRUCT)

#define type_tuple_switch(x, y) _Generic((int (*)[MYTYPEID(x)][MYTYPEID(y)])NULL,  \
    int (*)[MTI_INT][MTI_INT]      : "got two ints",                               \
    int (*)[MTI_INT][MTI_CHAR_PTR] : "got an int and a string",                    \
    int (*)[MTI_CHAR_PTR][MTI_INT] : "got a string and an int")
The enumeration and the
MYTYPEID
macro are
      reusable: if you have more than one macro that needs to switch
      on multiple types, you can use the same system of type ids for
      all of them, as long as you make an enum value for every type
      that
any
of them wants to use. (To demonstrate this,
      I’ve included a value in the example above which isn’t used
      in
type_tuple_switch
– we imagine that elsewhere in
      the same program is some other similar macro that
can
take an argument of type
struct SomeStruct
.)
In this example case, I’ve kept the output expressions simple:
      those don’t mention the arguments
x,y
at all. If
      they did, then it works fine to combine this workaround for the
      pair-based switch with the previous section’s workaround for
      referring to the arguments in the output expressions. As long as
      each output expression only coerces inputs to types that they
      would have to have
anyway
for that expression to be
      selected, the combination works fine.
Chaining one
_Generic
as the default of another
One annoying edge case in all of the above is: what if you want
      to select between lots of different integer types?
You could imagine wanting to do that in order to treat all the
      integer types
the same
(e.g. pass all of them to the
      one of your functions that accepts integers in general), or to
      treat them
differently
(e.g. return some value specific
      to an integer type, like the location of the high bit, or an
      appropriate
printf
format-string directive).
The problem with this in C is that you don’t reliably know
      which integer types are the
same
as each other. The
      basic
      types
short
,
int
,
long
and
long long
are all guaranteed to be distinct
      types, but which of those is the same as,
      say,
int32_t
? It could be either
      of
int
or
long
(in practice, and
      perhaps others in theory). Similarly,
int64_t
might
      very reasonably be an alias of
long
, or
      of
long long
.
This leads to a problem if you’re
      constructing
_Generic
expressions, because you’re not
      allowed to have two clauses specifying the
same
type. But
      you don’t know what types
are
the same time, so how do
      you avoid it?
#define MYTYPEID_INTEGER_EDITION(i) _Generic(i, \
    int     : MTI_INT,                          \
    long    : MTI_LONG,                         \
    int64_t : MTI_INT64_T)
This example macro tries to convert integer types into type
      ids, in the style of the previous section. It will work fine
      if
int64_t
is an alias for
long long
on the platform where you try to compile it. But
      if
int64_t
turns out to be an alias
      for
long
instead, you’ve got a compile error – two
      clauses of this
_Generic
specify the same type. And
      if you remove the
long
case and replace it with
      a
long long
case, now you’ll get a compile error on
      the
other
platform.
(Obviously, I’ve left out several of the
other
C
      integer types here. That’s just for the sake of keeping this
      example short.)
We can work around this annoyance in a similar way to the
      previous two workarounds I’ve shown: use
yet another
instance of
_Generic
to avoid the problems with the
      first one. In this case, we can chain together
      two
_Generic
s by their default clause, both
      switching on the type of the
same
expression:
#define MYTYPEID_INTEGER_EDITION(i)             \
_Generic(i,                                     \
    int       : MTI_INT,                        \
    long      : MTI_LONG,                       \
    long long : MTI_LONG_LONG,                  \
    default: _Generic(i,                        \
        int32_t : MTI_INT32_T,                  \
        int64_t : MTI_INT64_T,                  \
        default : MTI_NONE))
Now it doesn’t matter any more whether
int64_t
is
      an alias for
long
, because those two types don’t
      appear together in the
same
_Generic
: one
      is in the outer one, and the other is in the inner one. And
      if
int64_t
is an alias for
long long
instead, there’s still no problem, because
those
two
      don’t appear together. Generally, the idea is that I’ve put all
      the language’s
basic
integer types in one of the lists,
      and the
<stdint.h>
type aliases in the other,
      and as long as no two types in the
same
list collide,
      things should work.
However, a couple of things to note about this workaround:
Firstly,
not all the output expressions can be generated at
      all
, on a given platform. Suppose that our compiler’s
      headers define
int64_t
to be an alias
      for
long
. Then the macro above will never
      return
MTI_INT64_T
at all, because that branch of
      the inner
_Generic
will always have been pre-empted
      by the branch of the outer one that
      returns
MTI_LONG
. Conversely, on a different
      system, this macro might map an
int64_t
input
      to
MTI_LONG_LONG
.
(In fact, is there
any
integer type capable of getting
      through the non-default cases of the outer
_Generic
and reaching the inner one? Perhaps not! But writing it like this,
      we should cope even if there is.)
Secondly, note that even
      the
inner
_Generic
has a default clause.
      This isn’t optional: it’s necessary for the same reason as
      usual, namely that the inner
_Generic
as a whole
      will be checked for semantic validity
even if
one of
      the other branches of the outer
_Generic
is
      selected. So if any type handled by the
      outer
_Generic
is not also handled by the inner
      one, then you’ll get a compile error.
The simplest fix is to always return
something
from
      the expression as a whole. Here, we return the dummy
      value
MTI_NONE
, shown in the enum in the previous
      section. The idea would be that any attempt to use that value in
      an array-based type tuple would provoke a compile error in its
      own right, or even if not, it wouldn’t match any of the branches
      of a tuple-based
_Generic
you were writing.
Remaining problems
“Phew! Are we done yet?”
I’ve presented a variety of different workarounds for the
      various reasons why you might get unwanted compile errors when
      trying to do anything interesting with
_Generic
. Is
      there anything left that will
still
go wrong?
Unfortunately, yes. There are two problems left, and I’ve run
      out of workarounds.
Firstly: if you do all of this trickery with multiple
      nested
_Generic
expressions, and something goes
      wrong, the compiler error messages are
terrible
. If you
      define a macro that accepts three types, you’d like to see an
      error message saying something comprehensible like “Sorry, you
      gave
this
type and I wanted one of
these
.”
You can just about get that from a really simple use
      of
_Generic
: if an input type doesn’t match any
      clause then gcc’s or clang’s error message will tell you what
      the input type
was
, and will point at the source
      location of the generic expression that it didn’t match. You’ll
      still have to go through the source expression yourself to find
      out what types
would
have matched, but at least you
      know where to look for that.
But the more workarounds you add, the more the errors start
      talking about things in the workaround system and not things in
      the user’s actual code. For example, if you’re using the type-id
      system I’ve shown here, and it generates a type id that isn’t
      matched by a particular
_Generic
, the error message
      will tell you that the mismatching type is some nonsense
      multidimensional array type like
int (*)[5][2]
,
      which has no relation to the types you specified at the call
      site of your generic macro. Of course, we
had
to map
      the input types to opaque integers to make the system work at
      all – but a side effect is that those integers are now what you
      see in the error report.
The first duty of compile-time error checking is to only let
      code through if it’s right. The second is to tell the user
      something
useful
if it’s wrong. With all these
      workarounds, we’ve only managed to fulfill the first of those!
Secondly, the expansions of these macros become
enormous
.
A macro containing multiple workarounds of this kind will have
      to expand its parameters in lots of different places: at least
      one macro argument will need to appear in the controlling
      argument of each
_Generic
(inner or outer), and if
      the point of the workarounds was to let you use the macro
      argument again in the output expressions, then you’ll want to do
      that as well. It’s very easy to write a macro that expands its
      argument ten times.
This isn’t
dangerous
in correctness terms, which is
      the
usual
reason why people worry about multiply
      expanding macro parameters. In all the examples here, there’s no
      reason to expand any parameter in a way that will make it
      be
evaluated
twice (e.g. doubling its side effects).
      The controlling expression of
_Generic
is never
      evaluated, and at most one of its output expressions is. So you
      can perfectly well employ all the workarounds in this article,
      and still put at most one copy of the macro parameter in each
      output expression in a context where it will generate code. And
      only one of those output expressions will be evaluated, so you
      can easily arrange to get the expression’s side effects (if any)
      at most once.
But in some cases, even the multiple
expansion
can
      cause a problem. For example, suppose I’ve defined a macro
      that’s packed with complicated
_Generic
expressions, with workarounds everywhere. And then suppose
      someone innocently writes this in their source code:
int x = MY_MACRO(MY_MACRO(MY_MACRO(MY_MACRO(MY_MACRO(y)))));
Suppose the macro expands its parameter 10 times. Then the
      expansion of the innermost
MY_MACRO(y)
will still
      be reasonably small, because the text mentioned ten times is
      just the single identifier
y
. But the expansion of
      the next layer,
MY_MACRO(MY_MACRO(y))
, will repeat
      ten times the
entire innermost expansion
. And each of
      the next three layers will multiply
that
by another
      factor of ten.
The combined effect will be that the C preprocessor generates
      a
huge
amount of output, which the main C compiler has
      to painstakingly parse, store in an internal data structure,
      semantically validate, and then process to the point of deciding
      which branch of each
_Generic
to take. In the end,
      it will throw away nearly all of that huge amount of text, and
      emit just the single short expression that ended up being
      selected. But your compiler will go
very
slowly in the
      process – and it might even consume too much of the system’s
      memory, and crash, or start starving other processes of
      resources!
A user who knows that this is going on has an easy workaround,
      which is to avoid nesting expansions of macros that do this kind
      of trick. Instead, add extra intermediate variables, and use
      just a simple variable name in the next expansion:
int y1 = MY_MACRO(y);
int y2 = MY_MACRO(y1);
int y3 = MY_MACRO(y2);
int y4 = MY_MACRO(y3);
int x  = MY_MACRO(y4);
But not all users will be sympathetic to being told to do that!
Even the
intended
use of
_Generic
has
      this problem, to some extent. If you switch on your macro
      parameter to select one of a list of function names, and then
      write the parameter again after closing
      the
_Generic
, then you’ve expanded the parameter
      twice overall. So a nest of macro invocations like the above
      will still exponentially inflate the amount of preprocessor
      output. But it will only inflate by a factor of 2 each time,
      instead of 10 or more.
So the moral of this section is the same thing I’ve said
      already:
if you can
, it’s better to
      use
_Generic
in a mode where it just selects between
      function names – even if you have to write some functions
      specially to be selected.
Conclusion
In summary:
_Generic
has a huge design limitation that
        makes a lot of things you wanted to do with it not work.
The best available workaround is to try to use it the same
        way it was originally designed: select between function names
        only, and put the function call arguments outside
        the
_Generic
. This avoids
almost
all the
        inconvenience, if you can write your code in that style.
If you can’t, there are several alternative workarounds
        available, all with the common theme of using an extra
        instance of
_Generic
to present the outer one
        with something it can handle.
However, these workarounds create their own problems, in
        particular the risk of exponential compiler slowdown, so use
        with caution, if at all!
It’s tempting to ask: is there anything
      that
_Generic
is
useful for, if it’s so hard
      to make it do any of the things I’ve mentioned here?
Apart from the most obvious answer (that it’s useful for things
      exactly like
<tgmath.h>
), the best
      thing I’ve thought of to do with
_Generic
is to use
      it for deliberate error checking. The annoyance in all the
      previous sections was that it was very hard to
avoid
compile errors, when we wanted our code to actually compile, run
      and do something useful. But if what we
wanted
was to
      provoke compile errors on a hair-trigger basis, then perhaps we
      could use it for that more reliably?
An example: in a code base of mine I once refactored some
      open-coded uses of arrays for a particular purpose, replacing
      them with an abstract data type that had a documented API. One
      part of this refactoring involved finding all the places where I
      passed one of those arrays to
free()
– or rather,
      to the wrapper function
sfree()
that I habitually
      use in code bases of my own – and instead, pass the new ADT to
      its own dedicated free function. If I failed to do that, there
      would be a memory leak (secondary memory allocations hanging off
      the main object wouldn’t be cleaned up).
      But
sfree()
(just like
      standard
free()
) accepted a
void *
, so
      it wouldn’t throw an error if I used it for the new ADT.
My solution was to turn
sfree()
itself into a
      macro that checked the input type using
_Generic
:
extern void dummy(void *);

#define sfree(x) _Generic(x,   \
    MyNewADT *   : dummy,      \
    default      : sfree) (x)
Just like the dummy function in a previous
      section,
dummy()
here exists only as a declaration,
      and isn’t defined anywhere. So if I had any remaining cases of
      the new ADT being passed to
sfree()
, then this
      generic expression would select a call to a nonexistent
      function, and cause a link-time failure. Meanwhile,
      everything
else
gets freed as normal.
(I decided this was ugly enough that I should only do it during
      the refactoring process, as a one-off check that I’d converted
      all the old
sfree()
calls. Once the refactoring was
      complete, I removed the scaffolding, turned
sfree
back to the way it normally was, and trusted myself to carry on
      freeing instances of the new ADT using its own free function
      when I add new code in future.)
