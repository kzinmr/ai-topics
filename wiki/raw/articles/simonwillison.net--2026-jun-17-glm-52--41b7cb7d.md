---
title: "GLM-5.2 is probably the most powerful text-only open weights LLM"
url: "https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything"
fetched_at: 2026-06-18T07:01:30.023304+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GLM-5.2 is probably the most powerful text-only open weights LLM

Source: https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything

GLM-5.2 is probably the most powerful text-only open weights LLM
17th June 2026
Chinese AI lab
Z.ai
released GLM-5.2
to their coding plan subscribers
on June 13th, and then yesterday (June 16th) released the full open weights under an MIT license. Similar in size to their previous GLM-5 and GLM-5.1 releases, this is 753B parameter,
1.51TB
monster—with 40 active parameters (Mixture of Experts). GLM-5.2 is a text input only model—Z.ai have a separate vision family most recently represented by
GLM-5V-Turbo
, but that one isn’t open weights. GLM-5.2 has a 1 million token context window, up from GLM-5.1’s 200,000.
The buzz around this model is strong.
Artificial Analysis, who run one of the most widely respected independent benchmarks:
GLM-5.2 is the new leading open weights model on the Artificial Analysis Intelligence Index
.
GLM-5.2 is the leading open weights model on the Intelligence Index v4.1.
At 51, it leads MiniMax-M3 (44), DeepSeek V4 Pro (max, 44) and Kimi K2.6 (43)
They did however find it to be quite token-hungry:
GLM-5.2 uses more output tokens per task than other leading open weights models:
the model uses 43k output tokens per Intelligence Index task, up from GLM-5.1 (26k) and above MiniMax-M3 (24k), Kimi K2.6 (35k) and DeepSeek V4 Pro (max, 37k)
The model is also now ranked 2nd on the
Code Arena WebDev leaderboard
, behind only Claude Fable 5. That leaderboard measures “front-end web development tasks, including agentic coding workflows”. I’m impressed to see it rank so highly given the lack of image input, which I had incorrectly assumed was a key part of building a truly great frontend coding model.
I’ve been trying it out
via OpenRouter
, which has it from 9 different providers, almost all of which are charging $1.40/million for input and $4.40/million for output. For comparison, GPT-5.5 is $5/$30 and Claude Opus 4.5-4.8 is $5/$25.
Excellent pelican, disappointing opossum
GLM-5.1 gave me
one of my favorite pelicans
and my
all time favorite opossum
(for the prompt “Generate an SVG of a NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER”.) Interestingly, in both of those cases the model chose to return SVG wrapped in an HTML document that added additional animations using CSS.
Let’s try GLM-5.2. For “Generate an SVG of a pelican riding a bicycle” I
got this
:
It’s a self-contained fully animated SVG, and the animations aren’t broken! Often I’ll see eyes falling off or wheels rotating independently of the bicycle but here everything works great. It’s a very nice vector illustration of a pelican too. Very impressive.
Sadly, the NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER did not come out
nearly as well
:
This is such a step down from GLM-5.1! As a reminder, that possum looked like this:
5.2 didn’t even
try
to animate it.
