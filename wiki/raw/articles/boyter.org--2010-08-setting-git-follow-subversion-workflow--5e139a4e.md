---
title: "Setting up GIT to use a Subversion (SVN) style workflow"
url: "https://boyter.org/2010/08/setting-git-follow-subversion-workflow/"
fetched_at: 2026-05-05T07:02:07.873474+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Setting up GIT to use a Subversion (SVN) style workflow

Source: https://boyter.org/2010/08/setting-git-follow-subversion-workflow/

Moving from Subversion SVN to GIT can be a little confusing at first. I think the biggest thing I noticed was that GIT doesn’t have a specific work-flow; you have to pick your own. Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too. Since it took a while to set up I thought I would throw up a blog post on how to do it.
First on your server or wherever you are going to host your repository you need to create a bare repository. I created a new user on my server called repo which holds all of my repositories. I then created a directory which would hold my repository. This is similar to naming your repository in subversion.
$pwd
/home/repo
$mkdir newrepository
I then change directory into the newly created directory and create a git bare repository.
$cd newrepository
$git --bare init
Initialized empty Git repository in /home/repo/newrepository/
This creates an git bare repository which has no branches (not even master!). You can now log-off your server and from your client clone the repository. I use SSH for this, but you can clone in any other way you choose.
$git clone ssh://repo@servername/home/repo/newrepository
repo@servername's password:
warning: You appear to have cloned an empty repository.
Now that we have our repository cloned, the next thing to do is add whatever files you want have source control on, and then push them.
$git add .
$git commit -a -m 'Inital Commit'
$git push
repo@servername's password:
No refs in common and none specified; doing nothing.
Perhaps you should specify a branch such as 'master'.
Whoops. What went wrong there? Remember I said when you create a bare repository it dosnt even have branches? You need to push your master branch up to create it. Run the following.
$git push origin master
repo@servername's password:
Counting objects: 3, done.
Writing objects: 100% (3/3), 219 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To ssh://repo@servername/home/repo/newrepository
    * [new branch]      master -> master
$
Done. Everything you wanted to commit will be pushed up and you are set to go. Now this and any other machine you are working on can clone as per normal and start taking advantage of fast local branches.
