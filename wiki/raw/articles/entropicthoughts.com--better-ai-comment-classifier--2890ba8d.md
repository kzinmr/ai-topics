---
title: "Better AI code comment detector"
url: "https://entropicthoughts.com/better-ai-comment-classifier"
fetched_at: 2026-09-10T10:01:27.638311+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Better AI code comment detector

Source: https://entropicthoughts.com/better-ai-comment-classifier

When I trained
the previous
ai
comment classifier
, I used partially personal
private data to do it, and built it on a somewhat shaky foundation, so I
couldn’t share the code or data. I rebuilt it on public data and a better
foundation!
First off,
you might want to try it out
. Nothing you paste into that web page
leaves your browser, so you can safely try it with whatever you like. I have
invited some testers to try out an earlier version of it, and they had mainly
positive feedback to give.
We won’t break down robot-isms the way we broke down Claude-isms in the previous
article, because in the
ui
of the new classifier you can just click any part
of the text being classified to see which features activate on that portion of
the text, and how they contribute to the overall judgment. Here’s an example of
the expanded feature activation view.
In terms of performance, the headline number is the balanced accuracy of 77 %.
This is how often the classifier gets the human vs. robot verdict right,
assuming human-written and robot-generated comments are equally likely.
The classifier also prints a predicted percentage which is calibrated, meaning
it can be read as the probability that any specific verdict is correct. We test
this through the calibration curve, which shows what probability the classifier
assigns to an event with a known probability.
Since all dots lie very close to the reference diagonal, we know they are
approximately correct. This holds true across comments of multiple lengths,
where a fitted
temperature
parameter adjusts for increased confidence as the
amount of data increases.
We can get more details about the classifier’s failure modes by looking at its
confusion matrix. In this table, “robot” is considered the positive class, i.e.
the thing we want to detect. The abbreviations stand for true/false
positive/negative rate.
verdict: human
verdict: robot
input: human
tnr
= 0.73
fpr
= 0.27
input: robot
fnr
= 0.20
tpr
= 0.80
When presented with a known-human input, the classifier correctly judges it as
human 73 % of the time. With a known-robot input, it is correctly judged 80 % of
the time. This means in both cases (known-human and known-robot) the mistake
rate is around 25 %. That might sound high!
But remember that this mistake rate is the
aggregate
over
all possible
inputs
. We don’t need to pay too much attention to it, because the classifier
outputs a calibrated predictive percentage every time it classifies something.
Thus, for individual judgments, we
know
when the risk of false positives is
lower or higher. When the classifier is very confident – e.g. when the confidence is
80 % or more – the risk of a false positive drops to 5 %. When the classifier is
uncertain – when confidence is around 50 % – then by calibration it will issue
the wrong verdict around half the time.
I mention the numbers in this confusion matrix only because they are so often
used when discussing classifiers, so more academically inclined readers may
expect to see it. Here are some other requested numbers:
Accuracy
77 %
Precision
75 %
Recall
80 %
Sensitivity
80 %
Specificity
73 %
F1 score
77 %
The accuracy, precision, and F1 score depend on the base rate, but here they are
computed from an ignorance assumption, i.e. an equal mix of human-written and
robot-generated comments.
All of these numbers come from cross-validation. I have also manually tested a
smaller non-synthetic set of real-world comments from humans and robots to see
how well the classifier generalises slightly out of sample.
verdict: human
verdict: robot
input: human
tnr
= 0.89
fpr
= 0.11
input: robot
fnr
= 0.14
tpr
= 0.86
This translates to the following performance numbers:
Accuracy
88 %
Precision
89 %
Recall
86 %
Sensitivity
86 %
Specificity
89 %
F1 score
87 %
This is very good! It looks like non-synthetic, more real-worldy cases are
easier for the classifier to discriminate between than the training data.
Of course, all of this is tested with code comments only. The classifier is not built
to detect robot-generated texts of other kinds. It can do it, but I make no
promises of its accuracy.
With that out of the way, let’s talk about how it’s made.
The first step, as before, is to build a good data set. Ideally, we’d plan this
meticulously and do it right the first time. If we do that, it should cost us
about $30 to get the dataset that powers this classifier. It contains enough
data to reach diminishing returns in discriminating between the more similar
models.
1
It is possible to extract a more powerful classifier with more data, but
it would start to be very expensive since classifier power appears to scale with the
log of money spent.
That is,
if
you plan it out and do it right the first time. I
didn’t do that. I discovered much later, when evaluating features, that the data
I had was junk and I had to collect it all over
2
💸
. Then after a while I
discovered
again
that the data was still junk and had to be recollected
again
3
💸💸💸
.
The general idea was to find a set of permissively licenced or copy-left
repositories, check out their latest commit
from the year 2021
, and then
take a few random files from that commit. These contain human comments. Then we
strip out all comments from those files, and have
llm
s generate new comments
for the same files. That provides us with robot comments. As long as we try to
keep the number tokens for each file balanced between all classes (humans and
llm
models), we can avoid subject matter leakage, where the classifier learns
to distinguish files or repositories rather than the style of the text itself.
The general idea is simple! But the devil’s where the devil usually is.
Here are some mistakes I made, in no particular order:
Accidentally picking different source files for each
llm
to generate
comments for. This causes subject matter leakage.
Generating
llm
comments for files with very few human comments. This also
causes subject matter leakage over the human–robot barrier.
Failing to strip out docstrings when blinding
llm
s to human comments in
source files. This causes
llm
s to generate comments more similar to humans
because they try to match the existing repository style. Though it should be
said this had a smaller effect than I thought it would.
Related to the above, some languages support many different syntaxes for
comments, and some are used more often than others. Failure to detect
existing comments in all syntaxes leaves comments behind to contaminate
llm
generation, and also makes it hard to get all the data that has been produced.
Not filtering out human comments that are very short. Most human comments only
say things like “main task structure” or “chIcon” or “Alias” and including
those teaches the classifier that humans write like shit. Since
llm
s were
instructed to write more detailed comments, it seems reasonable to compare
those to more detailed human comments too.
Using a fixed prompt for generating
llm
comments. This results in a dataset
with narrower variation than desirable for learning all the quirks needed to
separate models and humans.
Not all of these problems required regenerating data from scratch. Some could be
worked around by filtering and preprocessing the data that already existed.
Either way, this was the least fun part of the project, and it cost
significantly more than the theoretical $30.
After collecting data, we need to design a classifier that works on that data.
This means evaluating candidate features. Doing so isn’t expensive in money, but
in
cpu
time. Evaluating features, in the most powerful sense, means training
the classifier on all subsets of candidate features and seeing which performs
best. That’s unreasonable, as even with only 15 candidate features, it requires
training over 30,000 different classifiers, which need to be trained five ways
each for cross-validation to boot.
What I ended up doing was guiding the feature selection by the accuracy of
classifiers as trained on individual features, for different discrimination tasks. In
other words, I had a script that checked “does character frequencies
discriminate better between robots and humans than word lengths?” and then
repeated that for comparisons between different features, and different
classes.
4
Different classes means the question is asked not just for
robots-vs.-humans but also Claude-vs.-Grok, and GPT-vs.-Gemini, etc.
Each of the class pair comparisons produced a list of feature rankings. These
lists mostly agreed on the order of features, but there were some disagreements.
The ranking of features by power, and the strength of disagreement around
relative rankings, is rendered in the graph below.
I think the graph reads quite intuitively, but just to be sure:
A black arrow means all comparisons agreed on the relative strength of the two
features connected with the arrow.
5
I suppose technically it means that if
a comparison didn’t agree, at least it didn’t disagree. In other words, if
four comparisons indicate that feature A and B have roughly the same power,
but a fifth comparison indicates feature A is better than feature B, then the
graph will show a black arrow from B to A despite the lukewarm response from
four out of five comparisons.
A blue arrow means at least two comparisons agreed on the relative strength of
the two features connected with the arrow, and only one comparison disagreed.
A red arrow means more disagreement (and the exact numbers are shown in the
arrow label), but the arrow still points in the direction of the dominant
opinion.
Each feature box also has an information quantity expressed in bits. That shows
how much that feature helps, on average, in distinguishing between two classes.
Not only is this graph extremely fun to look at – it is also very informative!
The feature names may be nonsensical, so we’ll have a brief description of each.
As the running example, I will use the following excerpt from a Donald Trump
speech:
markets are at their highest point in many years but we can actually say of all time
and a similar random excerpt from an article in the Economist:
the
oecd
member countries that have taken part in every edition of
pisa
reached a peak around
Here are the features:
bigwords
: the fraction of words longer than 5 letters in the comment.
Classic stylistic marker for fancy language, but very weak for discrimination
other than in obvious cases.
The Trump snippet has a
bigwords
value of 18 %, whereas the Economist
article is at 29 %.
wordlen
: replace each word with a number indicating how long that word is,
then count frequencies. This is similar to
bigwords
but captures the full
distribution.
Trump has 30 % words of three letters, 24 % words of two letters, 15 % each of
words of 4–7 letters, and 6 % words longer than that. The Economist has a
wider spread, with the most common length (35 %) being four letters, then very
equal fractions in the span 2–7 letters, and 5 % each for nine letters and a
single letter.
freqrank
: replace each word with a digit based on how common that word is.
The most common word gets the number 0, the ten most common words after that
get the number 1, the hundred most common words after that get the number 2,
etc. Then count the frequencies of these numbers.
Trump uses mostly rank-2 and rank-3 words at frequencies of 50 % and 30 %
respectively. This corresponds to the top-100 and top-1000 most common words.
The Economist snippet contains very few rank-2 words (though more rank-1
words!) and pulls in plenty of rank-3 and rank-4 words, again indicating more
complex vocabulary than Trump.
wordfreq
: count the frequency of a small set of
function words
. It sees
how many times a text includes content-less words like “the”, “in”, “many”,
“all”, etc.
The Trump example never repeats any function words, but this feature would
anyway report single occurrences of words “are”, “at”, “their”, “in”, “many”,
“but”, “we”, “can”, “of”, “all”. The Economist article has a different set:
“the”, “that”, “have”, “part”, “in”, “every”, “of”, “a”, “around”. With these
short snippets, this doesn’t tell us much, but with more data it can start to
distinguish sources of text.
word2gram
: counts bigrams of function words with other words filtered out.
This produces strange bigrams that were never in the original text, but it
remains a popular way to analyse how people write.
The Trump example would have, among other bigrams, “are at”, “at their”,
“their in”, “in many”, “many but”, etc. The Economist would have “the that”,
“that have”, “have part”, “part in”, etc.
word2gram_adj
: counts bigrams of function words only when they are actually
found next to each other in the text, i.e. not with other words filtered out.
This
seems
like a more natural way to analyse writing because it only results
in bigrams that actually existed in the original text, but as we can tell from
the graph, it is a weaker indicator than the regular
word2gram
.
The Trump example would have “are at”, “at their”, but then a jump to “in
many”, then another jump to “but we”, “we can”, etc. The Economist reduces to “that
have”, “part in”, and “in every”. We see that the Economist has fewer strings
of function words.
word3gram
and
word3gram_adj
is like the previous two except for trigrams.
The Trump example has two values for
word3gram_adj
, namely “are at their”
and “but we can”. The Economist has only one: “part in every”.
charfreq
: count the frequency of each character in the comment. This can be
a strong signal if sources have different tendencies to use symbols.
Since both Trump and the Economist use English and the fragments I selected
have an equal number of words, their character frequencies are actually very
similar.
char2gram
and
char3gram
: count the frequencies of bigrams and trigrams of
characters in the comment. This starts to tell us something about styles of
punctuation and word choice.
Since neither Trump nor the Economist used any punctuation in these snippets,
we can only look at letter frequencies, and in these examples, we can tell
Trump starts words with the letter “a” more often than the Economist, based on
the bigram
space-followed-by-a
. In contrast, the Economist ends words with the
letter “n” more often than Trump.
wordfreq_raw
: Count frequencies of words, but not limited to function words.
The benefit of this is that if there are some words strongly preferred by a
source
6
And they haven’t heeded their editor’s device to kill their
darlings.
like “mediated” that wouldn’t be in any function word list, but
with raw word frequencies the classifier can learn to distinguish on that word
anyway.
However, this is also a dangerous feature because it can train the classifier
to pick up on subject matter differences. For example, in the Economist case
it could learn that if the text contains the abbreviation “
oecd
”, it is from
the Economist, but if it contains the word “actually” it is from Donald
Trump.
7
Okay, that might not be a bad rule, but you can see how it could
lead to unintentional consequences in other cases!
Recall, however, that we took pains to construct a balanced dataset for the
code comment classifier. This is where that pays off. There is very little
subject matter leakage in the raw word frequency feature, and instead it does
pick up on actual stylistic quirks.
word2gram_raw
,
word3gram_raw
: take the frequencies of bigrams and trigrams
of words, with no filtering for function words.
wink
,
upos
,
ptb
: convert each word to a
part-of-speech
(
pos
) tag
indicating its grammatical role, and then count the frequencies of those
pos
tags. The reason this is a strong signal is that it captures the way different
sources phrase themselves, without getting distracted by choices of words.
The three variants of this feature use different engines for
pos
tagging
8
Some engines are more accurate than others.
, but they all produce
roughly the same result. The benefit of the
wink-nlp
engine is that – even
though it’s weaker than the other two in the graph – it runs in the browser.
The
pos
tag replacement turns the Trump speech into something like the
sequence
NNS VBP IN PRP$ JJS NN IN JJ NNS CC PRP MD RB VB IN DT NN
. This
sequence contains more plural nouns (
NNS
) than the Economist, which on the
other hand contains more proper nouns (
NNP
) and determiners (
DT
).
wink2gram
,
upos2gram
,
ptb2gram
,
wink3gram
,
upos3gram
,
ptb3gram
are
bigram and trigram variants of the above.
When evaluating classifiers with a single feature at a time, which is what the graph
above represents, we can see that
pos
tag n-grams are very powerful regardless
of which tagging engine is used. Character n-grams are also powerful, and raw
word frequencies are not so bad either.
But single features are only half the story, because when we train classifiers
on multiple features, the features interact. Interaction makes some features
redundant, but it can also make combinations of features stronger than they were
individually! I started with the set of top-scoring single features, and
systematically evaluated combinations of features by adding and removing
individual features to see how they influenced each other, but eventually I got
tired of that exercise and picked a set of features for the production
classifier rather arbitrarily.
9
I also had a few subcommands to the training
script that let me explore features and how their associated frequencies varied
among the classes to be dicriminated.
The classifier is trained to classify seven ways. Given a single comment, it
tries to discriminate between the following seven sources:
Humans
GPT 5.6
Gemini 3.7
Claude 5
Kimi K2.7
Grok 4.6
GLM 5.2
After a while, something seemed odd, though. It almost always predicted either
Kimi K2.7 or
glm
as one of the most likely
llm
models. Some plotting of
centroids of feature vectors later, it was clear that both of these models have
styles that overlap all the other models
10
I don’t know how distillation works
but it sounds like it could be a relevant term.
so the classifier’s judgment is
partially smeared out over those two models rather than assigned to the actual
source. Instead of retraining the classifier without those models, I take any
probability mass assigned to those models during classification time and smear
it back over the rest of the models in proportion to how much mass it sucked from
them during training. This means Kimi K2.7 donates probability mainly to Grok
and Claude, and
glm
roughly evenly to all other models.
I also realised when I started using the classifier that what I really wanted to
know was whether a comment was human-written or robot-generated; rarely is it
important to know which
llm
model may have generated the comment. So at the
classification stage the probability masses are re-normalised to emulate a 50/50
prior for human/robot rather than the 1/7 priors the classifier is trained for.
It might seem silly that we train a 7-way classifier, reduce it to a 5-way
classifier, and then simplify again to a 2-way classification. We could have
trained a 2-way classifier to begin with! But there are two benefits to doing it
the complicated way:
It makes it possible to show a cool
llm
model breakdown next to the main
prediction.
It might allow us to better capture the complex shape of the high-dimensional
surface that separates human writing from robot-generated text.
I haven’t actually run a formal benchmark on the reduced 7-way classifier
against a trained 2-way classifier, but I don’t think the difference in
performance would be that large, so consider the first point the real benefit.
One of the remaining problems is the same as in the previous article: with
L1-normalised features, the resulting probabilities of the logistic regression
become very small. A separate pass takes the trained model and calibrates a
temperature coefficient
k
which extremises predictions based on the square
root of the length of the input.
At first I built a
cli
interface for classification, but I rather quickly realised that
It would be easier for other people to play with if I ship it as a web page
with a classifier model bundled; and
It would be easier for
me
to diagnose and troubleshoot it if it had a
fancier diagnostics interface, and that would be easier in the browser.
I was worried about the size of the classifier model, which ran into several
megabytes in its raw form. Thus I ended up both quantising coefficients and
reducing the vocabulary of all features with a document frequency filter, i.e.
stripping out those feature values which only existed in a small subset of
comments. There was a knee in the precision curve around 0.05 %, meaning feature
values that only exist in fewer than that fraction of comments aren’t part of
the classifier. The model is now 355 kB.
The other change the web interface brought was that it required being able to
pos
tag input in the browser! This made the higher-performing Python-based
engines (
nltk
and
spaCy
) unavailable, and I was forced to use
wink-nlp
.
Hypothetically, there shouldn’t be an issue with training using one engine and
pre-processing classification input with another, but to avoid input being
out-of-sample for silly reasons, I opted to use
wink-nlp
in Python too, which
meant Python invoking a Node.js process and it’s not pretty.
But where’s the source code? You promised source code!
I genuinely had the intention of writing out the code for all of this myself. I
thought I’d use robots to generate experiments with models, features,
visualisations, etc., and then rewrite the final version on my own, to make sure
the code is high quality.
But I cannot be arsed. This is a side quest, not something I can spend much time
on. If you don’t want to read AI slop code, don’t read
the implementation
. Read
this description of how it’s done instead, and maybe you can make your own.
I also likely won’t continue to work on this because sourcehut’s newest
tos
,
going into effect for all changes submitted from tomorrow, forbids using it to
host
llm
-generated code. Enjoy this in the shape it is!
