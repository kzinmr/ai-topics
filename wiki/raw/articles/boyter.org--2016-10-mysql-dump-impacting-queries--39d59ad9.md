---
title: "MySQL Dump Without Impacting Queries"
url: "https://boyter.org/2016/10/mysql-dump-impacting-queries/"
fetched_at: 2026-05-05T07:02:00.468202+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# MySQL Dump Without Impacting Queries

Source: https://boyter.org/2016/10/mysql-dump-impacting-queries/

MySQL Dump Without Impacting Queries
2016/10/26
(71 words)
Posted more for my personal use (I have to look it up every time) but here is how to run a mysqldump without impacting performance on the box. It sets the ionice and nice values to be as low as possible (but still run) and uses a single transaction and ups the max packet size for MySQL.
ionice -c2 -n7 nice -n19 mysqldump -u root -p DATABASE --single-transaction --max_allowed_packet=512M > FILENAME
