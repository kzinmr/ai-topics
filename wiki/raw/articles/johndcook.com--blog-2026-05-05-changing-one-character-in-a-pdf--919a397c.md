---
title: "Changing one character in a PDF"
url: "https://www.johndcook.com/blog/2026/05/05/changing-one-character-in-a-pdf/"
fetched_at: 2026-05-06T07:01:09.183727+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Changing one character in a PDF

Source: https://www.johndcook.com/blog/2026/05/05/changing-one-character-in-a-pdf/

I saw a
post
on X saying
Changing a hyphen to an en-dash increases your PDF file size by ~10 bytes.
My first thought was that it had something to do with hyphen being an ASCII character and an en-dash not. Changing a hyphen to an en-dash would make a UTF-8 encoded text file a couple bytes longer. (See why
here
.) Maybe adding one non-ASCII character could cause the file to include a glyph it didn’t before.
I did a couple experiments. I made a minimal LaTeX file with only the text
See pages 9-10.
and another with
See pages 9--10.
(In LaTeX, a hyphen compiles to a hyphen and two hyphens compile to an en-dash.)
I compiled both files using
pdflatex
. The PDF with the hyphen was 13172 bytes and the one with the en-dash was 13099 bytes. Replacing the hyphen with the en-dash made the file 73 bytes
smaller
.
I repeated the experiment with a Libre Office ODT document. Changing the hyphen to an en-dash reduced the file size from 13548 bytes to 13514 bytes.
Then I went back to LaTeX and pasted a paragraph of lorem ipsum text into both files. Now the file with the hyphen produced a 18131 byte PDF and the file with the en-dash produced a 18203 byte PDF. So in this instance changing the hyphen to an en-dash
increased
the size of the file by 72 bytes.
After adding the lorem ipsum text to the ODT files, the PDF resulting from the file with the hyphen was 23 bytes larger, 17846 bytes versus 17823 bytes.
PDFs are complicated. Changing one character can make the file bigger or smaller, by an unpredictable amount. It depends, among other things, on what software was used to create the PDF. Even changing one letter in an all-ASCII text can change the size of the PDF, I suppose due to some internal text compression and aesthetic control characters. I don’t pretend to understand what’s going on inside a PDF.
Related posts
