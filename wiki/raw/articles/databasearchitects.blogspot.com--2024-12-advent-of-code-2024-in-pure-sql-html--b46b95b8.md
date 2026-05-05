---
title: "Advent of Code 2024 in pure SQL"
url: "https://databasearchitects.blogspot.com/2024/12/advent-of-code-2024-in-pure-sql.html"
fetched_at: 2026-05-05T07:01:27.597794+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Advent of Code 2024 in pure SQL

Source: https://databasearchitects.blogspot.com/2024/12/advent-of-code-2024-in-pure-sql.html

On a whim I decided to do this years
advent of code
in pure SQL. That was an interesting experience that I can recommend to everybody because it forces you to think differently about the problems. And I can report that
it was possible to solve every problem in pure SQL
.
In many cases SQL was actually surprisingly pleasant to use. The full solution for day 11 (including the puzzle input) is shown below:
1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
with
recursive
aoc10_input(i)
as
(
select
'
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'
),
lines(y,line)
as
(
select
0
, substr(i,
1
,
position
(E
'\n'
in
i)
-
1
), substr(i,
position
(E
'\n'
in
i)
+
1
)
from
aoc10_input
union
all
select
y
+
1
,substr(r,
1
,
position
(E
'\n'
in
r)
-
1
), substr(r,
position
(E
'\n'
in
r)
+
1
)
from
lines l(y,l,r)
where
position
(E
'\n'
in
r)
>
0
),
field(x,y,v)
as
(
select
x,y,ascii(substr(line,x::
integer
,
1
))
-
48
from
(
select
*
from
lines l
where
line
<>
''
) s,
lateral
generate_series(
1
,
length
(line))
g
(x)
),
paths(x,y,v,sx,sy)
as
(
select
x,y,
9
,x,y
from
field
where
v
=
9
union
all
select
f.x,f.y,f.v,p.sx,p.sy
from
field f, paths p
where
f.v
=
p.v
-
1
and
((f.x
=
p.x
and
abs
(f.y
-
p.y)
=
1
)
or
(f.y
=
p.y
and
abs
(f.x
-
p.x)
=
1
))
and
p.v
>
0
),
results
as
(
select
*
from
paths
where
v
=
0
),
part1
as
(
select
distinct
*
from
results)
select
(
select
count
(
*
)
from
part1)
as
part1, (
select
count
(
*
)
from
results)
as
part2
Parsing the input is a bit painful in SQL, but it is not too bad. Lines 1-10 are simply the puzzle input, lines 11-17 split the input into individual lines, and lines 18-21 construct a 2D array from the input. The algorithm itself is pretty short, lines 22-27 perform a recursive traversal of the field, and lines 28-39 extract the puzzle answer from the traversal results. For this kind of small scale traversals SQL works just fine.
Other days were more painful.
Day 16
for example does conceptually a very similar traversal of a field, and it computes the minimal traversal distance for each visited. Expressing that in SQL in easy, but evaluation is wasteful. When replacing the reference input with a real puzzle input the field is quite large, and the recursive query generates and preserves a lot of state, even though we only care about the last iteration of the recursive query. As a consequence you need a machine with over 200GB memory to execute that query, even though most of the computed tuples are irrelevant. We could fix that excessive memory consumption by using
iteration semantic
during recursion, but that is not widely supported by DBMSes. Umbra could do it, but Postgres and DuckDB cannot, thus I have not used it in my solutions.
And sometimes the programming model of recursive SQL clashes with what we want to do. On
day 23
we had to find the maximum clique in sparse graph. This can be computed reasonably well with the
Bron-Kerbosch algorithm
, but expressing that in recursive SQL is quite convoluted because the algorithm wants to maintain multiple sets, but recursive SQL only passes a single set along. It can be done, but the result
does not look pretty
.
This experiment has shown two things to me 1) it is possible to code quite complex algorithms in SQL, and often the SQL code is surprisingly pleasant, and 2) recursive SQL would be much more efficient and more pleasant to use if we had mechanisms to update state. There is
ongoing work
on supporting more complex control flow in recursion via a trampoline mechanisms, which is very useful, too, but we should definitively look into more complex state manipulation mechanisms. With just a bit extra functionality SQL would be quite a solid choice for running complex algorithms directly inside a database.
