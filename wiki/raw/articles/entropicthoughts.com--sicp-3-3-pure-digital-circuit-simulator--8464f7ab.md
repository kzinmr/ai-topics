---
title: "Purely functional digital circuit simulator (SICP 3.3)"
url: "https://entropicthoughts.com/sicp-3-3-pure-digital-circuit-simulator"
fetched_at: 2026-08-05T10:12:33.189959+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Purely functional digital circuit simulator (SICP 3.3)

Source: https://entropicthoughts.com/sicp-3-3-pure-digital-circuit-simulator

If we are going to manage the simulation in a pure functional manner, we still
have to contend with the fact that during simulation, wires are objects with a
fixed identity. A wire does not become a different wire just because its signal
changes – the same wire is still hooked up to the same gates. Wires need to
maintain their identity somehow.
2
The alternative is reconstructing the full
circuit any time a wire value changes, which is not so crazy as it sounds, given
that it can be stored as a
persistent data structure
. But we won’t go down that
route today.
In addition to the
Signal
type from before, we’ll define a
Wire
to be a
string. This is its identity. We’ll also make a convenience function for
creating a wire whose name is based on another wire name. This will be useful
for creating unique wire names when we build circuits.
In[1]:
data
Signal
=
Low
|
High
deriving
(
Show
,
Eq
,
Ord
,
Bounded
)
newtype
Wire
=
Wire
String
deriving
(
Show
,
Eq
,
Ord
)
make_wire
(
Wire
base) suffix
=
Wire
(base
<>
"."
<>
suffix)
We keep track of the state of the wires during simulation by maintaining a
mapping from wire identity to signal. I’m not a fan of type aliases like this
one
3
Type aliases increase indirection with no gain in abstraction. When
faced with a type alias, the first thing I have to do to understand something is
expand the alias to what it really stands for. So … what’s the point? I don’t
get it.
, but for saving space in this article, it’ll have to do.
In[2]:
type
WireState
=
Map
Wire
Signal
We will store signal changes as
Change
objects. They indicate at which time
the signal changed, in which wire it changed, and what the signal changed to.
In[3]:
data
Change
=
Change
{ time
::
Int
, wire
::
Wire
, signal
::
Signal
}
deriving
(
Show
,
Eq
,
Ord
)
A circuit is going to be a plain list of components.
4
Again, type alias for
brevity in the code examples in the article.
A component is a function
that responds to changes and produces downstream changes.
In[4]:
type
Circuit
=
[
Change
->
WireState
->
[
Change
]]
For example, here’s the
inverter
. When it receives a change, it verifies that
the change applies to its inputs, and if it does, it emits a change to its
output, scheduled for a propagation delay later.
5
In this function, both
pure
calls are in list context, meaning they construct singleton lists. The
way to understand it is that the
inverter
component has only one listener
function, and it only produces at most one downstream change. (The second
pure
only runs if the
guard
passes. If the condition is false, an empty list of
changes will be produced by this component.)
In[5]:
inverter
::
Wire
->
Wire
->
Circuit
inverter
input output
=
pure
$
\
change
_
->
do
guard (change
.
wire
==
input)
    pure
$
Change
(change
.
time
+
2) output
$
case
change
.
signal
of
Low
->
High
High
->
Low
The code for the binary gates will be similar, except they need to look at both
their inputs to see what the output should be. They get a convenience function
to look up the state of a wire with a default.
In[6]:
look
::
Wire
->
WireState
->
Signal
look
w
=
Map.findWithDefault
Low
w
Then the
and_gate
is implemented as
In[7]:
and_gate
::
Wire
->
Wire
->
Wire
->
Circuit
and_gate
a1 a2 output
=
pure
$
\
change state
->
do
guard (elem change
.
wire [a1, a2])
    pure
$
Change
(change
.
time
+
3) output
$
case
(look a1 state, look a2 state)
of
(
High
,
High
)
->
High
_
->
Low
and the
or_gate
is exactly the same but for the truth table.
In[8]:
or_gate
::
Wire
->
Wire
->
Wire
->
Circuit
or_gate
a1 a2 output
=
pure
$
\
change state
->
do
guard (elem change
.
wire [a1, a2])
    pure
$
Change
(change
.
time
+
5) output
$
case
(look a1 state, look a2 state)
of
(
Low
,
Low
)
->
Low
_
->
High
Since
Circuit
is a type synonym for a plain list of components, we can compose
components by appending lists. Here’s a half-adder.
In[9]:
half_adder
::
Wire
->
Wire
->
Wire
->
Wire
->
Wire
->
Circuit
half_adder
ns a b s c
=
let
d
=
make_wire ns
"d"
e
=
make_wire ns
"e"
in
or_gate  a b   d
<>
and_gate a b c
<>
inverter     c   e
<>
and_gate       d e s
The spacing between the arguments to the gates is not significant, but it does
help with circuit recognition at a glance. The full adder is constructed
similarly.
In[10]:
full_adder
::
Wire
->
Wire
->
Wire
->
Wire
->
Wire
->
Wire
->
Circuit
full_adder
ns a b c_in sum c_out
=
let
s
=
make_wire ns
"s"
c1
=
make_wire ns
"c1"
c2
=
make_wire ns
"c2"
ha1
=
make_wire ns
"ha1"
ha2
=
make_wire ns
"ha2"
in
half_adder ha1 a c_in s      c1
<>
half_adder ha1 b      s  sum    c2
<>
or_gate                      c1 c2 c_out
Seeing it this way makes me realise how big of a circuit a full adder really is.
