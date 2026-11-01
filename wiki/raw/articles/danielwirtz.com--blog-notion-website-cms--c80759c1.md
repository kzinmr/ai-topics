---
title: "Dynamic website CMS with Notion"
url: "https://danielwirtz.com/blog/notion-website-cms"
fetched_at: 2026-11-01T10:01:33.378229+00:00
source: "danielwirtz.com"
tags: [blog, raw]
---

# Dynamic website CMS with Notion

Source: https://danielwirtz.com/blog/notion-website-cms

Three years ago, I published the
first version of my current website
using Chakra UI, Next.js, and Airtable. One of the aspects I cherished most about my setup was implementing Airtable as the backend for pages like my reading tracker and tool page.
I also used Airtable for my blog, but while it’s amazing at managing data, it becomes cumbersome as a blogging backend. Primarily, because all the text editing has to happen in a single “Rich Text” field, which doesn’t provide a great writing experience or many features.
Since I hopelessly fell in love with a “no-code” backend, I turned my eyes to Notion as an alternative. What Airtable is for data, and Notion is for text. It’s much better suited for writing because it’s built around pages and blocks of content.
Reading a bit on Reddit, I found out about “Notion rendered” libraries like
react-notion-x
. Once I understood, that you can hand these libraries a page object (e.g. all blocks in a Notion page) and they render all the objects in the exact style of Notion, I was quickly sold.
There are a number of benefits I saw:
Notion’s default styling is already great, and I can easily tweak it
There are many text styles, such as
highlighting
,
code
, or
colored
text
Build-in components like Callout, Divider, Code blocks and Table of Contents
I can freely adjust the page layout, and it’s reflected in my blog article
And there is even a possibility to use tables, databases, and embeds!
So recently, I sat down to implement Notion on my blog, and so far, it has been great. It took some time to configure, but now it feels like a set-and-forget solution. I don’t need to touch the code—I can simply work in Notion to update my blog.
A few things I already like are that the Notion editor is designed for writing and provides a comfortable, distraction-free environment (plus, it has dark mode!). And Notion is also available on all platforms, allowing me to use it on all my devices from anywhere. The only exception is when I don’t have internet access, but I’ve read that
Notion is working on this
.
In addition to using it for my blog, I configured a second Notion database for general pages. When I add a new page to that database, it immediately appears on my root domain. This is useful for legal pages (see my
Privacy page
as an example). But in the future, it could also be beneficial for quickly showcasing projects and being able to quickly update them.
If you’re interested in how I implemented Notion, you can dig into the code on my website here:
