---
title: "pre-commit hooks are fundamentally broken"
url: "https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/"
fetched_at: 2026-04-28T07:02:50.193578+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# pre-commit hooks are fundamentally broken

Source: https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/

Let's start a new Rust project.
$
mkdir
best-fizzbuzz-ever
$
cd
best-fizzbuzz-ever
$
cat
<<
EOF
>
main.rs
fn main() { for i in 0.. {
println ("fizzbuzz");
}}
EOF
$
git
init
Initialized empty Git repository in /home/jyn/src/third-website/best-fizzbuzz-ever/.git/
$
git
add main.rs
$
git
commit
--
message
fizzbuzz
[main (root-commit) 661dc28] fizzbuzz
1 file changed, 4 insertions(+)
create mode 100644 main.rs
Neat. Now let's say I add this to some list of fizzbuzz projects in different languages.
Maybe ....
this one
.
They tell me I need to have "proper formatting" and "use consistent style".
How rude.
Maybe I can write a pre-commit hook that checks that for me?
$
cat
<<
'
EOF
'
>
pre-commit
#!/bin/sh
set -eu
for f in *.rs; do
rustfmt --check "$f"
done
EOF
$
chmod
+x pre-commit
$
ln
-
s
../../pre-commit .git/hooks/pre-commit
$
git
add pre-commit
$
git
commit
--
message
"
add pre-commit hook
"
Diff in /home/jyn/src/third-website/best-fizzbuzz-ever/src/main.rs:1:
-fn main() { for i in 0.. {
-    println ("fizzbuzz");
-}}
+fn main() {
+    for i in 0.. {
+        println("fizzbuzz");
+    }
+}
Neat! Let's commit that change.
$
rustfmt
main.rs
$
git
commit
--
message
"
add pre-commit hook
"
[main 3be7b87] add pre-commit hook
1 file changed, 4 insertions(+)
create mode 100755 pre-commit
$
git
status
On branch main
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   main.rs
Oh ... We fixed the formatting, but we didn't actually stage the changes.
The pre-commit hook runs on the
working tree
, not on the
index
, so it didn't catch the issue.
We can see that the version tracked by git still has the wrong formatting:
$
git
show HEAD:main.rs
fn main() { for i in 0.. {
println ("fizzbuzz");
}}
Maybe we can make the script smarter?
Let's checkout all the files in the index into a temporary directory and run our pre-commit hook there.
$
cat
<<
'
EOF
'
>
pre-commit
#!/bin/sh
set -eu
tmpdir=$(mktemp -d --tmpdir "$(basename "$(realpath .)")-pre-commit.XXXX")
trap 'rm -r "$tmpdir"' EXIT
git checkout-index --all --prefix="$tmpdir/"
for f in $tmpdir/*.rs; do
rustfmt --check "$f"
done
EOF
$
git
add pre-commit
$
git
commit
--
message
"
make pre-commit hook smarter
"
Diff in /tmp/best-fizzbuzz-ever-pre-commit.ZNyw/main.rs:1:
-fn main() { for i in 0.. {
-    println ("fizzbuzz");
-}}
+fn main() {
+    for i in 0.. {
+        println("fizzbuzz");
+    }
+}
Yay! That caught the issue.
Now let's add our rust program to that collection of fizzbuzz programs.
$
git
add main.rs
$
git
commit
--
message
"
make pre-commit hook smarter
"
[main 3cb40f6] make pre-commit hook smarter
2 files changed, 11 insertions(+), 4 deletions(-)
$
git
remote add upstream https://github.com/joshkunz/fizzbuzz
$
git
fetch upstream
remote: Enumerating objects: 222, done.
remote: Total 222 (delta 0), reused 0 (delta 0), pack-reused 222 (from 1)
Receiving objects: 100% (222/222), 29.08 KiB | 29.08 MiB/s, done.
Resolving deltas: 100% (117/117), done.
From https://github.com/joshkunz/fizzbuzz
* [new branch]      master     -> upstream/master
$
git
rebase upstream
Successfully rebased and updated refs/heads/main.
Maybe we'll make one last tweak...
$
sed
-
i
'
1i // Written by jyn
'
main.rs
$
git
commit main.rs
--
message
"
mark who wrote fizzbuzz
"
Diff in /tmp/best-fizzbuzz-ever-pre-commit.n1Pj/fizzbuzz-traits.rs:4:
use std::iter;
struct FizzBuzz {
-    from : i32
-  , to : i32
+    from: i32,
+    to: i32,
}
impl FizzBuzz {
Uh. Huh. Right.
The code that was already here wasn't formatted according to rustfmt.
Our script is running on every file in the git repo, so it won't let us commit.
Maybe we can change it to only run on modified files?
$
cat
<<
'
EOF
'
>
pre-commit
#!/bin/sh
set -eu
files=$(git diff --name-only --cached --no-ext-diff --diff-filter=d)
tmpdir=$(mktemp -d --tmpdir "$(basename "$(realpath .)")-pre-commit.XXXX")
trap 'rm -r "$tmpdir"' EXIT
printf %s "$files" | tr '\n' '\0' | xargs -0 git checkout-index --prefix="$tmpdir/"
for f in $tmpdir/*.rs; do
rustfmt --check "$f"
done
EOF
$
git
commit main.rs pre-commit
\
--
message
"
update main.rs; make pre-commit even smarter
"
[main f2925bc] update main.rs; make pre-commit even smarter
2 files changed, 5 insertions(+), 1 deletion(-)
Alright. Cool.
Let's do one last thing.
Let's say we had an existing PR to this repo and we need to rebase it.
Maybe it had a merge conflict, or maybe there was a fix on main that we need in order to implement our solution.
$
git
checkout upstream/HEAD
HEAD is now at 56bf3ab Adds E to the README
$
echo
'
fn main() { println!("this counts as fizzbuzz, right?"); }
'
>
print.rs
$
git
add print.rs
$
git
commit
--
message
"
Add print.rs
"
[detached HEAD 3d1bbf7] Add print.rs
1 file changed, 1 insertion(+)
create mode 100644 print.rs
And let's also say that we want to edit the commit message.
$
git
rebase
-
i
main
reword 3d1bbf7 Add print.rs
#
Rebase
f2925bc..3d1bbf7 onto f2925bc (1 command
)
Now, we
really
have a problem.
Error: file `/tmp/best-fizzbuzz-ever-pre-commit.p3az/*.rs` does not exist
Could not apply 3d1bbf7... Add print.rs
Two things went wrong here:
Our pre-commit hook can't handle commits that don't have any Rust files.
Our pre-commit hook
ran on a branch we were rebasing
.
Fixing the first thing doesn't really help us, because we don't control other people's branches.
They might have used
git commit --no-verify
.
They might not even have a pre-commit hook installed.
They might have had a branch that passed the hook when they originally wrote it, but not after a rebase (e.g. if your hook is
cargo check
or something like that).
They might have had a branch that used an old version of the hook that didn't have as many checks as a later version.
Our only real choice here is to pass
--no-verify
to
git rebase
every time we run it, and to
git commit
for every commit in the rebase we modify,
and possibly even to every
git merge
we run outside of a rebase.
This is because pre-commit hooks are a
fundamentally broken idea
.
Code does not exist in isolation.
Commits that are local to a developer machine do not ever go through CI.
Commits don't even necessarily mean that that the code is ready to publish—pre-commit hooks don't run on
git stash
for a reason!
I don't use
git stash
, I use
git commit
so that my stashes are tied to a branch, and hooks completely break this workflow.
More than that, pre-commit hooks are
preventing you from saving your work
.
There should be a
really, really good reason
to prevent you from saving your work, and IMO "doesn't pass the test suite" is not that.
I have similar feelings about format-on-save hooks.
There are a
bunch
of
other
footguns
with pre-commit hooks.
This doesn't even count the fact that nearly all pre-commit hooks are implemented in a broken way and just blindly run on the worktree, and are slow or unreliable or both.
Don't get me started on pre-commit hooks that try to add things to the commit you're about to make, or projects that try to automatically install a hook when you run the test suite.
The
pre-commit
framework (or its cousin,
lint-staged
) does
not
fix this.
It fixes the issues about running on the index by stashing your changes with
--keep-index
,
which works but modifies your git state.
It doesn't fix the issues about running during a rebase, nor does it prevent hooks from trying to add things to the current commit.
"Just don't write bad hooks" doesn't work if I'm working on someone else's project where I don't control the hook.
Please just don't use
pre-commit
hooks. Use
pre-push
instead.
pre-push
hooks nearly avoid all of these issues.
The only use case where I think pre-commit hooks are a good idea is for things that must
never
committed, that are worth interrupting a complicated rebase to prevent; namely: credentials.
Once credentials are committed they're quite difficult to get out, and even harder to be sure you haven't missed them.
Tips for writing a
pre-push
hook
Run on the index, not the working tree, as described above.
Only add checks that are fast and reliable. Checks that touch the network should never go in a hook. Checks that are slow and require an up-to-date build cache should never go in a hook. Checks that require credentials or a running local service should never go in a hook.
Be as quiet as possible. This hook is running buried inside a bunch of other commands, often without the developer knowing that the hook is going to run. Don't hide other important output behind a wall of progress messages.
Don't set the hook up automatically. Whatever tool you use that promises to make this reliable is wrong. There is not a way to do this reliably, and the number of times it's broken on me is more than I can count. Please just add docs for how to set it up manually, prominently featured in your CONTRIBUTING docs. (You do have contributing docs, right?)
If the hook does fail, and the changes affect an older commit than the most recent,
you can use a combination of
git-absorb
,
git-revise
,
and
git rebase -X ours --exec
to put them in the appropriate commit before pushing again.
And don't write
pre-commit
hooks!
