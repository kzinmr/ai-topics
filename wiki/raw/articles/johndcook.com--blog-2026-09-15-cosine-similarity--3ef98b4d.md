---
title: "What counts as a large cosine similarity?"
url: "https://www.johndcook.com/blog/2026/09/15/cosine-similarity/"
fetched_at: 2026-09-16T10:01:33.520465+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# What counts as a large cosine similarity?

Source: https://www.johndcook.com/blog/2026/09/15/cosine-similarity/

Machine learning represents words as vectors and measures the similarity of words by the angles between the vectors.
For vectors
x
and
y
,
where θ is the angle between the vectors, and so
This is the cosine similarity between the words represented by
x
and
y
.
Small angles have large cosines, and so words with larger cosine similarities are closer together than words with smaller cosine similarities. The cosine similarity between a word and itself equals 1, and we’d expect unrelated words to have a cosine similarity near 0.
You can do a sort of arithmetic with vector embeddings of words. The canonical example is that
“king” − “man” + “woman” ≈ “queen”
Implicit in this equation is that we’re really adding vector representations of the words. Let
a
,
b
,
c
, and
d
be the vector embeddings of the words
king
,
man
,
woman
, and
queen
. What we’re really asserting is that
a
−
b
+
c
≈
d
,
except that’s not true! Or at least it’s not true unless you view it in the right context.
The angle between
a
−
b
+
c
and
d
is about 49°, which corresponds to a cosine similarity of 0.656. Here I’m using the gensim glove-twitter-200 embedding that represents words as 200-dimensional vectors.
The way to interpret the equation above is not that a 49° degree angle is approximately 0, or that a similarity of 0.656 is approximately 1.
In high dimensions, such as 200-dimensional word embeddings, nearly all vectors are nearly perpendicular. I wrote a post about this
here
. So the angle between randomly selected words will usually be close to 90°, and so in that context an angle of 49° is relatively small. For example, the angle between the vector representations of
king
and
fireplace
is 89.25°.
If you divide word vectors by their norm, you can think of each vector as a point on a high-dimensional sphere, in our case a sphere in 200 dimensions. The proportion of vectors within 49° of a given point is surprisingly small in high dimensions.
Let’s say our point of interest is the north pole of an
n
-dimensional sphere. We’d like to calculate the proportion of the area of the sphere that is within an angle θ of the pole. I go through the calculations
here
. (Update: I give an approximation
here
that’s easier to work with than the exact formula.)
When
n
= 3, 17% of the area is with 49 degrees of the pole. But when
n
= 200, the proportion is on the order of 10
−26
, essentially zero.
The vector
d
above representing
queen
is within a relatively tiny region around the vector
a
−
b
+
c
.
In terms of cosine similarity, 0.656 is a large similarity. Words with a cosine similarity in this range are quite close, even though we wouldn’t normally think of 0.656 being close to 1. In this context, 0.656
is
close to 1.
Related posts
