---
title: "Do-it-yourself meta-analysis"
url: "https://entropicthoughts.com/diy-meta-analysis"
fetched_at: 2026-11-25T10:00:49.352799+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Do-it-yourself meta-analysis

Source: https://entropicthoughts.com/diy-meta-analysis

We
can
perform an even more powerful type of meta-analysis. First we need the
standard errors of each study. If we only have the p-values (and effect sizes),
we can convert them to standard errors, but the process relies on quite
significant assumptions. In our case, we extracted the standard errors from
confidence intervals, which is slightly better but still not ideal. Either way,
we have standard errors.
The idea is that we’ll compute a weighted average of the effect sizes, with the
weights coming from the
precision
of each study. The precision is the inverse
variance, i.e. one divided by the square of the standard error.
Trial
Mort.
se
weight
Trivedi
0.90
0.077
170
whi
0.92
0.046
470
Lyons
0.99
0.031
1100
record
0.93
0.043
530
This assigns the highest weight to the Lyons study, because that one seems to
have pinned down the effect most precisely.
4
There’s a mathematical argument
for why the weight should be the inverse variance, but I seem to have lost my
notes on the way here.
When we perform the weighted average of the observed effects using these
weights, we arrive at a combined odds ratio of 0.95. Since this is a linear
combination of uncertain values, and we know their variation, we can
compute the
variation of the weighted average
. We find out the aggregate standard error is
0.021.
That means the z-score of the aggregate effect is −2.17, which, under a
two-tailed test, corresponds to a p-value of 3 %.
5
If you don’t have a z
table around,
you can use the bottom row of the t table instead
.
Look at that!
When we use a powerful enough test, the combined impression of these four
studies
is
significant. If we believe Dynomight didn’t cherry-pick these four
studies, that would be a meaningful discovery.
Now that we have the standard error of the aggregate, we can also compute a
confidence interval for the aggregate.
6
Again, shouldn’t these intervals be
asymmetric due to the multiplicative nature of odds ratios? They should, but
apparently the data source for these intervals ignored that, so I will too.
Trial
All-cause mortality
95 % CI
p-value
Trivedi
0.90
0.77 to 1.07
0.21
whi
0.92
0.83 to 1.01
0.10
Lyons
0.99
0.93 to 1.05
0.75
record
0.93
0.85 to 1.02
0.12
Aggregate
0.96
0.83 to 0.99
0.04
If this table does not excite you, then surely this fancy text-based diagram
will.
Odds ratio:         0.8       0.9       1.0       1.1
- - - - - - - - - - - - - - - - - - - - - │ - - - - - - - - -
 Trivedi           ─────────────●─────────┼───────  (p=0.21)
 WHI                     ─────────●───────┼─        (p=0.10)
 Lyons                             ──────●┼─────    (p=0.75)
 RECORD                    ────────●──────┼──       (p=0.12)
- - - - - - - - - - - - - - - - - - - - - │ - - - - - - - - -
 Aggregate                       ────●────┤         (p=0.04)
I find this whole thing incredible. We can tell the aggregate is a sort of
average weighted toward the more precise results, but the information contained
in all of these four studies is still enough to draw the conclusion that (a)
yes, there is an effect, and (b) it is in the direction of benefit.
Disclaimer: a proper meta-analysis requires that we do things we have not
done in this article. We need to vet the studies we go through for
methodological problems, biases, differences in definitions, etc. The
statistical work of combining statistical significance is only a small part in
performing a real meta-analysis. We shouldn’t base our life decisions on what we
found in this article.
