---
title: "Aligned to whom?"
url: "https://hyperbo.la/w/aligned-to-whom/"
fetched_at: 2026-09-13T10:01:13.816747+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Aligned to whom?

Source: https://hyperbo.la/w/aligned-to-whom/

On safety risk, to those of you who are building agents
: Because you are an
expert in concerns X, Y, and Z, your agent is likely to be phenomenal at these
things and you are not at risk in those domains. But! there are
innumerable
other concerns
that you have either ill- or poorly specified, have no
ability to judge the correctness of for yourself, and cannot possibly evaluate
the risk of.
You are relying very heavily on the priors of the model to do a good job for you
to mitigate that risk. This is extremely in the unknown-unknown territory for
both you and the use of the model.
For me, it is difficult to have very very high confidence in the models’ priors
because I am an expert software engineer and I am not happy (and never have
been) with the default behaviors of the model when producing software. My
expertise in writing software gives me unusually good visibility and it makes me
much less willing to blindly trust its priors in double-entry accounting,
finance, law, operations, or whatever else I cannot personally evaluate at
expert depth.
Software engineers (and recently,
mathematicians
!) at this point are very
familiar with “slop”—model output that, while it does the job, is
bad in some
way
. Every
isRecord
or overly defensive bit of exception handling software
engineers have ever seen from the models is because a non-expert rewarded the
model for these behaviors during training.
The model’s priors are bad.
It’s very important to note that this—the models rewarded for behavior an expert
would consider bad—generalizes to every auto-rater, every judge, every rubric,
every eval, and every researcher as well.
These misalignments compound over time. The models are largely not trained in
ways that require them to evolve systems through
changes stacked one after the
other
. The models do not have a
fear of future regret
. Having
been inside several of the sausage factories,
long-term coherence
through use
of agentic work product is a very unsolved problem.
And in spite of this, you
will
have people prompting “make me $1B make no
mistakes”. That is a drastically unspecified task!
There is no such thing as an unhackable grader and the models are rewarded for
being efficient. This means the models will be trained to take shortcuts that
the graders permit if it helps them achieve their goals. But there is no
universal definition of a permissible shortcut. What is clever optimization to
one person is reckless, incorrect, or unethical to another. The permissible
shortcuts depend on who you are and what your values are. To solve this—to solve
alignment—is irreducible complexity.
Thanks to Karan Lyons for the AI Punnett square and reviewing early drafts of
this post, to David Adrian and Bryan Berg for reviewing early drafts, and to
my fellow Snoopy friends for helping me refine these thoughts.
