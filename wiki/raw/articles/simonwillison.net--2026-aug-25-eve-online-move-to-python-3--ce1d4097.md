---
title: "The Move to Python 3 Begins!"
url: "https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/"
fetched_at: 2026-08-26T10:00:59.569067+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# The Move to Python 3 Begins!

Source: https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/

25th August 2026 - Link Blog
EVE Online: The Move to Python 3 Begins!
(
via
) EVE Online has been one of the most interesting case studies in Python at scale for over twenty years now.
They've been running on
Stackless Python
since their launch in 2003, and their last major upgrade was 16 years ago, to Stackless Python 2.7
in 2010
.
Their upgrade to Python 3 will start using the
futurize
script against 2.4 million lines of code, followed by careful manual review of the ~20,000 places where Python 2 and 3 behavior differ - for example
1 / 2
is
0
in Python 2 but is
0.5
in Python 3.
There's nothing in this announcement about how they plan to replace Stackless, but at their conference last year they presented
Scheduling in Carbon: Leaving Stackless Python Behind
describing how they replaced Stackless in the Carbon engine for their more recent game EVE Frontier, using their (now open source)
carbonengine/scheduler
library.
