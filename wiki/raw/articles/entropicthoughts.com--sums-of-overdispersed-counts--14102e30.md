---
title: "Runs scored in World Baseball Classic"
url: "https://entropicthoughts.com/sums-of-overdispersed-counts"
fetched_at: 2026-11-04T10:01:00.914634+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Runs scored in World Baseball Classic

Source: https://entropicthoughts.com/sums-of-overdispersed-counts

We modeled the count for one team in one game as \(\mathrm{NB}(\mu=4.3, r=3.4)\).
We want the total number for all seven games in the knockout stages; that’s 14
draws from the distribution above.
Now, the negative binomial distribution has a convenient identity:
\[x_i \sim \mathrm{NB}(r, p) \Longrightarrow \sum_i^n x_i \sim \mathrm{NB}(nr, p)\]
This says that
if
we have parametrised the negative binomial distribution with
\((r, p)\) and we want the distribution of the sum of 14 such random values, we
can use the negative binomial distribution with parameters \((14r, p)\).
We don’t have \((r, p)\), though, we have \((\mu, r)\). We could convert that to
\((r, p)\) and then convert back, but there’s a more fun way: we can prove a
corresponding version of the identity for our parametrisation on our own! We
want to find \(\mu'\) and \(r'\) such that
\[x_i \sim \mathrm{NB}(\mu, r) \Longrightarrow \sum_i^n x_i \sim \mathrm{NB}(\mu', r')\]
We start with the parameter transformation
\[p(\mu, r) = \frac{r}{r + \mu}\]
which lets us rephrase the first identity to
\[x_i \sim \mathrm{NB}(r, p(\mu, r)) \Longrightarrow \sum_i^n x_i \sim \mathrm{NB}(nr, p(\mu', nr))\]
For this to be true still, we need to find the value of \(\mu'\) that makes
\(p(\mu', nr) = p(\mu, r)\). That means we need to make it so that
\[\frac{r}{r + \mu} = \frac{nr}{nr + \mu'}\]
This happens when \(\mu' = n\mu\) because then we get
\[\frac{nr}{nr + \mu'} = \frac{nr}{nr + n\mu} = \frac{nr}{n(r + \mu)} = \frac{r}{r + \mu}\]
Thus, the identity we are looking for is simply
\[x_i \sim \mathrm{NB}(\mu, r) \Longrightarrow \sum_i^n x_i \sim \mathrm{NB}(n\mu, nr)\]
How convenient.
8
The convenience makes it even more strange that I couldn’t
find anyone stating this version of the identity. I must have overlooked
something.
This means the number of runs scored in the knockout stages of the 2026
wbc
is
probably distributed as \(\mathrm{NB}(\mu=14 \times 4.3, r=14 \times 3.4)\). That
gives us a forecast of 42–80 at 90 % confidence.
The new interval of 42–80 based on more detailed modeling is better (narrower)
than the baseline we had at 35–87. That’s what we hoped for. Now that we
approached it as the sum of 14 independent-but-lumpy counts, we both used more
data to estimate the variation, and we average out some of the noise when we sum
it all together.
Go forth and use the negative binomial distribution when appropriate!
