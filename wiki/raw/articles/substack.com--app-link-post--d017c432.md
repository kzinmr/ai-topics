---
title: "Meta’s new model is Muse Spark, and meta.ai chat has interesting new tools"
url: "https://substack.com/app-link/post?publication_id=1173386&post_id=193797318&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM3OTczMTgsImlhdCI6MTc3NTgzMDI2MCwiZXhwIjoxNzc4NDIyMjYwLCJpc3MiOiJwdWItMTE3MzM4NiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.HxO2aIQs7OkFcwiRAf3ogAJSXizOsdHH-n4xKibQRQc"
fetched_at: 2026-04-10T16:19:47.003277+00:00
source_date: 2026-04-11
tags: [newsletter, auto-ingested]
---

# Meta’s new model is Muse Spark, and meta.ai chat has interesting new tools

Source: https://substack.com/app-link/post?publication_id=1173386&post_id=193797318&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTM3OTczMTgsImlhdCI6MTc3NTgzMDI2MCwiZXhwIjoxNzc4NDIyMjYwLCJpc3MiOiJwdWItMTE3MzM4NiIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.HxO2aIQs7OkFcwiRAf3ogAJSXizOsdHH-n4xKibQRQc

In this newsletter:
Meta’s new model is Muse Spark, and meta.ai chat has some interesting tools
Anthropic’s Project Glasswing - restricting Claude Mythos to security researchers - sounds necessary to me
The Axios supply chain attack used individually targeted social engineering
Plus 3 links and 6 quotations and 1 note
Sponsor message
: Security and IAM are the biggest blockers to running agents in production.
Teleport Beams
runs each agent in an isolated Firecracker VM with built-in identity — connected to your infrastructure and inference services. No secrets, no IAM wrestling.
Get early access.
Meta
announced Muse Spark
, their first model release since Llama 4
almost exactly a year ago
. It’s hosted, not open weights, and the API is currently “a private API preview to select users”, but you can try it out today on
meta.ai
(Facebook or Instagram login required).
Meta’s self-reported benchmarks show it competitive with Opus 4.6, Gemini 3.1 Pro, and GPT 5.4 on selected benchmarks, though notably behind on Terminal-Bench 2.0. Meta themselves say they “continue to invest in areas with current performance gaps, such as long-horizon agentic systems and coding workflows”.
The model is exposed as two different modes on
meta.ai
- “Instant” and “Thinking”. Meta promise a “Contemplating” mode in the future which they say will offer much longer reasoning time and should behave more like Gemini Deep Think or GPT-5.4 Pro.
A couple of pelicans
I prefer to run
my pelican test
via API to avoid being influenced by any invisible system prompts, but since that’s not an option I ran it against the chat UI directly.
Here’s the pelican I got for “Instant”:
And this one for “Thinking”:
Both SVGs were rendered inline by the Meta AI interface. Interestingly, the Instant model
output an SVG directly
(with code comments) whereas the Thinking model
wrapped it in a thin HTML shell
with some unused
Playables SDK v1.0.0
JavaScript libraries.
Which got me curious...
Poking around with tools
Clearly Meta’s chat harness has some tools wired up to it - at the very least it can render SVG and HTML as embedded frames, Claude Artifacts style.
But what else can it do?
I asked it:
what tools do you have access to?
And then:
I want the exact tool names, parameter names and tool descriptions, in the original format
It spat out detailed descriptions of 16 different tools. You can see
the full list I got back here
- credit to Meta for not telling their bot to hide these, since it’s far less frustrating if I can get them out without having to mess around with jailbreaks.
Here are highlights derived from that response:
Browse and search
.
browser.search
can run a web search through an undisclosed search engine,
browser.open
can load the full page from one of those search results and
browser.find
can run pattern matches against the returned page content.
Meta content search
.
meta_1p.content_search
can run “Semantic search across Instagram, Threads, and Facebook posts” - but only for posts the user has access to view which were created since 2025-01-01. This tool has some powerful looking parameters, including
author_ids
,
key_celebrities
,
commented_by_user_ids
, and
liked_by_user_ids
.
“Catalog search”
-
meta_1p.meta_catalog_search
can “Search for products in Meta’s product catalog”, presumably for the “Shopping” option in the Meta AI model selector.
Image generation
.
media.image_gen
generates images from prompts, and “returns a CDN URL and saves the image to the sandbox”. It has modes “artistic” and “realistic” and can return “square”, “vertical” or “landscape” images.
container.python_execution
- yes! It’s
Code Interpreter
, my favourite feature of both ChatGPT and Claude.
Execute Python code in a remote sandbox environment. Python 3.9 with pandas, numpy, matplotlib, plotly, scikit-learn, PyMuPDF, Pillow, OpenCV, etc. Files persist at
/mnt/data/
.
Python 3.9
is EOL
these days but the library collection looks useful.
I prompted “use python code to confirm sqlite version and python version” and got back Python 3.9.25 and SQLite 3.34.1 (from
January 2021
).
container.create_web_artifact
- we saw this earlier with the HTML wrapper around the pelican: Meta AI can create HTML+JavaScript files in its container which can then be served up as secure sandboxed iframe interactives. “Set kind to
html
for websites/apps or
svg
for vector graphics.”
container.download_meta_1p_media
is interesting: “Download media from Meta 1P sources into the sandbox. Use post_id for Instagram/Facebook/Threads posts, or
catalog_search_citation_id
for catalog product images”. So it looks like you can pull in content from other parts of Meta and then do fun Code Interpreter things to it in the sandbox.
container.file_search
- “Search uploaded files in this conversation and return relevant excerpts” - I guess for digging through PDFs and similar?
Tools for editing files in the container
-
container.view
,
container.insert
(with
new_str
and
insert_line
),
container.str_replace
. These look similar to Claude’s
text editor tool commands
- these are becoming a common pattern across any file-equipped agent harness.
container.visual_grounding
- see below, this one is
fun
.
subagents.spawn_agent
- the
sub-agent as a tool
pattern. “Spawn an independent sub-agent for research, analysis, or delegation. It returns its final text response.”
third_party.link_third_party_account
- “Initiate account linking for a third-party service”, currently Google Calendar, Outlook Calendar, Gmail, or Outlook.
Let’s talk about that
container.visual_grounding
one. Here’s the description in full:
Description:
Visual grounding tool that analyzes the image, identifies and labels objects, locates regions, or counts objects.
Parameters:
object_names
(array, required)
image_path
(string, default “”)
format_type
(”bbox”|”point”|”count”|null, default “bbox”)
title
(string|null)[string]
So it can take an image path, optional object names and return things in format
bbox
,
point
or
count
.
This sounded to me like Meta’s
Segment Anything
, (
I later heard that it’s not, this is a native feature of the model itself via a tool call with a custom system prompt
). I decided to take it for a spin.
Prompt
:
generate a photo of a raccoon sitting on a trash can wearing trash as a hat
Response
:
Here you go — king of the alley, in full regalia:
Coffee cup crown, banana peel brim, newspaper feather. Peak raccoon fashion. Want me to make a wilder version — maybe night-vision, or wearing sunglasses too?
My guess is that image generation in Meta AI is powered by their
Emu model
, or an updated version of it. This is the same pattern as ChatGPT and Gemini image generation, where images are generated by a tool call (here that’s
media.image_gen
).
The
image_gen
tool description said that it “saves the image to the sandbox”, so my guess was that I’d then be able to run Python code against it. I tried:
use python OpenCV to analyze that image and find out neat things about it
Annoyingly it did
not
show me the code it ran, but it did create this image:
Pretty neat! We can both generate images and then use them with Python tools.
Next, the
visual_grounding
tool. Knowing the names of the tools makes it easy to refer to them in prompts:
Now try the container.visual_grounding tool
The response (
full response here
):
Done — visual_grounding pinpointed every piece of the outfit with pixel-level precision:
[...]
Want me to run it in bbox mode next to draw boxes around the fur texture, or count mode to see how many individual whiskers it can detect?
Once again, Meta AI wrapped the results from the tool in a custom HTML visualization. That’s clearly
point
mode, but how about the others?
I prompted:
yes draw bounding boxes, can it do masks too?
Response:
Yes — bounding boxes work great. Masks? Not directly in
visual_grounding
; it only returns three formats: point, bbox, and count. No pixel-level segmentation masks.
Here’s the bbox output:
What you’re seeing:
raccoon
: big box from (270,240) to (892,845) — covers 62% of the width, basically the whole animal
coffee cup
: (424,115)-(610,273) — sits highest, 158px tall in the 0-1000 space
banana peel
: (472,215)-(667,291) — overlaps the cup’s base, confirming it’s draped over the side
newspaper
: (305,223)-(548,315) — left ear coverage
trash can lid
: (107,800)-(1000,998) — spans almost the full image width at the bottom
face
: (305,283)-(750,537) — tight crop around the mask
eyes
: both ~40×37 pixel boxes, perfectly level at y=379
Notice how the boxes nest: face is inside raccoon, eyes inside face, hat pieces overlap each other but stay above the face box. The tool is doing real object localization, not just guessing centers.
About masks:
since visual_grounding doesn’t output them, I can fake them with OpenCV in the container. Two quick options:
GrabCut
— I give it the raccoon bbox, it iteratively segments fur from background and returns a binary mask
SAM-style color threshold
— use the bbox plus k-means to isolate the coffee cup or banana peel
Want me to generate an actual alpha mask for the raccoon (cut it out from the alley), or for the trash hat pieces separately? Takes about 10 seconds and I can give you a transparent PNG.
Here’s
the HTML for that bbox visualization
.
Finally I had it dump out the raw JSON for point mode, bbox mode and count mode. You can
see that all here
. The count mode is particularly interesting - here’s that in full:
[
  {
    “object_name”: “raccoon whisker”,
    “points”: [
      {”x”: 403, “y”: 445},
      {”x”: 397, “y”: 458},
      {”x”: 392, “y”: 472},
      {”x”: 391, “y”: 485},
      {”x”: 398, “y”: 497},
      {”x”: 415, “y”: 512},
      {”x”: 618, “y”: 446},
      {”x”: 622, “y”: 461},
      {”x”: 625, “y”: 475},
      {”x”: 628, “y”: 488},
      {”x”: 635, “y”: 501},
      {”x”: 651, “y”: 518}
    ],
    “count”: 12
  },
  {
    “object_name”: “raccoon paw claw”,
    “points”: [
      {”x”: 406, “y”: 845},
      {”x”: 424, “y”: 847},
      {”x”: 441, “y”: 842},
      {”x”: 473, “y”: 833},
      {”x”: 596, “y”: 830},
      {”x”: 635, “y”: 844},
      {”x”: 660, “y”: 843},
      {”x”: 679, “y”: 838}
    ],
    “count”: 8
  },
  {
    “object_name”: “trash item on head”,
    “points”: [
      {”x”: 514, “y”: 191},
      {”x”: 568, “y”: 263},
      {”x”: 392, “y”: 274}
    ],
    “count”: 3
  },
  {
    “object_name”: “eye”,
    “points”: [
      {”x”: 462, “y”: 395},
      {”x”: 582, “y”: 398}
    ],
    “count”: 2
  },
  {
    “object_name”: “ear”,
    “points”: [
      {”x”: 359, “y”: 313},
      {”x”: 680, “y”: 294}
    ],
    “count”: 2
  }
]
So Meta AI has the ability to count a raccoon’s whiskers baked into the default set of tools.
Which means... it can count pelicans too!
Here’s that overlay
exported as HTML
.
Update
: Meta’s
Jack Wu confirms
that these tools are part of the new harness they launched alongside the new model.
On Twitter
Alexandr Wang said
:
this is step one. bigger models are already in development with infrastructure scaling to match. private api preview open to select partners today, with plans to open-source future versions.
I really hope they do go back to open-sourcing their models. Llama 3.1/3.2/3.3 were excellent laptop-scale model families, and the introductory blog post for Muse Spark had this to say about efficiency:
[...] we can reach the same capabilities with over an order of magnitude less compute than our previous model, Llama 4 Maverick. This improvement also makes Muse Spark significantly more efficient than the leading base models available for comparison.
So are Meta back in the frontier model game?
Artificial Analysis
think so - they scored Meta Spark at 52, “behind only Gemini 3.1 Pro, GPT-5.4, and Claude Opus 4.6”. Last year’s Llama 4 Maverick and Scout scored 18 and 13 respectively.
I’m waiting for API access - while the tool collection on
meta.ai
is quite strong the real test of a model like this is still what we can build on top of it.
Anthropic
didn’t
release their latest model, Claude Mythos (
system card PDF
). They have instead made it available to a very restricted set of preview partners under their newly announced
Project Glasswing
.
The model is a general purpose model, similar to Claude Opus 4.6, but Anthropic claim that its cyber-security research abilities are strong enough that they need to give the software industry as a whole time to prepare.
Mythos Preview has already found thousands of high-severity vulnerabilities, including some in
every major operating system and web browser
. Given the rate of AI progress, it will not be long before such capabilities proliferate, potentially beyond actors who are committed to deploying them safely.
[...]
Project Glasswing partners will receive access to Claude Mythos Preview to find and fix vulnerabilities or weaknesses in their foundational systems—systems that represent a very large portion of the world’s shared cyberattack surface. We anticipate this work will focus on tasks like local vulnerability detection, black box testing of binaries, securing endpoints, and penetration testing of systems.
There’s a great deal more technical detail in
Assessing Claude Mythos Preview’s cybersecurity capabilities
on the Anthropic Red Team blog:
In one case, Mythos Preview wrote a web browser exploit that chained together four vulnerabilities, writing a complex
JIT heap spray
that escaped both renderer and OS sandboxes. It autonomously obtained local privilege escalation exploits on Linux and other operating systems by exploiting subtle race conditions and KASLR-bypasses. And it autonomously wrote a remote code execution exploit on FreeBSD’s NFS server that granted full root access to unauthenticated users by splitting a 20-gadget ROP chain over multiple packets.
Plus this comparison with Claude 4.6 Opus:
Our internal evaluations showed that Opus 4.6 generally had a near-0% success rate at autonomous exploit development. But Mythos Preview is in a different league. For example, Opus 4.6 turned the vulnerabilities it had found in Mozilla’s Firefox 147 JavaScript engine—all patched in Firefox 148—into JavaScript shell exploits only two times out of several hundred attempts. We re-ran this experiment as a benchmark for Mythos Preview, which developed working exploits 181 times, and achieved register control on 29 more.
Saying “our model is too dangerous to release” is a great way to build buzz around a new model, but in this case I expect their caution is warranted.
Just a few days (
last Friday
) ago I started a new
ai-security-research
tag on this blog to acknowledge an uptick in credible security professionals pulling the alarm on how good modern LLMs have got at vulnerability research.
Greg Kroah-Hartman
of the Linux kernel:
Months ago, we were getting what we called ‘AI slop,’ AI-generated security reports that were obviously wrong or low quality. It was kind of funny. It didn’t really worry us.
Something happened a month ago, and the world switched. Now we have real reports. All open source projects have real reports that are made with AI, but they’re good, and they’re real.
Daniel Stenberg
of
curl
:
The challenge with AI in open source security has transitioned from an AI slop tsunami into more of a ... plain security report tsunami. Less slop but lots of reports. Many of them really good.
I’m spending hours per day on this now. It’s intense.
And Thomas Ptacek published
Vulnerability Research Is Cooked
, a post inspired by his
podcast conversation
with Anthropic’s Nicholas Carlini.
Anthropic have a 5 minute
talking heads video
describing the Glasswing project. Nicholas Carlini appears as one of those talking heads, where he said (highlights mine):
It has the ability to chain together vulnerabilities. So what this means is you find two vulnerabilities, either of which doesn’t really get you very much independently. But this model is able to create exploits out of three, four, or sometimes five vulnerabilities that in sequence give you some kind of very sophisticated end outcome. [...]
I’ve found more bugs in the last couple of weeks than I found in the rest of my life combined
. We’ve used the model to scan a bunch of open source code, and the thing that we went for first was operating systems, because this is the code that underlies the entire internet infrastructure.
For OpenBSD, we found a bug that’s been present for 27 years, where I can send a couple of pieces of data to any OpenBSD server and crash it
. On Linux, we found a number of vulnerabilities where as a user with no permissions, I can elevate myself to the administrator by just running some binary on my machine. For each of these bugs, we told the maintainers who actually run the software about them, and they went and fixed them and have deployed the patches patches so that anyone who runs the software is no longer vulnerable to these attacks.
I found this on the
OpenBSD 7.8 errata page
:
025: RELIABILITY FIX: March 25, 2026
All architectures
TCP packets with invalid SACK options could crash the kernel.
A source code patch exists which remedies this problem.
I tracked that change down in the
GitHub mirror
of the OpenBSD CVS repo (apparently they still use CVS!) and found it
using git blame
:
Sure enough, the surrounding code is from 27 years ago.
I’m not sure which Linux vulnerability Nicholas was describing, but it may have been
this NFS one
recently covered
by Michael Lynch
.
There’s enough smoke here that I believe there’s a fire. It’s not surprising to find vulnerabilities in decades-old software, especially given that they’re mostly written in C, but what’s new is that coding agents run by the latest frontier LLMs are proving tirelessly capable at digging up these issues.
I actually thought to myself on Friday that this sounded like an industry-wide reckoning in the making, and that it might warrant a huge investment of time and money to get ahead of the inevitable barrage of vulnerabilities. Project Glasswing incorporates “$100M in usage credits ... as well as $4M in direct donations to open-source security organizations”. Partners include AWS, Apple, Microsoft, Google, and the Linux Foundation. It would be great to see OpenAI involved as well - GPT-5.4 already has a strong reputation for finding security vulnerabilities and they have stronger models on the near horizon.
The bad news for those of us who are
not
trusted partners is this:
We do not plan to make Claude Mythos Preview generally available, but our eventual goal is to enable our users to safely deploy Mythos-class models at scale—for cybersecurity purposes, but also for the myriad other benefits that such highly capable models will bring. To do so, we need to make progress in developing cybersecurity (and other) safeguards that detect and block the model’s most dangerous outputs. We plan to launch new safeguards with an upcoming Claude Opus model, allowing us to improve and refine them with a model that does not pose the same level of risk as Mythos Preview.
I can live with that. I think the security risks really are credible here, and having extra time for trusted teams to get ahead of them is a reasonable trade-off.
The Axios team have published a
full postmortem
on the supply chain attack which resulted in a malware dependency going out
in a release the other day
, and it involved a sophisticated social engineering campaign targeting one of their maintainers directly. Here’s Jason Saayman’a description of
how that worked
:
so the attack vector mimics what google has documented here:
https://cloud.google.com/blog/topics/threat-intelligence/unc1069-targets-cryptocurrency-ai-social-engineering
they tailored this process specifically to me by doing the following:
they reached out masquerading as the founder of a company they had cloned the companys founders likeness as well as the company itself.
they then invited me to a real slack workspace. this workspace was branded to the companies ci and named in a plausible manner. the slack was thought out very well, they had channels where they were sharing linked-in posts, the linked in posts i presume just went to the real companys account but it was super convincing etc. they even had what i presume were fake profiles of the team of the company but also number of other oss maintainers.
they scheduled a meeting with me to connect. the meeting was on ms teams. the meeting had what seemed to be a group of people that were involved.
the meeting said something on my system was out of date. i installed the missing item as i presumed it was something to do with teams, and this was the RAT.
everything was extremely well co-ordinated looked legit and was done in a professional manner.
A RAT is a Remote Access Trojan - this was the software which stole the developer’s credentials which could then be used to publish the malicious package.
That’s a
very effective
scam. I join a lot of meetings where I find myself needing to install Webex or Microsoft Teams or similar at the last moment and the time constraint means I always click “yes” to things as quickly as possible to make sure I don’t join late.
Every maintainer of open source software used by enough people to be worth taking in this way needs to be familiar with this attack strategy.
Quote
2026-04-03
Months ago, we were getting what we called ‘AI slop,’ AI-generated security reports that were obviously wrong or low quality. It was kind of funny. It didn’t really worry us.
Something happened a month ago, and the world switched. Now we have real reports. All open source projects have real reports that are made with AI, but they’re good, and they’re real.
Greg Kroah-Hartman
, Linux kernel maintainer (
bio
), in conversation with Steven J. Vaughan-Nichols
Quote
2026-04-03
The challenge with AI in open source security has transitioned from an AI slop tsunami into more of a ... plain security report tsunami. Less slop but lots of reports. Many of them really good.
I’m spending hours per day on this now. It’s intense.
Daniel Stenberg
, lead developer of cURL
Quote
2026-04-03
On the kernel security list we’ve seen a huge bump of reports. We were between 2 and 3 per week maybe two years ago, then reached probably 10 a week over the last year with the only difference being only AI slop, and now since the beginning of the year we’re around 5-10 per day depending on the days (fridays and tuesdays seem the worst). Now most of these reports are correct, to the point that we had to bring in more maintainers to help us.
And we’re now seeing on a daily basis something that never happened before: duplicate reports, or the same bug found by two different people using (possibly slightly) different tools.
Willy Tarreau
, Lead Software Developer. HAPROXY
Note
2026-04-03
A fun thing about
recording a podcast
with a professional like Lenny Rachitsky is that his team know how to slice the resulting video up into TikTok-sized short form vertical videos. Here’s
one he shared on Twitter today
which ended up attracting over 1.1m views!
That was 48 seconds. Our
full conversation
lasted 1 hour 40 minutes.
Quote
2026-04-04
[GitHub] platform activity is surging. There were 1 billion commits in 2025. Now, it’s 275 million per week, on pace for 14 billion this year if growth remains linear (spoiler: it won’t.)
GitHub Actions has grown from 500M minutes/week in 2023 to 1B minutes/week in 2025, and now 2.1B minutes so far this week.
Kyle Daigle
, COO, GitHub
Quote
2026-04-05
From anonymized U.S. ChatGPT data, we are seeing:
~2M weekly messages on health insurance
~600K weekly messages [classified as healthcare] from people living in “hospital deserts” (30 min drive to nearest hospital)
7 out of 10 msgs happen outside clinic hours
Chengpeng Mou
, Head of Business Finance, OpenAI
Link
2026-04-05
Eight years of wanting, three months of building with AI
:
Lalit Maganti provides one of my favorite pieces of long-form writing on agentic engineering I’ve seen in ages.
They spent eight years thinking about and then three months building
syntaqlite
, which they describe as “
high-fidelity devtools that SQLite deserves
“.
The goal was to provide fast, robust and comprehensive linting and verifying tools for SQLite, suitable for use in language servers and other development tools - a parser, formatter, and verifier for SQLite queries. I’ve found myself wanting this kind of thing in the past myself, hence my (far less production-ready)
sqlite-ast
project from a few months ago.
Lalit had been procrastinating on this project for years, because of the inevitable tedium of needing to work through 400+ grammar rules to help build a parser. That’s exactly the kind of tedious work that coding agents excel at!
Claude Code helped get over that initial hump and build the first prototype:
AI basically let me put aside all my doubts on technical calls, my uncertainty of building the right thing and my reluctance to get started by giving me very concrete problems to work on. Instead of “I need to understand how SQLite’s parsing works”, it was “I need to get AI to suggest an approach for me so I can tear it up and build something better”. I work so much better with concrete prototypes to play with and code to look at than endlessly thinking about designs in my head, and AI lets me get to that point at a pace I could not have dreamed about before. Once I took the first step, every step after that was so much easier.
That first vibe-coded prototype worked great as a proof of concept, but they eventually made the decision to throw it away and start again from scratch. AI worked great for the low level details but did not produce a coherent high-level architecture:
I found that AI made me procrastinate on key design decisions. Because refactoring was cheap, I could always say “I’ll deal with this later.” And because AI could refactor at the same industrial scale it generated code, the cost of deferring felt low. But it wasn’t: deferring decisions corroded my ability to think clearly because the codebase stayed confusing in the meantime.
The second attempt took a lot longer and involved a great deal more human-in-the-loop decision making, but the result is a robust library that can stand the test of time.
It’s worth setting aside some time to read this whole thing - it’s full of non-obvious downsides to working heavily with AI, as well as a detailed explanation of how they overcame those hurdles.
The key idea I took away from this concerns AI’s weakness in terms of design and architecture:
When I was working on something where I didn’t even know what I wanted, AI was somewhere between unhelpful and harmful. The architecture of the project was the clearest case: I spent weeks in the early days following AI down dead ends, exploring designs that felt productive in the moment but collapsed under scrutiny. In hindsight, I have to wonder if it would have been faster just thinking it through without AI in the loop at all.
But expertise alone isn’t enough. Even when I understood a problem deeply, AI still struggled if the task had no objectively checkable answer. Implementation has a right answer, at least at a local level: the code compiles, the tests pass, the output matches what you asked for. Design doesn’t. We’re still arguing about OOP decades after it first took off.
Link
2026-04-06
Google AI Edge Gallery
:
Terrible name, really great app: this is Google’s official app for running their Gemma 4 models (the E2B and E4B sizes, plus some members of the Gemma 3 family) directly on your iPhone.
It works
really
well. The E2B model is a 2.54GB download and is both fast and genuinely useful.
The app also provides “ask questions about images” and audio transcription (up to 30s) with the two small Gemma 4 models, and has an interesting “skills” demo which demonstrates tool calling against eight different interactive widgets, each implemented as an HTML page (though sadly the source code is not visible): interactive-map, kitchen-adventure, calculate-hash, text-spinner, mood-tracker, mnemonic-password, query-wikipedia, and qr-code.
(That demo did freeze the app when I tried to add a follow-up prompt though.)
This is the first time I’ve seen a local model vendor release an official app for trying out their models on in iPhone. Sadly it’s missing permanent logs - conversations with this app are ephemeral.
Link
2026-04-07
GLM-5.1: Towards Long-Horizon Tasks
:
Chinese AI lab Z.ai’s latest model is a giant 754B parameter 1.51TB (on
Hugging Face
) MIT-licensed monster - the same size as their previous GLM-5 release, and sharing the
same paper
.
It’s available
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
That’s the pelican, floating up in the top left corner.
I usually don’t do follow-up prompts for the pelican test, but in this case I made an exception:
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
<!-- Pouch (lower beak) with wobble -->
<g>
    <path d=”M42,-58 Q43,-50 48,-42 Q55,-35 62,-38 Q70,-42 75,-60 L42,-58 Z” fill=”url(#pouchGrad)” stroke=”#b06008” stroke-width=”1” opacity=”0.9”/>
    <path d=”M48,-50 Q55,-46 60,-52” fill=”none” stroke=”#c06a08” stroke-width=”0.8” opacity=”0.6”/>
    <animateTransform attributeName=”transform” type=”scale”
    values=”1,1; 1.03,0.97; 1,1” dur=”0.75s” repeatCount=”indefinite”
    additive=”sum”/>
</g>
Update
: On Bluesky
@charles.capps.me suggested
a “NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER” and...
The HTML+SVG comments on that one include
/* Earring sparkle */, <!-- Opossum fur gradient -->, <!-- Distant treeline silhouette - Virginia pines -->, <!-- Front paw on handlebar -->
- here’s
the transcript
and the
HTML result
.
Quote
2026-04-08
I have a feeling that
everyone likes using AI tools to try doing someone else’s profession
. They’re much less keen when someone else uses it for their profession.
Giles Turnbull
, AI and the human voice
