---
title: "Inline rendering with document​.currentScript"
url: "https://simonwillison.net/2026/Oct/17/document-currentscript/"
fetched_at: 2026-10-18T10:01:01.116217+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Inline rendering with document​.currentScript

Source: https://simonwillison.net/2026/Oct/17/document-currentscript/

17th October 2026 - Link Blog
Inline rendering with document​.currentScript
. Lean Rada describes a neat trick that takes advantage of the
document.currentScript
property. You can use that to drop in a tiny inline
<script>
element that replaces itself when the page loads:
The year is <script>
document.currentScript.replaceWith(
  new Date().getFullYear())</script>
If you define a shortcut function like this:
$=(...n)=>document.currentScript.replaceWith(...n)
You get a tiny template language:
The year is <script>$(new Date().getFullYear())</script>
