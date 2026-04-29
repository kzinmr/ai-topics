---
title: "Accessing Fork Commits via Original Repository"
url: "https://susam.net/fork-commits-via-original-repo.html"
fetched_at: 2026-04-29T07:01:02.777897+00:00
source: "susam.net"
tags: [blog, raw]
---

# Accessing Fork Commits via Original Repository

Source: https://susam.net/fork-commits-via-original-repo.html

Accessing Fork Commits via Original Repository
By
Susam Pal
on 28 Mar 2026
I ran a small experiment with Git hosting behaviour using two demo
  repositories:
cuppa
: The original repository.
muppa
: Fork of
cuppa
with questionable changes.
Here is a table with links to these repositories on Codeberg and
  GitHub:
It is well known that GitHub lets us access a commit that exists
  only on the fork via the original repository using a direct commit
  URL.  I wanted to find out if Codeberg behaves the same.
The commit
f79ef5a
exists only on the fork
  (
muppa
) but not on the original repo
  (
cuppa
).  Let us see how the two hosting services
  handle direct URLs to this commit.
If we look at the second row, both commit URLs for Codeberg and
  GitHub work because that is where the commit was actually created.
  The commit belongs to the fork named
muppa
.
Now if we look at the first row, the commit URL for Codeberg returns
  a 404 page.  This reflects the fact that the
  commit
f79ef5a
does not exist on
cuppa
.
  However, GitHub returns a successful response and shows the commit.
  It shows the following warning at the top:
This commit does not belong to any branch on this repository, and
  may belong to a fork outside of the repository.
There is no particular point to this experiment.
  I just wanted to know.
