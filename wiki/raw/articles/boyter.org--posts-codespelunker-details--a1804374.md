---
title: "Code Spelunker how it works"
url: "https://boyter.org/posts/codespelunker-details/"
fetched_at: 2026-05-05T07:01:55.829629+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Code Spelunker how it works

Source: https://boyter.org/posts/codespelunker-details/

I released code spelunker a few days ago
https://github.com/boyter/cs
and literally one person asked for details on how it worked. Fitting in with my habit of putting any content I produce into my blog what follows is a built out version of it.
So code spelunker started when I noticed someone using Visual Studio to search files recursively in a directory and my own use of ripgrep with fzf. It’s development has been on and off over the last 4 years, roughly broken down into the following categories.
Code walking and .gitignore support
One of the first things I wanted was to do was have proper .gitigore an .ignore support. For scc I had previously used forked version of
go-gitignore
which was built to support
the_platinum_searcher
.
The reason for the fork was it crashing on certain inputs which I did
report back
but since the project appears to be abandoned I forked an patched it myself. However I was still unhappy with the library as such due to it’s lack of proper support for glob patterns.
Annoyingly this meant learning about how .gitignores and glob patterns worked. Thankfully there was a test repository created
https://github.com/svent/gitignore-test
which built to test ignore file support in
sift
. Because I could not find an existing library that worked correctly after trying several I decided to build my own.
The resulting library
gocodewalker
is a thin wrapper over the newer code walking functionality in Go and as far as I can tell fully supports all .gitignore and .ignore file logic correctly.
Faster string literal matching
I wanted to support case insensitive matching, so I started by using regular expressions. However anyone who has used the Go regex engine in anger soon realises that while it does have full unicode support it’s not as fast as you might expect especially when it comes to literal matches.
I wrote about this previously
faster literal string matching in Go
. However it also resulted in me going down a portion of the rabbit hole that is
unicode support
.
The resulting library can be obtained on github
go-string
. For unicode aware case insensitive literal string searches its close to a drop in replacement for some unicode functions.
It also includes a highlight function which you can use to wrap matching strings. For example
test
and have it return
<strong>te</strong>st
with it being aware of overlapping sections and being able to deal with it correctly.
Snippet’s are those extracts of text from the main document that you see in your search results. The general idea is to get a portion of the text that mostly closely matches your input string. It’s a complex problem with the results being subjective in the same way ranking is.
I wrote about this previously
abusing aws to make a search engine
but to save you a click, it works by passing the document content to extract the snippet from and all of the match locations for each term. It then looks though each location for each word, and checks on either side looking for terms close to it. It then ranks on the term frequency for the term we are checking around and rewards rarer terms. It also rewards more matches, closer matches, exact case matches and matches that are whole words.
The relevant code in code spelunker can be found in
snippet.go
and is reasonably well documented.
Ranking
Ranking was something I spent a bit of time on as well. At first I was not sure if it was even possible to brute force rank and so I implemented a few ranking algorithms, partly in case one was too slow and because I had way too much fun implementing them.
Learning about BM25 and TF/IDF is one of those things I had always wanted to do
The relevant code
is also reasonably well documented and if you are interested have a look. Its entirely possible I made some mistakes in there too, so if you find one please let me know.
TUI
I was sensible enough to not want to implement my own TUI. However it took a while for me to find one that I was able to wrap my brain around and then learn how it worked. I settled on
tview
which was simple enough to understand if you are familiar with css flexbox.
It did take me a while to understand its redraw logic and avoid a heap of random deadlocks. This took probably longer than any other thing since the only way to test it was try an excessive amount of searches across multiple sources.
The future…
Since it was asked, one of the things I am considering doing is adding in an index. To do this I would need to add literal extraction of regular expressions in order to make that initial query inside what would probably been a trigram index.
This would allow code spelunker to scale, although keeping the index in sync would be a little painful. Other ideas include syntax highlighters, the ability to sync repositories while its running, fuzzy finding by filenames and the ability to filter by filename and location.
