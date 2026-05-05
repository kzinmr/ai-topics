---
title: "searchcode now supports regex code search"
url: "https://boyter.org/2011/12/searchcode-now-supports-regex-code-search/"
fetched_at: 2026-05-05T07:02:06.072794+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# searchcode now supports regex code search

Source: https://boyter.org/2011/12/searchcode-now-supports-regex-code-search/

searchcode now supports regex code search
2011/12/17
(284 words)
searchcode updates now supports regex code search
Similar to the soon to be defunt Google Code Search you can now search over 1 billion lines of code from github, bitbucket, sourceforge, google code and codeplex on searchcode. All you need do it search using a regex such as
/[cb]at/
or
/a{1,5}/
etc… You can filter by file extension as well using ext:[FILETYPE] EG, [/print_r/ ext:php][3] The only catch is due to constraints you can only do prefix regex not infix. Essentially this means the following search /lisp*/ will work as expected but /*lisp/ may not. The reason for this is that I am a single founder without funding and resources are finite. Assuming there is a demand for these features I can ramp up pretty quickly however (just a few config changes). Some searches such as [/[a-z]/][4] will take a while to return initially as the system warms up. You can see a lot more examples on the [features][5] page.
A few other things that have been improved are listed below.
Programming functions documentation and cleaned up some broken links. All the iOS and OSX documentation links are still broken due to Apple changing around their site, but I have left them in there anyway.
searchcode has been on a diet and is now lean fit and buff. It should be much faster to search across the board. There is a new look to go with it as well.
Multiple bug fixes which have been hanging around for a while.
Modified backend to remove duplicate code and make things far more modular.
Anyway have a spin and let me know what you think in the comments below.
[3]:
http://searchco.de/?q=/print_r/
ext:php
[4]:
http://searchco.de/?q=/[a-z]/
[5]:
http://searchco.de/features/
