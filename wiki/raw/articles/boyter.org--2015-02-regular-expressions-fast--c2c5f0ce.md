---
title: "Regular Expressions are Fast, Until they Aren't"
url: "https://boyter.org/2015/02/regular-expressions-fast/"
fetched_at: 2026-05-05T07:02:02.854689+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Regular Expressions are Fast, Until they Aren't

Source: https://boyter.org/2015/02/regular-expressions-fast/

TL/DR: Regular expressions are fast, until they aren’t. How I got a 20x performance by switching to string functions.
With the new version of searchcode.com one of the main things I wanted to address was performance. The previous version had all sorts of performance issues which were not limited to the usual suspects such as the database or search index.
When developing the new version one of the tasks listed in my queue was to profile search operations for anything slowing things down. Sadly I have since lost the profile output but observed that one of the main speed culprits is the format_results function inside the code model. For most queries I tried while it was the slowest operation it wasn’t worth optimising simply because its impact was so low. I did however keep it in the back of my mind that if there were any performance issues it would be the first thing to look at.
The final step in any profiling however is to load some production data and run a load test. My personal preference being to generate a heap of known URL’s and tell a tool like Siege to go crazy with them. The results showed that 95% of pages loaded very quickly, but some took over 30 seconds. These instantly prompted further investigation.
A quick look at the profiler showed that the “back of mind function” was now becoming a serious issue. It seemed that for some regular expressions over some data types the worst case time was very bad indeed.
All of a sudden that function has become a major bottleneck.This needed to be resolved, to fix the worst case without selling out the best case which was very fast indeed. To get an understanding of what the function does you need to understand how searchcode works. When you search for a function of snippet searchcode tries to search for something that matches exactly what you are looking for first, and something containing anything in your query second. This means you end up with two match types, exact matches and fuzzy matches. The results are then processed by firstly trying to match the query exactly, and then going for a looser match.
This was implemented initially though two regular expressions like the below,
exact_match = re.compile(re.escape(search_term), re.IGNORECASE)
loose_match = re.compile('|'.join([re.escape(x) for x in search_term.split(' ')], re.IGNORECASE)
As you can see they are compiled before being handed off to another function which uses them for the actual matching. These are fairly simple regular expressions with the first just looking for any match and the second a large OR match. Certainly you would not expect them to cause any performance issues. Reading the following on stack overflow regarding the differences
https://stackoverflow.com/questions/4901523/whats-a-faster-operation-re-match-search-or-str-find
certainly seems to suggest that unless you are doing thousands of matches the performance should be negligible.
At heart searchcode is just a big string matching engine, and it does many thousands or hundreds of thousands of match operations for even a simple search. Since I don’t actually use of the power of regular expressions the fix is to change the code so that we pass in an array of terms to search for and use a simple Python
in
operator check.
exact_match = [search_term.lower()]
loose_match = [s.lower().strip()
                for s in search_term.split(' ')]
The results? Well remember we want to improve the worst case without selling out the best case, but the end result was pages that were taking nearly a minute to return were coming back in less than a second. All other queries seemed to come back either in the same time or faster.
So it turns our regular expressions are fast most of the time. Certainly I have never experienced and performance issues with them up till now. However at edge cases like the one in searchcode you can hit a wall and its at that point you need to profile and really re-think your approach.
