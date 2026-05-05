---
title: "The LLVM Project is Moving to GitHub"
url: "https://blog.llvm.org/2019/08/the-llvm-project-is-moving-to-github.html"
fetched_at: 2026-05-05T07:01:37.821211+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# The LLVM Project is Moving to GitHub

Source: https://blog.llvm.org/2019/08/the-llvm-project-is-moving-to-github.html

The LLVM Project is Moving to GitHub
The LLVM Project is Moving to GitHub
After several years of discussion and planning, the LLVM project is getting ready to complete the migration of its source code from SVN to GitHub!  At last year’s developer meeting, many interested community members convened at a series of round tables to lay out a plan to completely migrate LLVM source code from SVN to GitHub by the 2019 U.S. Developer’s Meeting.  We have made great progress over the last nine months and are on track to complete the migration on October 21, 2019.
As part of the migration to GitHub we are maintaining the ‘monorepo’ layout which currently exists in SVN.  This means that there will be a single git repository with one top-level directory for each LLVM sub-project.  This will be a change for those of you who are already using git and
accessing the code via the official sub-project git mirrors (e.g.
https://git.llvm.org/git/llvm.git
) where each sub-project has its own repository.
One of the first questions people ask when they hear about the GitHub plans is: Will the project start using GitHub pull requests and issues?  And the answer to that for now is: no. The current transition plan focuses on migrating only the source code. We will continue to use
Phabricator
for code reviews, and
bugzilla
for issue tracking after the migration is complete.  We have not ruled out using pull requests and issues at some point in the future, but these are discussions we still need to have as a community.
The most important takeaway from this post, though, is that if you consume the LLVM source code in any way, you need to take action now to migrate your workflows.  If you manage any continuous integration or other systems that need read-only access to the LLVM source code, you should begin pulling from the official
GitHub
repository instead of SVN or the current sub-project mirrors.  If you are a developer that needs to commit code, please use the
git-llvm
script for committing changes.
We have created a
status
page, if you want to track the current progress of the migration.  We will be posting updates to this page as we get closer to the completion date.  If you run into issues of any kind with GitHub you can file a bug in
bugzilla
and mark it as a blocker of the github tracking
bug
.
This entire process has been a large community effort.  Many many people have put in time discussing, planning, and implementing all the steps required to make this happen.  Thank you to everyone who has been involved and let’s keep working to make this migration a success.
Blog post by Tom Stellard.
