---
title: "Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code"
url: "https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything"
fetched_at: 2026-06-23T07:00:55.231702+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code

Source: https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything

Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code
22nd June 2026
This morning
on Hacker News
I saw
Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance
, describing a small but effective inpainting model—a model where you can mark regions of an image to remove and the model imagines what should fill the space. The released model
required PyTorch and NVIDIA CUDA
, but since it described itself as 0.2B I decided to try and get it running using WebGPU in a browser. TL;DR: I got it working, and you can try the demo at
simonw.github.io/moebius-web/
. Read on for the details.
Here’s a video demo of the finished tool:
You can open any image in it (non-square images get letterboxed), highlight areas to remove, click the “Run inpaint” button and wait for the model to do its magic.
A parallel agent side-project
My main project for today was landing a major feature in Datasette: a UI for creating and altering tables, as a follow-up to the
insert and edit rows feature
I released last week.
I was working on that in Codex Desktop (here’s
the PR
) and often found myself spending 5-10 minutes spinning my fingers waiting for it to complete a mid-sized refactor or add the finishing touches to a change to the UI.
(An amusing thing about coding agents is that the harder a problem is the
more
time you have to get distracted while you wait for them to finish crunching!)
So I decided to spin up Claude Code in a terminal window and see how far I could get at porting Moebius to the web.
Some agentic research to kick off the project
My first step was to ask regular Claude about the feasibility of this project. In
Claude.ai
, which has the ability to clone repos from GitHub:
Clone https://github.com/hustvl/Moebius/ and tell me if they published the code and weights to run this model anywhere
(I hadn’t spotted the link to the weights yet, that’s tucked away in the “News” section.)
Then:
For Moebius what are the options for running it right now - Python and NVIDIA CUDA only or other options too?
And:
Muse on the feasibility of porting it to Transformers.js or similar and running it in a browser
I like telling models to “muse on X”, it’s the shortest way I’ve found of expressing that I want them to contemplate a problem for me without providing them with a concrete goal.
Here’s
that chat transcript
. I copied out the last answer and saved it as
research.md
for Claude Code to read later.
Claude suggested using
ONNX Runtime Web on the WebGPU backend
—the layer
below
the
Transformers.js
library I had suggested.
That was enough to convince me it was worth setting Claude Code loose and seeing how far it could get.
I usually start projects like this by gathering as much information as the coding agent might need as possible. Since I didn’t expect this project to actually work I did everything in my
/tmp
folder:
cd
/tmp
mkdir Moebius
cd
Moebius
#
Grab the Moebius python code
git clone https://github.com/hustvl/Moebius
#
And the model weights (Claude figured this out):
GIT_LFS_SKIP_SMUDGE=0 git clone \
  https://huggingface.co/hustvl/Moebius Moebius-weights
#
Finally a couple of libraries we might use:
git clone https://github.com/huggingface/transformers.js
git clone https://github.com/microsoft/onnxruntime
Setting off Claude Code
I created a directory for the rest of the project and ran
git init
in that so Claude could start committing code notes:
mkdir /tmp/Moebius/moebius-web
cd
/tmp/Moebius/moebius-web
git init
#
Copy in that research.md from earlier
git add research.md
git commit -m
"
Initial research by Claude Opus 4.8
"
I fired up a
claude
instance in the
/tmp/Moebius
folder, the level above all of the research materials I had prepared for it. I prompted:
Read ./moebius-web/research.md - your goal is to port this model to ONNX and WebGPU so we can run it directly in a browser, with a simple UI
As it started to work I dropped in this follow-up (typos included):
Bulid this in /tmp/Moebius/moebius-web and commit early and often, also maintain a notes.md file in there with notes about what you figure out along the way - also start by writing out a plan.md in there and update that plan as oy work too
I often ask agents to keep notes like this—the end result is often interesting, both for myself and for the next agent session that touches the same project. Here’s what that
notes.md file
looked like at the end of the project.
I kicked it off and went back to my main project, checking in occasionally to see how Claude was doing. When it looked like it might have something that worked I prompted:
Tell me what URL I can visit in my own browser to try this
Then I tried it out in Chrome and pasted some errors (and screenshots of errors) back into Claude Code.
After a few rounds of this we had something that appeared to work! Time to put it on the internet so other people could use it.
How would we publish this to Hugging Face such that the model weights were on there and the HTML demo would show up in Hugging Face spaces?
Claude Code knows how to use the
hf
CLI tool, so I created a model repo on
Hugging Face
, then
created a token
that could write to that repo and dropped it into a
/tmp/Moebius/token.txt
file so Claude could use it.
It published the 1.24GB of converted ONNX weights to
huggingface.co/simonw/Moebius-ONNX
for me.
I’d seen other demos load weights into the browser from Hugging Face before, so I knew it was possible. I decided to host my own frontend code on GitHub Pages, so I said:
I want to publish the moebius-web folder to GitHub, minus the large files (so maybe minus the models/ folder), such that when I turn on GitHub Pages for that repo navigating to https://simonw.github.io/moebius-web/ serves the UI
Telling it the final URL was important in case it needed to fix the URLs in the demos that it was building so they would work when deployed to production.
After a few more rounds of iteration, in between working on my main project, we got to a working, deployed version!
Except... each time I reloaded the page it seemed to download ~1.3GB of model weights. Browser caching seemed pretty important for this!
anything clever we can do with serviceworkers or similar to help cache this stuff? It seems to reload every time, I am concerned that there might be something weird about the way HF redirects work that mean we don't benefit from browser caching
I knew that Transformers.js projects could handle this properly, so I grabbed a copy of the
Whisper Web
demo, dropped it into
/tmp/Moebius/whisper-web
and said:
look in /tmp/Moebius/whisper-web (with a subagent) and see how they do this
That project was entirely obfuscated, built JavaScript files so I figured using a subagent would avoid spending the rest of my top-level token context deciphering those files.
Claude figured out that it was using
caches.open("transformers-cache")
—the
CacheStorage API
—and
added that to our project
.
I’ve shared the
full Claude Code transcript
for this project (published using my
claude-code-transcripts
tool).
What did I learn from all of this?
This definitely counts as vibe coding: I didn’t look at a single line of code from the project, restricting my input to testing, suggesting small feature improvements (like a progress bar for the large file downloads) and pointing the model in the direction of examples of how I wanted things to work.
Since I didn’t write any code the amount I learned about the underlying technologies—WebGPU, ONNX, and the Moebius model itself—was very limited.
As is usually the case with this kind of project the most important things I learned concerned what was
possible
:
Claude Opus 4.8 is capable of converting a PyTorch model to ONNX, publishing the result to Hugging Face and then building out a web application and interface that can load and execute that model.
Chrome, Firefox and Safari are all now capable of running this kind of model—I tried it in all three.
The CacheStorage API works with ~1.3GB model files.
... which means we can have inpainting as a feature of a client-only web application! (If our users can tolerate the 1.3GB download.)
I felt like I should probably try and learn a little more about my project. I fired up
Claude.ai
and prompted:
Clone https://github.com/simonw/moebius-web/ and use it to teach me all about the model and ONNX and the process of converting a model to ONNX and WebGPU and basically everything I'd need to know in order to fully understand this repo
Here’s
the transcript
and the
understanding.md
Markdown file it created, which I’ve now added to the GitHub repo. I found the explanation of ONNX particularly enlightening:
ONNX
(Open Neural Network Exchange) is a portable, framework-neutral file format for neural networks. An
.onnx
file is essentially two things bundled together:
A computation graph
— a directed graph of
nodes
, where each node is an
operator
(
Conv
,
MatMul
,
Add
,
Einsum
,
Softmax
,
Gather
,
Resize
, …) wired together by named tensors flowing between them. This is the “recipe” for the forward pass.
The weights
— the learned parameter tensors (the convolution kernels, the embedding table, etc.), stored as initializers in that same graph.
Crucially, ONNX describes
what to compute
, abstractly, without saying
how
or
on what hardware
. The operator set is versioned by an
opset
number (this repo uses
opset 18
), which pins down exactly which operators exist and what their semantics are.
It turns out PyTorch has built in mechanisms for exporting to ONNX, as seen
here in export_onnx.py
:
torch
.
onnx
.
export
(
dec
, (
lat
,),
dec_path
,
opset_version
=
args
.
opset
,
input_names
=
[
"latent"
],
output_names
=
[
"image"
],
dynamic_axes
=
{
"latent"
: {
0
:
"B"
},
"image"
: {
0
:
"B"
}},
)
Claude also included a
handy glossary
and an only-slightly-broken
ASCII-art diagram
showing how the model pipeline fits together.
