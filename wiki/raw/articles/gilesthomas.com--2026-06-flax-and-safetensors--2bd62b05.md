---
title: "Using Safetensors with Flax"
url: "https://www.gilesthomas.com/2026/06/flax-and-safetensors"
fetched_at: 2026-06-05T07:01:41.454729+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Using Safetensors with Flax

Source: https://www.gilesthomas.com/2026/06/flax-and-safetensors

Archives
Categories
Blogroll
I'm porting my
PyTorch LLM code
to
JAX
, using
Flax
as the neural network layer.
For various reasons I wanted to use
Safetensors
to store checkpoints of the model.  It took a little while to get it working;
here's the trick I learned.
If you look at the Safetensors docs, you'll see that it doesn't mention a JAX implementation --
indeed, searching for "safetensors jax" at the time I'm writing this gives you a link
to
this GitHub repo by Alvaro Bartolome
-- which was last updated in
2023.
However, if you look more closely at the docs, they
do
have a link to the
Flax API
.  I feel this is somewhat
misnamed, as it is actually a JAX API.  There's no reference (again, as of the time of
writing) to Flax in the source -- it's all just JAX code.  And in fact Bartolome's library
uses it under the hood.
There is one problem, though.  The API works with simple single-level dictionaries,
with strings mapping directly to JAX arrays.  For example, the
save_file
function has this
signature:
def
save_file
(
tensors
:
Dict
[
str
,
Array
],
filename
:
Union
[
str
,
os
.
PathLike
],
metadata
:
Optional
[
Dict
[
str
,
str
]]
=
None
,
)
->
None
This can cause problems if you're not careful.  If you look at the
Flax documentation on checkpointing
,
it suggests that you use
Orbax
,
which has its own API and file format, but then goes on to say:
When interacting with checkpoint libraries (like Orbax), you may prefer to work
  with Python built-in container types. In this case, you can use the
nnx.State.to_pure_dict
and
nnx.State.replace_by_pure_dict
API to convert an
nnx.State
to and from pure nested dictionaries.
I initially put two and two together -- that and the dictionary-based API
for Safetensors -- and got five, and tried feeding one of those "pure" dicts into
Safetensors.  I got a very confusing error:
SafetensorError: dtype object is not covered
It's worth digging in to why that happens.
The problem is that although Safetensors is expecting a dict of strings mapping to
tensors, it doesn't check that that is what it actually gets.  And while the dictionaries
from
nnx.State.to_pure_dict
are "pure", they are also nested (as the docs say!).  Even for the simple
model I was working with, I got a structure like this:
{
'output_head'
:
{
'kernel'
:
Array
([
...
],
dtype
=
float32
)
},
'token_embedding'
:
{
'embedding'
:
Array
([
...
],
dtype
=
float32
)
}
}
So, we had strings mapping to dicts, and those dicts mapped from strings to the JAX arrays.
More complex models would have had deeper dict structures.
Now, internally inside Safetensors, the Flax/JAX API is a simple wrapper.  It
iterates over the keys in the dictionary it's been provided with, and tries to convert
their respective values into NumPy arrays.  It does that by passing them into
NumPy's
asarray
function, which accepts things like lists, tuples, and NumPy arrays,
and converts them into arrays.  JAX's own
Array
class exposes an interface that it
recognises, so they're converted without trouble.
Once it's done that, it passes the result
to a lower-level Rust implementation that actually converts everything to Safetensors
format.
But because Safetensors didn't check types, in my case it was iterating over the top level of the
dict, trying to convert the values to NumPy arrays, and got something like this:
{
'output_head'
:
numpy
.
array
({
'kernel'
:
Array
([
...
],
dtype
=
float32
)},
dtype
=
object
),
'token_embedding'
:
numpy
.
array
({
'embedding'
:
Array
([
...
],
dtype
=
float32
)},
dtype
=
object
)
}
That is -- because it assumed that the values in the top-level dict were JAX
Array
s,
it blindly tried to convert them to NumPy arrays.  But they were dicts (that
happened to map from strings to arrays) -- and if you ask
asarray
to create an array based on
a random object, it happily does so and wraps that object in a NumPy array, with a
dtype
of
object
.
When that is then fed into the lower-level Rust code that is trying to write the
file, it encounters NumPy arrays that have a
dtype
it can't handle,
object
--
hence that error:
SafetensorError: dtype object is not covered
It all makes sense when you read through the code, but I was a bit perplexed for a while!
I think all this might be the reason why Bartolome created his GitHub
repo.  In the README, he says that:
There are no plans from HuggingFace to extend safetensors to support anything
  more than tensors e.g.
FrozenDicts
, see their response at
huggingface/safetensors/discussions/138
.
So the motivation to create
safejax
is to easily provide a way to serialize
FrozenDicts
using safetensors as the tensor storage format
However, you don't need to use that library to serialise simple Flax models.
Consider how PyTorch models get serialised to Safetensors; my LLMs have keys with names
like
out_head.weight
,
pos_emb.weight
, and
trf_blocks.0.att.out_proj.weight
.
They're "flat" dictionaries mapping strings to PyTorch Tensors, similar to what Safetensors
wants for these Flax ones, but they use dots to separate different levels, with integers
for list items and strings for field names.
Looking at the pure-dict structure I had for my model:
{
'output_head'
:
{
'kernel'
:
Array
([
...
],
dtype
=
float32
)
},
'token_embedding'
:
{
'embedding'
:
Array
([
...
],
dtype
=
float32
)
}
}
...you can see that you could walk the dictionary structure to generate keys like
output_head.kernel
and
token_embedding.embedding
.  That would be easy enough to code
up.
But -- as Adithya Dsilva
points out on GitHub
-- you can get there even faster by using
nnx.to_flat_state
.
That returns a (non-dict) structure like this:
FlatState
([
((
'output_head'
,
'kernel'
),
Param
(
# 786,432 (3.1 MB)
value
=
Array
([[
2.3581974e-02
,
3.0957451e-02
,
-
3.5088759e-02
,
...
,
-
4.5880198e-02
,
5.3717274e-02
,
-
2.6590331e-02
],
...
,
[
-
9.6302675e-03
,
-
3.3276502e-02
,
5.7173111e-02
,
...
,
-
7.9063717e-03
,
2.0532632e-02
,
5.4753982e-02
]],
dtype
=
float32
)
)),
((
'token_embedding'
,
'embedding'
),
Param
(
# 786,432 (3.1 MB)
value
=
Array
([[
0.00273973
,
-
0.01754938
,
0.04656043
,
...
,
-
0.04276522
,
-
0.03986642
,
-
0.00781331
],
...
,
[
0.01421758
,
-
0.0219186
,
-
0.01701825
,
...
,
-
0.00793659
,
0.00500103
,
0.03839901
]],
dtype
=
float32
)
))
])
If you iterate over that
FlatState
, you get tuples where the first element is that
tuple of strings, like
('output_head', 'kernel')
, and the second is a
Param
object wrapping
the JAX
Array
.
The tuples mirror the dot-separated string format in the PyTorch-style Safetensors files.
Param
objects also implement an interface that
asarray
can understand,
so you can quickly and easily convert the
FlatState
to a regular dict for Safetensors:
from
safetensors.flax
import
save_file
...
model_state
=
nnx
.
state
(
model
)
flat_state
=
nnx
.
to_flat_state
(
model_state
)
simple_dict
=
{}
for
tuple_key
,
param
in
flat_state
:
key
=
"."
.
join
(
str
(
key
)
for
key
in
tuple_key
)
simple_dict
[
key
]
=
param
save_file
(
simple_dict
,
"model.safetensors"
)
(You need to wrap
key
in a
str
because if you have a
nnx.Sequential
in your model, the
item in the tuple will get an integer index rather than a string).
You can go the other way pretty easily too; given a model, you can load the saved
checkpoint into it like this (because
from_flat_state
accepts raw JAX
Array
s
in place of explicit
Param
s):
from
safetensors.flax
import
load_file
...
simple_dict
=
load_file
(
"model.safetensors"
)
dict_flat_state
=
{}
for
key
,
array
in
simple_dict
.
items
():
elements
=
key
.
split
(
"."
)
list_key
=
[]
for
element
in
elements
:
try
:
list_key
.
append
(
int
(
element
))
except
ValueError
:
list_key
.
append
(
element
)
dict_flat_state
[
tuple
(
list_key
)]
=
array
new_flat_state
=
nnx
.
from_flat_state
(
dict_flat_state
)
nnx
.
update
(
model
,
new_flat_state
)
A little more work than I'd ideally like, but given that it can be tucked away
in general
save_checkpoint
/
load_checkpoint
functions, not too big a deal.
Hope that's of use for other people coming across this problem!
