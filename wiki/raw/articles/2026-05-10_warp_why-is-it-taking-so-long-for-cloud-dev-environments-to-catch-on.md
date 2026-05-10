---
title: "Why is it taking so long for cloud dev environments to catch on?"
source: "Warp Blog"
url: "https://www.warp.dev/blog/why-is-it-taking-so-long-for-cloud-dev-environments-to-catch-on"
scraped: "2026-05-10T01:28:27.337583+00:00"
lastmod: "2026-04-24T14:40:06.000Z"
type: "sitemap"
---

# Why is it taking so long for cloud dev environments to catch on?

**Source**: [https://www.warp.dev/blog/why-is-it-taking-so-long-for-cloud-dev-environments-to-catch-on](https://www.warp.dev/blog/why-is-it-taking-so-long-for-cloud-dev-environments-to-catch-on)

Product
Why is it taking so long for cloud dev environments to catch on?
Zach Lloyd
September 20, 2022
tl;dr
One of Warp’s investors asked for my thoughts on the cloud development environment space.  It was a fun question to think about (and is relevant to Warp as well), so I wrote up my thoughts.  I could be totally off, but thought it would be fun to share them for feedback.
The high-level summary is that I think that development environments will eventually move to the cloud, but the incentives aren’t as strong as they are in other domains.  I think top-down adoption is more likely than bottom-up in this case, but it will depend on the stack and developer segment, and take a longish time.
–
I remember the first time I used a Google Sheet in 2006 where there were multiple collaborators moving around its cells in real-time.  The experience was magical, and it was pretty obvious that it represented the future of how document collaboration would work.  Everything would be shared via link, with one cloud-based source of truth that multiple people could work on together.
Fast-forward 16 years (eight of which I happened to spend helping build the current version of Google Sheets), and numerous other products have made the same transition from local, single-user desktop software to cloud-based collaboration.  The transition of design software from Sketch to Figma is a good example.
However, there has been one very notable exception to the general trend – the primary tools that developers use to write and run code. The code editor and the terminal, two tools that literally every developer uses every day – have both been very slow to make the transition off of said developers’ laptops and into the cloud. Why is that?
This post explores why what seems at first to be such an obvious evolution is actually much harder than it seems.  I believe we will eventually write most of our code in the cloud, but I think it will be a slow, uneven transition. Certain segments of developers and stacks will move to the cloud before others and it will take a long time for everyone to get there.
First though - what does it even mean for developer tools to move to the cloud?  It could mean a couple different things:
A full IDE in the browser (e.g. GitHub Codespaces) which integrates the code editor + terminal + execution environment that is running on some cloud machine.
A “DevBox” in the cloud that is the “runtime” for the dev environment – it has the source code, build tools, and so on, but it’s up to the developer how they connect to that DevBox, edit files, run builds, etc. They could connect through a browser based IDE or terminal or they could run a native app that “remotes” into the box as though it’s a local file system.
Of the two ways of doing remote dev (IDE in the browser or DevBox), there are tradeoffs amongst the two.
The IDE in the browser has the advantage of not requiring any setup, installation, etc.  It’s great for getting going quickly on new projects.
But to the extent that it requires an entire team to use the same code editor, it’s problematic.  Even though VSCode has a big market share, a lot of devs still prefer other editors like jetbrains or terminal editors like vim.  Sometimes you need to use a different editor because of the type of work you are doing (e.g. xcode / android studio).
Whatever the specifics end up being, the advantages of a cloud setup are pretty clear:
The environment is accessible from anywhere via the internet, not just whatever laptop you set it up on
You can have a powerful machine in the cloud (that possibly you pay for only when using it).  Consequently, devs can get cheaper laptops and speed up build times
Cloud hosting makes real time collaboration easier if you ever want to do simultaneous pair programming
Cloud hosting makes it necessary to have a (mostly) hermetic dev environment, which is a good thing
More secure in theory because source code is not on your laptop
Conversely, remote development comes with some inherent challenges to overcome:
Latency, in all possible ways: both in terms of spinning up the environment, and actually working in it (especially via approach #1 above)
Lack of offline access - devs like working on their laptops and don’t like being unable to code when there’s no internet
Complexity of different local setups that need to be emulated in the cloud - i.e. where do all of your microservies run, how are all of their endpoints configured, etc.
Complexity of using all your devtools in a remote env (everything is harder when you aren’t on your own machine and have to connect over the network)
Notably, the biggest single advantage that an app like Google Sheets brings to the knowledge worker – solving version skew and creating a system of record – isn’t really an incentive for development environments to make the cloud transition.
Before apps like GDocs and GSheets, knowledge workers were constantly in the situation of sending around document attachments via email that were actually multiple versions of what conceptually was one document (think back to when you would “Save As…” and give your file a new name like important\_doc\
zach\
1.xlx and your colleague would send you important\_doc\
lucy\
2.xlx and so on).  This caused a ton of wasted time and headache merging changes.
Avoiding version skew by having only one canonical version of the document is the killer collaborative feature of all of the online document editors, more so than even any of the flashier realtime features like multiple cursors.
Developers, however, solved the version skew problem years ago using a very different approach – distributed source control systems like git (and cvs, perforce, svn, mercurial etc). These systems obviate a lot of the benefit of multi-player cloud editing because they allow for asynchronous local change management in a way that never existed for an excel spreadsheet.
Plus, because developers typically work on text files (rather than binary document formats), merging changes is doable manually, even if it’s sometimes annoying.
Finally, this type of control is actually needed for source code – you need to be able to track every single change, merge, rebase, etc, whereas for spreadsheets the “always at head” model is generally good enough.
Individual developers – what’s the pull to remote dev?
The existence of distributed version control makes the pull of remote dev environments much less strong than it otherwise would be.  Without the “system of record” advantage, I’d contend that the pull of remote development
to an individual developer
simply isn’t that strong.
As an individual dev, here are some of the other reasons I might want to work in the cloud:
Hermetic dev envs
: Having hermetic, shareable dev envs is probably the strongest pull, as it’s very annoying to have to deal with the class of bugs that arises from development environments being different across developers A and B, and also from local to production. That said, doing remote development simply doesn’t solve the hermetic dev env problem.
Developers today tend to have dependencies on cloud-hosted services and APIs that can’t be made hermetic no matter where your dev env is hosted (e.g. how do you make a hermetic dev env if you’re calling out to something like the Twitter API)
Docker != hermetic – you get something that is hermetic across one VM, but most apps have lots of external deps, microservices, data dependencies, etc
Faster builds
: could be a big pull on larger projects.  However to really do fast builds, you end up needing to shard and cache them via something like bazel and that’s not really incompatible with doing your code editing locally - this is how it worked at Google when I was there.
Real-time collab / pair programming: could be a pull, but doesn’t actually require remote hosting (you can use something like ngrok or tandem), and also really isn’t that common in my experience – it’s hard for me to imagine this being the primary driver.
On the flip side, as a developer, I’m worried that the move to remote
Will introduce latency
Will make it so I can’t work unless I have fast internet
Will make it harder to use my existing toolset
Will require some big migration to make my existing project build
And sometimes it just won’t be possible at all, say if you are doing any kind of native or mobile development (using xcode, etc)
As an aside, at Warp, there are a lot of things we talk about with respect to improving engineering productivity, but moving our env from local to the cloud never comes up (in fairness though, we are building a native Rust app).
Top-down company adoption has a stronger pull
The other way the migration to remote dev could conceivably happen is from a top-down company mandate, rather than from developers choosing individually that remote dev improves their experience.  I believe this is how GitHub rolled out Codespaces internally.
However, this comes with its own set of challenges.
If the rollout is to some version of VSCode in the cloud, there is likely to be pushback because devs use different editors (e.g. vim, jetbrains, etc) and generally don’t like to be told to switch (you can take a big productivity hit).
Some setups are going to be hard to impossible to do remote (e.g. mobile / native / embedded systems)
That said, I think the top-down approach is actually most likely because the benefit is potentially stronger for a company than an individual:
Could save companies money to cloud host vs. buying everyone an expensive machine
Could be a significant security win not to have code on personal machines
Could be much easier to onboard / offboard engineers and work with external vendors
So I could imagine a CTO saying, “we are all switching to dev in the cloud – it may be a pain to start, but the long-term benefits to the company are worth it.”
My best-guess at how the transition will happen:
Remote dev shift will continue to happen gradually, not all at once
Remote dev will happen in a lot of different ways
+ In some places, it will be totally vertically integrated, like Codespaces
+ In some places, it will be a cloud devbox model
It will be easiest for
+ New projects to start remote (rather than migrating existing workflows to remote)
+ More limited domains like webdev / jamstack
+ New developers / novices / students
It could happen if certain companies start to mandate it for financial or security reasons
Dev technology is by its nature very fragmented though, and certain trends actually make the transition hardere
Remote dev shift will continue to happen gradually, not all at once
+ Proliferation of microservices
+ Proliferation of cloud services make it super hard to have a hermetic dev env, no matter what you do
At some point Warp may have the feature of “make my local terminal setup run on a cloud box” – I think it’s an interesting onramp to cloud dev.
But it’s not our current focus – right now we are just trying to create the best possible single-user terminal and prove that the terminal can also be a Teams product – which ironically doesn’t require any particular stance on remote dev at all.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
