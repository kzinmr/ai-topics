---
title: "Vector Space Search Model Explained"
url: "https://boyter.org/2011/06/vector-space-search-model-explained/"
fetched_at: 2026-05-05T07:02:06.427227+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Vector Space Search Model Explained

Source: https://boyter.org/2011/06/vector-space-search-model-explained/

A mate of mine was looking at a previous article I wrote about
Decoding CAPTCHA’s
where I pointed people to the following article (PDF)
http://la2600.org/talks/files/20040102/Vector_Space_Search_Engine_Theory.pdf
He was having some difficulty understanding it so I thought I would write up a very simple explanation of what’s actually happening in the vector space.
The vector space isn’t actually that complicated, but getting your head around how it works takes a few steps. Let’s imagine for the moment that we are going to search over a collection of documents which only contain one word “boffin”. Each document has a different count of our word but only contain those words. We can represent this visually using a simple graph.
1 2 3  4
+---------+
 012345678
The above is trying to show along the X axis the count of our word “boffin” that appears in the document whose id appears above the line. You can see that document 1 has 1 “boffin” words in it and document 4 has 8. You can also see that document 1 is closer to document 2 then it is to document 4. Let’s say we decide to search for boffin twice IE our search term is “boffin boffin”.
+------+ "boffin boffin"
   |
   +
  1X2 3  4
+---------+
 012345678
What you can see quite clearly is that the closest document to our search (labelled in X) is document 1 and 2 followed by document 3 and 4. Let’s try searching for “boffin boffin boffin boffin”
+------+ "boffin boffin boffin boffin"
     |
     +
  1 2X3  4
+---------+
 012345678
You can now see that documents 2 and 3 are equally close to our search document, followed by document 1 and document 4.
So far so good. We can work out how close any two “boffin” documents are and thus work out how relevant they are to a search. Let’s add another word to our index. Our new documents are going to contain the words “boffin” and “head”
+
8|     3
7|
6|
5|
4|        4
3|
2| 1
1|
0|   2
 +---------+
  012345678
Along the X axis we still have the count for the word boffin. However we also have a Y axis which represents the count of the term “head”. Thus document 1 has 1 “boffin” word in it and 2 “head” words. You can also see that document 1 is closer to document 2 then document 3. Those of you who remember high school should remember this fellow.
Yes Pythagoras, a philosopher and mathematician came up with a [theorem][4] (although I suspect it should be a law now) that you could use to work out the length of a triangle’s side assuming the triangle is right angled and you know the length of the other two sides. We can do that now to work out the distance between document 1 and every other document in our collection.
Document 1 Distances

1 to 2 = 2.83
1 to 3 = 7.28
1 to 4 = 7.21
Assuming now that we had a search which had the terms “boffin head head” we can work out that the next most relevant documents would be 1 (exact match) followed by 2, 4 and 3, simply by calculating out the distances and ordering by them.
So far so good. Now to the next step, adding a third dimension which would represent a third word. It follows the same basic idea as before, just we need to do a few extra calculations’ to work out which documents are closest to each other. I am not going to do this here but im sure you can see how its a natural progression of the idea.
Now the “magic” of the vector space is realizing that if you can work out the distance between two documents when cast in 1d (first example) 2d (second example) and 3d space, you can continue to do so in 4d, 5d, 6d etc… You can’t represent it in the physical world, but in the mathematical world it works perfectly. This is the trick behind the vector space model and how it calculates how close any documents are.
Additional reading over the topic can be found here,
http://www.thebananatree.org/vector_space/vector_space.html
http://la2600.org/talks/files/20040102/Vector_Space_Search_Engine_Theory.pdf
http://en.wikipedia.org/wiki/Pythagorean_theorem
http://en.wikipedia.org/wiki/Vector_space_model
http://la2600.org/talks/files/20040102/Vector_Space_Search_Engine_Theory.pdf
http://www.wausita.com/2010/08/build-vector-space-search-engine-python/
