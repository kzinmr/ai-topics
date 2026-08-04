---
title: "TerminalWidget for Mac, iPhone, and iPad"
url: "https://terminalwidget.app/"
fetched_at: 2026-08-04T10:18:16.558318+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# TerminalWidget for Mac, iPhone, and iPad

Source: https://terminalwidget.app/

How do I update a widget from a script or remote job?
Use the included terminal-widget CLI with flags like --target, --text, --progress, --chart, --icon, and --fg, or push the same fields via Shortcuts, AppleScript, or the URL scheme. On Mac, updates apply immediately. On iPhone and iPad, content syncs through iCloud after TerminalWidget has been opened once and notifications are allowed so background pulls can wake the app.
Can tapping a widget run an action?
Yes. You can assign a tap/click action per widget target — open a URL, open a Mac app, run a Shortcut, run a shell command (macOS), or refresh from a URL. Actions sync with the widget payload over iCloud. On iOS, URL and Shortcut actions are supported; Mac-only app and shell actions fall back to normal open/update behavior.
What can widgets display?
Plain or formatted text, progress (0–100), sparklines and other chart styles, matrix-style integer displays, tables (CSV/TSV/JSON), and local or remote images including edge-to-edge layouts. Colors, fonts, icons, titles, and captions are configurable per update.
Do I need internet or iCloud for sync?
Local Mac updates work without the network. Cross-device sync uses iCloud, so each Mac, iPhone, and iPad should be signed into the same Apple ID with iCloud enabled for TerminalWidget. iOS and iPadOS also need notification permission so widgets can refresh in the background when another device updates a target.
