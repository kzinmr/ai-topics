---
title: "Is the Monaco Grand Prix decided at qualifying?"
url: "https://entropicthoughts.com/is-monaco-decided-at-qualifying"
fetched_at: 2026-06-02T07:05:05.453773+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Is the Monaco Grand Prix decided at qualifying?

Source: https://entropicthoughts.com/is-monaco-decided-at-qualifying

The assignment of starting positions in a race is not random. Instead, drivers
take turns trying to set the fastest lap around the track the day before the
race, and the two equipages with the fastest laps in the final round get to
start on the first row in the race. This introduces a very annoying confounder:
naturally, higher equipage capability improves the chances of winning the race,
but it
also
improves the chances of starting in the first row through
qualifying well.
If a first row equipage wins the race, is that
because
they started in the
first row, or did they start in the first row
because
they were high in
capability on that track, and that’s also why they won? The causal graph looks
like this.
In order to measure the effect of a first row start in this system, we need to
control for equipage capability. One way to do that is to include it as a
separate predictor in a regression analysis. The idea is that the equipage
capability coefficient will eat up most of the effect of equipage capability,
and that leaves the first row start coefficient to contain just the effect of
the first row start.
But
that
requires being able to measure equipage capability. One way to do
that is to take the driver’s championship points at the end of the season, but
the drawback of that is that it doesn’t tell us anything about differences in
equipage capability across different tracks, or as it varies over a season. We
calso cannot use the qualifying results to measure equipage capability, because
the reason we are doing this in the first place is to separate out the effects
of equipage capability from qualifying results.
That’s where I got stuck for a while. Then a couple of years later I had a flash
of insight!
Qualifying proceeds in three rounds. If we take the
worst
result from each
round, that might represent a kind of capability baseline of that equipage. And
it turns out it is a decent proxy for equipage capability, too: if we order
drivers based on their average of this measurement, and compare to the driver’s
championship results, the correlation is +0.82. This means, loosely speaking,
that around 70 % of the variation in the driver’s championship result is
determined by which equipage can drive fast. The other 30 % is luck and race
dynamics such as being skilled at overtakes, etc.
4
On the one hand, I’m
surprised as much as 70 % of the driver’s championship is about driving fast. On
the other hand, maybe that’s not so strange if “driving fast” is what gives
drivers a start in the first row, and a start in the first row is what wins
races? I have not tried to tease those effects apart.
