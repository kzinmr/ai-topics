---
title: "Walking the dog with Claude"
url: "http://xania.org/202605/walking-the-dog?utm_source=feed&utm_medium=rss"
fetched_at: 2026-05-25T07:01:33.603093+00:00
source: "xania.org"
tags: [blog, raw]
---

# Walking the dog with Claude

Source: http://xania.org/202605/walking-the-dog?utm_source=feed&utm_medium=rss

Walking the dog with Claude
Written with LLM assistance.
The interview format is genuine; the prose is lightly tidied from voice notes.
I had lunch with a pal yesterday, and we got onto the subject of why
so much technical material is either accurate-but-impenetrable or
polished-but-slightly-wrong. It’s a gap I think about a lot, partly
because I make videos that try to land in the middle of it and don’t
always succeed. The conversation stuck with me on the drive home.
This morning, whilst walking the dog, I tried something a bit silly: I
asked Claude (dictating to the mobile app
) to interview me about it.
Voice-to-text on one end, an LLM
playing journalist on the other, and a black lab setting the pace. What
follows is that conversation, lightly tidied – paraphrased in places,
verbatim in others. The LLM is the interviewer; I’m the subject.
The words are mine, the questions aren’t.
Claude:
Let’s start wide. Your friend’s comment was about the gap
between people who know things and people who can explain them. Where
do you see that gap most clearly?
Matt:
Almost everywhere, honestly. The people with the information
may not be great presenters, and the great presenters don’t necessarily
have the information. You end up with two failure modes: dry, accurate
material that nobody wants to watch, or polished material that gets the
details slightly wrong in ways that make experts twitch. Both are
common; the overlap is rarer than I’d like.
Claude:
Who do you think bridges it well?
Matt:
Grady Hillhouse on
Practical Engineering
– he actually is a
civil engineer, and it shows. Devin Stone,
LegalEagle
, is a working
lawyer. And the Brady Haran shows –
Numberphile
,
Computerphile
– solve
it from the other end: Brady and
Sean Riley
are well-prepared “straight
man” interviewers, and the experts they bring in are carefully chosen.
The format itself is the trick. I’m biased on Computerphile, mind, since
I’ve
done a few
.
Claude:
Let’s talk craft. You’ve mentioned the Usborne robots
before. What are they, and why do they still matter to you?
Matt:
There were these late-70s / early-80s
Usborne books
on how
computers worked, and they used little cartoon robots to show
information moving around inside the machine. As a kid that just
clicked for me. The thing I find quietly remarkable is that I still
use it. When I’m reasoning about out-of-order execution, register
renaming, modern microarchitecture – somewhere underneath, there are
still little robots shuffling things between pigeon-holes. I’m not
consciously picturing them anymore, but the shape of the model is the
same.
Claude:
That sounds like a beginner’s model that you’ve never quite
outgrown.
Matt:
Maybe you’re right? The thing I
keep coming back to is that what’s easy for me to reason about as an
expert
is often
exactly
what’s easy for a beginner to grasp. The
mental model and the explanation aren’t two things – they’re the same
object. I think people assume good explanations are simplifications of
the expert’s real model. Sometimes they’re just the expert’s real
model.
Claude:
You’ve talked about a “tell my mum” test. Where does that
come from?
Matt:
When I was a teenager with a
BBC Micro
, if I figured
something out I’d run downstairs and tell my mum. She’d listen and
either follow or politely pretend to. Somewhere along the way that
became my actual yardstick: could I explain this to her? Simple enough
to follow, but
not
dumbed down. True. And underwritten by the fact
that I actually understand the thing properly, even if I don’t expose
all of it. If I can’t clear that bar, I’m not ready.
Claude:
And the prep that goes with it?
Matt:
More than people probably realise. For the early
Computerphiles I’d practise on paper, out loud, two or three times,
even though the finished video looks off-the-cuff. The
off-the-cuffness is the prep working.
Claude:
You skipped a Computerphile recording last week. What
happened?
Matt:
Yeah, that’s been nagging at me. The topic was how computers
tell the time – it’s fallout from my C++Now keynote on benchmarking
.
I wanted to talk about
rdtsc
and
rdtscp
on x86, how raw counter
ticks get turned into wall-clock time, and the out-of-order execution
wrinkles that show up when you read the clock. Good material. I just
couldn’t find a visual hook. Computerphile’s whole stick is hand-drawn,
handwritten stuff on lined paper, and I hadn’t worked out how to draw
this one. I’m now mulling writing a tiny x86 assembly snippet
long-hand and using
that
to show out-of-order behaviour. But the honest
reason I bailed is that I hadn’t cleared the mum test yet. I hadn’t
reduced it cleanly enough.
Claude:
Why do you do these at all? Be honest.
Matt:
Two layers, I think. The first is that I’m a show-off. My
mum’s side of the family are performers – singers and dancers, mostly –
and I did school musicals, played instruments, all of that. It faded
in my twenties and I’ve sort of rediscovered it through conference
talks and the videos. I like being on stage. I’m not going to pretend
otherwise.
Claude:
And the second layer?
Matt:
I was giving a guest lecture recently and made the
showing-off joke to a friend afterwards. He said, “I don’t think
that’s all of it.” He’s being kind, but he’s also right. The bigger
thing is the moment someone
gets
it. “I know this stuff, and now so
do you – isn’t that cool?” That penny-dropping moment is the actual
fuel. My territory is microarchitecture, compilers, assembly – how
computers really work, underneath.
Advent of Compiler Optimisations
2025
was probably the most concentrated dose of all of this in one go.
Claude:
You’ve been quieter on the video front lately. Why?
Matt:
Because they cost. And I want to be careful, because the
costs aren’t the same shape. Something like Advent of Compiler
Optimisations is genuinely expensive in
hours
– between the blog
posts, filming and editing, I
reckon
about ten hours per 5–10-minute
video, and there were twenty-five of them. Computerphile is much
lighter on time – an hour or two of prep once the idea’s ready. The
harder cost there isn’t hours, it’s the conceptual distillation. I
can’t take it to Sean until it clears the mum bar. Last week’s
no-show is the example.
Claude:
Final question, and it’s a deliberate provocation.
Compiler Explorer
takes the most opaque part of writing C++ – what the
compiler actually does – and makes it inspectable in real time. Is
that the same impulse as the videos and the talks, just made into a
tool?
Matt:
Do you know what? I’d never actually thought of it that way.
But – yeah, I suppose there is a bit of that going on. There’s the
immediacy I like: it compiles as you type, rather than you having to
kick off some long process. And I try
to keep pushing it to be more
accessible, more instinctive. Put like that, there’s clearly overlap.
The tool, the videos and the talks have something of the same flavour I suppose.
That last question was quite a surprise; I genuinely hadn’t thought of CE that
way before.
I want to do more of these – more Computerphiles, more talks, more written-up material – and I
keep not doing them as often as I’d like. The honest reason is the one
above: sometimes the cost is hours, sometimes it’s getting the idea
clean enough to be worth saying
. I’m trying to give myself permission
for the output to be
infrequent
without it being
stopped
. Those
are different things, and I keep conflating them.
And – is this the future? An LLM as an interviewer while you walk the
dog? I’m not sure, but I will say: I came home
with a thought I didn’t leave with, which is more than I can say for
most dog walks. Monty remains unconvinced (though he’s now snoozing happily on the sofa).
