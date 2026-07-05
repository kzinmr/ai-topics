---
title: "sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)"
url: "https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything"
fetched_at: 2026-07-05T07:00:45.295947+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)

Source: https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything

sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)
5th July 2026
I wrote about the
sqlite-utils 4.0rc1
release a couple of weeks ago. Since we only have Claude Fable on our Max subscriptions for a few more days, I decided to see if it could help me get to a 4.0 stable release that I felt truly comfortable about, since I try to keep to
SemVer
and like my incompatible major versions to be as rare as possible.
I started with this prompt, in Claude Code for web on my iPhone:
Final review before shipping a stable 4.0 release - very important to spot any last minute things that would be a breaking change if we fix them later
Here’s
that initial report
it created for me. There were some
significant
problems that I hadn’t myself encountered yet—5 that Fable categorized as “release blockers”. Here’s the worst of the bunch:
1.
delete_where()
never commits and poisons the connection (data loss)
Table.delete_where()
(
sqlite_utils/db.py:2948
) runs its DELETE via a bare
self.db.execute()
with no
atomic()
wrapper — compare
Table.delete()
at
db.py:2944
, which wraps correctly. The connection is left
in_transaction=True
, so every
subsequent
atomic()
call takes the savepoint branch (
db.py:430-440
) and never commits either.
Reproduced end-to-end:
db
=
sqlite_utils
.
Database
(
"dw.db"
)
db
[
"t"
].
insert_all
([{
"id"
:
i
}
for
i
in
range
(
3
)],
pk
=
"id"
)
db
[
"t"
].
delete_where
(
"id = ?"
, [
0
])
# conn.in_transaction is now True
db
[
"t"
].
insert
({
"id"
:
50
})
db
[
"u"
].
insert
({
"a"
:
1
})
db
.
close
()
# Reopen: rows are [0, 1, 2] — the delete, row 50, AND table u are all gone.
That’s a really bad bug! Very glad I didn’t ship that, although at least it would have been a bug I could fix in a 4.0.1 point release, not a design flaw that would force a 5.0.
Over the course of 37 prompts, 34 commits and +1,321 -190 code changes over 30 separate files, we worked through the entire set of feedback in turn, making several other design improvements along the way.
A weird thing about coding agents is that harder tasks like this one actually provide
more
opportunity to do other things at the same time, since the agent sometimes needs 10-15 minutes to churn away on a new task. I went out to enjoy the Half Moon Bay 4th of July parade, occasionally checking in and prompting the next step for Fable from my phone.
Full details
in the PR
and
this shared transcript
. I switched to my laptop for the final review, which I conducted through GitHub’s PR interface.
The most significant changes relate to transaction handling, which was the signature new feature in
the earlier RC
. The new RC now includes
comprehensive documentation
on the new transaction model, the intro to which I’ll quote here in full:
Every method in this library that writes to the database—
insert()
,
upsert()
,
update()
,
delete()
,
delete_where()
,
transform()
,
create_table()
,
create_index()
,
enable_fts()
and the rest—runs inside its own transaction and commits it before returning. Your changes are saved to disk as soon as the method call finishes:
db
=
Database
(
"data.db"
)
db
.
table
(
"news"
).
insert
({
"headline"
:
"Dog wins award"
})
# The new row is already saved - no commit() required
The same applies to raw SQL executed with
db.execute()
—a write statement is committed as soon as it has run.
You never need to call
commit()
, and you do not need to close the database to persist your changes. There are exactly two situations where you need to think about transactions:
You want to group several write operations together, so they either all succeed or all fail—use
db.atomic()
.
You are
managing a transaction yourself
with
db.begin()
, in which case nothing is committed until you commit—the library will never commit a transaction you opened.
In reviewing Fable’s documentation—I find that reviewing the documentation edits first is an
excellent
way to build an initial understanding of what has changed—I spotted
this detail
:
db.atomic()
and the automatic per-method transactions are designed for connections in Python’s default transaction handling mode. Connections created with the Python 3.12+
sqlite3.connect(..., autocommit=True)
or
autocommit=False
options are not supported, because
commit()
and
rollback()
behave differently on those connections.
I admit I hadn’t thought about how
sqlite-utils
would react to the more recent
autocommit setting
, added in Python 3.12. It turns out “behave differently on those connections” equated to almost the entire test suite failing, so I worked with the model to
ensure that this difference
would not break how the library works.
And a final review by GPT-5.5
I used to think that the idea of having one model review the work of another was somewhat absurd—it felt weirdly superstitious. The problem is
it really does work
—I’ve started habitually having Anthropic’s best model review OpenAI’s work and vice versa, because I’ve had that turn up interesting results often enough to be valuable.
I prompted Codex Desktop and GPT-5.5 xhigh with the following:
Review changes since the last RC. Also confirm that the changelog is up-to-date.
Which was enough to turn up two issues worth investigating:
Findings
[P1]
sqlite_utils/db.py:663
db.query()
now rejects non-row statements only after calling
db.execute()
, and
sqlite_utils/db.py:705
auto-commits those writes first. So
db.query("update ...")
raises
ValueError
but the update is already committed. That is a surprising side effect for a method documented as “can only be used with SQL that returns rows.”
[P1]
sqlite_utils/db.py:672
INSERT ... RETURNING
through
db.query()
only commits after the returned generator is fully exhausted.
db.query("insert ... returning ...")
without iteration, or common
next(db.query(...))
usage, leaves the transaction open and the write can be rolled back on close. This contradicts
docs/changelog.rst:15
and
docs/python-api.rst:232
, which say it takes effect without iteration.
I pasted that into a fresh Fable session, which ran some experiments to confirm the problem:
Both findings were confirmed.
db.query()
called
self.execute()
first, which auto-commits writes, and only then checked
cursor.description
— so
db.query("update ...")
committed the update before raising
ValueError
. And the
INSERT ... RETURNING
commit lived at the end of the returned generator, so it never fired unless you exhausted the iterator —
next(db.query(...))
or an un-iterated call left the transaction open, contradicting what the changelog and docs promise.
Here’s
the PR
with the fix, and the
full Claude Code transcript
. Reviewing this code helped me build a better mental model of the edge cases of SQLite transaction semantics!
For an estimated (unsubsidized) cost of $149.25
I upgraded to the Claude Max $200/month plan (I was previously on $100/month) to increase my Fable allowance for the remaining time until
the July 7th Fablepocalypse
, when even Claude Max subscribers will have to pay full API cost for the model.
I was curious as to how much this would have cost me if I had been paying those costs directly. At first I thought those numbers weren’t available to me since I had run the work remotely using Claude Code for web, and then I realized I could run
AgentsView
inside that existing session to get that cost estimate!
Run "uvx agentsview --help"​ and then use that tool to calculate the cost of this session
Claude figured out how to use the
session list --include-children
command and came out with the following:
Transcript
Model
Cost
Main session
claude-fable-5
$141.02
API-surface sweep agent
claude-fable-5
$2.40
Transactions/atomic review agent
claude-fable-5
$2.39
Post-rc1 commits review agent
claude-fable-5
$1.72
Migrations review agent
claude-fable-5
$1.40
Prompt-counting agent
claude-opus-4-8
$0.32
Total
$149.25
I’m very glad I’m on that subscription! I really should have
followed my own advice
and leaned more heavily into subagents with cheaper models.
Here’s what
claude.ai/settings/usage
is showing me right now:
I have several other major Fable-driven projects on the go right now as well, with the goal of hitting 100% on that Fable bar just in time for the price increase.
The full release notes for sqlite-utils 4.0rc2
Here are
the full release notes
for the RC. I had Fable add these to an “Unreleased” section of the changelog as each change landed, reviewing them as it went. This has the neat side effect that
the commit history of the changelog
acts as a concise summary of each of the changes that went into the release.
In the past I’ve had a policy of writing release notes by hand, but honestly these are better than I would have created myself. Release notes are a great example of writing that I’m OK to outsource to agents because they need to be boring, predictable and accurate.
Breaking changes:
Write statements executed with
db.execute()
are now committed automatically, unless a transaction is already open in which case they join it. Previously they opened an implicit transaction that stayed open until something committed it—writes appeared to work when read on the same connection but were silently rolled back when the connection closed. Code that relied on rolling back uncommitted
db.execute()
writes should use the new
db.begin()
method to open an explicit transaction first. The transaction model is documented in full at
Transactions and saving your changes
.
db.query()
now executes its SQL as soon as it is called, rather than waiting until the returned generator is first iterated. Rows are still fetched lazily during iteration. SQL errors are now raised at the call site, statements such as
INSERT ... RETURNING
are executed and committed immediately without needing to iterate over their results, and passing a statement that returns no rows—previously a silent no-op—now raises a
ValueError
recommending
db.execute()
instead. A statement rejected this way is rolled back before the error is raised, so it has no effect on the database.
Python API validation errors now raise
ValueError
instead of
AssertionError
. Previously invalid arguments—such as
create_table()
with no columns,
transform()
on a table that does not exist, or passing both
ignore=True
and
replace=True
—were rejected using bare
assert
statements, which are silently skipped when Python runs with the
-O
flag. Code that caught
AssertionError
for these cases should catch
ValueError
instead.
table.upsert()
and
table.upsert_all()
now raise
PrimaryKeyRequired
if a record is missing a value for any primary key column, or has a value of
None
for one. Previously such records—which can never match an existing row—were quietly inserted as brand new rows, or triggered a confusing
KeyError
after the insert had already taken place.
db.enable_wal()
and
db.disable_wal()
now raise a
sqlite_utils.db.TransactionError
if called while a transaction is open. Previously they would silently commit the open transaction as a side effect of changing the journal mode, breaking the rollback guarantee of
db.atomic()
and of user-managed transactions.
The
View
class no longer has an
enable_fts()
method. It existed only to raise
NotImplementedError
, since full-text search is not supported for views—calling it now raises
AttributeError
instead, and the method no longer appears in the API reference. The
sqlite-utils enable-fts
command shows a clean error when pointed at a view.
The no-op
-d/--detect-types
flag has been removed from the
insert
and
upsert
commands. Type detection has been the default for CSV/TSV data since 4.0a1, so the flag did nothing—invocations using it should simply drop it.
--no-detect-types
remains available to disable detection.
Database()
now raises a
sqlite_utils.db.TransactionError
if passed a connection created with the Python 3.12+
sqlite3.connect(..., autocommit=True)
or
autocommit=False
options.
commit()
and
rollback()
behave differently on those connections, which previously caused every write made by the library to be silently discarded when the connection closed.
Everything else:
Fixed a bug where
table.delete_where()
,
table.optimize()
and
table.rebuild_fts()
did not commit their changes, leaving the connection inside an open transaction. Their work—and any subsequent writes—could then be silently rolled back when the connection was closed. All three now use
db.atomic()
, consistent with the other write methods.
The
sqlite-utils drop-table
command now refuses to drop a view, and
drop-view
refuses to drop a table. Previously each would silently drop the wrong type of object if the name matched. Both now exit with an error suggesting the correct command to use.
Migrations applied by the new
migrations system
now run inside a transaction, together with the record of the migration having been applied. If a migration raises an exception its changes are rolled back and it stays pending, so it can be safely re-applied after the error is fixed. Migrations that cannot run inside a transaction, such as those executing
VACUUM
, can opt out using
@migrations(transactional=False)
—see
Migrations and transactions
.
table.upsert()
and
table.upsert_all()
now detect the primary key or compound primary key of an existing table, so the
pk=
argument is no longer required when upserting into a table that already has a primary key.
db.table(table_name).insert({})
can now be used to insert a row consisting entirely of default values into an existing table, using
INSERT INTO ... DEFAULT VALUES
. (
#759
)
Improvements to the
sqlite-utils migrate
command:
--stop-before
values that do not match any known migration are now an error instead of being silently ignored,
--stop-before
now works correctly with migration files that still use the older
sqlite_migrate.Migrations
class, and
--list
is now a read-only operation that no longer creates the database file or the migrations tracking table.
migrations.applied()
now returns migrations in the order they were applied.
New
db.begin()
,
db.commit()
and
db.rollback()
methods for taking manual control of transactions, as an alternative to the
db.atomic()
context manager.
New documentation:
Transactions and saving your changes
describes how transactions work and when changes are committed, and a new
Upgrading
page details the changes needed to move between major versions.
