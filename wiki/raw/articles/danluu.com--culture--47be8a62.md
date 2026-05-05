---
title: "Culture matters"
url: "https://danluu.com/culture/"
fetched_at: 2026-05-05T07:01:30.295757+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Culture matters

Source: https://danluu.com/culture/

Three major tools that companies have to influence behavior are incentives, process, and culture. People often mean different things when talking about these, so I'll provide an example of each so we're on the same page (if you think that I should be using a different word for the concept, feel free to mentally substitute that word).
Getting people to show up to meetings on time
Incentive: dock pay for people who are late
Process: don't allow anyone who's late into the meeting
Culture: people feel strongly about showing up on time
Getting people to build complex systems
Incentive: require complexity in promo criteria
Process: make process for creating or executing on a work item so heavyweight that people stop doing simple work
Culture: people enjoy building complex systems and/or building complex systems results in respect from peers and/or prestige
Avoiding manufacturing defects
Incentive: pay people per good item created and/or dock pay for bad items
Process: have QA check items before shipment and discard bad items
Culture: people value excellence and try very hard to avoid defects
If you read "old school" thought leaders, many of them advocate for a culture-only approach, e.g.,
Ken Thompson saying, to reduce bug rate, that tools (which, for the purposes of this post, we'll call process) aren't the answer, having people care to and therefore decide to avoid writing bugs is the answer
or Bob Martin saying "
The solution to the software apocalypse is not more tools. The solution is better programming discipline
."
The emotional reaction those kinds of over-the-top statements evoke combined with the ease of rebutting them has led to a backlash against cultural solutions, leading people to say things like "you should never say that people need more discipline and you should instead look at the incentives of the underlying system", in the same way that the 10x programmer meme and the associated comments have caused a backlash that's led to people to say things like
velocity doesn't matter at all
or there's absolutely no difference in velocity between programmers (
as Jamie Brandon has noted, a lot of velocity comes down to caring about and working on velocity
, so this is also part of the backlash against culture).
But if we look at quantifiable output, we can see that, even if processes and incentives are the first-line tools a company should reach for, culture also has a large impact. For example, if we look at manufacturing defect rate, some countries persistently have lower defect rates than others on a timescale of decades, generally robust across companies, even when companies are operating factories in multiple countries and importing the same process and incentives to each factory to the extent that's possible, due to cultural differences that impact how people work.
Coming back to programming, Jamie's post on "moving faster" notes:
The main thing that helped is actually wanting to be faster.
Early on I definitely cared more about writing 'elegant' code or using fashionable tools than I did about actually solving problems. Maybe not as an explicit belief, but those priorities were clear from my actions.
I probably also wasn't aware how much faster it was possible to be. I spent my early career working with people who were as slow and inexperienced as I was.
Over time I started to notice that some people are producing projects that are far beyond what I could do in a single lifetime. I wanted to figure out how to do that, which meant giving up my existing beliefs and trying to discover what actually works.
I was lucky to have the opposite experience starting out since my first full-time job was at Centaur, a company that, at the time, had very high velocity/productivity. I'd say that I've only ever worked on one team with a similar level of productivity, and that's my current team, but my current team is fairly unusual for a team at a tech company (e.g., the median level on my team is "senior staff"). A side effect of having started my career at such a high velocity company is that I generally find the pace of development slow at big companies and I see no reason to move slowly just because that's considered normal. I often hear similar comments from people I talk to at big companies who've previously worked at non-dysfunctional but not even particularly fast startups. A regular survey at one of the trendiest companies around asks "Do you feel like your dev speed is faster or slower than your previous job?" and the responses are bimodal, depending on whether the respondent came from a small company or a big one (with dev speed at TrendCo being slower than at startups and faster than at larger companies).
There's a story that,
IIRC, was told by Brian Enos
, where he was practicing timed drills with the goal of practicing until he could complete a specific task at or under his usual time. He was having a hard time hitting his normal time and was annoyed at himself because he was slower than usual and kept at it until he hit his target, at which point he realized he misremembered the target and was accidentally targeting a new personal best time that was better than he thought was possible. While it's too simple to say that we can achieve anything if we put our minds to it,
almost none of us are operating at anywhere near our capacity and what we think we can achieve is often a major limiting factor
. Of course, at the limit, there's a tradeoff between velocity and quality and you can't get velocity "for free", but, when it comes to programming,
we're so far from the Pareto frontier that there are free wins
if you just
realize that they're available
.
One way in which culture influences this is that people often absorb their ideas of what's possible from the culture they're in. For a non-velocity example, one thing I noticed after attending
RC
was that a lot of speakers at the well-respected non-academic non-enterprise tech conferences, like Deconstruct and Strange Loop, also attended RC. Most people hadn't given talks before attending RC and, when I asked people, a lot of people had wanted to give talks but didn't realize how straightforward the process for becoming a speaker at "big" conferences is (have an idea, write it down, and then submit what you wrote down as a proposal). It turns out that giving talks at conferences is easy to do and a major blocker for many folks is just knowing that it's possible. In an environment where lots of people give talks and, where people who hesitantly ask how they can get started are told that it's straightforward, a lot of people will end up giving talks. The same thing is true of blogging, which is why a disproportionately large fraction of widely read programming bloggers started blogging seriously after attending RC. For many people, the barrier to starting a blog is some combination of realizing it's feasible to start a blog and that, from a technical standpoint, it's very easy to start a blog if you just pick any semi-reasonable toolchain and go through the setup process. And then, because people give talks and write blog posts, they get better at giving talks and writing blog posts so, on average, RC alums are probably better speakers and writers than random programmers even though there's little to no skill transfer or instruction at RC.
Another kind of thing where culture can really drive skills are skills that are highly attitude dependent. An example of this is debugging. As Julia Evans has noted,
having a good attitude is a major component of debugging effectiveness
. This is something Centaur was very good at instilling in people, to the point that nearly everyone in my org at Centaur would be considered a very strong debugger by tech company standards.
At big tech companies, it's common to see people give up on bugs after trying a few random things that didn't work. In one extreme example, someone I know at a mid-10-figure tech company said that it never makes sense to debug a bug that takes more than a couple hours to debug because engineer time is too valuable to waste on bugs that take longer than that to debug, an attitude this person picked up from the first team they worked on. Someone who picks up that kind of attitude about debugging is unlikely to become a good debugger until they change their attitude, and many people, including this person, carry the attitudes and habits they pick up at their first job around for quite a long time.
By tech standards, Centaur is an extreme example in the other direction. If you're designing a CPU, it's not considered ok to walk away from a bug that you don't understand. Even if the symptom of the bug isn't serious, it's possible that the underlying cause is actually serious and you won't observe the more serious symptom until you've shipped a chip, so you have to go after even seemingly trivial bugs. Also, it's pretty common for there to be no good or even deterministic reproduction of a bug. The repro is often something like "run these programs with these settings on the system and then the system will hang and/or corrupt data after some number of hours or days". When debugging a bug like that, there will be numerous wrong turns and dead ends, some of which can eat up weeks or months. As a new employee watching people work on those kinds of bugs, what I observed was that people would come in day after day and track down bugs like that, not getting frustrated and not giving up. When that's the culture and everyone around you has that attitude, it's natural to pick up the same attitude. Also, a lot of practical debugging skill is applying tactical skills picked up from having debugged a lot of problems, which naturally falls out of spending a decent amount of time debugging problems with a positive attitude, especially with exposure to hard debugging problems.
Of course, most bugs at tech companies don't warrant months of work, but there's a big difference between intentionally leaving some bugs undebugged because some bugs aren't worth fixing and having poor debugging skills from never having ever debugged a serious bug and then not being able to debug any bug that isn't completely trivial.
Cultural attitudes can drive a lot more than individual skills like debugging. Centaur had, per capita, by far the lowest serious production bug rate of any company I've worked for, at well under one per year with ~100 engineers. By comparison, I've never worked on a team 1/10th that size that didn't have at least 10x the rate of serious production issues. Like most startups, Centaur was very light on process and it was also much lighter on incentives than the big tech companies I've worked for.
One component of this was that there was a culture of owning problems, regardless of what team you were on. If you saw a problem, you'd fix it, or, if there was a very obvious owner, you'd tell them about the problem and they'd fix it. There weren't roadmaps, standups, kanban, or anything else to get people to work on important problems. People did it without needed to be reminded or prompted.
That's the opposite of what I've seen at two of the three big tech companies I've worked for, where the median person avoids touching problems outside of their team's mandate like the plague, and someone who isn't politically savvy who brings up a problem to another team will get a default answer of "sorry, this isn't on our roadmap for the quarter, perhaps we can put this on the roadmap in [two quarters from now]", with the same response repeated to anyone naive enough to bring up the same issue two quarters later. At every tech company I've worked for, huge, extremely costly, problems slip through the cracks all the time because no one wants to pick them up. I never observed that happening at Centaur.
A side effect of big company tech culture is that someone who wants to actually do the right thing can easily do very high (positive) impact work by just going around and fixing problems that any intern could solve, if they're willing to ignore organizational processes and incentives. You can't shake a stick without
hitting a problem that's worth more to the company than my expected lifetime earnings
and it's easy to knock off multiple such problems per year.
Of course, the same forces that cause so many trivial problems to not get solved mean that people who solve those problems don't get rewarded for their work
.
Conversely, in eight years at Centaur, I only found one trivial problem whose fix was worth more than I'll earn in my life because, in general, problems would get solved before they got to that point. I've seen various big company attempts to fix this problem using incentives (e.g., monetary rewards for solving important problems) and process (e.g.,
making a giant list of all projects/problems, on the order of 1000 projects, and having a single person order them, along with a bureaucratic system where everyone has to constantly provide updates on their progress via JIRA so that PMs can keep sending progress updates to the person who's providing a total order over the work of thousands of engineers
), but none of those attempts have worked even half as well as having a culture of ownership (to be fair to incentives, I've heard that FB uses monetary rewards to good effect, but
I've failed FB's interview three times
, so I haven't been able to observe how that works myself).
Another component that resulted in a relatively low severe bug rate was that, across the company at Centaur, people cared about quality in a way that I've never seen at a team level let alone at an org level at a big tech company. When you have a collection of people who care about quality and feel that no issue is off limits, you'll get quality. And when you onboard people, as long as you don't do it so quickly that the culture is overwhelmed by the new hires, they'll also tend to pick up the same habits and values, especially when you hire new grads. While it's not exactly common, there are plenty of small firms out there with a culture of excellence that generally persists without heavyweight processes or big incentives, but this doesn't work at big tech companies since they've all gone through a hypergrowth period where it's impossible to maintain such extreme (by mainstream standards) cultural values.
So far, we've mainly discussed companies transmitting culture to people, but something that I think is no less important is how people then carry that culture with them when they leave. I've been
reasonably successful since changing careers from hardware to software
and I think that, among the factors that are under my control, one of the biggest ones is that I picked up effective cultural values from the first place I worked full-time and continue to operate as in the same way, which is highly effective. I've also seen this in other people who, career-wise, "grew up" in a culture of excellence and then changed to a different field where there's even less direct skill transfer, e.g., from skiing to civil engineering. Relatedly, if you read books from people who discuss the reasons why they were very effective in their field, e.g.,
Practical Shooting by Brian Enos
,
Playing to Win by Dan Sirlin
, etc., the books tend to contain the same core ideas (serious observation and improvement of skills, the importance of avoiding emotional self-sabotage, the importance of intuition, etc.).
Anyway, I think that cultural transmission of values and skills is an underrated part of choosing a job (some things I would consider overrated are
prestige
and
general reputation
and that people should be thoughtful about what cultures they spend time in because not many people are able to avoid at least somewhat absorbing the cultural values around them.
Although this post is oriented around tech, there's nothing specific to tech about this. A classic example is how idealistic students will go to law school with the intention of doing "save the world" type work and then absorb the
prestige-transmitted cultural values
of students around then go into the most prestigious job they can get which, when it's not a clerkship, will be a "BIGLAW" job that's the opposite of "save the world" work. To first approximation, everyone thinks "that will never happen to me", but from having watched many people join organizations where they
initially find the values and culture very wrong
, almost no one is able to stay without, to some extent, absorbing the values around them;
very few people are ok with everyone around them looking at them like they're an idiot for having the wrong values
.
Appendix: Bay area culture
One thing I admire about the bay area is how infectious people's attitudes are with respect to trying to change the world. Everywhere I've lived, people gripe about problems (the mortgage industry sucks, selling a house is high friction, etc.). Outside of the bay area, it's just griping, but in the bay, when I talk to someone who was griping about something a year ago, there's a decent chance they've started a startup to try to address one of the problems they're complaining about. I don't think that people in the bay area are fundamentally different from people elsewhere, it's more that when you're surrounded by people who are willing to walk away from their jobs to try to disrupt an entrenched industry, it seems pretty reasonable to do the same thing (which also leads to network effects that make it easier from a "technical" standpoint, e.g., easier fundraising).
There's a kind of earnestness in these sorts of complaints and attempts to fix them that's easy to mock
, but
that earnestness is something I really admire
.
Of course,
not all of bay area culture is positive
. The bay has, among other things,
a famously flaky culture
to an extent I found shocking when I moved there. Relatively early on in my time there, I met some old friends for dinner and texted them telling them I was going to be about 15 minutes late. They were shocked when I showed up because they thought that saying that I was going to be late actually meant that I wasn't going to show up (another norm that surprised me that's an even more extreme version was that, for many people, not confirming plans shortly before their commencement means that the person has cancelled, i.e., plans are cancelled by default).
A related norm that I've heard people complain about is how management and leadership will say yes to everything in a "people pleasing" move to avoid conflict, which actually increases conflict as people who heard "yes" as a "yes" and not as "I'm saying yes to avoid saying no but don't actually mean yes" are later surprised that "yes" meant "no".
Appendix: Centaur's hiring process
One comment people sometimes have when I talk about Centaur is that they must've had some kind of incredibly rigorous hiring process that resulted in hiring elite engineers, but the hiring process was much less selective than any "brand name" big tech company I've worked for (Google, MS, and Twitter) and not obviously more selective than boring, old school, companies I've worked for (IBM and Micron). The "one weird trick" was onboarding, not hiring.
For new grad hiring (and, proportionally, we hired a lot of new grads), recruiting was more difficult than at any other company I'd worked for. Senior hiring wasn't difficult because Centaur had a good reputation locally, in Austin, but among new grads, no one had heard of us and no one wanted to work for us. When I recruited at career fairs, I had to stand out in front of our booth and flag down people who were walking by to get anyone to talk to us. This meant that we couldn't be picky about who we interviewed. We really ramped up hiring of new grads around the time that Jeff Atwood popularized the idea that there are a bunch of fake programmers out there applying for jobs and that you'd end up with programmers who can't program if you don't screen people out with basic coding questions in his very influential post,
Why Can't Programmers.. Program?
(the bolding below is his):
I am disturbed and appalled that any so-called programmer would apply for a job without being able to write the simplest of programs
. That's a slap in the face to anyone who writes software for a living. ... It's a shame you have to do so much pre-screening to
have the luxury of interviewing programmers who can actually program
. It'd be funny if it wasn't so damn depressing
Since we were a relatively coding oriented hardware shop (verification engineers primarily wrote software and design engineers wrote a lot of tooling), we tried asking a simple coding question where people were required to code up a function to output Fibonacci numbers given a description of how to compute them (the naive solution was fine; a linear time or faster solution wasn't necessary). We dropped that question because no one got it without being walked through the entire thing in detail, which meant that the question had zero discriminatory power for us.
Despite not really asking a coding question, people did things like write hairy concurrent code (internal processor microcode, which often used barriers as the concurrency control mechanism) and create tools at a higher velocity and lower bug rate than I've seen anywhere else I've worked.
We were much better off avoiding hiring the way everyone else was because that meant we tried to and did hire people that other companies weren't competing over. That wouldn't make sense if other companies were using techniques that were highly effective but other companies were doing things like asking people to code FizzBuzz and then whiteboard some algorithms. While
one might expect that doing algorithms interviews would result in hiring people who can solve the exact problems people ask about in interviews, but this turns out not to be the case
.
The other thing we did was have much less of a prestige filter than most companies
, which also let us hire great engineers that other companies wouldn't even consider.
We did have some people who didn't work out, but it was never because they were "so-called programmers" who couldn't "write the simplest of programs". I do know of two cases of "fake programmers being hired who literally couldn't program, but both were at prestigious companies that have among the most rigorous coding interviews done at tech companies. In one case, it was discovered pretty quickly that the person couldn't code and people went back to review security footage from the interview and realized that the person who interviewed wasn't the person who showed up to do the job. In the other, the person was able to sneak under the radar at Google for multiple years before someone realized that the person never actually wrote any code and tasks only got completed when they got someone else to do the task. The person who realized eventually scheduled a pair programming session, where they discovered that the person wasn't able to write a loop, didn't know the difference between
=
and
==
, etc., despite being a "senior SWE" (L5/T5) at Google for years.
I'm not going to say that having coding questions will never save you from hiring a fake programmer, but the rate of fake programmers appears to be very low enough that a small company can go a decade without hiring a fake programmer without asking a coding question and larger companies that are targeted by scammers still can't really avoid them even after asking coding questions.
Appendix: importing culture
Although this post is about how company culture impacts employees, of course employees impact company culture as well. Something that seems underrated in hiring, especially of senior leadership and senior ICs, is how they'll impact culture. Something I've repeatedly seen, both up close, and from a distance, is the hiring of a new senior person who manages to import their culture, which isn't compatible with the existing company's culture, causing serious problems and, frequently, high attrition, as things settle down.
Now that I've been around for a while, I've been in the room for discussions on a number of very senior hires and I've never seen anyone else bring up whether or not someone will import incompatible cultural values other than really blatant issues, like the person being a jerk or making racist or sexist comments in the interview.
Thanks to Peter Bhat Harkins, Laurence Tratt, Julian Squires, Anja Boskovic, Tao L., Justin Blank, Ben Kuhn, V. Buckenham, Mark Papadakis, and Jamie Brandon for comments/corrections/discussion.
