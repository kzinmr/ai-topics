---
title: "Tool: LaTeX renderer"
url: "https://simonwillison.net/2026/Oct/15/latex/"
fetched_at: 2026-10-17T10:05:40.514469+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Tool: LaTeX renderer

Source: https://simonwillison.net/2026/Oct/15/latex/

Inspired by Paul Ford and Aboard Foundary's new web app
Tiny Little Office
, which provides a suite of web app content editors (a Word Processor, Outliner, Presentation Builder, Spreadsheet, Calculator, Drawing Tool, Diagram Maker, Animator, Calendar, and Trip Planner).
Tiny Little Office's signature trick is to store all of the document data in the
#fragment
section of the URL, so every document created using it becomes a bookmarkable and shareable link.
It also has
an llms.txt file
telling agents how to construct URLs that will render as documents. Claude
used that file
to generate
this link to a deck
that explains how the URL format works:
Tiny Little Office inspired me
to have Claude Code
(Opus 5.5 Extra) build a similar tool that works with LaTeX. Here's the sequence of prompts I used:
I want a tool where you can link to it with a fragment hash #code-here and it treats that code as LaTeX and renders it really effectively. It should also support a prefix which means the latex is compressed with a custom compression dictionary optimized for latex. Use the best available latex render library from a CDN (consider WebAssembly too). If loaded without a fragment hash show an editor you can paste latex into and then toggle to a "rendered" view. That rendered view should be bookmarkable. The #fragment view should let you switch to edit source too.
Since it was working in
my tools repo
I told it to take inspiration from the
<iframe sandbox="...">
mechanism used by my existing
SVG in Markdown tool
as protection against XSS risks:
Safe from XSS? We could run in an iframe sandbox like we do on the SVG markdown render project
I had it copy the Gist/URL loading feature from that tool as well:
We should have an option to load latex from a URL (or gist) similar to the markdown SVG tool
Here's
an example link
. The tool uses
Pako 2.1.0
,
MathJax 4.1.3
,
faster-latex 0.3.1
, and
DOMPurify 3.4.16
.
