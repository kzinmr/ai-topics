---
title: "Bayesian OCR"
url: "https://www.johndcook.com/blog/2026/09/10/bayesian-ocr/"
fetched_at: 2026-09-11T10:01:12.382062+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Bayesian OCR

Source: https://www.johndcook.com/blog/2026/09/10/bayesian-ocr/

The Greek letter β (beta) and the German letter ß (eszett) look similar, especially in some fonts.
Now suppose an OCR program sees some character that could be a beta or could be an eszett. It could calculate some kind of distance between between the pixel pattern of the character and the pixel patterns of beta and eszett. But that would be discarding context.
If you’re scanning a Greek document and run into a beta-like symbol, it’s very likely a beta. If you’re scanning a German document and run into a beta-like symbol, it
could
be a beta. For example, it could be a scientific paper that mentions beta particles or beta carotene. But most likely the symbol is an eszett.
The previous paragraph is saying you should compute the
conditional
probability of a set of pixels representing a character
given
the language of the document. You could be more sophisticated and look at the position of the symbol in a word as well. For example, if you see a symbol at the end of a Greek word that could either be ο (omicron) or σ (sigma), it’s likely an omicron because Greek has a different symbol ς for final sigma.
This post is a follow-on to my
earlier post
on the error rate in Google’s Ngram database. OCR errors are fairly common in that database, so why don’t they “just” fix the errors by using some sort of Bayesian method? OCR software probably does use some sort of Bayesian method, but it’s not that simple.
In that post I looked at the use of the word
grok
in English. The Ngram database shows the word being used before it was coined in 1961 due to OCR errors. Why didn’t Google compute the probability of a word being “grok” conditional on the publication date? That would be circular. We happen to know exactly when
grok
was coined, but in general we might try to determine when a word was coined by looking at a large set of scanned books, like the Ngram database!
Now we could compute the probable value of an ambiguously scanned word by conditioning on the language of the surrounding text. That would be a reasonable thing to do in general, but it could also lead to exactly the kind of errors we see in the Ngram data for
grok
.
Suppose you see an ambiguously scanned word in a book written in English. There is a higher prior probability that the word is an English word than a German word. Now suppose you see “gro?” where ? could be β, ß, or k. Without any context, perhaps the probability of the symbol being a
k
is small. But
grok
is an English word and groß is a German word which may lead you to conclude “?” is a
k
and the ambiguous word is
grok
.
Assigning higher prior probability to English words in English texts is the best thing to do
on average
, but in particular instances it will lead to errors. That’s life.
The Ngram database includes millions of scanned books. Google had to use OCR algorithms that work well on average. A linguist with a special interest in a particular word can be more careful and create a more sophisticated probability model (explicit or implicit) customized for their interests. Google did what they could operating at such a large scale.
Related posts
