---
title: "Cull your dependencies"
url: "https://tomrenner.com/posts/cull-your-dependencies/"
fetched_at: 2026-04-25T12:09:23.343063+00:00
source: "tomrenner.com"
tags: [blog, raw]
---

# Cull your dependencies

Source: https://tomrenner.com/posts/cull-your-dependencies/

Anyone  writing code professionally in December 2021 will remember the
“fun”
of
the
Log4J
vulnerability
. For those that weren’t - this was a critical security error that allowed attackers to run any code they wanted on your servers. The root cause was a logging library, Log4J, that is used by most projects that are writting in Java.
It’s usually used to write code something like:
log.info("Process completed successfully");
which will then appear in your logs, allowing you to track your application’s behaviour. Pretty innocuous stuff.
My company was one of the affected by the
vulnerability
(among countless others), and in looking into it I noticed something.
By the numbers
The underlying Log4J library is 168,000 lines of code.
Now, most commercial applications import tens if not hundreds of such packages, which at a conservative estimate gets us to 1M lines of code in the imported packages. This is roughly the size of an entire
operating system
.
In
Code Complete
Steve McConnell estimates that commercial software has roughly 15-50 errors per thousand lines of code.
For our hypothetical application with 1M LoC in its dependences, this suggests we’d have around 15,000 bugs in imported code alone. Code that you will likely never see, read, or often even think about.
Assumptions developers make
An interesting thing about developers is that we are lazy, and prefer to write as few lines of code as possible, sticking rigidly to the principle of “not reinventing the wheel”.
This encourages us to import packages to solve common problems, rather than write a utility class or method ourselves. However, this habit often results in the addition of thousands of lines to your dependencies, to save writing 20 lines yourself.
We also invariably assume that code provided via official means (maven, npm, pip, whatever) will be of higher quality. After all, it’s come from the package manager, it’s got to be good, right?
In reality, packages are often maintained by a single person or a small team of volunteers, and of course in general there are no quality checks required for packages added to package managers. Log4J has been in production  for nearly 20 years, and practically every version of it has contained the critical issue that kept many of us busy patching it in December.
Just because it’s been available to lots of people and “battle tested” in production systems  does not mean that it is secure.
These two assumptions together cause a poisonous mix whereby developers with the best of intentions end up adding in more and more external code of unknown quality to an application, in the naive pursuit of rapid development and efficient code re-use.
Process problems
Once a package has been added, it becomes part of your “assumed standard” – people will assume that using it is safe, and that to do so is best practice, so it will
proliferate
. And as usage proliferates, so the dependency will solidify and calcify, and until very rapidly it will prove impossible to remove without a major engineering effort.
Minimising dependencies is not something that’s (currently) widely valued in our industry, and putting in the refactoring effort to remove a dependency almost never happens (the only exception I’ve seen is the removal of Log4J, which is relatively easy to replace, and was only done after a truly massive incident).
And so dependencies will only grow over the lifetime of a piece of software, and vulnerabilities will silently accumulate in the application.
Additionally, even if you remove a method from being used in code, tooling to remove the package it came from from your project’s imports (via pom.xml, package.json, etc.) is pretty poor. It can be hard to determine whether you need a package any more at all, or whether it provides other functionality still used in another corner of the codebase. As a result, stale packages often hang around as bloat even after they’re not needed, just waiting to be reintroduced by an unsuspecting developer.
Proposals
As a rule, do not add dependencies to your codebase.
When a new package is added to the codebase, demand full justifications about why it is required, and record the reason for the addition in a log within the repository. This will both make it easier to remove the dependency later if it is not needed, and also ensure that it continues to be used only for its intended purpose.
Don’t import multiple packages for “utility methods” - use one and explicitly agree on using it as a standard within your team. This decision should again be recorded in a dependencies log within the repository.
I will be following these within my team, and in projects I’m involved in.  Do you agree with them?
Let me know
if you do, or if there are other techniques you follow to prevent dependency proliferation in your work.
Reactions collected from around the web using
webmentions
