---
title: "Predicting Peace"
url: "https://entropicthoughts.com/forecasting-peace"
fetched_at: 2026-10-06T10:01:35.143719+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Predicting Peace

Source: https://entropicthoughts.com/forecasting-peace

In the conflict episode termination dataset, the
ucdp
have coded intensity as
a binary variable:
low intensity
is 25–1000 annual battle deaths, and more
than that counts as a full-scale
war
. This is a dichotomisation, meaning
it
throws a third of the data in the rubbish bin
. Fortunately, the
ucdp
publishes
separate data sets for battle deaths, and both data sets are indexed by conflict
id and year, meaning we can inner join them to get a complete data set of both
durations and battle deaths.
We cannot include the raw sum of battle deaths as a predictor, because then it
would leak the duration of the conflict. What we can do is count the average
number of yearly battle deaths as the
intensity
of the conflict, and include
that as a predictor. However, the distribution of battle deaths is extremely
heavy-tailed.
This chart goes out so far to the right because
there are data points there
.
Almost all conflicts have a high battle death rate; the median is nearly 100
deaths per year. Yet there are a handful of conflicts that are staggeringly
violent at more than 10,000 battle deaths per year. The worst one has over
100,000 battle deaths per year. This handful of really deadly conflicts in the
pc
age are
Ethiopian Tigray war (2020–2022): 103,000 battle deaths/year.
Russia–Ukraine (2022–): 80,800 battle deaths/year.
Ethiopia–Eritrea (1998–2000): 32,700 battle deaths/year.
Syrian civil war (2011–2024): 20,500 battle deaths/year.
Israel–Palestine (2018–ongoing): 12,200 battle deaths/year.
This is insanity.
32,000 battle deaths per year is almost 100 people dying every
day. And that’s just among combatants, not counting civilians. I don’t even want
to look up civilian casualties.
What is going on in the world?
Deep breaths.
I sometimes have to remind myself why I do this. The examples in this article
are gruesome, but my hope is that (a) people realise that these things really
happen in real life, and (b) at least one reader will make the world a better
place using the tools I share.
If we take the logarithm of the battle death rate we get a more tractable
distribution.
Here we have taken the logarithm base ten, so that the number indicates how many
zeroes there are in the number. For example, 4 should be read as 10,000. From
this plot, it is clear that the median is somewhere around 100 annual battle
deaths. The standard deviation is nearly an order of magnitude.
When we include this variable in the model, the variable that indicated whether
the fight was over territory or government drops out. It seems that it mostly
served as a proxy for the level of violence in the conflict. The shape \(k\) goes
up to 0.7, and to get the scale, we need an estimation of the order of magnitude
of the intensity.
Log-intensity
1
2
3
4
5
Interstate war
\(\lambda\) = 0.4
1.7
8.7
43
214
Civil war
\(\lambda\) = 0.8
3.7
19
92
460
For interpretability reasons, we can convert this to a probability of peace when
ignorant of their duration
Log-intensity
1
2
3
4
5
Interstate war
74 %
32 %
8 %
2 %
<1 %
Civil war
52 %
17 %
4 %
1 %
<1 %
This would indicate probabilities of <1 % for the Ukraine conflict (interstate
ware with annual battle death rate \(10^5\)), and 4 % for the Sudan conflict (civil
war with annual battle death rate \(10^3\)). However, we also need to account for
their duration.
First, for interstate wars:
Log-intensity
1
2
3
4
5
1 year
77 %
40 %
15 %
5 %
2 %
2 years
67 %
33 %
12 %
4 %
1 %
3 years
62 %
30 %
11 %
4 %
1 %
4 years
59 %
27 %
10 %
3 %
1 %
5 years
56 %
26 %
9 %
3 %
1 %
5–10 years
53 %
23 %
8 %
3 %
<1 %
10–20 years
47 %
20 %
7 %
2 %
<1 %
20–40 years
41 %
17 %
6 %
2 %
<1 %
>40 years
33 %
14 %
4 %
1 %
<1 %
and then for civil wars:
Log-intensity
1
2
3
4
5
1 year
59 %
26 %
9 %
3 %
1 %
2 years
49 %
21 %
7 %
2 %
<1 %
3 years
45 %
18 %
6 %
2 %
<1 %
4 years
42 %
17 %
6 %
2 %
<1 %
5 years
40 %
16 %
5 %
2 %
<1 %
5–10 years
37 %
14 %
5 %
2 %
<1 %
10–20 years
32 %
12 %
4 %
1 %
<1 %
20–40 years
27 %
10 %
3 %
1 %
<1 %
>40 years
22 %
8 %
2 %
<1 %
<1 %
Of course, we don’t actually have data to fill all these fine-grained buckets.
We have made assumptions about how the data we do have are related to each
other, and used that to interpolate and extrapolate to where data is missing.
With this, our forecast for the two conflicts we opened with should be
Question
By contention
By raw intensity
Ukraine
21 %
1 %
Sudan
12 %
6 %
Well … I’m not sure what I think about that. Our model leads us to predict 1 %
for
every
extremely high-intensity (\(10^5\)) conflict. That’s obviously the
wrong prediction: those conflicts
do
end far sooner than in the 100 years
implied by the 1 % success rate. I would personally maybe not distinguish
between conflict intensities above \(10^3\), and use the probabilities for \(10^3\)
conflicts for those too. We can encode that intuition into the model by breaking
the intensity up into three bands:
Low intensity: fewer than 50 annual battle deaths. (30 % of the data.)
High intensity: more than 200 annual battle deaths. (31 % of the data.)
In between, we find the median, baseline intensity. The shape of the Weibull
distribution fitted to these predictors is 0.6.
Intensity
Low
Median
High
Interstate war
\(\lambda\) = 0.5
1.4
6.2
Civil war
\(\lambda\) = 1.0
3.1
13
Translated to duration-agnostic probabilities of peace for interpretation:
Intensity
Low
Median
High
Interstate war
55 %
29 %
9 %
Civil war
36 %
16 %
4 %
The duration-dependent probabilities for interstate wars would then be
Intensity
Low
Median
High
1 year
64 %
42 %
20 %
2 years
51 %
32 %
14 %
3 years
45 %
27 %
12 %
4 years
41 %
25 %
11 %
5 years
38 %
23 %
10 %
5–10 years
34 %
20 %
9 %
10–20 years
28 %
16 %
7 %
20–40 years
22 %
12 %
5 %
>40 years
17 %
10 %
4 %
For civil wars they are
Intensity
Low
Median
High
1 year
49 %
28 %
13 %
2 years
37 %
21 %
9 %
3 years
32 %
18 %
8 %
4 years
29 %
16 %
7 %
5 years
27 %
15 %
7 %
5–10 years
24 %
13 %
6 %
10–20 years
19 %
10 %
4 %
20–40 years
15 %
8 %
3 %
>40 years
12 %
6 %
2 %
Converted to a forecast, we get.
Question
By contention
By intensity
Ukraine
21 %
11 %
Sudan
12 %
8 %
These probabilities still need to be adjusted because the resolution criteria
for the forecasting competition are looser than in the
ucdp
data, so I would
add maybe one log-odds to both probabilities, and end up with a final forecast
of
Question
By contention
Forecast
Change
Ukraine
21 %
25 %
+0.23 log-odds
Sudan
12 %
19 %
+0.54 log-odds
That feels reasonable. It is lower than my naïve forecasts of 38 % and 43 %
respectively, but that also reflects my main takeaway from this analysis:
conflicts last much longer than I think. Since so many of them resolve so
quickly, it is easy to accidentally think that those that are currently ongoing
will resolve soon, too. But by looking at those that are ongoing now, we are
filtering for those that are long-running, thanks to the heavy tails of the
distribution of their duration.
