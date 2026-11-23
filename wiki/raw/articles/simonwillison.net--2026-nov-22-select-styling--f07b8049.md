---
title: "Select Styling Specimens"
url: "https://simonwillison.net/2026/Nov/22/select-styling/"
fetched_at: 2026-11-23T10:10:15.950420+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Select Styling Specimens

Source: https://simonwillison.net/2026/Nov/22/select-styling/

I got frustrated at how HTML
<select>
boxes default to looking different in different browsers, and are (I think) quite ugly in Chrome:
So I had Claude Fable 5.2
build
me
this page
showing all of the ways they can be styled:
Build an HTML page that shows all of the ways a select box can be styled, I plan to take screenshots in every desktop and mobile browser
After some experimentation I've decided my favorite CSS for select boxes is this:
select
{
appearance
:
none
;
color
:
#
1f2933
;
padding
:
0.5
em
2.25
em
0.5
em
0.75
em
;
border
:
1
px
solid
#
c4cbd3
;
border-radius
:
6
px
;
background
:
#
fff
url
(
"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5l5 5 5-5' fill='none' stroke='%23667085' stroke-width='1.5'/%3E%3C/svg%3E"
)
no-repeat right
0.75
em
center
/
0.75
em
;
}
Here's what that looks like in the three browsers:
