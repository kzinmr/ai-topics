---
title: "Introducing Claude Ship"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://claude.com/resources/articles/introducing-claude-ship"
status: complete
sources:
  - "https://claude.com/resources/articles/introducing-claude-ship"
  - "https://news.ycombinator.com/item?id=50618513"
sha256: c15df1b0b62db0fb240be0083b49e2ead2f2c0a6ca9e0351d70382840c8e01d2
---

# Introducing Claude Ship

Source: https://claude.com/resources/articles/introducing-claude-ship

## Article

Introducing Claude Ship | Claude by Anthropic 
 Skip to main content Anyone who has opened a pull request knows how this goes. They start on the next thing, and then the review comes back. So they stop, dig back into the old code, push a fix, and wait for the review to run again. Then they go find someone to approve it.
 There's a good reason it works this way. Most teams want a person to approve every change, and that's easy to keep up with when people write every line. But a lot of developers build with agents now. On the Claude Code team, Claude writes most of our code , and we wanted everything after the PR to move that fast too.
 That's why we built Claude Ship , available today in beta. It can review PRs, fix them, and decide what's ready to merge based on policies each team sets. Teams stay in control of where it runs and which changes need a person. The goal: ship code as fast as teams write it.
 Eligible Claude Enterprise organizations can claim at least $10,000 in Claude Ship credits to use within 30 days of claiming. Claim by January 15, 2027. Terms apply. 
 How Claude Ship works: review, fix, and approve
 Claude Ship is made up of Code Review , which is already generally available, and two new agents in beta: PR Steward and Claude Approvals. Together, they take a pull request through review, fixes, and an approval decision so teams don't have to manage each step manually.
 Code Review performs an in-depth review of pull requests against the codebase through multiple lenses. It collects findings, adversarially verifies them, categorizes them, and posts them to a PR. On the Claude Code team, where Claude's review is one layer of a broader process, merged PRs more than doubled from June to September while the share reverted fell by more than 40%. Code Review gives teams fast reviews, clear findings, and a choice of Quick, Standard, or Deep review levels for each repository.
 PR Steward works to keep a PR green, but is designed not to approve or merge pull requests. It jumps in on failing CI checks, merge conflicts, and review feedback from Code Review, other review tools, or team members. After every push, it comments with what it changed and how to undo it. Developers can comment @claude with an instruction to steer the work, or @claude stop to have it step back.
 
 From there, Claude Approvals applies an approval policy that the team writes as a file in the repository. Claude can approve routine changes on its own if the policy allows it, or can require deeper human sign-off for certain scenarios. It works like a smarter CODEOWNERS file. Teams can have Claude Approvals consider a variety of signals in its decision-making process, including Code Review findings or their own classifiers using natural language. For most customers, we recommend enabling this first in observe-only mode to build confidence before configuring branch protection to require Claude Approvals' green light.
 Two ways to get started
 For developers: /ship it from Claude Code
 Developers can try Claude Ship on their own pull requests with the new /ship command in Claude Code. When a change is ready, they run /ship . Claude pushes it, opens the PR, reviews the change, and works on feedback and failing checks to help get it ready to merge. What can merge depends on the developer's permissions and the repository's branch rules.
 For admins and engineering leaders: set the rules, one repository at a time
 Turning Claude Ship on for an entire repository puts it to work across a team's pull requests automatically, under settings and an approval policy the team controls. Developers don't need to manually invoke the /ship command.
 Admins choose where it runs. An admin turns on Code Review and PR Steward for each repository. Claude Approvals starts when a connected repository has a policy file on its default branch, and an admin can turn it off.
 Each repository gets the settings it needs. Admins choose the review level (Quick, Standard, or Deep), choose when reviews run, and configure spend limits.
 Teams keep the tools they have. Claude Ship works with existing branch protection and required checks.
 Teams set the pace. They can start with one repository, choose a review level and when reviews run, set a monthly spend limit, and run their approval policy in observe mode until they trust it.
 How the Claude Code team ships
 We run Claude Ship on many of our own pull requests. One of the biggest changes is who can act on customer feedback. For example, a product manager on the Claude Code team can now read a piece of feedback, talk through ideas and tradeoffs with Claude Tag , have it open a PR, and move on to the next thing while Claude Ship takes it through review, fixes, and an approval decision.
 Recently, a customer was confused because our Analytics API documentation implied an Admin key could pull Pro and Team usage. The PM asked Claude Tag whether a fix was in flight, and it opened one. Code Review found nothing blocking, a docs reviewer signed off, Claude Approvals passed, and the fix merged that same evening.
 What customers are saying

 “We have had numerous cases where Claude Code Review caught real issues before a human reviewer got to the pull request, and PR Steward helped the contributor fix them. Our reviewers were already using Claude Code to keep up with the volume, so having Code Review, PR Steward and Claude Approvals start automatically when a pull request opens makes that simpler. We keep a human in the loop, and the human’s time now goes to the changes that need it.”

 Vatsal Bhatt, Director of Engineering 

 “PR Steward is helping teams in our pilot spend less time working through code review feedback and more time building. We can tailor it to our teams’ processes, including how it suggests changes and organizes feedback. That flexibility has made it a useful part of the development workflow.”

 Alex Devkar, Senior Vice President, Engineering and Analytics 

 Availability
 Claude Ship is available on Claude Team and Enterprise plans for repositories on GitHub. Code Review is generally available , and PR Steward and Claude Approvals are in beta.
 Claude Ship usage is billed on tokens, so turning it on can add to an organization’s costs. The amount depends on the number and size of pull requests covered, the review level, how often reviews run, and how much work PR Steward does. Admins can set spend limits for Code Review and PR Steward. Claude Approvals has no base charge, but classifiers in a policy are billed on the tokens they use, and a policy that uses Claude's review triggers a billed Code Review, even in observe mode. Running /ship counts as regular Claude Code usage.
 Claude Ship is not available to organizations with Zero Data Retention, the HIPAA configuration, or customer-managed encryption keys.
 Get started
 Developers can update Claude Code and run /ship on their next change. /ship is rolling out in Claude Code and the desktop app starting today.
 Teams already using Code Review can add PR Steward on a repository, and an approval policy in observe mode.
 Teams new to Code Review can read the setup guide to connect GitHub and turn on their first repository.
 Learn more in documentation .

Article Nov 24, 2026 
 Turn artifacts into Mac and Windows apps
 Open the artifacts you use every day like any other app, and let them do more on your computer
 Claude apps 

Article Nov 24, 2026 
 MCP servers can now ship skills, run tasks, and more with Claude
 Claude apps Claude Platform 

Article Nov 23, 2026 
 Zero data retention with Enterprise Frontier Safeguards is now in beta
 Claude Platform 

Article Nov 17, 2026 
 Linked billing on the Claude Platform
 Claude Platform 

 Transform how your organization operates with Claude
 See pricing Contact sales 

 Get the developer newsletter
 Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

 Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

## HN discussion highlights (item 50618513)

# HN claude-ship — Claude Ship (88 pts, item 50618513)
# url: https://claude.com/resources/articles/introducing-claude-ship

[fwlr] “Claude writes the code - but I read it, my coworkers review it, and my team lead merges it” “Claude writes the code, Claude reads the code - but I review it, and my coworker merges it” “Claude writes the code, Claude reads the code, Claude reviews the code - but I merge it” “Claude writes the code, Claude reads the code, Claude reviews the code, Claude merges the code.” <—- You are here, already, somehow??
[thunfischtoast]   - Claude writes the issues. - Claude writes the roadmap. - Claude writes the transcript. - Claude sets up the VM. - Claude tells you what you need. How long until Claude tells you want you want?
[lelandfe]     - Claude interviews users - Claude distills feedback sessions into insights - Claude examines competitors to determine viability and novelty of insights - Claude finds competitors crowding out product, success unlikely - Claude finally locates competitor’s CEO’s fursona alt via stylometry - Claude partners with media buy company, success now likely
[archerx]   What will be the point of this dude and his coworkers when Claude can do anything, why would the shareholders keep him and the team on the payroll?
[fwlr]     Not sure if it was too subtle, but I intentionally had “coworkers”, plural, and “team lead” in the first line, and whittled it down to “coworker”, singular, then just the speaker, and finally not even them.
[bob1029] I'm gonna pitch this to the team. There is a lot of code authoring currently happening with OpenAI's models. Using a different provider's models to do the code review part seems like a pretty good separation of responsibilities.
[marssaxman]   That is what I've been doing for a few months - I'll set Claude and Codex up in an adversarial loop, one model reviewing the PR and the other one updating until it passes review. Then I have each one write me a summary of the changes made through the review process, and compare them.
[viklove] This is a tool which centralizes policy enforcement for teams with low-trust, I guess. I'm not sure what other value this offers, building a bot that can check for review comments and automatically push fixes is trivial for any engineering team. Of course, it probably makes even more sense to have your agent do all of this before it even hits the PR stage on GitHub? Yeah I'm really not sure who or what this is for. I feel like any engineering team worth its salt is going to have built their on agentic pipeline that's model-agnostic to avoid vendor lock-in. Sorry if I sound like a broken record
[springtimesun] It’s weird how close this matches the review process I built from individual pieces over the last few months. I call the steward the PR shepherd though so I guess it’s different :) I also layer model families in which I find to be important. Claude is good but the opens earn their keep as reviewers and catch a lot. I’m about to come to their conclusion as well for merges. Right now I still review and merge everything, but for low complexity items this is not worth the time. I can see it in my rate of accepts with no comments, commits pushed after review and how many request for changes I make.
[htrp]   you don't win because the frontier labs will try to capture all excess value (also just like lawyers you will no longer be able to bill by the hour at some point)
[springtimesun]     The thing I am holding onto, is that client projects (the ones I bid) are as much management consulting and business therapy as they are coding. People, even leaders who are paid to be good at it, are terrible at communicating (both their own thoughts and to others) and sometimes not very good at just thinking three or four moves ahead. It's certainly possible that the models get good enough to replace even that, but my hypothesis is that the human face becomes more important not less as the tools become more advanced. It's just that there are far fewer human faces needed as the robots put tea
[sambucini] this is a bit annoying as it overwrites our own /ship skill, a problem we're probably not alone with.. at first glance there are only 2 options: disable all bundled skills that come with claude or rename own skill, but apparently it's not possible to only disable this new ship command :-/
[suika] I believe you can build something similar to this with e.g. prime-agent and gerrit, both OSS and can use whatever model/provider you want. Claude Ship’s advantage is convenience and Github compatibility? But you have to bet that it survives as a product. What happens next?
[aniceperson]   github compatibility is webhooks + github app token. Claude Ships uses exactly the same set, it is very easy to replicate.
[htrp] at this point why bother with the pr. claude should just pick up open items from your issue queue, fix them, and then merge straight to prod
[Sol-] This basically needs Claude Code on the Web enabled so that Claude can check out your PRs in Anthropic infra, and like Code Reviews, is probably billed by API, right? Just to understand where it fits into the "Claude Code locally" vs. "Claude Code the agent" style of products that Anthropic mixes a bit.
