---
title: "Using Workflows and Commands.dev to Remember Commands We Often Forget"
source: "Warp Blog"
url: "https://www.warp.dev/blog/using-workflows-and-commands-dev-to-remember-commands-we-often-forget"
scraped: "2026-05-10T01:28:18.000072+00:00"
lastmod: "2026-04-24T14:39:59.000Z"
type: "sitemap"
---

# Using Workflows and Commands.dev to Remember Commands We Often Forget

**Source**: [https://www.warp.dev/blog/using-workflows-and-commands-dev-to-remember-commands-we-often-forget](https://www.warp.dev/blog/using-workflows-and-commands-dev-to-remember-commands-we-often-forget)

Product
Using Workflows and Commands.dev to Remember Commands We Often Forget
Ian Hodge
May 9, 2022
Introduction
When I was first learning to use the terminal, I would often find myself pressing the up arrow twenty to thirty times, painstakingly trying to find the exact command I had in my head but could not, for the life of me, seem to remember the exact syntax for. The command in question was not one I had committed to memory - it was rarely used, or had complex parameters that I did not fully understand enough to type from scratch. If my tedious history search proved fruitless, I'd be forced to switch my context away from my terminal, open a Chrome tab, and search through Stack Overflow or outdated team wikis until I found the exact command I needed.
As developers, there are many commands that (either through repetition, intuitive syntax, or both) we are able to commit to memory. These could be the git commands used for source control, or the build and test scripts run so often that they’re completely built into muscle memory. However, there are also more complex, unintuitive, or rarely used commands that are much harder to remember. This experience is especially frustrating because we often know
what
we need to accomplish but do not know how to translate this task into a specific terminal command. The resulting chase through Google or documentation can be very frustrating, waste precious engineering time, and, by switching context away from the terminal an IDE, break us out of our focus.
Aliasing can sometimes solve these pain points, but there are still a few limitations. Namely, aliases are difficult to document, hard to search for, not easily parameterized, and tough to share.
Completions are also very helpful with command entry, but, like aliasing, are limited in what problems they solve. Completions are useful for entering a command one step at a time (i.e. finding the next argument, flag, or subcommand). However, they do not help with remembering long, argument heavy commands, or let you search by what the command actually does.
These limitations and frustrations were the inspiration behind two products built by the Warp team:
1)
Workflows
: an in-app feature that brings the hard to remember commands directly into the terminal.
2)
Commands.dev
: a templated and searchable catalog of popular terminal commands.
Workflows
Workflows are searchable by name, description, or command - allowing users to easily translate the semantics of the task they need to accomplish directly into the correct syntax. Commands are easily parameterized, and documentation about the command and parameters informs users on how it should be executed. When designing the UX for Workflows, the team at Warp strove to ensure that the feature was not only more powerful than aliasing, but just as fast. This resulted in a keyboard first UI that allows the user to quickly tab between different parameters in the command directly in the input box before running the Workflow like any other command.
Warp comes loaded with a public list of workflows sourced by the Warp team and community. We started by bootstrapping workflows from common StackOverflow posts since we believed that would translate to commands users often have trouble remembering. Since we've launched, we've had twenty-nine contributions from twenty-two different users in our community to add even more useful workflows. As a result of both the manual sourcing and community, the workflows repo has grown to over 145 different commands, and all contributors (both direct and from StackOverflow) are credited within the repo. As the feature matures, we are so excited to see how this repo of commands continues to grow.
Although a public list of workflows is extremely useful for finding and executing general commands (such as
git reset HEAD~,
a command I find particularly unintuitive and often forget), many commands run on a daily basis are company or team specific and therefore not particularly useful to the broader community. Because of this, we also built support for users to create their own custom workflows and save specific team commands and scripts. These custom workflows can be associated either with a particular user or a git repository, allowing teams to bring their commands and documentation directly into Warp. For more information on how custom workflows work, or how to contribute to the public repo, you can check out
our documentation.
Commands.dev
A lot of manual effort by both the Warp team and community was put into curating the global list of Workflows, but the fruits of these efforts could only be experienced by Warp users. A well documented and maintained list of terminal commands has huge amounts of potential benefit for any developer, not just the ones on Warp. This realization was the impetus for
Commands.dev
- a website that serves as a catalog for all of the commands sourced by the Workflows community.
Commands.dev makes it incredibly easy to search for commands by name, description, or direct syntax. You can also browse by tag and discover other similar commands to the one you’re trying to find. While it’s still in its infancy now, we hope that open source contributions can build Commands.dev into the centralized source for all terminal commands. Instead of google searching through multiple sites to find their desired command, developers will just need one place - Commands.dev.
Conclusion
Workflow and Commands.dev are both products that are only as strong as the community that supports them. The better the list of globally sourced commands, the more powerful the feature becomes for every user. Commands.dev amplifies the visibility of the global workflows repo beyond just Warp users - it incentivizes contributions and expands the benefits.
The version of Workflows and Commands.dev live today are only the beginning of what we believe the features can become. In future iterations, Workflows has more potential to unlock command sharing for teams, and make it even easier to bring team specific documentation directly into the terminal. For Commands.dev, we have plans to integrate natural language search, greatly amplifying its ability to help you find the command you need. The team at Warp is so excited to see how both Workflows and Commands.dev grow as we continually strive to build the best systems for command entry and sharing!
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
