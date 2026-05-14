---
title: "Points are a weird and inconsistent unit of measure"
url: "https://buttondown.com/hillelwayne/archive/points-are-a-weird-and-inconsistent-unit-of/"
fetched_at: 2026-05-14T07:00:38.816469+00:00
source: "buttondown.com/hillelwayne"
tags: [blog, raw]
---

# Points are a weird and inconsistent unit of measure

Source: https://buttondown.com/hillelwayne/archive/points-are-a-weird-and-inconsistent-unit-of/

I'm in the middle of redoing the
Logic for Programmers
diagrams and this has surfaced a really annoying problem. The book is formatted in LaTeX using a pseudo-grid of 10.8pt × 7.2pt. The diagrams are done in Inkscape using a 10.8pt × 7.2pt.
Last week I found out that these are not the same points.
Latex defines a point as 1/72.27 inches (0.3515 millimeters). Inkscape instead uses 1/72 inches (0.3528 mm). It's only a difference of 0.4% but it still floors me that two widespread digital technologies would be different!
So, uh,
what happened?
A few hours of reading articles later, this is what I found, caveat that I didn't spend all that much time researching this and this is only initial impressions.
what even is a point
A
point
is a typographic measure, coming from 1517, that is supposedly the smallest interesting size for a printer. This was notably not a standardized measure- different companies in times used different point sizes depending on their equipment. Over time it was standardized, but each country picked a different standard: the German and Japanese point is 0.250 mm, the French point is allegedly 0.399 mm, etc.
But early computer history is super Americentric so that's what technology uses. In the US, they standardized the point around the end of the 19th century. To what? I dunno.
This source
from 1900 gives the length of a point as 35/996 cm (72.281 points/in) and then says there are exactly 867.4699 "ems per foot" (72.289 points/in).
This source
from 1916 says the standard pica (12 points) is 0.16604 inches and that there are 72.272 "pica ems per foot". Which conveniently enough gives us 72.272 points/in (a pica being 12 points). Then on the very next page they say no a pica is actually 0.16604
4
inches and a point is exactly 0.013837 inches. I found other sources with other definitions, too.
I'm going to chalk the differences up to a mix of "the definitions of 'meter' and 'foot' changed over time" and "these are less than a micron apart so who gives a shit". I do, I give a shit. Regardless, the
official NIST definition
settled on a point being 0.013837 inches, so you'd get 72.27 points/inch.
Wrong! You absolute moron. You get 72.270001 points/inch. This annoyed Donald Knuth enough that he rejiggered the ratio in
TeX
(pg 58):
TEX’s “pt” has been made slightly larger than the official printer’s point, which was defined to equal exactly .013837 in by the American Typefounders Association in 1886 [cf. National Bureau of Standards Circular 570 (1956)]. In fact, one classical point is exactly .99999999 pt, so the “error” is essentially one part in 10^8. … The new definition 72.27 pt = 1 in is not only better for calculation, it is also easier to remember.
(To explain his motivation a little: American printers measure things in inches, and define the point in terms of inches. TeX measures things in points
, and define the inch in terms of points.)
For the record, NIST seems to think "72 points/inch" is a good enough approximation. TeX calls this the
bp
(big point).
AKA the Inkscape value
Now what about Inkscape? As far as I can tell, this comes from the Postscript format's definition of the
unit size
:
The length of a unit along the
x axis and along the y axis is 1/72 of an inch. We call this coordinate system
default user space
.
These features of default user space are chosen for their mathematical simplicity and convenience. The location and orientation of the axes follow common mathematical practice and cause all points within the current page to have positive x and y coordinate values. The unit size, 1/72 of an inch, is very close to the size of a printer's point (1/72.27 inch), which is a standard measuring unit used in the printing industry.
Later on
page 86
they straight up call 1/72 inch a "point".
Later editions
would clarify it's not actually a point and that points are stupid anyway:
Note: The default unit size (1/72 inch) is approximately the same as a “point,” a unit
widely used in the printing industry. It is not exactly the same as a point, however;
there is no universal definition of a point.
Apple shipped PostScript in their
LaserWriter
laser printer, other companies followed suite, making PostScript the de facto printing language and 72 points/in the standard digital measure. The W3 consortium used the same measure in
CSS
and
SVG
, Inkscape is an SVG editor, and that's all she wrote.
Epilog: Frink
Whenever I need to mess with units of measure, I turn to
Frink
. Frink is a Turing-complete language with
really
good unit of measure support:
oldinch := surveyfoot / 12 // pre 1959 inch 
35 cm / (996 pts) -> oldinch / pts
0.013834839357429718876
The author does also does incredibly thorough research on the history of units measurements. Here's what the
Frink data file
says about points:
point :=          0.013837ee0 inch    // exact, NIST Handbook 44, Appendix 3
printerspoint :=       point

texscaledpoint :=      1/65536 point    // The TeX typesetting system uses
texsp :=               texscaledpoint   // this for all computations.
computerpoint :=       1/72 inch        // The American point was rounded 
computerpica :=        12 computerpoint // to an even 1/72 inch by computer
postscriptpoint :=     computerpoint    // people at some point.
Well, now we know what that "some point" is!
Now we also know that the definitions of
texscaledpoint
is (
gasp
) wrong.
realtexpoint := 1/72.27 inch
realtexsp := 1/65536 realtexpoint
(realtexsp - texsp)
5.36285100578e-17 m (length)
(realtexsp - texsp) / realtexsp
1.0000000000005691827e-8
The Frink definition is off by about 50 attometers, or approximately 3% of the width of a proton.
