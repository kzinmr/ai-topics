---
title: "Updates to searchcode.com"
url: "https://boyter.org/2015/03/updates-searchcode-com/"
fetched_at: 2026-05-05T07:02:02.761624+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Updates to searchcode.com

Source: https://boyter.org/2015/03/updates-searchcode-com/

Updates to searchcode.com
2015/03/18
(286 words)
Just a quick post to list some updates to searchcode.com The first is a slight modification to the home page. A while ago I received an email from the excellent
Christian Moore
who provided some mock-ups of how he felt it should look. I loved the designs, but was busy working on other issues. Thankfully however in the last week or so I found the time to implement his ideas and the result is far more professional to me.
It certainly is a large change from the old view but one that I really like as it is very clean. The second update was based on some observations I had. I was watching a colleague use searchcode to try finding some logic inside the Thumbor image resizer project. I noticed that once he had the the file open he was trying to navigate to other files in the same project. Since the only way to do was was to perform a new search (perhaps with the repo option) I decided to add in a faster way to do this. For some projects there is now an instant search box above the code result which allows you to quickly search over all the code inside that repository. It uses the existing searchcode API’s (which you can use as well!) to do so. Other ways of doing this would include the project tree (another piece of functionality I would like to add) but this was done using already existing code so was very easy to implement. An example would be going to
this result in pypy
and searching for import.
As always I would love some feedback on this, but as always expecting none (par for the course).
