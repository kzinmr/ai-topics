---
title: "My ramblings are available over gopher"
url: "https://maurycyz.com/misc/gopher/"
fetched_at: 2026-04-29T07:01:55.868621+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# My ramblings are available over gopher

Source: https://maurycyz.com/misc/gopher/

My ramblings are available over gopher
2026-04-01
(
Programming
)
It has recently come to my attention that people need a thousand lines of C code to read my website.
This is unacceptable.
For simpler clients, my server supports gopher:
#
telnet
maurycyz.com 70
/about.txt
--------------------[ About this site: ]---------------------
Publication date: 2026-02-03
Last updated:     2026-03-06


Yap, yap yap yap yap yap yap yap yap yap yap yap yap yap yap
yap yap yap yap yap yap yap yap yap yap yap yap yap. Yap yap
yap yap yap yap yap yap yap yap.
...
The response is just a text file: it has no markup, no links and no embedded content.
For navigation, gopher uses specially formatted directory-style menus:
#
telnet
maurycyz.com 70
/
0READ ME FIRST                     /gopherinfo.txt  maurycyz.com   70
i
1Files..........Programs           /programs.map    maurycyz.com   70
1               Rock photos        /misc/rocks.map  maurycyz.com   70
i
0Cool places....on the web         /real_pages.txt  maurycyz.com   70
1               on gopher          /gopherholes.map maurycyz.com   70
i
1Blog...........Projects           /projects/       maurycyz.com   70
1               Tutorials          /tutorials/      maurycyz.com   70
1               Other              /misc/           maurycyz.com   70
1               Photography        /astro/          maurycyz.com   70
.
The first character on a line indicates the type of the linked resource:
0
Plain text
1
Another directory
...
(stuff I don't use)
9
Binary data
I
Image
The type is followed by a tab-separated list containing a display name, file path, hostname and port.
Lines beginning with an "i" are purely informational and do not link to anything.
(This is non-standard, but widely used)
Storing metadata in links is weird to modern sensibilities
, but it keeps the protocol simple.
Menus are the only thing that the client has to understand:
there's no URLs, no headers, no mime types —
the only thing sent to the server is the selector (file path), and the only thing received is the file.
... as a bonus, this one liner can download files:
# 144 kB if you want to try it.
echo
/astro/m27/small.jpg
|
ncat
maurycyz.com
70
>
nebula.jpg
That's quite clunky
, but there are lots of programs that support it.
If you have Lynx installed, you should be able to just point it at this URL:
gopher://maurycyz.com
... although you will want to put
ASSUME_CHARSET:utf-8
in
/etc/lynx.cfg
because it's not 1991 anymore
[Citation Needed]
I could use informational lines to replicate the webs navigation
by making everything a menu —
but that would be against the spirit of the thing:
gopher is document retrieval protocol, not a hypertext format.
Instead, I converted all my blog posts in plain text and set up some directory-style navigation.
I've actually been moving away from using inline links anyways because they have two opposing design goals:
While reading, links must be normal text.
When you're done, links must be distinct clickable elements.
I've never been able to find a good compromise:
Links are always either distracting to the reader, annoying to find/click, or both.
Also,
to preempt all the emails
:
... what about
Gemini?
(The protocol, not the autocomplete from google.)
Gemini is the popular option for non-web publishing...
but honestly, it feels like someone took HTTP and slapped markdown on top of it.
This is a Gemini request...
gemini://example.com/about.gmi
... and this is an HTTP request:
GET
/about.html
HTTP/1.0
Host:
maurycyz.com
For both protocols, the server responds with metadata followed by hypertext.
It's true that HTTP is more verbose, but 16 extra bytes doesn't create a noticeable difference.
Unlike gopher, which has a unique navigation model and is of historical interest
,
Gemini is just the web but with limited features...
so what's the point?
I can already write websites that don't have ads or autoplaying videos,
and you can already use browsers that don't support features you don't like.
After stripping away all the fluff (CSS, JS, etc) the web is quite simple:
a functional browser can be put together in a weekend.
... and unlike gemini, doing so won't throw out 35 years of compatibility:
Someone with Chrome can read a barebones website, and someone with Lynx can read normal sites.
Gemini is a technical solution to an emotional problem
.
Most people have a bad taste for HTTP due to the experience of visiting a commercial website.
Gemini is the obvious choice for someone looking for "the web but without VC types".
It doesn't make any sense when I'm looking for an interesting (and humor­ously outdated) protocol.
Related:
