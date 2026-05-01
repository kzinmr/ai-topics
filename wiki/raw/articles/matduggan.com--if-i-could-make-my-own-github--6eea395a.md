---
title: "Untitled"
url: "https://matduggan.com/if-i-could-make-my-own-github/"
fetched_at: 2026-05-01T07:13:05.000865+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/if-i-could-make-my-own-github/

My friend and I have a game where we talk about what we'd do if we were rich. Not rich like 'paid off the mortgage' rich. Rich like a man who owns a submarine he's never been inside. Rich like a man whose third wife has a skincare line. Tech-titan rich — the kind of money that buys you a compound in Wyoming and the confidence to wear the same gray t-shirt to congressional testimony."
One of mine, for a long time, has been the dream of making a new forge. I was prompted to write this after reading the good post about
Ghostty leaving GitHub
but it's something I've written and talked about for a few years. Given how bad GitHub has become at its core job, it seemed like a fun opportunity to try and write up what my billionaire folly of a forge would look like. This folly would have less penile rockets filled with aging celebrities.
What are the problems with modern forges?
GitHub, GitLab and Gitea (those being the 3 I've used the most) are all modeled on effectively the same design. There are differences, but you can tell that GitHub sets the pattern for the industry and then those features are ported over to the other two with varying levels of success. The issue with all of these is that they're designed to add things git doesn't do that you need.
Git is great at what it is designed to do, but what it is designed to do
isn't the way
most people are using it. Git is a perfect tool for kernel development. It is a decentralized distributed version control system that relies on the idea of patches being sent to maintainers over email. You trust those maintainers to
maintain
their sections and merge in the stuff that makes sense and not merge in the other stuff. It's a pretty high trust environment that places very few restrictions on how online a specific contributor is or what system they are using. If you have a laptop from 2010 that connects to the Internet once a week you can still be a meaningful contributor to a project with these workflows. .
However, in most jobs, git is effectively just the way I pull and push from a centralized repository stored in a forge. All the important stuff happens inside the forge, and very little of it happens on my client. Pull Requests are how I enforce the four-eyes principle, GitHub Actions are how I run my tests and linting on those Pull Requests to ensure they are functional and meet my organizational requirements, the user's identity in relation to that forge is how I verify who they are. I track issues with my code through Issues and cut releases for users to download through Releases. There's not a lot of git in this workflow, this is mostly placed on top of git.
So here are the primary issues I see with modern forges that I would love to solve.
Stuff happens in the wrong order. You know the PR. Commit 1: 'Feature.' Commit 2: 'fix.' Commit 3: 'fix.' Commit 4: 'actually fix.' Commit 5: 'please.' Commit 6, made at 11:47 PM on a Thursday: 'asdfasdf'. This person has a family. This person has hobbies. This person is, at this moment, crying. You don't want the feedback loop
after
the commit you want it before. Let me do an enforced pre-commit hook to run the jobs remotely on the forge and provide the feedback to the user before they push.
PR approval is too boolean. The PR is approved or it's not approved. Real code review, like real life, lives in the middle. 'Sure, fine, we'll deal with it later' is a legitimate human response and should be a legitimate button. Gerrit has a better model for this. If I weakly approve something as a maintainer, let me flag it for later.
PRs are too inflexible. I don't need 4 eyes on every change, especially in a universe where LLMs exist. The global GDP lost annually to senior engineers staring at a four-line PR waiting for someone — anyone — to type 'LGTM' could fund a moon mission. A nice one. With legroom. Let me customize and more easily control this. If the person is a maintainer and the LLM says its low risk/no risk just let them go.
Stacked PRs are just better. They're easier to review and understand. They have to be a first-class citizen not an add-on through a tool other than your VCS.
A forge shouldn't do everything. Issue tracking yes. Kanban board, probably not. Wiki? I doubt it. Everything tools always turn into crap. You add features when its easy to add features and then pay the maintenance price for those features forever regardless of their rate of adoption because now someone, somewhere uses them and you are locked in.
The standard unit of hosting is too large. Running Github Enterprise is a big task. Running GitLab is also a relatively big ask. These are complicated products with a lot of moving pieces. I want smaller individual units of hosting that I can link together to make an organization. It's fine if they're not globally federated and I need to make an account for each Organization, but an Organization should be flexible enough to let me say "these 12 Raspberry Pis are my org". I don't know how they communicate securely, I hire people for that problem.
My local copy of the repo should be a representation of the
entire
repo, not just the code. I should be able to approve a PR from the same VCS I use to check in the code. I should be able to go through my issues by looking through local files.
On the flip side, since I need to be online all the time to really work with a team, don't make me pay the storage price all the time. I want my VCS and my forge to work together. If I clone a repo, I want a pretty limited history for that repo when I clone. If I start to go back in time, spin up a worker to go fetch that stuff from the VCS when I need it. I don't need to hammer the forge with giant clone requests on the assumption that I might need to rebuild the forge at any moment with the entire history of the entire project.
Actions need to be signed, SHA'd and usable offline. If I want, I should be able to get tarballs of all my actions, stick them in the repo and tell my system "don't go anywhere for checkout action, that's right here". If I say latest, have that work like Dependabot does now where it opens up a PR to put the latest tarballs in my repo. Actions are critical and they should be runnable on my local machine through the same VCS if I want to.
Well Y Does Some Of That
Absolutely. There are a lot of tools that do parts of this. I want someone to take them, put them all together and fit them up. I want JJ as the VCS, I want this as the forge and I want the expectation that I as a user could live happily with a raspberry pi as a forge for a long time. I want those forges designed around modern concepts like object storage and shallow clones and getting constantly hammered by LLM bots.
Now in a universe where GitHub was doing a good job, I wouldn't even bother writing this up. GitHub is the default and talking to people about overcoming the default is usually a waste of time. Heinz is the default ketchup, when I order a Coke I don't want a Pepsi and if I'm going to use a forge up until 2026 there would have to be an amazing reason for me to not choose the one that everyone uses. Up until recently other forges have been like sweet potato french fries, which is to say never the thing you actually want.
But we live in a world where the monolithic forge is breaking down and nobody has built the replacement. The people with the money are busy with the rockets. The people with the taste are busy with their day jobs. And the rest of us are opening PRs titled 'asdfasdf' at midnight, waiting for a robot to check them, wondering when the tool we spend our whole working lives inside stopped being built for us.
If I ever get the submarine money, I'll let you know.
