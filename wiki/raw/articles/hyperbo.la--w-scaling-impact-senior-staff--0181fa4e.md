---
title: "Scaling Myself by Letting My Team Fail"
url: "https://hyperbo.la/w/scaling-impact-senior-staff/"
fetched_at: 2026-04-29T07:02:15.440768+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Scaling Myself by Letting My Team Fail

Source: https://hyperbo.la/w/scaling-impact-senior-staff/

I am currently a Group Tech Lead for a developer productivity organization of 5
teams and 35 engineers. I am jointly accountable for the success of these folks
with the Senior Manager I partner with.
With 5 teams, there is a lot happening concurrently. Each team is committed to 3
or 4 OKRs each quarter; combined with the writing heavy culture, it is rarely
feasible for me to review every document and track every project directly. Each
week, I find I can provide attention to 3 things at most (technical or not), so
protecting my ability to focus has been essential to scaling myself.
Using Cost of Failure as a Proxy for Attention
One technique I’ve developed that has helped me be more ruthless with my focus
is to distinguish between projects where it is ok for folks to fail on their own
versus projects where failure is not permissible or is
expensive
. If it’s ok
for folks to fail, I spend way less energy on these projects.
One easy way I use to determine which projects can’t fail is to listen to
leadership and focus on what they think is important. This might look like:
Finding ways that my teams’ committed roadmaps roll up a set of company “big
rocks”.
Reading the tea leaves around
AI being the next big thing
.
Tracking which OKRs are committed by the larger Foundations organization that
my developer productivity organization rolls up to.
Aligning with my manager during OKR review on what projects we both believe
are
can’t fail
.
Leaning into this technique and being public about it with my broader team also
aligns my actions with the
making opportunities for others
part of the Staff+
role. Leaving projects more loosely defined or less closely supervised provides
space for Senior Engineers to gain project lead experience, gain direct exposure
to the
why
parts of building scalable infrastructure, and build comfort with
ambiguity.
Identifying Skill Gaps
As a precaution to the previously mentioned approach, if I notice a pattern of
repeated failures among team members when they have the freedom to handle tasks
independently, it is crucial to acknowledge that there may be skill gaps.
This
then becomes an area deserving of more dedicated attention. I mostly approach
this area from a project perspective; but sometimes after digging in with the
line engineering manager closer to the project, I might provide focused support
to 1 or 2 ICs who worked on the project. Usually this manifests as a prolonged
1:1 engagement to build up systems thinking skills.
For example, a team I support owns a load-bearing (but legacy!) piece of
infrastructure which has high operational burden and frequently fails to meet
SLAs. Upon setting the direction for the team to improve things, I took a
largely hands off approach to allow the Senior Engineers on the team to flex
some design and project leadership muscles.
But when the changes the team were making
increased
the brittleness of the
system (for example by directly porting bash scripts to golang instead of
writing idiomatic go code) and caused
more
SLA violations, I pivoted my focus
to upskill the team. Some techniques I used were:
Spend hands on time with the team writing code in the services they operate.
Introduce patterns in the codebase (like the
command pattern
) which are
cargo-cultable.
Leading by example to build a culture of maintaining a quality bar in code
review.
Takeaways
A failure mode I sometimes observe with Staff+ engineers is that they struggle
to
give away their LEGOs
and try to have their hand in
everything
their
group touches. This presents a very real risk of burnout, but it also limits the
size of the group one can influence. The ability to
let it go
means other
parts of the organization can carry the torch.
