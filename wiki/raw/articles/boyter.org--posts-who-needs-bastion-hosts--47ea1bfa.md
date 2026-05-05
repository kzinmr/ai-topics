---
title: "We don't need no stinking bastion host!"
url: "https://boyter.org/posts/who-needs-bastion-hosts/"
fetched_at: 2026-05-05T07:01:55.500443+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# We don't need no stinking bastion host!

Source: https://boyter.org/posts/who-needs-bastion-hosts/

So on occasion, I find myself wanting to run SQL against customer databases. Where this gets annoying is that because we are often in AWS using lambda I have no ability to connect to them. Occasionally im able to bully the friendly devops’ and security people to allow me access to a bastion host, which I can then connect to the SQL database.
However this is often a painful process if allowed at all, and so with permission I sometimes add a special route into the application allowing me to run arbitrary SQL as needed.
I thought this Go function worth keeping on my blog as something I can refer back to. Given a global database connection as
DB
function will take in any query, run it against the database, and return it in a formatted way which you can then display to the user. I tend to just return it as plain text from a protected route.
It’s not perfect, but good enough for those situations where you just want a small bit of information from the database. Note it has an explicit rollback to prevent any data loss, but I wouldn’t trust my life to that and you can of course still run queries that slow down the database. As such use with caution.
package
data
import
"database/sql"
// EvilSql run whatever you want... not to be used for anything really... its sql injectable, but useful
// since it rolls back the transaction at the end, its sort of limited in what can be done, so not quite as
// evil as you would expect
func
EvilSql
(
s
string
) (
string
,
error
) {
tx
:=
DB
.
Begin
()
rows
,
err
:=
tx
.
Raw
(
s
).
Rows
()
if
err
!=
nil
{
return
""
,
err
}
// Get column names
columns
,
err
:=
rows
.
Columns
()
if
err
!=
nil
{
return
""
,
err
}
// Make a slice for the values
values
:=
make([]
sql
.
RawBytes
, len(
columns
))
// rows.Scan wants '[]interface{}' as an argument, so we must copy the
// references into such a slice
// See <http://code.google.com/p/go-wiki/wiki/InterfaceSlice> for details
scanArgs
:=
make([]
interface
{}, len(
values
))
for
i
:=
range
values
{
scanArgs
[
i
] =
&
values
[
i
]
}
data
:=
""
// Fetch rows
for
rows
.
Next
() {
// get RawBytes from data
err
=
rows
.
Scan
(
scanArgs
...
)
if
err
!=
nil
{
return
""
,
err
}
// Now do something with the data.
// Here we just print each column as a string.
var
value
string
for
i
,
col
:=
range
values
{
// Here we can check if the value is nil (NULL value)
if
col
==
nil
{
value
=
"NULL"
}
else
{
value
= string(
col
)
}
data
+=
columns
[
i
]
+
": "
+
value
+
"\n"
}
data
+=
"-----------------------------------\n"
}
// remove this because if we don't commit we can leave it open for the most part
tx
.
Rollback
()
return
data
,
nil
}
