---
title: "Moving a MySQL/MariaDB database between servers using SSH"
url: "https://boyter.org/posts/move-mysql-database-between-servers/"
fetched_at: 2026-05-05T07:01:57.161354+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Moving a MySQL/MariaDB database between servers using SSH

Source: https://boyter.org/posts/move-mysql-database-between-servers/

I’m in the middle of moving searchcode.com’s database to another server while upgrading it. This means I need to copy it somehow. It’s especially difficult in this case because the server its sitting on does not have enough disk space to do my usual
mysqldump
then copy the file across using SCP.
I investigated splitting the database using
--where
clauses allowing me to get chunks of the database across, but that also means adding things like
--skip-create-options
and
--skip-add-drop-table
and I ended up having to redo it a few times, with dumps in between.
I started looking into doing the dump/import directly over mysql through a remote connection, which I am not a fan of because you have to start exposing your mysql instance to the internet, or setup a private network between the new and old severs. Neither are an appealing option.
A bit of searching around however and I discovered you can actually do it using SSH. This turned out to be a total game changer for me, hence writing this blog so I can keep reference to it.
The command is as follows,
mysqldump -u username -ppassword db-name | ssh user@remote mysql -u username -ppassword db-name
In my case I added some additional options in order to not smash the active MySQL instance, and deal with some of the larger content thats stored in it.
ionice -c2 -n7 nice -n19 mysqldump --single-transaction --max_allowed_packet=512M -u user -ppassword db-name | ssh user@remote mysql -u user -ppassword db-name
The result? It worked! Very well too. After a few hours the database was replicated and I am now able to finish the migration. All without exposing the database publicly. Bliss.
