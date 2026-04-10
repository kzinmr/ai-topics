---
title: "Simon Willison on pelican-riding-a-bicycle"
url: "https://substack.com/redirect/8b76ad88-36bc-404b-b585-a35c1d052daa?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-10T16:19:51.277492+00:00
source_date: 2026-04-11
tags: [newsletter, auto-ingested]
---

# Simon Willison on pelican-riding-a-bicycle

Source: https://substack.com/redirect/8b76ad88-36bc-404b-b585-a35c1d052daa?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Atom feed for pelican-riding-a-bicycle
Random
104 posts tagged “pelican-riding-a-bicycle”
2026
Meta
announced Muse Spark
today, their first model release since Llama 4
almost exactly a year ago
. It’s hosted, not open weights, and the API is currently “a private API preview to select users”, but you can try it out today on
meta.ai
(Facebook or Instagram login required).
[...
2,607 words
]
GLM-5.1: Towards Long-Horizon Tasks
.
    Chinese AI lab Z.ai's latest model is a giant 754B parameter 1.51TB (on
Hugging Face
) MIT-licensed monster - the same size as their previous GLM-5 release, and sharing the
same paper
.
It's available
via OpenRouter
so I asked it to draw me a pelican:
llm install llm-openrouter
llm -m openrouter/z-ai/glm-5.1 'Generate an SVG of a pelican on a bicycle'
And something new happened... unprompted, the model
decided to give me
an HTML page that included both the SVG and a separate set of CSS animations!
The SVG was excellent, and might be my new favorite from an open weights model:
But the animation
broke it
:
That's the pelican, floating up in the top left corner.
I usually don't do follow-up prompts for the pelican test, but in this case I made an exception:
llm -c 'the animation is a bit broken, the pelican ends up positioned off the screen at the top right'
GLM 5.1 replied:
The issue is that CSS
transform
animations on SVG elements override the SVG
transform
attribute used for positioning, causing the pelican to lose its placement and fly off to the top-right. The fix is to separate positioning (SVG attribute) from animation (inner group) and use
<animateTransform>
for SVG rotations since it handles coordinate systems correctly.
And spat out
fresh HTML
which fixed the problem!
I particularly like the animation of the beak, which is described in the SVG comments like so:
<!--
Pouch (lower beak) with wobble
-->
<
g
>
    <
path
d
=
"
M42,-58 Q43,-50 48,-42 Q55,-35 62,-38 Q70,-42 75,-60 L42,-58 Z
"
fill
=
"
url(#pouchGrad)
"
stroke
=
"
#b06008
"
stroke-width
=
"
1
"
opacity
=
"
0.9
"
/>
    <
path
d
=
"
M48,-50 Q55,-46 60,-52
"
fill
=
"
none
"
stroke
=
"
#c06a08
"
stroke-width
=
"
0.8
"
opacity
=
"
0.6
"
/>
    <
animateTransform
attributeName
=
"
transform
"
type
=
"
scale
"
values
=
"
1,1; 1.03,0.97; 1,1
"
dur
=
"
0.75s
"
repeatCount
=
"
indefinite
"
additive
=
"
sum
"
/>
</
g
>
Update
: On Bluesky
@charles.capps.me suggested
a "NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER" and...
The HTML+SVG comments on that one include
/* Earring sparkle */, <!-- Opossum fur gradient -->, <!-- Distant treeline silhouette - Virginia pines -->,  <!-- Front paw on handlebar -->
- here's
the transcript
and the
HTML result
.
#
7th April 2026
,
9:25 pm
/
css
,
svg
,
ai
,
generative-ai
,
llms
,
pelican-riding-a-bicycle
,
llm-release
,
ai-in-china
,
glm
Gemma 4: Byte for byte, the most capable open models
.
    Four new vision-capable Apache 2.0 licensed reasoning LLMs from Google DeepMind, sized at 2B, 4B, 31B, plus a 26B-A4B Mixture-of-Experts.
Google emphasize "unprecedented level of intelligence-per-parameter", providing yet more evidence that creating small useful models is one of the hottest areas of research right now.
They actually label the two smaller models as E2B and E4B for "Effective" parameter size. The system card explains:
The smaller models incorporate Per-Layer Embeddings (PLE) to maximize parameter efficiency in on-device deployments. Rather than adding more layers or parameters to the model, PLE gives each decoder layer its own small embedding for every token. These embedding tables are large but are only used for quick lookups, which is why the effective parameter count is much smaller than the total.
I don't entirely understand that, but apparently that's what the "E" in E2B means!
One particularly exciting feature of these models is that they are multi-modal beyond just images:
Vision and audio
: All models natively process video and images, supporting variable resolutions, and excelling at visual tasks like OCR and chart understanding. Additionally, the E2B and E4B models feature native audio input for speech recognition and understanding.
I've not figured out a way to run audio input locally - I don't think that feature is in LM Studio or Ollama yet.
I tried them out using the GGUFs for
LM Studio
. The 2B (4.41GB), 4B (6.33GB) and 26B-A4B (17.99GB) models all worked perfectly, but the 31B (19.89GB) model was broken and spat out
"---\n"
in a loop for every prompt I tried.
The succession of
pelican quality
from 2B to 4B to 26B-A4B is notable:
E2B:
E4B:
26B-A4B:
(This one actually had an SVG error - "error on line 18 at column 88: Attribute x1 redefined" - but after
fixing that
I got probably the best pelican I've seen yet from a model that runs on my laptop.)
Google are providing API access to the two larger Gemma models via their
AI Studio
. I added support to
llm-gemini
and then
ran a pelican
through the 31B model using that:
llm -m gemini/gemma-4-31b-it 'Generate an SVG of a pelican riding a bicycle'
Pretty good, though it is missing the front part of the bicycle frame:
#
2nd April 2026
,
6:28 pm
/
google
,
ai
,
generative-ai
,
local-llms
,
llms
,
llm
,
vision-llms
,
pelican-riding-a-bicycle
,
llm-reasoning
,
gemma
,
llm-release
,
lm-studio
OpenAI today:
Introducing GPT‑5.4 mini and nano
. These models join GPT-5.4 which was released
two weeks ago
.
[...
717 words
]
Introducing Mistral Small 4
.
    Big new release from Mistral today (despite the name) - a new Apache 2 licensed 119B parameter (Mixture-of-Experts, 6B active) model which they describe like this:
Mistral Small 4 is the first Mistral model to unify the capabilities of our flagship models, Magistral for reasoning, Pixtral for multimodal, and Devstral for agentic coding, into a single, versatile model.
It supports
reasoning_effort="none"
or
reasoning_effort="high"
, with the latter providing "equivalent verbosity to previous Magistral models".
The new model is
242GB on Hugging Face
.
I
tried it out
via the Mistral API using
llm-mistral
:
llm install llm-mistral
llm mistral refresh
llm -m mistral/mistral-small-2603 "Generate an SVG of a pelican riding a bicycle"
I couldn't find a way to set the reasoning effort in their
API documentation
, so hopefully that's a feature which will land soon.
Update 23rd March
: Here's new documentation for the
reasoning_effort parameter
.
Also from Mistral today and fitting their -stral naming convention is
Leanstral
, an open weight model that is specifically tuned to help output the
Lean 4
formally verifiable coding language. I haven't explored Lean at all so I have no way to credibly evaluate this, but it's interesting to see them target one specific language in this way.
#
16th March 2026
,
11:41 pm
/
ai
,
generative-ai
,
llms
,
llm
,
mistral
,
pelican-riding-a-bicycle
,
llm-reasoning
,
llm-release
Introducing GPT‑5.4
.
    Two new API models:
gpt-5.4
and
gpt-5.4-pro
, also available in ChatGPT and Codex CLI. August 31st 2025 knowledge cutoff, 1 million token context window. Priced
slightly higher
than the GPT-5.2 family with a bump in price for both models if you go above 272,000 tokens.
5.4 beats coding specialist GPT-5.3-Codex on all of the relevant benchmarks. I wonder if we'll get a 5.4 Codex or if that model line has now been merged into main?
Given Claude's recent focus on business applications it's interesting to see OpenAI highlight this in their announcement of GPT-5.4:
We put a particular focus on improving GPT‑5.4’s ability to create and edit spreadsheets, presentations, and documents. On an internal benchmark of spreadsheet modeling tasks that a junior investment banking analyst might do, GPT‑5.4 achieves a mean score of
87.3%
, compared to
68.4%
for GPT‑5.2.
Here's a pelican on a bicycle
drawn by GPT-5.4
:
And
here's one
by GPT-5.4 Pro, which took 4m45s and cost me
$1.55
:
#
5th March 2026
,
11:56 pm
/
ai
,
openai
,
generative-ai
,
llms
,
pelican-riding-a-bicycle
,
llm-release
Gemini 3.1 Flash-Lite
.
    Google's latest model is an update to their inexpensive Flash-Lite family. At $0.25/million tokens of input and $1.5/million output this is 1/8th the price of Gemini 3.1 Pro.
It supports four different thinking levels, so I had it output
four different pelicans
:
#
3rd March 2026
,
9:53 pm
/
google
,
ai
,
generative-ai
,
llms
,
llm
,
gemini
,
llm-pricing
,
pelican-riding-a-bicycle
,
llm-release
Gemini 3.1 Pro
.
    The first in the Gemini 3.1 series, priced the same as Gemini 3 Pro ($2/million input, $12/million output under 200,000 tokens, $4/$18 for 200,000 to 1,000,000). That's less than half the price of Claude Opus 4.6 with very similar benchmark scores to that model.
They boast about its improved SVG animation performance compared to Gemini 3 Pro in the announcement!
I tried "Generate an SVG of a pelican riding a bicycle"
in Google AI Studio
and it thought for 323.9 seconds (
thinking trace here
) before producing this one:
It's good to see the legs clearly depicted on both sides of the frame (should
satisfy Elon
), the fish in the basket is a nice touch and I appreciated this comment in
the SVG code
:
<!-- Black Flight Feathers on Wing Tip -->
<path d="M 420 175 C 440 182, 460 187, 470 190 C 450 210, 430 208, 410 198 Z" fill="#374151" />
I've
added
the two new model IDs
gemini-3.1-pro-preview
and
gemini-3.1-pro-preview-customtools
to my
llm-gemini plugin
for
LLM
. That "custom tools" one is
described here
- apparently it may provide better tool performance than the default model in some situations.
The model appears to be
incredibly
slow right now - it took 104s to respond to a simple "hi" and a few of my other tests met "Error: This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later." or "Error: Deadline expired before operation could complete" errors. I'm assuming that's just teething problems on launch day.
It sounds like last week's
Deep Think release
was our first exposure to the 3.1 family:
Last week, we released a major update to Gemini 3 Deep Think to solve modern challenges across science, research and engineering. Today, we’re releasing the upgraded core intelligence that makes those breakthroughs possible: Gemini 3.1 Pro.
Update
: In
What happens if AI labs train for pelicans riding bicycles?
last November I said:
If a model finally comes out that produces an excellent SVG of a pelican riding a bicycle you can bet I’m going to test it on all manner of creatures riding all sorts of transportation devices.
Google's Gemini Lead Jeff Dean
tweeted this video
featuring an animated pelican riding a bicycle, plus a frog on a penny-farthing and a giraffe driving a tiny car and an ostrich on roller skates and a turtle kickflipping a skateboard and a dachshund driving a stretch limousine.
I've been saying for a while that I wish AI labs would highlight things that their new models can do that their older models could not, so top marks to the Gemini team for this video.
Update 2
: I used
llm-gemini
to run my
more detailed Pelican prompt
, with
this result
:
From the SVG comments:
<!-- Pouch Gradient (Breeding Plumage: Red to Olive/Green) -->
...
<!-- Neck Gradient (Breeding Plumage: Chestnut Nape, White/Yellow Front) -->
#
19th February 2026
,
5:58 pm
/
google
,
svg
,
ai
,
generative-ai
,
llms
,
llm
,
gemini
,
pelican-riding-a-bicycle
,
llm-release
Introducing Claude Sonnet 4.6
(
via
)
    Sonnet 4.6 is out today, and Anthropic claim it offers similar performance to
November's Opus 4.5
while maintaining the Sonnet pricing of $3/million input and $15/million output tokens (the Opus models are $5/$25). Here's
the system card PDF
.
Sonnet 4.6 has a "reliable knowledge cutoff" of August 2025, compared to Opus 4.6's May 2025 and Haiku 4.5's February 2025. Both Opus and Sonnet default to 200,000 max input tokens but can stretch to 1 million in beta and at a higher cost.
I just released
llm-anthropic 0.24
with support for both Sonnet 4.6 and Opus 4.6. Claude Code
did most of the work
- the new models had a fiddly amount of extra details around adaptive thinking and no longer supporting prefixes, as described
in Anthropic's migration guide
.
Here's
what I got
from:
uvx --with llm-anthropic llm 'Generate an SVG of a pelican riding a bicycle' -m claude-sonnet-4.6
The SVG comments include:
<!-- Hat (fun accessory) -->
I tried a second time and also got a top hat. Sonnet 4.6 apparently loves top hats!
For comparison, here's the pelican Opus 4.5 drew me
in November
:
And here's Anthropic's current best pelican, drawn by Opus 4.6
on February 5th
:
Opus 4.6 produces the best pelican beak/pouch. I do think the top hat from Sonnet 4.6 is a nice touch though.
#
17th February 2026
,
11:58 pm
/
ai
,
generative-ai
,
llms
,
llm
,
anthropic
,
claude
,
llm-pricing
,
pelican-riding-a-bicycle
,
llm-release
,
claude-code
Qwen3.5: Towards Native Multimodal Agents
.
    Alibaba's Qwen just released the first two models in the Qwen 3.5 series - one open weights, one proprietary. Both are multi-modal for vision input.
The open weight one is a Mixture of Experts model called Qwen3.5-397B-A17B. Interesting to see Qwen call out serving efficiency as a benefit of that architecture:
Built on an innovative hybrid architecture that fuses linear attention (via Gated Delta Networks) with a sparse mixture-of-experts, the model attains remarkable inference efficiency: although it comprises 397 billion total parameters, just 17 billion are activated per forward pass, optimizing both speed and cost without sacrificing capability.
It's
807GB on Hugging Face
, and Unsloth have a
collection of smaller GGUFs
ranging in size from 94.2GB 1-bit to 462GB Q8_K_XL.
I got this
pelican
from the
OpenRouter hosted model
(
transcript
):
The proprietary hosted model is called Qwen3.5 Plus 2026-02-15, and is a little confusing. Qwen researcher
Junyang Lin  says
:
Qwen3-Plus is a hosted API version of 397B. As the model natively supports 256K tokens, Qwen3.5-Plus supports 1M token context length. Additionally it supports search and code interpreter, which you can use on Qwen Chat with Auto mode.
Here's
its pelican
, which is similar in quality to the open weights model:
#
17th February 2026
,
4:30 am
/
ai
,
generative-ai
,
llms
,
vision-llms
,
qwen
,
pelican-riding-a-bicycle
,
llm-release
,
openrouter
,
ai-in-china
Introducing GPT‑5.3‑Codex‑Spark
.
    OpenAI announced a partnership with Cerebras
on January 14th
. Four weeks later they're already launching the first integration, "an ultra-fast model for real-time coding in Codex".
Despite being named GPT-5.3-Codex-Spark it's not purely an accelerated alternative to GPT-5.3-Codex - the blog post calls it "a smaller version of GPT‑5.3-Codex" and clarifies that "at launch, Codex-Spark has a 128k context window and is text-only."
I had some preview access to this model and I can confirm that it's significantly faster than their other models.
Here's what that speed looks like running in Codex CLI:
That was the "Generate an SVG of a pelican riding a bicycle" prompt - here's the rendered result:
Compare that to the speed of regular GPT-5.3 Codex medium:
Significantly slower, but the pelican is a lot better:
What's interesting about this model isn't the quality though, it's the
speed
. When a model responds this fast you can stay in flow state and iterate with the model much more productively.
I showed a demo of Cerebras running Llama 3.1 70 B at 2,000 tokens/second against Val Town
back in October 2024
. OpenAI claim 1,000 tokens/second for their new model, and I expect it will prove to be a ferociously useful partner for hands-on iterative coding sessions.
It's not yet clear what the pricing will look like for this new model.
#
12th February 2026
,
9:16 pm
/
ai
,
openai
,
generative-ai
,
llms
,
cerebras
,
pelican-riding-a-bicycle
,
llm-release
,
codex-cli
,
llm-performance
Gemini 3 Deep Think
(
via
)
    New from Google. They say it's "built to push the frontier of intelligence and solve modern challenges across science, research, and engineering".
It drew me a
really good
SVG of a pelican riding a bicycle
! I think this is the best one I've seen so far - here's
my previous collection
.
(And since it's an FAQ, here's my answer to
What happens if AI labs train for pelicans riding bicycles?
)
Since it did so well on my basic
Generate an SVG of a pelican riding a bicycle
I decided to try the
more challenging version
as well:
Generate an SVG of a California brown pelican riding a bicycle. The bicycle must have spokes and a correctly shaped bicycle frame. The pelican must have its characteristic large pouch, and there should be a clear indication of feathers. The pelican must be clearly pedaling the bicycle. The image should show the full breeding plumage of the California brown pelican.
Here's
what I got
:
#
12th February 2026
,
6:12 pm
/
google
,
ai
,
generative-ai
,
llms
,
gemini
,
pelican-riding-a-bicycle
,
llm-reasoning
,
llm-release
GLM-5: From Vibe Coding to Agentic Engineering
(
via
)
    This is a
huge
new MIT-licensed model: 744B parameters and
1.51TB on Hugging Face
twice the size of
GLM-4.7
which was 368B and 717GB (4.5 and 4.6 were around that size too).
It's interesting to see Z.ai take a position on what we should call professional software engineers building with LLMs - I've seen
Agentic Engineering
show up in a few other places recently. most notable
from Andrej Karpathy
and
Addy Osmani
.
I ran my "Generate an SVG of a pelican riding a bicycle" prompt through GLM-5 via
OpenRouter
and got back
a very good pelican on a disappointing bicycle frame
:
#
11th February 2026
,
6:56 pm
/
definitions
,
ai
,
generative-ai
,
llms
,
ai-assisted-programming
,
pelican-riding-a-bicycle
,
llm-release
,
vibe-coding
,
openrouter
,
ai-in-china
,
glm
,
agentic-engineering
Two major new model releases today, within about 15 minutes of each other.
Anthropic
released Opus 4.6
. Here's
its pelican
:
OpenAI
release GPT-5.3-Codex
, albeit only via their Codex app, not yet in their API. Here's
its pelican
:
I've had a bit of preview access to both of these models and to be honest I'm finding it hard to find a good angle to write about them - they're both
really good
, but so were their predecessors Codex 5.2 and Opus 4.5. I've been having trouble finding tasks that those previous models couldn't handle but the new ones are able to ace.
The most convincing story about capabilities of the new model so far is Nicholas Carlini from Anthropic talking about Opus 4.6 and
Building a C compiler with a team of parallel Claudes
- Anthropic's version of Cursor's
FastRender project
.
#
5th February 2026
,
8:29 pm
/
llm-release
,
anthropic
,
generative-ai
,
openai
,
pelican-riding-a-bicycle
,
ai
,
llms
,
parallel-agents
,
c
,
nicholas-carlini
Kimi K2.5: Visual Agentic Intelligence
(
via
)
    Kimi K2 landed
in July
as a 1 trillion parameter open weight LLM. It was joined by Kimi K2 Thinking
in November
which added reasoning capabilities. Now they've made it multi-modal: the K2 models were text-only, but the new 2.5 can handle image inputs as well:
Kimi K2.5 builds on Kimi K2 with continued pretraining over approximately 15T mixed visual and text tokens. Built as a native multimodal model, K2.5 delivers state-of-the-art coding and vision capabilities and a self-directed agent swarm paradigm.
The "self-directed agent swarm paradigm" claim there means improved long-sequence tool calling and training on how to break down tasks for multiple agents to work on at once:
For complex tasks, Kimi K2.5 can self-direct an agent swarm with up to 100 sub-agents, executing parallel workflows across up to 1,500 tool calls. Compared with a single-agent setup, this reduces execution time by up to 4.5x. The agent swarm is automatically created and orchestrated by Kimi K2.5 without any predefined subagents or workflow.
I used the
OpenRouter Chat UI
to have it "Generate an SVG of a pelican riding a bicycle", and it did
quite well
:
As a more interesting test, I decided to exercise the claims around multi-agent planning with this prompt:
I want to build a Datasette plugin that offers a UI to upload files to an S3 bucket and stores information about them in a SQLite table. Break this down into ten tasks suitable for execution by parallel coding agents.
Here's
the full response
. It produced ten realistic tasks and reasoned through the dependencies between them. For comparison here's the same prompt
against Claude Opus 4.5
and
against GPT-5.2 Thinking
.
The
Hugging Face repository
is 595GB. The model uses Kimi's janky "modified MIT" license, which adds the following clause:
Our only modification part is that, if the Software (or any derivative works thereof) is used for any of your commercial products or services that have more than 100 million monthly active users, or more than 20 million US dollars (or equivalent in other currencies) in monthly revenue, you shall prominently display "Kimi K2.5" on the user interface of such product or service.
Given the model's size, I expect one way to run it locally would be with MLX and a pair of $10,000 512GB RAM M3 Ultra Mac Studios. That setup has
been demonstrated to work
with previous trillion parameter K2 models.
#
27th January 2026
,
3:07 pm
/
ai
,
llms
,
hugging-face
,
vision-llms
,
llm-tool-use
,
ai-agents
,
pelican-riding-a-bicycle
,
llm-release
,
ai-in-china
,
moonshot
,
parallel-agents
,
kimi
,
janky-licenses
2025
This is the third in my annual series reviewing everything that happened in the LLM space over the past 12 months. For previous years see
Stuff we figured out about AI in 2023
and
Things we learned about LLMs in 2024
.
[...
8,273 words
]
Introducing GPT-5.2-Codex
.
    The latest in OpenAI's
Codex family of models
(not the same thing as their Codex CLI or Codex Cloud coding agent tools).
GPT‑5.2-Codex is a version of
GPT‑5.2⁠
further optimized for agentic coding in Codex, including improvements on long-horizon work through context compaction, stronger performance on large code changes like refactors and migrations, improved performance in Windows environments, and significantly stronger cybersecurity capabilities.
As with some previous Codex models this one is available via their Codex coding agents now and will be coming to the API "in the coming weeks". Unlike previous models there's a new invite-only preview process for vetted cybersecurity professionals for "more permissive models".
I've been very impressed recently with GPT 5.2's ability to
tackle multi-hour agentic coding challenges
. 5.2 Codex scores 64% on the Terminal-Bench 2.0 benchmark that GPT-5.2 scored 62.2% on. I'm not sure how concrete that 1.8% improvement will be!
I didn't hack API access together this time (see
previous attempts
), instead opting to just ask Codex CLI to "Generate an SVG of a pelican riding a bicycle" while running the new model (effort medium).
Here's the transcript
in my new Codex CLI timeline viewer, and here's the pelican it drew:
#
19th December 2025
,
5:21 am
/
ai
,
openai
,
generative-ai
,
llms
,
pelican-riding-a-bicycle
,
llm-release
,
codex-cli
,
gpt-codex
It continues to be a busy December, if not quite as busy
as last year
. Today’s big news is
Gemini 3 Flash
, the latest in Google’s “Flash” line of faster and less expensive models.
[...
1,271 words
]
OpenAI reportedly
declared a “code red”
on the 1st of December in response to increasingly credible competition from the likes of Google’s Gemini 3. It’s less than two weeks later and they just
announced GPT-5.2
, calling it “the most capable model series yet for professional knowledge work”.
[...
964 words
]
Devstral 2
.
    Two new models from Mistral today: Devstral 2 and Devstral Small 2 - both focused on powering coding agents such as Mistral's newly released Mistral Vibe which
I wrote about earlier today
.
Devstral 2: SOTA open model for code agents with a fraction of the parameters of its competitors and achieving 72.2% on SWE-bench Verified.
Up to 7x more cost-efficient than Claude Sonnet at real-world tasks.
Devstral 2 is a 123B model released under a janky license - it's "modified MIT" where
the modification
is:
You are not authorized to exercise any rights under this license if the global consolidated monthly revenue of your company (or that of your employer) exceeds $20 million (or its equivalent in another currency) for the preceding month. This restriction in (b) applies to the Model and any derivatives, modifications, or combined works based on it, whether provided by Mistral AI or by a third party. [...]
Mistral Small 2 is under a proper Apache 2 license with no weird strings attached. It's a 24B model which is
51.6GB on Hugging Face
and should quantize to significantly less.
I tried out the larger model via
my llm-mistral plugin
like this:
llm install llm-mistral
llm mistral refresh
llm -m mistral/devstral-2512 "Generate an SVG of a pelican riding a bicycle"
For a ~120B model that one is pretty good!
Here's the same prompt with
-m mistral/labs-devstral-small-2512
for the API hosted version of Devstral Small 2:
Again, a decent result given the small parameter size. For comparison,
here's what I got
for the 24B Mistral Small 3.2 earlier this year.
#
9th December 2025
,
11:58 pm
/
ai
,
generative-ai
,
llms
,
llm
,
mistral
,
pelican-riding-a-bicycle
,
llm-release
,
janky-licenses
DeepSeek-V3.2
(
via
)
    Two new open weight (MIT licensed) models from DeepSeek today:
DeepSeek-V3.2
and
DeepSeek-V3.2-Speciale
, both 690GB, 685B parameters. Here's the
PDF tech report
.
DeepSeek-V3.2 is DeepSeek's new flagship model, now running on
chat.deepseek.com
.
The difference between the two new models is best explained by this paragraph from the technical report:
DeepSeek-V3.2 integrates reasoning, agent, and human alignment data distilled from specialists, undergoing thousands of steps of continued RL training to reach the final checkpoints. To investigate the potential of extended thinking, we also developed an experimental variant, DeepSeek-V3.2-Speciale. This model was trained exclusively on reasoning data with a reduced length penalty during RL. Additionally, we incorporated the dataset and reward method from DeepSeekMath-V2 (Shao et al., 2025) to enhance capabilities in mathematical proofs.
I covered
DeepSeek-Math-V2 last week
. Like that model, DeepSeek-V3.2-Speciale also scores gold on the 2025 International Mathematical Olympiad so beloved of model training teams!
I tried both models on "Generate an SVG of a pelican riding a bicycle" using the chat feature of [OpenRouter](https://openrouter.ai/). DeepSeek V3.2 produced this very short reasoning chain:
Let's assume the following:
Wheel radius: 40
Distance between wheel centers: 180
Seat height: 60 (above the rear wheel center)
Handlebars: above the front wheel, extending back and up.
We'll set the origin at the center of the rear wheel.
We'll create the SVG with a viewBox that fits the entire drawing.
Let's start by setting up the SVG.
Followed by this illustration:
Here's what I got from the Speciale model, which thought deeply about the geometry of bicycles and pelicans for
a very long time (at least 10 minutes)
before spitting out this result:
#
1st December 2025
,
11:56 pm
/
ai
,
generative-ai
,
llms
,
pelican-riding-a-bicycle
,
llm-reasoning
,
deepseek
,
llm-release
,
openrouter
,
ai-in-china
LLM SVG Generation Benchmark
(
via
)
    Here's a delightful project by Tom Gally, inspired by my
pelican SVG benchmark
. He
asked Claude
to help create more prompts of the form
Generate an SVG of [A] [doing] [B]
and then ran 30 creative prompts against 9 frontier models - prompts like "an octopus operating a pipe organ" or "a starfish driving a bulldozer".
Here are some for "butterfly inspecting a steam engine":
And for "sloth steering an excavator":
It's worth browsing the
whole collection
, which gives a really good overall indication of which models are the best at SVG art.
#
25th November 2025
,
4:02 am
/
benchmarks
,
svg
,
ai
,
generative-ai
,
llms
,
evals
,
pelican-riding-a-bicycle
,
tom-gally
Anthropic
released Claude Opus 4.5
this morning, which they call “best model in the world for coding, agents, and computer use”. This is their attempt to retake the crown for best coding model after significant challenges from OpenAI’s
GPT-5.1-Codex-Max
and Google’s
Gemini 3
, both released within the past week!
[...
1,120 words
]
Olmo is the LLM series from Ai2—the
Allen institute for AI
. Unlike most open weight models these are notable for including the full training data, training process and checkpoints along with those releases.
[...
1,834 words
]
Building more with GPT-5.1-Codex-Max
(
via
)
    Hot on the heels of yesterday's
Gemini 3 Pro release
comes a new model from OpenAI called GPT-5.1-Codex-Max.
(Remember when GPT-5 was meant to bring in a new era of less confusing model names? That didn't last!)
It's currently only available through their
Codex CLI coding agent
, where it's the new default model:
Starting today, GPT‑5.1-Codex-Max will replace GPT‑5.1-Codex as the default model in Codex surfaces. Unlike GPT‑5.1, which is a general-purpose model, we recommend using GPT‑5.1-Codex-Max and the Codex family of models only for agentic coding tasks in Codex or Codex-like environments.
It's not available via the API yet but should be shortly.
The timing of this release is interesting given that Gemini 3 Pro appears to have
aced almost all of the benchmarks
just yesterday. It's reminiscent of the period in 2024 when OpenAI consistently made big announcements that happened to coincide with Gemini releases.
OpenAI's self-reported
SWE-Bench Verified
score is particularly notable: 76.5% for thinking level "high" and 77.9% for the new "xhigh". That was the one benchmark where Gemini 3 Pro was out-performed by Claude Sonnet 4.5 - Gemini 3 Pro got 76.2% and Sonnet 4.5 got 77.2%. OpenAI now have the highest scoring model there by a full .7 of a percentage point!
They also report a score of 58.1% on
Terminal Bench 2.0
, beating Gemini 3 Pro's 54.2% (and Sonnet 4.5's 42.8%.)
The most intriguing part of this announcement concerns the model's approach to long context problems:
GPT‑5.1-Codex-Max is built for long-running, detailed work. It’s our first model natively trained to operate across multiple context windows through a process called
compaction
, coherently working over millions of tokens in a single task. [...]
Compaction enables GPT‑5.1-Codex-Max to complete tasks that would have previously failed due to context-window limits, such as complex refactors and long-running agent loops by pruning its history while preserving the most important context over long horizons. In Codex applications, GPT‑5.1-Codex-Max automatically compacts its session when it approaches its context window limit, giving it a fresh context window. It repeats this process until the task is completed.
There's a lot of confusion
on Hacker News
about what this actually means. Claude Code already does a version of compaction, automatically summarizing previous turns when the context runs out. Does this just mean that Codex-Max is better at that process?
I had it draw me a couple of pelicans by typing "Generate an SVG of a pelican riding a bicycle" directly into the Codex CLI tool. Here's thinking level medium:
And here's thinking level "xhigh":
I also tried xhigh on the my
longer pelican test prompt
, which came out like this:
Also today:
GPT-5.1 Pro is rolling out today to all Pro users
. According to the
ChatGPT release notes
:
GPT-5.1 Pro is rolling out today for all ChatGPT Pro users and is available in the model picker. GPT-5 Pro will remain available as a legacy model for 90 days before being retired.
That's a pretty fast deprecation cycle for the GPT-5 Pro model that was released just three months ago.
#
19th November 2025
,
11:15 pm
/
ai
,
openai
,
generative-ai
,
llms
,
evals
,
pelican-riding-a-bicycle
,
llm-release
,
gpt-5
,
codex-cli
,
gpt-codex
,
november-2025-inflection
Introducing GPT-5.1 for developers
.
    OpenAI announced GPT-5.1 yesterday, calling it
a smarter, more conversational ChatGPT
. Today they've added it to their API.
We actually got four new models today:
There are a lot of details to absorb here.
GPT-5.1 introduces a new reasoning effort called "none" (previous were minimal, low, medium, and high) - and none is the new default.
This makes the model behave like a non-reasoning model for latency-sensitive use cases, with the high intelligence of GPT‑5.1 and added bonus of performant tool-calling. Relative to GPT‑5 with 'minimal' reasoning, GPT‑5.1 with no reasoning is better at parallel tool calling (which itself increases end-to-end task completion speed), coding tasks, following instructions, and using search tools---and supports
web search⁠
in our API platform.
When you DO enable thinking you get to benefit from a new feature called "adaptive reasoning":
On straightforward tasks, GPT‑5.1 spends fewer tokens thinking, enabling snappier product experiences and lower token bills. On difficult tasks that require extra thinking, GPT‑5.1 remains persistent, exploring options and checking its work in order to maximize reliability.
Another notable new feature for 5.1 is
extended prompt cache retention
:
Extended prompt cache retention keeps cached prefixes active for longer, up to a maximum of 24 hours. Extended Prompt Caching works by offloading the key/value tensors to GPU-local storage when memory is full, significantly increasing the storage capacity available for caching.
To enable this set
"prompt_cache_retention": "24h"
in the API call. Weirdly there's no price increase involved with this at all. I
asked about that
and OpenAI's Steven Heidel
replied
:
with 24h prompt caching we move the caches from gpu memory to gpu-local storage. that storage is not free, but we made it free since it moves capacity from a limited resource (GPUs) to a more abundant resource (storage). then we can serve more traffic overall!
The most interesting documentation I've seen so far is in the new
5.1 cookbook
, which also includes details of the new
shell
and
apply_patch
built-in tools. The
apply_patch.py implementation
is worth a look, especially if you're interested in the advancing state-of-the-art of file editing tools for LLMs.
I'm still working on
integrating the new models into LLM
. The Codex models are Responses-API-only.
I got this pelican for GPT-5.1 default (no thinking):
And this one with reasoning effort set to high:
These actually feel like a
regression from GPT-5
to me. The bicycles have less spokes!
#
13th November 2025
,
11:59 pm
/
ai
,
openai
,
generative-ai
,
llms
,
llm
,
pelican-riding-a-bicycle
,
llm-reasoning
,
llm-release
,
gpt-5
,
gpt-codex
,
november-2025-inflection
Almost every time I share a new example of
an SVG of a pelican riding a bicycle
a variant of this question pops up: how do you know the labs aren’t training for your benchmark?
[...
325 words
]
Agentic Pelican on a Bicycle
(
via
)
    Robert Glaser took my
pelican riding a bicycle
benchmark and applied an agentic loop to it, seeing if vision models could draw a better pelican if they got the chance to render their SVG to an image and then try again until they were happy with the end result.
Here's what Claude Opus 4.1 got to after four iterations - I think the most interesting result of the models Robert tried:
I tried a similar experiment to this a few months ago in preparation for the GPT-5 launch and was surprised at how little improvement it produced.
Robert's "skeptical take" conclusion is similar to my own:
Most models didn’t fundamentally change their approach. They tweaked. They adjusted. They added details. But the basic composition—pelican shape, bicycle shape, spatial relationship—was determined in iteration one and largely frozen thereafter.
#
11th November 2025
,
11:23 pm
/
svg
,
ai
,
generative-ai
,
llms
,
ai-agents
,
pelican-riding-a-bicycle
Pelican on a Bike—Raytracer Edition
(
via
)
    beetle_b ran this prompt against a bunch of recent LLMs:
Write a POV-Ray file that shows a pelican riding on a bicycle.
This turns out to be a harder challenge than SVG, presumably because there are less examples of POV-Ray in the training data:
Most produced a script that failed to parse. I would paste the error back into the chat and let it attempt a fix.
The results are really fun though! A lot of them end up accompanied by a weird floating egg for some reason -
here's Claude Opus 4
:
I think the best result came
from GPT-5
- again with the floating egg though!
I decided to try this on the new
gpt-5-codex-mini
, using the
trick I described yesterday
. Here's
the code it wrote
.
./target/debug/codex prompt -m gpt-5-codex-mini \
  "Write a POV-Ray file that shows a pelican riding on a bicycle."
It turns out you can render POV files on macOS like this:
brew install povray
povray demo.pov # produces demo.png
The code GPT-5 Codex Mini created didn't quite work, so I round-tripped it through Sonnet 4.5 via Claude Code a couple of times -
transcript here
. Once it had fixed the errors I got this:
That's significantly worse than the one beetle_b got
from GPT-5 Mini
!
#
9th November 2025
,
4:51 pm
/
3d
,
ray-tracing
,
ai
,
generative-ai
,
llms
,
pelican-riding-a-bicycle
,
gpt-5
