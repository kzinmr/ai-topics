---
title: "Three LLM inflection points in twelve months"
url: "https://simonwillison.net/2026/Nov/24/llm-inflection-points/"
fetched_at: 2026-11-25T10:00:48.419267+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Three LLM inflection points in twelve months

Source: https://simonwillison.net/2026/Nov/24/llm-inflection-points/

Three LLM inflection points in twelve months
24th November 2026
I gave a keynote at the
AI Engineer Code Summit
a couple of weeks ago, constructed around the idea that there have been three significant inflection points in the abilities of LLMs and coding agents in the past twelve months.
Here’s
the video
of the talk. In this post I’m going to pull out the major inflection point theme and interrogate it more deeply.
Coding agents in November 2025
Today, November 24th 2026, is the one year anniversary of the release of
Claude Opus 4.5
. With hindsight, this was a consequential model.
In the Opus 4.5 announcement, Anthropic said:
Testers noted that Claude Opus 4.5 handles ambiguity and reasons about tradeoffs without hand-holding. They told us that, when pointed at a complex, multi-system bug, Opus 4.5 figures out the fix. They said that tasks that were near-impossible for Sonnet 4.5 just a few weeks ago are now within reach.
This held up.
Claude Code was 9 months old at that point, having been
introduced alongside Claude 3.7 Sonnet
on February 24th, 2025.
Opus 4.5 was the first model I had used with Claude Code where the default result was generally the right thing. I hadn’t been using Claude Code as a daily driver because it didn’t feel reliable enough—I had to correct it often enough that it didn’t feel like a clear accelerant.
The new Opus changed that. For most of the coding problems I faced on a daily basis, Opus would
get them right
. It was clearly faster than working through the problems myself.
Also in November, OpenAI released GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex, and GPT-5.1-Codex-Max. These had a similar effect on their Codex coding agent: it became reliably useful for many of my coding tasks.
The timing was convenient, because the December holidays were upon us. A lot of people, myself included, spent December tinkering with these new tools to see what they could do. By January we were ready to use them for our actual work.
Fable class models in June/July
We got our first hint of Claude Fable in April, when Anthropic announced Claude Mythos and
said that it was
too dangerous
to release
, due to its improved cybersecurity capabilities. Mythos was a model that could not just find security vulnerabilities, it could also figure out how to exploit them.
In June we got to see how good that model was for ourselves, with the release of Claude Fable 5—a defanged Mythos, that would solve most problems but would actively block you from using it for security work.
After three glorious days... the US government took it away from us. Fable 5 was placed under export controls that effectively banned the model. We wouldn’t get it back until July 1st.
For me, Fable was an inflection point because it introduced us to what I now think of as
Fable class models
. My definition of these:
In June I wrote about how
Claude Fable is relentlessly proactive
, after I asked it to help fix a display glitch in Safari and it spun up its own
pyobjc-framework-Quartz
screenshot mechanism and a CORS-enabled localhost logging server to help resolve the bug.
A more recent example of the power of Fable class models is my
mysterious beep finder
from a couple of weeks ago. I gave Opus 5.5 and then Fable 5.2 access to five WebAudio microphones in a room full of boxes and it was able to triangulate the source of an infuriating mysterious beep to within about 40cm.
Give it a goal, give it the right tools, and watch it cook.
I’d currently class Claude Fable 5, 5.1, 5.2 and Claude Opus 5.5 as Fable class (I think of Opus 5.5 as “cheap Fable”). GPT-6 Astra got there for me too, and I think the new Gemini 4 Neon may count as well.
These now represent the baseline for what I expect from a frontier model.
3D modeling and game development in September/October
Something interesting happened with frontier LLMs over just the past four months: they got
really good
at 3D modeling. Set them up
with Blender
or ask them to write Three.js code and they’ll produce credible models of almost anything you ask for.
I first noticed this with Claude Fable 5, but it really kicked into gear with Opus 5.5, GPT-5.6 Sol, GPT-6 Astra, and most recently the Gemini 4 family. Here’s
Gemini 4 Neon’s attempt
at “Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data”, for example.
3D spatial awareness is crucial if you want to use vision LLMs for robotics. I don’t know if 3D modeling capabilities are a side-effect of the labs focusing on that or vice-versa.
Back in August I experimented with
having Fable 5 build me a raccoon heist game
. It had 3D graphics, looked like a game, and played really poorly. GPT-5.6 Sol Ultra
did a much better job
but the game itself was still pretty dull after the first 90 seconds of play.
I was somewhat relieved that designing a game that was
fun
appeared to remain a uniquely human pursuit. I even used that
in a talk
in September to reassure people that us humans still had a role to play!
Then, I tried telling Claude Opus 5.5 “This game isn’t fun enough yet. Make it a LOT more fun.”
And it worked
. My Command & Conquer-style RTS went from boring to deeply entertaining overnight, after Opus spent 12 hours playtesting new features and rebalancing the gameplay.
Opus 5.5 was the first model I’d used that appeared to understand fun. I’ve since worked on
several little game projects
where prompts like “Think hard about how to make sure it is both fun and beautiful” produced results that kept me engaged for significant amounts of time.
Opus 5.5 came out on September 22nd, 2026. I’ve been to two different conferences since then where people showed me game projects they’d been working on that really did feel like proper, worthwhile games.
The indie games scene has descended into a
full-blown culture war
over AI-assisted programming. A lot of people are calling GTA VI
the last pre-generative AI blockbuster
.
It feels like another inflection point to me.
Is Fable 5.2 an inflection point too?
I’m still trying to decide if Fable 5.2 represents a new inflection point, or just another incremental improvement.
I’m getting
so much
done with that model right now!
It seems to have taste that almost exactly matches my own. I have been burning through all sorts of gnarly problems that I’ve been thinking about (or procrastinating on) for several years now. The release notes for Datasette
1.0a42
,
1.0a43
, and
1.0a44
—plus LLM
0.37
,
0.37.1
,
0.37.2
,
0.37.3
, and
0.38
—
all in the last three weeks
, represent a flood of fixes, features and improvements.
If this does represent an inflection point, the key feature seems to be that
if you can imagine and then clearly describe a piece of software, Fable can build it
. That’s a wild thing to say, but it matches my experience over the past few weeks.
Software development has transformed beyond recognition in the last year. I don’t think I’ll ever go back to typing most of my code by hand.
