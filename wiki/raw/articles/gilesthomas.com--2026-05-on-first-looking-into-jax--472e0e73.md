---
title: "On first looking into JAX"
url: "https://www.gilesthomas.com/2026/05/on-first-looking-into-jax"
fetched_at: 2026-05-31T07:01:06.258859+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# On first looking into JAX

Source: https://www.gilesthomas.com/2026/05/on-first-looking-into-jax

Archives
Categories
Blogroll
Much have I travell'd in the realms of gold,
And many goodly states and kingdoms seen;
Round many western islands have I been
Which bards in fealty to Apollo hold.
Oft of one wide expanse had I been told
That deep-brow'd Homer ruled as his demesne;
Yet did I never breathe its pure serene
Till I heard Chapman speak out loud and bold:
Then felt I like some watcher of the skies
When a new planet swims into his ken;
Or like stout Cortez when with eagle eyes
He star'd at the Pacific -- and all his men
Look'd at each other with a wild surmise --
Silent, upon a peak in Darien.
John Keats,
On First Looking into Chapman's Homer
I've been working with
PyTorch
quite a lot for the last couple of years, and feel
like I've come to a reasonably solid understanding of how it all fits together.
Working through
Sebastian Raschka
's book
"
Build a Large Language Model (from Scratch)
",
training my own LLMs
locally
and
in the cloud
,
rebuilding Andrej Karpathy's 2015-vintage RNNs
--
over time, it all adds up!
But, of course, there are other frameworks, and one I kept hearing about was
JAX
.  While it's less
dominant than PyTorch, it has a reputation for a certain cleanliness, a certain purity.
And having spent time over the last couple of weeks working through the tutorials, and translating small PyTorch examples
into it, I've been really impressed.
In this post I want to give an overview -- to report back to beginners like me, still
living in PyTorch-land, on my new discovery.  Less like Herschel discovering Uranus,
and more like a 16th-century European coming back after having discovered something that
the people who lived there were perfectly well aware of.  What is this JAX thing,
and how does it differ from PyTorch?
Some theses, significantly overstated
I think that the main differences between PyTorch and JAX are something like this, but a little
less strident:
PyTorch is engineering; JAX is maths.
PyTorch has historically been optimised piecewise, JAX is JITted.
PyTorch is procedural, JAX (tries to be) functional.
PyTorch is maximalist; JAX is minimalist.
Having overstated my claims, let me dig in and perhaps walk them back a bit.
Once I've gone through them, I'll do a walkthrough of porting a simple PyTorch
training loop to JAX, which should illustrate the points well.
Finally, I'll wrap up with the counterargument.  JAX is wonderful and shiny, and
30+ years of industry experience and cynicism makes me fear that it might be doomed :-(
But let's start with the positive!  [Happy face on.]
1. Maths versus engineering
A simple example that nicely contrasts the different philosophies of
the two frameworks is what the core of a training loop looks like.  Here's how
you might write one in PyTorch:
optimizer
.
zero_grad
()
result
=
model
(
inputs
)
loss
=
loss_function
(
result
,
targets
)
loss
.
backward
()
optimizer
.
step
()
This is kind of mechanistic.  You're telling the computer what to do, step by step:
Zero out the gradients that you currently have attached to the parameters.
Do a forward pass to get the model's outputs.
Work out the loss based on those outputs.
Do the backward pass.
Update the parameters based on the gradients that the backward pass attached to them.
Now let's look at a parallel JAX implementation:
def
calculate_loss
(
parameters
,
inputs
,
targets
):
result
=
forward
(
parameters
,
inputs
)
return
loss_function
(
result
,
targets
)
...
def
train
():
...
grads
=
jax
.
grad
(
calculate_loss
)(
layers
,
inputs
,
targets
)
layers
=
step
(
layers
,
grads
,
learning_rate
)
It's clearly very different.  No explicit backward pass, no gradient-zeroing,
and the forward pass and loss calculation are baked into a separate function.
But why is it shaped that way?
Let's think about what we're actually doing in our training loop.  The gradients
are the partial derivative of the loss function
ℒ
against
the weights
W
:
gradients
=
∂
ℒ
∂
W
Now, I'm being a bit sloppy with that notation, because
ℒ
is a function, and
it -- in the mathematical formulation -- takes the weights as a parameter.  So it would be
better written like this:
gradients
=
∂
∂
W
ℒ
(
W
)
But that's still not quite right.  In a real training loop, we're doing this in the
context of a particular input batch,
X
,
and its associated targets,
Y
.   We might write that mathematically as this:
gradients
=
∂
∂
W
ℒ
(
W
:
X
,
Y
)
...where you can read the colon as "given".  Now let's look again at the JAX code to work
out the gradients:
grads
=
jax
.
grad
(
calculate_loss
)(
layers
,
inputs
,
targets
)
That's an almost-perfect mirror of the maths!
The
jax.grad
function takes a function
f
, and returns another function,
g
,
which takes the same arguments.  When you call
g
, instead of returning the result
of
f
, it will return the derivative of
f
with respect to its first argument,
given the values of the others.
How is it doing that magic?  Let's look at a simple concrete example:
def
f
(
x
,
y
):
print
(
f
"In the function
{
x
=}
,
{
y
=}
"
)
return
x
+
y
If you do the initial call to
grad
:
...then it just wraps
f
in a helper function.  It's when you call
g
that the magic
happens.
...will print out this:
In the function x=GradTracer(primal=2.0, typeof(tangent)=f32[]), y=1.0
The first parameter -- the one with respect to which we're asking for the derivative --
is replaced by a
GradTracer
object.  Because it's wrapping a float, it can
be used like one, so the function executes as expected. But it also keeps track of what happens to this
variable as the code executes, and essentially builds up what in PyTorch would be
represented by the computation graph.
So: while in PyTorch, the variables that you pass in to a function that you need gradients
for need to be special PyTorch objects that can keep a reference to those gradients --
the
requires_grad
parameter that pops up frequently in PyTorch code -- in JAX, it's
all handled by variables being automatically wrapped in these special tracers.
Once it has the results of the function as a whole, including the chain of operations
that was traced, it can automatically do a backward pass, and we're done.
That's really nifty!
Now, the example above was a toy one, with just one parameter.
In a real training loop, you're differentiating against a set of weights, and
those will be something more complex.  But
grad
handles that gracefully.  Let's see what happens if we pass in an array
as the first parameter:
>>>
import
jax
>>>
import
jax.numpy
as
jnp
>>>
def
f
(
x
,
y
):
...
print
(
f
"In the function
{
x
=}
,
{
y
=}
"
)
...
return
(
x
+
y
)
.
sum
()
...
>>>
g
=
jax
.
grad
(
f
)
>>>
g
(
jnp
.
array
([
1.
,
2.
,
3.
]),
jnp
.
array
([
4.
,
5.
,
6.
]))
In
the
function
x
=
GradTracer
(
primal
=
[
1.
2.
3.
],
typeof
(
tangent
)
=
f32
[
3
]),
y
=
Array
([
4.
,
5.
,
6.
],
dtype
=
float32
)
Array
([
1.
,
1.
,
1.
],
dtype
=
float32
)
So, we've got partial derivatives with respect to the elements of the array that was the first parameter --
just what we'd need for a single-layer neural network without bias.
But what about something more
complicated?  For something like (say) an LLM, we have quite a lot of structure to our weights: our
input embeddings, output head, all of the layers with their attention and feed-forward
weights, and so on.
grad
handles that by understanding basic Python structures --
things that can be mapped to what JAX calls PyTrees.  PyTrees are nested tree structures of dictionaries,
lists, tuples and so on, where the leaves are numbers or JAX arrays .
If you ask for gradients of a variable that can be represented by a PyTree, you get them back in
a form that mirrors that PyTree:
>>>
def
f
(
x
,
y
):
...
print
(
f
"In the function
{
x
=}
,
{
y
=}
"
)
...
return
(
x
[
"a"
][
"b"
]
+
y
)
.
sum
()
...
>>>
g
=
jax
.
grad
(
f
)
>>>
g
({
"a"
:
{
"b"
:
jnp
.
array
([
1.
,
2.
,
3.
])}},
jnp
.
array
([
4.
,
5.
,
6.
]))
In
the
function
x
=
{
'a'
:
{
'b'
:
GradTracer
(
primal
=
[
1.
2.
3.
],
typeof
(
tangent
)
=
f32
[
3
])}},
y
=
Array
([
4.
,
5.
,
6.
],
dtype
=
float32
)
{
'a'
:
{
'b'
:
Array
([
1.
,
1.
,
1.
],
dtype
=
float32
)}}
If you combine that with JAX's tree-aware
map
function, you can combine those gradients with the
original parameters to update them as you train.  I'll show you how that works later on, when we go through an
example of porting some PyTorch code to JAX.
So, all of that cool stuff was made possible by the tracer objects, which are passed
in instead of the real parameters, and keep track of the computation graph (just like the
graph that PyTorch attaches directly to the variables).
But tracers are more generally useful than that; they really come into their own with the next JAX difference: the JIT.
2. JIT vs piecewise optimisation
Imagine that you've built some kind of nifty model in PyTorch.  As part of it, you
do a calculation something like this:
score
(
q
,
d
)
=
∑
i
max
j
⟨
q
i
,
d
j
⟩
You decide that this is generally useful, so you
code it up as a CUDA kernel
and make
it available to the community, like Erik Kaunismäki has with his "MaxSim" kernel.  Maybe later on, it will get
added to the PyTorch library as a standard component.
There are a lot of optimisations like that built into PyTorch; people found that there
were higher-level abstractions on top of basic tensor operations that were generally useful,
so they coded up lower-level optimised versions.  For example, in the LLM I've been
working with, there is
an implementation of LayerNorm
.
But PyTorch has
its own one built in
.
And there's a
CUDA implementation
that
it will use automatically if it has the appropriate hardware available.
There is a problem, though.  Imagine that someone else is working on a different kind
of model in the future.  And for reasons completely unrelated to the MaxSim calculations
that Kaunismäki nicely optimised, they happen to need to do the same calculations.
Now, there are two things that can happen from there:
They don't know that the MaxSim kernel exists, so their code remains unoptimised.
They do know that it exists, so they repurpose it for whatever their use case is.
The first is not ideal; but the second isn't great either, if what they're using it
for is not a MaxSim operation in reality, just something that happens to look the same
mathematically.
In the general case: all optimisations that get into PyTorch have to be carefully named
so that they reflect the exact level of abstraction that they're targeting.  And when
people are writing PyTorch models, they need to actually know which optimised abstractions
are available, and where to apply them.
Now let's look at JAX.
It has an innocuous-looking decorator,
jit
, and you can use it by adding a single
line before your function:
@jax
.
jit
def
selu
(
x
,
alpha
=
1.67
,
lambda_
=
1.05
):
return
lambda_
*
jnp
.
where
(
x
>
0
,
x
,
alpha
*
jnp
.
exp
(
x
)
-
alpha
)
Behind that single line is a huge amount of useful infrastructure.  Just like
grad
, it's a function that takes one function and returns another, without necessarily running
the underlying code.   But when you call the wrapped function for the first time, some impressive stuff
happens:
This will essentially execute the
selu
code twice:
The first time through, it will create another of those tracer objects; this time,
though, it won't wrap the number
1.234
-- it will just know that it is a wrapper
for a float.  It will call the Python code with that tracer, and all of the operations in the function will be run, but the result
that comes out at the end will essentially just be a representation of what calculations
were done in an abstract sense -- like the computation graph that was used for
working out gradients, but without specific numbers in it.
JAX has a nice way to display these representations
as what it calls JAXPRs, and the JAXPR for that function's representation when called
with a float parameter will look something
like this:
{ lambda ; a:f32[]. let
    b:bool[] = gt a 0.0:f32[]
    c:f32[] = exp a
    d:f32[] = mul 1.67:f32[] c
    e:f32[] = sub d 1.67:f32[]
    f:f32[] = jit[
      name=_where
      jaxpr={ lambda ; b:bool[] a:f32[] e:f32[]. let
          f:f32[] = select_n b e a
        in (f,) }
    ] b a e
    g:f32[] = mul 1.05:f32[] f
  in (g,) }
That JAXPR can be compiled into the appropriate code for the platform where
you're running it -- x86 machine code, compiled CUDA, the equivalent for AMD
or Google Tensor Processing Units (TPUs), and will be cached.  The key for
the cache will be meta-information about the parameter -- in this case, something
like "a 32-bit floating-point scalar".
Next, the compiled code -- not the original Python -- is run with the actual value of the parameter, the
1.234
that we provided.
Now, of course, the advantage of doing this is that when you call it with a different
floating-point number -- say,
5.678
-- then you don't need to do the compilation again.
You can just rely on the cached version.  And the fact that the compiled code is
cached based on the metadata means that if you call
selu
with a vector, then it will compile
a new version for that, and likewise for a matrix version.
This is all really nifty, and you can see how it would help right away.  But for me,
at least, an excellent extra benefit is how it can save people like Erik Kaunismäki the bother
of writing custom kernels.  The compilation that happens, taking the representation
that it got from the tracing process and turning it into backend code, goes through an
optimising compiler,
XLA
.  And that compiler can recognise
"standard" operations and combine them together.
This won't be at the level of "standard operations" like MaxSim, of course -- more,
"this looks like a convolution, let's use the standard kernel".  But it does mean that
instead of someone having to take code written in Python and hand-port it over to
CUDA to get a GPU speedup, the same expertise can be put into improving the optimisation
part of XLA to get a speedup for all code.
That's pretty amazing.  However...
3. Procedural vs functional code
If you want something like the JIT to work properly, you need to limit the kind of code
that it works with.  In particular, it needs to be functional.  A function must always
return the same value when given the same inputs -- so this is fine:
@jax
.
jit
def
add
(
x
,
y
):
return
x
+
y
print
(
add
(
1
,
2
))
print
(
add
(
1
,
3
))
...but this will cause problems:
@jax
.
jit
def
addY
(
x
):
return
x
+
y
y
=
2
print
(
addY
(
1
))
y
=
3
print
(
addY
(
1
))
...because
y
could be changed.  Specifically -- because the global
y
had the value
2
during the initial traced run of the function, that value will essentially get hard-coded
into the cached JITted version, so both prints in the second example will output
3
.
Something slightly surprising comes out of this -- something that makes JAX code look very different
to PyTorch.  How we handle randomness needs to completely change.
Consider this code:
import
random
def
f
(
x
):
return
x
+
random
.
randint
(
1
,
10
)
random
.
seed
(
42
)
print
(
f
(
1
))
print
(
f
(
1
))
As a whole, it's deterministic.  But it breaks the functional requirement that
the function can only depend on its inputs.  Both calls to
f
take the same input,
but they return different results.
Even worse, if we were to do something that consumed
randomness between those two calls to
f
, for example:
print
(
f
(
1
))
random
.
randint
(
1
,
10
)
print
(
f
(
1
))
...we'd get different results.  The state of the random number generator is
global state kept outside the function, just like
y
in the
addY
example above.
A naive solution to this might be to make the state of the RNG explicit as a variable --
you can imagine a library that worked something like this:
import
updated_random
def
f
(
x
,
random_state
):
return
x
+
random_state
.
randint
(
1
,
10
)
random_state
=
updated_random
.
new_state
(
42
)
print
(
f
(
1
,
random_state
))
print
(
f
(
1
,
random_state
))
That
looks
more functional, but when you think
about it, we haven't actually fixed the problem.  We're passing the same
random_state
variable in in both cases, along with the same number, but we're getting different results.
It's not global, but it's still mutable behind the scenes.
What you'd actually need to do to make it purely functional would be something like
this:
import
updated_random
def
f
(
x
,
random_state
):
new_state
,
randint
=
updated_random
.
randint
(
random_state
,
1
,
10
)
return
new_state
,
x
+
randint
initial_random_state
=
updated_random
.
new_state
(
42
)
first_call_random_state
,
result
=
f
(
1
,
initial_random_state
)
print
(
result
)
second_call_random_state
,
result
=
f
(
1
,
first_call_random_state
)
print
(
result
)
The
updated_random.randint
function is generating a new random integer and returning
both that and the new state of the RNG, then we pass that back along with our
result.  We've made the random state variables immutable, and so it's functional.  But the
API is getting pretty ugly pretty quickly.
So JAX does something that is
equivalent, but a bit cleaner.  There's a concept of a
key
, which needs to be passed
into any function that consumes randomness:
That's kind of like the
random_state
that we have in the first version of the code above.
But it's immutable; when you use it, like this:
jax
.
random
.
randint
(
key
,
(),
1
,
11
)
...it will not be changed, so no matter how many times you call it with the same
key, that function will return the same value.  (Note that
jax.random.randint
takes an inclusive lower bound and an exclusive upper bound, like Python's
range
,
but unlike the stdlib's
random.randint
.  It also needs to know the shape of the
result --
()
for a scalar,
(1, 2)
for a 1x2 array, and so on.)
If you want it to "move on" to a new state, you use the
split
function, which
takes an existing key and returns two (or more) new ones.  So you can do something like this:
import
jax.random
def
f
(
x
,
key
):
return
x
+
jax
.
random
.
randint
(
key
,
(),
1
,
11
)
initial_key
=
jax
.
random
.
key
(
42
)
first_call_key
,
new_key
=
jax
.
random
.
split
(
initial_key
)
print
(
f
(
1
,
first_call_key
))
second_call_key
,
new_new_key
=
jax
.
random
.
split
(
new_key
)
print
(
f
(
1
,
second_call_key
))
Now, that
new_key
and
new_new_key
stuff is a bit ugly, but while it's not OK
to mutate the contents of variables in functional code, it's absolutely fine to assign a new value to
an existing one, so what I've found myself doing is writing stuff like this:
import
jax.random
def
f
(
x
,
key
):
return
x
+
jax
.
random
.
randint
(
key
,
(),
1
,
11
)
key
=
jax
.
random
.
key
(
42
)
first_call_key
,
key
=
jax
.
random
.
split
(
key
)
print
(
f
(
1
,
first_call_key
))
second_call_key
,
key
=
jax
.
random
.
split
(
key
)
print
(
f
(
1
,
second_call_key
))
However, there are more powerful ways to use
split
; I'm not confident enough at
using it yet to go into that, though, so I'll hold back for now.  I suspect (assuming I keep using JAX) I'll be
posting about them in the future.
OK: so the JIT means that we have to write functional code, which makes things a
bit fiddly -- no more global state.  And that has a surprisingly big knock-on effect
with randomness.
But there's another thing that comes out of the JIT and the way it does
tracing.  It's not a functional thing (though some of the docs seem to almost be
treating it that way), but is caused by the same kind of constraints.  It's not
part of my four theses above, but I think it's important enough to call out in
its own subsection.
3.5. Control flow and values
Imagine this function:
@jax
.
jit
def
f
(
x
):
if
x
>
2
:
return
x
**
2
return
x
print
(
f
(
10.0
))
It's purely functional, so no problem there.
But let's think about what the JIT is trying to do.  It wants to convert the function
into a simple sequence of operations, so it will create a tracer for
a floating-point scalar, then call
f
with it.
When it hits that
if
statement, there will be
a problem.  The tracer is meant to represent any arbitrary float, so should it take
the
if
branch or not?  There's no good answer.  It doesn't know which branch to follow
-- whether the sequence should be "square it and return the result" or just
"return it directly" --
and will fail with a somewhat obscure error message:
jax.errors.TracerBoolConversionError: Attempted boolean conversion of traced array with shape bool[].
So this gives a hard constraint on functions that you want to JIT: by default, they can't base
control flow on the values you pass in.  There is a workaround -- but it comes
with tradeoffs.  Let's take a slightly sideways route to explain it.
Firstly, although you cannot do control flow based on the
value
of a parameter -- which
the tracer doesn't know -- you
can base it on other information that actually is stored in the tracer.  Let's say that we called
f
like this:
f
(
jax
.
numpy
.
array
([[
1.
,
2.
],
[
3.
,
4.
]]))
The tracer that would be passed in when trying to trace the function would be
something representing a 2x2 array.  The
shape
of the parameter is part of the tracer, even
though the values aren't.  So you could do something like this:
@jax
.
jit
def
f
(
x
):
if
len
(
x
.
shape
)
>
1
:
return
x
**
2
return
x
...and it would work.  It's worth thinking explicitly why this is.
When you call
a JITted function, it will create a tracer that contains information about the type
of thing you passed in as a parameter -- scalar versus array, and if it's an array,
the array's shape.  It then runs the function with the tracer, gets the sequence of
operations, compiles them and then stores the result in a cache keyed on the metadata --
type and, if appropriate, shape -- that it used to create the tracer.
So when we call that function with a 2x2 array, we get a 2x2 array version, then if we
call it later with a one-dimensional array of length 2, we'll get a new version for that.
One workaround for basing control flow on values is essentially to tell the
jit
function
that it should treat the values of a particular variable as being like the metadata used
for this cache keying: it should
compile a new version for each value it sees, rather than just using the metadata.  It
takes a parameter
static_argnums
, and a matching
static_argnames
, which tell it
which parameters to do that with.  So, this will work:
from
functools
import
partial
@partial
(
jax
.
jit
,
static_argnums
=
(
0
,))
def
f
(
x
):
if
x
>
2
:
return
x
**
2
return
x
print
(
f
(
10.0
))
(Remember that the thing after the
@
for a decorator needs to be a function that
returns a function, so we have to use
partial
to "inject" in the extra argument.)
However, the downside is pretty clear: every time we call
f
with a new value, it's
going to have to JIT a new version of the function and cache it -- that's going to be slow
and take up memory.
So, as an alternative, we can use
the
jax.lax
package
.
This provides more functional-looking alternatives for control flow, which
are
compatible with the way the JIT works.  For example, there's a
cond
function, which
we can use to replace
if
s:
@jax
.
jit
def
f
(
x
):
return
jax
.
lax
.
cond
(
x
>
2
,
lambda
:
x
**
2
,
lambda
:
x
)
print
(
f
(
10.0
))
That feels a little bit like a workaround, but it does solve the problem.  How?  Well,
it's worth checking the JAXPR for it:
>>>
jax
.
make_jaxpr
(
f
)(
10.0
)
{
lambda
;
a
:
f32
[]
.
let
b
:
f32
[]
=
jit
[
name
=
f
jaxpr
=
{
lambda
;
a
:
f32
[]
.
let
c
:
bool
[]
=
gt
a
2.0
:
f32
[]
d
:
i32
[]
=
convert_element_type
[
new_dtype
=
int32
weak_type
=
False
]
c
b
:
f32
[]
=
cond
[
branches
=
(
{
lambda
;
e
:
f32
[]
.
let
in
(
e
,)
}
{
lambda
;
f
:
f32
[]
.
let
g
:
f32
[]
=
integer_pow
[
y
=
2
]
f
in
(
g
,)
}
)
]
d
a
in
(
b
,)
}
]
a
in
(
b
,)
}
What's happened here, I think, is that the JIT has recognised the call to
jax.lax.cond
as
being a primitive function in its intermediate language, so has just kept it in there.  It
couldn't do that with the
if
because when it was tracing, all JAX itself saw was what was
happening to the tracer -- there was a boolean comparison, and then the stuff in the chosen
branch happened.  The fact that there was an
if
there happened in Python itself, outside
JAX, so it was "invisible" to the trace.
That feels a little inelegant to me right now, and I'll come back to
it later.
Let's move on to the final difference between the two libraries that I want to cover: JAX's relative
minimalism to PyTorch's more maximalist approach.
4. Minimalism versus maximalism
I think the smaller size of JAX -- at least in terms of its API, if not in terms of
the JIT and XLA magic under the hood -- compared to the sprawl of PyTorch is not
entirely unrelated to the JIT being at its core.
PyTorch, after some initial design, has almost been forced to grow organically; JAX feels more carefully designed,
so it doesn't have the same
need
to grow (though of course it can).
The reason for PyTorch's growth is, at least in part, because
it needs to absorb optimisations.  If something is slow, someone needs to write a CUDA
kernel for it.  If there's a CUDA kernel, it needs an API.  And if it is generally useful, that API becomes part of
PyTorch.  Multi-head attention?
There's a class for that
.
SELU?
Yup
.
Very specific softmax approximations based on a paper published in 2016?
PyTorch has you covered
.
By contrast, JAX doesn't even have linear layers or optimisers in the framework
itself; if you want to use them, you can write them yourself (contraindicated), or
you can use
libraries built on top of JAX
, like
Flax
for common neural network components
and
Optax
for optimisers.
This feels like a nice division of responsibilities, and it also seems like something
that would have been very hard without the JIT.  So while the JAX core may well grow in the
future, the design it has now puts it in a good position to grow in a more planned,
well-designed manner -- rather than
having
to grow to absorb more and more abstractions
just to keep it fast.  Those abstractions can more easily sit in libraries written on
top of JAX.
Porting a toy PyTorch model to JAX
That's the 10,000-foot overview; four (or maybe four and a half) main differences
between PyTorch and JAX.  It's more maths-y, JITted, functional and minimalist.
What does that actually mean when you get down to coding with it?  Let's get
into the weeds with an example.
Let's use a really simple one: training a neural network with two inputs and one hidden
layer to calculate the XOR function.  The code is in
this GitHub repo
,
but I'll put the relevant bits here in this post.
Firstly, an idiomatic PyTorch implementation:
import
time
import
torch
data
=
[
([
0.
,
0.
],
[
0
]),
([
0.
,
1.
],
[
1
]),
([
1.
,
0.
],
[
1
]),
([
1.
,
1.
],
[
0
]),
]
class
XORModel
(
torch
.
nn
.
Module
):
def
__init__
(
self
):
super
()
.
__init__
()
self
.
layer1
=
torch
.
nn
.
Linear
(
2
,
2
,
bias
=
True
)
self
.
layer1_activation
=
torch
.
nn
.
Sigmoid
()
self
.
layer2
=
torch
.
nn
.
Linear
(
2
,
1
,
bias
=
True
)
self
.
layer2_activation
=
torch
.
nn
.
Sigmoid
()
def
forward
(
self
,
x
):
hidden
=
self
.
layer1_activation
(
self
.
layer1
(
x
))
output
=
self
.
layer2_activation
(
self
.
layer2
(
hidden
))
return
output
def
calculate_loss
(
model
,
inputs
,
target
):
result
=
model
(
inputs
)
return
((
result
-
target
)
**
2
)
.
mean
()
def
main
():
torch
.
manual_seed
(
42
)
model
=
XORModel
()
optimizer
=
torch
.
optim
.
SGD
(
model
.
parameters
(),
lr
=
0.1
)
start
=
time
.
time
()
for
epoch
in
range
(
10000
):
losses
=
[]
for
x
,
y
in
data
:
optimizer
.
zero_grad
()
loss
=
calculate_loss
(
model
,
torch
.
tensor
(
x
),
torch
.
tensor
(
y
))
loss
.
backward
()
losses
.
append
(
loss
.
item
())
optimizer
.
step
()
if
epoch
%
1000
==
0
:
avg_loss
=
sum
(
losses
)
/
len
(
losses
)
print
(
f
"Loss at epoch
{
epoch
}
:
{
avg_loss
:
.6f
}
"
)
end
=
time
.
time
()
print
(
f
"Trained in
{
end
-
start
:
.3f
}
s"
)
print
(
f
"Loss at end:
{
avg_loss
:
.6f
}
"
)
model
.
eval
()
with
torch
.
no_grad
():
for
x
,
y
in
data
:
result
=
model
(
torch
.
tensor
(
x
))
print
(
f
"
{
x
=}
:
{
result
=}
,
{
y
=}
"
)
if
__name__
==
"__main__"
:
main
()
If we run that, it trains a solid-looking model in about four seconds on my machine:
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pytorch_xor.py
Loss
at
epoch
0
:
0
.279327
Loss
at
epoch
1000
:
0
.254715
Loss
at
epoch
2000
:
0
.254279
Loss
at
epoch
3000
:
0
.253985
Loss
at
epoch
4000
:
0
.253649
Loss
at
epoch
5000
:
0
.251566
Loss
at
epoch
6000
:
0
.189219
Loss
at
epoch
7000
:
0
.030093
Loss
at
epoch
8000
:
0
.006666
Loss
at
epoch
9000
:
0
.003516
Trained
in
4
.154s
Loss
at
end:
0
.003516
x
=[
0
.0,
0
.0
]
:
result
=
tensor
([
0
.0483
])
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
tensor
([
0
.9567
])
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
tensor
([
0
.9425
])
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
tensor
([
0
.0434
])
,
y
=[
0
]
Now, if we're porting to JAX we need to do something about the fact that JAX doesn't
have optimisers and the neural network stuff built in.  If this was a real codebase,
we'd almost certainly do that by using the libraries built on top of JAX, like
Flax and Optax.  But for this toy example, I think it's more illustrative to strip
down the PyTorch version so that it uses fewer parts of the API -- essentially so that
it only uses the stuff that JAX has -- and then to port the result.
The optimiser first.
The code is here
but the diffs are pretty simple.  Instead of creating an optimiser, we just
specify our learning rate:
<     optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
---
>     learning_rate = 0.1
Instead of zeroing out the gradients using the optimiser, we can just ask the model
to do it:
<             optimizer.zero_grad()
---
>             model.zero_grad()
And instead of stepping the optimiser, we call a new
step
function passing in
the model and the learning rate:
<             optimizer.step()
---
>             step(model, learning_rate)
The
step
function is simple enough; we just switch into
no_grad
mode so that PyTorch
doesn't try to track the computation graph (working out gradients for applying gradients
and triggering some kind of crazy gradient-ception), then we just iterate over the model's
parameters and follow the normal SGD process, subtracting the
gradients times the learning rate:
def
step
(
model
,
learning_rate
):
with
torch
.
no_grad
():
for
p
in
model
.
parameters
():
if
p
.
grad
is
not
None
:
p
-=
p
.
grad
*
learning_rate
Running that on my machine actually works out slightly faster than the original !
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pytorch_xor_no_optimizer.py
Loss
at
epoch
0
:
0
.279327
Loss
at
epoch
1000
:
0
.254715
Loss
at
epoch
2000
:
0
.254279
Loss
at
epoch
3000
:
0
.253985
Loss
at
epoch
4000
:
0
.253649
Loss
at
epoch
5000
:
0
.251566
Loss
at
epoch
6000
:
0
.189219
Loss
at
epoch
7000
:
0
.030091
Loss
at
epoch
8000
:
0
.006665
Loss
at
epoch
9000
:
0
.003516
Trained
in
3
.806s
Loss
at
end:
0
.003516
x
=[
0
.0,
0
.0
]
:
result
=
tensor
([
0
.0483
])
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
tensor
([
0
.9567
])
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
tensor
([
0
.9425
])
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
tensor
([
0
.0434
])
,
y
=[
0
]
It's also quite nice to see that (within the bounds of the printing precision) the
loss and the final results are identical.
OK, so now that we've got rid of the optimiser, let's do the same with the
nn.Linear
s.
Here's the code
,
but let's do a quick walk through the differences.
Instead of creating an
XORModel
, we will just generate an array of layers:
<     model = XORModel()
---
>     layers = [
>         generate_layer_parameters(2, 2),
>         generate_layer_parameters(2, 1),
>     ]
Zeroing out the existing gradients will also need to be done on those layers:
<             model.zero_grad()
---
>             zero_grad(layers)
...and likewise our loss calculations and the
step
function will need to use them:
<             loss = calculate_loss(model, torch.tensor(x), torch.tensor(y))
---
>             loss = calculate_loss(layers, torch.tensor(x), torch.tensor(y))
58c76
<             step(model, learning_rate)
---
>             step(layers, learning_rate)
We used a couple of new helper functions there; this one generates the
initial weights for the layers (based on the
docs for
torch.nn.Linear
):
def
generate_layer_parameters
(
d_in
,
d_out
):
root_k
=
math
.
sqrt
(
1.
/
d_in
)
weights
=
(
torch
.
rand
(
d_out
,
d_in
)
*
2
*
root_k
)
-
root_k
biases
=
(
torch
.
rand
(
d_out
)
*
2
*
root_k
)
-
root_k
return
{
"weights"
:
weights
.
requires_grad_
(),
"biases"
:
biases
.
requires_grad_
(),
}
Note that each of the tensors we created, the
weights
and the
biases
need to be
explicitly told, using
requires_grad_
, that we're going to want PyTorch to track
gradients on them.
Zeroing out the gradients is just a case of chugging through each layer, and then for each
setting the weights' and the biases' gradients to
None
:
def
zero_grad
(
layers
):
for
layer
in
layers
:
for
p
in
(
layer
[
"weights"
],
layer
[
"biases"
]):
p
.
grad
=
None
Now, to calculate the loss, we're actually not changing much.  We had this:
def
calculate_loss
(
model
,
inputs
,
target
):
result
=
model
(
inputs
)
return
((
result
-
target
)
**
2
)
.
mean
()
...and now we just change it to this:
def
calculate_loss
(
layers
,
inputs
,
target
):
result
=
forward
(
layers
,
inputs
)
return
((
result
-
target
)
**
2
)
.
mean
()
That is, we've added on a new function
forward
to do a forward pass through the
given layers with the given parameters.  That looks like this:
def
forward
(
layers
,
inputs
):
x
=
inputs
for
layer
in
layers
:
x
=
torch
.
sigmoid
(
x
@
layer
[
"weights"
]
.
T
+
layer
[
"biases"
]
)
return
x
Standard NN stuff
.
A quick tweak to use
forward
in the printing of the results at the end:
<             result = model(torch.tensor(x))
---
>             result = forward(layers, torch.tensor(x))
...and we're done!
Let's run it:
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pytorch_xor_no_nn_helpers.py
Loss
at
epoch
0
:
0
.279327
Loss
at
epoch
1000
:
0
.254715
Loss
at
epoch
2000
:
0
.254279
Loss
at
epoch
3000
:
0
.253985
Loss
at
epoch
4000
:
0
.253649
Loss
at
epoch
5000
:
0
.251566
Loss
at
epoch
6000
:
0
.189218
Loss
at
epoch
7000
:
0
.030092
Loss
at
epoch
8000
:
0
.006665
Loss
at
epoch
9000
:
0
.003516
Trained
in
3
.504s
Loss
at
end:
0
.003516
x
=[
0
.0,
0
.0
]
:
result
=
tensor
([
0
.0483
])
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
tensor
([
0
.9567
])
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
tensor
([
0
.9425
])
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
tensor
([
0
.0434
])
,
y
=[
0
]
Even faster!  Sounds like there aren't any nice pre-baked optimisations in that part
of PyTorch, then...  But again, within the bounds of our precision, that's exactly the
same numbers as we got from the original PyTorch version, which is very reassuring.
OK, now that we've got something that's kind of JAX-shaped, let's port it over.  I think
it's worth showing all of the code for that (though it's
here on GitHub
if you want to view it there), and then I'll highlight the important diffs separately.
import
math
import
time
import
jax
import
jax.numpy
as
jnp
jax
.
config
.
update
(
"jax_platform_name"
,
"cpu"
)
data
=
[
([
0.
,
0.
],
[
0
]),
([
0.
,
1.
],
[
1
]),
([
1.
,
0.
],
[
1
]),
([
1.
,
1.
],
[
0
]),
]
def
generate_layer_parameters
(
key
,
d_in
,
d_out
):
weight_key
,
bias_key
=
jax
.
random
.
split
(
key
)
root_k
=
math
.
sqrt
(
1.
/
d_in
)
weights
=
(
jax
.
random
.
uniform
(
weight_key
,
shape
=
(
d_out
,
d_in
))
*
2
*
root_k
)
-
root_k
biases
=
(
jax
.
random
.
uniform
(
bias_key
,
shape
=
(
d_out
,))
*
2
*
root_k
)
-
root_k
return
{
"weights"
:
weights
,
"biases"
:
biases
,
}
def
forward
(
layers
,
inputs
):
x
=
inputs
for
layer
in
layers
:
x
=
jax
.
nn
.
sigmoid
(
x
@
layer
[
"weights"
]
.
T
+
layer
[
"biases"
]
)
return
x
def
step
(
layers
,
grads
,
learning_rate
):
layers
=
jax
.
tree
.
map
(
lambda
p
,
g
:
p
-
g
*
learning_rate
,
layers
,
grads
,
)
return
layers
def
calculate_loss
(
layers
,
inputs
,
target
):
result
=
forward
(
layers
,
inputs
)
return
((
result
-
target
)
**
2
)
.
mean
()
def
main
():
key
=
jax
.
random
.
key
(
42
)
layer_1_key
,
layer_2_key
=
jax
.
random
.
split
(
key
)
layers
=
[
generate_layer_parameters
(
layer_1_key
,
2
,
2
),
generate_layer_parameters
(
layer_2_key
,
2
,
1
),
]
learning_rate
=
0.1
start
=
time
.
time
()
for
epoch
in
range
(
10000
):
losses
=
[]
for
x
,
y
in
data
:
loss
,
grads
=
jax
.
value_and_grad
(
calculate_loss
)(
layers
,
jnp
.
array
(
x
),
jnp
.
array
(
y
))
losses
.
append
(
loss
.
item
())
layers
=
step
(
layers
,
grads
,
learning_rate
)
if
epoch
%
1000
==
0
:
avg_loss
=
sum
(
losses
)
/
len
(
losses
)
print
(
f
"Loss at epoch
{
epoch
}
:
{
avg_loss
:
.6f
}
"
)
end
=
time
.
time
()
print
(
f
"Trained in
{
end
-
start
:
.3f
}
s"
)
print
(
f
"Loss at end:
{
avg_loss
:
.6f
}
"
)
for
x
,
y
in
data
:
result
=
forward
(
layers
,
jnp
.
array
(
x
))
print
(
f
"
{
x
=}
:
{
result
=}
,
{
y
=}
"
)
if
__name__
==
"__main__"
:
main
()
If you look at it side-by-side with
the previous PyTorch implementation
,
you'll see that it's really similar!  Running
diff
between them makes them look
more different than they are because of the extra threading through of keys that we
need to do in order to satisfy the strict constraints on random number handling in JAX,
(and of course there are function name changes like
torch.rand
becoming
jax.random.uniform
and
torch.sigmoid
becoming
jax.nn.sigmoid
).  But the important changes are much smaller.
Firstly, weights and biases no longer need to know that we'll want to track gradients for them,
because that's all handled by the tracers that JAX wraps around them:
<         "weights": weights.requires_grad_(),
<         "biases": biases.requires_grad_(),
---
>         "weights": weights,
>         "biases": biases,
Relatedly, the
zero_grad
function that iterated over the layers and zeroed out
the existing ones is completely gone.  Because gradients are now stored on tracers
that wrap around our parameters rather than on the parameters themselves, we don't need to zero them out.
The step function is still there, though, but it's much simpler.
Before we get to that, let's take a look at the way we're getting the gradients for it,
in the main training loop.  Here's the diff:
<             loss = calculate_loss(layers, torch.tensor(x), torch.tensor(y))
<             loss.backward()
---
>             loss, grads = jax.value_and_grad(calculate_loss)(layers, jnp.array(x), jnp.array(y))
Hopefully the change there will be nice and familiar from the start of this post:
we've moved from the PyTorch procedural "do a forward pass then do the backward pass"
to the JAX maths-y "work out the gradients for this function".
value_and_grad
is
a utility function that does the same as the
grad
we encountered then, but rather than
just returning the gradients, it also returns
the value of
calculate_loss
with the given parameters,
which is useful for our logging.
Now, remember that
layers
is a list of dictionaries, something like this:
[
{
'biases': Array([-0.11810607, -0.58481467], dtype=float32),
'weights': Array([[-0.37359995,  0.6218162 ], [-0.4298191 ,  0.15088385]], dtype=float32)
},
{
'biases': Array([-0.49658495], dtype=float32),
'weights': Array([[-0.38409787,  0.6165393 ]], dtype=float32)
}
]
And also remember that
grad
-- and likewise
value_and_grad
-- have that smart trick
where they return the gradients in the same PyTree structure as the parameter that we're
taking the derivative with respect to.  So
grads
will also be a list of dictionaries,
each of which has
weights
and
biases
.
Now, as I mentioned earlier, JAX has a useful function called
jax.tree.map
.  Like the
Python
map
function that maps a function over one or more lists, JAX's version maps a function over one or
more things with the same PyTree structure.
So, because
layers
and
grads
have the same
structure, our
step
function can just use it to apply simple gradient descent
like this:
def
step
(
layers
,
grads
,
learning_rate
):
layers
=
jax
.
tree
.
map
(
lambda
p
,
g
:
p
-
g
*
learning_rate
,
layers
,
grads
,
)
return
layers
Very clean :-)
That's it!  A full JAX implementation of our toy example, and when we run it:
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pure_jax_xor_no_jit.py
An
NVIDIA
GPU
may
be
present
on
this
machine,
but
a
CUDA-enabled
jaxlib
is
not
installed.
Falling
back
to
cpu.
Loss
at
epoch
0
:
0
.267455
Loss
at
epoch
1000
:
0
.247348
Loss
at
epoch
2000
:
0
.061305
Loss
at
epoch
3000
:
0
.008652
Loss
at
epoch
4000
:
0
.004108
Loss
at
epoch
5000
:
0
.002627
Loss
at
epoch
6000
:
0
.001912
Loss
at
epoch
7000
:
0
.001496
Loss
at
epoch
8000
:
0
.001224
Loss
at
epoch
9000
:
0
.001034
Trained
in
104
.540s
Loss
at
end:
0
.001034
x
=[
0
.0,
0
.0
]
:
result
=
Array
([
0
.03008602
]
,
dtype
=
float32
)
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
Array
([
0
.97214633
]
,
dtype
=
float32
)
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
Array
([
0
.96557194
]
,
dtype
=
float32
)
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
Array
([
0
.02664344
]
,
dtype
=
float32
)
,
y
=[
0
]
...it works!  So, let's move on to...
Hang on:
Yikes.  It was almost 30 times slower than the PyTorch version.  But then -- we did
all of that work to port the code over to JAX, which is great because it has a JIT,
and then we didn't use the JIT.  Whoops!
Adding a few calls to
@jax.jit
helps.  If we add them to the
forward
,
step
and
calculate_loss
function then we get
this code
,
which is faster:
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pure_jax_xor_initial_jit.py
An
NVIDIA
GPU
may
be
present
on
this
machine,
but
a
CUDA-enabled
jaxlib
is
not
installed.
Falling
back
to
cpu.
Loss
at
epoch
0
:
0
.267455
Loss
at
epoch
1000
:
0
.247348
Loss
at
epoch
2000
:
0
.061305
Loss
at
epoch
3000
:
0
.008652
Loss
at
epoch
4000
:
0
.004108
Loss
at
epoch
5000
:
0
.002627
Loss
at
epoch
6000
:
0
.001912
Loss
at
epoch
7000
:
0
.001496
Loss
at
epoch
8000
:
0
.001224
Loss
at
epoch
9000
:
0
.001034
Trained
in
27
.663s
Loss
at
end:
0
.001034
x
=[
0
.0,
0
.0
]
:
result
=
Array
([
0
.03008603
]
,
dtype
=
float32
)
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
Array
([
0
.97214633
]
,
dtype
=
float32
)
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
Array
([
0
.96557194
]
,
dtype
=
float32
)
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
Array
([
0
.02664347
]
,
dtype
=
float32
)
,
y
=[
0
]
...but it's still almost eight times slower than the PyTorch code.
How can we make it faster?  Well, perhaps we can do more if we put more of the
loop into the JITted stuff.  Right now,
the core of our training loop looks like this:
for
x
,
y
in
data
:
loss
,
grads
=
jax
.
value_and_grad
(
calculate_loss
)(
layers
,
jnp
.
array
(
x
),
jnp
.
array
(
y
))
losses
.
append
(
loss
.
item
())
layers
=
step
(
layers
,
grads
,
learning_rate
)
calculate_loss
and
step
are JITted.  But what happens if we try to JIT a larger
step?  We can move the forward pass and the step into a JITted function on their own:
@jax
.
jit
def
train_step
(
layers
,
inputs
,
targets
,
learning_rate
):
loss
,
grads
=
jax
.
value_and_grad
(
calculate_loss
)(
layers
,
inputs
,
targets
)
layers
=
step
(
layers
,
grads
,
learning_rate
)
return
layers
,
loss
...and then call it in the loop like this:
for
x
,
y
in
data
:
layers
,
loss
=
train_step
(
layers
,
jnp
.
array
(
x
),
jnp
.
array
(
y
),
learning_rate
)
losses
.
append
(
loss
.
item
())
With that, all of the JAX code apart from input and target wrangling is moved into a JITted function.
We get
this code
, and running it gives us this:
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pure_jax_xor_final_jit.py
An
NVIDIA
GPU
may
be
present
on
this
machine,
but
a
CUDA-enabled
jaxlib
is
not
installed.
Falling
back
to
cpu.
Loss
at
epoch
0
:
0
.267455
Loss
at
epoch
1000
:
0
.247348
Loss
at
epoch
2000
:
0
.061305
Loss
at
epoch
3000
:
0
.008652
Loss
at
epoch
4000
:
0
.004108
Loss
at
epoch
5000
:
0
.002627
Loss
at
epoch
6000
:
0
.001912
Loss
at
epoch
7000
:
0
.001496
Loss
at
epoch
8000
:
0
.001224
Loss
at
epoch
9000
:
0
.001034
Trained
in
2
.432s
Loss
at
end:
0
.001034
x
=[
0
.0,
0
.0
]
:
result
=
Array
([
0
.03008603
]
,
dtype
=
float32
)
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
Array
([
0
.97214633
]
,
dtype
=
float32
)
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
Array
([
0
.96557194
]
,
dtype
=
float32
)
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
Array
([
0
.02664347
]
,
dtype
=
float32
)
,
y
=[
0
]
Woohoo!  Almost 45% faster than the PyTorch version :-)
So: porting to JAX alone gives us nice maths-y code, but we need to JIT it properly
to get performance that matches PyTorch.  (The fact that it's faster than PyTorch in this
case is not something
that I think you could rely on -- this is, after all, a toy example.)
It's also an interesting indicator that you actually need to think about
what to JIT.  My initial thought, "just whack an
@jit
on the inner stuff", was
not enough.  We needed to do more than that.  I've just had an interesting chat
with Claude Opus 4.8 about that, though, and will probably post more about it later.
For now, I think a useful rule-of-thumb is to wrap stuff in
@jit
at as high a level
as you reasonably can, to maximise coverage.
So, this completes the happy part of this post -- I've shown what it can do, how
nicely it maps to the maths, and how it's (relatively) easy to make it fast.  What
are the downsides?
Why JAX is doomed
Another deliberately overly-strident heading ;-)
I've been programming for more than 40 years, and working professionally in the tech
industry for more than 30.  I'd like to feel that this makes me a better engineer than
I was when I was first starting out, but I can confidently say that it has made me a
much more cynical one.
Over that period, I've come to categorise new APIs, languages, and tools into three
approximate groups: godawful hacks, solid but not overly inspiring engineering,
and things of beauty.  They're loose categories, and most things are somewhere between one
and another.  But I think they hold reasonably well.
My cynicism and experience tells me that:
Horrible hacks can inexplicably become popular, but
normally die off when people get tired of swearing at them.  (Though sometimes
a large installed base means that they linger.)
Things of beauty get people excited, and often pull in the best engineers.  But eventually,
they drop by the wayside.  Perhaps there's some hidden flaw that no-one noticed at the outset,
or perhaps the mental model you need to build in order to use them effectively
is too complicated for them to get to critical mass.
Solid, boring engineering wins in the long term.
When we were building our programmable spreadsheet,
Resolver One
,
some of the team pointed out that a functional language -- specifically,
Haskell
-- would be a better fit than Python.  It was
a tough decision to stick with Python, and I'm still not 100% sure it was the right one.
But I do remember having sales meetings with quants at various financial firms about it,
and in those meetings, some of the potential customers also suggested a Haskell port.
I'm not saying that there's a perfect correlation between where we heard that,
and the later notes in our sales status spreadsheet saying
"client being acquired by a non-bankrupt competitor, all expenditure on hold"
during the 2008 financial crisis.  But I'm not
not
saying that either.
If you've read this far, you can probably tell that I see PyTorch as solid engineering,
and JAX as closer to a thing of beauty.
Maybe it's just the cynicism of age, but let me try to articulate the things I worry
might put JAX into the "beautiful but doomed" side of the "beautiful" category.
Firstly, I'm not convinced by the way that JAX, with its JIT, requires you to try
to write Python as if it were a functional language.  It's easy enough to see that
this isn't functional:
@jax
.
jit
def
addY
(
x
):
return
x
+
y
...but harder with this:
def
f
(
x
):
return
x
+
random
.
randint
(
1
,
10
)
Even worse, the way that tracing works means that you have even more constraints
than "just" being functional would require -- remember this example from earlier?
@jax
.
jit
def
f
(
x
):
if
x
>
2
:
return
x
**
2
return
x
Python is not functional, and is deliberately so.  Trying to make it so is always going
to lead to weird bugs (for example, how the value of the global
y
on the first run
would be baked into that
addY
function) and hard-to-understand error messages (you
really need to be clued-up to work out what
Attempted boolean conversion of traced array with shape bool[]
means).
The
jax.lax
package -- for example, the
cond
function we used to
work around the fact that JAX could not "see" the Python
if
way back in this post --
feels like a bit of an ugly workaround.  Python has control flow functions, but they
don't work with the JIT's tracing, so we have to re-implement them in JAX.  Hmmm.
Now, I've written extensively above about how JAX's restrictions, however confusing, enable a lot
of the amazing stuff that wouldn't be possible in normal PyTorch.  What if there were
some way to write PyTorch code and compile it directly to something that can execute
on the hardware?
It turns out that as of 2023, there is:
torch.compile
.
From what I understand, you're meant to be able to just attach it to your code and
it gets JITted.  But unlike JAX, you don't need to restrict the code you write.  I've
not investigated in much depth (after all, this post is already absurdly long and
has taken more than a month on and off to put together), but it looks like it handles
stuff that can't be compiled by using a concept of a "graph break" -- that is, it happily
JITs what it can, then if it hits something that it can't JIT, it will cache the
"work so far" as one compiled unit, run the Python code for the unJITable stuff, then
(when it can) drop back into JIT mode.
The best of both worlds?  I don't know, and would need to spend much more time investigating
in order to learn.  But I can say that for my minimal-effort
port of my toy XOR code
,
following the structure of the JITted JAX version, it really did not help:
giles@perry:~/Dev/toy-pytorch-to-jax
(
main
)
$
uv
run
pytorch_xor_with_compile.py
Loss
at
epoch
0
:
0
.279327
Loss
at
epoch
1000
:
0
.254715
Loss
at
epoch
2000
:
0
.254279
Loss
at
epoch
3000
:
0
.253985
Loss
at
epoch
4000
:
0
.253649
Loss
at
epoch
5000
:
0
.251566
Loss
at
epoch
6000
:
0
.189218
Loss
at
epoch
7000
:
0
.030091
Loss
at
epoch
8000
:
0
.006665
Loss
at
epoch
9000
:
0
.003516
Trained
in
6
.688s
Loss
at
end:
0
.003516
x
=[
0
.0,
0
.0
]
:
result
=
tensor
([
0
.0483
])
,
y
=[
0
]
x
=[
0
.0,
1
.0
]
:
result
=
tensor
([
0
.9567
])
,
y
=[
1
]
x
=[
1
.0,
0
.0
]
:
result
=
tensor
([
0
.9425
])
,
y
=[
1
]
x
=[
1
.0,
1
.0
]
:
result
=
tensor
([
0
.0434
])
,
y
=[
0
]
For those who are keeping track, that's slower than the uncompiled version, which came
in at about 3.5s.  And the
issue doesn't seem to be an up-front cost of JITting that would be paid off if we ran
for more epochs -- each individual "Loss at epoch XXX" print comes out slower.
Again, for the sake of sanity I'm not going to dig into it further, especially given that
this is a tiny toy model and probably about as far from the target use case of
torch.compile
as you can get.  But it's something
well worth noting for the future.
Stepping back: one other way of looking at this is that Python might just be the wrong language
to try to build code that compiles to GPUs.  I'm learning JAX right now so that I
can re-implement my existing
LLM from scratch
project in something
other than PyTorch, to make sure that I really understand it.  I
asked people on X/Twitter for votes or ideas
,
and while JAX won,
Jeremy Howard suggested Mojo
.
Mojo
is a Pythonic language that compiles directly to
CPU or GPU code, so it explicitly only contains features that can be ported that way.
Unfortunately, it's lower-level than I really wanted for this project (and, importantly, does not
have built-in autograd support).
But if it did -- if, for example, there was a library like JAX for it, perhaps it would
be better than using Python as the foundation?  I've looked for something like that, but
to no avail.  Some work-in-progress projects, but nothing ready for use.
At the end of the day, I think further experience is essential if I'm going to come to a solid
opinion on JAX.  Experience with other tools can only get you so far, and it's easy
to fail by pattern-matching what you're looking at with things that you've seen before,
especially when you're old and cynical.
All I can say at this point is that JAX is making my "beautiful but doomed" spidey-sense
tingle.
Wrapping up
The title of this post is important -- it is my impressions on first looking into
JAX, not the considered thoughts of someone who's spent months or years working with
it.  I've only scratched the surface, and haven't even touched the larger JAX ecosystem,
or indeed its powerful handling of memory sharding for multi-GPU or even multi-node
setups (which may well be one of its biggest advantages).
My next step is going to be to implement a GPT-2-style LLM in JAX, probably using
Flax and Optax as helpers, and perhaps by the time I'm done with that I'll have changed
my views.
But at this point -- after working through the tutorials and porting some toy models
to get at least an initial feel for it, I've come to the conclusion that I like it.
The question is, do I like it like I liked Python when I first came to it -- "this thing
is really neat and clean, even if it has flaws" or is it more like I liked Haskell -- "this is
a stunning thing of beauty and is completely doomed in the real world"?
Time will tell.  But in the meantime, if you've been working with JAX for some time
and want to counter any of the points I made, if I've completely misunderstood
anything, or if you have any corrections, then please let me know!  After all,
explorers in areas new to them are prone to making mistakes from time to time...
The forest of Skund was indeed enchanted, which was nothing unusual on the
  Disc, and was also the only forest in the whole universe to be called -- in the
  local language -- Your Finger You Fool, which was the literal meaning of the word Skund.
The reason for this is regrettably all too common. When the first explorers
  from the warm lands around the Circle Sea travelled into the chilly hinterland
  they filled in the blank spaces on their maps by grabbing the nearest native,
  pointing at some distant landmark, speaking very clearly in a loud voice, and
  writing down whatever the bemused man told them. Thus were immortalised in
  generations of atlases such geographical oddities as Just A Mountain,
  I Don't Know, What? and, of course, Your Finger You Fool.
Rainclouds clustered around the bald heights of Mt. Oolskunrahod ('Who is this
  Fool who does Not Know what a Mountain is') and the Luggage settled itself
  more comfortably under a dripping tree, which tried unsuccessfully to strike up a conversation.
Terry Pratchett,
The Light Fantastic
