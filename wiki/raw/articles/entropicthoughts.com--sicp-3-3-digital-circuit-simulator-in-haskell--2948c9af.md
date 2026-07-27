---
title: "Digital circuit simulator in Haskell (SICP 3.3)"
url: "https://entropicthoughts.com/sicp-3-3-digital-circuit-simulator-in-haskell"
fetched_at: 2026-07-27T10:17:12.753022+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Digital circuit simulator in Haskell (SICP 3.3)

Source: https://entropicthoughts.com/sicp-3-3-digital-circuit-simulator-in-haskell

There are many ways to implement mutable state in Haskell, but to begin with,
we’ll use the way that’s most similar to the
sicp
solution:
IORef
s. An
IORef
is a mutable variable, like in any other programming language.
2
The
only major difference is that we need a bit of extra machinery to read from
it, because it’s designed so that we cannot accidentally read from it in pure
code. (That would make the code impure, after all.)
We define a type
Wire
, which starts out with its signal
Low
, and with an
empty list of
action procedures
.
The idea of action procedures comes from the
sicp
implementation of this code;
action procedures are subscribers to the signal on this wire, and they will be
invoked whenever the signal changes. Action procedures will be installed by
components connected downstream of this wire, so those components can update
themselves when the wire value changes.
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
data
Wire
=
Wire
{ action_procedures
::
IORef
[
IO
()
]
  , signal_value
::
IORef
Signal
}
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
We can get the signal from a wire by reading the mutable variable holding its
current signal.
In[2]:
get_signal
(
Wire
_
signal)
=
readIORef signal
To set a signal on a wire we write to the mutable variable. If this causes a
state change of the wire, we’ll also run the installed action procedures to let
downstream components know.
3
This is the observer pattern, in case it sounds
familiar.
In[3]:
set_signal
(
Wire
procs signal) new_value
=
do
current
<-
readIORef signal
  when (new_value
/=
current)
$
do
writeIORef signal new_value
    actions
<-
readIORef procs
    sequence_ actions
Finally, we have a method on the wire that lets downstream components install
new action procedures. To ensure wires are initialised with the proper value
when components are connected, we immediately run all action procedures we
install.
In[4]:
add_action
(
Wire
procs
_
) action
=
do
modifyIORef procs (action
:
)
  action
A
probe
in the
sicp
implementation is an action procedure installed on a
wire that reports the value of the wire to the user of the program.
In[5]:
probe
name wire
=
add_action wire
$
do
current
<-
get_signal wire
    putStrLn (name
<>
" new value: "
<>
show current)
At this point the wire object is done, and we can experiment with it in the
repl
. We create a wire and add a probe to it. If we set its signal to the same
thing it was before, nothing changes. If we set its signal to a new value, the
probe fires.
In[6]:
λ
>
w
<-
make_wire
λ
>
probe
"wire"
w
wire
new value
:
Low
λ
>
set_signal w
Low
λ
>
set_signal w
High
wire
new value
:
High
Then we can start to implement the most basic components. An
inverter
is, as in
the
sicp
implementation, an action procedure on the input wire that sets the
signal on its output wire to the opposite of the input.
In[7]:
inverter
input output
=
add_action input
$
do
current
<-
get_signal input
    set_signal output
$
case
current
of
Low
->
High
High
->
Low
The
and_gate
works similarly, except it reads two inputs before determining
its output.
In[8]:
and_gate
a1 a2 output
=
let
action
=
do
c1
<-
get_signal a1
      c2
<-
get_signal a2
      set_signal output
$
case
(c1, c2)
of
(
Low
,
Low
)
->
Low
(
Low
,
High
)
->
Low
(
High
,
High
)
->
High
(
High
,
Low
)
->
Low
in
do
add_action a1 action
    add_action a2 action
The
or_gate
is like the
and_gate
except with a different truth
table.
4
Like a true designer of digital circuits, I have put the truth table
in Grey code.
In[9]:
or_gate
a1 a2 output
=
let
action
=
do
c1
<-
get_signal a1
      c2
<-
get_signal a2
      set_signal output
$
case
(c1, c2)
of
(
Low
,
Low
)
->
Low
(
Low
,
High
)
->
High
(
High
,
High
)
->
High
(
High
,
Low
)
->
High
in
do
add_action a1 action
    add_action a2 action
So far, we have invented nothing here; this is all in line with the
implementation from
sicp
. There are three neat properties of this Abelson and
Sussman design:
The set of components is open. If we turn this into a library, any user of the
library can add their own components and their components would interact
beautifully with those we have.
The components are not limited to a fixed number of inputs or outputs.
Anything that reads from wires and writes to other wires is a valid component.
We can compose these basic gates into higher-level components, as plain
procedure statements.
The latter means that we can make a half-adder by composing gates, and a
full-adder by composing half-adders and gates.
In[10]:
half_adder
a b s c
=
do
d
<-
make_wire
  e
<-
make_wire
  or_gate a b d
  and_gate a b c
  inverter c e
  and_gate d e s
full_adder
a b c_in sum c_out
=
do
s
<-
make_wire
  c1
<-
make_wire
  c2
<-
make_wire
  half_adder b c_in s c1
  half_adder a s sum c2
  or_gate c1 c2 c_out
This all comes straight out of the
sicp
implementation. The only thing we’re
missing so far is a scheduler to simulate propagation delay.
