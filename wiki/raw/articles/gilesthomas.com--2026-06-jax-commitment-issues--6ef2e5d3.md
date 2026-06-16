---
title: "JAX: commitment issues"
url: "https://www.gilesthomas.com/2026/06/jax-commitment-issues"
fetched_at: 2026-06-16T07:00:49.368181+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# JAX: commitment issues

Source: https://www.gilesthomas.com/2026/06/jax-commitment-issues

Archives
Categories
Blogroll
Posted on 15
June 2026
in
AI
,
TIL
,
JAX
Imagine you have JAX code like this, and run it on a machine with CUDA set up:
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
cpu0
=
jax
.
devices
(
"cpu"
)[
0
]
with
jax
.
default_device
(
cpu0
):
array
=
jax
.
random
.
randint
(
key
,
(
530640
,
6
,
1024
),
0
,
50_000
,
dtype
=
jax
.
numpy
.
uint16
)
array
.
block_until_ready
()
item
=
array
[
0
]
item
.
block_until_ready
()
We're creating a big array, blocking until it's ready (JAX is asynchronous, so
this makes sure that it's actually finished creating it), then getting
the first item, and as a belt-and-braces thing making sure that that is ready too.
How long do you think those last two lines -- a simple retrieval of a 6 x 1024 array
from a larger one -- will take?  Some tiny fraction of a second would seem
reasonable.
But running it on my machine just now, the answer is a bit of a surprise: just over 5 seconds.  And if you try to
get
array[1]
immediately afterwards, it still takes about 1.2s.  Further lookups into
array
consistently take more than a second -- so while the larger
initial number might be something to do with setup -- maybe internal stuff being JITted -- that's clearly not the whole story.
Something is making these seemingly-simple array lookups take much longer than you'd
expect them to.
Let's dig into that.
A bit of background
First things first, why would you want to do that slightly strange dance with the
jax.default_device
context manager in the first place, rather than telling
randint
what
device you want to use (eg. with
out_sharding
)?
I'm writing some LLM training
code, and want to load my training dataset.  I don't want to load it into the VRAM
on the GPU -- that would be a waste of valuable GPU resources -- so I need it in
the CPU-side memory.  I'm using Safetensors, which will
load stuff onto the system's default device
.
So I need to override that temporarily to make sure that the dataset is loaded onto
the device where I want it.
I initially discovered this problem when I tried to iterate over the resulting array in my training
loop; the code above is a simplified version of that -- a minimal repro of the issue.
And it's a serious one!  If each iteration has an overhead of 1.2s just to get 6,144 tokens
ready for the model, JAX will max out at about 5,000 tokens per second
of training speed
just due to that overhead
-- a real forward and backward pass plus
an optimiser step will obviously make things even slower.  For comparison, my PyTorch training loop managed almost 20,000 tokens/second
on the same hardware: all steps from getting the training data, putting it on the GPU,
and doing the actual training.
Debugging
So, let's look at that code again.  We've created
our variable
array
on the CPU explicitly, and indeed if you print
array.device
,
it says
CpuDevice(id=0)
.  But if you print the device of the
item
, you get
CudaDevice(id=0)
.  What's worse, if you watch
nvtop
while the code is running,
as soon as it hits the lookup into the array, it starts using the GPU -- for each one,
there's a spike in GPU usage.
So, what gives?  We asked JAX to put the array on the CPU, but now it's doing
GPU work, and putting the items there.
The problem is that when you create an array using the
default_device
context manager,
it is placed on the specified device, but it's not
committed
to it.
If an array is not committed to its device, then JAX will feel free to move it
around to others.
In order to commit an array to a device, you need to use
jax.device_put
explicitly
stating which device you want it on.  Running
the same code, but with this:
array
=
jax
.
device_put
(
array
,
cpu0
)
...immediately before the lookup into the array changes the numbers drastically;
the first lookup takes about 0.95s on my machine, the second 0.0002s, and then
subsequent ones less than 0.0001s.
Some more detailed tests
I decided to exercise this in depth, and wrote
this script
.
If you run it without the
--commit
command line flag, it will create the array,
then iterate over the first ten items, measuring how long it takes to get each one.
Running it just now:
Getting the zeroth item from the array took about 5.4s.
Each subsequent one consistently took about 1.2s
With the
--commit
flag, it uses
device_put
to explicitly commit the array to the
CPU.  Running that:
Getting the zeroth item from the array took about 0.95s
Each subsequent one took less than 0.0002s.
Now, that didn't quite cover my use case -- what if, I wondered, the slow operation
was putting things onto the GPU?  The script also has a
--put_items_to_gpu
flag to
do that -- after getting each item, it uses
device_put
.  With that flag:
Getting the zeroth item from the array took about 0.86s, and putting it on the GPU took 0.02s.
Subsequent items had "get" times similar to the previous run,
and "put" times of about 0.0006s.
So, there's still a small startup penalty -- perhaps JAX is having to JIT some of
its internal stuff -- but a perfectly decent speed after that.  Commitment works!
Wrapping up
I'm still building my mental model of how JAX works, and working out exactly what
is going on here is proving a bit tricky.  The split between a committed and an
uncommitted array seems clear; the former is tied to a device, while JAX will move
the latter around as needed.
It also makes a certain amount of sense that it would want to move the items to the GPU;
it is, after all, the default device.  But I'm less clear on why that was so slow, compared
to the manual process of getting the item then putting it there.
Hypothesis: the array is on the CPU's RAM, but not committed there.  We ask for an item
from that array, and maybe JAX wants that to be on the default device, the GPU.  So it moves the entire
"parent" array there, extracts that item, and then returns that.  Then next time around
when we ask for the next item, it does the same thing again.
Plausible?  Maybe, but it does sound a bit pathological!
Anyway, at the end of the day, I have a solid new heuristic of my own: if you want something
to definitely be on some specific device, make sure that you nail it down there with
device_put
.  And then you won't have commitment issues like these.
