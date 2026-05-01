---
title: "The toil of (blog) art"
url: "https://lcamtuf.substack.com/p/the-toil-of-blog-art"
fetched_at: 2026-05-01T07:02:12.265350+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# The toil of (blog) art

Source: https://lcamtuf.substack.com/p/the-toil-of-blog-art

When writing a technical blog, the first 90% of every article is a lot easier than the final 10%. Sometimes, the challenge is collecting your own thoughts; I remember walking through the forest and talking to myself about the articles about
Gödel’s beavers
or
infinity
. Other times, the difficulty is the implementation of an idea. I sometimes spend days in the workshop or writing code to get, say, the throwaway image of a
square-wave spectrogram
at the end of a whimsical post.
That said, by far the most consistent challenge is art. Illustrations are important, easy to half-ass, and fiendishly difficult to get right. I’m fortunate enough that photography has been my
lifelong hobby
, so I have little difficulty capturing good photos of the physical items I want to talk about:
A macro photo of a photodiode sensor. By author.
Similarly, because I’ve been
interested in CAD and CAM
for nearly two decades, I know how to draw shapes in 3D and know enough about rendering tech to make the result look good:
An explanation of resin casting, by author.
Alas, both approaches have their limits. Photography just doesn’t work for conceptual diagrams; 3D could, but it’s slow and makes little sense for two-dimensional diagrams, such as circuit schematics of most function plots.
Over the past three years, this forced me to step outside my comfort zone and develop a new toolkit for simple, technical visualizations. If you’re a long-time subscriber, you might have seen the changing art style of the posts. What you probably don’t know is that I often revise older articles to try out new visualizations and hone in my skills. So, let’s talk shop!
Electronic circuits are a common theme of my posts; the lifeblood of this trade are circuit schematics. I’m old enough to remember the beautiful look of hand-drawn schematics in the era before the advent of electronic design automation (EDA) software:
An old circuit schematic.
Unfortunately, the industry no longer takes pride in this craft; the output from modern schematic capture tools, such as KiCad, is uniformly hideous:
An example of KiCad schematic capture.
I used this style for some of the electronics-related articles I published in the 2010s, but for this Substack, I wanted to do better. This meant ditching EDA for general-purpose drawing software. At first, I experimented with the same CAD software I use for 3D part design,
Rhino3D
:
Chicken coop controller in Rhino3D. By author.
This approach had several advantages. First, I was already familiar with the software. Second, CAD tools are tailored for technical drawings: it’s a breeze to precisely align shapes, parametrically transform and duplicate objects, and so forth. At the same time, while the schematics looked more readable, they were nothing to write home about.
In a quest for software that would allow me to give the schematics a more organic look, I eventually came across
Excalidraw
. Excalidraw is an exceedingly simple, web-based vector drawing tool. It’s limited and clunky, but with time, I’ve gotten good at working around many of its flaws:
A schematic of a microphone amplifier in Excalidraw, by author.
What I learned from these two tools is that consistency is key. There is a temptation to start every new diagram with a clean slate, but it’s almost always the wrong call. You need to develop a set of conventions you follow every time: scale, line thickness, font colors, a library of reusable design elements to copy-and-paste into new designs. This both makes the tool faster to use — rivaling any EDA package — and allows you to refine the style over time, discarding failed ideas and preserving the tricks that worked well.
This brings us to
Affinity
. Affinity is a “grown-up” image editing suite that supports bitmap and vector files; I’ve been using it for photo editing ever since Adobe moved to a predatory subscription model for Photoshop. It took me longer to figure out the vector features, in part because of the overwhelming feature set. This is where the lessons from Rhino3D and Excalidraw paid off: on the latest attempt, I knew not to get distracted and to focus on a simple, reusable workflow first.
My own library of electronic components in Affinity.
This allowed me to finally get in the groove and replicate the hand-drawn vibe I’ve been after. The new style hasn’t been featured in any recent articles yet, but I’ve gone ahead and updated some older posts. For example, the earlier microphone amplifier circuit now looks the following way:
A decent microphone amplifier. By author.
Electronic schematics are about the simplest case of technical illustrations. They’re just a map of connections between standard symbols, laid out according to simple rules. There’s no need to make use of depth, color, or motion.
Many other technical drawings aren’t as easy; the challenge isn’t putting lines on paper, it’s figuring out the most effective way to convey the information in the first place. You need to figure out which elements you want to draw the attention to, and how to provide visual hints of the dynamics you’re trying to illustrate.
I confess that I wasn’t putting much thought into it early on. For example, here’s the original 2024 illustration for an article on photodiodes:
It’s not unusable, but it’s also not good. It’s hard to read and doesn’t make a clear distinction between different materials (solid color) and an electrical region that forms at the junction (hatched overlay).
Here’s my more recent take:
A better version of the same.
Once again, the trick isn’t pulling off a single illustration like this; it’s building a standardized workflow that lets you crank out dozens of them. You need to converge on backgrounds, line styles, shading, typefaces, arrows, and so on. With this done, you can take an old and janky illustration, such as the following visual from an
article on magnetism
:
A simple model of a conductor.
…and then turn it into the following:
A prettier model of the same. By author.
As hinted earlier, in many 2D drawings, it’s a challenge to imply a specific three-dimensional order of objects or to suggest that some of them are in motion. Arrows and annotations don’t always cut it. After a fair amount of trial and error, I settled on subtle outlines, nonlinear shadows, and “afterimages”, as shown in this illustration of a simple rotary encoder:
Explaining a rotary encoder.
The next time you see a blog illustration that doesn’t look like 💩 and wasn’t cranked out by AI, remember that more time might have gone into making that single picture than into writing all of the surrounding text.
