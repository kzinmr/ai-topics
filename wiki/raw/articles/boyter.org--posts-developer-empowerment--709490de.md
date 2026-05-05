---
title: "Developer Empowerment - Move fast, don't break things (for long), be productive"
url: "https://boyter.org/posts/developer-empowerment/"
fetched_at: 2026-05-05T07:01:58.610683+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Developer Empowerment - Move fast, don't break things (for long), be productive

Source: https://boyter.org/posts/developer-empowerment/

Recently my job/career path has had me looking “under the hood” at clients development practices. The idea being to see where their strengths and weaknesses are and then make actionable suggestions.
Generally every client wants the same outcome. They want to know how to improve software quality and deliver features faster.
When doing this I focus on the development side, but honestly a lot of this applies to DevOp’s as well. In most situations I realized very quickly that I would be terrified to make any changes in the environments I am working with. No safety net where the penalty for mistakes is very high. I also see the same issues over and over again. When asked to articulate what the issues I saw at one client I came back with the words “You need to focus on developer empowerment”.
That sounds rather hand wavy so here is is a list of what should be done to achieve it, why it is important and what issues it solves.
Developer Setups
You need to have a process for getting a developer from getting a fresh machine to writing code. Ideally this is an automated process or a hybrid one but at the very least you want excellent documentation that just works.
This is a requirement for a few reasons. The first is that by documenting how to get started you actually understand all the moving parts. I have seen many organizations where the knowledge on how to actually build the core application is in the heads of a few or even a single person. You do not want your
bus factor
to be 1 or any low digit number.
This solves the issue that most organizations I have seen suffer, where a new developer or team member is brought on-board and they spend a week waiting for access, another week getting things setup and asking team members how to achieve tasks which could be documented and is a distraction. Having a dedicated person to assist the new member setting things up, and at the same time improving your documentation or process is a great way to on-board someone as well. Rotate though people so everyone eventually knows hows how it works.
Having things up and running quickly is a nice psychological boost too. It makes new members feel the team has things sorted out and should not be underestimated.
Tests and Testing
I am no testing zealot that insists that everything should be developed using test driven development, or that you need 100% test coverage (in fact I think that is an anti-pattern). In fact if you are looking for
expert excuses to not test your code I am your guy
. However I do want unit tests to cover those mission critical tricky functions. I want integration tests to ensure that the SQL I wrote does what I expect it to, and that the things I am working on integrate nicely. I want HTTP tests for API’s. I also want smoke tests so I can be confident nothing obvious is broken before pushing to production.
People can and will argue about how to write and how many to write tests for days on end. The reality is that we generally are not paid to write tests but write useful software. Tests are something that assists with that goal but are not usually a goal in themselves. There are dozens of
categories of tests
but for most projects, unit/integration/http/smoke are enough to achieve your goals.
Its also vitally important that your test suite is not full of
flaky tests
. The tests should run reliably as close to 100% of the time. Avoid flaky tests, either by refactoring or deleting them. If you do not they will lower confidence in the test suite.
With a solid test suite developers will not be afraid to make sweeping changes. If you ever see a developer afraid to make a change for fear of breaking something you have a problem. Tests are a good strategy to deal with this.
Use Source Control
Being able to look though history of changes will make you feel like a wizard. Never losing code is another reason.
I feel like this is something that should not need explaining but please use some form of source control. I don’t care if its git, mercurial, svn, cvs, fossil, bitkeeper or perforce so long as you have it. It is especially useful with CI/CD so you can know what has been deployed where and can roll back to specific versions.
Much harder to enforce is writing good commit messages. This has been written about quite a lot, but I like
this guide
and its approach.
As for branching strategies, every team has their own approach. Personally I like unstable master/trunk where
Use CI/CD
Have a solid CI/CD process where you commit code, it is built, tested and deployed to a development environment for every check-in and then possibly integration tested. When that passes promoted to higher tier environments before hitting production.
You generally need a minimum of 3 environments although 4 is more common. The first is a development environment which is generally a free for all. Code that lands here is constantly in churn and as such breaking. It should be being deployed to dozens or more times a day. When the feature that a developer is working on is considered done it is moved into the next tiered environment, with the condition that all tests should first pass. Anything in this higher level environment that passes your higher level tests should be considered a candidate for production release.
The release to production can be automated (if you have solid tests) or if you prefer a manual process, which should consist of a single click. If the tests pass, QA signs off or the business agrees to release then push whatever was signed off on in the environment to production.
You want be able to roll back. If something does go wrong you want to have a single click rollback procedure. You want the penalty for a failed or broken deployment to be less than 5 minutes downtime. For releases with database migrations this can be tricky, so you need to ensure that you release makes changes that are backwards compatible at all times. At the very least be prepared to have a database rollback if required.
Logging / Dashboards
Having a way to peer into your production environment and what it is doing is essential. While I personally have no problems with developers having access to production (assuming they don’t change things there) I understand this is potentially a problem for compliance reasons or not practical. As such a good way to get around the issue is to have good logging software (
Scalyr
being my personal choice) and tools such as newrelic coupled to dashboards.
The dashboards give an idea of the health of the system quickly, and when an issue is spotted you can use your logging tool to drill into the details and find out what has gone wrong.
The Result
There is a lot more that can be added to the above but it is a bare minimum that I believe is required. You probably want to throw some load tests in there but for most internal CRUD applications this isn’t a huge issue.
The ultimate result of implementing the above points is to make failing part of the process. For 99.99% of projects/companies/products a small amount of failure is not a huge issue. The 0.01% of groups are companies and organizations like NASA and it is usually cost prohibitive to
write code the way they do
.
For most however its easier to accept that nobody is going to write perfect code every time. Nobody is going to get everything right 100% of the time. If you accept that and make it so the cost of failure is small to non-existent then it is no longer an issue that impacts your time-lines.
The best developers I have worked with had an interesting work-flow. They would check out the code, find what they were doing, then just start deleting code and/or refactoring. The code was in git so nothing was ever lost, the tests would catch any regressions they added, and the higher level tests would catch other logic bugs. With code promotion issues were almost always caught before hitting production. In the event they did break anything it was a few minutes to rollback in production and in the case of a critical issue 30 minutes to restore the database. The amount of things that would have to go wrong to cause any production issues was so high it almost never happened, and when it did it was a simple thing to fix.
You want your developers to rip apart old code and rewrite it to make it faster and easier to understand. You want them to feel free to delete chunks that are no longer required. You want them to make mistakes, find bugs and fix them quickly. You want them to be empowered, because when you get there they are not going to be afraid when you ask them to implement feature X thats a 8 point sprint estimation and touches most of the code-base, because they have the confidence in the process. More to the point you will have happy developers, who in turn feel empowered.
Keep in mind the above is only directly applicable to teams of say 10 developers or less, or if you have a huge install base (staggered production roll-outs will help you there). However it still holds true for the most part of even very large teams. Facebook claims to move fast and break things. I would argue its better to move fast and don’t break things for very long.
