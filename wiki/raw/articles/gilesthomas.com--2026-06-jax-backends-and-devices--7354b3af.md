---
title: "JAX backends and devices"
url: "https://www.gilesthomas.com/2026/06/jax-backends-and-devices"
fetched_at: 2026-06-06T07:01:19.342949+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# JAX backends and devices

Source: https://www.gilesthomas.com/2026/06/jax-backends-and-devices

Archives
Categories
Blogroll
There's nothing like writing your own code with a framework to clarify how things
fit together!  Continuing with my port of my
PyTorch LLM code
to
JAX
, I wanted to load up a large dataset:
the 10,248,871,837 16-bit unsigned integers in the
train
split of
gpjt/fineweb-gpt2-tokens
.
That's just over 19GiB of data.
from
safetensors.flax
import
load_file
...
full_dataset
=
load_file
(
dataset_dir
/
f
"train.safetensors"
)[
"tokens"
]
When I ran that, I got a CUDA out-of-memory error:
jax.errors.JaxRuntimeError: RESOURCE_EXHAUSTED: Out of memory while trying to allocate 19.09GiB.
That makes sense!  The allocation it was trying to do is exactly the size of
the data I was trying to load.  I have an RTX 3090 with 24 GiB, but some is already used up by
the OS, various apps, and a model that the code creates earlier on.
But in PyTorch land, I was used to things being loaded into RAM by default, and only
moved over to the GPU when I asked it to do that.  JAX was clearly loading to the GPU
by default.  How could I stop it from doing that for this case?  The load into the GPU
was happening inside Safetensors, in code I couldn't directly control.
Understanding how to do it helped me understand a little bit more about JAX.
JAX has a function that looks relevant:
jax.devices
.
Without reading the docs, let's try running it.  In my virtualenv, with the
jax[cuda13]
package installed, I get this:
In
[
1
]:
import
jax
In
[
2
]:
all_devices
=
jax
.
devices
()
In
[
3
]:
all_devices
Out
[
3
]:
[
CudaDevice
(
id
=
0
)]
That seems a bit weird!  I do indeed have a CUDA device, but I also have a CPU, obviously.
Why isn't it showing up?
Running the same code in another virtualenv, with just
jax
installed -- no CUDA -- gets this:
In
[
1
]:
import
jax
In
[
2
]:
all_devices
=
jax
.
devices
()
An
NVIDIA
GPU
may
be
present
on
this
machine
,
but
a
CUDA
-
enabled
jaxlib
is
not
installed
.
Falling
back
to
cpu
.
In
[
3
]:
all_devices
Out
[
3
]:
[
CpuDevice
(
id
=
0
)]
OK, so it
did
recognise it this time.  Feels like it might be time to RTFM.
The
jax.devices
docs
explain things
a bit:
jax.devices(
backend=None
)
Returns a list of all devices for a given backend.
...
If
backend
is
None
, returns all the devices from the default backend. The
  default backend is generally
'gpu'
or
'tpu'
if available, otherwise
'cpu'
.
OK.  So JAX has multiple backends -- named that because they're classes of backend hardware that XLA
(the compiler behind the JIT) targets.  There is a default one, which is essentially
going to be the "best" one available given the hardware configuration and the parts of
JAX that are installed.
When I had the CUDA version installed, it made the
gpu
backend
default, but when I didn't, it defaulted to
cpu
(and warned me).  And because it
only shows the devices on the default backend, when that was
gpu
, I didn't see the CPU.
However, you can specify which backend you want to use with that
backend
parameter, so let's go back to the
virtualenv with CUDA:
In
[
4
]:
jax
.
devices
(
"cpu"
)
Out
[
4
]:
[
CpuDevice
(
id
=
0
)]
Great!  So is there some way to list which backends are available?
Apparently not
-- the recommended
way appears to be to try loading devices for the different possibilities, and
catch
RuntimeErrors
to see which ones aren't available.  Yuck.
But maybe that's not such a big deal.  In PyTorch-land I was very much used to putting
code like this near the start of my code:
device
=
torch
.
device
(
"cuda"
if
torch
.
cuda
.
is_available
()
else
"cpu"
)
...then moving models to the device:
...and then moving data to the model's device as needed:
device
=
next
(
model
.
parameters
())
.
device
...
inputs
=
inputs
.
to
(
device
)
What I actually wanted was essentially what JAX does -- have everything on the fastest
device available at all times -- but with specific exceptions.  In particular, the one
that started off this investigation: how would I put this huge array of training
data on the CPU's RAM rather than the GPU's VRAM?
I had a bit of a false start when I spotted that the
load_file
function in the
Safetensors FLAX API
has a
backend
parameter, but that appears to be more to do with how it loads up the file -- a backend
in a different sense.  And anyway,
backend
is not the right concept in JAX-land, as
the backend means just something generic like
gpu
-- for what we're trying to do, we want
to load it onto a specific
device
.
After some digging around, I discovered that JAX has a concept of a
default device
,
which is the one used when it doesn't have any
indication of where to put something.  It makes sense that this will be on the default
backend -- indeed, it looks like it's essentially "the first device in the list that
jax.devices
returns for the default backend".
There is a
jax_default_device
config option which
you can use to set it; you'd
normally use
jax.config.update
or an environment
variable to change it.
But what if you only want to change it temporarily?  I found
this documentation for
jax.default_device
.
The docs are more than a little confusing:
jax.default_device =
<jax._src.config.State object>
Context manager for
jax_default_device
config option.
Configure the default device for JAX operations. Set to a Device object (e.g.
jax.devices("cpu")[0]
) to use that Device as the default device for JAX
  operations and jit’d function calls (there is no effect on multi-device
  computations, e.g. pmapped function calls). Set to None to use the system
  default device.
That
=
near the start tripped me up, as I missed the words "Context manager" just
below, and the odd
State
type, and tried this:
jax
.
default_device
=
jax
.
devices
(
"cpu"
)[
0
]
full_dataset
=
load_file
(
dataset_dir
/
f
"train.safetensors"
)[
"tokens"
]
jax
.
default_device
=
None
I still got the CUDA OOM, though, so I reread the docs, spotted the "context manager" bit,
swore violently, and tried this:
with
jax
.
default_device
(
jax
.
devices
(
"cpu"
)[
0
]):
full_dataset
=
load_file
(
dataset_dir
/
f
"train.safetensors"
)[
"tokens"
]
...which works.  It looks like the equals sign in the docs is being used to mean something
very different to what you'd normally use it for, and they decided not to actually
document the signature of the context manager.  Heigh ho.  I guess
documentation is hard
.
Still, at least now I have a solution.  And as I said earlier, doc grumbles aside,
the shape of the code might wind up being a little less fiddly than PyTorch.  The
default location of things I create is the fastest hardware I have, which is what I want.
And for the rare exceptions when I don't want to use that, there is a reasonably
simple (now that I know it) way to say where I want things to go.
I'll call that a win :-)   The only thing I'll need to remember is that when, in
my training loop, I want to use subsets of that in-RAM tensor, I'll need to move them
to the GPU.
jax.device_put
looks
like the right tool for that.
