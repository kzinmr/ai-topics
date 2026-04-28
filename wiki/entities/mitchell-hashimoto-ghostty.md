---
title: Mitchell Hashimoto — Ghostty Terminal Emulator
type: entity
handle: "@mitchellh/ghostty"
created: 2026-04-27
updated: 2026-04-27
depth: 22000
status: L3
tags:
  - ghostty
  - zig
  - terminal-emulator
  - libghostty
  - gtk
  - gpu-rendering
sources: []
---

# Ghostty Terminal Emulator

[[mitchell-hashimoto]] created Ghostty, a next-generation terminal emulator written from scratch in **Zig**:

- Native macOS (AppKit) and Linux (GTK/GObject) implementations
- GPU-accelerated rendering
- True color support, splits, vim compatibility
- Zig as the primary language for performance and safety
- libghostty — embeddable terminal library for other applications
- Closed beta since 2023, public release planned

## Technical Work

- Full GTK rewrite using GObject type system from Zig (Aug 2025)
- Every PR run through Valgrind for memory safety verification
- Zig debug allocator for leak detection
- 5 complete GUI rewrites, each carrying forward lessons learned

**On Zig + AI limitations:**
> "Anything more than trivial changes to Zig code bases is still hopeless with that language. The workaround I found is when it's helpful, I have it rewrite its solution in another language that it's good at, whether that's C or Rust or Swift or Python, and then I'll do the conversion back to Zig myself."

**Render Thread Optimization** (Nov 2023): "Love doing highly targeted performance work. I've been working the past few days on changing the way the render thread in Ghostty reads the terminal data (which requires a lock that blocks IO). I've got lock held time down 2.4x so far."

## "Vibing" a Non-Trivial Feature — Full Session Transparency (Oct 2025)

Mitchell published a transparent account of shipping a real Ghostty feature using AI agentic coding tools. The feature: **unobtrusive macOS automatic update notifications** — triggered after a high-profile OpenAI keynote demo was rudely interrupted by a Ghostty update prompt.

> "I recently shipped a non-trivial Ghostty feature that was largely developed with AI. I'm regularly asked to share non-trivial examples of how I use AI and agentic coding tools and this felt like a golden opportunity to walk through my process with a well-scoped, real-world, shipping feature."

**Key workflow patterns:**

1. **Plan First, Code Second** — "Creating a comprehensive plan interactively with an agent is a really important first-step for anything non-trivial. I usually also save it out to something like `spec.md`."
2. **The "Anti-Slop Session"** — When AI gets stuck, Mitchell steps back and manually restructures. Switched from optional-heavy struct to a tagged union pattern.
3. **Scaffold + TODO Pattern** — "AI is very good at fill-in-the-blank or draw-the-rest-of-the-owl."
4. **Simulation Testing** — AI generates multiple test scenarios (happy path, errors, not found).
5. **Final Manual Review** — "Please don't ever ship AI-written code without a thorough manual review."

**Cost & Time:** 16 sessions, $15.98 in token spend on Amp (using GPT-5.2-Codex), ~8 hours over 3 calendar days.

## Ghostty Non-Profit Transition (Dec 2025)

Ghostty is fiscally sponsored by **Hack Club**, a registered 501(c)(3) non-profit.

> "I want to lay bricks for a sustainable future for Ghostty that doesn't depend on my personal involvement technically or financially."

> "I want to squelch any possible concerns about a 'rug pull'. A non-profit structure provides enforceable assurances: the mission cannot be quietly changed, funds cannot be diverted to private benefit, and the project cannot be sold off or repurposed for commercial gain."

**Financial commitment:**
- Mitchell's family donating $150,000 directly to Hack Club (separate from Ghostty)
- $50,000 personal donation to Ghostty non-profit
- 7% of donations go to Hack Club for administrative overhead
- All financial transactions publicly viewable via Hack Club Bank ledger
- **Zero** funds will go to Mitchell personally — legally guaranteed

Simon Willison noted: "I have been enjoying hitting refresh on the Hack Club Bank transactions throughout today and watching the number grow — it's up to $2,000 now which would fund 33 hours of contributor time based on Ghostty's announced $60/hour standard."

Mitchell responded: "We're up to almost 200 paid developer hours at the time of posting this. Almost everyone who has given today is an individual."

## libghostty — Embeddable Terminal Emulation (Sep 2025)

Mitchell announced **libghostty**, a zero-dependency library extracted from Ghostty's production core:

> "My answer to this is libghostty: a cross-platform, minimal dependency library that exposes a C API so feature-rich, correct, and fast terminal functionality can be embedded by any application anywhere."

**Technical highlights:**
- Zero dependencies (doesn't even require libc)
- SIMD-optimized parsing
- Supports Kitty Graphics Protocol and Tmux Control Mode
- Target: macOS, Linux, Windows, embedded, WASM
- Initial Zig module available; C API in development

## Ghostty Blog Posts

- **[We Rewrote the Ghostty GTK Application](https://mitchellh.com/writing/ghostty-gtk-rewrite)** (Aug 14, 2025) — Deep technical post on interfacing GObject type system from Zig and verifying with Valgrind. "Our Zig codebase had one leak and one undefined memory access. That was really surprising to me (in a good way)."
- **[Talk: Introducing Ghostty and Some Useful Zig Patterns](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)** (Sep 12, 2023) — Zig Showtime talk covering comptime interfaces, Swift integration, and Ghostty's architecture.

## Sources

- [Ghostty GTK Rewrite](https://mitchellh.com/writing/ghostty-gtk-rewrite)
- [Ghostty Zig Patterns Talk](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Zed Blog: Agentic Engineering in Action](https://zed.dev/blog/agentic-engineering-with-mitchell-hashimoto)
