---
title: "Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing"
url: "https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing"
fetched_at: 2026-08-17T10:30:54.629576+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing

Source: https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing

Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing
Sunday, 16 August 2026
When I
wrote this week
about Anthropic’s announcement that all Claude models, worldwide, would soon begin “watermarking” everything they generate, including text, to comply with
this EU regulation
, we were left to speculate
how
this was going to work, because Anthropic offered not even a vague description of how it would work — despite the fact that the title of the announcement was, absurdly and insultingly, “
How Claude Marks AI-Generated Content
”.
My initial speculation was that maybe they’d hide invisible non-printing Unicode characters in the text. Just spitballing. Turns out that’s not what they’re going to do. What they’re going to do is apply a form of steganography, where the choice of words (or other token output) at inference time will leave fingerprints that can later, maybe, be detected probabilistically.
I initially guessed “invisible characters” not because I didn’t think of the semantic word-choice technique, but because I was a fool who took Anthropic at its word in their description of what they would do. Their original support document claims:
When a supported Claude model generates text, it weaves an
imperceptible watermark directly into the text itself. You won’t
see it, and it doesn’t change the meaning, quality, or readability
of Claude’s response.
They say “imperceptible” and “doesn’t change the meaning, quality, or readability”. Their words. Not
almost
imperceptible. Not
slightly
changes the meaning, quality, or readability. That made sense to me, because that’s absolutely what I want — nay, demand — from any tools I use personally. It’s unacceptable for a tool to sacrifice an iota of clarity, coherence, meaning, quality, etc. for the purpose of embedding hidden clues within the text to suggest its provenance. That’s what I would and will demand. And Anthropic’s (original) support document unambiguously claims that’s what their system will enable. So if that were true, I couldn’t see what was left other than hiding invisible characters within the text.
My error was believing Anthropic that their system wouldn’t adulterate and corrupt the semantics of the text their models generate.
That
is in fact exactly what they plan to do. I should have my head examined for believing a single word of a document titled “How Claude Marks AI-Generated Content” that doesn’t explain, at all, how Claude marks (or will mark) AI-generated content.
How It’s
Actually
Going to Work
Yesterday, on an entirely different website than
the original
“How Claude marks AI-generated content” article (the one that didn’t explain anything at all about how it works), Anthropic published “
How Claude’s Text Watermark Works
”, which does actually explain in layman-accessible terms how it’s going to work. I will return to Anthropic’s new highly euphemistic and slightly misleading description below.
There’s a bunch of research on this topic, some of which I have also linked to below. But the very best description of the general idea behind the technique is an interactive essay by James Padolsey, “
How AI Text Watermarking Works”
. It’s a wonderfully cogent read, and the interactive elements splendidly illustrate the main concepts. A+ work. If you have any interest in this at all, I dare say you must read — and play with — Padolsey’s piece.
But here’s my stab at a layman’s high-level summary. If you toss a coin
N
times and note the results, you can determine with a degree of certainty whether the coin is fair or biased. LLMs are, in their popular incarnations, non-deterministic. Ask the same question of the same model and you often get at least slightly different answers. Maybe the same meaning, but different phrasing. At each decision point for generating the next token, the model makes a choice. With these semantic watermarking techniques, they make different choices for some tokens based on word lists that could be called “green” and “red”. At each decision point, they’re a little more likely to pick a word from the green list than the red list. That doesn’t mean they never choose words from the red list. Just that they’re less likely to than they would if the adulterated marking technique weren’t in place. (Same way that a crooked 51-49 coin will still land “wrong” side up 49 times out of 100 on average.)
Words or word phrases are sorted into the green and red lists deterministically on the fly, at each “next token” generation point. So sometimes a specific word will be on the green list, and other times it will be on the red list. Someone with the secret key can determine which list a word will be on at each token generation point (which is how the watermarking is detected); those without the secret key cannot. This means there will never be a list of words that Claude prefers or eschews.
With coin flipping, the higher
N
is — the more times you flip — the more confident you can be that the coin is fair or biased. So too with this semantic watermarking. The more words in the text, the more accurate the analysis will be that the text was generated by a specific AI model or not. With too few coin flips, you can’t achieve any confidence at all regarding a coin’s fairness. With too few words (or tokens), there’s no way to achieve any confidence whether a string of text was AI-generated or not.
Given a string of text to examine for signs of a specific watermarking system, if there are more words tagged as green and fewer tagged as red than would otherwise be expected, the text can be flagged — with some degree of confidence — as having been generated, or merely modified, by the AI system that applies the specific secret-key watermarking system. The amount of confidence in the determination will obviously vary, significantly, based on the size of the text string and randomized weights given to words on the green and red lists. But only Anthropic will be able to determine if text was seemingly generated by Claude, and Anthropic will only be able to detect the watermarks that are applied by Claude. Claude can’t detect the hidden watermark signals generated by, say, Gemini, and Gemini can’t detect the hidden watermark signals created by Claude, because each implementation is predicated on secret keys held only by the LLM provider.
Objections to the Technical Premise
One of my fundamental problems with this is that no two synonyms carry the
exact
same meaning. “
He leaped at the chance
” and “
He jumped at the opportunity
” are very similar sentences expressing the same general sentiment, but they are
not
the same. The exact words we choose when writing matter. I want any LLM I use to choose the very best, most precise words at every single decision point. An obvious constraint that I accept is time and computation. Within the constraint of executing inference quickly, and at a certain cost per token, I want the best words. This constraint matches human writing. I could surely write a better column by taking longer to write it. I write with a sense of how much care I should put into every word and punctuation choice I make. I take more time with certain paragraphs, sentences, or even individual word choices when my gut feeling says I should.
In other words, these are
necessary
trade-offs. These factors are all in
my
interest: speed, cost, quality. Ideally I would like perfect writing, at instantaneous generation speed, at zero cost. None of those things are possible. Computation is not free of charge (and cloud-based LLM inference with leading models is actually expensive). Inference is not instantaneous. And great writing, whether natural or artificial, can only
approach
perfection.
The idea that anything other than
my
needs should factor into the generation of text
for me
is patently offensive.
This isn’t just about text one might generate with the intention of passing it off as their own natural work. This isn’t even about LLM proofreading of work written by hand. Anthropic is saying that
all
new Claude models are going to adulterate every single bit of text longer than 200 tokens (~150 words) they generate, including everything it presents to its users to read. So even in a private conversation between a user and Claude, which will never be read by anyone other than the user, Claude will begin making word choices in the name of marking its output in statistically predictable ways rather than maximizing clarity and precision.
Even today’s so-called frontier models are already decidedly
lacking in lucidity
. Claude, ChatGPT, Grok, et al. are “better writers” than most humans and produce better prose than the median human. But: no shit. Most people are terrible writers. The “average person” is pretty stupid and
half of all people are stupider than that
. And there are many smart, interesting people who are miserable writers. So as impressive as LLMs are, the bar is low. The best writing I see come out of these models is worse than anything I would choose to read for pleasure. And now Anthropic is saying they’re going to make it worse, on purpose, for purposes that do not benefit me in any way? Even if only slightly worse?
Get fucked.
Objections to the EU Regulation
Speaking of objections, the relevant EU regulation motivating all of this, “
Code of Practice on Transparency of AI-Generated Content
”, is red-tape nanny-state pipe-dream nonsense. Here’s Ben Thompson’s summary
from a paywalled Stratechery update this week
:
The regulation applies to text longer than 200 tokens.
The provider must mandate in their terms-of-service that users
not remove the watermarking.
The solution should be robust in terms of evading “typical
processing solutions” like screen shots, scanning and OCR,
copy-and-pasting, translations, etc.
Taken literally, compliant LLM terms of service must forbid users from rephrasing the output from models that comply with this regulation, because the word choices are the marks. But it’s not the European Union that is trying to impose their absurd, impractical, witch-hunt-fueling regulation on the entire world. That falls on Anthropic.
Complying with this, particularly with regard to
text
, is only going to create problems for honest users. Dishonest users attempting to pass off AI-generated text as their own writing (students, employees, whoever) will simply circumvent detection through non-compliant AI paraphrasing tools.
James Padolsey — whose interactive visual explanation of how these schemes work I linked to above — explains this in a post titled “
Anthropic’s Weak Watermarks Appease a Weak Law
” (which, if it rings a bell, I linked to
in a standalone post
earlier today):
The same thought that led to this law could have applied to
calculators at the time of their inception, had their outputs
revealed themselves through artefacts. Thankfully, a sum borne of
the brain is treated no differently from one produced by a
calculator. Likewise with spellcheckers. To make assistance
suspect only once the tool becomes capable enough to compose a
whole sentence is not a principled boundary. It is a moral premium
placed on difficulty itself.
Anthropic has nevertheless chosen a blanket, model-level
implementation that appears broader than the law’s minimum
requirement. That may be convenient compliance engineering, but it
discards distinctions the law expressly attempted to preserve. The
result is a signal broad enough to implicate harmless and
assistive use, yet fragile enough to be removed by a motivated
person through substantial recomposition. It risks concentrating
suspicion on ordinary and assistive users while remaining weakest
against deliberate deception.
Padolsey is the creator of
Declaude
, a delightfully simple web app that allows you to “Paste in AI-flavored text and get the same content back as plain prose”. Declaude’s original purpose is cleaning the saccharine Claude personality stink from text (whether it was created by Claude or any other LLM), but, if Anthropic persists in its stated plan to begin adulterating all text Claude generates, Declaude will also serve as a copy-paste single-extra-step way to eliminates those marks. Declaude is interesting and useful already, but it exemplifies how ill-considered and futile this EU regulation is when it comes to prose.
Google SynthID
Google has a watermarking system in place that they call SynthID, which they apply to AI-generated images, video, audio, and text. I’m concerned in this article only with text. With multimedia, embedded watermarks can be metadata within
files
, and truly not affect the experiential quality of the work when viewed or listened to. With text, we are talking about the actual words that are chosen. From the “AI-generated text” section of
Google DeepMind’s own description of SynthID
:
We’ve expanded SynthID to watermarking and identifying text
generated by the Gemini app and web experience. Large language
models generate text one word (token) at a time. Each word is
assigned a probability score, based on how likely it is to be
generated next. So for a sentence like “My favorite tropical
fruits are mango and…”, the word “bananas” would have a higher
probability score than the word “airplanes”. SynthID adjusts these
probability scores to generate a watermark. It’s not noticeable to
the human eye, and doesn’t affect the quality of the output.
In a group chat, a friend of mine quoted the above, and I responded that if a chatbot wrote “My favorite tropical fruits are mango and airplanes”, I’m pretty sure I’d fucking notice. Another friend then responded with this:
Days later, that still cracks me up.
But Google’s absurd description puts the lie to their own claim that it isn’t noticeable, and it serves to show just how little regard the people behind these generated-text fingerprinting schemes have for the actual craft of writing. Of course
bananas
has a higher probability score than
airplanes
, because airplanes aren’t fruit. But what about
pineapple
? Should the sentence complete to “mango and bananas” or “mango and pineapple”? That’s a good question, and the only acceptable answer for why an LLM should choose
bananas
instead of
pineapple
(or
coconut
, or
guava
, or
papaya
...) is that it has determined that it’s the best fit for the intended meaning, tone, and sentiment of the text. Not because
bananas
is on the watermarking “green” list and
pineapple
is on the “red” list, even though
pineapple
might be the better fit. Google’s own supposedly jocular description of how SynthID works in fact captures how the scheme perverts the text it generates.
They’re saying you won’t notice because if it only chooses
bananas
over
pineapple
for these fingerprinting purposes, well, they’re both tropical fruits and who cares. But it’s utter nonsense that the difference is “not noticeable to the human eye”. The semantic difference between
banana
and
pineapple
is just as noticeable to the human eye as the taste of the two are to the human tongue.
If it did produce “My favorite tropical fruits are mango and airplanes”, it’d be incredibly stupid, but it wouldn’t be
offensive
because we’d all recognize that something completely off-key happened. What’s offensive is that with a system like SynthId in place, where the fingerprinting decisions are motivated by a secret key, we have no idea whether it completed to “mango and bananas” because
bananas
was determined to be the best next token, or because
bananas
is in the “green” bucket of words. It calls every single word choice into question.
Here’s a paper published in Nature
where Google’s team behind SynthID published their work, after putting it into production with Gemini (née Bard):
We analysed approximately 20 million watermarked and unwatermarked
responses and computed the thumbs-up and thumbs-down rates (both
as a fraction of the total number of thumbs-up and thumbs-down
feedback received). We found that the thumbs-up rate for the two
models differed by 0.01% (with the watermarked model being
higher); and the thumbs-down rate differed by 0.02% (with the
watermarked model being lower). We found both of these differences
to be statistically insignificant, and well within the 95%
confidence intervals.
From this experiment, we conclude that over a wide variety of real
chatbot interactions, the difference in response quality and
utility, as judged by humans, is negligible. Subsequently,
non-distortionary SynthID-Text has been productionized and is
currently watermarking responses in Gemini and Gemini Advanced. To
the best of our knowledge, this evaluation represents the first
systematic watermarking investigation of its kind within a
large-scale production system.
To this I say:
Gemini/Bard’s thumbs-up/thumbs-down buttons are not a good experiment for evaluating the effect on quality. If a chatbot tells me “My favorite tropical fruits are mango and bananas” instead of “mango and pineapple”, I’m not going to give the response a thumbs down because of the fruit it chose. I’d give it a thumbs down if it said “airplanes”, yes, but that’s a strawman. (The paper in Nature even uses “My favourite tropical fruit is ...” as an illustration, but in the paper, the only four next tokens considered are, in order of probability distribution, mango, lychee, papaya, and durian. No airplanes. And, conveniently, in the paper’s example, the “winner” of the watermarking “tournament” just happens to be mango, the one that would have been selected as the best if the watermarking weren’t in place.)
A “difference in response quality and utility, as judged by humans” that is “negligible” does not mean
imperceptible
. What they really mean is that it’s only slightly worse and that everyone is either too stupid to notice or too indifferent to care.
It’s widely considered that Gemini is behind ChatGPT and Claude in quality. Perhaps the fact that they’ve put SynthID-text into production is one of many reasons why. I personally agree that Gemini’s prose is inferior. Maybe the use of SynthID has nothing to do with the fact that I, along with the general public consensus, consider Gemini to be a second-rate chatbot — but in that case, maybe it’s the fact that Gemini is a second-rate chatbot that makes the difference “negligible” when Google started mixing in SynthID-motivated tokens in its results. It’s a lot more likely that your restaurant customers won’t notice that you replaced your regular coffee
with Folgers Crystals
if your regular coffee is second-rate to start with.
Anthropic
Now, finally, back to Anthropic’s new “
How Claude’s Text Watermark Works
”, published yesterday. I have some comments.
To summarize:
We use a method of watermarking that does not have any practical
impact on the quality or content of Claude’s outputs;
The difference between watermarked and un-watermarked text will
not be distinguishable to readers;
Translation:
Specific words do not matter and we don’t think anyone reads anything closely.
Nothing is added to the text and there are no hidden characters;
This would have been worth clarifying at the outset.
Watermarking won’t be specific to Claude. As of August 2, the EU
requires AI providers serving its market to mark AI-generated
content. Other major model developers have signed the same Code of
Practice and will be implementing their own watermarks.
No other AI provider has stated that they will apply such marking, adulterating all generated text, outside the EU.
Take the sentence “The weather today was cold and…”. The next word
is very unlikely to be “sugary.” But it is quite likely to be
“overcast” or “grey.” Under most circumstances, it doesn’t matter
much to the reader which of these latter two words the model
ultimately chooses — the meaning of the sentence is largely the
same either way. In cases like this, the choice is settled by a
random number.
Arguing that
grey
vs.
overcast
“doesn’t matter much to the reader” is the crux of my argument that this entire endeavor is a perverse adulteration of what it means to write — or to read. That it’s subtle in some ways makes it
more
perverse, because it’s sneaky.
In internal testing, we’ve seen no impact of watermarking on the
content, level of creativity, or readability of Claude’s text. In
the
SynthID-Text paper
, which introduced the technique we
use, Google DeepMind tested this impact by serving a model that
used watermarking to a portion of their Gemini traffic and
comparing thumbs-up and thumbs-down ratings. They found no
statistically significant differences from the unwatermarked
model. And in a controlled study, human raters comparing
watermarked and unwatermarked answers side-by-side saw no
difference in quality.
See above for my argument that this thumbs-up/thumbs-down data is absolutely worthless in evaluating whether the SynthID-style word-bias watermarking makes text worse. By definition it
must
make text worse, unless the underlying LLM model’s scoring is wrong, because the nature of the watermarking algorithm requires it to sometimes increase the probability of selecting a
worse
word choice and decrease the probability of selecting the model’s
best
choice. It’s only a question of how much worse. What Google’s thumb-counting data shows is only that it isn’t so much worse as to make Gemini users click the thumbs-down button.
Watermarking doesn’t change the meaning or experience for the
person reading it, but if you wanted to check after the fact
whether the text was likely generated by Claude, the watermark
allows you to do so.
No, it does not. Because the entire scheme is tied to secret keys held only by the AI provider, it only allows Anthropic, not “you”, to check anything.
When Claude proofreads text written by a person, what it gives
back has generally only been lightly edited; because nearly all
the words are the person’s, there’s very little (if anything) for
the watermark to attach to. Depending on the length of the text
and how heavily Claude has edited it, those changes might not be
enough to make Claude’s involvement detectable. The more Claude
writes, the more decisions it has to make, and the more space
there is for a watermark.
Translation:
No one can ever again use Claude for proofreading their own prose unless they’re willing to risk that the whole thing might be flagged as having been generated by Claude.
For example, once the model has written “2 + 2 =”, there is a very
clear best choice for the next token (if the model is completing
the sum, there isn’t an answer that’s equally as good as “4”; if
it’s talking about George Orwell’s
Nineteen Eighty-Four
, there
isn’t an answer that’s equally as good as “5”). The “nudge” of the
watermark wouldn’t be applied here. For the same reason, code — which in very many cases has to be exact — has generally less
watermarking than some other forms of text.
Having said that, in areas where there
is
an arbitrary choice
between particular words or terms within the code, the watermark
can be used, such as comments within code. But by definition, it
will have a negligible effect on the actual code produced.
Translation:
We value precision in programming code; we do not in prose.
And it is exceedingly rich to cite George Orwell’s
Nineteen Eighty-Four
, approvingly, in the context of justifying a text adulteration scheme premised on the notion that specific words do not matter. I mean what the actual fuck? Orwell!
Lastly, as to why they’re doing this:
We’re implementing watermarking to comply with the EU AI Act.
Anthropic, along with several other major AI model providers and
around
190 total signatories
, signed the EU Code of
Practice on Transparency of AI-Generated Content in July 2026.
This requires AI system providers to use methods of “marking”
AI-generated text. We’re applying watermarking globally at launch
because we don’t yet have a durable way to scope it by region.
This, from a company that
the Financial Times just reported
is weeks away from an IPO with an intended valuation of $2 trillion, which would make it one of the 10 highest-valued companies in the world —
as of today
, placing it at #7, between TSMC ($2.2T) and Broadcom ($1.9T).
This leaves us to believe that one of the following must be true:
It’s perfectly reasonable that a technology company valued on par with Amazon and TSMC is technically incapable of complying with an EU regional law only within the EU itself.
1
Not a cause for concern at all.
Anthropic is in over their heads, wields shockingly little control over their own tech stack, and their imminent IPO is likely to be remembered only as a new high-water mark in the manic global AI bubble.
Also, what happens if another major global market makes it
unlawful
for AI to secretly watermark generated text?
OpenAI
From an OpenAI support document titled “
Provenance Signals (Content Credentials, SynthID) in OpenAI-Generated Content
”:
Consistent with our
commitments
under the European
Commission’s Code of Practice on Transparency of AI-generated
content, our goal is to expand provenance signals to all
modalities including text, so customers and developers have
clear ways to meet their own transparency obligations as
standards and tooling continue to mature.
There’s a lot of wiggle room in this brief statement, and it could just as well mean that OpenAI models will only adulterate text with fingerprint markers when users or developers ask for it. Or that it will only be mandatory for users in the EU. If I were at OpenAI I’d go hard on this and publicly say that ChatGPT will never watermark text it generates
unless you ask it to
, and that if you want tools that secretly work behind your back without telling you how they work to flag your words in ways you can’t see, go ahead and use Claude.
Further Reading
Three papers on ArXiv:
I will admit that while I’m profoundly offended by the idea of personally using tools that attempt to leave such watermarks in text they produce or touch, the mathematics behind it are fascinating.
Michael Lopp, at Rands in Repose, “
RIP Claude
”:
As a human who has had to wrangle with EU regulations in the past,
I am abundantly clear what’s involved in the laborious
bureaucratic process. I can guess what threats Anthropic is
facing. However, this is a tone-deaf, clumsy, and alarming opening
salvo in their watermark strategy. [...]
My writing is my work, and Anthropic’s current strategy is
aggressively writer-hostile.
Jeff Gamet, “
Anthropic’s Claude Watermark Is Akin to an AI Poison Pill
”:
To be clear, the watermarking is embedded in pretty much any text
Claude touches. Along with text Claude generates, it also applies
to text it processes, such as proofreading and summarizing. I
expect we’ll see too many inaccurate accusations of using Claude
to write documents where the content was human-written, but
AI-proofread.
The watermarking sticks with documents through copy-and-paste,
too. Imagine copying text from a blog post or email only to have
what you wrote tagged as potentially AI-generated. In fact, that
could very well happen with this post. I personally write all of
my content without AI tools, but I copied the quote at the top of
this piece directly from Anthropic’s website. Does that mean what
I wrote here will show as AI-generated? If they used their own
models to generate or edit what I quoted, then the answer is very
likely “yes.”
One of the papers published at ArXiv I cited above
claims that such watermarking even persists
when an article of text originally generated in English is translated into German.
Secrets are the poison here. When only Anthropic holds the secret keys that both produce the watermarking
and
perform the probabilistic detection of those marks, we’re all left to wonder. To wonder if what we’re reading is secretly watermarked, what we’re
quoting
is secretly watermarked, and whether what we ourselves are writing will be unjustly accused of being AI-generated based on secrets we don’t know and can’t see.
Poisonous
is exactly the right word.
Or should I say
toxic
? Or
airplanes
?
