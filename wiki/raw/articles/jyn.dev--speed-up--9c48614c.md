---
title: "Speed Up!"
url: "https://jyn.dev/speed-up/"
fetched_at: 2026-04-28T07:02:52.140580+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Speed Up!

Source: https://jyn.dev/speed-up/

Good news! As of
today
,
my site now takes less than a tenth of the time to load.
I found an excellent
site
which tests page load speeds.
It told me that my site (which is mostly static pages)
was taking a full 4.3 seconds to load.
I was very confused by this - I don't have any large pages that I'm aware of;
the
CSS
is
minified
and there's almost no JavaScript.
It turns out that the nifty DNSSEC testers I'd put in
the other day
were taking a second each to load.
Now, a second doesn't sound like a lot, but it makes a
big difference
to how users perceive the site. 3.5 seconds - the speed up I've since gotten -
is an eternity on the web.
Honestly, I feel a lot more comfortable without the DNSSEC testers.
They always felt suspiciously like analytics (which I firmly oppose),
even though I didn't see the results.
The site is now at 223 milliseconds per load and counting.
The slowest things still present are Open Sans (loaded from Google fonts, nearly half the load time)
and the second DNS tester.
However, I've been told the site looks a lot nicer than before, so I'm loath to remove the nice fonts.
If I were self-hosting, I could fix this with caching, but I unfortunately don't control GitHub's servers.
Let me know if you have any suggestions!
Appendix
