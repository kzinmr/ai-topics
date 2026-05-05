---
title: "MySQL Backups Done Easily"
url: "https://boyter.org/2010/08/mysql-backups-done-easily/"
fetched_at: 2026-05-05T07:02:07.903718+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# MySQL Backups Done Easily

Source: https://boyter.org/2010/08/mysql-backups-done-easily/

One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases.The first answer is usually use mysqldump. This is all fine and good, till you start to want to dump multiple databases. You can do this all in one like using the –all-databases option however this makes restoring a single database an issue, since you have to parse out the parts you want which can be a pain.
So the question is, have you ever wanted to script mysqldump to dump each database into a seperate gziped file?
The below script is what I use for backing up multiple databases, and does the above.
# !/bin/sh
date=`date -I

for I in $(mysql -u root -pPASSWORD -e 'show databases' -s --skip-column-names);
do
   mysqldump -u root -pPASSWORD $I | gzip &gt; "$date-$I.sql.gz";
done
Its a simple bash script, which connects to MySQL, prints out all the databases and then uses each line as a separate argument for mysqldump. All the databases are saved in their own file and restoring a single database is easy.
