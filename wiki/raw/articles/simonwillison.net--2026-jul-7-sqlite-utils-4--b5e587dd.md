---
title: "sqlite-utils 4.0, now with database schema migrations"
url: "https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything"
fetched_at: 2026-07-08T07:00:56.442603+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.0, now with database schema migrations

Source: https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything

sqlite-utils 4.0, now with database schema migrations
7th July 2026
This morning I released
sqlite-utils 4.0
, the 124th release of that project and the first major version bump since
3.0
in November 2020. In addition to some small but significant breaking changes (described in
this upgrade guide
), this version introduces three major features:
database migrations
,
nested transactions
(via a new
db.atomic()
method), and support for
compound foreign keys
.
Database schema migrations using sqlite-utils
Schema migrations define a sequence of changes to be made to a SQLite database, plus a mechanism for tracking which migrations have been applied and applying any that are found to be pending.
Migrations are defined in Python files using the
sqlite-utils Python library
, which includes a powerful
table.transform()
method providing
enhanced alter table capabilities
that are not supported by SQLite’s
ALTER TABLE
statement.
(
table.transform()
implements the pattern
recommended by the SQLite documentation
—create a new temporary table with the new schema, copy across the data, then drop the old table and rename the temporary one in its place.)
Here’s an example migration file which creates a table called
creatures
, adds an additional column to it in a second step, then changes the types of two of the columns in a third:
from
sqlite_utils
import
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
@
migrations
()
def
change_column_types
(
db
):
db
[
"creatures"
].
transform
(
types
=
{
"species"
:
int
,
"weight"
:
str
})
Save that as
migrations.py
and run it against a fresh database like this:
uvx sqlite-utils migrate data.db migrations.py
Then if you check the schema of that database:
uvx sqlite-utils schema data.db
You’ll see this SQL:
CREATE
TABLE
"
_sqlite_migrations
" (
"
id
"
INTEGER
PRIMARY KEY
,
"
migration_set
"
TEXT
,
"
name
"
TEXT
,
"
applied_at
"
TEXT
);
CREATE
UNIQUE INDEX
"
idx__sqlite_migrations_migration_set_name
"
ON
"
_sqlite_migrations
"
(
"
migration_set
"
,
"
name
"
);
CREATE
TABLE
"
creatures
" (
"
id
"
INTEGER
PRIMARY KEY
,
"
name
"
TEXT
,
"
species
"
INTEGER
,
"
weight
"
TEXT
);
The
_sqlite_migrations
table is used to keep track of which migration functions have been run. The
creatures
table above is the schema after all three migrations have been applied.
To see a list of migrations, both pending and applied, run this:
uvx sqlite-utils migrate data.db migrations.py --list
Output:
Migrations for: creatures

  Applied:
    create_table - 2026-07-07 17:58:41.360051+00:00
    add_weight - 2026-07-07 17:58:41.360608+00:00
    change_column_types - 2026-07-07 18:01:15.802000+00:00

  Pending:
    (none)
If you don’t specify a migrations file, the
sqlite-utils migrate data.db
command will scan the current directory and its subdirectories for files called
migrations.py
and apply any
Migrations()
instances it finds in them.
You can also execute migrations
from Python code
using the
migrations.apply(db)
method, which is useful for building tools that manage their own database schemas over multiple versions. My own
LLM tool
has been using a version of this pattern for several years now, as shown in
llm/embeddings_migrations.py
.
Prior art
My favorite implementation of this pattern remains
Django’s Migrations
, developed by Andrew Godwin based on his earlier project
South
. Fun fact: Andrew, Russ Keith-Magee, and I presented our competing approaches to schema migrations for Django on the
Schema Evolution panel
at the very first DjangoCon back in 2008! My attempt was called
dmigrations
, developed with a team at Global Radio in London.
Django’s migrations can be automatically generated from model definitions and include the ability to roll back to a previous version. The
sqlite-utils
approach is deliberately simpler: unlike Django,
sqlite-utils
encourages programmatic table creation rather than a model definition ORM, so there isn’t anything we can use to automatically generate migrations.
I decided to skip rollback, since in my experience it’s a feature that is rarely used. With a SQLite project, an easy way to achieve rollback is to create a copy of your database file before you apply the migrations!
Migrating from sqlite-migrate
The design of
sqlite-utils
migrations is three years old now—I had originally released it as a separate package called
sqlite-migrate
, which never quite graduated beyond a beta release.
I’ve used that package in enough places now that I’m confident in the design, so I’ve decided to promote it to a feature of
sqlite-utils
to make it available by default to all of the other tools in the growing sqlite-utils/Datasette/LLM ecosystem.
I made
one last release
of
sqlite-migrate
, which switches it to depend on
sqlite-utils>=4
and replaces the
__init__.py
file with the following:
from
sqlite_utils
import
Migrations
__all__
=
[
"Migrations"
]
Any existing project that depends on
sqlite-migrate
should continue to work without alterations.
Everything else in sqlite-utils 4.0
Here are the release notes for this version, with some inline annotations:
The 4.0 release includes some minor backwards-incompatible fixes (hence the major version number bump) and introduces three major new features:
I think of migrations as the signature new feature, hence this blog post.
sqlite-utils
has long had a confused relationship with database transactions, partly because when I started designing the library back in 2018 I didn’t yet have a great feel for how those worked in SQLite itself.
Adding migrations to the core library made me determined to finally crack this nut, since transactions make migration systems a whole lot safer and easier to reason about.
I ended up building this around a
db.atomic()
context manager which looks like this:
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
SQLite supports
Savepoints
, and as a result
db.atomic()
can be nested to carry out transactions inside of transactions. It’s pretty neat!
This came about when I asked a coding agent to review all open issues and PRs for things that should be included in a 4.0 release since they would represent breaking changes if I added them later, and it correctly identified that compound foreign keys were exactly that kind of feature.
I started with a breaking change to the
table.foreign_keys
introspection method, and then decided to see if Claude Fable 5 could handle the more fiddly job of integrating compound foreign key
creation
into the library. The API design it helped create felt
exactly right to me
—consistent with how the rest of the library worked already.
Other notable changes include:
Upserts now use SQLite’s
INSERT ... ON CONFLICT ... DO UPDATE SET
syntax, detect existing table primary keys automatically and reject records that are missing required primary key values. (
#652
)
This was the change that first pushed me to consider a breaking-change 4.0 version bump. I built this to help support
sqlite-chronicle
, which uses triggers to keep track of rows in a table that have been inserted, updated or deleted.
db.query()
now executes immediately and rejects statements that do not return rows; use
db.execute()
for writes and DDL.
Probably the
most disruptive breaking change
—I’ve had to update a few places in my own code to switch from
db.query()
to
db.execute()
as a result.
CSV and TSV imports now detect column types by default, while inserts into existing tables preserve those tables’ column types. (
#679
)
The
sqlite-utils insert data.db creatures creatures.csv --detect-types
flag was a later addition to allow column types (text, integer, real) to be automatically detected based on the data in a CSV. It should be the default, and releasing a 4.0 means I can make it so.
table.extract()
and
extracts=
no longer create lookup table records for all-
null
values. (
#186
)
The oldest issue addressed by this release—the underlying bug was opened (by me) in October 2020.
See
Upgrading from 3.x to 4.0
for details on backwards-incompatible changes.
The detailed release notes for the features and fixes shipped during the 4.0 pre-release cycle are available in
4.0a0
,
4.0a1
,
4.0rc1
,
4.0rc2
,
4.0rc3
and
4.0rc4
.
The upgrade guide was entirely written by Claude Fable 5, Claude Opus 4.8 and GPT-5.5. The same is true of the release notes.
This is the kind of documentation I’ve slowly become comfortable outsourcing to the robots. It doesn’t need to convince people of anything, or express any opinions—its job is to be as accurate and detailed as possible. I’ve reviewed the release notes closely and can confirm they are accurate and comprehensive.
Claude Fable 5 helped a lot
I released the first alpha of sqlite-utils 4.0
over a year ago
. I’ve been dragging my heels on the stable release because of the amount of work it would take to track down and clean up the many other minor design flaws that a major version number allowed me to take on.
Assistance from Claude Fable 5 (and to a lesser extent Opus 4.8 and GPT-5.5) gave me just the boost I needed to overcome inertia and make the most of the time I could afford to spend on this library.
Fable has
really good taste
in API design, and is
relentlessly proactive
if you give it a more open goal. My most successful prompt was a review task that I issued against what I thought was the last release candidate:
review the changes on main since the last tagged 3.x release - I am about to ship them as sqlite-utils 4.0, a stable version that promises no backwards-incompatible fixes for a very long time.
review the changelog and upgrade guide, and write yourself scratch scripts to try out all of the new features in v4 - save those scripts but don't commit them
I tried this with GPT-5.5 xhigh in Codex Desktop and Fable 5 in Claude Code.
GPT-5.5
wrote 5 Python scripts
and didn’t turn up anything particularly interesting—its
final report is here
.
Fable 5
wrote 12 scripts
, identified 4 release blockers and 10 additional issues
in its report
, and built a neat
combined repro script
, which, when run, output the following:
=== 1. Failed db.execute() write leaves an implicit transaction open ===
  in_transaction after failed write: True
  BUG: table 'other' silently lost when connection closed

=== 2. Leading ';' bypasses the query() first-token scanner ===
  BUG: raised OperationalError: no such savepoint: sqlite_utils_query
  BUG: row persisted despite rollback (count=1)

=== 3. Rejected write PRAGMA via query() still takes effect ===
  BUG: user_version=5 after 'rejected' statement (docs say no effect)

=== 4. Implicit compound FK resolves pk columns in table order, not PK order ===
  BUG: other_columns reported as ('b', 'a'), should be ('a', 'b')
  BUG: transform of valid data raised IntegrityError: FOREIGN KEY constraint failed

=== 5. ForeignKey (now a dataclass) is no longer hashable ===
  BUG: cannot use 'sqlite_utils.db.ForeignKey' as a set element (unhashable type: 'ForeignKey')

=== 6. Mixed ForeignKey objects and tuples in foreign_keys= rejected ===
  BUG: foreign_keys= should be a list of tuples

=== 7. insert --csv into an EXISTING table transforms its column types ===
  BUG: existing zip '01234' is now 1234 (column type: int)

=== 8. insert(pk=, alter=True) regression: InvalidColumns before alter runs ===
  BUG: InvalidColumns: Invalid primary key column ['id'] for table t with columns ['a']

=== 9. migrate --stop-before an already-applied migration applies everything ===
  BUG: m2 was applied despite --stop-before m1 (m1 already applied)

=== 10. ensure_autocommit_on() silently commits an open transaction ===
  BUG: row survived rollback (count=1) - transaction was committed
I found myself agreeing with almost all of them. Here’s
the PR with 16 commits
where we worked through them in turn.
There’s no doubt in my mind that sqlite-utils 4.0 is a significantly higher-quality release than if I had built it without the assistance of the latest frontier models.
