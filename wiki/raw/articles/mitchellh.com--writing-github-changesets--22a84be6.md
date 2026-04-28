---
title: "Reorient GitHub Pull Requests Around Changesets"
url: "https://mitchellh.com/writing/github-changesets"
fetched_at: 2026-04-28T07:02:40.843738+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Reorient GitHub Pull Requests Around Changesets

Source: https://mitchellh.com/writing/github-changesets

I've had the experience of
using GitHub as a maintainer for very large open source projects (1000+
contributors), as an engineer for very large closed source corporate projects,
and everything smaller. Through those experiences up to today, GitHub pull
requests is where I spend almost all of my time while on GitHub, and to me its
also unfortunately the most frustrating part of GitHub.
There are a lot of improvements I would love to see with pull requests,
but a massive chunk of my problems would be solved through
one major feature:
changesets
. This blog post describes this suggestion
and what I would love to see.
Disclaimer:
My ideas here are not original! I do not claim to have
come up with these ideas. My suggestions here are based on well-explored
Git workflows and also are partially or in full implemented by other
products such as Gerrit, Phabricator, or plain ol' email-based patch
review.
The Problem Today
The lifecycle of a GitHub pull request today is effectively one giant
mutable changeset. This is a mess!
Here is a typical PR today:
A contributor pushes a set of commits to a branch, opens a PR, and the PR now
represents that branch. People discuss the PR through comments. When the contributor
pushes new changes, they show up directly on the same PR, updating it immediately.
Reviewers can leave comments and the contributor can push changes at the same
time, and it all updates the same PR.
This has many problems:
A reviewer can leave a review for a previous state the PR was in and
it can become immediately outdated because while the review was happening
the contributor pushed changes.
Worse, a review can become
partially
outdated and the
other feedback may not make sense in the context of the changes a
contributor pushed. For example, a line comment may say "same feedback
as the previous comment" but the
previous comment is now gone/hidden
because
the contributor pushed a change that moved those lines.
1
Reviews don't contain any metadata about the commit they were attached to,
only a timestamp they were submitted. A user can roughly correlate timestamp
to commit but it isn't totally accurate because if a commit comes in during
a review, the timestamp will seem to imply it was after the most recent
commit but your review may have been against the prior commit. 😕
Work-in-progress commits towards addressing review feedback become visible
as soon as the branch is pushed. This forces contributors to address all
feedback in a single commit, or for reviewers to deal with partially-addressed
feedback.
You can't easily scrub to prior states of the PR. If you want to review
a set of earlier commits while ignoring later commits, you either have
to manually build a "compare" view or use a local checkout (I do the
latter). But through either approach you only get the code changes,
you don't also get the point-in-time reviewer feedback!
Similar to the above, if a contributor pushes multiple new commits, you
can't easily compare
the new set of commits
to the old. You can only
really scrub one commit at a time. For this, you again have to fallback
to local
git
to build up a diff manually.
And more... I talk about some more later, but I think I've made my point.
I'm sure I'm wrong about some detail about some of the points above.
Someone is likely to say "he could've just done
this
to solve problem
5(a)". That's helpful! But, the point I'm trying to make is that if you
step back the fundamentals
causing
these problems are the real issue.
Namely, a single mutable changeset tracking a branch on a per-commit basis.
Changesets
The solution is changesets:
A pull request is
versionable
through a monotonic number (v1, v2, ...).  These versions are often called "changesets."
Each changeset points to the state of a branch
at a fixed time
. These
versions are
immutable
: when new commits are pushed, they become part
of a new changeset. If the contributor force pushes the branch, that also
becomes part of a new changeset. The previous changeset is saved forever.
A new changeset can be published immediately (per commit) or it can be deferred
until the contributor decides to propose a new version for review. The latter
allows a contributor to make multiple commits to address prior feedback and
only publish those changes when they feel ready.
In the world of changesets, feedback is attached to a changeset. If a reviewer
begins reviewing a changeset and a new changeset is published, that's okay
because the review as an atomic unit is attached to the prior changeset.
In future changesets, it is often useful to denote that a file or line has
unresolved comments in prior changesets. This ensures that feedback on
earlier changesets is not lost and must be addressed before any changeset
is accepted.
Typically, each changeset is represented by a different Git ref. For example,
GitHub pull requests today are usually
refs/pr/1234
and you can use
git
locally to check out any pull request this way. A changeset would be something
like
refs/pr/1234/v2
(hypothetical) so you can also check out individual
changesets.
Instead of "approving" a PR and merging, reviewers approve a
changeset
. This
means that the contributor can also post multiple changesets with differing
approaches to a problem
in a single PR
and the maintainer can potentially
choose a non-latest changeset as the set of changes they want to merge.
GitHub, Please!
Changesets are a well-established pattern across many open source projects
and companies. They're already a well-explored user experience problem
in existing products like Gerrit and Phabricator. I also believe changesets
can be introduced in a non-breaking way (since current PRs are like
single-mutable-changeset mode).
Changesets would make pull requests so much more scalable for larger
projects and organizations. Besides the scalability, they make the review
process cleaner and safer for both parties involved in pull requests.
Of course, I can only speak for myself and my experience, but this single
major feature would dramatically improve my quality of life and capabilities
while using GitHub
2
.
