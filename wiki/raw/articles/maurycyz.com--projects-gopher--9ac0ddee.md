---
title: "GopherTree (Maurycy's blog)"
url: "https://maurycyz.com/projects/gopher/"
fetched_at: 2026-05-01T07:01:59.281084+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# GopherTree (Maurycy's blog)

Source: https://maurycyz.com/projects/gopher/

GopherTree
2026-04-01
(
Programming
)
While gopher is usually seen as a proto-web, it's really closer to FTP.

It has no markup format, no links and no URLs.
Files are arranged in a hierarchically, and can be in any format.
This rigid structure allows clients to get creative with how it's displayed
...
which is why I'm extremely disappointed that everyone renders gopher menus like shitty websites:
You see all that text mixed into the menu?
Those are informational selectors: a non-standard feature that's often used to recreate hypertext.
I know this "limited web" aesthetic appeals to certain circles, but it removes the things that make the protocol interesting.
It would be nice to display gopher menus like what they are, a directory tree
:
This makes it easy to browse collections of files, and help avoid the Wikipedia problem:
Absentmindedly clicking links until you realize it's 3 AM and you have a thousand tabs open...
and that you never finished what you wanted to read in the first place.
I've made the decision to hide informational selectors by default
.
These have two main uses: creating faux hypertext and adding ASCII art banners.
ASCII art banners are simply annoying:
Having one in each menu looks cute in a web browser, but having 50 copies cluttering up the directory tree is... not great.
Hypertext doesn't work well. 
In the strict sense, looking ugly is better then not working at all —
but almost everyone who does this also hosts on the web, so it's not a huge loss.
If you do find a server that uses them reasonably, they can be renabled with a keyboard shortcut.
The client also has a built in text viewer
, with pagination and proper word-wrap.
It supports both UTF-8 and Latin-1 text encodings, but this has to be selected manually:
gopher has no mechanism to indicate encoding.
(but most text looks the same in both)
Bookmarks
work by writing items to a locally stored gopher menu, which also serves as a "homepage" of sorts.
Because it's just a file, I didn't bother implementing any advanced editing features:
any text editor works fine for that.
The bookmark code is UNIX/Linux specific, but porting should be possible.
All this fits within a thousand lines of C code
, the same as my ultra-minimal web browser.
While arguably a browser, it was practically unusable: lacking basic features like a back button or pagination.
The gopher version of the same size is complete enough to replace Lynx as my preferred client.
Usage instructions can be found at the top of the source file.
Related:
