---
title: "Follow-Up Thoughts on Watermarking Schemes for AI-Generated Text"
url: "https://daringfireball.net/2026/08/follow-up_thoughts_on_watermarking"
fetched_at: 2026-08-18T10:03:44.285949+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Follow-Up Thoughts on Watermarking Schemes for AI-Generated Text

Source: https://daringfireball.net/2026/08/follow-up_thoughts_on_watermarking

Follow-Up Thoughts on Watermarking Schemes for AI-Generated Text
Monday, 17 August 2026
Some follow-up to this weekend’s stemwinder “
Anthropic’s ‘Watermark’ Text Adulteration in Claude Is a Perversion of Writing
”:
Temperature
Contra a bunch of idiots
at Hacker News
and elsewhere, I understand that popular LLMs do not just pick the “best” token (word) at each decision point. Counterintuitively, always selecting the highest-probability option produces undesirable results. So the models apply some randomization, and “temperature” is the term for the weighting that’s applied so that the “better” (higher-ranked by the model) choices have a higher chance of being chosen.
With a temperature of 1, models use their built-in probability distribution. With a temperature greater than 1, this distribution gets flatter — less-likely alternatives get a higher probability of being selected, and more-likely alternatives lower. With a temperature lower than 1, the probability distribution leans more toward the higher-ranked options. And with a temperature of 0, the highest-ranked option is always chosen. A temperature of 0 generally produces undesirable results — too predictable, too likely to get stuck. Like over-smoothing an image from a camera sensor, eliminating all noise makes the overall result worse, even if each single bit of “noise”, evaluated in isolation, is in some sense wrong.
The temperature-based randomness — which is what makes LLM output non-deterministic — is in place to help make the output
better
. The prose is clearly better with a temperature of 1 (with weighted randomness) than at temperature 0 (with no randomness). The watermarking schemes, on the other hand, are applying predictable-with-the-secret-key randomness for an entirely different purpose than improving the quality of the output, and thus, I believe, inherently make the output at least slightly worse.
Advocates of LLM watermarking schemes for text argue that the schemes don’t necessarily lower the quality of the generated prose, because they don’t change the temperatures — they only change the source of the randomness.
Daniel Jalkut wrote a good piece today about this
. I hope that’s true. I believe it’s possible that it is true. I think it’s highly unlikely that it is true. I do not see how a detectable signal can be added  encoded in the choice of words
without affecting the meaning of the prose
. If it
were
true I think they’d show examples proving that it’s true. Also,
Anthropic itself admits that it can’t properly watermark text that is programming language code
:
For the same reason, code — which in very many cases has to be
exact — has generally less watermarking than some other forms
of text.
Having said that, in areas where there is an arbitrary choice
between particular words or terms within the code, the watermark
can be used, such as comments within code. But by definition, it
will have a negligible effect on the actual code produced.
I hold that good prose is much more like programming code. Exactness in word choice, phrasing, tone, and even punctuation is always better than imprecision. The difference is that sloppy programming code doesn’t run, or doesn’t run correctly. The human brain, on the other hand, is adept at parsing and making sense out of inexact, even sloppy, prose.
I Object Even If Quality Isn’t Adversely Affected
I do not believe these schemes can work without degrading prose quality, if only slightly. Again, though, I am open to being proven wrong. But even if we concede for the moment that such watermarking schemes do not necessarily degrade the quality of generated prose — not one iota — I still object to their use when they are being applied secretly, behind users’ backs. A useful watermark would be one that
anyone
can check. These SynthID “watermarks” are entirely dependent upon secrets held by the LLM providers (so far, Anthropic/Claude and Google/Gemini). I find that unacceptable, for reasons I hopefully made clear
in my essay
.
The people in favor of this watermarking for text have been sold a pipe dream, a fantasy. I’ve encountered dozens of comments from angry AI haters (many of them on Bluesky in particular, but also Threads and Hacker News) who are convinced that the only people who could be against the watermarking of AI-generated text are those who are duplicitously passing off AI-generated text as their own writing — and thus that I must be upset only because the jig will soon be up for me too. This of course is not true. I don’t even use AI to write text messages or emails for me, let alone a single sentence of my work.
But I find it funny that so many people who claim to believe that LLMs only produce “slop” and never anything useful also seem 100 percent convinced that the same LLMs are capable of watermarking their output in reliable ways. These people so desperately want to be able to point a finger at AI-generated text that they’ve fallen hook, line, and sinker for the argument from Google and Anthropic that, thanks to them, they’ll be able to.
I don’t want to spend too much time thinking about this because it’s a waste of time, but how exactly do these people think the existence of these mandatory watermarks and detection tools will change anything for the better? Let’s say you work at an office and you suspect that numerous of your colleagues are using AI to write emails and other work-related messages. Their messages are too long, too prolific, and lack lucidity. What are you going to do now? Copy and paste each of their messages into the watermark detectors from Anthropic, Google, and OpenAI? There cannot exist a single detector for all LLMs. And even if you find out that it says it’s a match, that an email or blog post or Slack message was very likely generated by, say, Claude, what are you going to do? March into your colleague’s office and tell them you caught them?
Anyone in a situation where “getting caught” would matter — students, say — is going to use non-watermarking LLMs or run their watermarked text through paraphrasing tools like
Declaude
.
No practical good is going to come of this, even if these watermarking schemes work as promised (and to be clear, I don’t believe any of it is going to work as promised).
1
My advice is not to care whether anything was written by an AI or a human. The only thing worth evaluating is what we human readers are naturally good at determining: whether it is good or bad. If it’s good, read it. If it’s not, don’t. If you’ve got a job where you’re surrounded by colleagues filling your inbox with AI-generated messages that you can’t abide, get a new job or learn to live with it. Hidden secret watermarking signals — even if they work — aren’t going to make things go back to the way they used to be. If you read something and enjoy it, and subsequently find out it was generated by an LLM, don’t feel bad. You read something good that you enjoyed.
I read something earlier today that claimed most of the posts on LinkedIn are generated by AI. That the whole platform is just inundated with AI slop. Maybe it is, but I wouldn’t know, because I never look at LinkedIn because it’s always been filled with crap. If it smells like crap it’s crap, whether the turds came out of a human anus or a turd-generating robot.
The Argument That Only People Can Truly Write
Dan Moren, writing at Six Colors today, “
LLMs Aren’t Writing
”:
LLMs do not care about the words that they pick because they
cannot care about anything.
Speaking of two things that are not the same, John rightly points
out the difference between the phrases “he leaped at the chance”
and “he jumped at the opportunity”. Those are indeed distinct — if semantically similar — phrases, each of which might be more
apt in a particular situation; or, to put it in another fashion:
the use of each of those phrases tells us something different,
whether about the person being described or the writer.
But the LLM doesn’t know which of those phrases is the
right
phrase to use. It has a guess, based on its models and weights and
inputs. But the ultimate choice of those phrases tells us nothing
about the writer because there is no writer.
Moren’s is a fine retort to my post, but I fundamentally disagree — albeit at a philosophical level. If you’re reading a written work only to gain insight into the mind that produced it, there is no mind on the other end of AI-generated text. But the work itself exists. My disagreement with Moren starts and effectively ends with his (wonderfully summative) headline. I say if you can read something, it was necessarily written.
Again, this is philosophical. Was a photorealistic image generated by AI
photographed
? No, I would say it was not. Photography, I would say, is the act of focusing light through a lens onto a capturing sensor, capturing, to some extent, reality. I think Moren is arguing that
writing
is like that. If photography captures a physical scene from reality, writing captures thoughts from an actual mind. That something you can read that was produced by an LLM was merely
generated
in a way that doesn’t qualify as
writing
. Semantics. I just care about the article of text. Moren argues that LLMs are not writing; I say they are. But we’re disagreeing only over what the word
writing
means, not what is being produced.
As for “caring” about the difference between semantically similar but tonally different phrases, like “
he leaped at the chance
” versus “
he jumped at the opportunity
”, no, of course the LLM doesn’t “care”. But I, the reader, care very much.
I wrote a column back in November
on ChatGPT changing (and renaming) the “personalities” it allows users to choose from. These personalities generate text with strikingly different styles and tones. Because I use ChatGPT, I care very much about the tone and style of its responses to my queries. Not because I’m ever going to pass them off as my own writing, but because I’m the one who is reading them.
Moren, near the end of his column:
In the end, I can’t summarize it any better than to ask: if you
care so much about word choice,
why are you using AI to
generate text
?
If this does truly make AI-generated text worse, well…
good
. A
lot of people are already willing to accept what an LLM churns out
as “good enough” and, if I’m being realistic, I don’t think this
will change anything. But if it does lead to more people being
dissatisfied with the pablum they’re being fed and turning instead
to writing and editing their own text, then that would actually be
a positive outcome. Maybe it’d even mean fewer human writers being
put out of jobs.
I sympathize, but I must disagree that it can possibly be seen as a net good for LLMs to produce
worse
prose. I read the output of LLMs every day. I use AI to generate text because I ask it questions (in text). I want the answers that I read to be cogent, lucid, accurate, blessedly terse — and ideally to strike a consistent tone that is pleasant to my reading ear. The genie is not going back in the bottle.
English Is the Finest Language, and Thus, Perhaps, More Fingerprintable
Lastly, here’s an interesting point to ponder. English is the most expressive language in the world. Don’t take my word for it — it’s the only language I speak (despite four years of Spanish in high school). Take the word of famed 20th century author Jorge Luis Borges, an Argentine polyglot whose first language was Spanish. In 1977 he was the guest on William F. Buckley’s “Firing Line”. You can (and should)
watch the interview on YouTube
, but here’s
a transcript of the relevant portion from Jordan M. Poss
:
Borges:
I have done most of my reading in English. I find
English a far finer language than Spanish.
Buckley:
Why?
Borges:
Well, many reasons. Firstly, English is both a
Germanic and a Latin language. Those two registers — for any idea
you take, you have two words. Those words will not mean exactly
the same. For example if I say “regal” that is not exactly the
same thing as saying “kingly.” Or if I say “fraternal” that is not
the same as saying “brotherly.” Or “dark” and “obscure.” Those
words are different. It would make all the difference — speaking
for example — the Holy Spirit, it would make all the difference
in the world in a poem if I wrote about the Holy Spirit or I wrote
the Holy Ghost, since “ghost” is a fine, dark Saxon word, but
“spirit” is a light Latin word. Then there is another reason. The
reason is that I think that, of all languages, English is the most
physical of all languages.
Buckley:
The most what?
Borges:
Physical. You can, for example, say “He loomed over.”
You can’t very well say that in Spanish.
Buckley:
“
Asomó
?”
Borges:
Well, no, no, they’re not exactly the same. And then
you have, in English, you can do almost anything with verbs and
prepositions. For example, to “laugh off,” to “dream away.” Those
things can’t be said in Spanish. To “live down” something, to
“live up to” something — you can’t say those things in Spanish.
They can’t be said. Or really in any Romance language.
I’ve seen this interview before, but watched it again today after an email exchange with
Kirk McElhearn
. Quoting (with permission) from McElhearn’s email to me:
For many years, I worked as a French → English translator, and
there is one key difference between the two languages. France is a
Romance language, and English is a language with both Germanic and
Romance (mainly French) influence. This means that English often
has synonyms where other languages may not.
Using your example, “He leaped at the chance” and “He jumped at
the opportunity”, both would be translated in French as “Il a
sauté sur l’occasion.” Meaning that someone writing in French
wouldn’t have the same range of words to choose from. It’s maybe
not the best example, because both are clichés, but there are many
examples of French words where English has both a Romance
equivalent and a Germanic equivalent: pig and pork, sheep and
mutton, beef and cow. Food words are just one example, but English
also has many more verb choices than French, since it has a larger
vocabulary coming from both influences.
English gleefully borrows from any and all other languages. McElhearn wonders whether English is thus more fingerprintable than other languages, because of its richer vocabulary of
roughly
equivalent synonyms, and its multitude of idioms.
