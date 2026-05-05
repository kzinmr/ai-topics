---
title: "MySQL Popularity Ranking Algorithm"
url: "https://boyter.org/2010/12/mysql-popularity-ranking-algorithm/"
fetched_at: 2026-05-05T07:02:07.155691+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# MySQL Popularity Ranking Algorithm

Source: https://boyter.org/2010/12/mysql-popularity-ranking-algorithm/

Calculating the popularity of a page or article is something that usually comes up as a list of requirements for any social website. Essentially you want to display the post popular items/articles in some form of list but have them weighted by how old they are. Thankfully its pretty easy to do MySQL.
((popularity-1)/power(((unix_timestamp(NOW())-unix_timestamp(datetime))/60)/60,1.8))
The above produces a number which you can then sort on. It is based on the
Hacker News algorithm
and works well for items which change hourly. By removing one of the /60 you should get something which ranks based on days rather then hours. A full example is listed below,
select *,
((table.popularity-1)/power(((unix_timestamp(NOW())-unix_timestamp(table.datetime))/60)/60,1.8)) as rank
 from table order by rank desc
As a live example I added it to the following website,
http://www.chunews.com/
which now uses the above ranking to display news items.
NB. This website is now offline as I have moved all my focus over to searchcode.com
