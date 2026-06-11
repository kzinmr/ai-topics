---
source_url: https://github.com/hynek/structlog/releases/tag/26.1.0
title: "structlog 26.1.0 Release"
date: 2026-06-06
source_slug: hynek-structlog
author: Hynek Schlawack
x_referrer: hynek
tag_name: "26.1.0"
github_release_id: 335332226
---

# structlog 26.1.0

**Release date:** 2026-06-06
**Author:** Hynek Schlawack (@hynek)
**Repository:** [hynek/structlog](https://github.com/hynek/structlog)

## Highlights

Given how long this release took, it's pretty thicc with nice things all over the board! Apologies for the long release cycle; it's been a victim of the slopocalypse and me trying to navigate my way thru the new normal. Extra big thanks to my sponsors for not abandoning me in these unironically trying times. ❤️

## Full Changelog

### Removed

- Python 3.8 and 3.9 support.

### Deprecated

- Support for *better-exceptions* is deprecated and will be removed within a year. Use the Rich integration or copy-paste the [one line of code you need](https://github.com/hynek/structlog/blob/2c059a0dc029d9370e1e4a6e9683063205bbb68f/src/structlog/dev.py#L488-L498). [#802](https://github.com/hynek/structlog/pull/802)

### Added

- Python 3.15 support. [#813](https://github.com/hynek/structlog/pull/813)

- `structlog.dev.rich_monochrome_traceback` for Rich-based monochrome exception rendering and add support for it throughout `structlog.dev.ConsoleRenderer` when the user asks for no colors. [#794](https://github.com/hynek/structlog/pull/794)

- `structlog.BytesLogger` now has a `name` attribute which allows you to use it with the `structlog.stdlib.add_logger_name()` processor *without* using the standard library integration. [#786](https://github.com/hynek/structlog/pull/786)

- `structlog.processors.CallsiteParameterAdder` now supports `CallsiteParameter.QUAL_MODULE` that adds the qualified import name of the module of the callsite, or `__main__` if the module is the entry point. This is only available for *structlog*-originated events since the standard library has no equivalent (except for the convention of setting the logger's name to `__name__`). [#812](https://github.com/hynek/structlog/pull/812)

- `structlog.stdlib.BoundLogger` now has `is_enabled_for()` and `get_effective_level()` methods that are snake_case aliases for its `isEnabledFor()` and `getEffectiveLevel()` methods. This makes it more compatible with the native `structlog.typing.FilteringBoundLogger`, so you can swap configurations without changing your call sites. [#818](https://github.com/hynek/structlog/pull/818)

### Changed

- `structlog.dev.ConsoleRenderer` does not warn anymore when the `exception` key has a rendered value despite having a fancy formatter configured. [#790](https://github.com/hynek/structlog/pull/790)

### Fixed

- `structlog.BytesLogger`, `structlog.PrintLogger`, and `structlog.WriteLogger` now hold *weak* references to the files they use for output. This prevents their leakage in long-running processes that open many logfiles, such as task executors that create a per-task `BytesLogger` or `WriteLogger`. [#807](https://github.com/hynek/structlog/pull/807)

- `structlog.WriteLogger` is usable after unpickling. [#787](https://github.com/hynek/structlog/pull/787)

- `structlog.processors.CallsiteParameterAdder` now reports the calling thread's id and name for async log methods, instead of the thread from the executor pool that runs the underlying sync logger. [#710](https://github.com/hynek/structlog/issues/710) [#805](https://github.com/hynek/structlog/pull/805)

---

This release contains contributions from @ashb, @BlocksecPHD, @funkyfuture, @hynek, @JiwaniZakir, @sirosen, and @veeceey.
