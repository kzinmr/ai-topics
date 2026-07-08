---
title: "github-code Web Component"
url: "https://simonwillison.net/2026/Jul/7/github-code-component/#atom-everything"
fetched_at: 2026-07-08T07:00:56.405052+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# github-code Web Component

Source: https://simonwillison.net/2026/Jul/7/github-code-component/#atom-everything

An experimental Web Component built using GPT-5.5 and
the following prompt
:
let's build a Web Component for embedding code from GitHub
<github-code href="https://github.com/simonw/sqlite-ast/blob/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py#L9-L18"></github-code>
It takes URLs like that, converts them to https://raw.githubusercontent.com/simonw/sqlite-ast/437c759129154f05296324a7f82aa1246340dd14/sqlite_ast/parser.py, then uses fetch() to fetch them and displays the specified range of lines - with line numbers, no syntax highlighting though
Show me a preview web browser so I can see your work
Here's what it looks like embedded on this page:
