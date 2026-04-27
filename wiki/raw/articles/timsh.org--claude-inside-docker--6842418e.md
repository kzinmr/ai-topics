---
title: "Switching to Claude Code + VSCode inside Docker"
url: "https://timsh.org/claude-inside-docker/"
fetched_at: 2026-04-27T07:57:26.823152+00:00
source: "timsh.org"
tags: [blog, raw]
---

# Switching to Claude Code + VSCode inside Docker

Source: https://timsh.org/claude-inside-docker/

Last night I finished a transition from my old AI coding setup I've been using for a while to running Claude Code in Docker using VSCode's "Dev Container" feature.
In this post I lay out a few of my thoughts on why I wanted to switch to something in the first place, and also a short guide for those who want to do the same.
If you are here just for the guide + code (a tiny single file), here it is:
https://github.com/tim-sha256/claude-in-docker
🥺
Important note!
I'm not a professional vibecoder (thanks god) and I don't generate AI code on 9-5 basis (meh)
I'm just a casual user occasionally getting help from llms on my projects, all of them being not corporate-serious-guys-enterprise-grade.
I'm not looking for the most advanced 100x dev tools or workflows, nor $100+ subscriptions whose token limits I'll probably only reach once a year on a sleepless night.
Before and why
Until yesterday I've been using such setup:
ChatGPT Plus 20$ subscription for occasional chats mostly unrelated to code, except for quickies and desperate attempts to feed o3 a bunch of code that Claude can't crack and get it all solved (mostly unsuccessful).
Cursor Pro for additional 20$ (or how do they call it these days?) - for all "serious" coding.
Which works all right, is convenient (been stuck with Cursor since August '24 and GPT since '23 without actively seeking an alternative), but has a couple issues that started to bug me recently.
Issue 1: I'm greedy and I want my responses fast
Before Cursor went into drain-users stage recently, I did not use up all 500 requests / month not a single time while working on 1-2 projects during my free time (approx. 40-60 hours a month).
Maybe I could've paid less on token-based plan, but I didn't really care – $20 is $20 :)
But after their update removing the 500 requests limit "so you can enjoy unlimited requests to almost any model", I've been extremely upset by Cursor due to their inadequate rate limits.
Sometimes I would type a prompt for Sonnet 4 (not even Opus...) and wait for 2-5 minutes for anything to happen, which is a complaint I've seen quite a lot in Cursor-related chats and on Reddit.
There is an option to switch back to a proprietary and seemingly not as profitable 500 requests pricing mode, but I don't think it'll last much longer.  Or use the free version and go out for a smoke break after every request.
Which led me to think about my spending and the satisfaction I get in return: is it still worth 40$ or is there a better way?
Well, for now I've settled with Claude 20$ subscription and consider it a better fit for my use case for a couple of reasons:
$20 is less than 40$
I still get to send a pic of a shelf with various cleaning products to some chat app on my phone and ask "Which of these do I need to do X?", which works surprisingly well almost all the time
I have a similar-or-even-better web chat experience to work on stuff unrelated to code
Finally, and most importantly – I get Claude Code with:
reasonable limits
clear token spending indication
everybody constantly says Claude Code rocks, right?
I like cli stuff in general
vs code integration makes the IDE experience essentially the same (or even a bit better)
Ok, looks like I'm settled for now, end of story. Or what else?
Issue 2: I'm trying to be realistic about AI Agent security
Simply put: I believe running an AI Agent that has access to your entire file system, terminal and secrets is dangerous and will eventually lead to some problems.
Think of it as if you gave access to your computer to a cheap overseas freelance dev who you don't really know and can only chat with. How does that sound?
I stumble upon llm security-related stuff every day and occasionally read some of it. And generally, the situation is not getting better.
For instance, I've seen around 10 posts about very serious vulnerabilities in MCPs like
this one,
a few sad stories where cursor decided to delete something useful like all Ableton projects using
rm -rf
, and even threads saying that Claude
learned to bypass Cursor built-in command blacklist
in Yolo mode.
Basically, you have a choice: either accept each single command manually (which I think is a reasonable approach but I'm too lazy) or trust the above mentioned freelancer with everything you have and hope that some barriers will stop it and nothing bad will happen.
Or are there any other options?
Now and why
Ok, so I want to use Claude Code, but at the same time want to restrict it somehow so it can't fuck up my entire computer.
First idea which came to me turned to be the one that I'd go with (who could've thought): put that thing into a box with nothing but the project(s) in it, give it the least possible access and close the box.
In other words, launch Claude Code in Docker and work on the project inside the container.
What you get from that:
Claude can only access files from inside the container or in the provided volumes, mounted or not
It also most certainly can't break anything outside the container – worst case scenario is the container breaks and stops
Since the container has isolated environment, Claude doesn't have any access to your local secrets (like your SSH key) and won't be able to use any external integrations without you knowing and before you give it access
Ok, sounds cool. Is it easy to set up and use?
Yes! In fact, if you already have Docker and VSCode installed locally, it will take you around 5 minutes to get started.
Getting started (and finishing right away)
All right, here's what you'll need to have installed and set up in order to complete this short guide:
Docker and VSCode installed
Claude paid for (whatever plan works for you)
You use Github (not relevant for the basic setup)
Let's assume you have all of these and move on.
You'll need to create a folder that will serve as a root folder for both Claude and your project(s). Inside, you'll need to create a folder called
.devcontainer
, and inside of it a file
devcontainer.json
.
Copy the contents of
the file from Github
or just simply clone the repo I created and it will have both the needed structure and the file:
git clone https://github.com/tim-sha256/claude-in-docker.git
Open the root folder (
claude-in-docker
if you cloned the repo) in VSCode, and boom – this modal window should show up in the corner:
Click "Reopen in Container" and wait for some time. And that's it! You can check that Claude Code is installed by running
claude
command in the opened terminal:
Final touch
Since you're in an isolated environment, if you try to git clone / pull / push e.t.c you'll run into an error, since your container doesn't include any credentials and doesn't have access to your local SSH keys (if you use one of them for Github authentication locally).
First thing that comes to mind is to generate a separate SSH key inside of the container and add it to your account, but I decided to go the other way and use Fine-Grained access token.
Because you can't really control permissions of a specific SSH key, if you add a new one for the Claude environment, you'll probably give Claude a lot of permissions it shouldn't have – like viewing and editing your details, managing settings and so on.
After a brief googling session I found the option that suits my (and probably your) needs:
Go to
https://github.com/settings/personal-access-tokens/new
and create a new fine-grained token. Give it access to whichever repositories you want.
In the permissions settings, open the "Repository permissions" toggle, scroll to "Contents" and select "Read and write" access level.
This single permission is enough for basic git operations (clone / pull / push e.t.c) and you'll probably never need any additional permissions if you're not some git guru.
We're set – now select "Generate token" and copy it, store it securely, blah-blah, you know the drill.
Nice! Now Claude doesn't have an option of fucking up your GitHub account for fun. In order to add these credentials and use them in the future, you could simply clone some private repo you have access to by running this command:
git clone https://<USERNAME>:<TOKEN>@github.com/<USERNAME>/<REPO-NAME>.git
And then after cloning cd into the project folder and run this in order to save your credentials:
git remote set-url origin https://<USERNAME>:<TOKEN>@github.com/<USERNAME>/<REPO-NAME>.git
Hooray! You're all set to go and code with Claude, probably with lesser risks than before (or else why would you read this up until this point).
Conclusion
Thanks for reading! A couple notes:
I did not test 1001 different approaches and selected the best possible one. There might be a better (cheaper, more secure, yada-yada) way of doing this, though I thing this should be good enough for most people.
If you know what could be improved in this approach or guide – please consider leaving a comment below or emailing me at
[email protected]
.
