---
title: "The AI-collapse pre-mortem"
url: "https://berthub.eu/articles/posts/an-ai-premortem/"
fetched_at: 2026-04-29T07:02:25.082167+00:00
source: "berthub.eu"
tags: [blog, raw]
---

# The AI-collapse pre-mortem

Source: https://berthub.eu/articles/posts/an-ai-premortem/

An essential part of being able to say ‘I told you so’ is in fact having told you so. Here goes.
In April 2023, I wrote an article titled
AI: Guaranteed to disrupt our economies
. In this piece I also announced I was going to make a fool of myself by making some AI predictions. I have singularly failed to do so. In retrospect this was all spot on, except for perhaps missing the sheer magnitude of the madness that was about to ensue.
We’ve since had 30 further months to think about AI and to observe what it can and can’t do. Meanwhile, wise people (and Sam Altman) are starting to talk about AI possibly being
a bubble that is about to burst
(
here
,
here
and
here
).
When this happens, lots of people will be ready with reviews of how AI apparently sucks, or why we suck. I’d like to get my word in first, in this AI-collapse pre-mortem.
In what follows, I am not claiming AI is ‘good’ or ’ethical’. These are important questions, but I am not addressing them here. But for completeness, I am no fan of what people are doing with LLMs, how AI is burning through far too much energy, and the copyright issues also annoy me.
The tl;dr: even if the AI bubble bursts, LLMs can do some amazing things, despite not being overly useful in a business sense while also often being very wrong. Meanwhile, the other parts of AI have already led to a Nobel prize, and are doing astounding things for translation, transcription and image analysis. The AI bubble collapsing has no bearing on that this is some very impressive technology (even if
LLMs
are not generally useful yet, frequently very wrong and worrying on many fronts). AI is not going away, and we’d be fools to disregard it because everyone overhyped it enormously while ruining the economy.
Photo by
Anton Maksimov
on
Unsplash
AI is not close to being intelligent, yet it is an astounding miracle
As I wrote in 2023, we get hung up on if AI is truly intelligent. The current LLM-craze is in fact a very worthwhile vehicle for talking about what we consider intelligence to be. Our thinking on this has evolved - being able to beat absolutely everyone at chess is now not considered enough to be intelligent. But previously we did consider that a useful bar.
Back in the 1980s, intelligence was treated comprehensively in the
Chinese Room Argument
: is a room that can answer questions in Chinese using mountains of paper instructions “intelligent”? Anyone who wants to opine on AI would do well to
re-read that discussion
.
No matter if AI is intelligent, even today’s primordial large language models perform absolute miracles. And they are also right now mostly quite useless, while still upsetting many an apple cart.
What?
Yes. I love this joke. Someone runs into a guy playing chess with a pigeon. The man is blown away, a chess playing pigeon! So he asks the guy, wow, that is some special bird! And he says that it’s not so impressive since the pigeon still loses most of the time.
Now, the LLMs we have today are clearly chess playing birds. The thing is not that they aren’t very clever. The thing is that they are functional
at all
, and quite often impressively so. We should recognize these ‘stochastic parrots’ for what they are - an astounding achievement. And it wasn’t even that hard, lots of independent implementations now exist. And you can run these on relatively normal computers. Who knows where this technology might go in a few decades?
If you are a developer and want to experience training an LLM firsthand and figuring out how it all works, head to the 8000 line
nanochat
by Andrej Karpathy, who also wowed us back in 2015 with his post
The Unreasonable Effectiveness of Recurrent Neural Networks
.
It may be hard to square this positive appreciation with seeing how hard a time a typical LLM has with counting the number of r’s in “strawberry”. Note that in the above I never claimed that LLMs are intelligent or generally useful. Much like the pigeon that only occasionally wins at chess - no one has any use for that. But finding such a bird would profoundly upset our understanding of both birds and intelligence.
It is simultaneously possible for LLMs to be mostly useless (for now) and for them to be gobsmackingly upsetting, and showing that apparently if you hook up matrices in the right way, they can correct your grammar, change the tense of your sentences, spot bugs in your code or pinpoint (and fix) your mixed similes and split infinitives.
Because, to be very clear, before 2019 NOTHING came close to doing anything like that (in a generic sense).
Now, that does not mean we are close to a generically intelligent AI. Whatever that might mean by the way.
But the relative ease with which we got a pigeon that is actually not that bad at chess should give us pause. This technology is not going away. And most certainly not quietly.
I know that many people derive solace from LLMs often being singularly stupid, and “not really thinking”. And these models are most definitely overhyped, and indeed do not “think”. But our own brains and intelligence also exist and are physical and not magical things. That our current LLMs are “faking it” is no indication that we’ll never find the right arrangement of math and numbers that will deliver the real thing.
By one count evolution has delivered “serious intelligence” no less than three times (independently), in mammals,
corvids
, and
cephalopods
. If you take it broadly, you might include ant colonies as well. Intelligence can’t be
that
special. Oxygenic photosynthesis evolved exactly
once
and that took 1.5 billion years
. That’s special.
So even if the AI bubble collapses shortly because no one has an idea how to turn the existing language models into a profitable business proposition, don’t expect this to mean that LLMs will go away. Also, they most certainly won’t get worse at what they (
can
) do. Although to be clear, current efforts are not in any way on a recognizable path to “intelligence”.
This post was usefully proofread by ChatGPT, which found several issues that the human proofreaders had not. So take the claims of LLMs being useless with a grain of salt. If you are smart about it an LLM can be useful. But selling to clever people is not a trillion dollar opportunity.
The other things that AI is doing
Here I am quite confident. The current stock of AI pattern matching/predicting machines is crazily impressive. I use the Whisper AI speech recognition model often (
on my own hardware
) to transcribe talks I give. I speak a popular and a relatively rare language (Dutch), but Whisper doesn’t care. I can alternate Dutch and English and it is not fazed. Quote something in German mid-sentence? No problem either.
Recently I studied a transcription and was quite pleased with how well I had apparently phrased things. I later listened to the original audio and I was shocked to find that the transcription had cleaned up an absolute mess of a sentence. The transcript was actually what I should have said. Now is this entirely good? Can you use this without proofreading? You can not. However, the performance is clearly
super-human
. Whisper does this stunt for 99 languages. It correctly transcribes jargon that normal people have no idea about.
Another example. When (human) DNA is converted into RNA and thence into proteins, parts of the DNA are elided. As humans, we can not predict where such ‘splicing’ happens in DNA. To figure it out requires real live laboratories, because nature does know where the splicing occurs (obviously). I hand-built a truly trivial neural network to see if it could learn to predict those splice junctions. And stunningly enough, even my amateur efforts delivered something somewhat useful quickly enough. The equivalent of teaching a pigeon the rules of chess in a few days. This must be some pigeon.
Similarly, as humans, we have a very hard time predicting the shape of protein molecules based on the DNA that underlies them. For AI this does not appear to be very challenging, leading to a 2024 Nobel Prize in Chemistry for the achievements of
AlphaFold
. Here too there are accusations that AlphaFold “doesn’t really know what it is doing”, and this may in some philosophical sense be true. AlphaFold has not
generically
solved the problem of molecular or even protein shape prediction - it only works (well) on the kinds of proteins we see in nature. However, the work it does there is truly astounding, and we have no idea how it does what it does. It most certainly (again) is performing at a super-human level, even humans augmented with normal computers.
In medical circles, AI is making impressive strides in radiology. The jury is still out on who is best (us or the machine), but I can tell you this, AI-radiology is most definitely going to beat “we don’t have a radiologist available right now”-results. And I have a hard time seeing how AI is not going to be very useful here, even if only as a second opinion.
In terms of pattern matching & predicting transformations, be it from speech to text, or from English to Dutch, or from DNA to molecular shapes, AI is simply unsurpassed right now.
So, post-collapse, now what?
Even though the AI-economy might collapse, and perhaps take the rest of the economy with it, this does not invalidate that there are AI things that are truly astounding, and will remain so. They’ll likely get better, even.
I am as much in the dark as anyone on if you can get LLMs to reliably do useful work. Or if we’ll ever take this technology to something we could call ‘real intelligence’.
However, I am sure that a collapsing economic bubble is not a useful data point about where this technology will end up. Especially given the useful and impressive capabilities of AI outside of large language models, or video generation.
So once the collapse happens, try to keep an open mind on what this technology can actually do. Even if a lot of it makes no business sense right now. Once properly reevaluated, we may find more worthwhile gems in there.
