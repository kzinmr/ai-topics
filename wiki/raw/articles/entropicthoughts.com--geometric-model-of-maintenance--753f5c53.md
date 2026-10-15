---
title: "The geometric model of maintenance"
url: "https://entropicthoughts.com/geometric-model-of-maintenance"
fetched_at: 2026-10-14T10:01:16.202683+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# The geometric model of maintenance

Source: https://entropicthoughts.com/geometric-model-of-maintenance

Let’s say
we have a way of labeling each commit
as either “new development” or
“maintenance”. Then we can count how many commits of each type there are in a
month.
1
This article will assume that necessary maintenance gets performed,
and if maintenance is not performed, that’s because it wasn’t strictly
necessary
from the aggregate users’ points of view. I know a lot of people
would object to that assumption because maintenance they think of as necessary
is not performed, but try to suspend your disbelief. If you keep using the
software even when that thing is not getting fixed, how necessary is that thing
really
to keep you around as a user?
Possibly better, we can count
how much
complexity has been handled
in a month.
2
In this analysis, I am counting the
gross commit size, i.e. additions plus deletions, as the amount of effort that
went into the commit. One can argue that this is a bad measurement of effort,
but it’s the best I have, and in my experience, on longer timescales like the
ones we look at here, it’s not so bad.
The following plot shows the cumulative effort that has gone into the
development of tmux since its beginning to the day I start writing this article.
We will look first at the black curve, which represents effort spent adding
features to tmux. From left to right:
In the first month of the repository, a few thousand lines of feature work are
present almost from the start.
From the start in 2008 to 2010, tmux saw rather intense activity at
around 30,000 lines of new development effort per year.
Then new development slowed down, and between 2010 and 2026, it happened at a
fairly steady pace of 8,000 lines of effort per year.
As of today, tmux stands at just over 230,000 lines of effort of new
development that have happened throughout its history.
To see how much effort has been spent on maintenance, we perform the same
exercise but with the red curve instead.
Maintenance started dipping behind new development early on, but then traced
fairly closely to new development between 2008 and 2014.
After that, maintenance took off at a rate of 30,000 lines of effort per year,
continuing at that pace until 2022.
Then it slowed down again to around 10,000 lines of effort per year.
As of today, tmux has required around 430,000 lines of effort for maintenance.
In other words, of the total roughly 660,000 lines of effort spent on tmux, only
about a third has been on new development. This has changed over time, and we
can find roughly four regimes in the project’s history.
2008–2010: Total effort is 60,000 lines per year. About 50 % of that is maintenance.
2010–2014: Total effort is 16,000 lines per year. About 50 % of that is
maintenance.
2014–2022: Total effort is 38,000 lines per year. About 80 % of that is
maintenance.
2022–2026: Total effort is 18,000 lines per year. About 55 % of that is
maintenance.
This is not quite the continuous increase of maintenance fraction predicted by
the threshold model. To be sure, we should also check visually. The prediction
of the threshold model is represented by the dotted red line.
3
Note that we
are not using the threshold model to predict the
fraction
of maintenance here,
but instead applying it primitively for what it says about the
absolute size
of the maintenance demand. In Shore’s original application, he was able to
predict the fraction of maintenance through the threshold model, because the
model was allowed to also determine the rate of new development (through a fixed
monthly work rate.). We don’t do that, because we have the real new development
rate of the tmux project. It wouldn’t make sense to impose on the data an
assumed new development rate that we already know isn’t true.
All the way from 2008 to 2022, the simple threshold model does actually fairly
closely predict the amount of maintenance tmux has required. But the exponential
nature of the threshold model means its prediction eventually goes up faster
than actual maintenance performed.
4
If new development had been reduced to
make room for the maintenance work, as Shore argues is the case for many
corporate projects, then maintenance would have leveled off as new development
grinds to a halt. But clearly, in the tmux case, new development does not reduce
that much
to make room for maintenance work. And the same is true for all
projects I surveyed, including corporate-backed ones whose primary contributers
are on a payroll.
This means the model fit will likely worsen as time goes on.
The threshold model is also not a great fit for some other projects, where it
generally overestimates the amount of maintenance performed. As one example,
maintenance work has made up 63 % of the effort spent on nginx to date, but the
threshold model suggests it should be 81 %. Other projects where the model
overestimates the maintenance requirements are Rust, VSCode, and Go.
In contrast, the model underestimates the amount of maintenance required for
Neovim. The Neovim project has been maintenance-heavy from the start, and
through its history, 83 % of the work on Neovim has been maintenance, but the
threshold model suggests it should be 70 %.
However, the more general problem with the threshold model is one of timing. This is
best illustrated with Syncthing.
The threshold model lands close to the correct lifetime maintenance fraction
here (70 % vs. the real 67 %) but it is nowhere near following the actual maintenance
curve.
An apologist could argue that the lack of curve-following is not because the
model is wrong, but because the Syncthing project is an outlier that decided to
front-load a bunch of maintenance. Unfortunately, Syncthing isn’t the only
project where this happens, and it’s actually a symptom of the big flaw of the
threshold model. Given a constant level of new feature development, it predicts
maintenance will grow exponentially.
5
Shore would argue that we cannot base
our judgment on a constant level of new feature development because new features
should slow down as maintenance takes over the total work effort. But in the
projects I’ve looked at, new development seems to happen at a relatively
constant level.
That doesn’t seem to be what happens in practise in the
projects I’ve looked at.
