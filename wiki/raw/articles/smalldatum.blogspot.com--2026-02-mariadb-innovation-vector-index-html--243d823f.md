---
title: "MariaDB innovation: vector index performance"
url: "https://smalldatum.blogspot.com/2026/02/mariadb-innovation-vector-index.html"
fetched_at: 2026-05-05T07:01:17.284875+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# MariaDB innovation: vector index performance

Source: https://smalldatum.blogspot.com/2026/02/mariadb-innovation-vector-index.html

Last year I shared many posts documenting MariaDB performance for vector search using
ann-benchmarks
. Performance was great in MariaDB 11 and this blog post explains that it is even better in MariaDB 12. This work was done by
Small Datum LLC
and sponsored by the MariaDB Foundation. My previous posts were published in
January
and
February
2025.
tl;dr
Vector search recall vs precision in MariaDB 12.3 is better than in MariaDB 11.8
Vector search recall vs precision in Maria 11.8 is better than in Postgres 18.2 with pgvector 0.8.1
The improvements in MariaDB 12.3 are more significant for larger datasets
MariaDB 12.3 has the best results because it use less CPU per query, This is confirmed by running vmstat in the background.
Benchmark
This time I used the dbpedia-openai-X-angular tests for X in 100k, 500k and 1000k.
For hardware I used a larger server (Hetzner ax162-s) with 48 cores, 128G of RAM, Ubuntu 22.04 and HW RAID 10 using 2 NVMe devices.
For databases I used:
MariaDB versions 11.8.5 and 12.3.0 with
this config file
. Both were compiled from source.
Postgres 18.2 with pgvector 0.8.1 with
this config file
. These were compiled from source. For Postgres tests were run with and without halfvec (float16).
I had ps and vmstat running during the benchmark and confirmed there weren't storage reads as the table and index were cached by MariaDB and Postgres.
The command lines to run the benchmark using my
helper scripts
are:
bash rall.batch.sh v1
dbpedia-openai-100k-angular c32r128
bash rall.batch.sh v1
dbpedia-openai-500k-angular c32r128
bash rall.batch.sh v1
dbpedia-openai-1000k-angular c32r128
Results: dbpedia-openai-100k-angular
Summary
MariaDB 12.3 has the best results
the difference between MariaDB 12.3 and 11.8 is smaller here than it is below for 500k and 1000k
Results: dbpedia-openai-500k-angular
Summary
MariaDB 12.3 has the best results
the difference between MariaDB 12.3 and 11.8 is larger here than above for 100k
Results: dbpedia-openai-1000k-angular
Summary
MariaDB 12.3 has the best results
the difference between MariaDB 12.3 and 11.8 is larger here than it is above for 100k and 500k
