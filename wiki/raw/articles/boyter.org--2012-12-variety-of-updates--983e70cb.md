---
title: "Variety of Updates"
url: "https://boyter.org/2012/12/variety-of-updates/"
fetched_at: 2026-05-05T07:02:05.354447+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Variety of Updates

Source: https://boyter.org/2012/12/variety-of-updates/

A variety of updates have just rolled out. Firstly there is the new look and feel which I am actually proud of. The website looks far better, which wasn’t hard considering how awful it looked before. The other update is that documentation and code results are mixed together now. An example of this would be the search for
mysql_query
which displays the PHP reference which has mysql_query in it above the code results.
Other updates include that when you do perform a search like the above searchcode will suggest Language filters on the sidebar which you can click to restrict to a specific language. With
100+ languages
recognised this can really help you restrict things down.
Finally I was request by
Pádraig Brady
to include the
full fedora source code
into searchcode (that’s a mouthful). This is now live and you can search across fedora like the below
irq_create_mapping url:fedora
Of course I couldn’t just limit it to fedora, and so I added the following as well,
Finally I have bumped up the size of the code that’s indexed. It previously would only allow about 2000 lines of code to be indexed per file. I bumped the size up about 15x which should suit pretty much every code file, and have kicked off a full index refresh.
