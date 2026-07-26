---
title: "Ruff v0.16.0"
url: "https://simonwillison.net/2026/Jul/25/ruff/#atom-everything"
fetched_at: 2026-07-26T10:22:50.684831+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Ruff v0.16.0

Source: https://simonwillison.net/2026/Jul/25/ruff/#atom-everything

Ruff v0.16.0
. Astral shipped a significant new version of their Ruff Python linting tool a few days ago on July 23rd. I noticed today because my various CI jobs all started failing thanks to new default Ruff checks and my unpinned
"ruff"
dev dependency.
From Brent Westbrook's announcement post:
Ruff now enables 413 rules by default, up from 59 in previous versions.
Since Ruff's default rule set was last modified in
v0.1.0
, the number of rules in Ruff has grown from 708 to 968. Many of these rules catch severe issues, including
syntax errors
and
immediate runtime errors
but were not previously enabled by default. With the new rule set, Ruff will bring these issues and many others to your attention without any Ruff configuration.
Here's a one-liner for trying it on any Python project:
uvx ruff@latest check .
I ran the latest Ruff against my three biggest projects -
Datasette
,
sqlite-utils
, and
LLM
- and it found
hundreds
of minor issues that breached the new default rules.
All three projects have very comprehensive test suites, executed in CI against Python 3.10 through Python 3.14, so upgrades like this are pretty safe. The following command did the bulk of the upgrades:
uvx ruff@latest check . --fix --unsafe-fixes
Against
sqlite-utils
, that command reported:
Found 1618 errors (1538 fixed, 80 remaining).
As an illustrative example, here are three of the remaining issues. Ruff does a nice job of explaining each one:
DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> tests/test_duplicate.py:17:10
   |
15 |     "datetime_col" TEXT)""")
16 |     # Insert one row of mock data:
17 |     dt = datetime.datetime.now()
   |          ^^^^^^^^^^^^^^^^^^^^^^^
18 |     data = {
19 |         "text_col": "Cleo",
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

BLE001 Do not catch blind exception: `Exception`
  --> tests/test_plugins.py:16:12
   |
14 |         db.execute("select * from pragma_function_list()")
15 |         return True
16 |     except Exception:
   |            ^^^^^^^^^
17 |         return False
18 |     finally:
   |

B018 Found useless attribute access. Either assign it to a variable or remove it.
  --> tests/test_update.py:46:5
   |
44 | def test_update_invalid_pk(fresh_db, pk, update_pk):
45 |     table = fresh_db["table"]
46 |     table.insert({"id1": 5, "id2": 3, "v": 1}, pk=pk).last_pk
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
47 |     with pytest.raises(NotFoundError):
48 |         table.update(update_pk, {"v": 2})
   |
Unsurprisingly, given Astral's
new home at OpenAI
, this output provides everything a coding agent would need to fix the problems.
I had Codex (GPT-5.6 Sol high)
upgrade LLM
and
sqlite-utils
, and Claude Code (with Opus 5)
upgrade Datasette
.
