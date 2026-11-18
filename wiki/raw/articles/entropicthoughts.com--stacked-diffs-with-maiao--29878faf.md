---
title: "Stacked diffs with Maiao"
url: "https://entropicthoughts.com/stacked-diffs-with-maiao"
fetched_at: 2026-11-18T10:01:22.964987+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Stacked diffs with Maiao

Source: https://entropicthoughts.com/stacked-diffs-with-maiao

On traditional forge platforms
1
Like GitHub, Codeberg, GitLab, BitBucket,
etc.
, pre-commit
2
Pre-commit because it’s the review that happens before the
code is merged (“committed”) to the upstream branch, in contrast to e.g. audits
which are a kind of post-commit review.
code review happens on
pull requests
(sometimes called
merge requests
), where each pull request is created from a
git branch.
Users that are new to git can then think of a branch as one development effort
toward a small goal. They keep adding commits to that branch as long as its tip
does not represent the goal state. At the end, when everything looks right and
the change is approved, they perform an explicit merge. This means they create a
merge commit on the upstream branch that references both the old upstream and
the branch they worked on.
This lets beginners work in smaller increments while not dealing with the
intricacies of rewriting git history
3
Sometimes the beginner is instructed to
perform a squash merge instead, which typically means the forge platform creates
a single, regular commit on the upstream branch, referencing only the old
upstream, and containing all the changes implied by the tip of the development
branch. Although it sounds like this rewrites history, it doesn’t really – the
old development branch is still exactly the same as it was before. The
difference is that the changes implied by it were copied over to the upstream
branch without reference to the development branch.
; the workflow lowers the
barrier to collaborating with others using git, which is nice.
It also means
the reviewing interface
in a traditional forge doesn’t have to
deal with the intricacies of rewriting git history. This means the reviewing
ui
typically only shows the differences between commits still on the
development branch, and not what changed between two versions of “the same”
commit, when one of them is no longer on the branch.
To be more concrete, here’s an example of a part of the history graph of a
project that uses this workflow.
4
The commits are not shown in chronological
order. I reordered them (where it was possible to do so without changing the
structure of the graph) to make the graph read more clearly.
▲ (upstream)
│
│   ▲ (input-validation)
│   │
│   │   ▲ (priv-cache)
│   │   │
│   ●   │       Tighten input validation
│   │   │
│   │   ●       Rename cache variables
│   │   │
│   │   ●       Cache user permissions
├───╯   │
●◀──╮   │   Merge flaky-test-fix (PR #835)
│   ├───╯
│   ●           Fix timezone offset instead
│   │
│   ●           Disable login test
│   │
●◀──┼───╮   Merge log-migration (PR #834)
├───╯   │
●◀──╮   │   Merge avatar-upload (PR #833)
│   │   │
│   ●   │       Fix typo in readme
│   │   │
│   ●   │       Clean up unused imports
│   │   │
│   ●   │       Add avatar upload
├───╯   │
●◀──╮   │   Merge parser-null-check (PR #832)
│   │   │
We can see a total of 12 commits. Four of them are merge commits on the
upstream branch, and two of those merge commits correspond to branches we can
see the work on (
avatar-upload
and
flaky-test-fix
). We can see each of those
two branches had three and two commits of actual work on them, respectively.
Then there are two more branches (
input-validation
and
priv-cache
) which are
still open (not merged with upstream). One of them (
priv-cache
) has two
commits of work, and it’s not based on the upstream branch, but on the final
result of one of the earlier branches (
flaky-test-fix
), before it got merged.
