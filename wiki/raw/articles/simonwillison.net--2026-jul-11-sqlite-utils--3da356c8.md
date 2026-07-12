---
title: "sqlite-utils 4.1"
url: "https://simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything"
fetched_at: 2026-07-12T07:01:17.034295+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.1

Source: https://simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything

The first dot-release since
4.0 a few days ago
, introducing a number of minor new features.
sqlite-utils insert
and
sqlite-utils upsert
now accept a
--code
option for
providing a block of Python code
(or a path to a
.py
file) that defines a
rows()
function or
rows
iterable of rows to insert, as an alternative to importing from a file. (
#684
)
sqlite-utils
already had features that allow you to pass blocks of Python code as CLI arguments, for example
this one
for the
sqlite-utils convert
command:
sqlite
-
utils
convert
content
.
db
articles
headline
'
def
convert
(
value
):
return
value
.
upper
()'
Allowing blocks of code to
generate new rows directly
was on obvious extension of that pattern:
sqlite
-
utils
insert
data
.
db
creatures
-
-
code
'
def
rows
():
yield
{
"id"
:
1
,
"name"
:
"Cleo"
}
yield
{
"id"
:
2
,
"name"
:
"Suna"
}
'
-
-
pk
id
A long-standing feature request which turned out to be a
simple implementation
.
New
table.drop_index(name)
method and
sqlite-utils drop-index
command for dropping an index by name. Both accept
ignore=True
/
--ignore
to ignore a missing index. (
#626
)
sqlite-utils query
can now read the SQL query from standard input by passing
-
in place of the query, for example
echo "select * from dogs" | sqlite-utils query dogs.db -
. (
#765
)
Two more small features. I had Codex review all open issues and highlight the easiest ones!
sqlite-utils upsert
can now infer the primary key of an existing table, so
--pk
can be omitted when upserting into a table that already has a primary key.
Another Codex suggestion, an obvious missing CLI feature from a Python library improvement that shipped in the 4.0 release.
table.transform()
and
table.transform_sql()
now accept
strict=True
or
strict=False
to change a table’s
SQLite strict mode
. Omitting the option preserves the existing mode. (
#787
)
The
sqlite-utils transform
command now accepts
--strict
and
--no-strict
to change a table’s strict mode. (
#787
)
These two were inspired by
Prefer STRICT tables in SQLite
by Evan Hahn, which did the rounds
on Hacker News
today. Evan pointed out that:
Unfortunately, I don’t think there’s a way to ALTER a table to make it strict. I think you have to copy the data out of the non-strict table into the strict one.
That's exactly what the
sqlite-utils transform mechanism
does, so I extended it to add the ability to switch tables from strict to non-strict and vice-versa.
Here's
the GPT-5.6 Sol xhigh Codex transcript
I used to implement those new strict table features. One of the most useful prompts I ran was this one:
use uv run python -c and manually exercise the new .transform(strict=) option, see if you can find any edge-cases or bugs
Effectively telling the model to manually test its work, outside of the automated tests it had already written. This turned up two minor issues that we then fixed.
