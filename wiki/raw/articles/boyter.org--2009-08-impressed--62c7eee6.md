---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2009/08/impressed/"
fetched_at: 2026-05-05T07:02:08.296908+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2009/08/impressed/

Impressed
2009/08/19
(76 words)
Was playing around with Python for a second there. I learnt about one of the new “multiprocessing” features. Its pretty standard stuff, but thankfully does what I actually wanted Python to always do. Allow me to multiprocess any Map function. Below is the sample code (2.6 and above only sorry).
from
multiprocessing
import
Pool
import
time
def
f
(x):
return
x
*
x
if
__name__
==
'__main__'
:
p
=
Pool(processes
=
2
)
r
=
range(
1
,
10000000
)
t
=
time
.
time()
p
.
map(f,r)
print time
.
time()
-
t
