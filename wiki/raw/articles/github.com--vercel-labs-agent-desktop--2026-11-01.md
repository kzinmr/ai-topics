# vercel-labs/agent-desktop

> Source: https://github.com/vercel-labs/agent-desktop
> Scraped from GitHub README (server-rendered `<article>` block) on 2026-11-01.
> Surfaced by X scan: [@ctatedev](https://x.com/ctatedev) amplifying the parent
> announcement tweet (2026-10-31), built by @mdlahfir who "just joined the Vercel Labs team".

## Repo description

> Agent Desktop gives any agent reliable computer use on the desktop. Built with
> Rust, it sees any app's real UI structure through OS accessibility trees and
> operates it — refs stay stable and actions stay safe to retry, instead of
> guessing from pixels. - vercel-labs/agent-desktop

## README (excerpt)

**agent-desktop** — Computer use for AI agents: read and operate desktop apps
through the OS accessibility tree.

A CLI and C library for macOS, Windows and Linux. A snapshot returns JSON with a
`ref` for every element an agent can act on. The agent acts on a `ref` and
snapshots again to check, with no pixel matching; the loop stays in your agent.

On macOS, CLI calls reuse a private command host for each snapshot namespace and
binary build. It retains native accessibility objects so a removed row cannot
silently resolve to a surviving row with the same identifier. The host exits
after 15 idle minutes. `TMPDIR` must be owned by the current user with mode
`0700`; the standard macOS per-user temporary directory satisfies this
requirement. Headless calls still prohibit foreground activation and synthesized
input.

Snapshots, clipboard reads, screenshots, command output and debug artifacts can
contain private desktop content. Keep them out of public logs and uploads. The
optional JEV helper sends screen descriptions to a configured model provider; it
is separate from the native CLI. See privacy and data handling.

### Installation

Install on macOS, Windows and Linux with npm:

```
npm install -g agent-desktop
agent-desktop version
```

Bun, Yarn and pnpm can install the same package. It includes native binaries and
platform helpers for x64 and ARM64. For direct execution without a JavaScript
launcher, download the matching native archive from GitHub Releases and keep its
helper beside the executable. Official Homebrew and Scoop packages are being
submitted; they are not yet available in the default catalogs. The repository no
longer maintains a custom Homebrew tap or Scoop bucket.

- macOS needs Accessibility permission: `agent-desktop permissions --guide`.
- Windows needs no grant for apps at your terminal's integrity level.
- Linux needs the user's graphical session with `at-spi2-core`.

### Quick start

Observe, act on a ref, observe again. Any app name from
`agent-desktop list-apps` works; Finder is the macOS example. Each command
prints one JSON envelope.

```
agent-desktop snapshot --app Finder -i         # interactive elements, each with a ref
agent-desktop click @s8f3k2p9:e8               # act on a ref from that snapshot
agent-desktop snapshot --app Finder -i         # observe again to verify
```

Example snapshot envelope (`version: 2.5`) returns a `tree` of role/name/
`ref_id`/available_actions nodes with `snapshot_id`, `ref_count`, `complete`.

- Refs belong to their snapshot. A bare `@e8` is rejected with `INVALID_ARGS`.
  When the UI changes, an action returns `STALE_REF` or `AMBIGUOUS_TARGET`: take
  a new snapshot and use its refs.
- Several windows give `AMBIGUOUS_TARGET`; snapshot lists candidate window ids in
  `error.details`. Pass one with `--window-id`.
- Dense apps: map first with `snapshot --skeleton --app Slack -i --compact`, then
  drill into one region with `snapshot --root @s8f3k2p9:e3 -i --compact`.
- **Headless by default.** Ref actions go through the accessibility API without
  moving the pointer or taking focus. The global `--headed` flag allows physical
  input.
- PowerShell: quote every ref (`'@s8f3k2p9:e8'`), because a bare `@token` is the
  splatting operator.

### For AI agents

The binary carries its own docs, matched to its version:

```
agent-desktop skills get desktop    # the loop, refs, verification and retry rules
agent-desktop skills get platform   # what differs on the OS you run on
agent-desktop <command> --help      # flags for one command
```

Install the skill into an agent harness from skills.sh:
`npx skills add https://github.com/vercel-labs/agent-desktop`

## Announcement tweet (parent, @ctatedev, 2026-10-31)

> Introducing agent-desktop
>
> agent-browser, for your whole computer
>
> → Computer Use for any coding agent
> → macOS, Windows and Linux
> → Runs in bg while you keep working
> → Agents use your computer in parallel, each with its own cursor

Amplified by @ctatedev: *"Star it, fork it, tell your agents about it. Built by
@mdlahfir, who just joined the Vercel Labs team!"*
