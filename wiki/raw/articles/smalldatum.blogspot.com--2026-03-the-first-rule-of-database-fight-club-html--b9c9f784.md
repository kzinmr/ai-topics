---
title: "The first rule of database fight club: admit nothing"
url: "https://smalldatum.blogspot.com/2026/03/the-first-rule-of-database-fight-club.html"
fetched_at: 2026-05-05T07:01:17.229619+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# The first rule of database fight club: admit nothing

Source: https://smalldatum.blogspot.com/2026/03/the-first-rule-of-database-fight-club.html

I am fascinated by tech marketing but would be lousy at it.
A common practice is to admit nothing -- my product, project, company, idea is perfect. And I get it because admitting something isn't perfect just provides fodder for marketing done by the other side, and that marketing is often done in bad faith.
But it is harder to fix things when you don't acknowledge the problems. I wrote about this in 2019, this post builds on the
previous post
.
In the MySQL community we did a good job of acknowledging problems -- sometimes too good. For a long time as an external contributor I filed many bug reports, fixed some bugs myself and then spent much time marketing open bugs that I hoped would be fixed by upstream. Upstream wasn't always happy about my marketing, sometimes there was much snark, but snark was required because there was a large wall between upstream and the community. I amplified the message to be heard.
My take is that the MySQL community was more willing than the Postgres community to acknowledge problems. I have theories about that and I think several help to explain this:
Not all criticism is valid
While I spend much time with Postgres on benchmarks I don't use it in production. I try to be fair and limit my feedback to things where I have sweat equity my perspective is skewed.  This doesn't mean my feedback is wrong but my context is different. And sometimes my feedback is wrong.
Bad faith
Some criticism is done in bad faith. By bad faith I means that truth takes a back seat to scoring points. A frequent source of Postgres criticism is done to promote another DBMS. Recently I have seen much anti-Postgres marketing from MongoDB. I assume they encounter Postgres as competition more than they used to.
Good faith gone bad
Sometimes criticism given in good faith will be repackaged by others and used in bad faith. This happens with some of the content from my blog posts. I try to make this less likely by burying the lead in the details but it still happens.
MySQL was more popular than Postgres until recently.
Perhaps people didn't like that MySQL was getting most of the attention and admitting flaws might not help with adoption. But today the attention has shifted to Postgres so this justification should end. I still remember my amusement at a Postgres conference long ago when the speaker claimed that MySQL doesn't do web-scale. Also amusing was being told that Postgres didn't need per-page checksums because you should just use ZFS to get similar protection.
Single-vendor vs community
MySQL is a single-vendor project currently owned by Oracle. At times that enables an us vs them mentality (community vs coporation). The coporation develops the product and it is often difficult for the community to contribute. So it was easy to complain about problems, because the corporation was responsible for fixing them.
Postgres is developed by the community. There is no us vs them here and the community is more reluctant to criticize the product (Postgres). This is human nature and I see variants of it at work -- my work colleagues are far more willing to be critical of open-source projects we used at work than they were to be critical of the many internally developed projects.
