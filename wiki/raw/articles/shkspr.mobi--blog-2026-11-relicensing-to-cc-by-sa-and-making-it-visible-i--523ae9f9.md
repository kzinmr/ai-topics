---
title: "Relicensing to CC BY-SA and making it visible in Schema metadata"
url: "https://shkspr.mobi/blog/2026/11/relicensing-to-cc-by-sa-and-making-it-visible-in-schema-metadata/"
fetched_at: 2026-11-22T10:01:12.195155+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Relicensing to CC BY-SA and making it visible in Schema metadata

Source: https://shkspr.mobi/blog/2026/11/relicensing-to-cc-by-sa-and-making-it-visible-in-schema-metadata/

How do you make it clear what copyright licence a blog post uses? I know in our wonderful AI-powered future that copyright and copyleft are but a distant memory. But some of us still believe it's worth making these things clear to both men and machines.
The first port of call is the page's metadata. Using the
rel
attribute
. Placing something like this in your page's
<head>
indicates that the copyright information can be found at a specific URl.
Copied HTML to 📋
⧉
HTML
<
link
rel
="license"
href
="https://example.com/copyright">
But that's not overly specific. Someone (or some
thing
) has to visit that website and then interpret what it says. How about we use some fancy
Schema.org
metadata to make things slightly clearer?
Here's a minimum viable example you can
paste into the validator
:
Copied HTML to 📋
⧉
HTML
<
body
itemscope
itemtype
=https://schema.org/Blog>
    <
main
itemprop
=blogPost itemscope
itemtype
=https://schema.org/BlogPosting>
        <
article
>
            <
span
itemprop
="author copyrightHolder"
                  itemscope
itemtype
=https://schema.org/Person>
                <
span
itemprop
=name>Terence Eden</
span
>
            </
span
>
            <
a
href
=https://shkspr.mobi/blog/copyright-and-copyleft/
itemprop
=license>
                <
img
alt
="🄯 CC BY-SA"
content
="Creative Commons Attribution ShareAlike"
itemprop
=copyrightNotice
src
="https://example.com/cc-by-sa.svg">
            </
a
>
That says this website is a blog. The
<main>
element is a blog post. The article has an author who is also the copyright holder (they may be two different entities). The link is to the licence URl. The image shows the copyright notice with human readable text also available.
It looks like this to a machine:
This sort of structure will allow you to assign different copyright and copyleft licences to different parts of the same page.
In other news, this blog is now CC BY-SA!
