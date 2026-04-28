---
title: "JJ LSP Follow Up"
url: "https://matklad.github.io/2026/03/05/jj-lsp-followup.html"
fetched_at: 2026-04-28T07:02:44.922806+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# JJ LSP Follow Up

Source: https://matklad.github.io/2026/03/05/jj-lsp-followup.html

JJ LSP Follow Up
Mar 5, 2026
In
Majjit LSP
, I described an idea of implementing
Magit
style UX for
jj
once
          and for all, leveraging LSP protocol. I’ve learned today that the
          upcoming 3.18 version of LSP has a feature to make this massively less
          hacky:
Text Document Content Request
LSP can now provide virtual documents, which aren’t actually
          materialized on disk. So this:
can now be such a virtual document, where highlighting is provided by
          semantic tokens, things like “check out this commit” are code actions,
          and “goto definition” jumps from the diff in the virtual file to a
          real file in the working tree.
Exciting!
