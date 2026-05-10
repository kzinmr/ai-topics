---
title: "Everything You Need To Know About Git Checkout -b"
source: "Warp Blog"
url: "https://www.warp.dev/blog/git-checkout-b"
scraped: "2026-05-10T01:27:27.624743+00:00"
lastmod: "2026-04-24T14:39:32.000Z"
type: "sitemap"
---

# Everything You Need To Know About Git Checkout -b

**Source**: [https://www.warp.dev/blog/git-checkout-b](https://www.warp.dev/blog/git-checkout-b)

Engineering
Everything You Need To Know About Git Checkout -b
Jess Wang
June 17, 2022
“Git checkout -b” is a command that you need to know when you’re learning to code. It’s actually very simple, and this blog will teach you everything you need to know.
What is "git checkout" ?
Git checkout is a terminal command that allows you to switch between and create git branches. By itself, it doesn't do anything. But prepended onto different commands, it can do a variety of different things.
This is what happens when I run git checkout by itself
.
‍
Nothing!
GIt checkout
‍
What does the "-b" in "git checkout -b" mean?
The "-b" is a flag that bundles two different commands together.
Git branch
<
new\_branch\_name>
This creates a new branch named
<
new\_branch\_name>
‍
Git checkout
<
new\_branch\_name>
This switches you from your current branch to the new branch named
<
new\_branch\_name>
I went ahead and ran these commands on my local environment.
Here is what the output looks like
.
Git branch & Git checkout
‍What happens when I run "git checkout -b" ?
Git checkout -b is a command that will create a new branch and switch you into that new branch from your current branch. I went ahead and ran the command in my local environment to show you what you should be seeing as your output.
Here is what the output looks like
.
‍
Git checkout -b
As you can see, this command does exactly the same thing as the previous image, but it's a lot shorter, quicker to type, and easier to remember.
How do I use "git checkout -b" ?
One common use case is creating a new local git branch with git checkout -b, and then pushing it to a remote server to create a remote branch of the same name.
Here are the exact commands you need to run to do this
.
Create a new remote git branch
Hope this helped!
You can find links to our socials at the bottom of this page - feel free to tweet us any comments or questions, or join our Discord for any further discussions. Good luck on your developer journey!
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
