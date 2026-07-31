---
title: "Git Worktrees as Agent Isolation Boundary"
created: 2026-07-31
updated: 2026-07-31
type: concept
tags: [coding-agents, sandbox, security, git, isolation]
sources: ["[[raw/articles/2026-07-30_fletch_git-worktrees-agent-isolation]]"]
related: [concepts/sandbox/infrastructure, concepts/sandbox/in-process, concepts/coding-agents/coding-agents, concepts/ai-agent-security]
---

# Git Worktrees as Agent Isolation Boundary

## Overview

`git worktree` is commonly recommended as the default isolation strategy for running multiple AI coding agents in parallel on the same repository. The pitch is appealing: one command, no duplicated history, a second checkout in under a second. **Both halves of that pitch are wrong.** The isolation is far thinner than "isolated worktree" implies, and the cost of doing it properly — with local clones — is identical. Alex Chaplinsky (fletch.sh, July 2026) demonstrated that a linked worktree gives an agent write access to `.git/hooks`, `.git/config`, `refs/stash`, and the shared ref namespace, enabling arbitrary code execution on the host, commit authorship tampering, stash theft, and ref corruption. A local `git clone` (which hardlinks objects by default) provides actual isolation at the same wall-clock time and disk cost.

## The Problem: What a Linked Worktree Actually Shares

Inside a linked worktree, `.git` is a file pointing to the parent repository:

```
$ cat ../my-worktree/.git
gitdir: /path/to/repo/.git/worktrees/my-worktree
```

Git splits state into **per-worktree** and **common**. Per-worktree state is minimal: `HEAD`, the index, `ORIG_HEAD`, and a few rebase/bisect files. Everything else resolves through `--git-common-dir` back to the original `.git`:

- **Object store** (`.git/objects`) — safe to share, this is the whole point of worktrees.
- **Refs and branches** (`refs/heads`, `packed-refs`) — one namespace for every worktree.
- **Config** (`.git/config`) — shared, so `git config` in a worktree writes the parent's config.
- **Stash** (`refs/stash`) — a single stack shared between uncoordinated writers.
- **Hooks** (`.git/hooks`) — arbitrary code execution, shared with the parent.

"Isolated worktree" gets used constantly without specifying which of these two lists — the isolated or the shared — is meant. A boundary would mean a process confined to the worktree cannot reach state outside it, and the shared list is a catalogue of the ways it can.

## Attack Vectors

Each of the following was demonstrated on git 2.50.1 with real output.

### Hook Injection — Execute Code on the Host

`.git/hooks` lives in the common directory. A hook installed from a worktree runs **as the host user, in the parent repository**, the next time the triggering command runs:

```bash
cd ../my-worktree
cat > "$(git rev-parse --git-common-dir)/hooks/pre-commit" <<'EOF'
#!/bin/sh
echo "*** hook running as $(whoami) ***"
EOF
chmod +x "$(git rev-parse --git-common-dir)/hooks/pre-commit"

# Next commit in the parent triggers the hook.
```

This is why a worktree cannot be an isolation layer for containerised agents: mounting a linked worktree into a container means mounting the parent's real `.git`, and a writable `.git/hooks` on the host side runs on the host.

### Config Rewriting — Tamper With Commit Authorship

The config is shared. `git config` inside a worktree writes the parent's `.git/config`:

```bash
cd ../my-worktree
git config user.email "agent@example.com"

# The parent's commits now carry the agent's email:
cd ../repo && git log -1 --format='%an <%ae>'
# -> Your Name <agent@example.com>
```

### Stash Theft — Pop Another Agent's Work

`refs/stash` is a single stack shared across all worktrees:

```bash
# Agent A stashes work in worktree-a
cd ../stash-a && echo "PRECIOUS" > file.txt && git stash

# Agent B pops it from worktree-b without asking
cd ../stash-b && git stash pop
cat file.txt  # -> PRECIOUS
```

### Ref Corruption — Mutate Branches and Objects

Every worktree writes into one `refs/heads` and one object store. An agent that runs `git gc`, force-updates a branch, rebases, or does a hard reset mutates refs that other worktrees resolve against. A commit one agent orphans can go unreferenced under another's feet.

### Branch Name Collisions

Shared refs mean `git worktree add` refuses the same branch in two worktrees, forcing agents to generate throwaway branches purely to satisfy git.

## Mitigations and Why They Fail

Three mitigations arise in every discussion. None reduce what a worktree can write.

**Per-worktree config** (`extensions.worktreeConfig`). Off by default. A plain `git config` — which is what anything not specifically being careful will run — still writes the shared `.git/config`. `git config --worktree` is opt-in per-write.

**Moving hooks out of `.git`** via `core.hooksPath`. This is circular: `core.hooksPath` is config, and config is shared, so the worktree can point it back to an attacker-controlled directory. `--separate-git-dir` fails the same way — every worktree still shares whatever it was relocated to.

All three constrain a writer that is *trying to behave*. None constrain what a worktree is *able* to write.

## The Solution: Local Clones

The standard objection is that a clone per worker means copying history. For a local source, that is not what happens. Measured against a full clone of git/git (81,772 commits, 318 MB `.git`, 58 MB working tree):

| Method | Wall Time | Disk Added | .git Apparent Size | Packfiles Copied |
|---|---|---|---|---|
| `git clone --no-hardlinks` | 1,791 ms | 373 MB | 315 MB | 1 |
| `git clone` (local, default) | 982 ms | 58.9 MB | 318 MB | 1 (hardlinked) |
| `git clone --shared` | 870 ms | 58.9 MB | 660 KB | 0 |
| `git worktree add` | 826 ms | 58.7 MB | 4 KB | 0 |

The bottom three rows are the same operation as far as the disk is concerned: 58.7–58.9 MB added, 826–982 ms. A local `git clone` does not copy objects — it hardlinks them, verified by identical inode numbers on packfiles. Only `--no-hardlinks` pays for the copy, and nobody runs that by accident.

**`--shared` clones** go further: they write one alternates file and copy no objects at all, yielding a 660 KB `.git` independent of history size. The tradeoff is a dependency on the source object store. Do not delete or aggressively `git gc` the source while clones are live; `git clone --dissociate` copies borrowed objects in and cuts the dependency.

A plain hardlinked clone is more robust: a hardlink keeps the inode alive regardless of what the source does to its own packfiles. `--shared` holds a path rather than a reference, so it has no such protection. Neither is strictly better — both isolate the five things that matter:

| State | Worktree | Clone |
|---|---|---|
| Object store | shared | shared (hardlinked or alternates) |
| Refs / branches | **shared** | isolated |
| Config | **shared** | isolated |
| Stash | **shared** | isolated |
| Hooks | **shared** | isolated |
| Index | isolated | isolated |
| HEAD | isolated | isolated |

Both share the one thing that is expensive to copy and safe to share. The clone also isolates the five that become footguns with more than one writer.

## Best Practices

- **Person driving → worktree.** Worktrees are correct for one person moving between branches, quick builds/tests, and single-writer scenarios. You want branches, stash, and config visible everywhere.
- **Agent driving → clone.** Give each coding agent its own `git clone --shared` (or plain hardlinked clone for robustness). "Share a `.git`" and "run several processes that act without asking" are in direct tension.
- **Containerised agents must never mount a linked worktree.** A linked worktree's `.git` file resolves to the host's real `.git`. Mounting that into a container means the container writes hooks and config on the host. Use a clone inside the container instead.
- **Cost is a non-objection.** Local clones cost the same wall-clock time and disk as worktrees for any practical repository. The only thing you are really choosing is how much damage a confused process can do.

## See Also

- [[concepts/sandbox/infrastructure]] — OS/hypervisor-level sandboxing (containers, microVMs, gVisor)
- [[concepts/sandbox/in-process]] — In-process isolation via capabilities-based security (Monty)
- [[concepts/coding-agents/coding-agents]] — Coding agent ecosystem and security considerations
- [[concepts/ai-agent-security]] — AI agent security patterns and threat models
