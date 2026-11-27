---
title: "OGP Image Format Support on Major Sites and Apps"
url: "https://shkspr.mobi/blog/2026/11/ogp-image-format-support-on-major-sites-and-apps/"
fetched_at: 2026-11-27T10:00:55.581333+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# OGP Image Format Support on Major Sites and Apps

Source: https://shkspr.mobi/blog/2026/11/ogp-image-format-support-on-major-sites-and-apps/

I've built a quick tool to see which image formats are supported on sites that allow Open Graph Protocol link previews.
As I've whinged about before,
Facebook have all-but abandoned their efforts to standardise OGP
. Which leads to a situation where a bunch of sites all have conflicting requirements on what they'll show. There's no easy way to find out which sites support which image formats, so I've done this manually.
I built
OGP Format Tester
to see whether social networking sites and apps supported modern formats like AVIF and JPEG-XL. Here are the results of my tests:
AVIF
GIF
JPEG
JXL
PNG
SVG
WEBP
Mastodon
❌
✅
✅
❌
✅
❌
✅
BlueSky
❌
✅
✅
❌
✅
❌
✅
Threads
✅
✅
✅
❌
✅
❌
✅
Facebook
✅
✅
✅
❌
✅
✅
✅
WhatsApp
❌
✅
✅
❌
✅
❌
✅
LinkedIn
❌
✅
✅
❌
✅
❌
✅
Signal
❌
✅
✅
❌
✅
❌
✅
Telegram
❌
✅
✅
❌
✅
❌
✅
Slack
❌
✅
✅
❌
✅
❌
✅
Discord
✅
❌
❌
❌
✅
❌
✅
Lemmy
✅
✅
✅
✅
✅
✅
✅
Teams
✅
✅
✅
❌
✅
❌
✅
Discourse
✅
✅
✅
✅
✅
❌
✅
There's a never ending parade of image formats - but these seven are the ones which seem best supported in all major browsers.
Similarly, I'm sorry if I haven't included your favourite site on here - feel free to leave the results in a comment.
I created a simple page like this:
Copied HTML to 📋
⧉
HTML
<!DOCTYPE html>
<
html
lang
="en-GB">
    <
head
>
        <
meta
charset
="UTF-8">
        <
title
>An OGP Image Test Site for WebP</
title
>
        <
meta
property
="og:type"
content
="website">
        <
meta
property
="og:locale"
content
="en_GB">
        <
meta
property
="og:site_name"
content
="OGP Site Name">
        <
meta
property
="og:title"
content
="OGP Title"> 
        <
meta
property
="og:description"
content
="Testing whether WEBP images are displayed in OGP">
        <
meta
property
="og:image"
content
="https://ogp.viii.fi/webp.webp">
        <
meta
property
="og:image:type"
content
="image/webp">
        <
meta
property
="og:image:width"
content
="800">
        <
meta
property
="og:image:height"
content
="600">
        <
meta
property
="og:image:alt"
content
="A WebP Image">
    </
head
>
That should contain all the metadata necessary for a site to display some preview text and an image.
I then pasted in a URl for each image format into each site. If a preview image came up, they got a tick. If not, a cross.
It's weird that Meta owned Facebook, WhatsApp, and Threads all have slightly different support, and I have no idea why Discord won't show (my?) JPEG previews.
Annoyingly, Facebook, Threads, and Discord are the only ones who support AVIF. JPEG-XL is still a distant dream for most.
Perhaps one day the promise of Web 2.0 will be fully realised and sites will be interoperable with each other.
If you want to test these yourself, you can use the following URls:
Copied  to 📋
⧉
https://ogp.viii.fi/ogp.php?format=AVIF
https://ogp.viii.fi/ogp.php?format=GIF
https://ogp.viii.fi/ogp.php?format=JPEG
https://ogp.viii.fi/ogp.php?format=JXL
https://ogp.viii.fi/ogp.php?format=PNG
https://ogp.viii.fi/ogp.php?format=SVG
https://ogp.viii.fi/ogp.php?format=WEBP
