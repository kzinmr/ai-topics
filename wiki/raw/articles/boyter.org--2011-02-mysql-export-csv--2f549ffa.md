---
title: "MySQL Export to CSV"
url: "https://boyter.org/2011/02/mysql-export-csv/"
fetched_at: 2026-05-05T07:02:07.131737+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# MySQL Export to CSV

Source: https://boyter.org/2011/02/mysql-export-csv/

MySQL Export to CSV
2011/02/14
(49 words)
Ever needed to export data from MySQL into a CSV file? Its actually fairly simple,
SELECT * INTO OUTFILE '/tmp/name.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n'
FROM [tablename]
Certainly easier then writing a quick Python/Perl/PHP script to do the job.
