---
title: "Multiple URLs in Git Remote"
url: "https://susam.net/multiple-urls-in-git-remote.html"
fetched_at: 2026-05-01T07:13:06.099174+00:00
source: "susam.net"
tags: [blog, raw]
---

# Multiple URLs in Git Remote

Source: https://susam.net/multiple-urls-in-git-remote.html

Multiple URLs in Git Remote
By
Susam Pal
on 29 Apr 2026
Typically a Git remote contains a single URL.  For example, when we
  clone a repository, a remote named
origin
is
  automatically created and its URL is set to the location of the
  upstream repository.  For example:
$
git clone -q https://codeberg.org/spxy/spica.git && cd spica/
$
git remote -v
origin  https://codeberg.org/spxy/spica.git (fetch)
origin  https://codeberg.org/spxy/spica.git (push)
$
sed '/remote/,$!d' .git/config
[remote "origin"]
        url = https://codeberg.org/spxy/spica.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
        remote = origin
        merge = refs/heads/main
A perhaps less known detail is that we can set multiple URLs for a
  remote.  For example:
$
git remote set-url origin --add https://github.com/spxy/spica.git
$
git remote -v
origin  https://codeberg.org/spxy/spica.git (fetch)
origin  https://codeberg.org/spxy/spica.git (push)
origin  https://github.com/spxy/spica.git (push)
$
sed '/remote/,$!d' .git/config
[remote "origin"]
        url = https://codeberg.org/spxy/spica.git
        fetch = +refs/heads/*:refs/remotes/origin/*
        url = https://github.com/spxy/spica.git
[branch "main"]
        remote = origin
        merge = refs/heads/main
As evident from the above output, with multiple URLs for the same
  remote, the first one becomes the fetch URL whereas all URLs become
  push URLs.  For example:
$
git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 327 bytes | 109.00 KiB/s, done.
From https://codeberg.org/spxy/spica
   d473dde..31db503  main       -> origin/main
Updating d473dde..31db503
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
$
git log --oneline
31db503 (HEAD -> main, origin/main, origin/HEAD) Explain that Spica is a binary star system
d473dde Create README.md
The output above confirms that the fetch was performed from the
  first remote URL.  Although the output shows that
origin
contains commit 31db503, it is possible
  that not all remote locations for
origin
have received
  this commit yet.  Since we have not configured a
pushurl
, pushes are sent to all remote URLs by default.
  For example:
$
echo 'It is about 250 light years away from the Sun.' >> README.md
$
git add README.md
$
git commit -m 'Mention distance from the Sun'
[main 816998d] Mention distance from the Sun
 1 file changed, 1 insertion(+)
$
git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 10 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 325 bytes | 325.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
To https://codeberg.org/spxy/spica.git
   31db503..816998d  main -> main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 10 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 791 bytes | 791.00 KiB/s, done.
Total 9 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/spxy/spica.git
 * [new branch]      main -> main
$
git log --oneline
816998d (HEAD -> main, origin/main, origin/HEAD) Mention distance from the Sun
31db503 Explain that Spica is a binary star system
d473dde Create README.md
A
pushurl
can be set as follows:
$
git remote set-url --push origin https://github.com/spxy/spica.git
$
git remote -v
origin  https://codeberg.org/spxy/spica.git (fetch)
origin  https://github.com/spxy/spica.git (push)
$
sed '/remote/,$!d' .git/config
[remote "origin"]
        url = https://codeberg.org/spxy/spica.git
        fetch = +refs/heads/*:refs/remotes/origin/*
        url = https://github.com/spxy/spica.git
        pushurl = https://github.com/spxy/spica.git
[branch "main"]
        remote = origin
        merge = refs/heads/main
When one or more
pushurl
locations are set, pushes are
  sent to only those locations.  Fetches continue to occur from the
  first URL as before.
$
echo 'Its two stars orbit each other roughly every four days.' >> README.md
$
git add README.md
$
git commit -m 'Mention the four-day orbital period'
[main 2e9f4e8] Mention the four-day orbital period
 1 file changed, 1 insertion(+)
$
git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 10 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 342 bytes | 342.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/spxy/spica.git
   816998d..2e9f4e8  main -> main
$
git log --oneline
2e9f4e8 (HEAD -> main, origin/main, origin/HEAD) Mention the four-day orbital period
816998d Mention distance from the Sun
31db503 Explain that Spica is a binary star system
d473dde Create README.md
Note that in this case, the new commit has been pushed only to the
  second remote URL.  If we perform a pull, Git will fetch changes
  from the first remote URL and will move
origin/main
back to the latest commit available there.  For example:
$
git pull
From https://codeberg.org/spxy/spica
 + 2e9f4e8...816998d main       -> origin/main  (forced update)
Already up to date.
$
git log --oneline
2e9f4e8 (HEAD -> main) Mention the four-day orbital period
816998d (origin/main, origin/HEAD) Mention distance from the Sun
31db503 Explain that Spica is a binary star system
d473dde Create README.md
For this reason, configuring a separate
pushurl
should
  be done with care.  It is useful only in a narrow range of scenarios
  such as fetching from a primary repository that we want to treat as
  read-only while pushing changes to a mirror.
The difference between
pushurl
and a normal remote URL
  is explained in
man git-fetch
as well as
man
  git-push
of Git 2.54.0 as follows:
The <pushurl> is used for pushes only.  It is optional and
  defaults to <URL>.  Pushing to a remote affects all defined
  pushurls or all defined urls if no pushurls are defined.  Fetch,
  however, will only fetch from the first defined url if multiple urls
  are defined.
