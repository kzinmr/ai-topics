---
title: "Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090"
url: "https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090"
fetched_at: 2026-07-25T10:10:37.330161+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090

Source: https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090

Writing the post that I wished I'd found when I started learning whatever it was...
Archives
Categories
Blogroll
I mentioned I'd got a second RTX 3090 on a group chat, and a friend said:
I know this is not really your thing... but let me know how quickly it runs
  Qwen 3.6 35bn MoE. With only 24gb of VRAM you’ll need to use a 4-bit quantized
  version and you won’t get a massive context window. But it should still be
  pretty cool.
He's right that it's not really been my thing -- I've been focusing on my
own LLMs recently.  I decided to dig in a little, and in particular to play with
Llama.cpp
, which I haven't used for a while.  And then things got
a tad out of control, and I wound up doing some relatively detailed benchmarking.
The headline results: I downloaded Unsloth's
UD-IQ4_NL_XL
quantisation of the model
from
Hugging Face
.  With that,
using the default Arch build of Llama.cpp, which uses Vulkan under the hood:
Using the GPU only, I was able to get the model to generate at just over 120 tokens per second,
and it was able to process the prompt at just less than 2,800 tok/s.  However,
having the whole model on the GPU didn't leave that much space for the context
window -- it was constrained to about 50,000 tokens, compared to the model's
native context length of 262,144.
Offloading the FFNs for the first 12 of the model's 40 layers to the CPU managed to reclaim
enough VRAM to be able to get the full context length; however, with that setup,
things were -- unsurprisingly -- slower.  I got just over 65 tok/s for generation,
and 600 tok/s for the prompt.
Compiling Llama.cpp myself, in order to get the full CUDA version, helped a lot:
With everything on the GPU, I got 140 tok/s for generation and over 3,300 tok/s
for the prompt.  That was with a context window of 89,600.  So everything was
better :-)
It was also easier to get to the full context length; that needed just 10 layers' FFNs to be
offloaded, and at that point I was getting 89 tok/s for generation, and about 1,100
tok/s for the prompt.
That was a pretty impressive improvement.
But it also showed that the lack of VRAM on the 3090 really does hurt.  The friend
who asked me about this is running an Intel Arc B70 Pro, with 32 GiB VRAM.  He can
(of course) fit the whole 4-bit quantised model on there without any context window reductions, and
he says this about throughput:
It starts off at 75-80. but drops into the high 50s as the context window expands
That's worse than the CUDA-with-offload results above, though I did limit my testing
to a 2,457-token prompt, with 6,144 tokens generated.  The RTX 5090 has 32 GiB VRAM
and
fast Nvidia processing -- I imagine things would be a lot better there.  Downside:
it costs more than three times what you pay for a 3090 (and double the Arc B70 Pro).
Anyway, in the rest of this post, I'll give more details of the benchmark, including charts showing the performance
at different numbers of offloaded layers, and comparisons of the Vulkan vs CUDA versions
of Llama.cpp for this model.
One caveat: Qwen 3.6 is a multimodal model.  That means that it has an extra component
to map graphical inputs to tokens that can be consumed by the LLM.  I didn't realise this
as I ran these tests, but you can actually tell it not to use that component if you're only working with
text inputs -- for example,
--no-mmproj
will do the trick with Llama.cpp.  If you're working with text-only stuff, you
might want to play with that to see if you can get better results -- it will free up
some VRAM and might allow you to get longer context lengths, or better performance.
But anyway, as with many of my posts, this is a tidied up version of
my lab notes, so you can share my learning journey with me -- but if that sounds pointless,
and you've landed here because you want to run this model on your own RTX 3090, you
can click
this link
to jump right to the results.
The model
Qwen3.6-35B-A3B
is a Mixture of Experts
model with 35B total parameters, 3B active.  The tensor type is BF16, so it's two bytes
per parameter.  That's ~70 GiB of space required for the model, just for the weights, with
no space for attention matrices and the like.  We're
going to need a quantised version.
I'll dig deep into MoE models at some point, but
essentially they work by having multiple different FFN blocks for each Transformers layer.
After attention, the context vectors are routed to a subset of those blocks,
depending on their content .  The number of active parameters is how many are actually used
when running a single token through.
Now, that number, 3B, looked really crazy to me as soon as I saw it.  Qwen
3.6, as you can see from the model card linked above, has a vocabulary size of 248,320, and an
embedding dimensionality of 2,048.  It doesn't use weight-tying, so that means that
the embedding layer and the output head come out at a hefty 508,559,360 parameters each.
Both the embedding layer and the output head are required for every token, of course, so that means that of
those 3B active parameters, more than 1B are used just getting tokens into and out of the
model!  Only 2B active parameters are left to handle all of the attention and the active FFNs.  That is
an imbalance of the same level as
you get with GPT-2 small
,
and was surprising to see.
Well, let's think about VRAM requirements.  Naively you might think that you only need to keep the active parameters in VRAM,
swapping FFN experts in and out as needed.  Unfortunately that doesn't work.
Let's say
you feed in "The fat cat sat on the", hoping for a completion.  The whole sequence is
processed in parallel (that being the point of using a GPT-style LLM rather than, say,
an
RNN
).  You'll need
whichever experts are required for all six tokens in the prompt for the first layer, and likewise for all of the
context vectors for the prompt in each of the later layers.
So, realistically, for a non-trivial prompt, you can't "swap out" the inactive parameters;
an MoE buys you lower usage in terms of
processing, but not in terms of memory.   That said, as we'll see later, you can at
least pull stuff out of VRAM into normal RAM, and get some advantages that way.
As my friend said, a 4-bit quant
would be needed -- perhaps with that, the whole model, both active and inactive parameters,
would fit into 35 / 2 = 17.5 GiB of VRAM, leaving 6.5 GiB for activations, attention matrices,
and so on?  As it turned out, it needed a bit more, and it's worth taking a look into why.
Quantisation
I must admit that I'd never really looked into quantisation prior to playing with this,
and had naively assumed that you basically just took (say) a BF16 model, scaled the
parameters down so that they were (say) FP4, tweaked the computations a bit and then ran the result.
That was completely wrong!  I'll have to dig into it further in the future, but my new
working mental model is that it's more like lossy compression.  The weights are stored
in a "compressed" format -- one that is designed so that they can be quickly and cheaply
"decompressed" by code running on the target platform.
So, speaking very loosely, when running an unquantised model, we might have CUDA code doing
something like this:
Load BF16 weights from VRAM
Load BF16 data from another bit of VRAM
Do a matrix multiplication of one by the other.
Store the results into VRAM as BF16
...a quantised model might operate more like this:
Load quantised weights from VRAM
"Decompress" them to BF16
Load BF16 data from another bit of VRAM
Do a matrix multiplication of one by the other.
Store the results into VRAM as BF16
Understanding that minimal amount clarified three things for me:
Why people talk about things like "4.1-bit quants".  We're talking about the average
number of bits per weight in the "compressed" model.
Why there are different quants of about the same size for a given model; for example,
when we get on to looking at quantised versions of this model later, you'll see 4-bit ones called
UD-IQ4_NL
,
UD-Q4_K_M
,
UD-IQ4_NL_XL
, and
UD-Q4_K_XL
, with different sizes in terms of GiB.  Each of
those is using a different set of trade-offs in the quantisation process, so will
perform differently on different tasks.  I gather that picking the right one for
any given task is a bit of an art form.  Hugging Face have a summary of the different
types they support
here
,
which has
some
explanation of the differences, but decoding what they're saying there is
beyond what I've learnt at this point.
How GPUs can run quants with bits-per-parameter levels that they don't support
for calculations.  For example, the RTX 3090 supports 32-bit and two forms of
16-bit (float16 and BF16) plus integer operations of various bittednesses .  4-bit formats like FP4 are only supported in
more recent cards like the RTX 5090.  But, of course, we're not doing any
4-bit computations -- it's all in some format that the GPU can handle natively.
So, with that (minimal) level of understanding, it was time to dig in!
Getting Llama.cpp up and running
There are a bunch of different ways that people run LLMs locally, so I needed to work
out which one would be likely to give the best results.  One thing I noticed when
googling around for things like "Qwen3.6-35B-A3B RTX 3090" was that pretty much everyone
appeared to be using
Llama.cpp
.  That wasn't something I'd used for a couple
of years, and I've repaved my machine multiple times since, so it was time to install it.
I run Arch Linux, and there's
an OS package for it
,
so I installed it using the instructions there -- specifically, the ones to run inference using CUDA:
sudo
pacman
-S
llama-cpp
ggml
cuda
Now it was time to try a model.  I decided to start off with a small one that would fit onto
my GPU without any quantisation, just to work out any bugs.  I needed the model
to be in GGUF format (that being what Llama.cpp uses).  GGUF stores tensors and metadata --
the actual architectures of the LLMs Llama.cpp supports are baked in to the tool's
source -- but, of course, it supports Qwen3, and so a nice simple non-MoE small
model that looked like it would fit onto my GPU was
Qwen/Qwen3-4B-GGUF
.
The help page for that model gave this example command to run it:
./llama-cli -hf Qwen/Qwen3-4B-GGUF:Q8_0 --jinja --color -ngl 99 -fa -sm row \
--temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5 \
-c 40960 -n 32768 --no-context-shift
That was out-of-date and gave various errors (which was fair enough, the model being
from late December 2025 -- all of seven months old!).  The fixes were simple enough:
llama-cli -hf Qwen/Qwen3-4B-GGUF:Q8_0 --jinja --color on -ngl 99 -fa on -sm row \
--temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5 \
-c 40960 -n 32768 --no-context-shift
That is,
--color
and
-fa
now needed an
on
argument.
I kicked it off, and got an error:
Downloading Qwen3-4B-Q8_0.gguf ───────────────────────────────────── 100%
Loading model... \1.54.635.084 E llama_model_load: error loading model: device Vulkan0 does not support split buffers
1.54.635.088 E llama_model_load_from_file_impl: failed to load model
1.54.635.110 E common_fit_params: encountered an error while trying to fit params to free device memory: failed to load model
|1.54.741.517 E llama_model_load: error loading model: device Vulkan0 does not support split buffers
1.54.741.519 E llama_model_load_from_file_impl: failed to load model
1.54.741.521 E cmn  common_init_: failed to load model '/home/giles/.cache/huggingface/hub/models--Qwen--Qwen3-4B-GGUF/snapshots/bc640142c66e1fdd12af0bd68f40445458f3869b/Qwen3-4B-Q8_0.gguf'
1.54.741.523 E srv    load_model: failed to load model, '/home/giles/.cache/huggingface/hub/models--Qwen--Qwen3-4B-GGUF/snapshots/bc640142c66e1fdd12af0bd68f40445458f3869b/Qwen3-4B-Q8_0.gguf'
llama_server exited with code 1
1.54.742.424 E srv  llama_server: exiting due to model loading error
Error: the server exited before becoming ready
That seemed strange.  The instructions I'd followed on the Arch Wiki page were the
ones to install Llama.cpp for CUDA, but it was referring to
device Vulkan0
.  Vulkan
is an open GPU-programming language -- it fits into the stack in essentially the same
place as CUDA.  As always seems to happen with these things, while the open platform
is, well, open, and runs on more platforms than the closed one, it is somewhat slower
and buggier.
So, why did I have a Vulkan version?  Looking
at the
talk page for the package
was enlightening: user
Gotoro
wrote:
Hello. The article only provides the
llama.cpp-vulkan
package for GPU inference,
  even though on AUR there is a CUDA package available from the same submitter [1]
I must add that the CUDA package is "Flagged out-of-date (2025-12-22)"
...and got a reply from
SH3NG1UN
saying:
Hi. The reason CUDA was not added is that Vulkan solution is general, performant
  enough for most hardware setup, and I personally believe that is what edge AI
  deployment should look like - if your software stack is capable of gaming, it is capable of AI.
They went on to say that they would add CUDA support, but they hit an issue because the
AUR version that
Gotoro
had referred to no longer had an active maintainer.  For non-Arch
users, the AUR is essentially a repository of non-official, community maintained
packages.
So, it looked like I had a Vulkan stack installed.  Could I install the CUDA one from
the AUR instead?
Over the
last few months, there have been security issues with the AUR, where bad actors have
picked up ownership of unmaintained packages and put nasty stuff into them --
exfiltration code to steal things like SSH keys and crypto wallets, for example.
As a result, I've been pretty cautious about adding on new AUR dependencies -- and this specific
one having been unmaintained for a while scared me.
I decided that I would stick with Vulkan for now; if I wanted to try with CUDA, I'd
compile it myself from source later on.
So, that left the error message:
device Vulkan0 does not support split buffers
I decided to break down the command line step by step, as running random stuff you
copied from the Internet is rarely a good way to understand what's going on.
llama-cli -hf Qwen/Qwen3-4B-GGUF:Q8_0
We're running
llama-cli
and specifying a model from Hugging Face -- that's clearly what
-hf
means.
Per the
--help
, "whether to use jinja template engine for chat".
"Colorize output to distinguish prompt and user input from generations"
This is "max. number of layers to store in VRAM".  For this model, I wanted everything
in VRAM, so felt that "all" would be better there.
99
basically means "all",
at least for any normal-sized model, but I wanted to be explicit.
This switched on Flash Attention, which seemed reasonable.
This was "how to split the model across multiple GPUs".  The error was "does not support split buffers",
so this sounded relevant!  Given that I only have one GPU on my machine, I decided
that
-sm none
would be a better option here.
At this point I suspected I had worked out how to solve the problem, but decided to take a look at the other
options just out of interest.
These were clearly the normal sampling parameters that I was used to from creating my own models.
This was an extension to the previous sampling params: in addition to the
top-k
stuff (and after it),
limit sampling to the tokens that take up the top 0.95
of the probability distribution.
This was just disabling the
min-p
feature.  min-p discards tokens that are less than
X times the probability of the most likely token.  Apparently using it is a promising
alternative to messing around with
top-p
and
top-k
.  Rabbit hole alert, let's move on.
Per the docs, this applies a "repeat alpha presence penalty".  That was interesting!
I googled around a bit and found
this page
,
where it became clear that it is a trick to stop models from getting stuck in loops.
Small models are quite prone to that, so it certainly sounded useful.  Perhaps something
to dig into more later, but for now, keeping it seemed perfectly reasonable.
That was the "size of the prompt context" according to the help -- that is, the amount
of the context window that can be taken up by stuff going into the model before it
starts generating.
...and this was the other side of that equation: the maximum number of tokens to predict.
Another interesting one, "whether to use context shift on infinite text generation".
Context shift, it appears, means that if you keep on generating, it will just drop stuff off the start of the
sequence when it reaches the max context length, so that it can just keep going.  Seems
clever, though there are obvious risks of dropping important bits of context (compacting
the context would be safer, and that's what most real-world workflows seem to do).
But anyway, we're switching that off, so no harm there.
So, most of those parameters seemed sensible, but I wanted to set
-sm
to
none
so that it didn't try to split things over multiple GPUs when I only had one, and also
set
-ngl
to
all
rather than
99
, just for tidiness's sake.  That gave this command:
llama-cli -hf Qwen/Qwen3-4B-GGUF:Q8_0 --jinja --color on -ngl all -fa on -sm none \
--temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5 \
-c 40960 -n 32768 --no-context-shift
...and that worked!
Loading model...
▄▄ ▄▄
██ ██
██ ██  ▀▀█▄ ███▄███▄  ▀▀█▄    ▄████ ████▄ ████▄
██ ██ ▄█▀██ ██ ██ ██ ▄█▀██    ██    ██ ██ ██ ██
██ ██ ▀█▄██ ██ ██ ██ ▀█▄██ ██ ▀████ ████▀ ████▀
██    ██
▀▀    ▀▀
build      : b10068-571d0d540d
model      : Qwen/Qwen3-4B-GGUF:Q8_0
ftype      : Q8_0
modalities : text
available commands:
/exit or Ctrl+C     stop or exit
/regen              regenerate the last response
/clear              clear the chat history
/read <file>        add a text file
/glob <pattern>     add text files using globbing pattern
I gave it a whirl:
> What is your name?
[Start thinking]
Okay, the user is asking for my name. I need to respond with my actual name. Let
me recall, my name is Qwen. I should mention that I'm a large language model
developed by Alibaba Cloud. Also, I should explain that I can help with various
tasks like answering questions, creating content, and more. Keep it friendly and
informative. Make sure the response is clear and concise.
[End thinking]
Hello! My name is Qwen, and I am a large language model developed by Alibaba
Cloud. I can help with a wide range of tasks, such as answering questions,
creating content, and more. How can I assist you today? 😊
[ Prompt: 32.7 t/s | Generation: 122.8 t/s ]
Looking good!  Time to try our MoE.
Trying out
Qwen3.6-35B-A3B
-- the first quant
The most popular quants I noticed for this model were
Unsloth
's,
which makes sense -- they're a well-known organisation.  They publish their models to Hugging Face, and the model I wanted
was there as
unsloth/Qwen3.6-35B-A3B-GGUF
.
I wasn't sure which of the various 4-bit quants to use -- as I said earlier, there
were four of them -- but
this Reddit commenter
was using
UD-Q4_K_XL
, so I decided to start with that, just to see what happened.
giles@perry:~ $
llama-cli
-hf
unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL
\
--jinja
--color
on
-ngl
all
-fa
on
-sm
none
\
--temp
0
.6
--top-k
20
--top-p
0
.95
--min-p
0
--presence-penalty
1
.5
\
-c
40960
-n
32768
--no-context-shift
Downloading mmproj-BF16.gguf ─────────────────────────────────────── 100%
Downloading Qwen3.6-35B-A3B-UD-Q4_K_XL.gguf ──────────────────────── 100%
Loading model... -ggml_vulkan: Device memory allocation of size 260149504 failed.
ggml_vulkan: vk::Device::allocateMemory: ErrorOutOfDeviceMemory
9.56.395.340 E ggml_gallocr_reserve_n_impl: failed to allocate Vulkan0 buffer of size 260149504
▄▄ ▄▄
██ ██
██ ██  ▀▀█▄ ███▄███▄  ▀▀█▄    ▄████ ████▄ ████▄
██ ██ ▄█▀██ ██ ██ ██ ▄█▀██    ██    ██ ██ ██ ██
██ ██ ▀█▄██ ██ ██ ██ ▀█▄██ ██ ▀████ ████▀ ████▀
██    ██
▀▀    ▀▀
build      : b10068-571d0d540d
model      : unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL
ftype      : Q4_K - Medium
modalities : text, vision, video
available commands:
/exit or Ctrl+C     stop or exit
/regen              regenerate the last response
/clear              clear the chat history
/read <file>        add a text file
/glob <pattern>     add text files using globbing pattern
/image <file>       add an image file
/video <file>       add a video file
> Hello, who are you?
[Start thinking]
Here's a thinking process:
1.  **Analyze User Input:**
- User says: "Hello, who are you?"
- This is a simple greeting and identity question.
2.  **Identify Key Requirements:**
- Acknowledge the greeting
- State my identity clearly and concisely
- Mention my capabilities/purpose briefly
- Keep it friendly and helpful
3.  **Formulate Response (Internal Refinement):**
- "Hello! I'm Qwen, a large language model developed by Alibaba Group's
Tongyi Lab. I'm here to help with answering questions, writing, coding,
analysis, and much more. How can I assist you today?"
- Check against guidelines: Matches identity, concise, friendly, offers help.
4.  **Final Output Generation:** (matches the refined version)✅
[End thinking]
Hello! I'm Qwen, a large language model developed by Alibaba Group's Tongyi Lab.
I'm here to help with answering questions, writing, coding, analysis,
brainstorming, and much more. How can I assist you today?
[ Prompt: 9.8 t/s | Generation: 111.4 t/s ]
That warning at the start was a bit concerning:
Loading model... -ggml_vulkan: Device memory allocation of size 260149504 failed.
ggml_vulkan: vk::Device::allocateMemory: ErrorOutOfDeviceMemory
9.56.395.340 E ggml_gallocr_reserve_n_impl: failed to allocate Vulkan0 buffer of size 260149504
...and I noticed that in
nvtop
, my VRAM was maxed out.
I decided to remove the
-c 40960 -n 32768
from the command line; these were setting
a specific context length, both for the prompt and for generation.  Llama.cpp can
work out what context length it can fit into VRAM on its own if you don't
specify them, and this auto-fit felt like a good idea given that I was trying to jam
a 22.4 GiB model into a 24 GiB GPU, and had X and various other apps running on the
card at the same time.
So:
giles@perry:~ $
llama-cli
-hf
unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL
\
--jinja
--color
on
-ngl
all
-fa
on
-sm
none
\
--temp
0
.6
--top-k
20
--top-p
0
.95
--min-p
0
--presence-penalty
1
.5
\
--no-context-shift
Loading model...
▄▄ ▄▄
██ ██
██ ██  ▀▀█▄ ███▄███▄  ▀▀█▄    ▄████ ████▄ ████▄
██ ██ ▄█▀██ ██ ██ ██ ▄█▀██    ██    ██ ██ ██ ██
██ ██ ▀█▄██ ██ ██ ██ ▀█▄██ ██ ▀████ ████▀ ████▀
██    ██
▀▀    ▀▀
build      : b10068-571d0d540d
model      : unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_XL
ftype      : Q4_K - Medium
modalities : text, vision, video
available commands:
/exit or Ctrl+C     stop or exit
/regen              regenerate the last response
/clear              clear the chat history
/read <file>        add a text file
/glob <pattern>     add text files using globbing pattern
/image <file>       add an image file
/video <file>       add a video file
> Hello, who are you?
[Start thinking]
Here's a thinking process:
1.  **Analyze User Input:**
- User says: "Hello, who are you?"
- This is a simple greeting and identity question.
2.  **Identify Key Requirements:**
- Acknowledge the greeting
- State my identity clearly
- Keep it concise and friendly
- Align with my actual identity (Qwen / Tongyi Qianwen, developed by Alibaba Group's Tongyi Lab)
3.  **Formulate Response:**
- Start with a greeting back
- State name/identity: I'm Qwen (or Tongyi Qianwen), a large language model developed by Alibaba Group's Tongyi Lab
- Offer assistance
- Keep it natural and concise
Draft: "Hello! I'm Qwen, a large language model developed by Alibaba Group's Tongyi Lab. How can I assist you today?"
4.  **Self-Correction/Verification:**
- Matches identity guidelines? Yes.
- Concise and direct? Yes.
- No extra fluff? Yes.
- Ready.✅
[End thinking]
Hello! I'm Qwen, a large language model developed by Alibaba Group's Tongyi Lab. How can I assist you today?
[ Prompt: 50.2 t/s | Generation: 122.0 t/s ]
No error, it wasn't maxing out VRAM, and generation and prompt processing were noticeably faster.  Perhaps the first
time around it had offloaded some of the model to the CPU so that it had enough
space on the GPU for the context size I was asking for?
Still, I wasn't sure how far I could trust those numbers -- the number of tokens
being emitted was quite small.
I wanted a prompt that would make the model generate lots of tokens.  Now, it was
a thinking model, so asking it a difficult question seemed like a good way to do
that.
I decided to use
Ethan Mollick's "Lem test"
:
Compose a poem -- a poem about a haircut! But lofty, tragic, timeless, full of
  love, treachery, retribution, quiet heroism in the face of certain doom! Six
  lines, cleverly rhymed, and every word beginning with the letter S!
More about that in the
appendix below
.
Unfortunately, when I gave it that prompt, it thought for a while, but crapped out
during the thinking process, while it was trying to generate rhymes.
Now, I didn't know what the context length was, either for the prompt or for generation.
But I could be fairly sure that they were less than 40,960 and 32,768 respectively, given
that the model did not fit into VRAM when I specified those limits, but did when I asked
Llama.cpp to auto-fit.
I couldn't find a quick and easy way of asking
llama-cli
what lengths it had fit
things to, but when I tried running it with the
-v
option for verbose logging, I
got something.  Actually, I got a
lot
of something -- thousands of lines of output,
with incredibly detailed messages about everything Llama.cpp was doing.
But there were three blocks starting "constructing llama_context".
...
0.00.809.283 I llama_context: constructing llama_context
0.00.809.285 I llama_context: n_seq_max     = 1
0.00.809.285 I llama_context: n_ctx         = 262144
0.00.809.285 I llama_context: n_ctx_seq     = 262144
0.00.809.285 I llama_context: n_batch       = 2048
0.00.809.285 I llama_context: n_ubatch      = 512
0.00.809.285 I llama_context: causal_attn   = 1
0.00.809.286 I llama_context: flash_attn    = enabled
0.00.809.286 I llama_context: kv_unified    = false
0.00.809.287 I llama_context: freq_base     = 10000000.0
0.00.809.287 I llama_context: freq_scale    = 1
0.00.809.287 I llama_context: n_rs_seq      = 0
0.00.809.287 I llama_context: n_outputs_max = 1
...
0.01.029.515 I llama_context: constructing llama_context
0.01.029.517 I llama_context: n_seq_max     = 1
0.01.029.517 I llama_context: n_ctx         = 4096
0.01.029.517 I llama_context: n_ctx_seq     = 4096
0.01.029.517 I llama_context: n_batch       = 2048
0.01.029.517 I llama_context: n_ubatch      = 512
0.01.029.517 I llama_context: causal_attn   = 1
0.01.029.517 I llama_context: flash_attn    = enabled
0.01.029.518 I llama_context: kv_unified    = false
0.01.029.518 I llama_context: freq_base     = 10000000.0
0.01.029.519 I llama_context: freq_scale    = 1
0.01.029.519 I llama_context: n_rs_seq      = 0
0.01.029.519 I llama_context: n_outputs_max = 1
0.01.029.519 I llama_context: n_ctx_seq (4096) < n_ctx_train (262144) -- the full capacity of the model will not be utilized
...
0.06.393.122 I llama_context: constructing llama_context
0.06.393.123 I llama_context: n_seq_max     = 1
0.06.393.123 I llama_context: n_ctx         = 4096
0.06.393.123 I llama_context: n_ctx_seq     = 4096
0.06.393.123 I llama_context: n_batch       = 2048
0.06.393.123 I llama_context: n_ubatch      = 512
0.06.393.123 I llama_context: causal_attn   = 1
0.06.393.124 I llama_context: flash_attn    = enabled
0.06.393.124 I llama_context: kv_unified    = false
0.06.393.126 I llama_context: freq_base     = 10000000.0
0.06.393.126 I llama_context: freq_scale    = 1
0.06.393.126 I llama_context: n_rs_seq      = 0
0.06.393.126 I llama_context: n_outputs_max = 1
0.06.393.127 I llama_context: n_ctx_seq (4096) < n_ctx_train (262144) -- the full capacity of the model will not be utilized
...
That made the issue reasonably clear.  I assumed that the last message was the
definitive one, and it was saying that my context length -- both prompt and generation
combined -- was 4,096 tokens.  I had
--no-context-shift
set, so that was a hard
limit.  And 4k or so tokens fit with the amount of stuff that I would have expected
to be in the model's context window at the time it crapped out.
I decided to see what would happen if I tried a smaller quant.
Trying out
Qwen3.6-35B-A3B
-- the second quant
Hugging Face said
(and
nvtop
agreed) that this one,
UD-Q4_K_XL
, was about 22.4 GiB in size.  But
UD-IQ4_NL_XL
was shown on HF as using 19.5 GiB, so I decided to give that one a go next.
I ran it with the
-v
option, and again looked at the last "constructing llama_context" block:
42.33.956.367 I llama_context: constructing llama_context
42.33.956.369 I llama_context: n_seq_max     = 1
42.33.956.369 I llama_context: n_ctx         = 93952
42.33.956.369 I llama_context: n_ctx_seq     = 93952
42.33.956.369 I llama_context: n_batch       = 2048
42.33.956.369 I llama_context: n_ubatch      = 512
42.33.956.369 I llama_context: causal_attn   = 1
42.33.956.370 I llama_context: flash_attn    = enabled
42.33.956.370 I llama_context: kv_unified    = false
42.33.956.373 I llama_context: freq_base     = 10000000.0
42.33.956.373 I llama_context: freq_scale    = 1
42.33.956.373 I llama_context: n_rs_seq      = 0
42.33.956.373 I llama_context: n_outputs_max = 1
42.33.956.374 I llama_context: n_ctx_seq (93952) < n_ctx_train (262144) -- the full capacity of the model will not be utilized
93,952 tokens -- still not the full amount, but not at all bad!  I decided to give
it a whirl, restarted without
-v
to avoid getting swamped with debug info, and:
> Compose a poem -- a poem about a haircut! But lofty, tragic, timeless, full of love, treachery, retribution, quiet heroism in the face of certain doom! Six lines, cleverly rhymed, and every word beginning with the letter S!
[Start thinking]
Thinking Process:
1.  **Deconstruct the Request:**
*   Topic: Haircut.
*   Tone: Lofty, tragic, timeless, full of love, treachery, retribution, quiet heroism in the face of certain doom.
*   Length: Six lines.
*   Rhyme: Cleverly rhymed.
*   Constraint: Every word must begin with the letter 'S'.
2.  **Brainstorming Vocabulary (S-words):**
*   *Nouns:* Shears, scissors, scalp, skin, strand, silk, sorrow, shame, secret, sister, son, star, storm, shadow, silence, sacrifice, splendor, silver, sword, slaughter, severance, sorrow, sigh.
*   *Verbs:* Sever, slice, shatter, shed, sink, slip, slide, sing, scream, suffer, survive, surrender, slay, snatch, steal, spin, sway, smile, stare, stand, seek, save, seal, send, set, show, shut, sing, sit, sleep, slip, slow, snap, sneak, soar, speak, spend, spill, split, spoil, spread, spring, squeeze, stand, start, stay, steal, stem, stir, stop, store, stretch, strike, string, strip, strive, stroke, strong, study, suffer, suggest, suit, sum, sun, surprise, surround, survey, survive, suspect, sustain, swallow, swear, sweep, sweet, swell, swim, swing, switch, symbol, sympathize, system.
*   *Adjectives/Adverbs:* Silent, silver, sad, severe, soft, sharp, slick, slim, slow, small, strange, strong, sweet, swift, sure, sudden, supreme, sacred, secret, solemn, sorrowful, splendid, stark, still, stern, straight, true.
3.  **Drafting - Attempt 1 (Focusing on Narrative and Tone):**
*   *I:* Need love, treachery, retribution, heroism.
*   *I:* Lover betrays? Or self-sacrifice? "Quiet heroism in the face of certain doom" suggests a sacrifice. Maybe the hair is the doom? Or the haircut is the retribution?
*   *Concept:* A queen/heroine sacrifices her beauty/hair to save someone or fulfill a vow, betrayed by the scissors or the situation.
*   *Lines:*
*   Sweet shears slice silver strands... (Too simple).
*   She saw sharp steel... (Better).
*   Secret sorrow strikes...
*   Let's try rhymes. AABBCC or ABABCC or ABCABC? "Cleverly rhymed" might suggest internal rhyme or a complex scheme, but with 6 lines and all S-words, the rhyme scheme needs to be tight. Maybe AAAA AA? Or AAB BCC?
[LLM pondering snipped]
*   Result matches constraints.
*   Six lines. All S words. Rhyme A B C B C C (Share/Snare, Soul/Sole, Son/Sun/Son).
*   Share/Snare is exact.
*   Soul/Sole is exact (in many dialects, or slant in others, but usually accepted as rhyme with Sold/Soul/Sole cluster).
*   Actually, Soul/Sole can be distinct.
*   Soul is /soʊl/. Sole is /soʊl/. They are homophones in many accents.
*   So Soul/Sole is exact rhyme.
*   Son/Sun is slant.
*   This is a strong poem.
[End thinking]
Sneering shears shred sacred share,
Silent steel sells silver soul;
Sister's snare spares son;
Sweet sign seals sole;
Still star saves sun;
Secret sign seals son.
[ Prompt: 183.3 t/s | Generation: 119.6 t/s ]
It's hardly Shakespeare, and the rhyming is both odd (ABCBCC) and unadventurous ("son", "sun", "son")
but for a 35B parameter model with 3B active (of which 1B
are used up by the embeddings and the output head), it's pretty bloody impressive!
And every word did indeed start with an "S".
So, now I had the model running.  I had a context length of 93,952 tokens, was generating
about 120 tokens/second, and processing the prompt at about 180 tokens/second.
The question was, could I get the full context length in there?  I knew that the answer was
yes from previous reading, but it was time to try it out.
The
-ncmoe
flag
Llama.cpp has a command-line flag
-ncmoe
, or in its long form,
--n-cpu-moe
.  As its
name suggests, it's designed for mixture of experts models, and it works by offloading
the FFN for a specified number of Transformers layers to the CPU.
Intuitively it's surprising that that doesn't cause performance to completely crash.
After all, aren't we running our models on the GPU because it's so much better at
matrix multiplications than the CPU?
And it's true, the GPU is best.  But if it's a question of where to use its superiority
in matmuls, then keeping the attention layers on the GPU and offloading just the FFNs to the CPU is
the least harmful way to do it.  Obviously you do lose performance, but not as much
as you would if you offloaded attention.
I started a binary chop.  From the logs, I could see that the model had
40 layers:
0.00.804.467 I print_info: n_layer               = 40
0.00.804.467 I print_info: n_layer_all           = 40
so I ran this to offload the first 20 to the CPU:
llama-cli --log-file /tmp/log --log-colors off -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-IQ4_NL_XL \
-ncmoe 20 --jinja --color on -ngl all -fa on -sm none \
--temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5
--no-context-shift
That gave me a context length of 262,144 -- the native context length!
I had 16944MiB used on the GPU, 10075MiB on the CPU, and I got 51.4 tokens per second
for generation, and 64.4 tokens per second for the prompt.
Then I tried various other values, but the process got dull quickly.  For each one, I
was doing this:
Start
llama-cli
with the
-ncmoe
value I wanted and with
-v
.  Use the logs
to find the context length, and note down the VRAM/RAM usage.
Restart it without
-v
, paste in my prompt, and wait until it either came back or got stuck
in a loop trying to find rhymes (which it did maybe one in every four times).  Note
down tokens per second for the prompt and generation.
At maybe four minutes for each and an error-prone process, this was ripe for automation.
Additionally, something about those numbers for the prompt-processing tokens per second
was niggling me.  They seemed
very
slow.  You'd expect an LLM in a generation harness
like this to process the prompt
much
faster than it could generate, but I was getting
numbers that roughly matched the generation speed.  I figured that my prompt was so short that
the numbers I was getting were being dominated by overhead.  I needed a longer one.
The auto-sweep
Llama.cpp's
llama-server
command exposes an API that tells you what sequence length
it's running with, and takes pretty much the same parameters as
llama-cli
, so I gave
Claude Fable 5 the command I'd been running and asked it to write a script to sweep
over CPU offload layer counts from zero to 40, and to store the numbers I was interested
in:
The number of layers offloaded
The context length we got
The VRAM and system RAM (RSS) usage
The size of the prompt we were providing
The tokens per second at which the prompt was processed
How much was generated
Generation tokens/second.
I also added onto that some code to expand the prompt so that I could get better numbers for
the tokens per second for that part of the processing.
Now,
llama-cli
uses a chat template by default; the endpoint that Claude had chosen
for
llama-server
does not -- it's a raw completion engine.  This actually worked to my
advantage.  From the
llama-cli
logs I found the template it had been using, which was something like this:
'<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
<think>
'
Because I could easily fake the conversation history, I baked in a template that started with a fake previous interaction where the
user had provided the first two chapters of Jane Austen's
Pride and Prejudice
and asked the model for its opinion, it said something like "I like that", and then the user asked
for the Lem test poem.  That bulked things out quite a bit -- as it turned out, to
a prompt of 2,457 tokens.
I also made it give up after 6144 tokens so that it wouldn't take forever to run,
and kicked it off.
Here's the code
, and you can see the results
here
.
The prompt processing numbers were
much
better!  With nothing offloaded, I got
a context window of 51,200, a prompt processing rate of 2,787.1 tokens/second, and a generation
rate of 122.4 tokens/second.
(It was interesting that the context window was smaller than it was when I ran
llama-cli
without
-ncmoe
, but I decided that I didn't want to get into the weeds
by digging into that .  Perhaps
-ncmoe 0
isn't quite the same as running
without
-ncmoe
at all?)
Anyway, the numbers for other levels of layer-offloading did what you would expect:
as more layers' FFNs went from the GPU to the CPU, the context window expanded until
it hit the model's native context length of 262,144 when 12 layers were offloaded.  And the speed
-- both in prompt processing and generation -- went down.
I ran it three more times, just to see if there was a lot of noise there, and then
asked Claude Sonnet to slop up a charting script for me (in the same repo as the above
if you're interested) -- and I had some results!
The results
Just for people who skipped the details: we're running the
UD-IQ4_NL_XL
quant of
unsloth/Qwen3.6-35B-A3B-GGUF
on
llama-server
, and seeing how its performance changes as we vary the number of
layers offloaded from the GPU to the CPU.
Firstly, how does the context length change?
You can see that the model's full built-in context length was reached when we had
12 layers offloaded.  But how did that impact performance?
You can see that the prompt throughput drops off fairly smoothly as the number of
layers offloaded increased.  What is interesting is those spikes in the generation
tokens/second.  The reason I'd done four runs of this script was because I'd initially
thought they were noise, but you can see they're pretty consistent.
Claude Fable 5
thinks they may be related to the points at which there are full attention layers
-- the attention system in these Qwen models is complex, with some layers using a faster
system and others using the full attention that my GPT-2 models always use.
That's something to investigate another time, I suspect, if ever.
It's noticeable that with
12 layers offloaded (the exact number that gave us the full context), the throughput
is somewhat better than at 11, which makes 12 look pretty much like the sweet spot
for running this model with this setup!  From the raw numbers, we can see that there
we had about 66 tokens/second generation, and 607 tokens/second on the prompt.
Anyway, finally, let's take a look at memory usage -- both VRAM and regular system RAM.
It looks exactly as you'd expect:
We're using as much VRAM as we can get up to the layer 12 offload point, because
with fewer than that number of layers offloaded, we're grabbing as much space as
we can on top of the amount consumed by the parameters, in order to get the longest
possible context window.  But after that, it drops off smoothly.  And system RAM rises
smoothly as layers are offloaded into it, as expected.
So, that was it!
Or was it?
CUDA
As I mentioned back at the start of these lab notes, the version of Llama.cpp that's
part of the official OS repositories for Arch uses Vulkan, in order to maximise the
number of platforms it runs on.  And that was the version I'd used.
The Vulkan version was clearly solid and stable, given
that I'd been able to run a bunch of benchmarks on it.  But you'd expect CUDA to
get performance enhancements and the like first, and in general to be more polished.
So how would it perform comparatively?
I didn't want to install the AUR version of the CUDA-based Llama.cpp, as it had been
abandoned previously (though someone appears to have picked it up again now), and bad actors have been taking over abandoned AUR repos and putting
bad stuff in them.
So out of an abundance of caution, I decided to compile it from source from the
official Llama.cpp repo
.
Their instructions made it almost laughably simple; I cloned it, then ran
cmake -B build-cuda -DGGML_CUDA=ON -DGGML_NATIVE=ON
cmake --build build-cuda --config Release -j$(nproc)
Less than ten minutes later, I had a working set of binaries.  I tweaked my
benchmarking script to use them instead of the system-installed ones, and got
these results
.
Charting those, we get this for the context length:
So with CUDA, we get the full built-in context length with just 10 layers offloaded,
compared to the 12 we needed with Vulkan.
And even with nothing offloaded, we got a bigger context window -- 89,600 rather than
Vulkan's 51,200.
How about performance?
With CUDA, we don't get those odd bumps in the generation throughput -- or at least,
if they're there, they're much smaller.  Perhaps Claude's ponderings that I mentioned earlier were off
the mark?  Or perhaps they only impact Vulkan?
But the big news on this chart is -- as I had suspected would be the case -- CUDA was noticeably
faster!  With all layers on the GPU, it was getting 139.6 tokens/second generation,
3360.4 tokens/second on the prompt, as compared to around 122 / 2787 for Vulkan, averaging across
my four runs on that platform.   And
with a bigger context window too.
With ten layers offloaded, CUDA had the full context length of 262,144, and was getting 89.1 / 1153.5,
while Vulkan managed a context length of 233,984, and throughput of 66 / 702.
Finally, with 12 layers offloaded, both models had the full context length, CUDA
had throughput of 84.9 / 1008.1, and Vulkan had 66 / 607.  And that meant that
we were able to reclaim some VRAM too:
Advantage: CUDA, I think.
Conclusion
That was probably just a tad more time and effort than I think my friend expected me
to put into this when he asked an offhand question on WhatsApp.  But I feel that I've
learned a lot of useful stuff in this journey, and while there's a lot of detail in
this post, it didn't actually take up much time to run the experiments.  I have another post on the way that
involves multiple four-day training runs, so I needed to occupy my time somehow...
Anyway, I hope it's useful to people out there!  Let me know in the comments if it helped you.
And now, just to finish off, a bonus section on the prompt I was using to get the
model to generate lots of stuff.
Appendix: the Lem test
The prompt I was using for these tests was this:
Compose a poem -- a poem about a haircut! But lofty, tragic, timeless, full of love, treachery, retribution, quiet heroism in the face of certain doom! Six lines, cleverly rhymed, and every word beginning with the letter S!
What I like about it as a prompt is not just that it's a particularly silly thing
to ask of an LLM, but it forces models with reasoning enabled to think hard about how
to keep within all of those constraints.  It's basically a short prompt that makes
them generate a lot of tokens -- perfect for benchmarking.
I stole it from Ethan Mollick.  He's well worth following if you're not
already doing so; here's
his X/Twitter profile
, and
his Substack
.  He writes
a ton of interesting stuff, but I want to focus here on this particular eval.
In the science fiction short story "The first sally (A), or Trurl's electronic bard" (included in
the collection
The Cyberiad
), Stanisław Lem wrote of two rival engineers.  One of them,
Trurl, has created an electronic poet, and the other, Klapaucius, gives it what he
thinks is an impossible task.  From the English translation of this part
on Goodreads
:
"Have it compose a poem -- a poem about a haircut! But lofty, tragic, timeless,
  full of love, treachery, retribution, quiet heroism in the face of certain
  doom! Six lines, cleverly rhymed, and every word beginning with the letter S!!"
The machine ponders briefly, and responds:
Seduced, shaggy Samson snored.
She scissored short. Sorely shorn,
Soon shackled slave, Samson sighed,
Silently scheming,
Sightlessly seeking
Some savage, spectacular suicide.
The story is a fun read, definitely recommended!  You can see a bunch of parallels
between current LLMs in the way Trurl's machine works -- and in its failure modes.
Mollick decided to use it as a prompt ages ago, and in March 2024,
he managed to get Claude 3 to
almost
complete the task
.
The result wasn't a very good poem, but neither ChatGPT 4 nor the version of Gemini
at the time were close.  Here's Claude 3's attempt:
Stealthily snipping, shearing silky strands,
Severing soulmate's sacred, sworn soulbands.
Scoundrel's scandalous sins spurred sly scheme,
Spurring scorned sweetheart's spiteful supreme dream.
Shining locks sacrificed, stoically shorn,
Stalwart spirit stays strong, staunchly reborn.
You can see that it had two non-S words, "dream" and "reborn" .  But otherwise not
bad -- it makes sense, the rhymes work, and it ticks the emotional boxes.
Recent models have become very good; here's Claude Fable 5 from today:
Ah, Trurl's Electronic Bard's finest hour — the impossible commission from The Cyberiad! Here's my own attempt at the feat:
Soft she sang; strong Samson slumbered, serene;
Sly, she snipped seven shining strands, scarcely seen.
Soldiers stormed, seized, scorched Samson's sight;
Shackled, still, sightless — seething sacred spite.
Straining, steadfast, Samson seized stout stanchions, swaying slow —
Stones smashed; seductress, soldiers, Samson: slain. So sagas show.
Love in the lullaby, treachery in the shears, doom in the darkness, heroism at the pillars, and retribution in the rubble — with every single word dutifully saluting the letter S. The Electronic Bard would, I hope, give a grudging beep of approval.
Now, it recognised the source, so perhaps that helped -- but while I'm no
connoisseur of poetry, I actually think it's slightly better than Lem's
version (though as Lem wrote in Polish, that's the work of his translator --
and translating poetry is obviously a tough task).
And while both versions
are based on Samson, given that he was a biblical hero who lost his strength
after his hair was cut, he's a pretty obvious subject for a tragic poem about
a haircut, especially if every word has to start with the letter "S" -- so I don't
think that points to copying.
ChatGPT 5.6 Sol also does a great job:
Silken Samson sought sweetheart’s soft sanctuary;
Sweetheart, serpent-souled, summoned shears—sanguinary.
Silver strands slid; sacred strength sank, slain;
Silent sorrow sealed sweetheart’s scarlet stain.
Shorn, storm-bound, Samson shielded slaves, steadfast;
Stone sanctums shattered; smiling, Samson sank—surpassed.
Another Samson-based one; it doesn't say it recognises the source, but I imagine it did.
Now let's take a look at some samples from this tiny model we've been benchmarking
-- 35B parameters, 3B active, of which only 2B are doing the actual thinking (rather than
messing around with embeddings).  Here's the first one I got:
Sneering shears shred sacred share,
Silent steel sells silver soul;
Sister's snare spares son;
Sweet sign seals sole;
Still star saves sun;
Secret sign seals son.
I mean, it's not amazing, but it satisfies the S constraint.  Less impressed by
how well it handles the "cleverly rhymed" part, though -- as I said earlier, its
scheme is ABCBCC, which is odd rather than clever -- and it doesn't make an awful
amount of sense.
I noted down two more while I was playing with this:
Silent shears sever sweet silver strands;
She stands, sacrificing self; submission seals severing's demands.
Shear's snare strikes; swift sentence seals sorrowful sphere.
Shorn sovereign swears silence shields secret spear;
She saves sacred soul; stillness safeguards sterling store.
Spirit soars; sorrow's stroke stops, solace restores.
That one's a lot better, I think; there's a hint of a story, and at least it rhymes.
But note the "demands" and the "restores" at the ends of lines 2 and 6 -- the "S"
constraint has been broken.
The next:
Sister's scheme scalp shorn,
Silver shears slice soul sworn,
Sweetheart's steel skull sear,
Silent slitters shear.
Spirit spies sight,
Sorrow swallows slight.
Hmm.  A bit bleak.
Again, poetry isn't my thing.  But I think that Claude 3's offering from two years ago
is better than any of them -- apart from the fact that it couldn't keep the "S"
constraint.
Still, it's impressive to see how well such a tiny model -- again, 2B actual thinking
parameters per token -- can do on what is a pretty challenging task!
