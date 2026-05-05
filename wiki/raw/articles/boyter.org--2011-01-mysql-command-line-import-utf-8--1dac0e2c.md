---
title: "MySQL Command Line Import UTF-8"
url: "https://boyter.org/2011/01/mysql-command-line-import-utf-8/"
fetched_at: 2026-05-05T07:02:07.132249+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# MySQL Command Line Import UTF-8

Source: https://boyter.org/2011/01/mysql-command-line-import-utf-8/

MySQL Command Line Import UTF-8
2011/01/27
(94 words)
Ever wanted to command line import some data into MySQL and keep the encoding type? Turns out its not that difficult. Just a simple command line option. That said I have to look it up all the time.
mysql -u USERNAME  -pPASSWORD --default_character_set utf8  DATABASE > file.sql
That will import things across with the correct encoding type. I think personally that the face that MySQL fails to throw an error or even raise a warning when it encounters these sort of issues is wrong but where you have no choice the above fixes problems.
