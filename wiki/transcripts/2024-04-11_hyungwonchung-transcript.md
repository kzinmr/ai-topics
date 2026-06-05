---
title: "Stanford CS25: Shaping the Future of AI from the History of Transformer — Transcript"
author: Hyung Won Chung (@hwchung27)
source: YouTube
url: https://www.youtube.com/watch?v=orDKvo8h71o
published: 2024-04-11
type: transcript
tags:
  - transcript
  - scaling-hypothesis
  - transformer
  - encoder-decoder
---

# Talk Transcript — Shaping the Future of AI from the History of Transformer

[00:05] now we have uh kangan um give a talk so
[00:08] he is currently a research scientist at
[00:10] um on the open AI chat gbd team um he
[00:13] has worked on various aspects of large
[00:15] language models um things like
[00:17] pre-training instruction fine-tuning
[00:19] reinforcement learning with human
[00:21] feedback uh reasoning um and so forth
[00:24] and some of his notable Works include um
[00:26] the scaling flan paper such as flan T5
[00:29] as well as flan Palm and uh t5x the
[00:31] training framework used to train the
[00:33] Palm language model and before open AI
[00:36] um he was at Google brain and um he
[00:38] received his PhD from MIT

[00:54] all right my name isan and really
[00:57] happy to be here today and this week I
[00:59] was thinking about okay I'm giving a lecture on
[01:08] Transformers at Stanford what should I
[01:10] talk about and I thought some of
[01:13] you in this room and in Zoom will
[01:16] actually go shape the future of AI so
[01:18] maybe I should talk about that it's a
[01:20] really important goal and ambitious and
[01:21] we really have to get it right so that
[01:24] could be a good topic to think about and
[01:26] when we talk about something into the
[01:29] future the best place to get advice
[01:31] is to look into the history and in
[01:34] particular we'll look at the early
[01:36] history of Transformer and try to learn
[01:39] many lessons from there and the goal
[01:41] will be to develop a unified perspective
[01:45] with which we can look into many
[01:48] seemingly disjoint events and from that
[01:51] we can probably hope to project
[01:54] into the future what might be coming

[02:05] AI is advancing so fast that it's so
[02:11] hard to keep up and doesn't matter if
[02:13] you have like years of experience so
[02:16] many things are coming out every week
[02:18] that it's just hard to keep up and I do
[02:20] see many people spend a lot of time and
[02:22] energy catching up with latest
[02:24] development the cutting edge and the
[02:27] newest thing and then not enough
[02:29] attention goes into old things

## The Bitter Lesson & Driving Forces

[05:11] the best way to talk about this is to
[05:13] talk about what I call the driving force
[05:15] behind AI progress so there are many
[05:18] things happening in AI every week and
[05:20] some of them are important some are not
[05:22] so important and we want to identify
[05:24] this Dominant driving force behind AI

[05:33] if you think about reading a paper
[05:35] there is surface level information and
[05:39] deep level information and the trick is
[05:42] to identify something that is called
[05:44] the zeitgeist of the time
[05:46] so there's a deep intellectual current
[05:48] running across papers and it manifests
[05:50] in many different forms so we want to
[05:53] identify that intellectual current

[06:21] the dominant driving force behind AI
[06:24] is that compute is getting cheaper
[06:27] and this is getting cheaper
[06:29] exponentially and associated with it
[06:32] is this scaling effort

[07:16] the Bitter Lesson (Rich Sutton) basically
[07:19] says that over 70 years of AI research
[07:22] the biggest lesson that we can learn is
[07:24] that general methods that leverage
[07:26] compute are ultimately the most effective
[07:29] and by far
[07:30] so to understand that we need to know
[07:33] what are these general methods and
[07:35] what's the opposite of general methods

[07:37] the opposite is something that I will call
[07:39] structure or modeling assumptions that
[07:42] we as humans impose onto the method
[07:44] to solve the problem more efficiently

[07:50] having more structure makes a method
[07:52] less scalable and having less structure
[07:54] makes a method more scalable

## The Structure Paradox

[10:11] I want to argue that adding optimal
[10:13] inductive bias for a given level of
[10:16] compute is critically important but at
[10:19] the same time they are shortcuts that
[10:21] will hinder future scaling so remove
[10:24] them later

[10:38] compute is getting cheaper faster
[10:41] than we are becoming better researchers

## Transformer Architecture Analysis

[12:40] if we look at encoder-decoder vs decoder-only
[12:45] the transformation from encoder-decoder
[12:47] to decoder-only involves removing
[12:49] various structures

### Structure 1: Separate parameters (13:41)
[13:41] in machine translation the input and
[13:43] target are completely different languages
[13:46] so it makes sense to have separate
[13:47] parameters for input and output

[14:15] but the model should learn world
[13:49] knowledge not just language

### Structure 2: Information bottleneck (21:30)
[21:30] in encoder-decoder the target attends
[21:33] only to the final layer of the encoder
[21:37] this could be a bottleneck

### Structure 3: Bidirectionality (28:44)
[32:16] bidirectional attention was really
[32:17] useful at solving SQuAD but at scale
[32:20] I don't think this matters as much
[32:22] in Flan 2 we tried both bidirectional
[32:25] and unidirectional fine-tuning
[32:27] didn't really make much difference

## Conclusion & Final Remark

[35:16] the dominant driving force covering
[35:19] this AI research was the exponentially
[35:22] cheaper compute and associated scaling
[35:24] effort

[35:40] we have looked at these analysis
[35:43] which are all things one can say
[35:46] this is just historical artifacts
[35:48] and doesn't matter
[35:50] but if you do many of these and
[35:53] look at current events you can hopefully
[35:55] think about those in a more unified
[35:57] manner

[36:00] see what assumptions in my
[36:03] problem that I need to revisit

[36:16] together we can really shape the future
[36:19] of AI in a really nice way so that's it
[36:19] thanks
