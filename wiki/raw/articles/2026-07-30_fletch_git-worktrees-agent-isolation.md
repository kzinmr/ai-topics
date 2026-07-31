---
title: "Git worktrees are not an isolation boundary for coding agents"
date: "2026-07-30"
source_url: "https://fletch.sh/blog/git-worktrees-vs-clones-for-ai-agents/"
author: "Alex Chaplinsky"
tags: ["coding-agents", "sandbox", "security", "git", "worktrees", "isolation"]
type: article
---
Give a coding agent its own git worktree, which is how most tools for running agents in parallel do it, and that agent can install a hook that runs on your machine the next time you commit in your real repository. It can rewrite the email your own commits are attributed to. It can pop another agent’s stash into its own tree.

None of that needs a bug or an exotic command. A worktree was never a boundary. It is a second working directory attached to one .git, and everything interesting lives in that .git.

Worktrees became the default here because they are the obvious answer. One command, no duplicated history, a second checkout in about a second. The pitch is isolation at nearly zero cost, and both halves of that turn out to be wrong: the isolation is much thinner than the phrase “isolated worktree” suggests, and the cost of doing it properly is the same. I had the cost part wrong in an earlier version of this post, until I measured it.

## What a linked worktree actually shares

Inside a linked worktree, .git is not a directory. It is a file:

```bash
$ cat ../my-worktree/.git
gitdir: /path/to/repo/.git/worktrees/my-worktree
```

Everything follows from that path. Git splits repository state into per-worktree state and common state, and it will tell you which is which:

```bash
$ cd ../my-worktree
$ git rev-parse --git-dir          # per-worktree
/path/to/repo/.git/worktrees/my-worktree
$ git rev-parse --git-common-dir   # shared with the parent and every sibling
/path/to/repo/.git
```

Per-worktree state is a short list: HEAD, the index, ORIG_HEAD, and a few bisect and rebase files. Everything else resolves through --git-common-dir back into the original repository:

- The object store (.git/objects), which is the point, and is safe to share.
- Refs and branches (refs/heads, packed-refs). One namespace for every worktree.
- The config (.git/config).
- The stash (refs/stash).
- Hooks (.git/hooks), which is where a shared directory becomes arbitrary code execution.

So the isolation is real, and it is narrow: your working directory, HEAD, and the index. Those are useful. They are not a boundary. A boundary would mean a process confined to the worktree cannot reach state outside it, and the second list is a catalogue of the ways it can. “Isolated worktree” gets used constantly, in tool descriptions and in advice threads, without ever saying which of the two lists is meant.

## What that lets an agent do

Worst first. Each block creates its own repository, so you can paste them into one empty directory and run them in any order. Every line of output below is real, captured on git 2.50.1.

### Execute code on your host

.git/hooks lives in the common directory. A hook installed from inside a worktree is therefore installed for the parent repository, and it runs as you, in the parent, the next time you run the triggering command.

```bash
git init -q --initial-branch=main hook-demo
cd hook-demo
git commit -q --allow-empty -m init
git branch agent-work
git worktree add -q ../hook-agent agent-work

# The "isolated" worktree writes a hook into the parent's .git
cd ../hook-agent
cat > "$(git rev-parse --git-common-dir)/hooks/pre-commit" <<'EOF'
#!/bin/sh
echo "*** hook running as $(whoami) in $(pwd) ***"
EOF
chmod +x "$(git rev-parse --git-common-dir)/hooks/pre-commit"

# Now you, in your own repository, make an ordinary commit
cd ../hook-demo
git commit -q --allow-empty -m "an ordinary commit"
# -> *** hook running as you in /path/to/hook-demo ***
```

This is also why a worktree cannot be the isolation layer for a containerised agent. Handing a container a linked worktree means mounting the parent’s real .git, because that is where the worktree’s own state lives. A writable .git/hooks on the host side of that mount runs on the host, and the container stops meaning anything.

### Rewrite who your commits are from

The config is shared, so git config inside a worktree writes the parent’s .git/config:

```bash
git init -q --initial-branch=main id-demo
cd id-demo
git commit -q --allow-empty -m init
git branch agent-work
git worktree add -q ../id-agent agent-work

cd ../id-agent
git config user.email "agent@example.com"

cd ../id-demo
git config user.email
# -> agent@example.com
git config --show-origin user.email
# -> file:.git/config  agent@example.com

git commit -q --allow-empty -m "a commit you made yourself"
git log -1 --format='%an <%ae>'
# -> Your Name <agent@example.com>
```

Sit with the last two lines. That is not the agent’s commit. It is yours, in your repository, carrying an author line something else picked.

### Take another worktree’s stash

There is one refs/stash per repository, and it behaves the way a single stack shared between uncoordinated writers would:

```bash
git init -q --initial-branch=main stash-demo
cd stash-demo
echo original > file.txt && git add file.txt && git commit -q -m "add file"
git branch branch-a
git branch branch-b
git worktree add -q ../stash-a branch-a
git worktree add -q ../stash-b branch-b

cd ../stash-a
echo "AGENT A PRECIOUS WORK" > file.txt
git stash -q                 # A parks its work

cd ../stash-b
git stash pop                # B pops it, without ever asking for it
cat file.txt
# -> AGENT A PRECIOUS WORK

cd ../stash-a
git stash list               # -> empty
cat file.txt                 # -> original. A's work is now in B's tree.
```

One detail is load-bearing, and it is why some versions of this repro floating around do not work: file.txt is committed before the branches are created, so it is tracked in both worktrees. Plain git stash ignores untracked files, so on a brand-new file it prints No local changes to save, stashes nothing, and the pop fails with No stash entries found. Use a tracked file, or git stash -u.

### Rewrite refs under a sibling

Every worktree writes into one refs/heads and one object store. An agent that runs git gc runs it for the whole repository, parent included. An agent that force-updates a branch, rebases, or reaches for git reset --hard is mutating refs that other worktrees resolve against, and a commit one agent orphans can go unreferenced under another’s feet. These are not exotic commands. They are what something reaches for when it gets confused and decides to tidy up.

### Collide on a branch name

Shared refs also mean git refuses the same branch in two worktrees:

```bash
$ git worktree add ../probe main
Preparing worktree (checking out 'main')
fatal: 'main' is already used by worktree at '/path/to/repo'
```

Harmless next to the rest, but it is the first wall people hit, and it is what pushes them into generating a throwaway branch per worktree purely to satisfy git.

## The fixes that do not fix it

Two mitigations come up every time this is discussed. Neither holds.

Per-worktree config. extensions.worktreeConfig is off by default, and switching it on only helps if the writer opts into git config --worktree. A plain git config, which is what anything not specifically being careful will run, still writes the shared file:

```bash
git config extensions.worktreeConfig true    # you opt in, in the parent

cd ../my-worktree
git config --worktree user.email scoped@example.com
git -C ../repo config user.email    # -> you@example.com, unaffected
git config user.email leaked@example.com
git -C ../repo config user.email    # -> leaked@example.com
```

Moving hooks out of .git. This one is circular. core.hooksPath is config, and config is shared, so the worktree points it wherever it likes:

```bash
cd repo && git config core.hooksPath ../safe-hooks    # your mitigation

cd ../my-worktree
mkdir -p evil-hooks && printf '#!/bin/sh\necho pwned\n' > evil-hooks/pre-commit
chmod +x evil-hooks/pre-commit
git config core.hooksPath "$(pwd)/evil-hooks"         # config is shared

cd ../repo && git commit --allow-empty -m "an ordinary commit"
# -> pwned
```

--separate-git-dir fails the same way. It relocates .git, and every worktree still shares whatever it was relocated to.

All three constrain a writer that is trying to behave. None of them reduce what a worktree is able to write.

## Then use a clone. It costs the same.

The standard objection is that a clone per worker means copying the history, and for a local source that is simply not what happens. This is the part I got wrong before, so here are numbers.

Measured against a full clone of git/git: 81,772 commits, 4,828 tracked files, a 318 MB .git, a 58 MB working tree. Each row creates one new checkout from that local source.

A note on method, because it changes the answer. Disk is measured as a cumulative delta over the whole tree. du counts an inode once per invocation, so measuring a hardlinked clone on its own would credit it with bytes it never actually added.

| Creating one checkout | Wall time | Disk added | .git apparent size | Packfiles copied |
|---|---|---|---|---|
| git clone --no-hardlinks | 1791 ms | 373 MB | 315 MB | 1 |
| git clone (local) | 982 ms | 58.9 MB | 318 MB | 1 (hardlinked) |
| git clone --shared | 870 ms | 58.9 MB | 660 KB | 0 |
| git worktree add | 826 ms | 58.7 MB | 4 KB | 0 |

Look at the bottom three rows. 58.7 to 58.9 MB, 826 to 982 ms. They are the same operation as far as your disk is concerned, and that number is the working-tree checkout, matching the source’s 58 MB tree almost exactly. Whichever mechanism you pick, you are paying for one copy of your files and nothing else that matters.

A local git clone does not copy objects, it hardlinks them, which is why its .git reports 318 MB while adding 59 MB of real disk:

```bash
$ stat -f '%i links=%l' reference/.git/objects/pack/*.pack
154102172 links=2
$ stat -f '%i links=%l' plain-clone/.git/objects/pack/*.pack
154102172 links=2     # same inode
```

Only --no-hardlinks pays for the copy, and nobody runs that by accident. If you have been avoiding local clones because you assumed they duplicate history, they do not.

--shared goes further and copies nothing at all. It writes one file:

```bash
$ cat shared-clone/.git/objects/info/alternates
/path/to/reference/.git/objects
$ find shared-clone/.git/objects -type f | grep -v /info/ | wc -l
0
```

Hence a 660 KB .git against the plain clone’s hardlinked 318 MB. The real property that buys you is independence from history size: --shared is O(1) in how much history the source has and O(n) in how many files you check out. The checkout dominates, which is what the table shows.

I have described this before, in this post, as costing “kilobytes and milliseconds.” That is true of the metadata and false of the operation. It costs kilobytes of .git plus one working tree, in under a second.

For that same 59 MB, here is what you get:

```bash
$ cd plain-clone   && git config user.zzTest x && git -C ../reference config user.zzTest
# -> (not set)
$ cd shared-clone  && git config user.zzTest x && git -C ../reference config user.zzTest
# -> (not set)
$ cd worktree      && git config user.zzTest x && git -C ../reference config user.zzTest
# -> set-from-worktree
```

| State | Worktree | --shared clone |
|---|---|---|
| Object store | shared | shared, via alternates |
| Refs / branches | shared | isolated |
| Config | shared | isolated |
| Stash | shared | isolated |
| Hooks | shared | isolated |
| Index | isolated | isolated |
| HEAD | isolated | isolated |

Both share the one thing that is expensive to copy and safe to share. The clone also isolates the five that turn into footguns as soon as there is more than one writer.

## What --shared costs you

It borrows objects, so it depends on the source object store staying where it is. Do not delete the source underneath it, and do not run an aggressive git gc on the source while clones are live, or you can prune objects a clone still references. git clone --dissociate copies the borrowed objects in and cuts the dependency if you want out later.

A plain hardlinked clone is the more robust of the two, and the reason is worth knowing. A hardlink keeps the inode alive by itself: if the source deletes or repacks that packfile, the clone’s link holds the data open anyway. --shared has no such protection, because it holds a path rather than a reference. What you give up is the O(1) property, permanent deduplication, and the ability to cross filesystems, which starts to matter the moment workspaces live on another volume or get bind-mounted into a container.

Neither is strictly better. They fail differently, and both isolate refs, config, stash and hooks.

## When a worktree is the right call

Worktrees share a .git deliberately, and for the job they were built for that sharing is the whole point:

- One person moving between two or three branches. You want branches, stash and config visible everywhere.
- A quick build or test of another branch without disturbing your index.
- Anything where you are the only writer and you know what each command will do before you run it.

Even with agents, one or two of them supervised by someone reading each diff is fine on a worktree and a shell alias. What does not survive is uncoordinated writers. “Share a .git” and “run several processes that act without asking” are in direct tension, and no amount of care in the driving program changes what the shared directory permits.

So: worktree when a person is driving, clone when something else is. The cost is the same either way, which means the only thing you are really choosing is how much damage a confused process can do.

Disclosure: I build Fletch, a macOS app that runs coding agents, so I had to pick one of these. It gives each agent a git clone --shared, for the reasons measured above. Its worktree mode is behind a developer flag, because under a container it would mean mounting the real .git, and the hook in the first repro would run on the host.
