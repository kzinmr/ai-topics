---
title: "List of Most Commonly Used PHP Functions"
url: "https://boyter.org/2011/03/list-of-most-commonly-used-php-functions/"
fetched_at: 2026-05-05T07:02:06.831026+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# List of Most Commonly Used PHP Functions

Source: https://boyter.org/2011/03/list-of-most-commonly-used-php-functions/

One of the things about ranking in Search is that you need to consider all sorts of methods of working out what is relevent. Google broke new ground (although the idea had already existed) with its PageRank algorithm which supplied better search results then all the other search engines. For what I am doing however I need to consider what programmers are looking for. One thing that I considered some time ago was working out which are the most common functions in a language and adding this as an additional signal to ranking.
I couldn’t find anywhere else on the web with this question answered so I took my own approch. The method was to take a collection of large PHP projects, including, WordPress, Mambo, Sphider, Smarty, Drupal, CodeIgniter, dump all their source code into a single file stripped of comments, and then run some simple regex over this file counting the occurance of each function.
Of course the problem with that is for languages like Python with namespaces you need to build the first parts of a compiler/interpreter to work out the most commonly used functions and objects. PHP however traditionally has not had namespaces which makes it rather easy to pull apart and work out the most common functions.
The results of this can be found below.
