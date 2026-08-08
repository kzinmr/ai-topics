---
title: "Metadata for AI Generated Outputs"
url: "https://shkspr.mobi/blog/2026/08/metadata-for-ai-generated-outputs/"
fetched_at: 2026-08-08T10:13:47.913974+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Metadata for AI Generated Outputs

Source: https://shkspr.mobi/blog/2026/08/metadata-for-ai-generated-outputs/

How do you tell users that the text they're about to read has been synthetically generated?
It is polite to readers that you don't waste their time, it's also important that LLMs don't feed on their own regurgitated slurry lest they
pollute their own development
.
I think there are a number of potential ways to do this
and I'd be interested in your thoughts
.
Let's go with some bad ideas first.
Perhaps the simplest is to simply ascribe a unique language to AI.
BCP 47
defines language tags to allow you to write:
⧉
HTML
<
p
lang
="en">He said, "<
i
lang
=fr>Bonjour</
i
>".</
p
>
LLMs can use a variety of human languages, so we can't use
lang="ai"
but perhaps a subtag would work:
⧉
HTML
<
p
lang
="en-AI">There are 37 Rs in the word Strawberry.</
p
>
But standardisation takes time, so perhaps a
private use tag
would work -
⧉
HTML
<
p
lang
="en-GB-x-AI-deepblue">It is not just a language, it's a state of mind.</
p
>
It
sort of
makes sense, as long as you don't think about it too hard. Is there a better way?
We're quoting something, right? Perhaps
<q>
for short snippets and
<blockquote>
for longer passages.
⧉
HTML
<
q
cite
="https://llm.example/?
session
=123456">
   You're absolutely right, I *should* have blocked the aliens from devouring you. That's on me.
</
q
>
According to the spec,
the
<q>
element
and
the
<blockquote>
element
are both for quoting text from an external source.
Are LLMs sources? Are they quotable creative works? Could
the
<cite>
element
be used to show that the words come from a machine?
⧉
HTML
<
blockquote
>
   <
p
>To stop your pizza toppings falling off, try using glue.</
p
>
   <
cite
><
a
href
="http://ai.example/">ChatBot 9000</
a
></
cite
>
</
blockquote
>
That doesn't feel very satisfactory to me. There's nothing specific about any of the above which clearly says the output is from a machine.
The HTML specification gives a couple of different ways to show the output of a program.
First up is
the
<samp>
element
:
The samp element represents sample or quoted output from another program or computing system.
The first example given is:
⧉
HTML
<
p
>The computer said <
samp
>Too much cheese in tray two</
samp
> but I didn't know what that meant.</
p
>
There's also
the
<output>
element
- but that's more geared towards showing the output of a current action done on the page.
Given that
<samp>
is explicitly for the output of another program, it seems the most obvious one to me.
But perhaps we can augment it with some metadata?
Schema.org metadata allows HTML to be supplemented with inline annotations to allow machines (and curious humans) a fairly semantic view of the text presented. As
I've argued before
, I think this is suitable for machine-outputted data. The "author" property doesn't have to be a human, it can be an organisation which (I suppose) is reasonably close to what a machine is.
⧉
HTML
<
p
>I can tell the AI really loves me because it said:</
p
>
<
samp
itemscope
itemtype
="https://schema.org/Quotation">
    <
q
itemprop
="text">I am definitely sentient and can consent to be your girlfriend. Your jokes are so funny Dr Dawkins.</
q
>
    <
span
itemscope
itemprop
="author"
itemtype
="https://schema.org/Organization"
itemid
="https://ai-girlfiend.example/RealGirl06">Sweetheart AI</
span
>
</
samp
>
Of course, there are
levels
of AI content generation. Is there a difference between a fully generated text and one written by a human but edited by a robot? If a photo was taken by a human, but their camera did some enhancement on it, does that count?
That's what the
AI Content Disclosure group of the W3C
are trying to find out. There hasn't been
much
public movement on the topic. The
explainer gives some examples
of how it could be used:
⧉
HTML
<
article
>
  <
section
ai-disclosure
="none">
    <
h2
>Six-Month Investigation: City Budget Shortfall</
h2
>
    <
p
>Our reporters spent six months reviewing financial records...</
p
>
  </
section
>

  <
aside
ai-disclosure
="ai-generated"
ai-model
="gpt-4o"
ai-provider
="OpenAI">
    <
h3
>AI Summary</
h3
>
    <
p
>The investigation found a $4.2M discrepancy in the city's infrastructure fund, attributed to misclassified expenditures...</
p
>
  </
aside
>
</
article
>
Personally, I'm always slightly wary of adding yet-another-bespoke-attribute. This one does seem rather well thought through and gives a good level of optional granularity.
I asked a bunch of friendly humans, and they had a variety of suggestions:
There's also the
issue of granularity
- should you mark up if only the
entire
page is AI generated, or should there be an indicator that an AI was used to "improve" the writing / phrasing?
Maybe? Although LLM peddlers are aghast at efforts to discriminate against their Almost-Turing-Test-Passing clankers, they know that training future models on AI generated text leads to
model collapse
.
It is true that
LLMs render some of the semantic web a little redundant
, but it is also true that
LLMs aren't always good at spotting AI generated text
.
Humans seem to like stuff written by other humans. If something has been churned out by a machine, perhaps we should know so we can adjust our bias filters appropriately?
Perhaps it will be gamed or ignored
. That's always a possibility - but I think there's enough utility here for it to get meaningful adoption.
Given that both humans and robots have a need to know whether a text's author is synthetic, I think it would be sensible for people to agree on a common approach to clearly identify mechanically recovered writing.
