---
title: "Crabs, the bitmap terror!"
url: "https://research.swtch.com/crabs"
fetched_at: 2026-05-05T07:01:02.061881+00:00
source: "Russ Cox (research.swtch)"
tags: [blog, raw]
---

# Crabs, the bitmap terror!

Source: https://research.swtch.com/crabs

Crabs, the bitmap terror!
Russ Cox
January 9, 2008
research.swtch.com/crabs
Posted on Wednesday, January 9, 2008.
Today, window systems seem as inevitable as hierarchical file systems, a fundamental building block of computer systems.  But it wasn't always that way.  This paper could only have been written in the beginning, when everything about user interfaces was up for grabs.
A bitmap screen is a graphic universe where windows, cursors and icons live in harmony, cooperating with each other to achieve functionality and esthetics.  A lot of effort goes into making this universe consistent, the basic law being that every window is a self contained, protected world.  In particular, (1) a window shall not be affected by the internal activities of another window.  (2) A window shall not be affected by activities of the window system not concerning it directly, i.e. (2.1) it shall not notice being obscured (partially or totally) by other windows or obscuring (partially or totally) other windows, (2.2) it shall not see the
image
of the cursor sliding on its surface (it can only ask for its position).
Of course it is difficult to resist the temptation to break these rules.  Violations can be destructive or non-destructive, useful or pointless.  Useful non-destructive violations include programs printing out an image of the screen, or magnifying part of the screen in a
lens
window.  Useful destructive violations are represented by the
pen
program, which allows one to scribble on the screen.  Pointless non-destructive violations include a magnet program, where a moving picture of a magnet attracts the cursor, so that one has to continuously pull away from it to keep working.  The first pointless, destructive program we wrote was
crabs
.
As the crabs walk over the screen, they leave gray behind, “erasing” the apps underfoot:
For the rest of the story, see Luca Cardelli's “
Crabs: the bitmap terror!
” (6.7MB).  Additional details in “
Crabs (History and Screen Dumps)
” (57.1MB).
