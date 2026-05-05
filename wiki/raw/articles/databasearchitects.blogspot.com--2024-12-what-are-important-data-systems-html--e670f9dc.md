---
title: "What are important data systems problems, ignored by research?"
url: "https://databasearchitects.blogspot.com/2024/12/what-are-important-data-systems.html"
fetched_at: 2026-05-05T07:01:27.645466+00:00
source: "Database Architects"
tags: [blog, raw]
---

# What are important data systems problems, ignored by research?

Source: https://databasearchitects.blogspot.com/2024/12/what-are-important-data-systems.html

In November, I had the pleasure of attending the
Dutch-Belgian DataBase Day
, where I moderated a panel on practical challenges often overlooked in database research. Our distinguished panelists included Allison Lee (founding engineer at Snowflake), Andy Pavlo (professor at CMU), and Hannes Mühleisen (co-creator of DuckDB and researcher at CWI), with attendees contributing to the discussion and sharing their perspectives. In this post, I'll attempt to summarize the discussion in the hope that it inspires young (and young-at-heart) researchers to tackle these challenges. Additionally, I'll link to some paper that can serve as motivation and starting points for research in these areas.
One significant yet understudied problem raised by multiple panellists is the handling of variable-length strings. Any analysis of real-world analytical queries reveals that strings are
ubiquitous
. For instance,
Amazon Redshift recently reported
that around 50% of all columns are strings. Since strings are typically larger than numeric data, this implies that strings are a substantial majority of real-world data. Dealing with strings presents two major challenges. First, query processing is often slow due to the variable size of strings and the (time and space) overhead of dynamic allocation. Second, surprisingly little research has been dedicated to efficient database-specific string compression. Given the importance of strings on real-world query performance and storage consumption, it is surprising how little research there is on the topic (there
are
some
exceptions
).
Allison highlighted a related issue: standard benchmarks, like TPC-H, are overly simplistic, which may partly explain why string processing is understudied. TPC-H queries involve little complex string processing and don't use strings as join or aggregation keys. Moreover, TPC-H strings have static upper bounds, allowing them to be treated as fixed-size objects. This sidesteps the real challenges of variable-size strings and their complex operations. More broadly, standard benchmarks fall short of reflecting real-world workloads, as they lack advanced relational operators (e.g., window functions, CTEs) and complex expressions. To drive meaningful progress, we likely need new, more realistic benchmarks. While the participants agreed on most points, one particularly interesting topic of discussion was distributed query processing. Allison pointed out that many query processing papers overlook distributed processing, making them hard to adopt in industrial systems. Hannes, however, argued that most user workloads can be handled on a single machine, which should be the primary focus of publicly funded research. My personal view is that both single-node and distributed processing are important, and there is ample room to address both challenges.
While database researchers often focus on database engine architectures, Andy argued that surrounding topics, such as
network connection handling
(e.g., database proxies), receive little attention despite their practical importance. Surprisingly, there is also limited research on scheduling database workloads and optimizing the network stack, even though
communication bottlenecks
frequently constrain efficient OLTP systems. Multi-statement stored procedures, though a potential solution, are not widely adopted and fail to address this issue in practice. I believe there are significant research opportunities in exploring how to better structure the interface between applications and database systems.
One striking fact about major database conferences, such as SIGMOD and VLDB, is how few papers address practical database system problems. From personal experience, I believe this presents a significant opportunity for researchers seeking both academic and real-world impact. Solutions to the problems discussed above (and many others) are likely to gain industry attention and be adopted by real database systems. Moreover, with the availability of open-source systems like DuckDB, DataFusion, LeanStore, and PostgreSQL, conducting systems research has become easier than ever.
