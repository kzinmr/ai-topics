---
title: "Death to px, long live ch!"
url: "https://shkspr.mobi/blog/2026/08/death-to-px-long-live-ch/"
fetched_at: 2026-08-24T10:32:20.730658+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Death to px, long live ch!

Source: https://shkspr.mobi/blog/2026/08/death-to-px-long-live-ch/

Pixels are a lie. Even if you think you're drawing something with "
pixel perfect
" accuracy, your monitor is lying to you. There is no grid of platonically perfect squares.
In CSS,
pixels are a double lie
:
Note that
1px
doesn't necessarily equal one physical device pixel. On HD displays, it may span multiple physical pixels. Similarly,
1cm
in CSS often doesn't correspond to one hundredth of SI meter. On a large TV screen, it typically is longer than that. The lengths are perceptual:
16px
looks roughly the same on a phone, laptop, or TV screen at typical viewing distance.
This blog is primarily text based. I want the
width of the text to be readable
for the average human. So, rather than setting the main width to be a percentage of the screen, I set it based on character width using the
ch
unit - which
isn't exactly a character
but good enough for my purposes:
⧉
CSS
--width-content
:
min
(75ch, 100%);
main
{
max-width
:
var
(
--width-content
);
}
When it comes to padding and margins, the same is true. If I want a gap around an element, I want that gap to be in proportion to the text inside it.
For widths, it makes sense to re-use the
ch
unit. I want the gap to be in proportion to the text.
But for
height
, perhaps it doesn't make sense to express vertical distance on character width? In which case
the
ex
unit can be used
. It is the size of a typical lower-case letter.
Just like my idea to
eliminate CSS classes from my HTML
, it's possible to go too far with this. I haven't changed
every
reference from px to ch, I'm just experimenting to see if it works.
There's nothing wrong, immoral, or evil about using px - or any other measure unit. Using ch and ex fit with my particular proclivities.
