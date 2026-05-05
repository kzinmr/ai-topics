---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2009/03/linq/"
fetched_at: 2026-05-05T07:02:08.421345+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2009/03/linq/

Thought while my code was compiling and being tested I would throw up some thoughts about it. For those who don’t know you should probably go and read something else, since what follows is going to be pretty technical.
So LINQ to SQL. At first I was totally opposed to it. The idea of taking a language that most developers know (SQL) and morphing it into something that .NET can use and slightly resembles SQL didn’t really appeal to me. Since I was forced to use it (unless you use entity framework you cant write your own SQL against the database it as far as I can tell). So I didn’t like it. Then I had to take some queries I had and write them against a bunch of criteria for a simple search program. It was at this point I saw the light. Dynamic SQL. Yes im sure anyone who has written any sort of web application against a database will come come up with ssomething like the following,
$query
=
"select * from table "
;
if
(
advancedSearch
) {
if
($firstname
!=
null
)
query
+=
"where firstname = "
+
$firstname
if
($lastname
!=
null
)
query
+=
" and lastname = "
+
$lastname
}
Which frankly is ugly, had to debug, hard to modify. This is where LINQ to SQL totally rocks because you can do the following.
var
results
=
from m in table
select m;
if
(advancedSearch) {
if
(firstname
!=
null
)
results
=
from m in results
where m.
firstname
.
compareTo
(firstname)
==
0
select m;
if
(lastname
!=
null
)
results
=
from m in results
where m.
lastname
.
compareTo
(lastname)
==
0
select m
}
Now while it looks the same it has a few advantages.
It has compile time checking and provides intellisense.
There is no string concatenation. The number of times I have written a SQL statement like the first example and had it fail is quite high. This is prevented in this case because if it compiles at least it is going to run.
So yes I was happy with LINQ to SQL for a bit. I coded everything up, and all was well. However I then hit some stumbling blocks. Say you have two tables and have a one to many relationship between them. Rather then display the ID’s you want to display the name using the foreign key relationship. Well guess what, you have to change a lot of code and NOT just the linq to do this. See LINQ returns an entity class. If you decide to modify the fields it returns you need to dynamically construct a new type which isn’t the same as your entity. Consequently all your code breaks. If you are doing a lot of queries against this table and translations through a service layer well it just sucks.
So then I was unhappy at LINQ to SQL.
Then I needed to do something which is a pain to do in straight SQL, but I figured LINQ to SQL could do easily.
I had a two lists of ID’s which together were unique identifiers for a field. I wanted to run a query which would combine the ID’s and compare them to combined columns in the database. Something like the following,
var
results
=
from m in table
where ids.
Select
(n
=>
string.
Format
(
"{0}{1}"
,n.
id1
,n.
id2
).
ToList
().
Contains
(string.
Format
(
"{0}{1}"
,m.
id1
,m.
id2
)
select m;
And guess what… LINQ to SQL cant do this. It cant take the string format and convert it to an appropriate cast in SQL Server. It was at this point I was very unhappy with LINQ.
So anyway that’s my experience so far. I think that LINQ over lists is great, however in most cases you can just use a lambda expression and get the same results, for less effort and greater readability, but having a choice is still nice.
