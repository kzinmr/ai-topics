---
title: "How I store Enumerations in the Database"
url: "https://boyter.org/2011/03/store-enumerations-database/"
fetched_at: 2026-05-05T07:02:06.662945+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How I store Enumerations in the Database

Source: https://boyter.org/2011/03/store-enumerations-database/

One of the things I come across in databases now and then is a collection of single tables with a name like “MessageType”. You have a look in them and it turns out to have 6 or so rows with no foreign key relationships. Every single time it turns out to be someone had the idea to store an Enumeration (Enum) type in the database. Not a bad idea as it turns out since you can add sort options, soft deletes and the like, but the implementation of a single table for each one is flawed.
The following is how I deal with it (probably not ideal but works well for me). Essentially you define two tables in the database with names like Lookup and Value. Inside lookup you have something similar to the following.
+------+
    |id    |
    |lookup|
    |name  |
    +------+
This is basically a representation of the enum name. Id is usually an auto-incrementing id to make joins easy while lookup is the primary key. This is the definition of the enum, IE the name part in the database, or in our example “Message”.
Then you add the enum values to your Values table which looks similar to the below,
+---------+
    |id       |
    |lookupid |
    |name     |
    |sortorder|
    |deleted  |
    +---------+
Then through the power of a simple join you can get your enum values,
SELECT * FROM Value v INNER JOIN Lookup l ON l.id = v.lookupid WHERE l.name = '?';
Adding a simple index on lookupid and id ensures that any lookups are pretty fast (its a very simple join), and you are away. A single place to look for your enum values, the ability to add all sorts of extra metadata to your enums and no more creation of dozens of small tables in your database.
