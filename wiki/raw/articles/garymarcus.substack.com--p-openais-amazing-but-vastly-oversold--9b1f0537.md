---
title: "OpenAI’s amazing - but vastly oversold - new model Astra"
url: "https://garymarcus.substack.com/p/openais-amazing-but-vastly-oversold"
fetched_at: 2026-08-03T10:24:08.324142+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# OpenAI’s amazing - but vastly oversold - new model Astra

Source: https://garymarcus.substack.com/p/openais-amazing-but-vastly-oversold

Astra, a new model that OpenAI is testing internally, is amazing. No denying that:
An internal version of Astra, ’s next major model family, solved 10 major open problems in mathematics, quantum complexity, and theoretical computer science.

We believe it will be a major step for scientific reasoning.
10 proofs from our next major model Astra on long-standing open problems in mathematics and theoretical computer science (also including new circuit lower bounds for computing the permanent!)

GPT-5.6 has already enabled so much exciting work in math and science. Can’t wait to
8:17 AM · Aug 1, 2026
·
8.4M Views
664 Replies
·
2.11K Reposts
·
14.9K Likes
But at the same time, a whole raft of people, some fairly prominent, are running around making a deeply flawed argument about the implications.
See if you can spot the fallacy. Here are three examples among many.
Everyone in the world will soon be able to use the model that made these breakthroughs for every problem they face in life, no matter how mundane, at a cost that will fall dramatically in a matter of months. I still struggle to get my head around this fact.
ten significant advances in mathematics and theoretical computer science.

solved using an internal version of Astra, our next major model, for a total cost of about $2000 at Sol API prices:
1:29 PM · Aug 1, 2026
·
89.9K Views
79 Replies
·
102 Reposts
·
1.48K Likes
Solving just one of these problems would have been unbelievably impressive.

The next OpenAI model solved ten.

Looks like GPT-next is going to make Fable look like a toy, and usher in a golden age of science.
An internal version of Astra, @OpenAI’s next major model family, solved 10 major open problems in mathematics, quantum complexity, and theoretical computer science.

We believe it will be a major step for scientific reasoning. https://t.co/iP6cyheZ7i https://t.co/jHuulDwV46
4:45 PM · Aug 1, 2026
·
59K Views
77 Replies
·
27 Reposts
·
404 Likes
Another tweet went so far as to claim that “
the species just crossed a one-way threshold
”;  Elon Musk took it
as evidence that we had reached The Singularity
.
Each is making essentially the same error.
§
The fallacy has a name; it’s called the
fallacy of composition
.
The
wiki on it
is filled with great examples; here are just the first few.
What’s the manifestation of the fallacy in the current case? Thinking that a system that is great at a certain kind of math problem is great at all math,  great at science or even quite possibly great at everything. The “AGI-is-near” community keeps committing the same logical fallacy over and over. Every time there’s an advance, I see the same error.
Here’s how the fallacy works.
1. Someone pretends that all cognition is created equally. (Totally untrue.)
2. Whenever AI achieves success on some form of (fancy) cognition, they want you to believe that success on all forms of AI is imminent.
You don’t have to be a cognitive psychologist to realize that this inference just doesn’t follow. We all know, for example, that expertise in math doesn’t guarantee genius in all domains. Someone who is great at math or physics or programming may struggle with writing or understanding human relationships (and conversely a great writer may be weak at math, etc).
Expertise in one domain does not at all guarantee expertise in all or even most domains
.
That’s precisely *why* people like Howard Gardner and Robert Sternberg developed multidimensional theories of intelligence, why the SAT tests math separately from verbal, etc.
Astra appears to be —we still haven’t seen the methodology—great at math, or at least some forms of math, but that does not mean that it will avoid hallucinations or solve the reliability problems other GenAI systems have. It doesn’t even mean it will be able to read PDFs reliably.  And it doesn’t mean it will be the first generative AI to be able to obey hard rules, either. (Which should terrify you.)
In particular, Astra is obviously excellent at some problems; but that doesn’t mean it will be excellent or even competent at problems that
are hard to formalize
. It doesn’t mean it will be magic. It doesn’t mean it’s AGI or ASI or any of that.
It’s *very* impressive. But I see no reason whatsoever to think Astra is AGI let alone ASI. If it can score even a 5/10 on
my 2024 bet with Miles Brundage
I will be surprised.
I wouldn’t go on about this fallacy at such length if (a) it wasn’t wildly common and (b) I didn’t think that there was very good reason to think that the fallacy applied
here.
It’s not an accident that math is where these models are shining. Math lends itself to two things: verification (using symbolic tools), and massive amounts of cheaply produced synthetic data where you can guarantee that the answers are correct. The same applies to coding — but it is
not
true in general.  You can generate as many math facts as you want; you can’t simulate the open-ended world. You can verify math; you can’t verify a military strategy in the same way.
This is not news.  I have been pointing this out at least since January 2025 [first line should have said coding
and
math], echoing something Ernie Davis and I said about Go (and why AlphaGo would not be a panacea) in 2019:
OpenAI can do what Astra does in math because
math allows for external tools to do verification and to create synthetic data
.
That doesn’t make Astra less impressive, but as we learned a decade ago from IBM’s shambolic and ultimately failed attempt to turn Jeopardy-winning Watson into a cancer-fighting machine,
success in one domain does not guarantee success in all.
The kind of math OpenAI is dealing with here is radically different from many (perhaps most) real-world problems in which verification neither guarantees solutions nor allows one to produce infinite training data effectively for free.
To expect it to be a universal solvent is to show you don’t understand that basic fact.
Yesterday's tweet and blog were marketing, not science. Neither of those nor the 249-page math article that went with them give any information about how this was accomplished:
“Open”AI dropped a 249 page paper on new math results but not one page is about how the model works, how the proofs were verified, what role if any humans played, whether any of the proposed proofs had errors, etc.

What happened to science?
2:59 PM · Aug 1, 2026
·
123K Views
108 Replies
·
67 Reposts
·
694 Likes
In an email commenting on the first draft of this essay Ernie Davis added, quite rightly:
To properly evaluate the significance of these discoveries we would need some
critical pieces of information.
First: How many conjectures were attempted? If the OpenAI team picked these 10 conjectures at random from the space of all outstanding significant mathematical conjectures and Astra solved all 10, that would be amazing; but that seems altogether unlikely. If they cherry-picked 50 conjectures that they thought Astra would succeed on and it succeeded on 10, that’s still amazing, but significantly less so. If they ran Astra on all 1000 or so open Erdos conjectures and on 10,000 other open conjectures, then its failure to solve those is significant information on its limits as a mathematical reasoner.
Second: OpenAI brags loudly that this was done for a total computation cost of $2000. It seems a safe bet that this includes only the conjectures where Astra succeeded, not the ones where it failed. But what was the cost in terms of the salaries of the highly-paid mathematicians and computer scientists who worked on this project? I’d be astonished if it was less than $20,000 and would not be surprised if it was upward of $200,000.
We don’t know this, and the way things are going, we may never know this. We still have zero information about the OpenAI system that achieved gold-medal performance at the 2025 International Mathematical Olympiad, and very little information about the Google system.
Astra is good at some math but it is
very doubtful that math is “solved”
(
as a lot of people on X seemed to believe
).  It seems to be good at
certain kinds
of math
But quite possibly not all. Here are some examples from
Eric Weinstein on X
about some kinds of math it might be less good at
Ernie Davis also adds “
The problem of autoformalization --- turning mathematics written by a human mathematician into a strictly logical form -- does not seem close to being solved, though certainly progress has been made. For example: For the last two years, mathematician Kevin Buzzard has been leading a
project
to formalize Andrew Wiles' proof of Fermat's Last Theorem in Lean. It is quite safe to say that no AI system is capable of carrying out that monumental task. Presumably if they could do it unassisted, they would scoop him, and if they could cut down his work from years to weeks, he would be using them.”
Consistent with my general prediction that facility in math doesn’t guarantee universality
,
it appears that
Astra’s proofwriting is not on par with the proofs themselves
(echoing something Ernie Davis and I observed here a year ago)” [click through for full tweet]
4. I am disappointed by the writeup of this proof (sorry Lijie -- I should've taken a look at it earlier!). It writes in a way that's characteristic of a lot of ChatGPT-generated proofs, in which it elaborates at length on "boilerplate" setup, but then nonchalantly introduces
6:39 PM · Aug 1, 2026
·
63.2K Views
11 Replies
·
13 Reposts
·
382 Likes
I seriously doubt that Astra will magically solve all the things that don’t work reliably in current models.
Will it be able to reliably extract numbers from arbitrary PDFs? Doubt it. Will it solve Sabine Hossenfelder’s desire to have AI write scripts [click the tweet for more details] for her YouTube series? Doubt it.
I have tried many times to get ChatGPT, Claude, Grok or Gemini to write scripts for my YouTube videos. It is still a complete failure. 

For one thing, they are unable to come up with interesting topics. They will inevitably suggest topics that have already been widely reported
12:34 PM · Aug 1, 2026
·
127K Views
490 Replies
·
144 Reposts
·
2.17K Likes
Astra is not (as Musk suggested) the Singularity
. Enough said. (But see my recent essay on the topic; nothing has really changed).
It is absurd to claim that the Astra debut is “
plausibly the most significant day in the history of mathematics
”
as a bunch of people went around saying, based on a quote from one run of Fable (which might give different answers if asked twice). There was no new theory, no new techniques, and as impressive as it is, it is not on remotely on par with the development of calculus,  algebra, logarithms, probability, the decimal system, information theory, the concept of zero. Says Davis “The claim quoted from Fable that "several of those would individually have been the result of the decade" is absurd … As a reality check, 14 of David Hilbert's 23 problems have been solved since 1900 --- that's one every nine years --- and these results are nowhere near that league. You could easily compile a list of 100 much more important results that have been proved since 1926.”
I doubt it will lead directly to
a cure for cancer
, or enormous advances in
“materials research, energy production, drug discovery, Everything”, as some excitable AI “influencers” envision.
Nor does this mean we just entered “the era of automated scientific discovery”
. Against overwrought claims like these…
Derya Unutmaz, MD
@DeryaTR_
Another major historical milestone in the age of AI has been achieved by 's next model family, Astra! We are now entering the era of automated scientific discovery!

Essentially, mathematics and theoretical computer science have entered the post-human-bottleneck era of
An internal version of Astra, @OpenAI’s next major model family, solved 10 major open problems in mathematics, quantum complexity, and theoretical computer science.

We believe it will be a major step for scientific reasoning. https://t.co/iP6cyheZ7i https://t.co/jHuulDwV46
12:47 PM · Aug 1, 2026
·
25.7K Views
29 Replies
·
45 Reposts
·
463 Likes
.. this just came out, echoing the new article by
Arvind Narayanan
and others that I linked to a few days ago.
How To Prompt
@HowToPrompt__
MIT and Harvard argue LLMs are nowhere near doing real scientific discovery.

They published a paper called “Evaluating Large Language Models in Scientific Discovery.”

Every week, tech labs claim an LLM has made a breakthrough in biology, physics, or chemistry.

But this proves
4:54 AM · Aug 2, 2026
·
26.9K Views
33 Replies
·
61 Reposts
·
241 Likes
Despite immense pushback on X yesterday (most of it ad hominem, some literally involving fabrication, a lot of it involving outright lies), my overall hot take on Astra remains what I first posted:
What’s sad about this is that Ernie Davis and I raised a lot of the same points about how one
could
properly examine new systems a year ago:
I get that people are excited about Astra, but anyone hoping for magic is likely to be disappointed.
