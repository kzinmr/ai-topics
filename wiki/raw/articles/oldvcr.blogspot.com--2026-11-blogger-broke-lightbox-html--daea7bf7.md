---
title: "Old Vintage Computing Research"
url: "https://oldvcr.blogspot.com/2026/11/blogger-broke-lightbox.html"
fetched_at: 2026-11-25T10:00:48.568162+00:00
source: "oldvcr.blogspot.com"
tags: [blog, raw]
---

# Old Vintage Computing Research

Source: https://oldvcr.blogspot.com/2026/11/blogger-broke-lightbox.html

[UPDATE: This has been
reported to Google
and now appears to be fixed.]
Some regular readers have alerted me to the fact that the Blogger lightbox for images isn't working. This is a photo-heavy blog, so that's a problem. Although I use a lightly modified basic theme, I did a test post with a current theme and it still didn't work, on Edge, Firefox, Safari and Chrome, so I don't think it's something I did. The offender appears to be, in the minified JS, a couple instances of things like
var Zp={}.getUniqueId("photofactoryservice");
which is of course nonsense because you can't get
blood
a function from a
turnip
empty object and I don't see an obvious proto that would provide it. I also looked at a few other blogs and they seem to be similarly affected, so I think this is global and the whole thing feels like a flubbed deploy that didn't get enough testing. In the meantime, you can right click on an image and open it in a new tab to see the larger version, or you can use the mobile view (append
?m=1
to the URL) which doesn't use the lightbox at all. Happy Thanksgiving, I guess.
