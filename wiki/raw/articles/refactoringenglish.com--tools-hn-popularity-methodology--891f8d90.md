---
title: "HN Popularity Contest"
url: "https://refactoringenglish.com/tools/hn-popularity/methodology/"
fetched_at: 2026-04-29T07:01:22.825600+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# HN Popularity Contest

Source: https://refactoringenglish.com/tools/hn-popularity/methodology/

HN Popularity Contest
Methodology
What counts as a personal blog?
I count a site as a personal blog if:
the site contains written content (not just an app or a video)
the site is authored by a single person
A blog still counts as a personal blog even if the blogger is a professional journalist (e.g.,
Brian Krebs
) or blogging on their company’s website (e.g.,
Raymond Chen
).
Social media (Twitter / Mastodon) doesn’t count as a personal blog.
Podcasts websites count as blogs if they’re hosted by a single person and are independently owned.
I exclude github.com links even though some people post blogs there.
It’s too hard to filter out all the non-blog links to github.com.
Pages under the
github.io
domain are eligible.
Aggregating scores
I aggregate scores across all submissions that received a score of at least 20 and are not dead or deleted.
e.g., If a single link was submitted 100 times and never scored at least 20, none of those submissions would increase the aggregate score for the domain.
Duplicate submissions of the same URL all count as long as each submission received at least 20 points.
I aggregate together domains when the author moved domains as long as the new domain is the canonical URL for the old content.
e.g., all submissions from
christine.website
count towards
xeiaso.net
, their new canonical URL.
I do not aggregate together blogs by the same author at different domains if they contain distinct content.
e.g.,
kalzumeus.com
and
bitsaboutmoney.com
count separately, even though Patrick McKenzie is the author of both.
To reduce the size of the dataset, I only include domains that have accumulated at least 500 points across all submissions.
Update frequency
The data automatically updates on the second day of each month, but I sometimes do out of band updates.
Generating bios and topics
I created the bios and topic lists with a combination of LLM generation and manual fixes.
Generally, older and more popular authors have more accurate bios.
I manually inspected the top 100 in the most popular views, but I probably missed some mistakes. I accept corrections on
the Github repo
.
