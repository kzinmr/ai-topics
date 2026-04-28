---
title: "an engineer's perspective on hiring"
url: "https://jyn.dev/an-engineers-perspective-on-hiring/"
fetched_at: 2026-04-28T07:02:50.585640+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# an engineer's perspective on hiring

Source: https://jyn.dev/an-engineers-perspective-on-hiring/

note for my friends: this post is targeted at companies and engineering managers. i know you know that hiring sucks and companies waste your time. this is a business case for why they shouldn't do that.
hiring sucks
most companies suck at hiring. they waste everyone’s time (i once had a 9-round interview pipeline!), they
chase the trendiest programmers
, and they
can’t even tell programmers apart from an LLM
. in short,
they are not playing moneyball
.
things are bad for interviewees too. some of the best programmers i know (think people maintaining the rust compiler) can’t get jobs because
they interview poorly under stress
. one with 4 years of Haskell experience and 2 years of Rust experience was labeled as “non-technical” by a recruiter. and of course, companies repeatedly ghost people for weeks or months about whether they actually got a job.
this post explores why hiring is hard, how existing approaches fail, and what a better approach could look like. my goal, of course, is to get my friends hired.
reach out to me
if you like the ideas here.
what makes a good interview
before i start talking about my preferred approach, let’s start by establishing some (hopefully uncontroversial) principles.
interviews should:
differentiate
. be able to tell the difference between a senior programmer and a marketer using chatgpt.
be applicable
. reflect the actual job duties.
this includes coding. but it also includes architecture design, PR review, documentation, on and on and on. all good senior software engineers are generalists.
think long term
. select for applicants who will be good employees for years to come, not just in the next quarter.
be time efficient
. spend as little time as possible interviewing.
engineer time is expensive.
be respectful
. respect the applicant and their time.
if you don't respect the applicant, you will select for people who don't respect themselves, and drive away the best applicants.
"but i want to select for people that don't respect themselves so i can pay them less"—get the hell off my site and don't come back.
there is also a 6th criteria that's more controversial. let's call it
taste
. an engineer with poor
taste
can ship things very quickly at the expense of leaving a giant mess for everyone else on the team to clean up. measuring this is very hard but also very important. conversely,
someone who spends time empowering the rest of their team has a multiplicative effect on their team's productivity
(c.f.
"Being Glue"
).
let's look at some common interviews and how they fare.
live coding, often called "leetcode interviews"
fails on
differentiating, applicability, respect, taste
. gives very little signal about
long term value
. live coding
cannot distinguish a senior programmer from a marketer using chatGPT
, and most interview questions have very little to do with day-to-day responsibilities. all good software engineers are generalist and live coding does not select for generalists.
you can augment live coding with multiple rounds of interviews, each of which tests one of the above responsibilities. but now you lose
time efficiency
; everything takes lots of engineer time. doing this despite the expense is a show of wealth, and now you are no longer playing moneyball.
additionally, people with lots of experience often find the experience demeaning, so you are filtering out the best applicants. a friend explicitly said "I have 18 years of experience on GitHub; if you can't tell I'm a competent programmer from that it's not a good fit."
something not often thought about is that this also loses you
taste
. the code that someone puts together under pressure is not a reflection of how they normally work, and does not let you judge if your engineers will like working with them.
take-home interviews
fails on
differentiating
and
respect
, and partially on
applicability
. take home interviews are very easy for chatGPT to game and have all the other problems of live interviews, except that they remove the "interview poorly under stress" component. but they trade off a fundamental
time asymmetry
with the applicant, which again drives away the best people.
architecture design
this does a lot better. you can't use chatGPT to fake an architecture interview. it fails at
applicability
(you don't ever see the applicant's code). at first glance it appears to give you some insight into
taste
, but often it is measuring "how well does the applicant know the problem domain" instead of "how does the applicant think about design problems", so you have to be careful about over-indexing on it.
"meet the team"
i haven't seen this one a lot for external interviews, but i see it very commonly for internal transfers within a company. it has much of the same tradeoffs as architecture design interviews, except it usually isn't trying to judge skills at all, mostly personality and "fit" (i.e. it fails on
differentiating
and partially on
applicability
). i think it makes sense in environments where the candidate has a very strong recommendation and there's little competition for the position; or if you have some other reason to highly value their skills without a formal assessment.
extended essays and work samples
this is an interesting one. i've only ever seen it from
Oxide Computer Company
. i like it really quite a lot. the process looks like this:
the applicant submits samples of their existing work (or writes new documents specially for the interview)
the applicant writes detailed responses to 8 questions about their values, work, career, and goals.
the applicant goes through 9 hours of interviews with several oxide employees.
this does really really well on nearly every criteria (including
respect
—note that the time spent here is symmetric, it takes a
long
time for Oxide's engineers to read that much written material).
it fails on
time efficiency
. i have not gone through this process, but based on the questions and my knowledge of who gets hired at oxide, i would expect
just
the written work to take at around 5-15 hours of time for a single application. given oxide and their goals, and the sheer number of people who apply there, i suspect they are ok with that tradeoff (and indeed probably value that it drives away people who aren't committed to the application). but most companies are not oxide and cannot afford this amount of time on both sides.
if i were to take ideas from the oxide process without sacrificing too much time, i’d keep "you write the code ahead of time and discuss it in the interview". this keeps the advantage of take-home interviews—no time pressure, less stressful environment—while adding a
symmetric time
component that makes talented engineers less likely to dismiss the job posting out of hand, without an enormous up-front expenditure of time. and discussing the code live filters out people who just vibecoded the whole thing (they won't be able to explain what it does!) while giving everyone else a chance to explain their thinking, helping with
applicability
and
taste
.
this still has some
time asymmetry
if the applicant doesn’t have existing open source work they want to show to an interviewer, but it’s a lot less than 5-15 hours, and the company is forced to dedicate some of their own engineer time, so they have motivation not to “throw work over the wall”, showing respect for the applicant.
code review
this one i’ve also only ever seen once. the format is that the interviewer writes some mediocre code ahead of time and asks the applicant how they would improve it. i did very well on this format so i'm biased, but i like it a lot. it aces all our criteria:
it reverses the
time asymmetry
and reduces the amount of
time spent
. the interviewer makes one up front time commitment, the applicant makes no up front commitment, and they spend the same amount of time per interview.
it’s
applicable
: you see how the applicant gives interpersonal feedback; discussions about the code naturally lead into discussions about design; and you get information about their sense of taste.
imagining a better interview process
if i were a hiring manager, i would use a combo of a code review interview and a work sample discussed live, giving precedence to the code review and telling the applicant ahead of time that the work sample doesn’t have to be perfect.
programming is fundamentally a collaborative process. having the applicant collaborate on both sides (reviewing and authoring) shows you a lot about how they work, and signals to them that you care about more than the equivalent of their SAT score.
i also suggest there always be at least one interview between the applicant and their future manager (this seems to already be common practice—yay!). "people don't quit jobs, they quit bosses": letting them meet ahead of time saves everyone pain down the road.
thank you for reading! i hope this inspires you to change your own hiring processes, or at least to write a comment telling me why i'm wrong ^^. you can reach me by
email
if you want to comment privately.
P.S. other interview processes
pairing
a friend worked at a Pivotal Labs where the primary job responsibility was to pair with client developers. the interview process was for a candidate to pair with an existing employee for a whole day and "shadow" them. he points to
Nat Bennett's notes on the interview process
as a more detailed writeup.
P.P.S. measuring interview effectiveness
the most interesting comment i got in response to this post was about "red-teaming" the interview to see how effective it is. for example:
taking existing employees and putting them through the interview process and seeing whether it suggests hiring them again. if it doesn't, it's either horribly noisy or filtering out good candidates or both.
"regret analysis": following the careers of rejected candidates to see who went on to do interesting things. if so, find out which part of the interview process failed and change it.
the friend who suggested this said both ideas were categorically rejected by management and they continued to send him mediocre resumes for people he didn't want to hire.
