---
title: "(One) Good AI Is Here"
url: "https://anildash.com/2026/04/28/one-good-ai-is-here/"
fetched_at: 2026-04-29T07:00:51.987303+00:00
source: "anildash.com"
tags: [blog, raw]
---

# (One) Good AI Is Here

Source: https://anildash.com/2026/04/28/one-good-ai-is-here/

The cultural battles over AI have broken down over predictable lines in the past few years, with critics rightfully calling out the big AI platforms for training on content without consent, recklessly building without considering environmental impact, and designing platforms that are unaccountable because their code and weights (the parameters that describe how an AI model works) aren’t open for third-parties to evaluate. The AI zealots have done themselves no favors, by not only dismissing all of these valid criticisms, but by also making increasingly outlandish and extreme claims about the capabilities of the Big AI platforms, while simultaneously scaremongering about the brutal effect they’ll have on people’s lives and careers. It’s no wonder the public sentiment about AI has become so negative.
But a small cohort of us who are curious about LLMs as a technology, yet deeply critical of Big AI companies for their impact on society, have been asking
what would “good” AI look like
? Is it possible to make versions of these technologies that provide real benefits, and actually help people, without all of the attendant harms? We’ve had prior eras of machine learning tools that were useful technologies without being massively destructive — are the negative externalities intrinsic to LLMs in general?
We might have just gotten our first glimpse at an AI that’s
actually
good.
This is just one small example that I saw recently, in a very unexpected place, but I can’t get it out of my mind. It’s not a tool that every person in the world is going to use, but it feels a bit like the famous
William Gibson
quote, “The future is already here — it's just not very evenly distributed.” This might be a little tiny bit of a good AI future, and now we just need to distribute the same kind of thing to a lot more people.
What’s
good
? Something that checks every box I can think of for our most immediately positive goals: it’s trained entirely with data that were consensually gathered; it’s completely open source and open weights, so anybody can examine it to know exactly how it works and what biases or flaws it might have; it’s designed to run on ordinary computers that normal people have access to — including those that can run entirely on renewable and responsible energy sources. And it is controlled by
creators
, not extractors, people who are inarguably on the side of artists and creatives and those who make art and culture in the world, designed to support and enable and empower their expression. No billionaires or guests of Epstein’s island were involved in the creation of this technology.
Going Green
Let’s back up a little bit.
Corridor Digital
is a video production shop and content studio that have been popular on YouTube since the earliest days of its independent filmmaking community. They’ve stayed relevant through many changing trends and format shifts, most recently becoming wildly popular for their ongoing series of video reactions to the visual effects and stunt sequences in popular films and TV shows. Over time, the series has earned a ton of respect from many of the top practitioners in the industry from areas like VFX, stunt work, animation, and more. They even went direct to their fans with a nice subscription service, helping support their work directly.
But still, this was basically a bunch of (mostly) guys making videos. Until something interesting happened recently.
Niko Pueringer, one of the cofounders of Corridor Digital, and one of the more prominent on-screen characters in their filmed content, is not a software developer. Then, a few weeks ago, he decided he had reached a breaking point in one of the challenges that effects artists regularly have to deal with: green screen keying. (That’s the process in which an artist extracts a foreground image from the green background when they’re creating a clip that will be composited together for an effects shot.) Basically, the current tools were crude enough that it felt like an almost manual process, requiring artists to painstakingly cut out images like they were snipping out pictures from a magazine with a dull pair of scissors.
So, Niko created a set of his own videos using CGI to simulate a green screen, and began training an AI model — in this case, a neural network — to learn how to key the footage that he'd generated for this purpose. (He was able to build the tools that carried out this training by asking one of the current popular commercial AI tools to help.) After a good bit of time, trial and error, and heavy computation, the end result was a system that was
extremely
effective at green screen keying. He even sent an early version of the system to other professionals in the industry to compare its results to their own commercial-grade tools, and they confirmed that it often performed comparably to some of the best tools on the market.
Niko made
a video explaining the project
— and released the code that would enable others to run the same tool for themselves. (Do check out the clip — the team have become very gifted storytellers, and the narrative does a wonderful job of bringing you along on the journey of the highs and lows of discovering how to try to invent something new.)
Opening up
Once the new tool, now called
CorridorKey
was out in the wild, a community rapidly formed, and instantly adopted the software into a full-fledged open source project — even though Niko had never led an open source project before. As is typical for such an enthusiast community, they were able to teach their leader about all the arcane processes involved in accepting code improvements from strangers around the world.
Within
days
, the community had made the tool significantly easier to use — especially for non-expert video editors who would struggle with the complexities of configuring conventional (super-nerdy) open source software. Other community members massively reduced the hardware requirements needed to perform the advanced video processing that the tool enables, moving from needing some of the most powerful workstations available to running on ordinary consumer desktop computers that many home filmmakers might have access to. And all of this for
free
. Many comparable tools would cost thousands, or even
tens
of thousands of dollars for video editing teams to use. As Niko said in his original video, he didn’t “want to pay rent for his paintbrush”.
In the
follow-up video
just two weeks later, it was clear that there had been an extraordinary response to the release of CorridorKey. And an even more extraordinary next milestone was achieved, with the announcement that Niko would be releasing
all of the original training data
for the creation of the tool — all of the videos and content used to create the model, so that others could replicate the work, or even create their own models if they wanted to improve upon the work itself.
For the technically-minded, CorridorKey is licensed under a modified Creative Commons license, with the intention of preventing commercial exploitation without consent. I’m sure this will prompt some hand-wringing about whether it fits everyone’s definitions of “open source”, but given that someone could certainly reimplement this approach from scratch, given all of the material that Niko and his community have shared, I think that’s a distinction without a difference. The larger point here about a turning point in the AI and LLM ecosystem is what is transformative for creators who’ve been beleaguered by the AI cheerleading for the last few years.
Importantly,
using
CorridorKey doesn’t impose any restrictions or obligations on people making videos. There’s no phoning home, no scraping of videos to be used for training models, not even collecting an email address for marketing purposes. It’s a stark contrast to what people are used to in the commercial software world, let alone the hyper-surveillance world of most Big AI companies.
Where does this lead?
Okay, so that’s one tool. But what if you’re not a video creator who does things with green screens? How does this help anybody else? There are a few really important breakthroughs here that start to help more people realize what’s possible.
The bad behaviors are a choice.
The Big AI companies that take content without consent, or who refuse to let people see their code, or who insist they can’t give people control over how their models run and whether they are responsible about their environmental impact can now be definitively refuted. If this small team of creators who
aren’t even a tech company
can make an AI that does the right thing, how come the biggest companies in the world can’t?
It’s about purpose, not one-size-fits-all.
There’s no risk that CorridorKey is going to tell kids to self-harm in the way that ChatGPT does. Because CorridorKey has a specific
job
to do. And that’s the way AI should work — solving a specific problem for a particular community, instead of trying to be all things to all people, which is when these platforms start becoming unaccountable and start harming massive numbers of people.
It’s
under
-hyped, not over-hyped.
If anything, the launch of CorridorKey was buried towards the end of a longer video that was about the creative process; the launch video doesn’t even mention the name of the product! The creator doesn’t make any claims about how great it is, or say it’s better than anything else, or say it’s going to change the world. Instead, he’s humble and hopeful that it’s of use to a specific community, and they respond with enthusiasm and connection and collaboration to that sincerity. This isn’t a tool that needs to be shoved in anybody’s face.
All of these traits are things that can be replicated in many more fields, by many more passionate people who don’t have to necessarily be experts, but who care about displacing the tech tycoons’ one-size-fits-all platforms with something that is human-scale and accountable.
For years, I’ve had this conviction that a better AI is possible, and I understand why many people have felt I was being naive, or that the way tech is today makes it impossible for such a thing to survive. But I think the tide is turning, and people are so fed up with the
software-brained
CEOs forcing things on them that they don’t want. That doesn’t mean that people hate technology! It just means that they hate what these dudes have made technology
in to
.
It’s nice to be reminded of what tech can be at its best. Sometimes it’s a thing that extracts exactly what we want to see from the background we’re trying to leave behind.
