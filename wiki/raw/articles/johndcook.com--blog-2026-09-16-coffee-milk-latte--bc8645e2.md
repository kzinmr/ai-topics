---
title: "Coffee + milk ≠ latte"
url: "https://www.johndcook.com/blog/2026/09/16/coffee-milk-latte/"
fetched_at: 2026-09-17T10:01:20.274815+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Coffee + milk ≠ latte

Source: https://www.johndcook.com/blog/2026/09/16/coffee-milk-latte/

Yesterday
I wrote about the canonical example of how vector embeddings of words add:
“king” − “man” + “woman” ≈ “queen”
This should be interpreted as saying that the word vector for
king
, minus the word vector for
man
, plus the word vector for
woman
, is in some sense close to the word vector for
queen
.
This post will look at another example. Is the expression
“coffee” + “milk” ≈ “latte”
true in some sense?
Notation
In this post I will use “foo” to mean the vector embedding of the word
foo
.
Coffee + milk
The cosine similarity between “coffee” + “milk” and “latte” is about 0.63. And for reasons given in the previous post, this is a large value of cosine similarity. But there are 11 words that are more similar to “milk” + “coffee” than “latte”. Here are the top 12 matches in order.
coffee
milk
tea
drink
chocolate
cream
breakfast
ice
beer
vanilla
starbucks
latte
There are two questions to resolve. First, why isn’t
latte
one of the closest words? Second, why is the cosine similarity large even though
latte
is not one of the best matches?
Concept arithmetic
When word vector arithmetic works, as in the king and queen example, the vectors combine
concepts
. If you replace the male gender component of
king
with a female component, you get a vector close to the vector for
queen
.
But when you add the vectors for
milk
and
coffee
, you’re not adding concepts, you’re adding ingredients.
The concepts of
milk
and
coffee
are similar in that they’re both common beverages, as are tea and even beer. A latte is a beverage, but it’s not as common as milk, coffee, tea, or beer.
Extremely uneven distribution
If you divide word vectors by their norm, you get a point on a high-dimensional sphere. In the case of the glove-twitter-200 vector embedding, you get a point on a sphere in 200 dimensions. As explained in the earlier post, a fairly large cosine similarity corresponds to a tiny portion of the sphere’s surface area.
In the example of “king” − “man” + “woman”, the vector “queen” is the closest match (except for “king” itself).
But there are a lot of words whose vectors are within a tiny region around “coffee” + “milk”. And by tiny, I mean a region that accounts for a proportion of the sphere on the order of 10
−23
.
The glove-twitter-200 vector list contains vectors for 1.2 million words. If these vectors were roughly evenly distributed on the sphere when normalized, you’d expect each patch representing 10
−6
of the sphere to contain about a word or two. You wouldn’t expect a patch taking up 10
−12
of the sphere to contain more than one word, and you certainly wouldn’t expect a patch taking up 10
−23
of the sphere to contain 12 words.
Rank order
Rank order based on cosine similarity is more robust than cosine similarity itself. This is an example of a phenomenon that occurs regularly: a metric whose values are dubious might still rank things well. Naive Bayes is another example. It naively computes probabilities in a way that is blatantly wrong, and yet ranking things by these spurious probabilities works well in some cases.
The cosine similarity between “king” − “man” + “woman” and “queen” is roughly the same as the cosine similarity between “coffee” + “milk” and “latte.” But in the former example, rank order picks out
queen
as the best match; rank order works like you’d expect, because you’re working with attributes that can be decomposed.
Dog + infant = puppy?
I wouldn’t be surprised if the Anglo-Saxon word for
puppy
was something like
dogchild
. The language was full of colorful compound words, such as
hronrad
(“whale-road”) for the sea and
nosethyrl
(“nose-hole”) for nostril.
Here are the top ten matches for “dog” + “infant” along with their cosine similarities.
dog, 0.819
infant, 0.809
toddler, 0.734
dogs, 0.697
puppy, 0.688
cat, 0.682
pet, 0.676
child, 0.671
newborn, 0.670
baby, 0.650
This shows that “puppy” is close to “dog” + “infant”, both in terms of cosine similarity and rank order, though it’s not the closet.
This also shows that you have to take the addition of word vectors with a grain of salt. It’s no surprise that
puppy
was a good match, but it’s surprising that
cat
is nearly as good.
