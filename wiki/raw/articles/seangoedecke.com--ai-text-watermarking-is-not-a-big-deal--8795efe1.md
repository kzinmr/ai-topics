---
title: "AI text watermarking is not a big deal"
url: "https://seangoedecke.com/ai-text-watermarking-is-not-a-big-deal/"
fetched_at: 2026-08-16T10:14:41.752473+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# AI text watermarking is not a big deal

Source: https://seangoedecke.com/ai-text-watermarking-is-not-a-big-deal/

People are
pretty
unhappy
about Anthropic’s recent
announcement
that they’re planning to include a hidden watermark in Claude model outputs. Will this lead to a mass exodus from Anthropic models? Will the introduction of watermarking be a meaningful change for users?
No. AI text watermarking is not a big deal. It doesn’t make the text worse, it doesn’t make AI outputs more detectable in practice, it doesn’t violate user privacy, and everyone’s going to be doing it by 2027 regardless.
Watermarked text is not lower-quality
There is no meaningful difference in quality between watermarked and unwatermarked text.
I wrote about this more
here
, but the two popular ways to do it — Google’s
SynthID-Text
and Meta’s
TextSeal
— are completely transparent to the user. They work by replacing the pseudo-random logit sampler with a different pseudo-random logit sampler.
Suppose you were gambling on coin flips with your friends, and instead of flipping a coin you decided to do this:
Check the current time since midnight in seconds
Count that many words forward in the
Encyclopaedia Britannica
Count whether the word you land on has an even or odd number of letters
That would still be random enough to gamble with, right? But, like a watermark, you could theoretically go back and identify that that method was used, so long as you recorded the exact time of each “coin flip”. Text watermarking works the same way: it chooses a method of “randomness” that can be detected after-the-fact. Watermarked models will not be any less capable than unwatermarked models.
What about cases where the model is quoting something, or giving you the answer to a mathematical problem, or doing something else where the output is largely pre-determined? Wouldn’t enforcing a watermark there make the output worse? It would, which is why none of the AI labs are going to do that. Text watermarking approaches only replace the
existing
randomness in the logit sampler: in any case where the model is always going to pick the same tokens, there’s basically no randomness to play with, so there won’t be a detectable watermark in those tokens.
I think all this comes from a worry that you were previously getting the
best
token, but now you’re getting a lower-quality token that satisfies the watermark. For instance, Anthropic’s announcement suggested that the watermarking is visible in choices like the decision between “overcast” and “grey”. Many people have
predictably
come out
to say that decisions like these are really important to good writing, and that only an illiterate tech bro could think these words are identical.
This is a misunderstanding of Anthropic’s position and of how watermarking works. Specifically, it’s a misunderstanding because it suggests that the unwatermarked model would choose “overcast” while the watermarked one would choose “grey”. This is not how it works! If Claude Fable prefers “overcast” to “grey” in a particular context (say, 80% to 20%), you’ll get “grey” 20% of the time from both the watermarked and unwatermarked model.
Models already include a healthy amount of randomness in order to promote creativity.
Text watermarking just introduces a way to make those random choices that’s detectable after the fact.
AI outputs are already “watermarked”
The other big reason to not worry about AI watermarking is that
AI text content has always effectively been watermarked
. Most careful readers can tell when they’re reading
AI outputs
, because language models tend to gravitate towards certain
habits of language
: em-dashes, rhetorical opposition, punchy one-liners, “claudese”, and so on. In fact, it’s possible to train classifier models that reliably
distinguish
AI from human writing.
From what I can tell, some of the backlash to watermarking comes from
people
who buy AI inference in order to pass it off as their own work, and who worry that watermarking will make it harder for them to do that. For these people, the watermarking announcement is akin to Anthropic saying “hey, instead of making you seem smart, we’re going to publicly brand you as AI users and make you seem dumb”.
But of course this has always been the case! Nobody who is currently getting away with passing off AI outputs as their own will be caught by watermarking. For the majority of cases, it’s already painfully clear what’s happening for anyone who reads the
slop
. For sophisticated AI users who are avoiding the “house style”, any suspicious readers who would paste their stuff into Anthropic’s watermark detector could already have been pasting it into
Pangram
.
Tools like Pangram
only give you an estimate of the
chance
that output is AI-generated. Wouldn’t a watermark be a more solid confirmation? Not really. Text watermarks are probabilistic too, because any token chosen by SynthID could theoretically have been chosen by a human. I suppose the Anthropic watermark page could be considered more trustworthy than Pangram, because it comes right from the source, but it’s not impossible that in some cases Pangram might actually be
better
at identifying AI-generated text than the watermarking too.
AI text watermarking is not a violation of privacy
I’ve also seen theories floating around that watermarking encodes secret content into your outputs, or somehow tags outputs with your personal information.
I don’t think AI labs are using watermarks to encode data into your outputs.
Text watermarking is
hard
: like I just said, you can’t do it when the model can only respond with the same words, it doesn’t work for very short responses, and even on long responses it can only provide a probabilistic fingerprint. And that’s encoding one single bit
of information!
I’m not saying that encoding longer messages into a watermark is technically impossible — there are
papers
describing ways it might work — but there’s no way any of the labs are doing it
. If they wanted to associate you with your responses that badly, they’d just secretly store every model response they generated.
AI text watermarking is inevitable
Another reason to not get too angry at any individual AI lab for watermarking is that
every single AI lab is going to do text watermarking this year
. It won’t just be Anthropic. The alternative is to completely stop doing business in the EU, because of the
EU AI Act
. That’s currently a
sixty-billion-dollar
market. I am not a lawyer, but to me it seems genuinely unclear whether an AI lab could even legally do something like only watermarking EU responses: short of having an entirely different
claude-eu.ai
service, the plain text of the Act seems like it applies to any
service offered in the EU
, not just the content that service outputs to EU citizens specifically.
If people
really
hate watermarking enough, some labs might stand up a completely separate EU service, or make an aggressive interpretation of the EU AI Act and see how the legal battle goes. When I try to be maximally charitable to anti-watermarking histrionics, I adopt an interpretation like this: people are saying that watermarking is an invasion of privacy and makes outputs worse and so on not because they believe it, but because they’re trying to pressure AI labs to firewall EU AI regulations behind a completely separate interface. In this case, it probably doesn’t matter — text watermarking is not a big deal — but I can see an American consumer being worried about more aggressive future regulation, and wanting to draw a firm line in the sand as early as possible.
Here's a preview of a related post that shares tags with this one.
