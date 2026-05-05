---
title: "Faster Literal String Matching in Go"
url: "https://boyter.org/posts/faster-literal-string-matching-in-go/"
fetched_at: 2026-05-05T07:01:57.701305+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Faster Literal String Matching in Go

Source: https://boyter.org/posts/faster-literal-string-matching-in-go/

TL/DR:
I wrote a fast literal string matching library in Go get it here
https://github.com/boyter/go-string/
Recently I rebuilt
searchcode
in Go, as
mentioned
.
While there was a variety of reasons for this one was that performance in the previous Python version was not great. Please note this was mostly due to my own shortcomings and not the language itself. However I have always used searchcode as a test bed for interesting problems, since it gets enough traffic to verify things at scale, and I wanted to get better at Go.
One of the main performance hotspots in searchcode has always been finding lines to display based on the search query and then highlighting them. While most search index tools can do this for you, I have always done this myself, because I want to control whats displayed as I find it an interesting problem to solve.
It sounds simple, for some search terms “sally sea shell” find all the locations of inside a string “Sally sells sea shells by the sea shore” and then wrap them in a tag. This seems to be a trivial, since all you need a
indexOf
in a loop and some string splitting and insertion.
I had previously written about some of the issues with the above when writing about
unicode support
with the relevant portion below,
At which point you go, fine i’ll just search for all case variants of Java and use that to work things out, and then realise adding case folding is a small addition to what you just wrote and working with just bytes to save time was a red-herring.
The generally always correct answer to case insensitive matching is to use Regular Expressions. However there can be issues with it. Firstly the regular expression engine in Go is slower than you think, and for matching string literals its a very large hammer for a smallish nail.
So I wrote my own implementation which does the same thing but without touching the regular expression engine
https://github.com/boyter/go-string/
thus making it much faster than using FindAllIndex for the majority of cases.
Talk is cheap… show me the benchmarks. Included below is the output from a small application I wrote. A small program which you supply a search string and a filename. I have tested it against a 550MB file. First it runs case insensitive search using FindAllIndex in the regex package, then against IndexAllIgnoreCase my own implementation. The number on the end of each line is the number of matches found.
$ ./csperf ſecret 550MB
File length 576683100

FindAllIndex (regex ignore case)
Scan took 25.403231773s 16680
Scan took 25.39742299s 16680
Scan took 25.227218738s 16680

IndexAllIgnoreCase (custom)
Scan took 2.04013314s 16680
Scan took 2.019360935s 16680
Scan took 1.996732171s 16680
Note using the long s,
ſ
in the search term so both solutions are unicode aware!
The results speak for themselves. The case insensitive search is considerably faster. For pure literal case insensitive searches based on wall clock time it can be 10 times faster. I also added an implementation of
IndexAll
for case sensitive matches saving you from having to do your own logic there or again falling back to regular expressions, although its speedup will depend on your needle and haystack.
If you are curious about I did this read on. Otherwise feel free to just suck down the library and use it. It’s published under either MIT or The Unlicense so be as liberated as I can make it. There is also some other useful functions in there such as the highlight function which I am not going to discuss here.
So how does it work?
The code itself is reasonably
well commented
so you may want to just read the code.
In short it copies some techniques from tools like ripgrep.
When looking at string matching algorithms, you run into algorithms such as Boyer-Moore, Aho-Corasick and Rabin-Carp. It may then surprise you to learn that Go’s implementation of strings.Index does not use them, well at least not till the needle is over 64 characters when 64 bit compiled where it starts to use Rabin-Carp, presumably as a CPU cache line optimisation.
What strings.Index actually does a simple loop through each byte checking for a match, and then when one is found starts checking against the needle. This means it does not do any byte skipping which Boyer-Moore does! Naturally, I was appalled by this and looked for a Boyer-Moore implementation to swap it out for. Turns out there is one inside the Go codebase which made me very curious. Why was it not used? Well after trying a few implementations each turned out to be much slower than the simple one Go uses. As it turns out, that implementation compiles down to fancy vector instructions on modern CPU’s. It’s pretty hard to beat silicon with algorithms, unless you algorithm happens to be massively more efficient so there was no trivial gains to be made there with a fancy algorithm.
So what actually happens in the code is that it takes the needle, and uses the first 3 characters (if over 3 characters long) to create a string of every possible case. So
foo
would return the following strings
foo Foo fOo FOo foO FoO fOO FOO
. It then searches using each one of those cases and collecting all the resulting matching locations. For strings over 3 characters (note characters, not bytes so it is unicode aware for simple case fold rules), as mentioned the first 3 characters are used, and then when a possible match is found the rest of the characters are checked to see if there is actually a match before recording the location.
In theory Aho-Corasick would be faster than the above as you could use maybe the first 4 characters and use that for matching each byte, however I was not going for extreme performance, but something much faster than regular expressions. Also its reasonably simple to follow, while leveraging the Go SDK which is a massive win in my opinion.
The result is currently running in searchcode. This replaces what was the slowest portion of the code in the old version of searchcode and is much faster reducing the load on the servers considerably. Every string runs through the implementation and as such its fairly battle tested. It might not be perfect, but there has been no crashes to date with the v1.0.0 tag release so it should be reasonably safe to use, but of course there is no warranty. As mentioned a few times the code is open and on github, so feel free to bash against it
https://github.com/boyter/go-string
and report bugs! If you do run into an interesting case where you use it let me know and ill add it to the README.
