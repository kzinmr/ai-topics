---
title: "Markdown SVG upgrades"
url: "https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/"
fetched_at: 2026-08-17T10:30:54.454634+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Markdown SVG upgrades

Source: https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/

16th August 2026
I started building my
markdown-svg-renderer
tool
in May
, but I've since added enough features to it that it's worth talking about here again.
It's evolved into my ideal tool for sharing Markdown transcripts that include SVG documents. Given my
proclivity for drawing pelicans riding bicycles
this is a problem that I needed to solve!
The tool is very simple. Navigate to
markdown-svg-renderer
in your browser and paste in some Markdown to see it rendered... or save that Markdown to a CORS-friendly URL or a GitHub Gist and paste in a URL to that document.
The URL option will give you a bookmarkable page, for example
https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6f9e48293be5c916652d29f0dc0b0657
- which bakes in the URL to
this Gist
.
If you visit
the Gist
you'll see raw SVG:
In the rendered tool that
looks like this
instead:
As you can see, that SVG block in the Markdown has been transformed into a rendered SVG (in this case animated) plus several tabs.
The tabs are the really fun bit. The PNG and JPEG tabs render that SVG to those image formats in the browser and lets you copy or download them - useful for sharing on platforms that don't support SVG directly.
The MP4 tab is
new today
- it examines the SVG to see if it contains any animations, attempts to guess how long the looped video should be, then renders a whole bunch of frames of the animation and loads 30+MB of
ffmpeg.wasm
so it can compile those frames into an MP4 video using the full power of FFMPEG compiled to WebAssembly and running in the browser.
Being able to turn an animated SVG into a MP4 again makes it easy to share on platforms that can't support SVG animation natively. It's a neat trick!
