---
title: "Go install loop. The \"clang\" command requires the command line developer tools."
url: "https://boyter.org/posts/golang-the-clang-command-requires-command-line-developer-tools/"
fetched_at: 2026-05-05T07:01:56.475283+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Go install loop. The "clang" command requires the command line developer tools.

Source: https://boyter.org/posts/golang-the-clang-command-requires-command-line-developer-tools/

Recently on my M1 Macbook I ran into the following issue when trying to compile some Go code with C dependencies.
The “clang” command requires the command line developer tools.
Being a Mac this also prompted me with a button I could click to install them. Naturally I clicked it, only to be prompted with the following.
I can only assume that whoever wrote the Windows file copy dialog estimator now works at Apple as it gave me the following estimates one after another,
38 hours
41 mins
19 mins
32 mins
And then started installing about 2 minutes later.
Regardless this did not resolve the issue, and trying to run my
go build
failed again with the same repeated steps. Out of curiosity I tried it again, with a reboot and there was no change.
I have no idea as to the root cause of this, but the resolution was to run the following in the same command line,
xcodebuild -runFirstLaunch
Of course that makes sense. Please remind me how Mac’s just work again?
Posting this so I can have sympathy for future me, or perhaps save someone else a lot of effort.
