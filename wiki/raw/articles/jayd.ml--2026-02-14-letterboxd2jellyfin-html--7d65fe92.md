---
title: "letterboxd2jellyfin sync script"
url: "https://jayd.ml/2026/02/14/letterboxd2jellyfin.html"
fetched_at: 2026-04-29T07:02:13.309888+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# letterboxd2jellyfin sync script

Source: https://jayd.ml/2026/02/14/letterboxd2jellyfin.html

I have an incredibly niche use case where I
Have a physical media collection that I haven’t ripped
Would like to browse that collection in Jellyfin like its my own personal 
Netflix
Have a public list in Letterboxd of all the movies I own
So I wrote a
quick script
and
published it to pypi
.
Shout out to
letterboxdpy
that made
this incredibly simple.
This script reads the playlist from letterboxd and writes stub
.mp4
files in 
the appropriate Jellyfin file structure so you can browse it, eg
$
letterboxd2jellyfin
-o
'/path/to/jellyfin/library/Movies'
-url
https://letterboxd.com/matchup/list/scream-ranked/
parsing URL
Loading playlist
`
scream-ranked
`
from username
`
matchup
`
...
done
!
This playlist has 6 entries
creating stub file  deleteme/Scream
(
1996
)
/Scream
(
1996
)
.mp4
creating stub file  deleteme/Scream 4
(
2011
)
/Scream 4
(
2011
)
.mp4
creating stub file  deleteme/Scream 2
(
1997
)
/Scream 2
(
1997
)
.mp4
creating stub file  deleteme/Scream VI
(
2023
)
/Scream VI
(
2023
)
.mp4
creating stub file  deleteme/Scream
(
2022
)
/Scream
(
2022
)
.mp4
creating stub file  deleteme/Scream 3
(
2000
)
/Scream 3
(
2000
)
.mp4
all
done
!
Now obviously you can’t play this, it just plays a
cheeky stub of a video
,
but it is good enough to trick Jellyfin into showing all of the metadata. This
lets me doomscroll my own collection without having to walk over a few feet and
actually look at it, but also lets me sort and filter easily by actors.
This was also my first project using
uv
- it is indeed quite fast! Took me a 
while to figure out how to get those
.mp4
files embedded though. Turns out you
still have to opt in to the
uv build
backend even though that was what I was
trying to configure.
