---
title: "Regatta Starting Stations - Chi-squared Continued"
url: "https://entropicthoughts.com/regatta-starting-stations"
fetched_at: 2026-05-12T07:00:49.806188+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Regatta Starting Stations - Chi-squared Continued

Source: https://entropicthoughts.com/regatta-starting-stations

We have seen that men win more often from the Berkshire station than women. What we
want to know is what the source of this variation is:
does it come from a true difference between the sexes, or
does it arise from sampling error?
The chi-squared test can help us rule out sampling error as a cause.
If the source of variation is purely sampling error, that would mean the real
Berkshire win rate for both men and women is actually the population average of
53.5 %. Under that assumption, we can compare the hypothesised counts to the
actual counts.
We compute the hypothesised counts by multiplying the total number of races for
each sex with 53.5 % to get their wins, and then the losses fall out of that
too. The hypothesis suggests that men, who competed in 3441+2969=6410 races,
should have won 0.535×6410=3429 races, and lost the other 2981. We put the
hypothesised counts into brackets in the table.
Men
Women
Wins
3441 [3429]
603 [613]
Losses
2969 [2981]
542 [532]
Note that once we determined the first expected count, the rest were given to us
for free. This is because we don’t want to change the totals across rows and
columns. Once we have determined the hypothesised count of 3429 wins for the
men, we could not have picked any other number of wins for women or losses for
men without changing proportions we want to stay fixed. This fact is going to
become important shortly!
To figure out whether this difference between observed and hypothesised is
significant, we compute the squared difference between observed and
hypothesised, divided by the hypothesised. We get
Men
Women
Wins
\(\frac{(3441-3429)^2}{3429} = 0.042\)
\(\frac{(603-613)^2}{613} = 0.16\)
Losses
\(\frac{(2969-2981)^2}{2981} = 0.048\)
\(\frac{(542-532)^2}{532} = 0.19\)
When we add these together, we get the \(\chi^2\) statistic from which the
test derives its name. In this case, we have
\[\chi^2 = 0.042 + 0.048 + 0.16 + 0.19 = 0.44\]
Just as
when we encountered the chi-squared test earlier
, this number is –
assuming variation is attributable to sampling error only – going to follow a
chi-squared distribution. On the contrary, if our statistic lies meaningfully
outside of what normally happens when drawing from a chi-squared distribution,
we are right to suspect that there is something beyond sampling error going on;
in this case, that there is some actual difference between the sexes in terms of
Berkshire win rate.
Because all hypothesised values fell out of the first we calculated (thanks to
the sums being fixed), we should be looking at the chi-squared distribution with
one degree of freedom. If we plot that or look up 0.44 in a table, we will see
that it falls smack in the middle of the chi-squared distribution. This means we
have no reason to suspect the variation in the Berkshire win rate between sexes
have any cause other than sampling error.
We already knew this from the poor man’s logistic regression above
2
Different
ways of performing the same hypothesis test will never yield different results.
If one test does not show significance, then the other also will not. Two tests
can show different results only if they are somehow different tests, i.e. one
test makes assumptions the other does not.
, but we went through the motions
here anyway to introduce the \(\chi^2\) test with a 2×2 table before we extend it
to a 3×2 table.
