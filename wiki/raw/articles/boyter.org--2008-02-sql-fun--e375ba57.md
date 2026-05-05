---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2008/02/sql-fun/"
fetched_at: 2026-05-05T07:02:08.600258+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2008/02/sql-fun/

Well today while pondering things at lunch I was looking into the performance of SQL queries one stood out. That being the performance of getting random rows out of a database.
Most people who have a basic understanding of MySQL (the database I use at home because its easy to set up, though I am looking at Posgresql) would say oh, to get random rows you do this,
SELECT
*
FROM
`
table
`
ORDER
BY
rand()
LIMIT
0
,
5
Which isn’t very efficient. The reason for this is that behind the scenes the database loads the table into memory, assigns a random number to each row and then sorts on that number. For small stuff its not an issue. However run it on a database with 10,000 rows and it becomes quite slow.
So I was looking at this and ways to make it faster. One of the obvious ones is to do the following,
SELECT
*
FROM
`
table
`
WHERE
id
in
(randnum,randnum,randnum,randnum,randnum)
ORDER
BY
rand()
LIMIT
0
,
5
Where the randnum is a number between the beginning of the database and the maximum number. This however assumes you are incrementing the count between rows by one and that nothing has been deleted. Hardly an ideal or realistic situation.
So anyways I was thinking about how you could make it fast over a huge data set, have it all handled by the database. Anyways I think I came up with a solution,
SELECT
*
FROM
`
table
`
WHERE
rand()
>
0
.
99
ORDER
BY
rand()
Its quite elegant I think. The trick is to make the 0.99 number capture a small amount of the total rows. So for 4 million rows I was actually using 0.99995 which returned about 200 rows which is easy to sort.
Anyways I was trying it before over two databases I have sitting on my machine. The first has 500,000 records. Running a the first example over it took longer then I was willing to wait (so over 10 mins) before I restarted the SQL server. My faster version once the database was warmed up returned the results in less then 1 second. I then tried it on the database of 4,000,000 rows and it returned results in about 2.7 seconds. I played around with different numbers of returned results and it seems the time taken is in the random selection rather then the sorting.
Anyways thats kinda nerdy but I thought someone might find it interesting.
