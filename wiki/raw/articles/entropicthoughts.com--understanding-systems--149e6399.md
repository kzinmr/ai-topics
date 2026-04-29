---
title: "Understanding systems"
url: "https://entropicthoughts.com/understanding-systems"
fetched_at: 2026-04-29T07:00:51.895640+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Understanding systems

Source: https://entropicthoughts.com/understanding-systems

Some time ago I read an article on what makes a good tutor.
1
I cannot find
the article again, but in the process of writing this I came across the book
Improving Academic Achievement
, which has a chapter that may have inspired
that article:
The Wisdom of Practice: Lessons Learned from the Study of HIghly
Effective Tutors
; Lepper and Woolverton; Academic Press; 2002.
It explicated
many of the things I do when tutoring, so obviously I thought it was a great
article. When I had a side gig as a private tutor, I covered mostly maths and
physics, so that’s how I’ll frame things in this article. The same thing applies
to other fields too, but it might be
harder the further away from maths they
are
.
The main thrust of the lost article (as I remember it) was that effective tutors
are highly empathetic to the level of motivation of their student, and they
quickly adjust the lesson to that. That’s it. That’s the main thing good tutors
do differently. If motivation decreases, they switch to lighter content, or even
transition into non-lesson conversation. If motivation increases, they ramp up
the difficulty of the lesson. Tutoring is, say, 80 % motivation management.
Okay, but that undersells it a little. Lesson difficulty is not fixed for any
topic; it depends on the student. Annoyingly, it even depends on the student’s
level of motivation! The tutor must somehow know what is going to be difficult
and what is going to be easy for their student, in every specific situation.
Here’s how I figured it out when I was tutoring. A lesson with me consisted
basically of me repeatedly (a) selecting an exercise for the student from their
book, and then (b) watching the student work through it.
2
You can guess why
motivation management is a big part of this! It sounds very monotonous and
boring unless done right.
Selecting an exercise for the student is a really fun activity. There needs to
be some thematic variety to break the monotony of the lesson. But then the
exercise should also be just at the limit of the student’s abilities at that
moment, and ideally it should also end up revealing a flawed mental model of
theirs. This meant I could only tutor students in subjects I was good at,
because I had to quickly skim the exercises and visualise the steps to solve
them, to find one in which a flawed mental model would be exposed.
I knew which flawed mental models the student had because that’s what happened
in the watching-them-work step. As the student performs the motions, they
continuously emit clues as to the mental models running in their head. Sometimes
there is something subtly weird about what they do – even if the result works
out in the end – and that’s a potential flawed mental model. If I observed
something weird, I would choose the next exercise to bring that specific mental
model to the forefront. Most of the time, that exercise reveals there was
nothing wrong at all, but sometimes the student does something very wrong in
that exercise, confirming the suspicion.
3
This is also why, with new
students, I would start out by going through a bunch of different exercises.
Open a random page in the book, do one exercise there, then switch to another
random page. The goal of this is for me to calibrate catalogue of mental models
the student uses, and find out which are good and which need improvement.
The student needs to find out about their flawed mental model too, of course.
Many of my students had a learned response to check the solutions in the back of
the book as soon as they had attempted to solve an exercise. I really, really
wanted to tear out the solutions pages from their books and throw them in the
rubbish bin. Looking at the solutions is not a good way to learn.
When the student had attempted to solve an exercise, I would ask them if they
believed their answer was correct. Whatever they answered, I would then ask them
to verify their own solution.
4
Then why did I ask? The strength of their
belief indicates how much work it will take to rip out bad mental models. When
we believe incorrect things strongly, we use our incorrect beliefs as
knowledge
shields
to reject the correct belief. It takes more work to get at a
misconception when it is used as a shield.
How to verify one’s solution is
rarely taught in school, so early on with a student I would have to ask more
leading questions at this stage. There are three main ways to do it:
Use a different approach to solve the same problem, and see if they come out
to the same answer.
Perform a feasibility check by coming up with loose, intuitive bounds for the
answer that would be reasonable for the solution.
Recursively: in a multi-step solution, start with the step one is most
uncertain about, and verify that step in isolation. Continue the depth-first
search until confident in all steps.
Being able to verify one’s own solution is a critical skill, and none of my
students had it before I started working with them.
This interacts with motivation management. It is often demotivating for the
student to finish a solution attempt when the tutor recognises early on that
they are barking up the wrong tree, and that they will fail to verify their
solution. In those cases, I would sometimes step in and ask for immediate
verification.
5
To keep the student on their toes, I would also ask for
immediate verification even when nothing at all was wrong.
I also recognise
that some errors are unproductive (simple slips of the mind) and some errors are
productive (reveal a fundamental misunderstanding.) These should be treated
differently. Unproductive errors can usually be ignored entirely (and this is
another reason to prevent the student from reading the solutions in the book!)
or, if they’re going to cause problems, be casually corrected right away. On the
other hand, productive errors are a great starting point for discussion.
There is an underlying current here. The student learns in part through the
sheer volume of exercise. Without the tutor managing motivation, they would not
be doing as many high quality exercises as they are. But they also learn to
verify their solutions and diagnose their problems. They learn the right
questions to ask to figure out if they are wrong. This is a critical skill
that’s – for some reason – not emphasised elsewhere.
Of course, the tutor already needs to do this: they need to continuously form
hypotheses about their student’s knowledge, and need to select questions to ask
to figure out if they are wrong. Nobody teaches the tutor about their student’s
understanding – they have to figure that out on their own. What’s amazing about
this skill is that it is transferable. It works when trying to learn anything.
When I was a
ta
in computer networking and security in university, I would
walk around to provide assistance during lab hours. A student might observe
something unexpected on their systems, and call me over. I would ask, “What do
you think happened?” Sometimes they needed to be convinced they would not be in
trouble for giving me an incorrect answer, but eventually they’d respond with a
guess.
Then I’d ask, “Okay, and what else could you do that would have a known
consequence only if that is true?” Usually, they
could
think of a way to
verify their hypothesis. They’d perform that action, and discover if their guess
was wrong or right. If it was wrong, we’d go through the loop again.
I never taught them anything. They figured it out on their own.
This is how experienced people understand systems: they continuously form
hypotheses about how the system works, and then they deliberately place
themselves in situations which have a chance of invalidating their hypotheses.
I describe tutoring as “giving students an opportunity to reevaluate their
assumptions, by asking the right questions to expose the critical mechanisms
from their invidial perspectives.”
That’s how tutoring works, but it’s also how to debug broken code, how to learn
how a network is put together, and how to learn to drive a race car. That is how
to learn.
