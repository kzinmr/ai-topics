---
title: "sqlite-utils 4.0rc1 adds migrations and nested transactions"
url: "https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/#atom-everything"
fetched_at: 2026-06-22T07:01:36.771610+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.0rc1 adds migrations and nested transactions

Source: https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/#atom-everything

sqlite-utils 4.0rc1 adds migrations and nested transactions
21st June 2026
sqlite-utils
is my combined Python library and CLI tool for working with SQLite databases. It provides an extensive set of higher-level operations on top of Python’s default
sqlite3 package
, including support for
complex table transformations
, automatic table creation
from JSON data
and a whole lot more.
I released
sqlite-utils 4.0rc1
, the first release candidate for sqlite-utils v4. The major version bump indicates some (minor) backwards incompatible changes, so I’m interested in having people try this out before I commit to a stable release.
New feature: migrations
There are two significant new features in this RC compared to the previous 4.0 alphas.
The first is support for
database migrations
. This isn’t a completely new implementation—it’s a slightly modified port of the
sqlite-migrate
package I released a few years ago. I think that package has proved itself over time, so I’m now ready to bundle it with
sqlite-utils
directly.
Here’s what a set of migrations in a
migrations.py
file looks like:
from
sqlite_utils
import
Database
,
Migrations
migrations
=
Migrations
(
"creatures"
)
@
migrations
()
def
create_table
(
db
):
db
[
"creatures"
].
create
(
        {
"id"
:
int
,
"name"
:
str
,
"species"
:
str
},
pk
=
"id"
,
    )
@
migrations
()
def
add_weight
(
db
):
db
[
"creatures"
].
add_column
(
"weight"
,
float
)
This defines a set of two migrations, one creating the
creatures
table and another adding a column to it.
You can then run those migrations either using Python:
db
=
Database
(
"creatures.db"
)
migrations
.
apply
(
db
)
Or with the command-line
migrate
command:
sqlite-utils migrate creatures.db migrations.py
The system is deliberately small: it doesn’t provide reverse migrations, so any mistakes you make should be fixed by deploying a fresh migration to undo them.
Its predecessor has been used by
LLM
and various other projects for several years, so I’m confident that the design is stable and works well.
The new migrations feature
is documented here
.
New feature: db.atomic() transactions
This feature is a lot less exercised than migrations, so it deserves more attention from testers.
Previously,
sqlite-utils
mostly left transaction management up to its users, via a
with db.conn:
construct that reused the
sqlite3
mechanism directly.
SQLite supports nested transactions in the form of savepoints, so I wanted an abstraction that could make those as easy to use as possible.
I borrowed the terminology “atomic” from Django and Peewee. Here’s what the new API looks like:
with
db
.
atomic
():
db
.
table
(
"dogs"
).
insert
({
"id"
:
1
,
"name"
:
"Cleo"
},
pk
=
"id"
)
try
:
with
db
.
atomic
():
db
.
table
(
"dogs"
).
insert
({
"id"
:
2
,
"name"
:
"Pancakes"
})
raise
ValueError
(
"skip this one"
)
except
ValueError
:
pass
db
.
table
(
"dogs"
).
insert
({
"id"
:
3
,
"name"
:
"Marnie"
})
More details
in the documentation
.
Backwards incompatible changes
The backwards incompatible changes in v4 were described in the alpha release notes. For
4.0a0
:
Upsert operations now use SQLite’s
INSERT ... ON CONFLICT SET
syntax on all SQLite versions later than 3.23.1. This is a very slight breaking change for apps that depend on the previous
INSERT OR IGNORE
followed by
UPDATE
behavior. (
#652
)
Python library users can opt-in to the previous implementation by passing
use_old_upsert=True
to the
Database()
constructor, see
Alternative upserts using INSERT OR IGNORE
.
Dropped support for Python 3.8, added support for Python 3.13. (
#646
)
sqlite-utils tui
is now provided by the
sqlite-utils-tui
plugin. (
#648
)
Test suite now also runs against SQLite 3.23.1, the last version (from 2018-04-10) before the new
INSERT ... ON CONFLICT SET
syntax was added. (
#654
)
And for
4.0a1
:
Breaking change
: The
db.table(table_name)
method now only works with tables. To access a SQL view use
db.view(view_name)
instead. (
#657
)
The
table.insert_all()
and
table.upsert_all()
methods can now accept an iterator of lists or tuples as an alternative to dictionaries. The first item should be a list/tuple of column names. See
Inserting data from a list or tuple iterator
for details. (
#672
)
Breaking change
: The default floating point column type has been changed from
FLOAT
to
REAL
, which is the correct SQLite type for floating point values. This affects auto-detected columns when inserting data. (
#645
)
Now uses
pyproject.toml
in place of
setup.py
for packaging. (
#675
)
Tables in the Python API now do a much better job of remembering the primary key and other schema details from when they were first created. (
#655
)
Breaking change
: The
table.convert()
and
sqlite-utils convert
mechanisms no longer skip values that evaluate to
False
. Previously the
--skip-false
option was needed, this has been removed. (
#542
)
Breaking change
: Tables created by this library now wrap table and column names in
"double-quotes"
in the schema. Previously they would use
[square-braces]
. (
#677
)
The
--functions
CLI argument now accepts a path to a Python file in addition to accepting a string full of Python code. It can also now be specified multiple times. (
#659
)
Breaking change:
Type detection is now the default behavior for the
insert
and
upsert
CLI commands when importing CSV or TSV data. Previously all columns were treated as
TEXT
unless the
--detect-types
flag was passed. Use the new
--no-detect-types
flag to restore the old behavior. The
SQLITE_UTILS_DETECT_TYPES
environment variable has been removed. (
#679
)
Try it out
You can install the new RC like this:
pip install sqlite-utils==4.0rc1
Or try the CLI version directly with
uvx
like this:
uvx --with sqlite-utils==4.0rc1 sqlite-utils --help
Come chat with us about it in the
sqlite-utils Discord channel
, or file any bugs in
GitHub Issues
.
