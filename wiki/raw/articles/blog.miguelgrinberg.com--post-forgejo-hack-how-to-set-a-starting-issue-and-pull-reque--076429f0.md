---
title: "Forgejo hack: How to set a starting issue and pull request number"
url: "https://blog.miguelgrinberg.com/post/forgejo-hack-how-to-set-a-starting-issue-and-pull-request-number"
fetched_at: 2026-08-26T10:01:01.039174+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# Forgejo hack: How to set a starting issue and pull request number

Source: https://blog.miguelgrinberg.com/post/forgejo-hack-how-to-set-a-starting-issue-and-pull-request-number

I'm currently working on migrating my open source projects from GitHub to a self-hosted
Forgejo
instance. As part of this effort I often end up looking through the Forgejo source code to figure out if there are hidden ways to configure certain things to my liking when I can't do it on the administration UI. I thought I'd start putting my discoveries in writing here, in case they can help others. So here goes the first one.
One of the aspects of the migration that is tricky is how to transition issues and pull requests. What makes the most sense to me is to only use Forgejo to track issues and pull requests going forward, leaving all the issues and pull requests created up to the migration point on GitHub. Of course whether this is a good or bad idea is debatable, but considering all the options I have decided that this is the solution that is going to inflict the least pain on me.
The one problem with this approach is that I would end up having duplicate issue numbers, because Forgejo would start creating issues and pull requests all the way back from
#1
, and all those low numbers have been used on the GitHub side. So I wanted to hack my Forgejo instance so that issues start from, say, 10000. That way when anyone references an issue by its number I would know that numbers below 10000 are on GitHub and only those above are on my own instance.
I could not find a way to set a starting issue number through configuration, but this turns out to be easy to do by modifying the database directly. To set the base issue number for all the repositories at the same time, you can use the following SQL statement:
update issue_index set max_index=10000;
With this, the next issue or pull request that is created on each repository will have number
#10001
, and it will go up from there.
If you want to do this for just one repository, then it gets a bit more complicated, because you need to know the database
id
of the repository in question. In that case, first list the repositories and their
id
values:
select id, name from repository;
Once you have the
id
associated with the repository, you can set its next issue number. If, for example, your repository has
id=123
, then you can do this:
update issue_index set max_index=10000 where group_id=123;
It goes without saying that you will want to put a number that is higher than any issues or pull requests that exist in the repository, because if not you may end up having duplicate numbers and that could lead to problems.
I should also note that the above SQL statements are verified to work on a Postgres Forgejo database. I would expect the same statements to work for MySQL or sqlite databases, but I have not tested that myself. I'm using Forgejo version 15, so keep in mind that this trick may not work on other versions.
Happy Forgejo hacking!
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
