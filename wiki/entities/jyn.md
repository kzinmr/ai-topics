---
title: Jynn Nelson (jyn)
type: entity
created: 2026-04-09
updated: 2026-04-10
tags:
  - person
  - blogger
  - hn-popular
  - rust
  - compiler
  - build-systems
  - developer-tools
  - documentation
sources: []
---


# Jynn Nelson (jyn)

| | |
|---|---|
| **Blog** | [jyn.dev](https://jyn.dev) |
| **RSS** | https://jyn.dev/atom.xml |
| **GitHub** | [github.com/jyn514](https://github.com/jyn514) |
| **Resume** | [jyn.dev/assets/Resume.pdf](https://jyn.dev/assets/Resume.pdf) |
| **Role** | Software Engineer (YottaDB); former Rust team lead (Rustdoc, Bootstrap, Docs.rs) |
| **Location** | Delft, NL |
| **Company** | Ferrous Systems (prior), Redjack (prior), YottaDB (current) |
| **Bio** | Compiler engineer and developer tools specialist. Led Rust teams across rustdoc, bootstrap, and docs.rs. Known for deep technical writing on build systems, the Rust compiler toolchain, and the human side of open-source engineering. Passionate about lowering the barrier to contributing to complex systems projects. |

## Core Ideas

### "The Core of Rust" — Interwoven Complexity

Jyn's most philosophically significant essay argues that **Rust's learning difficulty is a feature, not a bug**. Adapting Stroustrup's famous quote about C++:

> *"Within Rust, too, there is a much smaller and cleaner language struggling to get out: one with a clear vision, goals, focus. One that is coherent, because its features cohere."*

The thesis: Rust's foundational concepts (iterators, Send/Sync, borrow checker, references, traits, generics, pattern matching, enums, closures) are **deeply interwoven**. You can't learn them in isolation because each one affects how the others work. The standard library itself relies on all of them simultaneously.

This is why a 20-line Rust file watcher requires understanding the entire core ecosystem, while the JavaScript equivalent needs only 3 concepts. The complexity isn't accidental — it enables compile-time guarantees that other languages can't provide (like thread safety verified at compile time via Send/Sync + borrow checker + closure capture analysis).

### Build Systems Tradeoffs (4-Part Series)

Jyn wrote the definitive multi-part series on **build system architecture**, grounded in their professional experience maintaining Rust's build system (`x.py`/`bootstrap`):

**Part 1: Build System Tradeoffs**
- The space of concerns: nested invocations, dependency tracking, cross-compilation, libc, dynamic linking, environments
- Configuration languages: use real programming languages, not custom DSLs. *"If I am even TEMPTED to use sed, in my goddamn build system, you have lost."* — Qyriad
- Tradeoff matrix: Manual (make) → Compiler-assisted (Cargo) → Ephemeral state (Docker) → Hermetic (Bazel/Nix) → Tracing (Tup/Ekam)

**Part 2: Negative Build** (architecture for builds that only touch what changed)
**Part 3: Persistence** (orthogonal persistence in build systems)
**Part 4: Build Executor** (market fit analysis, comparing Git vs jj adoption patterns)

Key insight: **Tracing is best for graph generation, hermetic is best for execution.** The ideal system combines both.

### Pre-Commit Hooks Are Fundamentally Broken

A widely-discussed critique of `pre-commit` hooks that demonstrated, through iterative examples, why they break standard Git workflows:

- Hooks run against the **working tree**, not the **staged index** — causing false negatives and false positives
- They trigger during `git rebase -i` and merge conflict resolution, checking commits from other branches
- Attempts to "fix" them (temp directory checkout, diff filtering) all fail in edge cases

> *"There should be a really, really good reason to prevent you from saving your work, and IMO 'doesn't pass the test suite' is not that."*

**Recommendation:** Use `pre-push` hooks instead. The only valid pre-commit use case is **preventing credential leaks**.

### Building a Custom rustc_driver

A deep-dive tutorial on **writing your own Rust compiler driver**, revealing the ~10-step indirection chain behind `cargo clippy`:

1. `cargo clippy` → `cargo-clippy` (cargo subcommand)
2. `cargo-clippy` sets `RUSTC_WORKSPACE_WRAPPER=clippy-driver`
3. `cargo-clippy` calls back to `cargo check`
4. `cargo check` invokes `clippy-driver` instead of `rustc`
5. `clippy-driver` receives `rustc` as an argument and acts as a transparent wrapper

The tutorial covers rustup proxies (hardlinks to `rustup`), shared library loading (`librustc_driver.so` — 136MB vs the 2.6MB `rustc` binary), sysroot resolution, and building a working driver that disables the unsafe checker.

### "I'm Just Having Fun" — Anti-Mystique Writing

One of jyn's most personal essays, addressing the "genius mystique" that surrounds compiler engineering:

> *"i work professionally on a compiler and write about build systems in my free time and as a result people often say things to me like 'reading your posts points to me how really smart you are' or 'reading a lot of this shit makes me feel super small'. this makes me quite uncomfortable and is not the reaction i'm seeking when i write blog posts."*

Key themes:
- **You can do hard things** — "all the things i know i learned by experimenting with them, or by reading books or posts or man pages or really obscure error messages"
- **Everyone has their own specialty** — "i don't know jack shit about economics or medicine! having a different specialty than me doesn't mean you're dumb"
- **Fucking around is the point** — "half the time it's because i want to make art with my code. i really, sincerely, believe that art is one of the most important uses for a computer"
- **Build something for yourself** — the best way to learn is to have a real project that motivates you when "the computer is breaking in three ways you didn't even know were possible"

## Rust Project Contributions

| Team | Role | Period | Key Achievements |
|------|------|--------|-----------------|
| **Rustdoc** | Team Lead | Jul 2020–Jan 2022 | Reduced rustdoc compile time by 9×; stabilized intra-doc links RFC; stabilized macros in doc comments; recruited 5 members |
| **Bootstrap** | Team Founder | May 2022–Jul 2023 | Fixed "broken windows"; made compiler easier to build from source; recruited 3 members |
| **Docs.rs** | Team Lead | Dec 2019–Aug 2023 | Made docs.rs runnable locally without production credentials; greatly reduced incident frequency; recruited 4 members |
| **Prioritization** | Working Area | — | — |
| **Infrastructure** | Member | — | — |

### Stabilized Features (Rust Releases)

- **Intra-doc links** (RFC 2017, stuck 2018, jyn starts work 2020) — Changed the long-term approach of the rustdoc team to ensure future changes wouldn't break the feature. Made it much easier for library authors to write documentation.
- **Macros in doc comments** — Avoided re-implementing 6+ months of work by breaking down communication barriers between teams.
- **Labeled groups in rustdoc** — Stabilized features that had been in limbo for 3+ years.

## Professional History

| Period | Role | Company |
|--------|------|---------|
| Nov 2024–present | Software Engineer | YottaDB |
| Jan 2023–Apr 2024 | Senior Rust Engineer | Redjack |
| — | — | Ferrous Systems |

## Tools & Technical Preferences

Jyn maintains a public tools list reflecting deep opinions about developer experience:

- **Search:** ripgrep + fd (never grep/find)
- **Data:** jq strongly preferred over format-specific tools (except XML)
- **Shell:** zsh (sunk cost), recommends fish for most users, praises PowerShell for typed data
- **Editor:** neovim with heavy custom config, recommends VSCode for most users
- **Terminal:** tmux fork with heavy config, evaluated zellij/wezterm/kitty
- **Rust:** bacon (background checker), cargo bisect-rustc (regression hunting)
- **Debugging:** strace, rr (time-travel debugging), GIT_TRACE, RUSTC_LOG
- **Networking:** tailscale for NAT punching and DDNS

Notable quote: *"i pride myself on integrating tools that were not designed to integrate with each other"*

## Writing Philosophy

Jyn's blog alternates between **deep technical walkthroughs** (build systems, rustc internals, compiler drivers) and **reflective essays** on open-source burnout, hiring practices, and what makes software work sustainable. The writing is both rigorous and humane — technical enough to satisfy compiler engineers, personal enough to connect with anyone who's ever felt intimidated by systems programming.

## Related

- [[concepts/build-systems]] — Deep analysis of build architecture
- [[concepts/rust-ecosystem]] — Rust compiler, tooling, and language design
-  — Making complex systems approachable
-  — The Rust programming language project
-  — Rust consulting company

## Sources

- [The Core of Rust](https://jyn.dev/the-core-of-rust)
- [Build System Tradeoffs](https://jyn.dev/build-system-tradeoffs) (Part 1/4 series)
- [Pre-commit hooks are fundamentally broken](https://jyn.dev/pre-commit-hooks-are-fundamentally-broken/) (Dec 2025)
- [Building your own rustc_driver](https://jyn.dev/rustc-driver/)
- [I'm just having fun](https://jyn.dev/i-m-just-having-fun/) (Dec 2025)
- [Tools I Use](https://jyn.dev/tools/)
- [Redesigning the Initial Bootstrap Sequence](https://blog.rust-lang.org/inside-rust/2025/05/29/redesigning-the-initial-bootstrap-sequence) (May 2025)
- [Rust Project: Jynn Nelson](http://rust-lang.org/governance/people/jyn514)

## References

- jyn.dev--an-engineers-perspective-on-hiring--edc59a49
- jyn.dev--bootstrapping-rust-in-2023--3dfa2a80
- jyn.dev--borrow-checker-faqs--7132b954
- jyn.dev--borrow-mut-dyn-fnmut-brokenlink-cowstring-and-other-valid-ru--8f8e1320
- jyn.dev--brownouts-reveal-system-boundaries--f7cf6b51
- jyn.dev--buffer-overflows-and-stacks-and-assembly-oh-my--5999882e
- jyn.dev--build-system-tradeoffs--0ff00f88
- jyn.dev--building-docs-rs--65a2931d
- jyn.dev--complected-and-orthogonal-persistence--26e868ab
- jyn.dev--constrained-languages-are-easier-to-optimize--e509cb51
- jyn.dev--copying-generic-arrays-in-java--5780981f
- jyn.dev--do-not-disturb-in-gnome--37a7c9af
- jyn.dev--first-post--b1a7806a
- jyn.dev--fun-with-gaming-on-linux--acd61e67
- jyn.dev--git-cheats--362469ae
- jyn.dev--hosting-an-ssh-server--dcfaf6b2
- jyn.dev--how-i-use-my-terminal--b6765ac5
- jyn.dev--how-i-write-blog-posts--84c11f1b
- jyn.dev--how-to-communicate-with-intent--b007de64
- jyn.dev--how-to-maintain-an-open-source-project--c93ba607
- jyn.dev--i-ll-rust-with-you-the-song--d69c0b11
- jyn.dev--i-m-just-having-fun--0119f1ce
- jyn.dev--i-want-a-better-action-graph-serialization--66ab97da
- jyn.dev--i-want-a-better-build-executor--6b29c79b
- jyn.dev--keepass-on-linux-and-android--c203d886
- jyn.dev--negative-build-dependencies--60f804e1
- jyn.dev--object-oriented-python--a17b8525
- jyn.dev--operators-not-users-and-programmers--c8646176
- jyn.dev--password-safety--5f9bc3d6
- jyn.dev--pre-commit-hooks-are-fundamentally-broken--c03fc558
- jyn.dev--remotely-unlocking-an-encrypted-hard-disk--c55c3f63
- jyn.dev--reverse-engineering-x86-assembly--b10a4891
- jyn.dev--rewriting-jython--808d1a1c
- jyn.dev--rust-in-2021--c8dc9f72
- jyn.dev--rustc-driver--1636edf6
- jyn.dev--setting-up-jekyll--028a3f6e
- jyn.dev--sftp-sandboxing--ce05f01a
- jyn.dev--sorry-for-the-rss-screwup--c5aae3d4
- jyn.dev--speed-up--9c48614c
- jyn.dev--talks-assembly--7c2ab39f
- jyn.dev--talks-async-await--e6d48cbb
- jyn.dev--talks-linux--0ab9e213
- jyn.dev--talks-python--f9fe5bd2
- jyn.dev--technical-debt-is-different-from-technical-risk--aca1a3f0
- jyn.dev--terrible-horrible-no-good-very-bad-python--9f7b396d
- jyn.dev--the-core-of-rust--225c597f
- jyn.dev--the-intra-doc-links-saga--f5ee2914
- jyn.dev--the-rust-project-has-a-burnout-problem--56c8f3a7
- jyn.dev--the-terminal-of-the-future--53a0e6fd
- jyn.dev--theory-building-without-a-mentor--ea96bbb6
- jyn.dev--there-is-a-car-in-space--c0ca576d
- jyn.dev--tools--bdfe52fb
- jyn.dev--using-pgp-keys--2f76fb29
- jyn.dev--what-is-a-build-system-anyway--1cc551b0
- jyn.dev--wonder--136680c8
- jyn.dev--you-are-in-a-box--fdc08f9f
