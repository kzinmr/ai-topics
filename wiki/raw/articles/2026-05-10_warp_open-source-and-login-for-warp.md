---
title: "Open source and login for Warp, the collaborative terminal"
source: "Warp Blog"
url: "https://www.warp.dev/blog/open-source-and-login-for-warp"
scraped: "2026-05-10T01:27:57.938404+00:00"
lastmod: "2026-04-24T14:39:46.000Z"
type: "sitemap"
---

# Open source and login for Warp, the collaborative terminal

**Source**: [https://www.warp.dev/blog/open-source-and-login-for-warp](https://www.warp.dev/blog/open-source-and-login-for-warp)

Company
Open source and login for Warp, the collaborative terminal
Zach Lloyd
February 22, 2024
Update (November 22, 2024)
: Warp no longer requires login. You can now download and start using Warp without signing up. Read more about this change in our blog post:
Lifting the Login Requirement
.
---
This blog post lays out my thoughts as the founder of Warp on two of its (somewhat) controversial aspects, namely that it currently requires login and is closed source.
My hope is not that I’ll convince every developer we are doing things the right way, but to communicate the rationale behind our choices and let folks considering trying the product understand why Warp is the way it is.
Login
Warp requires developers to log in once when they start using the app. The basic rationale is the same as in other cloud based apps: login enables a consistent experience wherever a developer accesses the app so you don’t waste time setting things up over and over and all your work is available wherever you are (note that this isn’t fully implemented yet in Warp, but it’s the product vision we are working towards).
Moreover, for our collaboration features like Warp Drive, login enables secure sharing of a team’s terminal stuff like Workflows, Notebooks, Sessions, Preferences, and more. Login is necessary for Warp AI because without it we couldn’t meter usage. In short, login is a key enabler of the product experiences that developers who use Warp love.
That said, I get that Warp is an outlier when it comes to login in a terminal and some folks will dismiss all this on principle – “a terminal just shouldn’t have login” – and that’s understandable. My counter-take is that logging in is relatively low cost and unlocks the ability for Warp to seamlessly provide a lot of value. I hope that over time that we can demonstrate this value is worth the perceived cost.
I also get that the deeper concern here is one of trust – should a developer trust a relatively young startup to take care of their data? On this I think there’s no shortcut, we need to earn trust. The (reasonable) underlying fear here is that for a free product, a user’s data ends up being the product.
For Warp, this is emphatically not the case. We are not building a business around collecting developer data and we are not going to start showing you ads in your terminal (oy). No console data is ever sent to Warp’s servers unless you opt in for collaboration or device-syncing. We have listened to user feedback and
made telemetry optional
. When telemetry is enabled, it only monitors
high-level developer interactions with features
so we can understand how to improve our product (
Update, March 12, 2025:
We have updated our telemetry policies. Please visit
What telemetry does Warp collect and why?
). There is also a
Network Log tool
available you can use to observe any data leaving the Warp client.
We take data security extremely seriously and are in the process of a SOC2 audit and have completed a pen test. All data is encrypted at rest using industry standard AES-256 encryption.
Why not delay login?
Some folks also make the reasonable suggestion that login should only gate access to cloud-oriented features and be “opt-in.” There is precedent for this in some other apps – e.g. login in VSCode is optional and you only have to login if you want to use features like settings sync or Copilot.
We have debated this delayed-login approach a lot internally and I (Zach) have made a decision that overall it leads to worse user experiences than logging in once at the start of using the app and I don’t want Warp to go this direction.
For example, I recently had a negative experience with this “opt-in login” in VSCode. I moved from New Mexico to New York, switching computers. When I got to NYC and started using VSCode again nothing worked the way I expected (none of my settings were right, I didn’t have Copilot anymore) because I had neglected to log in in both places. It was annoying and I felt like it could have been solved by having a one-time login and using the cloud to keep my experience consistent.
I’m pretty convinced about this, but I recognize I could be wrong and there’s a chance we could relax the requirement. But to me the one-time cost of a login followed by everything seamlessly working outweighs the potential negatives.
Open Source
With respect to open source, it’s more of an evolving story, but the tl;dr is that we are currently closed-source and proceeding cautiously.
Our goal with Warp is to provide developers with a totally reimagined terminal experience that they love using. We’ve been working on this for a few years now and I’m really proud of what we’ve shipped so far. While there’s still a ton to do, I believe that Warp is a huge step up from the standard terminal experience.
Our hope is that we can continue developing Warp and improving it for years to come. One of the things I’m personally passionate about is that developers shouldn’t have to just tolerate their tools – they should love them, and Warp’s ethos as a company is trying to make this a reality.
There are many approaches companies can take to ensure their longevity, and I don’t expect developers reading this to care much about Warp as a business.  But when it comes to open source, the primary reason we have not yet open sourced Warp is that we fear it would make it harder for the company to succeed in the long term.
Most of the value of Warp is in our client-side app and there’s a risk that if we were to open-source Warp now we’d cap our ability to monetize it – or worse, a better-resourced competitor could use what we’ve built to compete with us. This isn’t an idle concern; we’ve seen it play out with other startups (e.g. with
Elasticsearch
and AWS). We’ve also seen companies have to reverse their position on open source (most recently
Terraform
) in order to better monetize, causing a lot of churn and user anger. We want to avoid this.
Staying closed source for now gives us the most flexibility as we grow our business. We still support the open source community in a few ways: we are committed to open sourcing Warp’s Rust-based cross-platform UI framework (shooting for later this year), and we sponsor a number of open source projects such as
Neovim
,
wtf,
lazydocker
, and more.
As an aside, I’m hopeful that we will eventually open source Warp as I see a ton of benefits in terms of ecosystem, contributions, being more auditable – I just don’t want to commit to a time frame or set expectations that we can’t fully live up to.
However, I will commit that if Warp somehow stops existing (unlikely but possible), we will open source everything (client and server) so folks can continue using Warp forever.
I hope this post at least clarifies my thinking on these two somewhat contentious issues and if you’ve read this far, I’m grateful. Thank you for giving Warp a shot!
Related articles
Apr 28, 2026  ·  4 min
The virtuous loop of open, automated development
With today’s open-sourcing of Warp, our goal is to create a new way of building, where humans and agents collaborate in the open to ship better software, more quickly.
Mar 16, 2026  ·  8 min
What happens when you give the company 4 hours to automate everything
The Warp team held a company-wide hackathon to build with Oz, our cloud agent platform. Here's every project, from docs migrations to churn detection, that shipped in just 4 hours.
Feb 10, 2026  ·  12 min
Introducing Oz: the orchestration platform for cloud agents
Run hundreds of coding agents in parallel with full visibility and full control
