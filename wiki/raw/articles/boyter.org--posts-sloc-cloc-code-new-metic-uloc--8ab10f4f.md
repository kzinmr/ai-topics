---
title: "Sloc Cloc and Code - ULOC Unique Lines of Code"
url: "https://boyter.org/posts/sloc-cloc-code-new-metic-uloc/"
fetched_at: 2026-05-05T07:01:54.991031+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Sloc Cloc and Code - ULOC Unique Lines of Code

Source: https://boyter.org/posts/sloc-cloc-code-new-metic-uloc/

I recently pushed out a new release of Sloc Cloc and Code (scc) with two main pieces of functionality. The first being accurate .gitignore support. The latter being the first new feature to hit the codebase in a long time in the form of a new metric you can access Unique Lines of Code or ULOC.
A few years ago exwhyz (who appears to have dropped off the internet) posted a
feature request
to include this new metric into
scc
’s outputs.
They also helpfully included the following links,
https://cmcenroe.me/2018/12/14/uloc.html
and its
lobste.rs discussion
about the idea.
To save you a click I have included the most relevant quote,
In my opinion, the number this produces should be a better estimate of the complexity of a project. Compared to SLOC, not only are blank lines discounted, but so are close-brace lines and other repetitive code such as common includes. On the other hand, ULOC counts comments, which require just as much maintenance as the code around them does, while avoiding inflating the result with license headers which appear in every file, for example.
At the time I was busy doing other things, and I had been wanting to fix .gitignore support in scc by moving it to use
gocodewalker
. With that recently done I remembered this feature and took another look at it.
What really helped was that the link contained an implementation (this makes implementing it much easier)
sort -u *.h*.c | wc -l
I have always been pretty open with adding new metrics into scc, such as the complexity estimate, the COCOMO calculations, and frankly this sounded like it could be useful. Especially with the suggestion by minimax at lobste.rs of a DRYness calculation where
DRYness = ULOC / SLOC
. Since scc does have the SLOC count, this makes adding a DRYness calculation into the app rather trivial.
Now looking at the supplied calculation, it of course has a few problems in that it does not recurse directories, does not respect .gitignore files and groups languages together which may not be ideal. We can overcome all of that by adding this into scc. Which is what I did.
$ scc -i go,java -a --no-cocomo
───────────────────────────────────────────────────────────────────────────────
Language                 Files     Lines   Blanks  Comments     Code Complexity
───────────────────────────────────────────────────────────────────────────────
Go                          30      9335     1458       453     7424       1516
(ULOC)                              3930
-------------------------------------------------------------------------------
Java                        24      3913      798       651     2464        547
(ULOC)                               102
───────────────────────────────────────────────────────────────────────────────
Total                       54     13248     2256      1104     9888       2063
───────────────────────────────────────────────────────────────────────────────
Unique Lines of Code (ULOC)         4026
DRYness %                           0.30
───────────────────────────────────────────────────────────────────────────────
Processed 524736 bytes, 0.525 megabytes (SI)
───────────────────────────────────────────────────────────────────────────────
scc now has two additional flags for this,
-a --dryness
and
-u --uloc
with the former implying the latter. Adding a new metric to the output of what was already a very condensed display was took a while but we can now see per language the ULOC value, and of course the total. NB I am not sold on this output yet, and am happy to change it if someone comes up with something better.
Now what does this tell us? I know that the inclusion of Java here is a lot of redundant copy pasted Java files used in scc to test the duplication detection. This is reflected in the ULOC calculation of Java where only 102 of the lines are unique compared to the 3913 that exist.
Restriction to just Go gives the following output, with the corresponding DRYness % value increasing as is expected.
$ scc -i go -a --no-cocomo
───────────────────────────────────────────────────────────────────────────────
Language                 Files     Lines   Blanks  Comments     Code Complexity
───────────────────────────────────────────────────────────────────────────────
Go                          30      9335     1458       453     7424       1516
(ULOC)                              3930
───────────────────────────────────────────────────────────────────────────────
Total                       30      9335     1458       453     7424       1516
───────────────────────────────────────────────────────────────────────────────
Unique Lines of Code (ULOC)         3930
DRYness %                           0.42
───────────────────────────────────────────────────────────────────────────────
Processed 395673 bytes, 0.396 megabytes (SI)
───────────────────────────────────────────────────────────────────────────────
Is the DRYness % there a good value? I had no idea. So I tried it against the C portion of the redis fork
Valkey
since it is/was well known to be a pretty clean codebase.
$ scc -a -i c --no-cocomo valkey
───────────────────────────────────────────────────────────────────────────────
Language                 Files     Lines   Blanks  Comments     Code Complexity
───────────────────────────────────────────────────────────────────────────────
C                          423    244716    27969     42431   174316      42926
(ULOC)                            135502
───────────────────────────────────────────────────────────────────────────────
Total                      423    244716    27969     42431   174316      42926
───────────────────────────────────────────────────────────────────────────────
Unique Lines of Code (ULOC)       135502
DRYness %                           0.55
───────────────────────────────────────────────────────────────────────────────
Processed 8553843 bytes, 8.554 megabytes (SI)
───────────────────────────────────────────────────────────────────────────────
As expected the higher the value the more “clean” the codebase is, with a value of 0.55 being what I am guessing is a very good value. The closer you get to 1 the more DRY your code is, with a score close to 0.5 being considered “good”.
Alas its not a free lunch with the new metric eating into the runtime of scc… by a lot.
$ hyperfine 'scc -i c valkey' 'scc -i c -a valkey'
Benchmark 1: scc -i c valkey
  Time (mean ± σ):      48.8 ms ±   0.5 ms    [User: 94.5 ms, System: 38.5 ms]
  Range (min … max):    48.0 ms …  50.6 ms    56 runs

Benchmark 2: scc -i c -a valkey
  Time (mean ± σ):      89.3 ms ±   2.1 ms    [User: 154.5 ms, System: 45.8 ms]
  Range (min … max):    86.9 ms …  95.2 ms    32 runs

Summary
  scc -i c valkey ran
    1.83 ± 0.05 times faster than scc -i c -a valkey
Thankfully however I had paid so much attention to performance in scc over the years that while there is a cost for metrics you only want every now and again its not too painful to get.
Anyway is this useful? I have no idea. I hope the user exwhyz comes back and reports on it in the github issue at some point. If you however are using scc and find this useful please let me know as I am still learning what it means myself.
