---
title: "Ian Nuttall — Barkeep: macOS menu bar manager"
date: 2026-08-25
date_ingested: 2026-08-25
source: https://x.com/iannuttall/status/2092236673643897146
author: Ian Nuttall (@iannuttall)
type: x_post
tags: [developer-tooling, macos, local-first, open-source]
related:
  - entities/ian-nuttall
---

# Ian Nuttall — Barkeep: macOS menu bar manager

## Tweet

**Posted:** 2026-08-25T13:04:29Z  
**Author:** Ian Nuttall (@iannuttall), indie hacker and AI tooling builder  
**URL:** https://x.com/iannuttall/status/2092236673643897146  
**Context:** Reply to his own earlier post announcing the project.

> Repo: [GitHub - iannuttall/barkeep](https://github.com/iannuttall/barkeep)

**Engagement (2026-08-25 UTC):** 8 likes, 1 reply, 0 retweets, 0 quotes, 11 bookmarks, 807 impressions.

## Linked repository: `iannuttall/barkeep`

- **URL:** https://github.com/iannuttall/barkeep
- **Description:** "Manage hidden macOS menu bar items from one place"
- **Language:** Swift
- **License:** MIT
- **Created:** 2026-08-23
- **Stars/forks/watchers:** 13 / 3 / 13 at ingest
- **Default branch:** main
- **Topics:** accessibility, local-first, macos, menu-bar, menu-bar-manager, swift

### What the repo says (README summary)

**Barkeep** is a native macOS menu bar manager. It organizes status bar items into three sections:

| Section | Behavior |
|---|---|
| **Always visible** | Items stay in the menu bar. |
| **Hidden** | Shown/hidden by clicking the Barkeep icon. |
| **Always hidden** | Shown only on Option-click of the Barkeep icon. |

Key characteristics:

- **Local-first, no account, no analytics.** Settings, item rules, and profiles are stored in a single JSON file at `~/Library/Application Support/Barkeep/state.json`.
- **Safe moves:** Barkeep checks the real menu bar after each move and saves the new section only when macOS completes the move. Launch, wake, display changes, and timers cannot move an item.
- **Keyboard-driven:** `Command-Backslash` toggles items; `Command-Shift-Space` searches and opens a menu bar item.
- **Security:** Touch ID or Mac password can protect reveal paths; Developer ID signing and Apple notarization; public builds include SHA-256 checksums.
- **Build:** Xcode 16+ and XcodeGen required for local builds; `make check/build/install/dmg/release` commands.

## Wiki context

This is a relatively minor macOS developer tool, but it is consistent with Ian Nuttall's pattern of shipping polished, practical, open-source utilities and sharing the repo publicly on X. It is logged here for completeness; no dedicated concept page is warranted. The [[entities/ian-nuttall]] entity page should note Barkeep in its projects/timeline.

## Related pages

- [[entities/ian-nuttall]] — Ian Nuttall
