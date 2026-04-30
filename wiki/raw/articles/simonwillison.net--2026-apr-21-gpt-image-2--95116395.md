---
title: "Where’s the raccoon with the ham radio? (ChatGPT Images 2.0)"
url: "https://simonwillison.net/2026/Apr/21/gpt-image-2/#atom-everything"
fetched_at: 2026-04-30T07:01:12.891217+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Where’s the raccoon with the ham radio? (ChatGPT Images 2.0)

Source: https://simonwillison.net/2026/Apr/21/gpt-image-2/#atom-everything

Where’s the raccoon with the ham radio? (ChatGPT Images 2.0)
21st April 2026
OpenAI
released ChatGPT Images 2.0 today
, their latest image generation model. On
the livestream
Sam Altman said that the leap from gpt-image-1 to gpt-image-2 was equivalent to jumping from GPT-3 to GPT-5. Here’s how I put it to the test.
My prompt:
Do a where's Waldo style image but it's where is the raccoon holding a ham radio
gpt-image-1
First as a baseline here’s what I got from the older gpt-image-1 using ChatGPT directly:
I wasn’t able to spot the raccoon—I quickly realized that testing image generation models on Where’s Waldo style images (Where’s Wally in the UK) can be pretty frustrating!
I tried
getting Claude Opus 4.7
with its new higher resolution inputs to solve it but it was convinced there was a raccoon it couldn’t find thanks to the instruction card at the top left of the image:
Yes — there’s at least one raccoon in the picture, but it’s very well hidden
. In my careful sweep through zoomed-in sections, honestly, I couldn’t definitively spot a raccoon holding a ham radio. [...]
Nano Banana 2 and Pro
Next I tried Google’s Nano Banana 2,
via Gemini
:
That one was pretty obvious, the raccoon is in the “Amateur Radio Club” booth in the center of the image!
Claude said:
Honestly, this one wasn’t really hiding — he’s the star of the booth. Feels like the illustrator took pity on us after that last impossible scene. The little “W6HAM” callsign pun on the booth sign is a nice touch too.
I also tried Nano Banana Pro
in AI Studio
and got this, by far the worst result from any model. Not sure what went wrong here!
gpt-image-2
With the baseline established, let’s try out the new model.
I used an updated version of my
openai_image.py
script, which is a thin wrapper around the
OpenAI Python
client library. Their client library hasn’t yet been updated to include
gpt-image-2
but thankfully it doesn’t validate the model ID so you can use it anyway.
Here’s how I ran that:
OPENAI_API_KEY=
"
$(
llm keys get openai
)
"
\
  uv run https://tools.simonwillison.net/python/openai_image.py \
  -m gpt-image-2 \
"
Do a where's Waldo style image but it's where is the raccoon holding a ham radio
"
Here’s what I got back. I don’t
think
there’s a raccoon in there—I couldn’t spot one, and neither could Claude.
The
OpenAI image generation cookbook
has been updated with notes on
gpt-image-2
, including the
outputQuality
setting and available sizes.
I tried setting
outputQuality
to
high
and the dimensions to
3840x2160
—I believe that’s the maximum—and got this—a 17MB PNG which I converted to a 5MB WEBP:
OPENAI_API_KEY=
"
$(
llm keys get openai
)
"
\
  uv run
'
https://raw.githubusercontent.com/simonw/tools/refs/heads/main/python/openai_image.py
'
\
  -m gpt-image-2
"
Do a where's Waldo style image but it's where is the raccoon holding a ham radio
"
\
  --quality high --size 3840x2160
That’s pretty great! There’s a raccoon with a ham radio in there (bottom left, quite easy to spot).
The image used 13,342 output tokens, which are charged at $30/million so a total cost of around
40 cents
.
Takeaways
I think this new ChatGPT image generation model takes the crown from Gemini, at least for the moment.
Where’s Waldo style images are an infuriating and somewhat foolish way to test these models, but they do help illustrate how good they are getting at complex illustrations combining both text and details.
Update: asking models to solve this is risky
rizaco
on Hacker News
asked ChatGPT to draw a red circle around the raccoon in one of the images in which I had failed to find one. Here’s an animated mix of their result and the original image:
Looks like we definitely can’t trust these models to usefully solve their own puzzles!
