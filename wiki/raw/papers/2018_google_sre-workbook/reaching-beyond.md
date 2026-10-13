---
title: Google SRE Core Principles. Google's 14 Years of Learnings
source_url: https://sre.google/workbook/reaching-beyond/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/reaching-beyond.html
original_sha256: f3ee918c3aa3978d1086ff82259595cef2828c64ee4c00860fbc34edc5f556c7
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/reaching-beyond/
ingested: '2026-10-14'
sha256: 0ea15d3f5d0c7e8d66c2f51f99de3e92613d23265406b2fca5e79a7a7efed2da
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
SRE: Reaching Beyond Your Walls
By Dave Rensin
with Betsy Beyer, Niall Richard Murphy, and Liz Fong-Jones
It has been 14 years since we started practicing SRE at Google. Some of what has come in that time seems obvious in retrospect, while other developments came as something of a shock. The past two years since the publication of
our first SRE book
have been especially interesting. The number of companies now practicing the SRE discipline and the amount of time we spend talking about it at conferences and with customers has grown beyond anything we previously imagined.
That change in particular—the rapid expansion of the non-Google ecosystem around SRE—is the most exciting development, but it makes predicting the future of the SRE profession more difficult. Still, in our own SRE work at Google we are starting to see some trends that might inform an outline of the profession’s future. This chapter represents our effort to share what we, along with our SRE coworkers around the globe, have seen, and what we have concluded so far.
Truths We Hold to Be Self-Evident
The only way to make any useful sense of the future is to start with a set of principles and work forward. Some of what follows should be uncontroversial. Other bits, not so much. In every case, though, these principles are based on real things
we’re seeing in the world
.
Reliability Is the Most Important Feature
People don’t normally disagree much with us when we assert that “reliability is the most important feature of any system”—as long as we take care to point out that “reliability” often covers a wide area.
The argument is simple enough:
If a system isn’t reliable, users won’t trust it.
If users don’t trust a system, when given a choice, they won’t use it.
Since all software systems are governed by network effects, if a system has no users, it’s worth nothing.
You are what you measure, so choose your metrics carefully.
Your Users, Not Your Monitoring, Decide Your Reliability
Since the value of a system is related to its users, it stands to reason that the only measure of reliability that matters is how your users experience reliability. If your user is worried that your platform is responsible for instability they’re experiencing, then telling them “our monitoring looks fine; the problem must be on your end” won’t make them any less grumpy. They’re experiencing your system as unstable, and that’s what they will remember when the time comes to choose between you and your competitor. (This phenomenon is called the
peak-end rule
.)
Your monitoring, logs, and alerting are valuable only insofar as they help you notice problems before your customers do.
If You Run a Platform, Then Reliability Is a Partnership
If
the only way for someone to use your system is via a visual user interface (e.g., a web page)
and
your system is consumed only by actual human beings (as opposed to machines),
then
the reliability your users experience is almost exclusively tied to the job you do as an SRE keeping your system healthy.
However, once you add an API and some of your “users” are actually other machines, you are running a platform and the rules change.
When your product acts as a platform, the reliability your users experience isn’t limited to the choices you make. Reliability becomes a partnership. If your users build or operate a system on your platform that never achieves better than 99% availability—even if you’re running your platform at 99.999% availability—then their
best-case
experience
is 98.99901%.
The choices these users make directly affect the experience they have and associate with your service. You might not like it, but they will hold you accountable for whatever they experience—even if it’s not “your fault.”
Everything Important Eventually Becomes a Platform
Since the value of your system increases with the number of people using it, you will want to find ways to reach other large established user pools. As you attract more users, other software systems will want to reach your audience, too.
This is when other companies start making their machines talk to your machines via APIs. If your system is even remotely popular, integration is an inevitable step in your evolution.
Even if you decide that you don’t care about other user communities, and decide to never create a machine-consumable API, you still won’t be able to avoid this future. Other people will simply
wrap
your UI into a machine API and consume it. The only difference is that you’ll have no control over the outcome.
Once your system becomes a gateway to a large collection of users, it becomes valuable. APIs—official or unofficial—will be a part of your future.
When Your Customers Have a Hard Time, You Have to Slow Down
When your customers have a hard time, their frustration turns into friction for you. Even if you don’t have traditional modes of support (trouble tickets, email, phone, etc.), you will still spend time triaging questions and responding to complaints via StackOverflow, or even Twitter, Facebook, and other social platforms.
Whatever energy you put into helping users past their difficult moments is energy you can’t invest in advancing your system. We have seen many teams (and companies) allow their time to be slowly absorbed by break/fix customer problems—leaving an ever-diminishing innovation budget. These teams are consumed by toil.
Once in this state, it’s hard to dig out (see
Eliminating Toil
). A better plan is to get ahead of the impending toil. You might be reading this and thinking,
Gee, I’m on an internal platform team. This doesn’t apply to me!
We’re sorry to inform you that this
doubly
applies to you! In your case, your customers are the consumers of your system within your company.
This leads us to the next conclusion.
You Will Need to Practice SRE with Your Customers
If you want your customers to design and operate reliable systems using your platform, you have to teach them how to do it. Yes, this includes your
internal
customers, too. Just because you work on an internal platform team doesn’t mean you escape this dynamic—in fact, you’re likeliest to run into it first.
Even if you could perfectly distill that information into highly scaled one-to-many forms (books, blog posts, architecture diagrams, videos, etc.), you still need a way to figure out what content and training to include. As you grow and improve your platform, those lessons will change. You will always need a way to keep these resources from getting stale.
The best way to learn these lessons is to “do SRE” with your customers.
That doesn’t necessarily mean you need to take the pagers for your customers’ systems, but you do need to undertake most of the work that normally leads up to pager handoff (meaning the system has met certain minimum viable reliability requirements), with at least a representative sample of your users.
How to: SRE with Your Customers
The idea of walking an SRE journey with your customers might seem a little daunting. You’re probably reading this book because you’re not entirely sure how to walk it yourself! No worries. It’s possible to do both at the same time. In fact, the former can help you accelerate the latter.
Here are the steps we like to follow. They work pretty well for us, and we think they’ll be useful for you, too.
Step 1: SLOs and SLIs Are How You Speak
You want your customers to perceive your system as reliable. Otherwise, you risk losing them. It stands to reason, therefore, that you should care a lot about
how
they form those opinions. What do they measure? How do they measure it? Most importantly, what
promises
are they making to
their
customers?
Your life will be a lot better if your customers measure SLIs and
alert on SLOs
, and if they share those measurements with you. Otherwise, you will spend a lot of energy in conversations like this:
Customer:
API call X usually takes time T, but now it’s taking time U. I think you are having a problem. Please look into it and get back to me immediately.
You:
That performance seems in line with what we expect, and everything looks fine on our end. Is it a problem if API call X takes this long?
Customer:
I don’t know. It doesn’t usually take this long, so obviously something has changed and we’re worried about it.
This conversation will go round in circles and never reach a satisfactory answer. You will either spend a lot of time convincing your customer that they shouldn’t care, or you will spend a lot of time root-causing the change so you can convince your customer they shouldn’t care. In either case, you’re spending a lot of effort that you could be using elsewhere.
The root cause of this problem is that the customer isn’t using SLOs to figure out if they should care about the performance they’re seeing. They’re just noticing an unexpected change and deciding to worry about it. Remember, in the absence of a stated SLO, your customer will inevitably invent one and not tell you until you don’t meet it! You’d much rather have this conversation:
Customer:
We’re burning through our SLO for application FOO too quickly and the application is in jeopardy. SLIs X and Y seem to have fallen off a cliff. They both depend on your API X.
You:
Okay. Let me look into how API X is performing in our system and/or how it’s performing specific to you.
That’s a
much
more productive conversation because (a) it will happen only when the SLO is threatened, and (b) it relies on mutually understood metrics (SLIs) and targets (SLOs).
If you’re running your systems using SRE practices, then you are speaking SLOs internally. Your life will be better and your customers will be happier if they are speaking SLOs, too, because it makes it easier for the two of you to talk.
We recommend a simple exercise to make your working relationship with a customer a lot better: sit down with your customer. Explain SLOs, SLIs, and error budgets—and especially how you practice them in your teams. Then help them describe the critical applications they’ve built on your platform in those terms.
Step 2: Audit the Monitoring and Build Shared Dashboards
Once your customers have picked some basic SLOs for their application, the next question is if they are
measuring the right things
to determine whether or not they’re meeting those goals. You should help them figure out if the measurements they’re using are appropriate.
In our experience, up to half of the things your customer is measuring (and alerting on) have zero impact on their SLOs. Your life will be better when you point this out to them and they turn off the offending alerting. It will mean fewer pages for them, and for you!
The remaining measurements are useful candidate SLIs. Help your customer assemble those measurements to calculate their SLOs.
Once you begin this exercise, you’ll quickly find that parts of the SLOs are
uncovered
—there aren’t relevant measurements in place to say anything useful about these dimensions. You should help your customer cover these parts of their SLOs, too.
Now, your customers can start to say something about their application’s SLO performance on your platform.
Finally, build a set of shared SLO dashboards with your customer. You should be able to see their application SLOs, and you should share any information you have that’s relevant to how they’re experiencing your system performance. Your goal is that whenever your customer contacts you because their SLO seems threatened, you shouldn’t have to swap much additional information. All of that information should be in the shared monitoring.
Step 3: Measure and Renegotiate
Once you sort the measurements out, you should collect data for a month or two. Be prepared for the likelihood that your customer is in for a rude awakening. The application they thought was operating at “five 9s” (99.999%;
everybody
thinks they’re getting five 9s) is probably achieving only 99.5%–99.9% when measured against their shiny new SLOs.
After the initial shock wears off, this is a great time to point out that their users aren’t yelling all the time, so they probably never needed the five 9s they haven’t really been getting.
The key question is, how satisfied are their users with the application’s performance? If their users are happy, and there’s no evidence that improving performance or availability will increase user adoption/retention/usage, then you’re done. You should periodically ask yourself this question to make sure that your budgets and priorities are still correct. (See
Implementing SLOs
for a more in-depth treatment of this topic.)
If the customer thinks they still need to make things a little better, move on to the next step.
Step 4: Design Reviews and Risk Analysis
Sit down with your customer and really understand how their application is designed and operated. Do they have any hidden single point of failures (SPOFs)? Are their rollouts and rollbacks manual? Basically, conduct the same exercise you conduct for your own internal applications.
Next, rank the issues you find by how much of their error budget each item consumes. (Read more about how to do that
on the Google Cloud Platform Blog
.) Pay attention to which items your customer chooses to fix in order to “earn back the 9s” they want (e.g., to move from 99.5% to 99.9%).
What you learn from these reviews will tell you:
How your customers consume your platform
What reliability mistakes they make when doing so
Which tradeoffs they choose when trying to improve
This exercise will also help your customer set realistic expectations around the reliability they should experience with their current application. Their expectations will affect their perceptions, so setting them appropriately can only be helpful in earning and keeping their trust.
Step 5: Practice, Practice, Practice
The final step is to create some operational rigor with your customer. Practice simulated problems (Wheel of Misfortune exercises,
disaster and recovery testing
, paper game days, etc.).
Develop a healthy muscle memory between the teams for effective ways to communicate during a crisis. It’s a great way to build trust, lower the MTTR, and learn about weird operational edge cases that you can integrate as enhancements into your platform features.
When an incident does occur, don’t just share your postmortems with your customer. Actually conduct some
joint postmortems
. Doing so will also build trust and teach you some invaluable lessons.
Be Thoughtful and Disciplined
It will quickly become impossible to carry out these steps with more than a small percentage of your customers. Please don’t try extending this model to everyone. Instead, make some principled decisions about how you will make selections. Here are some common approaches:
Revenue coverage
Select the minimum number of customers to account for XX% of your revenue. If your revenue is heavily weighted to a few large customers, then this might be the right choice for you.
Feature coverage
Select the minimum number of customers to cover more than XX% of your platform features. If you run a highly diverse platform with a long tail of customers doing a lot of different things, then this approach will help you avoid surprises.
Workload coverage
Your platform’s usage may be dominated by a few distinct use cases or customer types. Perhaps no individual customer in those types is dominant, but you can easily group them into cohorts. In that case, sampling one or two customers from each cohort is a good way to get platform coverage and discover operational differences between the use cases.
Whatever approach you choose, stick to it. Mixing and matching will confuse your stakeholders and quickly overwhelm your team.
Conclusion
Over the last few years, the SRE profession and role has spread widely outside the walls of Google. Although we never expected this, we are nonetheless thrilled by it. We might be able to say something credible about how we think the discipline will evolve inside Google, but in the wild—well, that’s an
“uncomfortably exciting” proposition
.
One thing we feel pretty sure about is that as you adopt SRE principles into your organization, you will cross many of the same inflection points we did (and some we have not!)—including the need to blur the lines more between where your customers end and where you start.
Engaging with individual customers at this level of operational depth is a rewarding new frontier for us, and we’re still very much on the path. (You can follow along online at the
Google Cloud Platform Blog
.) The further we go, however, the more certain we are that this is a journey that you, too, will need to take.
