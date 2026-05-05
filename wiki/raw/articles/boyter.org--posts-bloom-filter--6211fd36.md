---
title: "Bloom Filters - Much, much more than a space efficient hashmap!"
url: "https://boyter.org/posts/bloom-filter/"
fetched_at: 2026-05-05T07:01:57.541308+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Bloom Filters - Much, much more than a space efficient hashmap!

Source: https://boyter.org/posts/bloom-filter/

A bloom filter is one of those data structures you are probably already aware of, or have at least heard about. For those looking for a simple recap, they are a probabilistic data structure which can be used to determine if something is in a set or not, giving a slight chance of returning a false positive result for some checks but while using less space than a full hashmap.
What you may not know is that while you can use them as a space efficient hash/dictionary there are other use cases you might not be aware of.
Implementation of a bloom filter
However before going though usage though, lets take a quick moment to build one. A lot of people seem to lack this understanding and assume that bloom filters are more complex or mysterious than they actually are.
Turns out a bloom filter is actually really easy to build if you don’t mind doing it inefficiently (at least at first). I am going to implement one using JavaScript because anyone reading this can follow along using the browser console. Why? Well I find a simple bit of code tends to be mostly unambiguous and communicates meaning quite well.
The first thing you need is a hash function. Ideally for a bloom filter you want to use something like Murmur3 and FNV-1a because you want the hash to be as fast as possible and yet have a good distribution. See
this excellent stackexchange
question and the first comment for more detail.
However because JavaScript in the browser does not come with hash, here is a port of the Java string hash which gets us moving without needing to implement anything too difficult. You can copy and paste the below into your console, which will add a hash function to strings.
// Primitive hash function that for a string returns a positive 32 bit int
// Do not use in production, use murmur3 or fnv1
Object.
defineProperty
(String.
prototype
,
'hashCode'
, {
value
:
function
() {
var
hash
=
0
,
i
,
chr
;
for
(
i
=
0
;
i
<
this
.
length
;
i
++
) {
chr
=
this
.
charCodeAt
(
i
);
hash
=
((
hash
<<
5
)
-
hash
)
+
chr
;
hash
|=
0
;
// Convert to 32bit integer
}
return
Math.
abs
(
hash
);
}
});
So with that done lest create our filter. At it’s heart the filter itself is just an array of bits. You only need to store two states for every entry in the array. Note that in many languages using a boolean is not backed by a bit so using boolean’s as your backing array might not be as efficient as you expect. You tend to need to use a bitset implementation or bit packing into an integer for efficiency but that’s out of the scope of what we need here.
Lets create a bloom filter which contains 16 boolean’s to represent our bits and then hash two words and put them into the filter.
// start out our bloom filter out with 16 0's indicating its empty
var
bloom
=
[
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
0
];
// add some words to the filter using a single hash
// we use % to convert our 32 bit number into one of 16 values
// for the length of our bloom filter
bloom
[
"something"
.
hashCode
()
%
bloom
.
length
]
=
1
;
bloom
[
"another"
.
hashCode
()
%
bloom
.
length
]
=
1
;
After running the above your bloom filter should have 2 bits set and look like the following,
[
0
,
0
,
0
,
0
,
0
,
0
,
0
,
1
,
0
,
0
,
0
,
0
,
0
,
0
,
0
,
1
,
0
]
As you can see positions 7 and 15 in this filter are now set. In order to check if something is in the filter, you do the same hash operations and check the value rather than setting. So if we want to see if something is in the filter,
if
(
bloom
[
"something"
.
hashCode
()
%
bloom
.
length
]
==
1
) {
// something might be in the filter
}
Note the comment that says it “might” be in the filter due to the false positive properties of a bloom filter.
The above is pretty much all you need to get started with bloom filters. For a real implementation swap out for a better hash function, in fact use two of them with salts in order to get more than 2 hashes which you will need to drive down the false positive rates. You also need to increase the size of the filter itself for anything non trivial. Use
this calculator
in order to determine how large a filter you need to achieve your desired false positive rate.
Note that the false positive rate is actually a feature, and there are situations where you might want to drive it up or down to achieve your goal.
If you are looking for bit more detail about how to implement one here is a gist
https://gist.github.com/boyter/0cffa9ff8e2e7259d455594d744f1164
which has a bit more details and examples.
Note that bloom filters don’t have any inbuilt limit to how many terms you can add. You can add as many terms to them as you want, but at some point it drives the false positive rate close to 100% making the filter effectively useless, so knowledge of how many terms you are going to store in it up front is a requirement of using them effectively.
Interesting use cases of bloom filter’s
Bloom filters can be so much more than a space efficient hashmap! Lets go though some of the more and less common use cases for them.
The first and most obvious is to use it as a lookup cache. This is the same idea as a hashmap but more space efficient. Consider running a video/music e-store where you pull detailed information about the movie or song from a back-end database or cache. With a bloom filter fronting it you could use a smallish amount of memory to filter requests to the back-end by only looking where you are confident that a result exists. Because each key you need to store can fit into ~10 bits of data you can trade a small amount of memory to avoid overloading your backend systems.
You can also use bloom filters to mitigate cache busting attacks on your website. For any website its fairly common to use various cache levels in order to prevent multiple requests hitting your back-end and overloading it. However most websites also allow parameters either in the URL itself or via GET parameters. Consider a e-commerce site where you have many product id’s, and by fiddling with the URL someone can iterate though them all. While you can cache results for each product, what happens if someone malicious decides to request items for which there is no product? You have to check your back-end in order to actually check if its there, which at scale can cause contention on your system. You can use bloom filters to hold all of the product id’s, and only hit the back-end for a full lookup if the filter says the item actually appears.
Akami also uses bloom filters to avoid one hit wonder items filling the cache. There is little benefit in populating your cache for items that are only requested once, and the long tail of the internet is very large. Akami realized this and used a bloom filter to determine if the item in question had been requested before and only after being requested the second time would the item be cached. A similar technique can be used by any cache system to avoid populating your cache with rarely requested items.
Spelling checkers were also a use case for bloom filters back in the day when you really had to worry about your memory usage. At ~10 bits per term you could pack a lot of words into limited memory, with fast lookups to determine if a word was a real word or not.
One thing to consider is the properties of a bloom filter. Because you hash keys multiple times through a non reversible function, it’s possible to then share your bloom filter at the end as a way to share information that you hold without sharing the information itself. You can even make it impossible to brute force to get the information back because you can configure your filter to have a higher error rate and swamp the attacker with false positives as they brute force things.
Consider a distributed social network where I want to have two people determine if there is any overlap in their contact lists. I want to do so without having to share the lists because of privacy reasons. You could build a filter for each users contacts, and swap them. Then check against the filter in order to determine if we have an overlap, without the possibility of you being able to reconstruct either list even were you to hold even both filters. Assuming I am worried about someone getting a copy of these filters I can also drive up the false positive rate to thwart the potential attack.
You can extend this idea further as well. Say I want to determine the overlap between two user’s social circles. Build two filters of the same size containing each users friends. Then compare the bits of the two filters. The more overlap the more shared bits. This also applies to finding distance between words or sentences, and it works regardless of how long the text is as its driven more closely by the words/terms and not how often they appear. You split the document into ngrams (say trigrams), add each into your filter and compare them the same way. The more overlapping bits the closer they are.
The idea of sharing reasonable proof of ownership is an interesting use case for bloom filters. Say for example you have obtained a list of hashed passwords and want to prove you have them without transmitting the hashes themselves. You could encode them all into a bloom filter configured with a high error rate.
You can also use bloom filters to make a search engine. I first read about this idea on
Hacker News
with the idea being you build a bloom filter per document you want to index and then loop over each filter to check if terms are in each. This works at a small scale of a few thousand documents.
However this is a fairly primitive version of a bloom filter search engine. You can do much better as it turns out.
The nice thing about bloom filters is that you can query them using bitwise operations. In effect if you store each document in a filter of the same size, you end up with a collection of filters in a block that looks like the below for 3 documents with 8 bit bloom filters for each one.
document1 10111010
document2 01100100
document3 00100111
This is great because say you have search for a term with the hash
10010000
(note that the search filter must be as long as the documents you are searching) you can then step through each document applying bitwise AND operations to see if the result is zero and if not it means we might have a matching document. Bitwise operations are very fast on any CPU so the actual check is effectively free from a CPU point of view. The catch being you need to step through every part of memory for your whole corpus.
There is a way to reduce this however. If you rotate the bit vectors you can then just check those which match your search term hash bit positions, so documents move from being rows to columns like so.
In the below document 1 is now represented by column 1.
term1 100
term2 010
term3 111
term4 100
term5 100
term6 011
term7 101
term8 001
Then given our search
10010000
you would look at the bits for term1 and term4 (as bit position 1 and 4 are set). Then AND them together and you get
1
indicating that document 1 is a possible match for the search. It also reduced the number of bits we looked at for this query from 24 to 9. This is more impressive when you have larger filters (which you would expect).
It looks like this,
search 10010000

positions 1 and 4 are set so we want to use those

take from our filter positions term1 and term4

term1 100
term4 100

then OR them together

100

which means document1 which was in the first column might be a match
What’s really cool about this search technique is that because bitwise operations are so fast you can consider them free you end up being limited only by memory bandwidth, which means you can actually work out how long each search will take based on the number of documents in your index per machine.
However part of the bing.com managed to improve this algorithm even more. It’s well out of the scope of this document, but it involves using what they call higher ranked rows where they logically OR half of the filter against itself to reduce memory access. Along with the ability to shard filter lengths to different machines (possible because of scale) they are able to reduce memory access to a level where they can run thousands of searches on each machine per second. Its a very cool collection of techniques.
The links you need to get started on how Bing does this are below,
They are worth looking at!
Similar data structures
There are modified versions of bloom filters, as well as other similar structures.
Variants of bloom filters include compressed bloom filters, expiring and counting bloom filters. They use less memory, expire old keys and record how many times keys were added (allowing removal if you implement it correctly at the expense of memory).
Another similar one is the cuckoo filter which works in a similar way to a bloom filter, except it has a inbuilt limit after which it will no longer add items, can delete items and has some different memory characteristics.
Conclusion
So, what started as me wanting to implement bitfunnel myself turned into a longer than I expected look at bloom filters in general. I have to admit they are now my new favorite data structure (wow… how much of a nerd do you have to be to have one of those) supplanting my previous which was the vector space. While I don’t really have any use for bloom filters in much of what I do from day to day I’m hoping like
https://boyter.org/posts/media-clipping-using-ffmpeg-with-cache-eviction-2-random-for-disk-caching-at-scale/
2 random cache eviction I might get to use it one of these days.
