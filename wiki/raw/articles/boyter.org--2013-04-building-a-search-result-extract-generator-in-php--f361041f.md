---
title: "Building a Search Result Extract Generator in PHP"
url: "https://boyter.org/2013/04/building-a-search-result-extract-generator-in-php/"
fetched_at: 2026-05-05T07:02:04.984383+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Building a Search Result Extract Generator in PHP

Source: https://boyter.org/2013/04/building-a-search-result-extract-generator-in-php/

During some contracting I was doing recently there was a requirement to implement some search logic using only PHP. There are no issues with that but it turns out I couldn’t find a decent extract generator handy as usually one would just plug into the search engines provided version to do this.
Off the top of my head I could only think of one example I was aware of which lives in
Sphider
(for the record it lives in searchfuncs.php from line 529 to 566). Sadly it has a few issues. Firstly the code is rather difficult to understand, and more importantly it usually has accuracy issues. A quick search turned up this link
http://stackoverflow.com/questions/1436582/how-to-generate-excerpt-with-most-searched-words-in-php
on StackOverflow. The second answer looked promising but its even more difficult to understand and a bit of profiling showed some performance issues will all of the regex going on in there.
Since I couldn’t find a solution I was happy with I naturally decided to write my own. The nice thing about reinventing the wheel is you can get a round one. The algorithm is fairly simple,
Identify all the matching word locations.
Work out a section of text that best matches the terms.
Based on the snip location we trim around the string ensuring we don’t skip whole words and don’t remove the last or first word if that’s the actual match.
Sounds good in theory, but lets see the results.
Sample Text
“Welcome to Yahoo!, the world’s most visited home page. Quickly find what you’re searching for, get in touch with friends and stay in-the-know with the latest news and information. CloudSponge provides an interface to easily enable your users to import contacts from a variety of the most popular webmail services including Yahoo, Gmail and Hotmail/MSN as well as popular desktop address books such as Mac Address Book and Outlook.”
Search Term
“yahoo and outlook”
Sphider Snippet
“get in touch with friends and stay in-the-know with the latest news and information. CloudSponge provides an interface to easily enable your users to import contacts from a variety of the most popular webmail services including Yahoo, Gmail and Hotmail/MSN as well as popular desktop address books such as Mac Address Book and”
Stackoverflow Snippet
“Welcome to Yahoo!, the world’s most visited home page. Quickly find what you’re searching for, get in touch with friends and stay in-the-know with the latest news and information. CloudSponge provides an interface to easily enable your users to import contacts from a variety of the most…”
My Snippet
"..an interface to easily enable your users to import contacts from a variety of the most popular webmail services including Yahoo, Gmail and Hotmail/MSN as well as popular desktop address books such as Mac Address Book and Outlook."
I consider the results to be equally good in the worst case and better in most cases I tried. I also tried each over much larger portions of text and both the Sphider and Stackoverflow seemed to produce either nothing relevant or were missing what I thought was the best match.
As always the code is on
GitHib
and included below just in case.
<?
php
// find the locations of each of the words
// Nothing exciting here. The array_unique is required
// unless you decide to make the words unique before passing in
function
_extractLocations
($words, $fulltext) {
$locations
=
array
();
foreach
($words
as
$word) {
$wordlen
=
strlen
($word);
$loc
=
stripos
($fulltext, $word);
while
($loc
!==
FALSE
) {
$locations[]
=
$loc;
$loc
=
stripos
($fulltext, $word, $loc
+
$wordlen);
}
}
$locations
=
array_unique
($locations);
sort
($locations);
return
$locations;
}
// Work out which is the most relevant portion to display
// This is done by looping over each match and finding the smallest distance between two found
// strings. The idea being that the closer the terms are the better match the snippet would be.
// When checking for matches we only change the location if there is a better match.
// The only exception is where we have only two matches in which case we just take the
// first as will be equally distant.
function
_determineSnipLocation
($locations, $prevcount) {
// If we only have 1 match we dont actually do the for loop so set to the first
$startpos
=
$locations[
0
];
$loccount
=
count
($locations);
$smallestdiff
=
PHP_INT_MAX
;
// If we only have 2 skip as its probably equally relevant
if
(
count
($locations)
>
2
) {
// skip the first as we check 1 behind
for
($i
=
1
; $i
<
$loccount; $i
++
) {
if
($i
==
$loccount
-
1
) {
// at the end
$diff
=
$locations[$i]
-
$locations[$i
-
1
];
}
else
{
$diff
=
$locations[$i
+
1
]
-
$locations[$i];
}
if
($smallestdiff
>
$diff) {
$smallestdiff
=
$diff;
$startpos
=
$locations[$i];
}
}
}
$startpos
=
$startpos
>
$prevcount
?
$startpos
-
$prevcount
:
0
;
return
$startpos;
}
// 1/6 ratio on prevcount tends to work pretty well and puts the terms
// in the middle of the extract
function
extractRelevant
($words, $fulltext, $rellength
=
300
, $prevcount
=
50
, $indicator
=
'...'
) {
$textlength
=
strlen
($fulltext);
if
($textlength
<=
$rellength) {
return
$fulltext;
}
$locations
=
_extractLocations
($words, $fulltext);
$startpos
=
_determineSnipLocation
($locations,$prevcount);
// if we are going to snip too much...
if
($textlength
-
$startpos
<
$rellength) {
$startpos
=
$startpos
-
($textlength
-
$startpos)
/
2
;
}
$reltext
=
substr
($fulltext, $startpos, $rellength);
// check to ensure we dont snip the last word if thats the match
if
( $startpos
+
$rellength
<
$textlength) {
$reltext
=
substr
($reltext,
0
,
strrpos
($reltext,
" "
))
.
$indicator;
// remove last word
}
// If we trimmed from the front add ...
if
($startpos
!=
0
) {
$reltext
=
$indicator
.
substr
($reltext,
strpos
($reltext,
" "
)
+
1
);
// remove first word
}
return
$reltext;
}
?>
