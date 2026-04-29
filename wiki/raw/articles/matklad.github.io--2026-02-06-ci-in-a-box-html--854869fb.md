---
title: "CI In a Box"
url: "https://matklad.github.io/2026/02/06/ci-in-a-box.html"
fetched_at: 2026-04-29T07:02:05.075090+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# CI In a Box

Source: https://matklad.github.io/2026/02/06/ci-in-a-box.html

I wrote
box
, a thin wrapper around ssh for running commands
          on remote machines. I want a box-shaped interface for CI:
const
repository =
"git@forge.com/me/my-project"
;
const
commit_sha =
Deno
.
env
[
"COMMIT"
];
const
runners =
await
Promise
.
all
(
[
"windows-latest"
,
"mac-latest"
,
"linux-latest"
]
.
map
(
(
os
) =>
$
`box create
${os}
`
)
);
await
Promise
.
all
(runners.
map
(
async
($runner) => {
await
$
`box run
${runner}
git clone
${repository}
.`
;
await
$
`box run
${runner}
git switch --detach
${commit_sha}
`
;
await
$
`box run
${runner}
./zig/download.ps1`
;
await
$
`box run
${runner}
./zig/zig build test`
;
}));
That is, the controlling CI machine runs a user-supplied script, whose
          status code will be the ultimate result of a CI run. The script
          doesn’t run the project’s tests directly. Instead, it shells out to a
          proxy binary that forwards the command to a runner box with whichever
          OS, CPU, and other environment required.
The hard problems are in the
["windows-latest", "mac-latest",
              "linux-latest"]
part:
One of them is not UNIX.
One of them has licensing&hardware constraints that make
            per-minute billed VMs tricky (but not impossible, as GitHub Actions
            does that).
All of them are moving targets, and require
someone
to do
            the OS upgrade work, which
might involve pointing and clicking
.
CI discourse amuses me — everyone complains about bad YAML, and it
is
bad, but most of the YAML (and associated reproducibility and
          debugging problems) is avoidable. Pick an appropriate position on a
          dial that includes
What you can’t just do by writing a smidgen of text is getting the
          heterogeneous fleet of runners. And you need heterogeneous fleet of
          runners if some of the software you are building is cross-platform.
If you go that way, be mindful that
The SSH wire protocol only takes a single string as the command,
              with the expectation that it should be passed to a shell by the
              remote end.
Colin Watson on SSH quoting
In other words, while SSH supports syntax like
ssh $HOST cmd arg1 arg2
,
it just blindly intersperses all arguments with a space. Amusing to
          think that our entire cloud infrastructure is built on top of
shell injection
!
This, and the need to ensure no processes are left behind
          unintentionally after executing a remote command, means that you can’t
          “just” use SSH here if you are building something solid.
