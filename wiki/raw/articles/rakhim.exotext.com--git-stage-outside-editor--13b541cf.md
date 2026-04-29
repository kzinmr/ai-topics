---
title: "Why I prefer to git stage outside of the editor or the terminal"
url: "https://rakhim.exotext.com/git-stage-outside-editor"
fetched_at: 2026-04-29T07:01:21.093093+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Why I prefer to git stage outside of the editor or the terminal

Source: https://rakhim.exotext.com/git-stage-outside-editor

Sublime Merge
is a fantastic Git client. I’ve been using it for years, even after switching from Sublime Text to VS Code.
VS Code has excellent built-in Git support, but I still prefer a dedicated app for staging files. Even when I used Neovim or Emacs (which has
Magit
, arguably the best Git client), I stuck with a separate tool for this step. Why?
Staging files is the last significant step in preparing a meaningful commit. It’s a moment for a preliminary self-review, an opportunity to catch issues before pushing changes. Doing this in the same editor where I’ve been writing code makes it harder to see things objectively. By the time I reach staging, I’ve been immersed in that view of the codebase for a while. A shift in presentation — simply by using a different app — helps me see the changes with fresh(er) eyes.
For the same reason, I prefer native browser-based views on GitHub and GitLab when reviewing other people’s merge requests. I like keeping "writing code" and "reading code" as distinct experiences.
