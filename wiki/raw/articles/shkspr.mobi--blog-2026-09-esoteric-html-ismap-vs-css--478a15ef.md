---
title: "Esoteric HTML - ismap vs CSS"
url: "https://shkspr.mobi/blog/2026/09/esoteric-html-ismap-vs-css/"
fetched_at: 2026-09-15T10:01:20.196623+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Esoteric HTML - ismap vs CSS

Source: https://shkspr.mobi/blog/2026/09/esoteric-html-ismap-vs-css/

The HTML specification is old and, while there is beauty in longevity, there's an inevitable build-up of boondoggles and baggage. Some elements like
<marquee>
have sadly been consigned to the dustbin of history - but there are still vestigial attributes just waiting to trip up the unwary.
If you're young, you may never have heard of Image Maps. Back in the bad-old-days, there weren't many good options for laying out a pixel-perfect HTML page. One option was to draw your website in an image editor, load it into a website
as an image
, and then make certain areas of the image clickable.
One way to do this was to add the attribute
ismap
. It is
only
valid on
<img>
elements which are inside an
<a href=…>
element. Like so:
Copied HTML to 📋
⧉
HTML
<
a
href
="click.php">
    <
img
ismap
src
="img.png"
width
="100"
height
="100">
</
a
>
When you click on that image, you don't go to
click.php
- instead you go to
click.php?12,34
where the two numbers represent the X and Y coordinates of
where
on the image you clicked. That's brilliant! Your server knows the size of the image - so if you click on the top half it can take you to one place, and if you click in the lower left corner you can go to another.
Brilliant!
Except, of course, there's a catch!
The
specification of the
<img>
element
is a little obtuse. Merely saying:
The ismap attribute […] indicates by its presence that the element provides access to a server-side image map. This affects how events are handled on the corresponding a element.
Instead, the details are in
4.6.2 Links created by a and area elements
:
set x to the distance in CSS pixels from the left edge of the image to the location of the click, and set y to the distance in CSS pixels from the top edge of the image to the location of the click.
Did you notice the gotcha?
the distance in CSS pixels
This is
not
based on the actual size of the image! It is based on the layout
Let's suppose you have an image which is 100 x 100 pixels. It is added to the website like this:
<img src="100.png" width="100" height="100" ismap>
Click on this image and you'll see that your X and Y positions are based on the natural size of the image.
But suppose you change the HTML to this:
<img src="100.png" width="500" height="20" ismap>
When you click on the image, the X & Y positions are
not
based on the actual size of the image; they're based on its layout size.
Suppose you use CSS to resize the image:
<img src="100.png" width="100" height="100" ismap style="width:7em;height:30ch">
The X and Y aren't based on the image's natural size, nor their declared height and width. Instead they're based on the size on screen determined by CSS.
And, of course, that's not necessarily
your
CSS! If the user has turned off style sheets, supplied their own, or uses an accessibility tool - the CSS size of the image might be
vastly
different from what you intended.
If you have an image 100 pixels wide and you want people clicking on the left half to go to a different location to the people clicking on the right half, you might have server-side code which says:
Copied  to 📋
⧉
if X < 50 :
    return page1.html
else
    return page2.html
But if the CSS has stretched, shrunk, skewed, or distorted the image then you have
no way of knowing
where the user clicked.
As far as I can tell, this behaviour is the same in all major browsers.
Basically, what I'm saying is, don't use
ismap
unless you're absolutely sure that there will be no CSS shenanigans. Even then, it probably isn't worth the risk.
