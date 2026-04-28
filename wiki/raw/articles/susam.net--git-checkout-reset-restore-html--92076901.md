---
title: "Git Checkout, Reset and Restore"
url: "https://susam.net/git-checkout-reset-restore.html"
fetched_at: 2026-04-28T07:01:41.818855+00:00
source: "susam.net"
tags: [blog, raw]
---

# Git Checkout, Reset and Restore

Source: https://susam.net/git-checkout-reset-restore.html

Git Checkout, Reset and Restore
By
Susam Pal
on 12 Mar 2026
I have always used the
git checkout
and
git
  reset
commands to reset my working tree or index but since
  Git 2.23 there has been a
git restore
command available
  for these purposes.  In this post, I record how some of the 'older'
  commands I use map to the new ones.  Well, the new commands aren't
  exactly new since Git 2.23 was released in 2019, so this post is
  perhaps six years too late.  Even so, I want to write this down for
  future reference.  It is worth noting that the old and new commands
  are not always equivalent.  I'll talk more about this briefly as we
  discuss the commands.  However, they can be used to perform similar
  tasks.  Some of these tasks are discussed below.
Contents
Experimental Setup
To experiment quickly, we first create an example Git repository.
mkdir foo/; cd foo/; touch a b c
git init; git add a b c; git commit -m hello
Now we make changes to the files and stage some of the changes.  We
  then add more unstaged changes to one of the staged files.
date | tee a b c d; git add a b d; echo > b
At this point, the working tree and index look like this:
$
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
modified:   a
        modified:   b
        new file:   d
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
modified:   b
        modified:   c
File
a
has staged changes.  File
b
has
  both staged and unstaged changes.  File
c
has only
  unstaged changes.  File
d
is a new staged file.  In
  each experiment below, we will work with this setup.
All results discussed in this post were obtained using Git 2.47.3 on
  Debian 13.2 (Trixie).
Reset the Working Tree
As a reminder, we will always use the following command between
  experiments to ensure that we restore the experimental setup each
  time:
date | tee a b c d; git add a b d; echo > b
To discard the changes in the working tree and reset the files in
  the working tree from the index, I typically run:
git checkout .
However, the modern way to do this is to use the following command:
git restore .
Both commands leave the working tree and the index in the following
  state:
$
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
modified:   a
        modified:   b
        new file:   d
Both commands operate only on the working tree.  They do not alter
  the index.  Therefore the staged changes remain intact in the index.
Reset the Index
Another common situation is when we have staged some changes but
  want to unstage them.  First, we restore the experimental setup:
date | tee a b c d; git add a b d; echo > b
I normally run the following command to do so:
git reset
The modern way to do this is:
git restore -S .
Both commands leave the working tree and the index in the following
  state:
$
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
modified:   a
        modified:   b
        modified:   c
Untracked files:
  (use "git add <file>..." to include in what will be committed)
d
no changes added to commit (use "git add" and/or "git commit -a")
The
-S
(
--staged
) option tells
git
  restore
to operate on the index (not the working tree) and
  reset the index entries for the specified files to match the
  version in
HEAD
.  The unstaged changes remain intact as
  modified files in the working tree.  With the
-S
option, no changes are made to the working tree.
From the arguments we can see that the old and new commands are not
  exactly equivalent.  Without any arguments, the
git
  reset
command resets the entire index to
HEAD
,
  so all staged changes become unstaged.  Similarly, when we run
git restore -S
without specifying a commit, branch or
  tag using the
-s
(
--source
) option, it
  defaults to resetting the index from
HEAD
.
  The
.
at the end ensures that all paths under the
  current directory are affected.  When we run the command at the
  top-level directory of the repository, all paths are affected and
  the entire index gets reset.  As a result, both the old and the new
  commands accomplish the same result.
Reset the Working Tree and Index
Once again, we restore the experimental setup.
date | tee a b c d; git add a b d; echo > b
This time we not only want to unstage the changes but also discard
  the changes in the working tree.  In other words, we want to reset
  both the working tree and the index from
HEAD
.  This is
  a dangerous operation because any uncommitted changes discarded in
  this manner cannot be restored using Git.
git reset --hard
The modern way to do this is:
git restore -WS .
The working tree is now clean:
$
git status
On branch main
nothing to commit, working tree clean
The
-W
(
--worktree
) option makes the
  command operate on the working tree.  The
-S
(
--staged
) option resets the index as described in the
  previous section.  As a result, this command unstages any changes
  and discards any modifications in the working tree.
Note that when neither of these options is specified,
-W
is implied by default.  That's why the
  bare
git restore .
command in the previous section
  discards the changes in the working tree.
Summary
The following table summarises how the three pairs of commands
  discussed above affect the working tree and the index, assuming the
  commands are run at the top-level directory of a repository.
Old
New
Working Tree
Index
git checkout .
git restore .
Reset to match the index.
No change.
git reset
git restore -S .
No change.
Reset to match
HEAD
.
git reset --hard
git restore -SW .
Reset to match
HEAD
.
Reset to match
HEAD
.
The
git restore
command is meant to provide a clearer
  interface for resetting the working tree and the index.  I still use
  the older commands out of habit.  Perhaps I will adopt the new ones
  in another six years, but at least I have the mapping written down
  now.
