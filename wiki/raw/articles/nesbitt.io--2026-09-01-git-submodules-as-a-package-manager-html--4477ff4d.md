---
title: "Git Submodules as a Package Manager"
url: "https://nesbitt.io/2026/09/01/git-submodules-as-a-package-manager.html"
fetched_at: 2026-09-01T10:00:43.867465+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Git Submodules as a Package Manager

Source: https://nesbitt.io/2026/09/01/git-submodules-as-a-package-manager.html

I added a worktree to a repository last week to try a branch alongside the main checkout, ran
git submodule update --init
in it because the build needed the vendored dependencies, and when I was done went to clean up with
git worktree remove
, which git refused. Per
the man page
only clean worktrees can be removed, and “unclean worktrees or ones with submodules” need
--force
. Submodules get their own clause in that sentence, distinct from dirty state.
git worktree move
is stricter again and
refuses outright
on any worktree containing submodules. I’d spent
the previous week
cataloguing how command-line tools harden their
--force
flags, and here was git requiring one because two of its own features had collided.
GitHub’s
git 2.5 announcement
introduced
git worktree
in July 2015 with a one-line caveat: “It’s not recommended to use
git worktree
with a repository that contains submodules.” Eleven years later git still requires
--force
to remove a worktree that has submodules and refuses to move one. In between,
worktree add
had to be
patched to ignore
submodule.recurse
because honouring it made the internal
reset --hard
recurse into submodule paths that were still empty in the fresh worktree.
This got me thinking about submodules as a package manager. Most of the pieces are there and the behaviour roughly matches, but they don’t quite line up and the experience of using them is worse at almost every step. Enough projects have adopted them and then
backed out
that
“why are git submodules so bad”
is a recurring thread.
The gitlink in the superproject’s tree, a commit SHA recorded at a path with mode
160000
, is the lockfile entry, and the
.gitmodules
file
mapping paths to fetch URLs is the manifest.
git submodule update
reads both and populates the working tree, which is the install step. The pin itself is as precise as any package manager’s: an exact commit identified by object ID.
Resolution
The gitlink records only which commit to check out, so
.gitmodules
carries a
url
per submodule and
update
clones from there, which is the only resolution mechanism. If the upstream repository is renamed, transferred to a different host, or taken private, every downstream pin breaks, even though the SHA is unchanged and the objects still exist in every clone that already has them. The manifest hard-codes a host because git has no lookup from a commit ID to servers that hold it.
Git also copies each URL into the superproject’s
.git/config
the first time
git submodule init
runs, under
submodule.<name>.url
, and later commands read it from there, ignoring
.gitmodules
. Editing the committed
.gitmodules
to point at a mirror or a fork leaves an already-initialised clone unchanged until
git submodule sync
copies the new value across.
The usual workaround in CI is git’s global
url.<base>.insteadOf
config, which rewrites any URL with a matching prefix before fetching, submodule URLs included. The common cases are rewriting
https://github.com/
to
[email protected]
:
so an SSH deploy key applies, or redirecting an internal hostname to a mirror.
Installation
A plain
git clone
writes the gitlink into the index so the submodule directory exists, and leaves it empty until
git submodule update --init
runs or the clone was made with
--recurse-submodules
. The
submodule.recurse
config setting makes
checkout
,
fetch
,
pull
,
grep
and several other commands recurse automatically, and it defaults to off.
By default
update
checks out the gitlink commit, detached, and two independent flags modify that:
--init
: copy any missing
.gitmodules
entries into
.git/config
first, required on first run and a no-op after
--remote
: check out the tip of the submodule’s configured remote-tracking branch instead of the gitlink commit (the remote’s
HEAD
if
submodule.<name>.branch
is unset)
The
command reference
documents both, though the name
update
conflates “install what’s pinned” with “update to latest”. Switching branches in the superproject changes the gitlink in the index and leaves the submodule’s working tree wherever it already was, so
git status
immediately shows the submodule as modified. Passing
--recurse-submodules
to
checkout
, or setting
submodule.recurse
, brings the submodule working tree along with the branch switch. The Rust project’s
account of moving compiler subprojects off submodules
lists this cluster from experience: checkouts left empty or on the wrong commit after clone, unrelated submodule bumps landing in pull requests because a branch switch left the submodule dirty, and custom logic in the
bootstrap
build tool to check each submodule out to the right commit before building.
Storage
A submodule’s git directory is stored under the superproject’s
$GIT_DIR/modules/<name>/
, with a
.git
file in the submodule’s working tree containing a
gitdir:
pointer back to it and a
core.worktree
setting pointing the other way.
git submodule absorbgitdirs
migrates older clones that still have a nested
.git/
directory. Each entry under
modules/
is a git directory with its own refs, HEAD, index, config, hooks, and by default its own object store. Removing a submodule is correspondingly spread across three places:
git rm <path>
drops the gitlink and the
.gitmodules
entry,
git submodule deinit <path>
clears the working tree and the
.git/config
entry, and the absorbed
$GIT_DIR/modules/<name>
directory that both leave behind is
documented
as a manual
rm -rf
.
Worktrees and submodules collide over this layout because a linked worktree shares the superproject’s
$GIT_DIR
but has its own working tree, HEAD, and index under
$GIT_DIR/worktrees/<id>/
. Put two worktrees on different superproject branches and they reference the same submodule at two different commits. Each needs its own submodule checkout and index, tied to storage that’s partly per-worktree and partly shared.
worktree remove
requires the override rather than checking whether that state is disposable, and
worktree move
refuses because the pointer-file rewrite it would need is unimplemented.
Xavier Morel
asked on the git list this March
whether a submodule checkout could itself be a worktree of an existing shared clone, having found bare repositories plus worktrees worked well for a set of related projects but that adding submodules on top always cloned fresh. An
RFC
and a
three-patch series
proposing
--recurse-submodules
for
git worktree add
followed in April, giving each linked worktree its own submodule git directory under
$GIT_COMMON_DIR/worktrees/<id>/modules/
and sharing the object storage between them by hardlink.
The same multiplication happens in a single-worktree clone when two submodules both depend on a third repository. Each path in the superproject gets its own
modules/
entry, its own object store unless alternates are configured by hand, and its own gitlink. The two pins can point at different commits of the same repository, and git treats them as unrelated checkouts. Package managers with a shared cache (cargo’s
registry cache
, pnpm’s
content-addressable store
, the
Go module cache
) store the bytes once and check them out per location.
Updating
The gitlink holds one commit SHA, so moving a submodule forward means entering it, fetching, checking out the new commit, leaving, and
git add <path>
in the superproject to record the new gitlink.
git submodule update --remote
fetches the configured branch’s tip and checks that out instead of the recorded gitlink, and committing the result in the superproject is what moves the pin.
.gitmodules
can name a
branch
per submodule for
--remote
and the update bots to follow. A plain
update
ignores that field and checks out the gitlink SHA regardless. There is no syntax for a version range, a tag pattern, or a minimum commit, so the manifest’s only floating reference is a branch name and the gitlink is the only pin.
Dependabot and Renovate can both open pull requests bumping a gitlink. Dependabot’s
gitsubmodule
ecosystem
proposes a new gitlink SHA when the submodule’s configured branch moves, and Renovate’s
git-submodules
manager
does the same, shipping disabled by default; both follow branch tips because a branch name is the only reference the manifest exposes.
Security
.gitmodules
is committed to the repository, so a hostile upstream controls its contents, and git parses it during
clone --recurse-submodules
before the user has seen any of the fetched files, a combination that has produced remote code execution repeatedly.
CVE-2018-11235
used
../
in a submodule’s name so its git directory, hooks included, was written outside
$GIT_DIR/modules/
and a
post-checkout
hook ran during clone. In
CVE-2018-17456
the submodule URL began with
-
, so the child
git clone
parsed it as an option, the class of bug git’s
--end-of-options
delimiter defends against.
CVE-2022-39253
was a disclosure bug: a symlink in a submodule’s object directory made a local-transport clone copy arbitrary files from the victim’s disk. The fix changed the
protocol.file.allow
default to
user
, so local-path submodules now need an explicit opt-in.
CVE-2024-32002
combined a symlink with a case-insensitive filesystem to write a hook into
.git/
during recursive clone. I covered the broader pattern of package-manager checkout paths as an attack surface in
the CWE field guide
.
Abstraction
Submodules expose git’s internals directly: object IDs as the pin, detached HEADs after update, the
$GIT_DIR/modules/
layout, transport URLs in the manifest. A package manager wraps the equivalents behind a manifest format, a resolver, and a local cache; submodules surface them raw.
Most of the gaps map to things package managers already solved: a shared object cache, recursing into dependencies by default on clone and checkout, a single lifecycle for adding and removing a dependency, range constraints in the manifest. The
April patch series
adding
--recurse-submodules
to
git worktree add
tackles one instance of the storage problem, giving each worktree its own submodule checkout over hardlinked shared storage. Resolution is the harder one: a commit SHA is a host-independent identity for the object, and the URL in
.gitmodules
is git’s only mapping from that identity to a server that holds it.
