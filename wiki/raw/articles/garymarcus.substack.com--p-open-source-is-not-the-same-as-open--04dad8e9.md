---
title: "Open-source is NOT the same as open-weight"
url: "https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open"
fetched_at: 2026-08-11T10:16:31.129366+00:00
source: "garymarcus.substack.com"
tags: [blog, raw]
---

# Open-source is NOT the same as open-weight

Source: https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open

Sad to see the  confuse open-source (fully transparent) with open-weight models (less transparent; no access eg to training data).

The new Meta model is open-weight but not open-source. NYT got it wrong.  

It is time for both the media and the public to learn this
1:26 PM · Aug 10, 2026
·
3.29K Views
9 Replies
·
4 Reposts
·
43 Likes
It’s no exaggeration to say that
open-source software
— in which the complete
source
code is available to anyone — has changed the world and accelerated software development.
But
open-source
and
open-weight
are
two very different things
, and too many people —this morning it was editors and writers at
The New York Times
among others—are failing to distinguish the two.
The essence of open-source is twofold: transparency and customizability. If you want to know how something works, you look at the code. You can change literally anything about that code (“forking” a new version of that code, for example, if you want to make a different version). All of this is fantastic for the community, and that is why open-
source
has been such a dynamic force. It’s called open-source because you release the
source
code of the final product. Open-
weight
doesn’t do that.
Open-weight piggybacks onto all the great press that open-source has but offers few of the advantages. Open-weight models are NOT fully customizable, and not transparent. They are the
product
of machine learning (the
weights
of a trained neural network), but not the whole thing, from soup to nuts. That means you can run them (or “posttrain” them), but, crucially, users can’t customize or improve them to remotely the same degree (more about that in a second), and outsiders can’t investigate them to nearly the same degree. You also can’t build community in the same way.
If pigeons are “just rats with better PR”, open-weights is open-source with all the good press but far fewer advantages.
Understanding all this requires a basic familiarity with the life cycle of a machine learning model. Let’s start with a simplified sketch I have snarfed (and modified) from
geeksforgeeks.org
.  The highlighting, which I will explain in a moment, is mine.
(Not shown is “
post training
”, in which people try to align and bend trained “base” models to their will. That’s all you can do with an open-weight model; I will give you examples of what you can’t do in a moment.)
When someone releases an open-weight model they are releasing the (highlighted) candidate model [also sometimes known as a base model]—which is the
output
of a complex process—
not
the full pipeline that generated that model.  You can adapt that candidate model, but you can’t rebuild it or investigate it to your liking, the way you could with a true open-source model, such as AllenAI’s
Olmo
or Nvidia’s
Nemotron
, which truly is what it says on the tin: “open weights, training data, and recipes.”
In contrast, when people release
open-weight
models, they are not revealing the
Full Monty
. They are
not
releasing the raw data; they are
not
revealing how they preprocessed that data; and they are
not
revealing the exact algorithms and parameters that they used in training. (For those who can stand yet one more loose metaphor, it’s like they are releasing a cake, but not the recipe; you can add icing on top, and maybe some fruit or hot fudge too, but you can’t change the raw ingredients that went into the cake itself.)
All this makes a world of difference, to developers who might use the systems, to regulators, to scientists, and ultimately to the world.
For developers, let’s say you have a hypothesis that you could make a safer AI if you delete all of the Reddit data from training. Sorry, out of luck: in an open-weight system (as opposed to a truly open-source system) you can’t change the training data at all, and in fact you can’t even
see
the training data.  Or let’s say you would like to train a model on legal reasoning and recognize that common law and statutory law are different. To reduce confusion in the system you would like to filter out the common law stuff before training; again you are out of luck. Or suppose you would like to use Big Company’s training process purely on your own data, rather than on whatever random stuff they scraped from the web. Nope, can’t do that either. (Nor can you share the results of any of those experiments with the community, since you can’t run them in the first place.)
Or say you are a regulator, and you would like to know how much bias there is towards white males in the training data. Sorry, can’t look at that, either.  What kinds of instructions are there relevant to bioweapons? Again, nope.
Are you a scientist? Want to investigate how much of what the model does is regurgitation and how much extends beyond the training data, which is arguably the central question in AI? Sorry, out of luck there, too. Those who
released
the open-weight model could do that, since they are privy to all these details that are actually closed, but you can’t.  Or maybe you just want to know whether the answers to your favorite benchmarks are actually already in the training data? Nope, can’t look at that, either.
All of this is unfortunate. It means that developers often can’t really use the open-weight models (despite the hype) to develop what they want; scientists can’t use them to test a lot of key hypotheses, and regulators can’t peer inside the process.
Furthermore, if you wanted to know how much of the training data was copyrighted, you can’t look at that either — which is perhaps part of why none of the big companies want to release true open-source, and instead settle for open-weight, getting nearly all of the positive press without actually helping the community nearly as much.
§
What prompted me to finally write about this?
Meta just released an open-weight model. To his credit, Zuckerberg himself got the terminology right here:
Releasing Muse Code in beta today. It's a terminal coding agent that takes on complete software engineering tasks across large repos: planning changes, writing code, validating the results. Powered by Muse Spark 1.2, a coding-focused model update.
7:09 PM · Aug 5, 2026
·
2.87M Views
1.34K Replies
·
1.28K Reposts
·
14.6K Likes
But the Times did not:
Putting scares quotes around open-source does not make an open-weight model more open. And although one can post-train
Meta’s new model, readapting it to some degree, for all the reasons I just described, it can’t be freely modified, nor used for proper science. You can’t do any of the modifications I described above. And you can’t figure out how the model got to be the way it is in the first place.
§
Zuckerberg knows perfectly well the difference between open-weight and open-source. A few weeks ago he was extolling the value of open-source:
But also played bait and switch with another tweet here:
Open source is a positive and important force for both empowering people and preventing centralization. Proud to support this.
Satya Nadella
@satyanadella
Open-weight models are essential to a healthy AI ecosystem. Together with others across our industry, we are outlining a path for open-weight models to strengthen American competitiveness and expand economic opportunity, while protecting national security. https://t.co/Tr0sAzAxTD
7:13 PM · Jul 24, 2026
·
8.29M Views
1.22K Replies
·
1.97K Reposts
·
25.4K Likes
And then today he released a model that is NOT open-source, hoping you wouldn’t notice the difference between the two. And, sadly, the Times didn’t.
I implore them, and everyone else, for the love of Turing, please don’t confuse open-weight with open-source.
P.S. Bonus analogy; pick your favorite:
Open weights similar to compiled binary - you cannot see the source code and internal guts. It's like calling a river "open source" because you're free to swim in it. Access is not the same as knowing the watershed that feeds it.
Sad to see the @nytimes confuse open-source (fully transparent) with open-weight models (less transparent; no access eg to training data).

The new Meta model is open-weight but not open-source. NYT got it wrong.  

It is time for both the media and the public to learn this
3:13 PM · Aug 10, 2026
·
5 Views
1 Like
