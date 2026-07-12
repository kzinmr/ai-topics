---
title: "Prefer STRICT tables in SQLite"
url: "https://evanhahn.com/prefer-strict-tables-in-sqlite/"
fetched_at: 2026-07-12T07:01:17.491270+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# Prefer STRICT tables in SQLite

Source: https://evanhahn.com/prefer-strict-tables-in-sqlite/

Prefer STRICT tables in SQLite
In short: I prefer
strict tables
in SQLite because they avoid some datatype problems, such as putting text in number columns.
SQLite has a feature that I think is underrated:
strict tables
. Strict tables help enforce rigid typing, preventing mistakes like putting text into integer columns. I like them, and wrote this post to promote their use!
To make a strict table, add
STRICT
to the end of its definition. Like this:
-CREATE TABLE people (name TEXT);
+CREATE TABLE people (name TEXT) STRICT;
That’s it! But what does it do?
Advantages of strict tables
Broadly, strict tables help enforce rigid types, like other SQL engines do.
Prevents type mismatches on insert/update
Most significantly, strict tables keep you from inserting the wrong type into a column. For example, SQLite normally lets you put text into an
INTEGER
column, but not with strict tables.
-- Non-strict tables let you put anything anywhere.
CREATE
TABLE
people_nonstrict (age INTEGER);
INSERT
INTO
people_nonstrict (age)
VALUES
(
'garbage'
);
-- => works fine
-- Strict tables don't allow that, which I prefer.
CREATE
TABLE
people_strict (age INTEGER)
STRICT
;
INSERT
INTO
people_strict (age)
VALUES
(
'garbage'
);
-- => error: cannot store TEXT value in INTEGER column
Personally, I think it’s a mistake to try to put text in an integer column, or vice-versa.
I don’t want SQLite to let me make this error!
The same validation happens for
UPDATE
s, too.
Notably, if a value can be losslessly converted, it will still be accepted. For example, the string
'123'
can be perfectly converted to an integer, so it’s allowed. These two lines are equivalent, even for a strict table:
INSERT
INTO
people_strict (age)
VALUES
(
'123'
);
INSERT
INTO
people_strict (age)
VALUES
(
123
);
Prevents bogus column types on table creation
By default, you can create columns with bogus types. For example, all of these work even though they aren’t valid SQLite datatypes:
-- SQLite doesn't support these types, but this is all accepted.
CREATE
TABLE
tbl (name GARBAGE);
CREATE
TABLE
tbl (name DATETIME);
CREATE
TABLE
tbl (name JSON);
CREATE
TABLE
tbl (name UUID);
CREATE
TABLE
tbl (name BLOBB);
I think these aren’t what the developer intended. Some of these are typos, some of them are misunderstandings of
which datatypes SQLite supports
, and some are egregious mistakes.
Appending
STRICT
to any of these statements makes them error. In my opinion, that’s the correct behavior!
-- All of these give errors, which I prefer.
CREATE
TABLE
tbl (name GARBAGE)
STRICT
;
CREATE
TABLE
tbl (name DATETIME)
STRICT
;
CREATE
TABLE
tbl (name JSON)
STRICT
;
CREATE
TABLE
tbl (name UUID)
STRICT
;
CREATE
TABLE
tbl (name BLOBB)
STRICT
;
Only
INT
,
INTEGER
,
REAL
,
TEXT
,
BLOB
, and
ANY
are allowed.
Strict tables also require a column type, so you can’t do
CREATE TABLE tbl (name)
.
Still allows flexibility with
ANY
If you still need a column to be flexible, you can use the
ANY
datatype. As the name suggests, it allows anything—even in a strict table.
CREATE
TABLE
tbl (value
ANY
)
STRICT
;
-- All of these are valid because the column is ANY:
INSERT
INTO
tbl (value)
VALUES
(
123
);
INSERT
INTO
tbl (value)
VALUES
(
'text'
);
INSERT
INTO
tbl (value)
VALUES
(
12
.
34
);
INSERT
INTO
tbl (value)
VALUES
(X
'8647'
);
I haven’t found a use for this, but maybe you will!
Disadvantages of strict tables
I prefer strict tables but I must share a few cons. Not everything is better!
Can’t strict-ify an existing table
I think it’s best to use strictness from the start, but that’s not always possible.
Unfortunately, I don’t think there’s a way to
ALTER
a table to make it strict. I think you have to copy the data out of the non-strict table into the strict one. Something like this:
-- 1. Create a new strict table with the same schema
CREATE
TABLE
new_people (name TEXT)
STRICT
;
-- 2. Copy data (risky if types are wrong!)
INSERT
INTO
new_people
SELECT
*
FROM
people;
-- 3. Replace the old table
DROP
TABLE
people;
ALTER
TABLE
new_people
RENAME
TO
people;
Note that this could be tricky if the non-strict table has invalid data! For example, if the old data accidentally contains text in an integer column, you’ll get errors when doing the migration. You’ll probably need to clean the data or
cast it
.
You could make a rule for your codebase that all
new
tables are strict. That might be useful—at least
some
of your tables are valid! But it might also mean you have inconsistent validation across your tables, which might be more surprising than having weak validation on all tables. It’s up to you to decide whether this is a good fit for you.
The SQLite developers disagree with me
SQLite has a whole page called
“The Advantages Of Flexible Typing”
, where they argue that SQLite’s flexible behavior is good, actually.
I hesitate to wade into the controversy of static-versus-dynamic, but I disagree in most cases. I’ve personally encountered
many
bugs where an unexpected data type caused subtle headaches. I’d much rather these mistakes explode loudly. But it’s worth noting that SQLite’s developers seem not to share my preference for strict tables!
They point out a few good uses for flexible tables, such as “a pure key-value store” or “a place to store miscellaneous attributes” of different types. They also mention that you might
want
to keep the invalid data in some cases, like if you’re directly importing a messy CSV and don’t want to lose any data. I still prefer strict tables, but acknowledge there are some reasonable cases for non-strict ones.
(There’s also
at least one comment in the SQLite source that calls non-strict tables “legacy”
, but I trust that less than the official documentation.)
Only in SQLite 3.37.0+
SQLite introduced strict tables in
version 3.37.0
, released November 2021. If you’re on an older version of SQLite, you can’t use strict tables.
It’s worth noting that old versions of SQLite can’t read databases with strict tables. For example, if you create a strict table in the newest version of SQLite and then try to read that database in SQLite 3.36.0 (before strict tables were added), you’ll get an error—even if the strict table is already in the database.
Performance
maybe
?
Strict tables are theoretically slower because they have to do a little extra work. For example, they
check datatypes when doing an insert or update
.
But in practice, I don’t think this is an issue. I wrote a hacky script that inserted millions of rows into a table with 100 columns, and there was no obvious difference on multiple machines I tried. The file size on disk was also the same. I didn’t test this thoroughly, so maybe there’s something I missed, but I don’t think strict tables present a performance problem.
In fact, one might expect
better
performance because you won’t be accidentally mismatching SQLite’s column affinities. But again, I haven’t tested this.
Conclusion: I like strict tables!
Personally, I think the pros of strict tables outweigh the cons.
I generally prefer when types are rigidly enforced. It squashes a class of mistakes, and help enforce good data integrity. They’re not a panacea, but they’re usually easy to add and go a long way.
If there’s a SQLite feature
you
think is underrated,
please tell me
.
