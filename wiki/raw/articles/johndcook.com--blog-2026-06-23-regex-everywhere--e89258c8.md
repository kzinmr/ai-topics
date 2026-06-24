---
title: "Regular expressions that work “everywhere”"
url: "https://www.johndcook.com/blog/2026/06/23/regex-everywhere/"
fetched_at: 2026-06-24T07:01:00.582050+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Regular expressions that work “everywhere”

Source: https://www.johndcook.com/blog/2026/06/23/regex-everywhere/

The most frustrating aspect of regular expressions is that implementations vary. Features supported in one tool may not be supported at all in another tool, or they may be supported with slightly different syntax.
I learned regular expressions in the context Perl, a maximalist regex environment. This led to frustration when features I expect to work are missing [1]. One way around this is to use
Perl analogs
of other tools, but this is very non-standard. I want to be able to send colleagues and clients code that works out of the box.
As I mentioned in my post on
computational survivalism
, I occasionally need to work on computers that I cannot install software on. So a better approach is to identify a subset of regex features that work everywhere. The stricter your definition of “everywhere” the less this includes. The strictest subset would be
literals
character classes
[…]
the special characters
. * ^ $
A more relaxed definition of “everywhere” would be the tools you most care about. Currently the tools I most want to use with regular expressions are sed, awk, grep, and Emacs.
Awk as lowest common denominator
If you use the Gnu versions of sed, awk, and grep, and use the
-E
option with sed and grep, then the list of common features is bigger. The regular expression features of of the three tools are similar, and awk’s features are supported in the other tools, with one exception: word boundaries in awk are
\<
and
\>
rather than
\b
and
\B
.
I wrote about Awk’s regex features
here
.
Emacs as the oddball
Emacs supports analogs of most of awk’s regex features. However, the characters
+ ? ( ) { } |
all require a backslash in front in order to act like the awk counterparts. Also, the analog of
\s
and
\S
in awk is
\s-
and
\S-
in Emacs.
Instead of meaning space or nonspace,
\s
and
\S
in Emacs begin a (negated) character class, and one of those classes is
-
for space. But there are many others. For example,
\s.
stands for a punctuation character and
\S.
stands for a non-punctuation character.
What works everywhere
So for my definition of “everywhere,” with the caveats mentioned above, the following features work everywhere. YMMV.
.
    ^, $
    […], [^…]
    *
    \w, \W, \s, \S
    \1 - \9 backreferences
    \b \B
    ? + 
    | alternation
    {n,m} for counting matches
    (...) capturing
[1] To some extent, basic Perl features work elsewhere and advanced features do not, depending on your idea of what is basic or advanced. I think of
look-around
features as advanced, and that tracks. But I think of
\d
for digits as basic, but that’s not supported in many regex flavors.
