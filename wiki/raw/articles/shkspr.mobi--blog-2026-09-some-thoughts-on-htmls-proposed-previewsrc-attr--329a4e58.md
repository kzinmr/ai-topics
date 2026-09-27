---
title: "Some thoughts on HTML’s proposed previewsrc attribute"
url: "https://shkspr.mobi/blog/2026/09/some-thoughts-on-htmls-proposed-previewsrc-attribute/"
fetched_at: 2026-09-25T10:01:25.691202+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Some thoughts on HTML’s proposed previewsrc attribute

Source: https://shkspr.mobi/blog/2026/09/some-thoughts-on-htmls-proposed-previewsrc-attribute/

One of the great things about modern HTML is that it tries to standardise stuff that developers are already doing. If there are a myriad ways of, for example, loading video onto a page - then browsers and other interested parties should work out how to make a standard
<video>
element.
An interesting new proposal has been brought forth by Microsoft. There are a dozen ways to show a preview of an
<img>
element before the
src=
attribute has loaded. So why not standardise on
previewsrc=
? There's an
excellent explainer on Patrick Brosset's blog
.
I instinctively like the idea - if only to simplify source code and reduce JS usage. But I do have some concerns which
I've shared with the team
.
This is the thing I always bang on about when I'm discussing standards. Additions to HTML should primarily benefit end users, not developers.
Do end users want this? Is there a bunch of research that shows normal people are confused that they don't see a preview image? Do they recoil in fear and distress while waiting for a full resolution picture to appear?
When people see a blurry or blocky image, do they understand that they need to wait for the full thing - or do they assume their computer is broken?
Microsoft has a bazillion dollars - it can afford to spend a few thousand on interviewing some real users and mapping out what they're likely to want from this.
I begrudgingly admit that developers need love too.
What are the pain points of the current implementations? Is it hard to dynamically generate multiple images? Is the syntax hard to use? Do blurs slow down the page?
Again, MS needs to pony up some cash to talk to developers. At the very least run a survey of all existing websites in the BING! database and see what they use.
When an image doesn't load, or loads slowly, a user will normally be shown some alt text - like this:
Is that more or less useful than this?
Accessibility isn't just for people with visual impairments!  This is
an issue I've raised with them
.
I've written before about
the usability of HTML elements
. Some of the newer ones like
<picture>
have very poorly named attributes in my opinion.
One alternative for
previewsrc
is
poster
. That would match with the
poster
attribute on the
<video>
element. They both show a preview image before the main content is loaded.
Given their functionality is identical, I think it makes sense for them to have the same name. You wouldn't expect to see
<video horizontal="1920" vertical="1080">
would you? No. That's why they use the same
width
and
height
attributes as images.
There are
several interesting objections and discussions on the GitHub repo
. I'm delighted that this is being talked about in the open, rather than just being presented as a
fait accompli
(remember
the toast proposal
?).
As I said, I genuinely think that there's a useful idea in here. But after writing all of this, I
think
it would be better and simpler for developers to use progressive images rather than overload HTML with a new attribute.
If website owners can't be bothered to save progressive images, I don't see why they'd bother to create a separate preview image.
Keeping preview images in sync with their full images is also likely to be a problem.
If you think I'm wrong,
read the explainer and then chat with Microsoft
.
