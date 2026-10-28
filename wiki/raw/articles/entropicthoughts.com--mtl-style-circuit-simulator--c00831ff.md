---
title: "MTL-style circuit simulator"
url: "https://entropicthoughts.com/mtl-style-circuit-simulator"
fetched_at: 2026-10-28T10:01:26.453709+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# MTL-style circuit simulator

Source: https://entropicthoughts.com/mtl-style-circuit-simulator

After the first attempt at making
a very side-effectful circuit simulator
, and
then an ambitious attempt at
making it pure
, I was reminded of a middle ground,
using a pattern common in production Haskell code. It is called
mtl
-style
effects
, and it is a specific type of
final tagless encoding
.
The idea is that we first find a set of operations that our circuit simulator
needs to support. Drawing this boundary well requires some experience and taste.
Then we encode that limited set of operations into a type class. Here’s one way
to do it.
In[1]:
class
CircuitOperations
m
where
make_wire
::
m
Wire
get_signal
::
Wire
->
m
Signal
set_signal
::
Wire
->
Signal
->
m
()
add_action
::
Wire
->
m
()
->
m
()
after_delay
::
Int
->
m
()
->
m
()
get_time
::
m
Int
probe_output
::
String
->
m
()
propagate
::
m
()
Having read the previous article, these operations should sound familiar. I’m
sure it’s possible to create a better set of operations, but this will suffice
to illustrate the point.
Previously, the
get_signal
function had type
In[2]:
get_signal
::
Wire
->
IO
Signal
which means that it takes a wire, and to execute its effects and return a signal
value, it must run in the
IO
context. This context allows the implementation
to do all kinds of naughtiness, like reading files or launching missiles. With
this type signature, the function
knows
it runs in the
IO
context, so it can
do all those things.
With the new type class, the signature is instead
In[3]:
get_signal
::
CircuitOperations
m
=>
Wire
->
m
Signal
This hides from the
get_signal
function which context it runs in
. The
actual, concrete context it will run in is going to be selected at some point
later by the compiler, and chucked into the variable
m
. But the implementation
of
get_signal
has no idea what context it will run in. All
get_signal
knows
is that whatever context it gets, it will be a context that supports
CircuitOperations
.
Thus, even if the function ends up
running
in the
IO
context, the
implementation
doesn’t know that, so it won’t be able to launch missiles. All
the implementation is allowed to do is call the operations specified in the
CircuitOperations
interface.
Even components we define outside of this set of operations are now implemented
in terms of that interface. Previously we had e.g.
In[4]:
inverter
::
Wire
->
Wire
->
IO
()
inverter
input output
=
add_action input
$
do
--
------------- >8 -------
Now, with no change of any code, this function has type
In[5]:
inverter
::
CircuitOperations
m
=>
Wire
->
Wire
->
m
()
Thus, other component implementations are also no longer allowed to perform
arbitrary side effects. They can only do whatever is allowed by the
CircuitOperations
interface. This does not mean a component cannot misbehave;
it can, for example, unschedule other component’s effects. But it’s restricted
to a smaller set of misbehaviour than before.
So far we have only have the specification of the
CircuitOperations
interface,
and the components that use it. We don’t have an implementation of it, so in
practice it is impossible to run this program, because the compiler won’t know
which type to instantiate for that interface.
This is where we will be cheeky. Without changing our previous implementations
of the operations involved, we will simply move them into an instance definition
for this interface.
In[6]:
instance
CircuitOperations
IO
where
make_wire
=
do
initial_procs
<-
newIORef
[]
initial_signal
<-
newIORef
Low
pure (
Wire
initial_procs initial_signal)

  get_signal (
Wire
_
signal)
=
readIORef signal
--
------------- >8 -------
This definition says that the
IO
type supports all circuit operations. We
already knew that, because the previous version of the program ran only in
IO
.
What this definition does is teach the compiler how that happens, using the
exact same implementations as before.
In fact, at this point, the
only
type that supports all circuit operations is
the
IO
type! So when the compiler is faced with the choice of which type to
pick for simulating the circuit, it will pick
IO
. At run-time, everything will
happen in
IO
, just as it did before.
But that’s not the point! The point is that in the code, the circuit simulation
is now restricted to a smaller set of circuit simulation operations, rather than
the whole wide world of
IO
. This doesn’t make it pure, because it’s still
impossible to run it from any context other than
IO
. But it does make it a
little pure…er?
Postscriptum: Due to the mutable global variable
the_agenda
, we cannot
implement this interface for any other type than
IO
. But we could, for
example, add the agenda-specific operations to this interface (or a
sub-interface) and then implement the interface with a type that encapsulates
the impurity, like
ST
.
Then our components would still be generic and be able to run in
IO
, but they
could also run in
ST
. This is useful because
IO
is convenient when possible,
but
ST
is executable from a pure context because it encapsulates its impurity.
It’s also useful because it unties the components from the specific context
they’re implemented in. It clearly delineates which operations make up a circuit
simulation.
