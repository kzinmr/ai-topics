---
title: "Producing a video lesson"
url: "https://rakhim.exotext.com/producing-a-video-lesson"
fetched_at: 2026-04-29T07:01:21.745290+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Producing a video lesson

Source: https://rakhim.exotext.com/producing-a-video-lesson

A few years ago, I've made a bunch of
videos on YouTube
about foundational topics in programming. There are lots of hand-drawn cartoons and some rudimentary animation. People keep asking how I made those, so here we go.
Inspiration
Structure and Interpretation of Computer Programs
(SICP). If you’re only going to read one book on programming, it should be this one.
Interactive articles and talks by
Bret Victor
. An amazing person — at the very least, watch his talk
Inventing on Principle
.
Mindstorms
by Seymour Papert. About math anxiety, poor teaching methods, and innovative approaches to education. Every teacher — especially math or CS teachers — should read it.
A bunch of YouTube channels with great visualizations:
Ted-ED
,
Vox
,
Minute Physics
,
Numberphile
,
Computerphile
.
Scriptwriting
First, I define the topic and write the script. I have an initial course outline, but the order sometimes shifts to maintain logical flow.
I start with all major topics written on sticky notes, laid out on the desk: past topics, current candidates, and future ones. This helps visualize what concepts were already introduced, which ones I need to reinforce, and which to hint at.
The upcoming lesson is on
recursion
. Time to develop the explanation flow and draft visuals.
Visuals aren’t secondary — they are first-class citizens alongside the verbal explanation. Consistency is key. For example, constants were introduced as sticky notes (name on one side, value on the other).
The next lesson had introduced variables: erasable versions of those notes. Functions are boxes with input/output holes.
Functions are visualized as boxes that return values.
Functions can be "chained", so that the returning value is immediately fed into another function. I mean literally —
anotherFunction(someFunction(3))
is:
In this lesson I extend the same metaphor: functions can call other functions, which effectively creates new "boxes"; a function can even call itself, creating a new box of the same structure, but with different data. This is key to understanding recursion visually.
I sketch the visuals and the structure in a notebook, then switch to Sublime Text 3 for the actual script. One lesson is about 1000 words. Drafting takes 1–3 hours. I review, read aloud, revise, and then move to recording the audio. (though some lessons also contain exercises.)
Audio
I record using my trusty Rode Podcaster mic (10 years old!). Lessons run 5–6 minutes. I usually do at least two takes. When something goes wrong, I just keep recording, sometimes repeating the same segment multiple times. This is fixed in editing later.
Recording 5 minutes of usable audio takes up to 40 minutes. Once it’s "not terrible", I clean it up: cut errors, adjust pauses, remove noises, apply filters (noise reduction, EQ, compression).
Visuals
I draw intentionally simple visuals using an excellet iPad app called Paper. I storyboard scenes in alignment with the script. Each lesson folder ends up filled with  three types of media: drawings, videos, and text (mostly code).
I also film real-world objects — sticky notes, boxes, strings, pencils — using my phone and a ghetto DIY tripod.
Editing and publishing
The most time-consuming part. I import everything into Final Cut Pro and sync visuals with audio. Fill the whole timeline with a structural skeleton, and some static filler assets, then proceed to enrich it all with actual detailed content.
Sound effects: I record simple ones myself, others I find online. Occasionally, I add brief music or movie clips for laughs.
Some sequences, like visualizing recursive factorial calls, are particularly intensive, involving multiple layers of animation and transitions.
Once exported, I review the video again (at double speed). Then I upload it to YouTube. For the thumbnail, I pick an interesting frame, rearrange elements if needed, and add a handwritten title.
Subtitles are added using the lesson script — after cleaning it up and removing Markdown. YouTube's auto-sync feature handles timing based on the voice track, which is a lifesaver.
Final Result
Here’s the final video:
VIDEO
