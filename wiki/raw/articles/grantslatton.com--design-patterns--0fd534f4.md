---
title: "Design Patterns"
url: "https://grantslatton.com/design-patterns"
fetched_at: 2026-04-29T07:02:16.184666+00:00
source: "grantslatton.com"
tags: [blog, raw]
---

# Design Patterns

Source: https://grantslatton.com/design-patterns

Design Patterns
A software design pattern is just what the name suggests: a pattern that comes up repeatedly in software design.
Just like an architect may design two different houses, there are a lot of similar problems faced. For example, where to position the door to a room? The middle of a wall? The corner? Does it open in or out?
A skilled architect may say "this is a small bedroom, so I'll apply the corner-door-that-swings-outwards pattern". The architect has used his experience to match a common situation to a common solution. That's a design pattern.
In code, you may have a situation where you need to keep around several different pieces of state in order to construct objects that need the state. Maybe all these different pieces of state are tedious to keep organized. This is a common problem! And it has a common solution — the "factory pattern" discussed more below.
Design patterns are much-maligned, but that's just because people blow them out of proportion, and that generates an equal and opposite antagonism.
This post is a no-fanfare, nuts-and-bolts description of the major design patterns and when to use them.
A preliminary note
Most people learning design patterns go wrong by
looking for
places to apply design patterns.
They think "if I structure my code this way, I'll
get to
use the foobar design pattern".
You mustn't think of design patterns as something you want to or get to use. You should think of them the exact same way you think of a simple if-statement or for-loop. When your code needs one, you use it, and when it doesn't need one, you don't.
You could stretch the definition of design pattern just a little to say that any commonly used programming construct is a design pattern. The double-nested for-loop pattern. The recursive function pattern. Etc.
You should think of the design patterns in this post just the same as these, though perhaps just
slightly
less obvious, and thus worth naming and discussing.
Let's dive in.
Strategy
Suppose you have some code that needs to sort an array as part of its operation. But suppose you want the
caller
to be able to configure how this sort happens. Is it parallel? Is it
stable
? Is it ascending or descending?
One way to implement this is to simply pass in a bunch of booleans and have the code do all the branching.
Another way to do this is to invert where the branching happens. Rather than the caller passing in booleans so the code can branch on the sorting algorithm, you can have the caller do the branching and
pass in
a sorting algorithm.
That is, you can imagine an interface like:
trait
Sorter
{
fn
sort
(
data
:
&
mut
[
u32
]
)
;
}
and then imagine now rather than accepting a bunch of booleans and branching, the code just accepts a
Sorter
and calls
sorter.sort(data)
.
Now the calling code doesn't need to clutter itself with the details of the sorting algorithm and the branching.
You might ask "but doesn't this just move the code around? it doesn't actually reduce code?" and this is true in this simple case! There are in fact many places where you
don't
want to use this pattern!
The cases where you might want to use it are:
You care a lot about making this bit of code very clean and de-noised. That is, you are happy to push the complexity to the caller because you care more about this code being clean than the caller's code.
You have more than one place that wants to use the strategy. Imagine there are 10 functions that all want to branch on sorting logic. Reduces boilerplate and bug surface area to push up the stack and deduplicate in the caller.
You now might ask "isn't this just passing in a function?" and you would be 100% correct. In most cases the strategy pattern is basically just a fancy way of talking about passing around functions.
If you come from a functional programming background, you won't even think about this as interesting. But many imperative programmers will have never encountered functions-as-values until they get more advanced.
The strategy pattern is a
little
more powerful than a simple function pointer, since the strategy object can have state, whereas a pure function doesn't have state. This makes it more equivalent to what some functional languages might call a lambda or a closure that
capture
their scope and thus have some implicit state.
Another example of a common strategy pattern is a random number generator. There are a ton of ways to generate random numbers. You can reach out to the OS random number generator (e.g.
/dev/urandom
on Linux) or you can use any number of pseudorandom number generator (PRNG) algorithms.
Those PRNGs all have their own state, so every time you call
random.generate()
, it's mutating some internal state. A random number generator is an example of the strategy pattern because it abstracts the
strategy
it uses to generate the random numbers.
Factory
A factory is an object that has a method that produces other objects.
Why use a factory to produce those objects instead of just calling the objects' constructors yourself?
There are two main reasons to use a factory.
The first is to encapsulate state that would be tedious to maintain, or that the caller should not know about.
Consider an object whose constructor has 10 fields, but at the place you want to construct an object, only 3 of them are relevant and changing from construction to construction.
You can pass the other 7 values in to this code so that they can be passed in to the constructor, but this has a few issues:
Noisy code, the unrelated values distract from what this code is actually trying to do, confuse/mislead future devs who will maintain this code
Noisy diffs, if you ever add a field to the constructor, you'll have to update this otherwise unrelated code
The second reason to use a factory is to hide
logic
for constructing the object that the caller shouldn't know about. This is overlapping with the Strategy pattern described above. That is, the factory has some internal
strategy
or logic for
how
to construct the value, and the caller doesn't need to concern itself with this logic.
It would be fair to say that a Factory is actually a
subset
of the more general Strategy pattern. It's the subset of strategies that produce values.
Note that not all strategies are factories though, e.g. a sorting algorithm might mutate the data in place instead of constructing a new value.
Visitor
The visitor is the inverse of the iterator.
In an iterator, the object produces an iterator, and the iterator produces values.
In a visitor, the object
is given
a visitor, and the visitor
is fed
values.
An example might make it more clear:
//
Iterator
let
mut
sum
=
0
;
for
x
in
collection
{
sum
+
=
x
;
}
//
visitor
let
mut
sum
=
0
;
collection.
visit
(
|
x
|
{
sum
+
=
x
;
}
)
;
Note that the calling code looks very similar! In the latter, we have created a closure (anonymous lambda function) that
accepts
the values that
collection.visit
sends
into it. Presumably its implementation sends all the values, just like presumably its iterator yields all the values.
The visitor does have a major limitation: you cannot do all the normal control flow. You can't break from the loop. You can't early-return from the function. You're trapped inside the closure. If you early-return from the closure,
collection.visit
doesn't know, it'll just call you again with the next value.
Some visitor implementations will be a little more sophisticated and allow the visitor to return a boolean value to signal that it wants to stop the visiting. This is more powerful, but also code noise if your code happens to never want to early-break.
So, in general, you will usually prefer the iterator pattern to the visitor pattern.
The one major caveat is that it's really hard to implement the iterator pattern for some structures, the most common culprit being trees and graphs.
In a tree, it's trivial to recursively visit all the nodes and apply a visitor to the values. Returning an iterator on the other hand is kind of tedious to implement, and often will have performance impact due to dynamic dispatch needed to handle the recursive type.
Another potential route for performance impact with the iterator is if you want to produce an iterator that iterates over several constituent collections. This is typically done with iterator chaining. That code looks like:
fn
iter_numbers
(
&
self
)
->
impl
Iterator
<
Item =
u32
>
{
self
.ages.
iter
(
)
.
chain
(
self
.heights.
iter
(
)
)
}
In this code, we have a struct that has two integer arrays: ages and heights. For whatever reason, we want a way to iterate all those numbers. So we produce iterators for the individual collections and chain them together.
There is a little bit of runtime impact to this, though! Every call to get the next value of the iterator must check the ages iterator, and if it's empty, go check the heights iterator.
Compare to a visitor pattern:
fn
visit_numbers
(
&
self
,
visitor
:
impl Fn
(
u32
)
)
{
self
.ages.
iter
(
)
.
for_each
(
visitor
)
;
self
.heights.
iter
(
)
.
for_each
(
visitor
)
;
}
Now, we don't need to do that check on every single element, so this might perform better than the iterator. But at the cost of those ergonomics we mentioned above. So only do this for performance reasons if you have run a profiler and know you must do it. Otherwise, the ergonomics should be more important.
Also, note that in the visitor method, we construct an iterator and then use the iterator method
for_each
to
visit
each element. This is just equivalent to looping through the iterator with a for-loop and sending every element into the visitor.
Builder
A builder is an object that makes it easier or safer to construct another object. This should remind you of the factory from above. Both are objects that create objects.
The main difference is really just in the ergonomics and how they are used in practice.
Builders typically look like this:
let
person
=
PersonBuilder
::
default
(
)
.
name
(
"
Grant Slatton
"
)
.
age
(
123
)
.
height
(
456
)
.
weight
(
789
)
.
build
(
)
;
It's possible that
Person
has 20 different configurable fields, but here I only wanted to set 4 of them, and presumably the builder will set the others to the default values.
What's going on here API-wise is each method on
PersonBuilder
is doing the update and then returning a
PersonBuilder
to enable this call style (often referred to as a
fluent interface
).
So the main use-case for builders is to configure an object with a lot of knobs, whereas the main use of factories is to hide state used in object construction.
Builders might also use the type system to prevent illegal constructions at compile time. For example, some method on the builder might not return the original builder, but some new object that only has a subset of the methods that are now valid after some choice has been made.
For example, you might have something like
let person = PersonBuilder::default()
.name("Jane")
.age(30)
.female()
.is_pregnant();
The
female()
method might consume the
PersonBuilder
and return a
FemalePersonBuilder
that has female-specific methods such as
is_pregnant
. So the type system is used to create a construction flow-chart that makes constructing a pregnant male
Person
object impossible.
Important note: It's
very
tedious to create a builder by hand, and you should not do it unless you
really
need some fancy behavior. Most languages have libraries or other tools to automate a lot of the builder process.
Here's the
derive_builder
crate in Rust that gives a procedural macro that generates a
PersonBuilder
automatically:
#
[
derive
(
Default
,
Builder
)
]
struct
Person
{
name
:
String,
age
:
u32
,
likes_dogs
:
bool
,
plays_tennis
:
bool
,
}
And here's a
@Builder
annotation in Project Lombok that does the same for Java:
@
NoArgsConstructor
@
Builder
public
class
Person
{
private
String
name
;
private
int
age
;
private
boolean
likesDogs
;
private
boolean
playsTennis
;
}
All this being said, in my years of software development, I have never actually needed to make a builder for one of my own classes.
When you're building an
application
, all the classes you write have some exact fields they need, and that's it. You just use the constructor, or, if you want to encapsulate state for code tidiness, a factory.
The main place I've
used
builders written by other people are in libraries.
As a library author, exposing a builder allows you to change the underlying implementation of an object with a lot of knobs without changing the builder and thus breaking code that uses the library.
Consider a CSV parser. It might look like this:
struct
CsvParser
{
delimiter
:
char
,
quote
:
char
,
newline
:
String,
}
The builder defaults are probably comma, double-quote, and linefeed. So someone who just wants to change the newlines to Windows style might do:
let
parser
=
CsvParserBuilder
::
default
(
)
.
newline
(
"
\r
\n
"
)
.
build
(
)
;
Now suppose the CSV parsing library realizes some files are actually degenerate and have a mix of different newline types, both
"\n"
and
"\r\n"
— probably because someone naively concatenated files with different origins together.
So they want to refactor their CSV parser to accommodate this new mode:
struct
CsvParser
{
…
newline
:
NewlineMode,
}
enum
NewlineMode
{
Both
,
Known
(
String
)
,
}
If the library author had exposed a simple constructor for the parser, the type signature of that thing would need to change. It used to take
newline: String
and now takes
newline: NewlineMode
.
You could keep the old constructor, make a new constructor with the new signature, and make the old implementation delegate to the new one. I've seen code that does this and winds up with 20 different constructors!
This is actually not terrible if the code is in a slow-moving part of some application codebase. It's not great for a library though, where having a user-friendly API is a big part of the game.
So to add this new mode, the CSV parser library simply makes the existing
newline(String)
method of the builder now internally construct a
NewlineMode::Known
, and the author adds a new method to the builder,
accept_both_newlines()
.
Existing code doesn't need to change, the library gains a new feature in a non-breaking way, the world keeps on turning.
To summarize: probably don't make your own builders if you are writing an application, their main utility is when authoring a library. If you do need them, most languages have builder-making libraries that will do most of the work for you.
Singleton
A singleton is a class that is written in a way that only one instance of the object can exist. This is usually accomplished by means of the language's visibility rules. Rather than a constructor, the class will expose a way to get a handle to this one global instance.
Here's an example:
mod
example
{
pub
struct
GlobalCounter
{
counter
:
Mutex
<
u64
>
,
}
impl
GlobalCounter
{
pub
fn
instance
(
)
->
&
GlobalCounter
{
static
INSTANCE
:
GlobalCounter
=
GlobalCounter
{
counter
:
Mutex
::
new
(
0
)
,
}
;
INSTANCE
}
pub
fn
increment_and_get
(
&
self
)
->
u64
{
let
mut
counter
=
self
.counter.
lock
(
)
.
unwrap
(
)
;
*
counter
+
=
1
;
*
counter
}
}
}
Now, callers cannot create their own
GlobalCounter
. There is no public constructor, and the fields are private too. The only way to get a
GlobalCounter
is with the
instance
method, for example:
let
counter
=
GlobalCounter
::
instance
(
)
;
let
current_count
=
counter.
increment_and_get
(
)
;
The main way you arrive at this pattern is you're building an
application
, not some generic module or library, so you know for certainty only one of a thing will ever exist, you need access to that thing all over the codebase, and the global variable saves you the plumbing.
The classic example here is a logger. You only need one logger. You log from everywhere. You don't wanna add a
logger
argument to every function in the codebase. You use a singleton.
Other classic examples are thread pools or caches.
Thread pools make sense because physical resources like CPU cores are a globally constrained resource, so global management in a singleton threadpool makes sense.
Caches make sense because they are transparent to the user — whether a cache is local or global doesn't affect its correctness to the user. This
can
be a little false depending on the use case, i.e. if the eviction policy matters a lot. The use cases that make the most sense are when you never evict from the cache.
The
major
downside of singletons is testability.
For example, consider you want to test that some log statement gets emitted. All your other tests are going to be running in that same test suite run, and they will spam your logs and make it really hard to deterministically figure out what's going on.
Fundamentally, if your singleton isn't transparent like a cache, all your tests will be touching it all the time, non-deterministically, so it's hard to test the singleton itself.
Unless you really know what you're doing, the only singleton you should ever make is probably a logger.
Conclusion
But Grant, you've only written about 5 patterns.
The book
has 23 patterns! What about prototypes? And adapters? And flyweights?
I think the rest of the patterns in that book are trivial — no more a pattern than a for-loop or an if-statement is a pattern — whereas the 5 mentioned above are a little "clever" in that they may not be what a new programmer intuitively invents.
The
Facade Pattern
is when you wrap a complex interface with a simplified interface. The
Command Pattern
is where you create a class that bundles a whole set of configuration knobs, so you can send the whole command as a single object instead of the individual knob values.
Both of these are just trivial abstractions anyone will naturally intuitively and so aren't worth talking about further. The rest of the patterns in that book are the same.
So you should look at these patterns more as "fancy tricks" that are
not
intuitive, and should thus be avoided unless the alternative is quite a bit worse.
The common names help make them more intuitive. When I see a
FooFactory
, I know to expect it has some
make_foo
method. When I see a
PersonBuilder
, I have a pretty good idea it has a
with_name
and
build
method.
And when I see a visitor, I know I'm expected to pass a function that is kind of like an iterator loop body. I don't have to think more about what's going on. The name tells me what's up.
So as best as you can, when you use these patterns, explicitly refer to them by the common pattern name.
FooBuilder
,
visit
,
BarFactory
, etc.
